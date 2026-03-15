"""
================================================================================
                    PYSPARK - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive examples organized by topic for easy revision
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. SPARK SESSION & DATAFRAME BASICS
2. DATA READING & WRITING
3. DATA CLEANING & NULL HANDLING
4. TRANSFORMATIONS & COLUMN OPERATIONS
5. AGGREGATIONS & GROUP BY
6. WINDOW FUNCTIONS (RANK, ROW_NUMBER, DENSE_RANK, LAG, LEAD)
7. JOINS (BROADCAST, SHUFFLE, SORT-MERGE)
8. PERFORMANCE OPTIMIZATION (CACHE, PERSIST, PARTITIONING)
9. AWS INTEGRATION (S3, GLUE, DYNAMICFRAMES)
10. DELTA LAKE & INCREMENTAL LOADS
11. RDD OPERATIONS
12. DATA VALIDATION & QUALITY CHECKS
13. SPARK ARCHITECTURE CONCEPTS
================================================================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# ============================================================================
# 1. SPARK SESSION & DATAFRAME BASICS
# ============================================================================

""" Initialize Spark Session with Configurations """
spark = SparkSession.builder \
    .appName("DataEngineerInterview") \
    .config("spark.sql.shuffle.partitions", "200") \
    .config("spark.executor.memory", "4g") \
    .config("spark.driver.memory", "2g") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

""" Create DataFrame from Data """
data = [(1, "Alice", 85, "Math"), (2, "Bob", None, "Science"), (3, "Charlie", 78, "Math")]
columns = ["id", "name", "marks", "subject"]
df = spark.createDataFrame(data, columns)

# Display DataFrame
df.show()
df.printSchema()
df.describe().show()
df.count()

""" Define Schema Manually (Important for Production) """
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("marks", IntegerType(), True),
    StructField("subject", StringType(), True)
])

df = spark.createDataFrame(data, schema)

# ============================================================================
# 2. DATA READING & WRITING
# ============================================================================

""" Reading CSV """
# Method 1: Using format
df_csv = spark.read.format('csv') \
    .option('header', 'true') \
    .option('delimiter', ',') \
    .option('inferSchema', 'true') \
    .option('mode', 'PERMISSIVE') \
    .load('path/to/file.csv')

# Method 2: Direct method
df_csv = spark.read.csv('path/to/file.csv', header=True, inferSchema=True)

""" Reading JSON """
df_json = spark.read.json('path/to/file.json')
df_json_multiline = spark.read.option("multiline", "true").json('path/to/file.json')

""" Reading Parquet (Recommended for Big Data) """
df_parquet = spark.read.parquet('path/to/file.parquet')

""" Reading from S3 """
df_s3 = spark.read.parquet('s3://bucket-name/path/to/data/')
df_s3_csv = spark.read.csv('s3a://bucket-name/path/to/data.csv', header=True)

""" Reading from Database (JDBC) """
jdbc_url = "jdbc:postgresql://hostname:port/dbname"
connection_properties = {
    "user": "username",
    "password": "password",
    "driver": "org.postgresql.Driver"
}
df_jdbc = spark.read.jdbc(url=jdbc_url, table="table_name", properties=connection_properties)

""" Read Modes in Spark """
# PERMISSIVE (default): Sets corrupt records to null
# DROPMALFORMED: Drops corrupt records
# FAILFAST: Throws exception on corrupt records
df_permissive = spark.read.option("mode", "PERMISSIVE").csv("path/to/file.csv")

""" Writing Data """
# Write as Parquet (Columnar format - Best for Analytics)
df.write.mode('overwrite').parquet('path/to/output/')

# Write as CSV
df.write.mode('append').option('header', 'true').csv('path/to/output/')

# Partitioned Write (Important for Performance)
df.write.partitionBy('year', 'month').mode('overwrite').parquet('path/to/output/')

# Write to Database
df.write.jdbc(url=jdbc_url, table="target_table", mode="append", properties=connection_properties)

# Write to S3
df.write.parquet('s3://bucket-name/path/to/output/')

# ============================================================================
# 3. DATA CLEANING & NULL HANDLING
# ============================================================================

""" Handling Null Values - fillna() """
# Fill null values in specific columns
df_filled = df.fillna({"marks": 0, "name": "Unknown"})

# Fill with average (Common Interview Question)
average_marks = df.select(avg(col("marks"))).collect()[0][0]
df_filled = df.na.fill({"marks": average_marks})

# Fill with forward fill or backward fill (using window functions)
window_spec = Window.orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_filled = df.withColumn("marks_filled", last("marks", ignorenulls=True).over(window_spec))

""" Replacing Values """
# Replace specific values
df_replaced = df.replace(0, average_marks, subset=["marks"])
df_replaced = df.replace(["Math", "Science"], ["Mathematics", "Sciences"])

""" Drop Null Values """
# Drop rows with any null
df_clean = df.na.drop(how='any')

# Drop rows with all nulls
df_clean = df.na.drop(how='all')

# Drop rows where at least 2 non-null values are required
df_clean = df.na.drop(thresh=2)

# Drop nulls in specific columns
df_clean = df.na.drop(subset=['marks', 'name'])

""" Drop Duplicates """
df_no_duplicates = df.dropDuplicates()
df_no_duplicates = df.dropDuplicates(['id', 'name'])

# ============================================================================
# 4. TRANSFORMATIONS & COLUMN OPERATIONS
# ============================================================================

""" Select Columns """
df.select("name", "marks").show()
df.select(col("name"), col("marks")).show()
df.select(df.name, df.marks).show()

""" Add New Column """
df = df.withColumn("marks_doubled", col("marks") * 2)
df = df.withColumn("grade", when(col("marks") >= 80, "A")
                                .when(col("marks") >= 60, "B")
                                .otherwise("C"))

""" Rename Column """
df = df.withColumnRenamed("old_column", "new_column")

""" Drop Column """
df = df.drop("column_to_drop")

""" Cast Column Type """
df = df.withColumn("marks", col("marks").cast("double"))
df = df.withColumn("id", col("id").cast(IntegerType()))

""" Conditional Logic - when/otherwise """
df = df.withColumn("status", 
    when(col("marks") >= 80, "Excellent")
    .when(col("marks") >= 60, "Good")
    .when(col("marks") >= 40, "Average")
    .otherwise("Poor"))

""" Filter Rows """
df_filtered = df.filter(col("marks") > 70)
df_filtered = df.where(col("marks") > 70)
df_filtered = df.filter((col("marks") > 70) & (col("subject") == "Math"))

""" String Operations """
# Trim whitespace
df = df.withColumn("name", trim(col("name")))

# Upper/Lower case
df = df.withColumn("name_upper", upper(col("name")))
df = df.withColumn("name_lower", lower(col("name")))

# Substring
df = df.withColumn("first_char", substring(col("name"), 1, 1))

# Concatenate strings
df = df.withColumn("full_info", concat_ws(" - ", col("name"), col("subject")))

# Split strings
df = df.withColumn("name_parts", split(col("name"), " "))
df = df.withColumn("first_name", split(col("name"), " ")[0])

# Contains
df_filtered = df.filter(col("name").contains("Alice"))

# Regex replace
df = df.withColumn("phone_cleaned", regexp_replace(col("phone"), r"\D", ""))

# Regex extract
df = df.withColumn("area_code", regexp_extract(col("phone"), r"(\d{3})", 1))

""" Date Operations """
from pyspark.sql.functions import current_date, date_add, date_sub, datediff, months_between

df = df.withColumn("current_date", current_date())
df = df.withColumn("date_plus_7", date_add(col("date_column"), 7))
df = df.withColumn("date_minus_7", date_sub(col("date_column"), 7))
df = df.withColumn("days_diff", datediff(col("end_date"), col("start_date")))
df = df.withColumn("months_diff", months_between(col("end_date"), col("start_date")))

# Extract year, month, day
df = df.withColumn("year", year(col("date_column")))
df = df.withColumn("month", month(col("date_column")))
df = df.withColumn("day", dayofmonth(col("date_column")))

""" Array Operations """
# Explode array into rows
df_exploded = df.select(col("name"), explode(col("languages")).alias("language"))

# Array contains
df_filtered = df.filter(array_contains(col("languages"), "Python"))

# Array size
df = df.withColumn("num_languages", size(col("languages")))

""" Sort/Order By """
df_sorted = df.orderBy("marks")
df_sorted = df.orderBy(col("marks").desc())
df_sorted = df.orderBy(col("subject").asc(), col("marks").desc())

# ============================================================================
# 5. AGGREGATIONS & GROUP BY
# ============================================================================

""" Basic Aggregations """
df.agg(sum("marks"), avg("marks"), max("marks"), min("marks"), count("*")).show()

""" Group By """
df_grouped = df.groupBy("subject").agg(
    count("*").alias("student_count"),
    avg("marks").alias("avg_marks"),
    max("marks").alias("max_marks"),
    min("marks").alias("min_marks"),
    sum("marks").alias("total_marks")
)

""" Count Distinct """
df.agg(countDistinct("subject").alias("unique_subjects")).show()

""" Collect List/Set """
df_grouped = df.groupBy("subject").agg(
    collect_list("name").alias("students"),
    collect_set("name").alias("unique_students")
)

""" Pivot (Convert rows to columns) """
df_pivot = df.groupBy("name").pivot("subject").agg(sum("marks"))

""" Multiple Aggregations """
df_agg = df.groupBy("subject").agg(
    count("*").alias("count"),
    avg("marks").alias("avg_marks"),
    stddev("marks").alias("std_marks"),
    variance("marks").alias("var_marks")
)

# ============================================================================
# 6. WINDOW FUNCTIONS (VERY IMPORTANT FOR INTERVIEWS)
# ============================================================================

""" Window Specification """
window_spec = Window.partitionBy("subject").orderBy(col("marks").desc())

""" ROW_NUMBER - Assigns unique sequential number """
df = df.withColumn("row_num", row_number().over(window_spec))

""" RANK - Assigns rank with gaps """
df = df.withColumn("rank", rank().over(window_spec))

""" DENSE_RANK - Assigns rank without gaps """
df = df.withColumn("dense_rank", dense_rank().over(window_spec))

""" LAG - Access previous row value """
df = df.withColumn("previous_marks", lag("marks", 1).over(window_spec))

""" LEAD - Access next row value """
df = df.withColumn("next_marks", lead("marks", 1).over(window_spec))

""" Running Total """
window_running = Window.partitionBy("subject").orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df = df.withColumn("running_total", sum("marks").over(window_running))

""" Moving Average (Last 3 rows) """
window_moving = Window.partitionBy("subject").orderBy("id").rowsBetween(-2, 0)
df = df.withColumn("moving_avg", avg("marks").over(window_moving))

""" Cumulative Distribution """
df = df.withColumn("cume_dist", cume_dist().over(window_spec))

""" Percent Rank """
df = df.withColumn("percent_rank", percent_rank().over(window_spec))

""" NTILE - Divide into N buckets """
df = df.withColumn("quartile", ntile(4).over(window_spec))

""" Find Nth Highest Salary by Department (Common Interview Question) """
window_dept = Window.partitionBy("department").orderBy(col("salary").desc())
df_nth = df.withColumn("rank", dense_rank().over(window_dept)) \
           .filter(col("rank") == 2)  # 2nd highest

""" Find First and Last Value in Window """
df = df.withColumn("first_marks", first("marks").over(window_spec))
df = df.withColumn("last_marks", last("marks").over(window_spec))

# ============================================================================
# 7. JOINS (VERY IMPORTANT)
# ============================================================================

""" Inner Join """
df_joined = df1.join(df2, df1.id == df2.id, "inner")
df_joined = df1.join(df2, "id", "inner")  # When column names are same

""" Left Join """
df_joined = df1.join(df2, "id", "left")

""" Right Join """
df_joined = df1.join(df2, "id", "right")

""" Full Outer Join """
df_joined = df1.join(df2, "id", "outer")

""" Left Anti Join (Rows in df1 not in df2) """
df_anti = df1.join(df2, "id", "left_anti")

""" Left Semi Join (Rows in df1 that have match in df2) """
df_semi = df1.join(df2, "id", "left_semi")

""" Cross Join (Cartesian Product) """
df_cross = df1.crossJoin(df2)

""" Broadcast Join (Performance Optimization) """
from pyspark.sql.functions import broadcast
# Use when one table is small (< 10MB)
df_joined = large_df.join(broadcast(small_df), "id")

""" Multiple Join Conditions """
df_joined = df1.join(df2, 
    (df1.id == df2.id) & (df1.date == df2.date), 
    "inner")

# ============================================================================
# 8. PERFORMANCE OPTIMIZATION
# ============================================================================

""" Cache and Persist """
# Cache (stores in memory)
df.cache()
df.count()  # Triggers caching

# Persist with storage level
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.DISK_ONLY)

# Unpersist
df.unpersist()

""" Partitioning """
# Check number of partitions
print("Number of partitions:", df.rdd.getNumPartitions())

# Repartition (full shuffle)
df_repartitioned = df.repartition(10)
df_repartitioned = df.repartition("subject")  # Partition by column

# Coalesce (reduce partitions without full shuffle)
df_coalesced = df.coalesce(5)

""" Broadcast Variables """
# Broadcast small lookup data to all nodes
broadcast_var = spark.sparkContext.broadcast({"key1": "value1", "key2": "value2"})
# Access: broadcast_var.value

""" Predicate Pushdown """
# Filter early to reduce data movement
df_filtered = spark.read.parquet("path").filter(col("year") == 2023)

""" Column Pruning """
# Select only needed columns
df_selected = spark.read.parquet("path").select("col1", "col2")

""" Bucketing """
df.write.bucketBy(10, "id").sortBy("id").saveAsTable("bucketed_table")

""" Salting (Handle Data Skew) """
# Add random salt to skewed keys
df = df.withColumn("salted_key", concat(col("key"), lit("_"), (rand() * 10).cast("int")))

# ============================================================================
# 9. AWS INTEGRATION (S3, GLUE, DYNAMICFRAMES)
# ============================================================================

""" S3 Operations using boto3 """
import boto3

s3_client = boto3.client('s3')

# List objects in S3
response = s3_client.list_objects_v2(Bucket='my-bucket', Prefix='path/')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Upload file to S3
s3_client.upload_file('local_file.txt', 'my-bucket', 'remote_file.txt')

# Download file from S3
s3_client.download_file('my-bucket', 'remote_file.txt', 'local_file.txt')

# Read from S3 in PySpark
df = spark.read.parquet('s3://my-bucket/path/to/data/')

# Write to S3 in PySpark
df.write.mode('overwrite').parquet('s3://my-bucket/path/to/output/')

""" AWS Glue DynamicFrame """
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Create DynamicFrame from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_database",
    table_name="my_table"
)

# Create DynamicFrame from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://my-bucket/path/"]},
    format="json"
)

# Convert DynamicFrame to DataFrame
df = datasource.toDF()

# Convert DataFrame to DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# Apply transformations on DynamicFrame
from awsglue.transforms import *

# ApplyMapping - Rename and cast columns
mapped_df = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ("old_col1", "string", "new_col1", "string"),
        ("old_col2", "int", "new_col2", "long")
    ]
)

# ResolveChoice - Handle schema conflicts
resolved_df = ResolveChoice.apply(
    frame=datasource,
    choice="cast:long",
    database="my_database",
    table_name="my_table"
)

# DropFields - Remove columns
dropped_df = DropFields.apply(
    frame=datasource,
    paths=["column_to_drop"]
)

# Filter
filtered_df = Filter.apply(
    frame=datasource,
    f=lambda x: x["age"] > 30
)

# Write DynamicFrame to S3
glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": "s3://my-bucket/output/"},
    format="parquet"
)

""" Glue Job Bookmarks (Incremental Processing) """
# Enable job bookmarks in Glue job configuration
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_db",
    table_name="orders",
    transformation_ctx="orders",
    additional_options={"jobBookmarkKeys": ["order_id"], "jobBookmarkKeysSortOrder": "asc"}
)

# ============================================================================
# 10. DELTA LAKE & INCREMENTAL LOADS
# ============================================================================

""" Delta Lake Setup """
from delta.tables import DeltaTable

spark = SparkSession.builder \
    .appName("DeltaLakeExample") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

""" Create Delta Table """
df.write.format("delta").mode("overwrite").save("/path/to/delta/table")

""" Read Delta Table """
df_delta = spark.read.format("delta").load("/path/to/delta/table")

""" Upsert (Merge) Operation """
delta_table = DeltaTable.forPath(spark, "/path/to/delta/table")

delta_table.alias("existing") \
    .merge(
        new_data.alias("new"),
        "existing.id = new.id"
    ) \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll() \
    .execute()

""" Time Travel """
# Read older version
df_v1 = spark.read.format("delta").option("versionAsOf", 1).load("/path/to/delta/table")

# Read as of timestamp
df_ts = spark.read.format("delta").option("timestampAsOf", "2023-01-01").load("/path/to/delta/table")

""" Incremental Load Pattern """
# Get max timestamp from target
max_timestamp = target_df.agg({"updated_at": "max"}).collect()[0][0]

# Filter source for new records
incremental_df = source_df.filter(col("updated_at") > max_timestamp)

# Append to target
incremental_df.write.mode("append").parquet("/path/to/target/")

""" SCD Type 2 Implementation """
# Add effective dates and current flag
df_scd2 = df.withColumn("effective_from", current_date()) \
            .withColumn("effective_to", lit("9999-12-31").cast("date")) \
            .withColumn("is_current", lit(True))

# ============================================================================
# 11. RDD OPERATIONS
# ============================================================================

""" Create RDD """
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd_from_file = spark.sparkContext.textFile("path/to/file.txt")

""" RDD Transformations """
# Map
rdd_mapped = rdd.map(lambda x: x * 2)

# Filter
rdd_filtered = rdd.filter(lambda x: x > 2)

# FlatMap
rdd_flat = rdd.flatMap(lambda x: [x, x * 2])

# ReduceByKey (Word Count Example)
text_rdd = spark.sparkContext.textFile("path/to/file.txt")
word_counts = text_rdd.flatMap(lambda line: line.split(" ")) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

# GroupByKey
grouped_rdd = rdd.groupByKey()

# SortByKey
sorted_rdd = rdd.sortByKey()

""" RDD Actions """
# Collect
results = rdd.collect()

# Count
count = rdd.count()

# Take
first_5 = rdd.take(5)

# Reduce
total = rdd.reduce(lambda a, b: a + b)

""" Convert between RDD and DataFrame """
# RDD to DataFrame
df = rdd.toDF(["column_name"])

# DataFrame to RDD
rdd = df.rdd

# ============================================================================
# 12. DATA VALIDATION & QUALITY CHECKS
# ============================================================================

""" Check for Null Values """
from pyspark.sql.functions import col, isnan, when, count

# Count nulls in each column
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()

""" Check for Duplicates """
duplicate_count = df.count() - df.dropDuplicates().count()
print(f"Number of duplicates: {duplicate_count}")

""" Data Quality Checks """
# Check if column values are within range
invalid_marks = df.filter((col("marks") < 0) | (col("marks") > 100)).count()

# Check for valid email format
invalid_emails = df.filter(~col("email").rlike(r'^[\w\.-]+@[\w\.-]+\.\w+$')).count()

# Check for referential integrity
orphan_records = df1.join(df2, "foreign_key", "left_anti").count()

""" Schema Validation """
expected_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("marks", IntegerType(), True)
])

if df.schema != expected_schema:
    print("Schema mismatch!")

# ============================================================================
# 13. SPARK ARCHITECTURE CONCEPTS
# ============================================================================

"""
SPARK ARCHITECTURE:
1. Driver Program: Runs main() function, creates SparkContext
2. Cluster Manager: Allocates resources (YARN, Mesos, Kubernetes, Standalone)
3. Executors: Worker nodes that run tasks and store data
4. Tasks: Units of work sent to executors

