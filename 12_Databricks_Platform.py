"""
================================================================================
                DATABRICKS - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive Databricks examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. DATABRICKS ARCHITECTURE & CONCEPTS
2. DATABRICKS NOTEBOOKS
3. DATABRICKS CLUSTERS
4. DELTA LAKE
5. DATABRICKS SQL
6. DATABRICKS WORKFLOWS (JOBS)
7. UNITY CATALOG
8. AUTO LOADER
9. STRUCTURED STREAMING
10. DATABRICKS UTILITIES (dbutils)
11. PERFORMANCE OPTIMIZATION
12. BEST PRACTICES
================================================================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from delta.tables import DeltaTable
import json

# ============================================================================
# 1. DATABRICKS ARCHITECTURE & CONCEPTS
# ============================================================================

"""
DATABRICKS ARCHITECTURE:

1. CONTROL PLANE (Managed by Databricks):
   - Web application UI
   - Cluster manager
   - Notebook server
   - Jobs scheduler
   - Security & access control

2. DATA PLANE (In your cloud account):
   - Compute clusters (VMs)
   - Storage (S3, ADLS, GCS)
   - Networking

KEY COMPONENTS:
- Workspace: Collaborative environment for notebooks, libraries, experiments
- Clusters: Compute resources (All-Purpose, Job, SQL Warehouse)
- Notebooks: Interactive development environment
- Jobs: Scheduled or triggered workflows
- Delta Lake: ACID-compliant storage layer
- Unity Catalog: Unified governance solution
- MLflow: Machine learning lifecycle management

CLUSTER TYPES:
1. All-Purpose Clusters: Interactive development, shared
2. Job Clusters: Automated jobs, terminated after job
3. SQL Warehouses: SQL analytics workloads

DATABRICKS RUNTIME:
- Standard Runtime: General-purpose Spark
- ML Runtime: Pre-installed ML libraries
- Photon Runtime: Optimized query engine
- GPU Runtime: GPU-accelerated workloads
"""

# ============================================================================
# 2. DATABRICKS NOTEBOOKS
# ============================================================================

"""
NOTEBOOK FEATURES:
- Multiple languages: Python, Scala, SQL, R
- Magic commands: %python, %scala, %sql, %md, %sh, %fs
- Widgets for parameterization
- Visualization capabilities
- Version control integration
- Collaborative editing
"""

# Magic Commands
# %python - Python code
# %sql - SQL queries
# %scala - Scala code
# %md - Markdown documentation
# %sh - Shell commands
# %fs - File system commands
# %run - Run another notebook

""" Python Cell """
# Regular Python code
df = spark.read.parquet("/mnt/data/sales")
df.show()

""" SQL Cell """
# %sql
# SELECT * FROM sales WHERE date >= '2024-01-01'

""" Markdown Cell """
# %md
# # Sales Analysis
# This notebook analyzes sales data from 2024

""" File System Commands """
# %fs ls /mnt/data/
# %fs head /mnt/data/sample.csv
# %fs rm -r /mnt/data/temp/

""" Run Another Notebook """
# %run ./helper_notebook

""" Widgets for Parameterization """
# Create widget
dbutils.widgets.text("start_date", "2024-01-01", "Start Date")
dbutils.widgets.dropdown("environment", "dev", ["dev", "staging", "prod"], "Environment")

# Get widget value
start_date = dbutils.widgets.get("start_date")
environment = dbutils.widgets.get("environment")

# Remove widget
dbutils.widgets.remove("start_date")

# Remove all widgets
dbutils.widgets.removeAll()

""" Display Data """
# Display DataFrame
display(df)

# Display with visualization
display(df.groupBy("category").agg(sum("sales").alias("total_sales")))

# ============================================================================
# 3. DATABRICKS CLUSTERS
# ============================================================================

"""
CLUSTER CONFIGURATION:

1. CLUSTER MODE:
   - Standard: General workloads
   - High Concurrency: Multiple users, optimized for concurrency
   - Single Node: Development, small datasets

