"""
================================================================================
                    PYSPARK - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive examples organized by topic for easy revision
Last Updated: April 2026
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
13. SPARK SQL OPERATIONS
14. USER DEFINED FUNCTIONS (UDFs)
15. ERROR HANDLING & LOGGING
16. SPARK STREAMING BASICS
17. SPARK ARCHITECTURE CONCEPTS
18. COMMON INTERVIEW QUESTIONS & SOLUTIONS
================================================================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
import logging

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
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.sql.adaptive.skewJoin.enabled", "true") \
    .getOrCreate()

# Set log level
spark.sparkContext.setLogLevel("WARN")

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

""" Get DataFrame Info """
df.info()  # In PySpark, use printSchema() instead
print(f"Number of rows: {df.count()}")
print(f"Number of columns: {len(df.columns)}")
print(f"Column names: {df.columns}")

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

# CSV with different delimiter and escape character
df_csv = spark.read.csv('path/to/file.csv', header=True, sep=';', escape='\\')

""" Reading JSON """
df_json = spark.read.json('path/to/file.json')
df_json_multiline = spark.read.option("multiline", "true").json('path/to/file.json')

# JSON with schema inference
df_json = spark.read.option("inferSchema", "true").json('path/to/file.json')

""" Reading Parquet (Recommended for Big Data) """
df_parquet = spark.read.parquet('path/to/file.parquet')

# Read multiple parquet files
df_multi_parquet = spark.read.parquet('path/to/file1.parquet', 'path/to/file2.parquet')

""" Reading from S3 """
# Make sure AWS credentials are configured
df_s3 = spark.read.parquet('s3://bucket-name/path/to/data/')
df_s3_csv = spark.read.csv('s3a://bucket-name/path/to/data.csv', header=True)

# For s3a protocol, ensure Hadoop-AWS is configured
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "your-key")
spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "your-secret")

""" Reading from Database (JDBC) """
jdbc_url = "jdbc:postgresql://hostname:port/dbname"
connection_properties = {
    "user": "username",
    "password": "password",
    "driver": "org.postgresql.Driver"
}
df_jdbc = spark.read.jdbc(url=jdbc_url, table="table_name", properties=connection_properties)

# JDBC with partition for parallel read
df_jdbc = spark.read.jdbc(
    url=jdbc_url,
    table="table_name",
    column="id",
    lowerBound=1,
    upperBound=1000000,
    numPartitions=10,
    properties=connection_properties
)

""" Read Modes in Spark """
# PERMISSIVE (default): Sets corrupt records to null
# DROPMALFORMED: Drops corrupt records
# FAILFAST: Throws exception on corrupt records
df_permissive = spark.read.option("mode", "PERMISSIVE").csv("path/to/file.csv")
df_dropmalformed = spark.read.option("mode", "DROPMALFORMED").csv("path/to/file.csv")
df_failfast = spark.read.option("mode", "FAILFAST").csv("path/to/file.csv")

""" Writing Data """
# Write as Parquet (Columnar format - Best for Analytics)
df.write.mode('overwrite').parquet('path/to/output/')

# Write as CSV
df.write.mode('append').option('header', 'true').csv('path/to/output/')

# Write modes: overwrite, append, ignore, error (default)
df.write.mode('overwrite').parquet('path/to/output/')

# Partitioned Write (Important for Performance)

df_sorted = df.repartition("year", "month").sortWithinPartitions("id")

df_sorted.write.partitionBy("year", "month").mode("overwrite").parquet("path/to/output/")


# Bucketed Write (sorts within buckets)

df.write.bucketBy(10, "id").sortBy("id").saveAsTable("bucketed_table")


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

# Fill with median - requires window function
from pyspark.sql.functions import percentile_approx
median_marks = df.agg(percentile_approx("marks", 0.5)).collect()[0][0]
df_filled = df.fillna({"marks": median_marks})

# Fill with forward fill (using window functions)
window_spec = Window.orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_filled = df.withColumn("marks_filled", last("marks", ignorenulls=True).over(window_spec))

# Fill with backward fill
window_spec = Window.orderBy(col("id").desc()).rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_filled = df.withColumn("marks_filled", last("marks", ignorenulls=True).over(window_spec))

""" Replacing Values """
# Replace specific values
df_replaced = df.replace(0, average_marks, subset=["marks"])
df_replaced = df.replace(["Math", "Science"], ["Mathematics", "Sciences"])

# Replace using when/otherwise for complex logic
df_replaced = df.withColumn("subject", 
    when(col("subject") == "Math", "Mathematics")
    .when(col("subject") == "Science", "Sciences")
    .otherwise(col("subject")))

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

# Select with renaming
df.select(col("name").alias("student_name"), col("marks").alias("score")).show()

""" Add New Column """
df = df.withColumn("marks_doubled", col("marks") * 2)
df = df.withColumn("grade", when(col("marks") >= 80, "A")
                                .when(col("marks") >= 60, "B")
                                .otherwise("C"))

# Multiple columns at once
df = df.withColumns({
    "marks_doubled": col("marks") * 2,
    "half_marks": col("marks") / 2
})

""" Rename Column """
df = df.withColumnRenamed("old_column", "new_column")

# Rename multiple columns
df = df.withColumnsRenamed({"old_col1": "new_col1", "old_col2": "new_col2"})

""" Drop Column """
df = df.drop("column_to_drop")
df = df.drop("col1", "col2", "col3")  # Drop multiple

""" Cast Column Type """
df = df.withColumn("marks", col("marks").cast("double"))
df = df.withColumn("id", col("id").cast(IntegerType()))

# Cast multiple columns
df = df.withColumn("marks", col("marks").cast(DoubleType())) \
       .withColumn("age", col("age").cast(IntegerType()))

""" Conditional Logic - when/otherwise """
df = df.withColumn("status", 
    when(col("marks") >= 80, "Excellent")
    .when(col("marks") >= 60, "Good")
    .when(col("marks") >= 40, "Average")
    .otherwise("Poor"))

# Nested when/otherwise
df = df.withColumn("category",
    when((col("marks") >= 80) & (col("subject") == "Math"), "Top Math Student")
    .when((col("marks") >= 80) & (col("subject") == "Science"), "Top Science Student")
    .otherwise("Regular Student"))

""" Filter Rows """
df_filtered = df.filter(col("marks") > 70)
df_filtered = df.where(col("marks") > 70)
df_filtered = df.filter((col("marks") > 70) & (col("subject") == "Math"))
df_filtered = df.filter((col("marks") > 70) | (col("name") == "Alice"))

# Filter with isin
df_filtered = df.filter(col("subject").isin(["Math", "Science"]))

# Filter with not
df_filtered = df.filter(~col("name").contains("Alice"))

""" String Operations """
# Trim whitespace
df = df.withColumn("name", trim(col("name")))
df = df.withColumn("name", ltrim(col("name")))  # Left trim
df = df.withColumn("name", rtrim(col("name")))  # Right trim

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

# Starts with / Ends with
df_filtered = df.filter(col("name").startswith("A"))
df_filtered = df.filter(col("name").endswith("e"))

# Regex replace
df = df.withColumn("phone_cleaned", regexp_replace(col("phone"), r"\D", ""))

# Regex extract
df = df.withColumn("area_code", regexp_extract(col("phone"), r"(\d{3})", 1))

# String length
df = df.withColumn("name_length", length(col("name")))

""" Date Operations """
from pyspark.sql.functions import current_date, current_timestamp, date_add, date_sub, datediff, months_between

df = df.withColumn("current_date", current_date())
df = df.withColumn("current_timestamp", current_timestamp())
df = df.withColumn("date_plus_7", date_add(col("date_column"), 7))
df = df.withColumn("date_minus_7", date_sub(col("date_column"), 7))
df = df.withColumn("days_diff", datediff(col("end_date"), col("start_date")))
df = df.withColumn("months_diff", months_between(col("end_date"), col("start_date")))

# Extract year, month, day
df = df.withColumn("year", year(col("date_column")))
df = df.withColumn("month", month(col("date_column")))
df = df.withColumn("day", dayofmonth(col("date_column")))
df = df.withColumn("week", weekofyear(col("date_column")))

# Add months
df = df.withColumn("date_plus_3m", add_months(col("date_column"), 3))

# Date formatting
df = df.withColumn("formatted_date", date_format(col("date_column"), "yyyy-MM-dd"))

""" Array Operations """
# Explode array into rows
df_exploded = df.select(col("name"), explode(col("languages")).alias("language"))

# Array contains
df_filtered = df.filter(array_contains(col("languages"), "Python"))

# Array size
df = df.withColumn("num_languages", size(col("languages")))

# Create array
df = df.withColumn("languages_array", array(col("lang1"), col("lang2")))

# Array concat
df = df.withColumn("all_langs", concat(col("languages1"), col("languages2")))

# Collect array elements into string
df = df.withColumn("langs_str", concat_ws(",", col("languages")))

""" Numeric Operations """
# Absolute value
df = df.withColumn("abs_marks", abs(col("marks")))

# Round
df = df.withColumn("rounded_marks", round(col("marks"), 2))

# Ceil and Floor
df = df.withColumn("ceil_marks", ceil(col("marks")))
df = df.withColumn("floor_marks", floor(col("marks")))

# Power
df = df.withColumn("marks_squared", pow(col("marks"), 2))

# Modulo
df = df.withColumn("remainder", col("marks") % 5)

""" Sort/Order By """
df_sorted = df.orderBy("marks")
df_sorted = df.orderBy(col("marks").desc())
df_sorted = df.orderBy(col("subject").asc(), col("marks").desc())

# With NULLs first/last
df_sorted = df.orderBy(col("marks").desc_nulls_first())
df_sorted = df.orderBy(col("marks").desc_nulls_last())

# ============================================================================
# 5. AGGREGATIONS & GROUP BY
# ============================================================================

""" Basic Aggregations """
df.agg(sum("marks"), avg("marks"), max("marks"), min("marks"), count("*")).show()

# Single aggregation
df.agg(sum("marks").alias("total_marks")).show()

""" Group By """
df_grouped = df.groupBy("subject").agg(
    count("*").alias("student_count"),
    avg("marks").alias("avg_marks"),
    max("marks").alias("max_marks"),
    min("marks").alias("min_marks"),
    sum("marks").alias("total_marks")
)

# Multiple group by columns
df_grouped = df.groupBy("subject", "year").agg(
    count("*").alias("count"),
    avg("marks").alias("avg_marks")
)

""" Count Distinct """
df.agg(countDistinct("subject").alias("unique_subjects")).show()

# Count distinct in group by
df_grouped = df.groupBy("year").agg(
    countDistinct("subject").alias("unique_subjects")
)

""" Collect List/Set """
df_grouped = df.groupBy("subject").agg(
    collect_list("name").alias("students"),
    collect_set("name").alias("unique_students")
)

""" Pivot (Convert rows to columns) """
df_pivot = df.groupBy("name").pivot("subject").agg(sum("marks"))

# Pivot with specific values
df_pivot = df.groupBy("name").pivot("subject", ["Math", "Science"]).agg(sum("marks"))

""" Multiple Aggregations """
df_agg = df.groupBy("subject").agg(
    count("*").alias("count"),
    avg("marks").alias("avg_marks"),
    stddev("marks").alias("std_marks"),
    variance("marks").alias("var_marks"),
    max("marks").alias("max_marks"),
    min("marks").alias("min_marks")
)

""" Having Clause (Filter after aggregation) """
df_grouped = df.groupBy("subject").agg(
    count("*").alias("student_count"),
    avg("marks").alias("avg_marks")
).filter(col("student_count") > 2)  # HAVING equivalent

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

# LAG with default value
df = df.withColumn("previous_marks", lag("marks", 1, 0).over(window_spec))

""" LEAD - Access next row value """
df = df.withColumn("next_marks", lead("marks", 1).over(window_spec))

# LEAD with default value
df = df.withColumn("next_marks", lead("marks", 1, 0).over(window_spec))

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

""" Window with ROWS and RANGE """
# ROWS: Physical rows from window
window_rows = Window.partitionBy("subject").orderBy("id").rowsBetween(-1, 1)

# RANGE: Logical range based on values (default)
window_range = Window.partitionBy("subject").orderBy("id").rangeBetween(-10, 10)

# ============================================================================
# 7. JOINS (VERY IMPORTANT)
# ============================================================================

""" Inner Join """
df_joined = df1.join(df2, df1.id == df2.id, "inner")
df_joined = df1.join(df2, "id", "inner")  # When column names are same

""" Left Join """
df_joined = df1.join(df2, "id", "left")
df_joined = df1.join(df2, "id", "leftouter")  # Same as left

""" Right Join """
df_joined = df1.join(df2, "id", "right")
df_joined = df1.join(df2, "id", "rightouter")  # Same as right

""" Full Outer Join """
df_joined = df1.join(df2, "id", "outer")
df_joined = df1.join(df2, "id", "fullouter")  # Same as outer

""" Left Anti Join (Rows in df1 not in df2) """
df_anti = df1.join(df2, "id", "left_anti")

""" Left Semi Join (Rows in df1 that have match in df2) """
df_semi = df1.join(df2, "id", "left_semi")

""" Cross Join (Cartesian Product) """
df_cross = df1.crossJoin(df2)

# WARNING: Causes data explosion! Use with caution

""" Broadcast Join (Performance Optimization) """
from pyspark.sql.functions import broadcast
# Use when one table is small (< 10MB)
df_joined = large_df.join(broadcast(small_df), "id")

""" Multiple Join Conditions """
df_joined = df1.join(df2, 
    (df1.id == df2.id) & (df1.date == df2.date), 
    "inner")

""" Join with column rename (to avoid duplicates) """
df_joined = df1.join(df2.select(col("id").alias("df2_id"), col("name")), 
    df1.id == df2.id, "inner")

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
df.persist(StorageLevel.MEMORY_ONLY_SER)

# Unpersist
df.unpersist()

# Check cache status
df.is_cached

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
lookup_dict = {"key1": "value1", "key2": "value2"}
broadcast_var = spark.sparkContext.broadcast(lookup_dict)

# Access in UDF
def lookup_func(key):
    return broadcast_var.value.get(key, "Not Found")

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

# Remove salt after aggregation
df = df.withColumn("key", regexp_replace(col("salted_key"), "_\\d+$", ""))

""" Check Spark Configuration """
print(spark.sparkContext.getConf().getAll())

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

# Delete object from S3
s3_client.delete_object(Bucket='my-bucket', Key='file.txt')

# Read from S3 in PySpark
df = spark.read.parquet('s3://my-bucket/path/to/data/')

# Write to S3 in PySpark
df.write.mode('overwrite').parquet('s3://my-bucket/path/to/output/')

""" AWS Glue DynamicFrame """
try:
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

except ImportError:
    print("AWS Glue libraries not available")

""" Glue Job Bookmarks (Incremental Processing) """
# Enable job bookmarks in Glue job configuration
# datasource = glueContext.create_dynamic_frame.from_catalog(
#     database="my_db",
#     table_name="orders",
#     transformation_ctx="orders",
#     additional_options={"jobBookmarkKeys": ["order_id"], "jobBookmarkKeysSortOrder": "asc"}
# )

# ============================================================================
# 10. DELTA LAKE & INCREMENTAL LOADS
# ============================================================================

""" Delta Lake Setup """
try:
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

    """ View Delta History """
    history_df = spark.sql("DESCRIBE HISTORY /path/to/delta/table")

    """ Optimize Delta Table """
    spark.sql("OPTIMIZE delta.`/path/to/delta/table`")

    """ Compact Small Files """
    spark.sql("OPTIMIZE delta.`/path/to/delta/table` ZORDER BY (id)")

except ImportError:
    print("Delta Lake not installed")

""" Incremental Load Pattern """
# Get max timestamp from target
max_timestamp = target_df.agg({"updated_at": "max"}).collect()[0][0] if target_df.count() > 0 else "1900-01-01"

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

# Distinct
distinct_rdd = rdd.distinct()

# Union
combined_rdd = rdd1.union(rdd2)

""" RDD Actions """
# Collect
results = rdd.collect()

# Count
count = rdd.count()

# Take
first_5 = rdd.take(5)

# Reduce
total = rdd.reduce(lambda a, b: a + b)

# First
first = rdd.first()

# SaveAsTextFile
rdd.saveAsTextFile("path/to/output")

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

# Check NaN values
df.select([count(when(isnan(c), c)).alias(c) for c in df.columns if df.schema[c].dataType == DoubleType()]).show()

""" Check for Duplicates """
duplicate_count = df.count() - df.dropDuplicates().count()
print(f"Number of duplicates: {duplicate_count}")

# Find duplicate rows
df.groupBy(df.columns).count().filter(col("count") > 1).show()

""" Data Quality Checks """
# Check if column values are within range
invalid_marks = df.filter((col("marks") < 0) | (col("marks") > 100)).count()

# Check for valid email format
invalid_emails = df.filter(~col("email").rlike(r'^[\w\.-]+@[\w\.-]+\.\w+$')).count()

# Check for referential integrity
orphan_records = df1.join(df2, "foreign_key", "left_anti").count()

# Check data completeness
completeness = (df.count() - df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).collect()[0][0]) / df.count() * 100

""" Schema Validation """
expected_schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False),
    StructField("marks", IntegerType(), True)
])

if df.schema != expected_schema:
    print("Schema mismatch!")

# ============================================================================
# 13. SPARK SQL OPERATIONS
# ============================================================================

""" Create Temporary Views """
df.createOrReplaceTempView("temp_view")  # Session scoped
df.createOrReplaceGlobalTempView("global_view")  # Application scoped

""" SQL Queries """
result = spark.sql("SELECT * FROM temp_view WHERE marks > 70")

# Group by with SQL
result = spark.sql("""
    SELECT subject, COUNT(*) as count, AVG(marks) as avg_marks
    FROM temp_view
    GROUP BY subject