EXECUTION FLOW:
1. Driver creates logical execution plan
2. Catalyst optimizer optimizes the plan
3. Tungsten execution engine generates physical plan
4. Tasks are distributed to executors
5. Results are collected back to driver

KEY CONCEPTS:
- Transformations: Lazy operations (map, filter, join)
- Actions: Trigger execution (collect, count, save)
- Lineage: DAG of transformations for fault tolerance
- Shuffle: Data redistribution across partitions (expensive)
- Partitioning: Data distribution strategy
- Broadcast: Send small data to all nodes
- Accumulator: Shared variable for aggregation

DATAFRAME vs RDD:
DataFrame:
- Higher-level API with schema
- Optimized by Catalyst optimizer
- Better performance
- Easier to use

RDD:
- Lower-level API
- No schema
- More control
- Use for unstructured data

READ MODES:
- PERMISSIVE: Sets corrupt records to null (default)
- DROPMALFORMED: Drops corrupt records
- FAILFAST: Throws exception on corrupt records

STORAGE LEVELS:
- MEMORY_ONLY: Cache in memory only
- MEMORY_AND_DISK: Spill to disk if memory full
- DISK_ONLY: Store only on disk
- MEMORY_ONLY_SER: Serialized in memory
- OFF_HEAP: Store in off-heap memory
"""

# ============================================================================
# COMMON INTERVIEW QUESTIONS & SOLUTIONS
# ============================================================================

""" Q1: Find employees with salary greater than their department average """
from pyspark.sql.window import Window

window_dept = Window.partitionBy("department")
df_result = df.withColumn("dept_avg_salary", avg("salary").over(window_dept)) \
              .filter(col("salary") > col("dept_avg_salary"))

""" Q2: Find top N records per group """
window_spec = Window.partitionBy("category").orderBy(col("sales").desc())
top_n = df.withColumn("rank", row_number().over(window_spec)) \
          .filter(col("rank") <= 3)

""" Q3: Calculate running total """
window_running = Window.partitionBy("user_id").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_running = df.withColumn("running_total", sum("amount").over(window_running))

""" Q4: Find consecutive login days """
window_spec = Window.partitionBy("user_id").orderBy("login_date")
df_streak = df.withColumn("prev_date", lag("login_date", 1).over(window_spec)) \
              .withColumn("days_diff", datediff(col("login_date"), col("prev_date")))

""" Q5: Pivot data (rows to columns) """
df_pivot = df.groupBy("student").pivot("subject").agg(sum("marks"))

""" Q6: Handle skewed data """
# Add salt to skewed keys
df_salted = df.withColumn("salted_key", concat(col("key"), lit("_"), (rand() * 10).cast("int")))

""" Q7: Deduplicate keeping latest record """
window_latest = Window.partitionBy("id").orderBy(col("timestamp").desc())
df_dedup = df.withColumn("row_num", row_number().over(window_latest)) \
             .filter(col("row_num") == 1) \
             .drop("row_num")

""" Q8: Calculate percentage contribution """
total_sales = df.agg(sum("sales")).collect()[0][0]
df_pct = df.withColumn("pct_contribution", (col("sales") / total_sales) * 100)

""" Q9: Find gaps in sequence """
window_spec = Window.orderBy("id")
df_gaps = df.withColumn("next_id", lead("id", 1).over(window_spec)) \
            .filter(col("next_id") - col("id") > 1)

""" Q10: Cumulative sum with reset """
window_spec = Window.partitionBy("group").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_cumsum = df.withColumn("cumulative_sum", sum("value").over(window_spec))

# ============================================================================
# END OF PYSPARK INTERVIEW GUIDE
# ============================================================================