2. DATABRICKS RUNTIME:
   - Runtime version (e.g., 13.3 LTS)
   - ML Runtime for machine learning
   - Photon for performance

3. AUTOSCALING:
   - Min workers and max workers
   - Automatic scale up/down based on load

4. AUTO TERMINATION:
   - Terminate after X minutes of inactivity
   - Save costs

5. INSTANCE TYPES:
   - Driver node type
   - Worker node type
   - Spot instances for cost savings
"""

""" Cluster Configuration Example (JSON) """
cluster_config = {
    "cluster_name": "data-engineering-cluster",
    "spark_version": "13.3.x-scala2.12",
    "node_type_id": "i3.xlarge",
    "driver_node_type_id": "i3.xlarge",
    "autoscale": {
        "min_workers": 2,
        "max_workers": 8
    },
    "autotermination_minutes": 30,
    "spark_conf": {
        "spark.databricks.delta.preview.enabled": "true",
        "spark.sql.adaptive.enabled": "true"
    },
    "custom_tags": {
        "project": "sales_analytics",
        "environment": "production"
    }
}

""" Get Cluster Information """
# Get current cluster ID
cluster_id = spark.conf.get("spark.databricks.clusterUsageTags.clusterId")

# Get Spark configuration
spark_conf = spark.sparkContext.getConf().getAll()
for conf in spark_conf:
    print(conf)

# ============================================================================
# 4. DELTA LAKE
# ============================================================================

"""
DELTA LAKE FEATURES:
- ACID transactions
- Time travel (data versioning)
- Schema enforcement and evolution
- Unified batch and streaming
- Audit history
- DML operations (UPDATE, DELETE, MERGE)
- Optimized file management
"""

""" Create Delta Table """
# From DataFrame
df = spark.read.csv("/mnt/data/sales.csv", header=True, inferSchema=True)
df.write.format("delta").mode("overwrite").save("/mnt/delta/sales")

# Create managed table
df.write.format("delta").mode("overwrite").saveAsTable("sales")

# Create external table
df.write.format("delta").mode("overwrite").option("path", "/mnt/delta/sales").saveAsTable("sales")

""" Read Delta Table """
# Read from path
df_delta = spark.read.format("delta").load("/mnt/delta/sales")

# Read from table
df_delta = spark.table("sales")

# Read specific version (Time Travel)
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load("/mnt/delta/sales")

# Read as of timestamp
df_ts = spark.read.format("delta").option("timestampAsOf", "2024-01-01").load("/mnt/delta/sales")

""" Update Data """
from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "/mnt/delta/sales")

# Update records
delta_table.update(
    condition = "category = 'Electronics'",
    set = {"discount": "discount * 1.1"}
)

""" Delete Data """
delta_table.delete("status = 'cancelled'")

""" Merge (Upsert) """
# Source data
updates = spark.read.csv("/mnt/data/updates.csv", header=True)

# Merge operation
delta_table.alias("target").merge(
    updates.alias("source"),
    "target.id = source.id"
).whenMatchedUpdate(
    set = {
        "name": "source.name",
        "price": "source.price",
        "updated_at": "current_timestamp()"
    }
).whenNotMatchedInsert(
    values = {
        "id": "source.id",
        "name": "source.name",
        "price": "source.price",
        "created_at": "current_timestamp()",
        "updated_at": "current_timestamp()"
    }
).execute()

""" Schema Evolution """
# Allow schema evolution
df.write.format("delta") \
    .mode("append") \
    .option("mergeSchema", "true") \
    .save("/mnt/delta/sales")

""" Optimize Delta Table """
# Compact small files
delta_table.optimize().executeCompaction()

# Z-ordering (for better query performance)
delta_table.optimize().executeZOrderBy("date", "category")

""" Vacuum (Remove old files) """
# Remove files older than 7 days (default retention)
delta_table.vacuum(168)  # hours

""" View History """
delta_table.history().show()

# Get detailed history
history_df = delta_table.history()
display(history_df)

""" Restore to Previous Version """
# Restore to version 5
delta_table.restoreToVersion(5)

# Restore to timestamp
delta_table.restoreToTimestamp("2024-01-01")

""" Clone Delta Table """
# Deep clone (copies data)
spark.sql("CREATE TABLE sales_backup DEEP CLONE sales")

# Shallow clone (references data)
spark.sql("CREATE TABLE sales_dev SHALLOW CLONE sales")

# ============================================================================
# 5. DATABRICKS SQL
# ============================================================================

""" SQL Queries in Notebooks """
# %sql
# CREATE OR REPLACE TABLE sales_summary AS
# SELECT 
#     date,
#     category,
#     SUM(amount) as total_sales,
#     COUNT(*) as num_transactions
# FROM sales
# WHERE date >= '2024-01-01'
# GROUP BY date, category

""" SQL in Python """
# Execute SQL and get DataFrame
result_df = spark.sql("""
    SELECT 
        category,
        SUM(amount) as total_sales
    FROM sales
    WHERE date >= '2024-01-01'
    GROUP BY category
    ORDER BY total_sales DESC