""")

# Join with SQL
result = spark.sql("""
    SELECT t1.id, t1.name, t2.subject
    FROM temp_table1 t1
    INNER JOIN temp_table2 t2 ON t1.id = t2.id
""")

# Window functions with SQL
result = spark.sql("""
    SELECT name, marks, 
           ROW_NUMBER() OVER (PARTITION BY subject ORDER BY marks DESC) as rank
    FROM temp_view
""")

# CTE (Common Table Expressions)
result = spark.sql("""
    WITH filtered_data AS (
        SELECT * FROM temp_view WHERE marks > 60
    )
    SELECT subject, COUNT(*) as count
    FROM filtered_data
    GROUP BY subject
""")

""" Register DataFrame as SQL table """
spark.sql("""
    CREATE OR REPLACE TABLE my_table AS
    SELECT * FROM temp_view
""")

# ============================================================================
# 14. USER DEFINED FUNCTIONS (UDFs)
# ============================================================================

""" Python UDF (Standard, but slower) """
from pyspark.sql.types import StringType, IntegerType

@udf(StringType())
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

df = df.withColumn("grade", get_grade(col("marks")))

""" Pandas UDF (Vectorized, much faster) """
import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf(StringType())
def get_grade_pandas(s: pd.Series) -> pd.Series:
    return s.apply(lambda x: "A" if x >= 80 else "B" if x >= 60 else "C")

df = df.withColumn("grade", get_grade_pandas(col("marks")))

""" UDF with Multiple Parameters """
@udf(StringType())
def categorize(marks, subject):
    if marks >= 80 and subject == "Math":
        return "Top Math Student"
    elif marks >= 80:
        return "Top Student"
    else:
        return "Regular Student"

df = df.withColumn("category", categorize(col("marks"), col("subject")))

""" Register UDF for SQL """
spark.udf.register("get_grade_sql", get_grade)

result = spark.sql("SELECT name, marks, get_grade_sql(marks) as grade FROM temp_view")

""" Aggregate UDF (UDAF) """
from pyspark.sql.expressions import UserDefinedAggregateFunction

class MeanUDAF(UserDefinedAggregateFunction):
    def inputSchema(self):
        return StructType([StructField("value", DoubleType())])
    
    def bufferSchema(self):
        return StructType([
            StructField("sum", DoubleType()),
            StructField("count", LongType())
        ])
    
    def dataType(self):
        return DoubleType()
    
    def deterministic(self):
        return True
    
    def initialize(self, buffer):
        buffer[0] = 0.0
        buffer[1] = 0L
    
    def update(self, buffer, input):
        buffer[0] += input[0]
        buffer[1] += 1
    
    def merge(self, buffer1, buffer2):
        buffer1[0] += buffer2[0]
        buffer1[1] += buffer2[1]
    
    def evaluate(self, buffer):
        if buffer[1] == 0:
            return None
        return buffer[0] / buffer[1]

mean_udf = MeanUDAF()
spark.udf.register("mean_udf", mean_udf)

# ============================================================================
# 15. ERROR HANDLING & LOGGING
# ============================================================================

""" Set up Logging """
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

""" Try-Except Error Handling """
try:
    df = spark.read.csv("non_existent_file.csv", header=True)
except Exception as e:
    logger.error(f"Error reading file: {str(e)}")
    df = spark.createDataFrame([], StructType([]))

""" Data Validation with Error Handling """
def validate_and_process(df, required_columns):
    try:
        # Check required columns
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns: {missing_cols}")
        
        # Check for nulls
        null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
        logger.info(f"Null counts: {null_counts.collect()[0].asDict()}")
        
        # Process data
        df_processed = df.dropDuplicates().na.drop(subset=required_columns)
        logger.info(f"Processed {df_processed.count()} records")
        
        return df_processed
    
    except Exception as e:
        logger.error(f"Error during validation: {str(e)}")
        raise

""" Catch Specific Exceptions """
try:
    result = df.agg(sum("non_existent_column"))
except AnalysisException as e:
    logger.error(f"Analysis error: {str(e)}")
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")

# ============================================================================
# 16. SPARK STREAMING BASICS
# ============================================================================

""" Structured Streaming - Reading from Socket (for demo) """
try:
    lines = spark.readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    # Count words in real-time
    words = lines.select(explode(split(col("value"), " ")).alias("word"))
    wordCounts = words.groupBy("word").count()

    # Write stream output
    query = wordCounts.writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()

except Exception as e:
    logger.info(f"Streaming not available in this environment: {e}")

""" Micro-batch Streaming """
# Read from Kafka
try:
    df_kafka = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "topic_name") \
        .load()

    # Parse and process
    df_parsed = df_kafka.select(
        from_json(col("value").cast("string"), schema).alias("data")
    ).select("data.*")

    # Write to parquet
    query = df_parsed.writeStream \
        .format("parquet") \
        .option("path", "/path/to/output") \
        .option("checkpointLocation", "/path/to/checkpoint") \
        .start()

except Exception as e:
    logger.info(f"Kafka streaming not available: {e}")

# ============================================================================
# 17. SPARK ARCHITECTURE CONCEPTS
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

JOIN OPTIMIZATION:
- Broadcast Hash Join: One side < broadcast threshold
- Shuffle Sort Merge Join: Both sides large, shuffle then sort
- Shuffle Hash Join: Hash-based join after shuffle

QUERY OPTIMIZATION:
- Predicate Pushdown: Filter data early
- Column Pruning: Select only needed columns
- Constant Folding: Pre-compute constant expressions
- Null Propagation: Eliminate null conditions
"""

# ============================================================================
# 18. COMMON INTERVIEW QUESTIONS & SOLUTIONS
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

""" Q11: Find duplicates with business logic """
# Find customers with duplicate transactions
duplicate_txn = df.withColumn("row_num", row_number().over(Window.partitionBy("customer_id", "amount").orderBy("timestamp"))) \
                  .filter(col("row_num") > 1)

""" Q12: Unpivot (Melt) data """
# Convert columns to rows
from pyspark.sql.functions import array, struct

id_cols = ["student_id"]
value_cols = [c for c in df.columns if c not in id_cols]

unpivoted = df.select(
    col("student_id"),
    explode(array([struct(lit(c).alias("subject"), col(c).alias("marks")) for c in value_cols])).alias("data")
).select("student_id", col("data.subject"), col("data.marks"))

# ============================================================================
# END OF PYSPARK INTERVIEW GUIDE
# ============================================================================