""")

result_df.show()

""" Create Database """
spark.sql("CREATE DATABASE IF NOT EXISTS sales_analytics")
spark.sql("USE sales_analytics")

""" Create Table """
spark.sql("""
    CREATE TABLE IF NOT EXISTS customer_metrics (
        customer_id INT,
        total_purchases DECIMAL(10,2),
        last_purchase_date DATE,
        customer_segment STRING
    )
    USING DELTA
    PARTITIONED BY (customer_segment)
""")

""" Views """
# Create view
spark.sql("""
    CREATE OR REPLACE VIEW high_value_customers AS
    SELECT *
    FROM customer_metrics
    WHERE total_purchases > 1000
""")

# Temporary view
df.createOrReplaceTempView("temp_sales")

# Global temporary view
df.createOrReplaceGlobalTempView("global_sales")

# ============================================================================
# 6. DATABRICKS WORKFLOWS (JOBS)
# ============================================================================

"""
DATABRICKS JOBS:
- Schedule notebooks, Python scripts, JARs
- Task dependencies (DAG)
- Retry logic
- Alerts and notifications
- Job clusters (cost-effective)
"""

""" Job Configuration Example (JSON) """
job_config = {
    "name": "Daily Sales ETL",
    "tasks": [
        {
            "task_key": "extract",
            "notebook_task": {
                "notebook_path": "/Workspace/ETL/extract",
                "base_parameters": {
                    "date": "{{job.start_time.iso_date}}"
                }
            },
            "job_cluster_key": "etl_cluster"
        },
        {
            "task_key": "transform",
            "depends_on": [{"task_key": "extract"}],
            "notebook_task": {
                "notebook_path": "/Workspace/ETL/transform"
            },
            "job_cluster_key": "etl_cluster"
        },
        {
            "task_key": "load",
            "depends_on": [{"task_key": "transform"}],
            "notebook_task": {
                "notebook_path": "/Workspace/ETL/load"
            },
            "job_cluster_key": "etl_cluster"
        }
    ],
    "job_clusters": [
        {
            "job_cluster_key": "etl_cluster",
            "new_cluster": {
                "spark_version": "13.3.x-scala2.12",
                "node_type_id": "i3.xlarge",
                "num_workers": 4,
                "autotermination_minutes": 30
            }
        }
    ],
    "schedule": {
        "quartz_cron_expression": "0 0 2 * * ?",
        "timezone_id": "UTC"
    },
    "email_notifications": {
        "on_failure": ["data-team@example.com"]
    },
    "max_concurrent_runs": 1
}

""" Exit Notebook with Value """
# Return value from notebook
dbutils.notebook.exit(json.dumps({"status": "success", "records": 1000}))

""" Run Notebook from Another Notebook """
# Run notebook and get result
result = dbutils.notebook.run(
    "/Workspace/ETL/process_data",
    timeout_seconds=3600,
    arguments={"date": "2024-01-01", "mode": "incremental"}
)

# Parse result
result_dict = json.loads(result)
print(f"Status: {result_dict['status']}")

# ============================================================================
# 7. UNITY CATALOG
# ============================================================================

"""
UNITY CATALOG:
- Unified governance for data and AI
- Fine-grained access control
- Data lineage
- Audit logging
- Data discovery
- Cross-cloud data sharing

HIERARCHY:
Metastore → Catalog → Schema → Table/View
"""

""" Create Catalog """
spark.sql("CREATE CATALOG IF NOT EXISTS production")
spark.sql("USE CATALOG production")

""" Create Schema """
spark.sql("CREATE SCHEMA IF NOT EXISTS sales_data")
spark.sql("USE sales_data")

""" Three-Level Namespace """
# catalog.schema.table
df = spark.table("production.sales_data.transactions")

# Fully qualified name
spark.sql("SELECT * FROM production.sales_data.transactions")

""" Grant Permissions """
# Grant SELECT on table
spark.sql("GRANT SELECT ON TABLE production.sales_data.transactions TO `data_analysts`")

# Grant USAGE on schema
spark.sql("GRANT USAGE ON SCHEMA production.sales_data TO `data_analysts`")

# Grant CREATE on catalog
spark.sql("GRANT CREATE ON CATALOG production TO `data_engineers`")

""" External Locations """
# Create external location
spark.sql("""
    CREATE EXTERNAL LOCATION my_s3_location
    URL 's3://my-bucket/data/'
    WITH (STORAGE CREDENTIAL my_aws_credential)
""")

# Create external table
spark.sql("""
    CREATE TABLE production.sales_data.external_sales
    LOCATION 's3://my-bucket/sales/'
""")

""" Data Lineage """
# Lineage is automatically captured
# View in Unity Catalog UI

# ============================================================================
# 8. AUTO LOADER
# ============================================================================

"""
AUTO LOADER:
- Incrementally process new files
- Schema inference and evolution
- Exactly-once processing
- Scalable file discovery
- Supports JSON, CSV, Parquet, Avro, ORC, text
"""

""" Basic Auto Loader """
df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/mnt/schema/sales") \
    .load("/mnt/landing/sales/")

# Write to Delta
df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/checkpoints/sales") \
    .trigger(availableNow=True) \
    .start("/mnt/delta/sales")

""" Auto Loader with Schema Inference """
df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "csv") \
    .option("cloudFiles.schemaLocation", "/mnt/schema/customers") \
    .option("cloudFiles.inferColumnTypes", "true") \
    .option("cloudFiles.schemaHints", "id INT, created_at TIMESTAMP") \
    .option("header", "true") \
    .load("/mnt/landing/customers/")

""" Auto Loader with Schema Evolution """
df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/mnt/schema/events") \
    .option("cloudFiles.schemaEvolutionMode", "addNewColumns") \
    .load("/mnt/landing/events/")

df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/checkpoints/events") \
    .option("mergeSchema", "true") \
    .trigger(processingTime="5 minutes") \
    .start("/mnt/delta/events")

""" Auto Loader with Transformations """
from pyspark.sql.functions import current_timestamp

df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/mnt/schema/orders") \
    .load("/mnt/landing/orders/")

# Apply transformations
transformed_df = df \
    .withColumn("ingestion_time", current_timestamp()) \
    .withColumn("year", year(col("order_date"))) \
    .withColumn("month", month(col("order_date")))

# Write with partitioning
transformed_df.writeStream \
    .format("delta") \
    .partitionBy("year", "month") \
    .option("checkpointLocation", "/mnt/checkpoints/orders") \
    .trigger(availableNow=True) \
    .start("/mnt/delta/orders")

# ============================================================================
# 9. STRUCTURED STREAMING
# ============================================================================

""" Read Stream from Delta """
df_stream = spark.readStream \
    .format("delta") \
    .load("/mnt/delta/events")

""" Streaming Aggregations """
# Windowed aggregation
windowed_counts = df_stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        window(col("timestamp"), "5 minutes"),
        col("event_type")
    ) \
    .count()

# Write stream
windowed_counts.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/mnt/checkpoints/windowed_counts") \
    .start("/mnt/delta/windowed_counts")

""" Stream-Stream Join """
stream1 = spark.readStream.format("delta").load("/mnt/delta/orders")
stream2 = spark.readStream.format("delta").load("/mnt/delta/shipments")

joined = stream1.join(
    stream2,
    expr("""
        orders.order_id = shipments.order_id AND
        shipments.timestamp >= orders.timestamp AND
        shipments.timestamp <= orders.timestamp + interval 1 hour
    """)
)

""" Streaming Deduplication """
deduplicated = df_stream \
    .withWatermark("timestamp", "1 hour") \
    .dropDuplicates(["id", "timestamp"])

""" Trigger Options """
# Process all available data once
# query.trigger(availableNow=True)

# Continuous processing
# query.trigger(continuous="1 second")

# Micro-batch with interval
# query.trigger(processingTime="5 minutes")

# Process once (for testing)
# query.trigger(once=True)

# ============================================================================
# 10. DATABRICKS UTILITIES (dbutils)
# ============================================================================

""" File System Operations """
# List files
files = dbutils.fs.ls("/mnt/data/")
for file in files:
    print(file.path, file.size)

# Copy file
dbutils.fs.cp("/mnt/source/file.csv", "/mnt/destination/file.csv")

# Move file
dbutils.fs.mv("/mnt/source/file.csv", "/mnt/destination/file.csv")

# Remove file/directory
dbutils.fs.rm("/mnt/data/temp/", recurse=True)

# Create directory
dbutils.fs.mkdirs("/mnt/data/new_folder/")

# Read file
content = dbutils.fs.head("/mnt/data/sample.txt", maxBytes=1000)

# Put content to file
dbutils.fs.put("/mnt/data/output.txt", "Hello, World!", overwrite=True)

""" Secrets Management """
# Get secret from scope
api_key = dbutils.secrets.get(scope="my_scope", key="api_key")
db_password = dbutils.secrets.get(scope="my_scope", key="db_password")

# List secret scopes
scopes = dbutils.secrets.listScopes()

# List secrets in scope
secrets = dbutils.secrets.list(scope="my_scope")

""" Notebook Workflows """
# Run another notebook
result = dbutils.notebook.run(
    "/Workspace/ETL/process",
    timeout_seconds=3600,
    arguments={"date": "2024-01-01"}
)

# Exit with value
dbutils.notebook.exit("Success")

""" Widgets """
# Create widgets
dbutils.widgets.text("environment", "dev")
dbutils.widgets.dropdown("region", "us-east-1", ["us-east-1", "us-west-2", "eu-west-1"])
dbutils.widgets.multiselect("categories", "Electronics", ["Electronics", "Clothing", "Food"])

# Get widget values
env = dbutils.widgets.get("environment")

# Remove widgets
dbutils.widgets.removeAll()

""" Library Management """
# Install library on cluster
dbutils.library.installPyPI("pandas", version="1.5.0")
dbutils.library.restartPython()

# ============================================================================
# 11. PERFORMANCE OPTIMIZATION
# ============================================================================

""" Adaptive Query Execution (AQE) """
# Enable AQE (enabled by default in Databricks Runtime 7.3+)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

""" Photon Engine """
# Photon is automatically used for SQL operations
# No code changes needed, just enable in cluster config

""" Caching """
# Cache DataFrame
df.cache()
df.count()  # Trigger caching

# Persist with storage level
df.persist()

# Unpersist
df.unpersist()

""" Broadcast Join """
from pyspark.sql.functions import broadcast

# Broadcast small table
result = large_df.join(broadcast(small_df), "key")

""" Partition Optimization """
# Repartition for better parallelism
df_repartitioned = df.repartition(100)

# Repartition by column
df_repartitioned = df.repartition("date")

# Coalesce (reduce partitions without shuffle)
df_coalesced = df.coalesce(10)

""" Z-Ordering (Delta Lake) """
# Optimize with Z-ordering
delta_table = DeltaTable.forPath(spark, "/mnt/delta/sales")
delta_table.optimize().executeZOrderBy("date", "customer_id")

""" Data Skipping """
# Delta Lake automatically uses data skipping
# Ensure proper partitioning and Z-ordering

""" Predicate Pushdown """
# Filter early
df_filtered = spark.read.parquet("/mnt/data/sales") \
    .filter(col("date") >= "2024-01-01")

""" Column Pruning """
# Select only needed columns
df_selected = spark.read.parquet("/mnt/data/sales") \
    .select("id", "amount", "date")

# ============================================================================
# 12. BEST PRACTICES
# ============================================================================

"""
DATABRICKS BEST PRACTICES:

1. CLUSTER MANAGEMENT:
   - Use job clusters for scheduled jobs (cost-effective)
   - Enable autoscaling for variable workloads
   - Set auto-termination to save costs
   - Use spot instances for non-critical workloads
   - Right-size clusters based on workload

2. DELTA LAKE:
   - Use Delta format for all tables
   - Run OPTIMIZE regularly
   - Use Z-ordering for frequently queried columns
   - Set appropriate VACUUM retention
   - Enable auto-optimize for write-heavy tables

3. DATA ORGANIZATION:
   - Partition by date or high-cardinality columns
   - Use appropriate file sizes (128MB-1GB)
   - Organize data in medallion architecture (Bronze/Silver/Gold)
   - Use Unity Catalog for governance

4. PERFORMANCE:
   - Enable Photon for SQL workloads
   - Use broadcast joins for small tables
   - Cache frequently accessed data
   - Use appropriate file formats (Parquet, Delta)
   - Optimize partition count (2-4x cores)

5. STREAMING:
   - Use Auto Loader for file ingestion
   - Set appropriate trigger intervals
   - Use checkpoints for fault tolerance
   - Monitor streaming metrics
   - Handle late data with watermarks

6. SECURITY:
   - Use Unity Catalog for access control
   - Store secrets in Databricks Secrets
   - Enable audit logging
   - Use service principals for automation
   - Implement row/column-level security

7. DEVELOPMENT:
   - Use version control (Repos)
   - Parameterize notebooks with widgets
   - Write modular, reusable code
   - Test notebooks before production
   - Document code and workflows

8. MONITORING:
   - Monitor job runs and failures
   - Set up alerts for critical jobs
   - Track cluster utilization
   - Monitor costs
   - Use Ganglia for cluster metrics

9. COST OPTIMIZATION:
   - Use job clusters instead of all-purpose
   - Enable autoscaling
   - Set auto-termination
   - Use spot instances
   - Right-size clusters
   - Clean up unused resources

10. DATA QUALITY:
    - Implement data validation
    - Use expectations (Great Expectations)
    - Monitor data freshness
    - Track data lineage
    - Implement error handling
"""

""" Medallion Architecture Example """
# Bronze Layer (Raw data)
bronze_df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/mnt/schema/bronze") \
    .load("/mnt/landing/raw/")

bronze_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/checkpoints/bronze") \
    .start("/mnt/delta/bronze/events")

# Silver Layer (Cleaned, validated)
silver_df = spark.readStream \
    .format("delta") \
    .load("/mnt/delta/bronze/events") \
    .filter(col("id").isNotNull()) \
    .dropDuplicates(["id"]) \
    .withColumn("processed_at", current_timestamp())

silver_df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/mnt/checkpoints/silver") \
    .start("/mnt/delta/silver/events")

# Gold Layer (Business-level aggregations)
gold_df = spark.read.format("delta").load("/mnt/delta/silver/events") \
    .groupBy("date", "event_type") \
    .agg(
        count("*").alias("event_count"),
        countDistinct("user_id").alias("unique_users")
    )

gold_df.write.format("delta").mode("overwrite").save("/mnt/delta/gold/event_summary")

"""
================================================================================
END OF DATABRICKS PLATFORM GUIDE
================================================================================
"""
