# PySpark – Data Engineer Interview Guide

Spark 3.x (most examples also work on Spark 3.3+; version-specific APIs are marked). AWS context: S3, Glue, EMR.

**Imports used throughout**
```python
from pyspark.sql import SparkSession, Window, functions as F
from pyspark.sql.types import *
import logging
```
Use `functions as F` instead of `from pyspark.sql.functions import *` – the wildcard import silently replaces Python's built-in `sum`, `max`, `min`, `abs`, `round` and `pow`, which causes confusing bugs.

---

## 1. Spark Architecture (start here in interviews)

| Component | Role |
|---|---|
| **Driver** | Runs your `main()`, creates the `SparkSession`, builds the plan, schedules tasks, collects results |
| **Cluster manager** | Allocates resources – YARN (EMR), Kubernetes, Standalone (Mesos is deprecated) |
| **Executors** | JVM processes on worker nodes; run tasks and cache data. Each has cores (parallel task slots) and memory |
| **Task** | Work on **one partition** by one core |

**Job → Stage → Task**
- An **action** (`count`, `collect`, `write`) triggers a **job**.
- A job is split into **stages** at every **shuffle** boundary.
- Each stage runs one **task per partition**.

**Lazy evaluation:** transformations (`select`, `filter`, `join`) only build a plan; nothing runs until an action. This lets Spark optimize the whole plan (e.g. push filters down, prune columns).

**Narrow vs wide transformations**
- Narrow – each output partition depends on one input partition, no data movement: `select`, `filter`, `withColumn`, `map`, `union`, `coalesce`.
- Wide – requires a **shuffle** (data exchanged over the network; expensive): `groupBy`, `join` (non-broadcast), `distinct`, `orderBy`, `repartition`, window functions.

**Execution flow**
1. Your code → unresolved **logical plan**.
2. **Catalyst** optimizer: analysis (resolve columns/tables) → logical optimization (predicate pushdown, column pruning, constant folding) → **physical plan** (chooses join strategies, etc.).
3. **Tungsten** executes it efficiently (off-heap memory management, whole-stage code generation).
4. **AQE (Adaptive Query Execution)** – on by default since Spark 3.2 – re-optimizes at runtime using real shuffle statistics: coalesces small shuffle partitions, switches to broadcast joins, splits skewed partitions.

`df.explain("formatted")` shows the physical plan; the **Spark UI** shows jobs, stages, tasks, shuffle sizes, spill and skew.

**DataFrame vs RDD**
| DataFrame | RDD |
|---|---|
| Schema, columnar, optimized by Catalyst/Tungsten | No schema, no optimizer |
| Faster, less code; Python and JVM run at the same speed for built-in functions | Python lambdas run in Python workers (slower) |
| Default choice | Low-level control, unstructured data, legacy code |

**Fault tolerance:** Spark records each dataset's **lineage** (the DAG of transformations). If an executor dies, lost partitions are recomputed from lineage.

**Deploy modes:** *client* – driver runs where you submit (notebooks, debugging); *cluster* – driver runs inside the cluster (production).

---

## 2. SparkSession and DataFrame Basics

```python
spark = (SparkSession.builder
         .appName("DataEngineerInterview")
         .config("spark.sql.shuffle.partitions", "200")              # default 200; AQE can coalesce
         .config("spark.sql.adaptive.enabled", "true")               # default true in 3.2+
         .config("spark.sql.adaptive.coalescePartitions.enabled", "true")
         .config("spark.sql.adaptive.skewJoin.enabled", "true")
         .getOrCreate())
# Executor/driver memory must be set at launch (spark-submit / cluster config), not after the JVM starts:
# spark-submit --driver-memory 2g --executor-memory 4g --executor-cores 4 job.py
spark.sparkContext.setLogLevel("WARN")
```

```python
data = [(1, "Alice", 85, "Math"), (2, "Bob", None, "Science"), (3, "Charlie", 78, "Math")]
df = spark.createDataFrame(data, ["id", "name", "marks", "subject"])

# Explicit schema – always do this in production (faster than inference, no surprises)
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("marks", IntegerType(), True),
    StructField("subject", StringType(), True),
])
df = spark.createDataFrame(data, schema)
# DDL string alternative: schema = "id INT, name STRING, marks INT, subject STRING"

df.show(5, truncate=False); df.printSchema(); df.describe().show()
df.count(); df.columns; df.dtypes; len(df.columns)
```
There is no `df.info()` in PySpark – use `printSchema()`, `dtypes` and `describe()`/`summary()`.

---

## 3. Reading and Writing Data

### Reading
```python
# CSV
df_csv = (spark.read.format("csv")
          .option("header", "true").option("sep", ",")
          .option("inferSchema", "true")          # extra pass over the data – prefer .schema(schema)
          .option("mode", "PERMISSIVE")
          .load("path/to/file.csv"))
df_csv = spark.read.csv("path/to/file.csv", header=True, schema=schema)
df_csv = spark.read.csv("path/to/file.csv", header=True, sep=";", escape="\\", quote='"')

# JSON (schema is inferred by default; pass a schema for speed)
df_json = spark.read.json("path/to/file.json")                       # JSON Lines: one object per line
df_json_multi = spark.read.option("multiLine", "true").json("path/to/file.json")   # one big JSON document/array

# Parquet / ORC (schema stored in the file)
df_parquet = spark.read.parquet("path/to/data/")
df_multi = spark.read.parquet("path/a.parquet", "path/b.parquet")
df_merged = spark.read.option("mergeSchema", "true").parquet("path/")   # files with evolving schemas

# S3 – on EMR/Glue use s3:// (EMRFS); with open-source Hadoop use s3a://
df_s3 = spark.read.parquet("s3://bucket-name/path/to/data/")
```
Credentials: use the IAM role of the cluster/Glue job. **Never** hardcode `fs.s3a.access.key`/`secret.key` in code.

**Read modes (CSV/JSON)**
| Mode | Behaviour |
|---|---|
| `PERMISSIVE` (default) | Malformed fields become null; the raw line goes to `_corrupt_record` if that column is in the schema |
| `DROPMALFORMED` | Drops malformed rows |
| `FAILFAST` | Throws on the first malformed row |

```python
bad_schema = schema.add("_corrupt_record", StringType())
df = (spark.read.schema(bad_schema).option("mode", "PERMISSIVE")
      .option("columnNameOfCorruptRecord", "_corrupt_record").csv("path/"))
df.cache()   # cache first: Spark disallows queries that reference only the corrupt-record column on raw files
bad_rows = df.filter(F.col("_corrupt_record").isNotNull())
```
On Databricks, `option("badRecordsPath", ...)` writes bad rows to a separate location.

**JDBC**
```python
jdbc_url = "jdbc:postgresql://host:5432/dbname"
props = {"user": user, "password": password, "driver": "org.postgresql.Driver"}   # fetch secrets from Secrets Manager
df_jdbc = spark.read.jdbc(url=jdbc_url, table="table_name", properties=props)

# Parallel read: 10 queries, each on a range of id
df_jdbc = spark.read.jdbc(url=jdbc_url, table="table_name", column="id",
                          lowerBound=1, upperBound=1_000_000, numPartitions=10, properties=props)
# lowerBound/upperBound only define the stride – they do NOT filter rows.
# Push a filter with a subquery: table="(SELECT * FROM t WHERE updated_at > '2026-10-01') AS q"
# Tune with option("fetchsize", 10000)
```

### Writing
```python
df.write.mode("overwrite").parquet("path/to/output/")
df.write.mode("append").option("header", "true").csv("path/to/output/")
# Modes: overwrite, append, ignore, error / errorifexists (default)

# Partitioned write – one folder per value: .../year=2026/month=10/
(df.repartition("year", "month")                 # one task per partition value → fewer, larger files
   .sortWithinPartitions("id")
   .write.partitionBy("year", "month").mode("overwrite").parquet("path/to/output/"))

# Overwrite only the partitions present in df (not the whole table)
spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

# Bucketed write – only with saveAsTable (needs a metastore/catalog)
df.write.bucketBy(10, "id").sortBy("id").saveAsTable("bucketed_table")

df.write.jdbc(url=jdbc_url, table="target_table", mode="append", properties=props)
df.write.option("maxRecordsPerFile", 1_000_000).parquet("s3://bucket-name/path/to/output/")
```

**File format choice**
| Format | Notes |
|---|---|
| Parquet | Columnar, compressed, schema included, predicate pushdown → default for analytics |
| ORC | Similar to Parquet (Hive ecosystem) |
| Avro | Row-based, good for streaming/Kafka and schema evolution |
| CSV / JSON | Human-readable, slow, no types (JSON) or fragile (CSV) |
| Delta / Iceberg / Hudi | Parquet + transaction log → ACID, MERGE, time travel, schema evolution |

**Partition-column choice:** low-to-medium cardinality columns used in filters (date, region). Partitioning by a high-cardinality column (customer_id) creates millions of tiny files.

---

## 4. Data Cleaning and Null Handling

```python
# fillna
df_filled = df.fillna({"marks": 0, "name": "Unknown"})

# Fill with mean / median (common question)
avg_marks = df.select(F.avg("marks")).first()[0]
df_filled = df.na.fill({"marks": avg_marks})          # float into an INT column is cast to int
median_marks = df.select(F.percentile_approx("marks", 0.5)).first()[0]   # aggregate; F.median() in 3.4+
df_filled = df.fillna({"marks": median_marks})

# Forward fill: last non-null value so far (per group)
w_ffill = Window.partitionBy("subject").orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df_ffill = df.withColumn("marks_filled", F.last("marks", ignorenulls=True).over(w_ffill))

# Backward fill: next non-null value
w_bfill = Window.partitionBy("subject").orderBy("id").rowsBetween(Window.currentRow, Window.unboundedFollowing)
df_bfill = df.withColumn("marks_filled", F.first("marks", ignorenulls=True).over(w_bfill))
```
A window with `orderBy` but **no** `partitionBy` moves all rows to a single partition – fine for small data, a bottleneck for big data.

```python
# Replace values
df_replaced = df.replace(0, 50, subset=["marks"])
df_replaced = df.replace(["Math", "Science"], ["Mathematics", "Sciences"], subset=["subject"])
df_replaced = df.withColumn("subject",
    F.when(F.col("subject") == "Math", "Mathematics")
     .when(F.col("subject") == "Science", "Sciences")
     .otherwise(F.col("subject")))
df = df.withColumn("marks", F.coalesce("marks", F.lit(0)))   # first non-null

# Drop nulls
df.na.drop(how="any")                   # any column null
df.na.drop(how="all")                   # all columns null
df.na.drop(thresh=2)                    # keep rows with at least 2 non-null values
df.na.drop(subset=["marks", "name"])

# Duplicates
df.dropDuplicates()                     # same as distinct()
df.dropDuplicates(["id", "name"])       # keeps an ARBITRARY row per key – use a window to keep the latest (section 18)
```

---

## 5. Column Operations and Transformations

```python
# Select / rename
df.select("name", "marks"); df.select(F.col("name"), df.marks)
df.select(F.col("name").alias("student_name"), F.col("marks").alias("score"))
df.selectExpr("name", "marks * 2 AS marks_doubled")

# Add / change columns
df = df.withColumn("marks_doubled", F.col("marks") * 2)
df = df.withColumns({"marks_doubled": F.col("marks") * 2, "half_marks": F.col("marks") / 2})   # 3.3+
df = df.withColumnRenamed("old_column", "new_column")
df = df.withColumnsRenamed({"old_col1": "new_col1", "old_col2": "new_col2"})                   # 3.4+
df = df.drop("col1", "col2")
```
Calling `withColumn` in a long loop creates a huge plan (slow analysis, even StackOverflow) – use one `select`/`withColumns` instead.

```python
# Cast
df = df.withColumn("marks", F.col("marks").cast("double"))
df = df.withColumn("id", F.col("id").cast(IntegerType()))
df = df.withColumn("amount", F.col("amount").cast("decimal(12,2)"))   # use DECIMAL for money
# Invalid casts return NULL (non-ANSI mode) – validate after casting

# when / otherwise
df = df.withColumn("status",
    F.when(F.col("marks") >= 80, "Excellent")
     .when(F.col("marks") >= 60, "Good")
     .when(F.col("marks") >= 40, "Average")
     .otherwise("Poor"))
df = df.withColumn("category",
    F.when((F.col("marks") >= 80) & (F.col("subject") == "Math"), "Top Math Student")
     .when((F.col("marks") >= 80) & (F.col("subject") == "Science"), "Top Science Student")
     .otherwise("Regular Student"))

# Filter – use & | ~ with parentheses (not and/or/not)
df.filter(F.col("marks") > 70); df.where("marks > 70")
df.filter((F.col("marks") > 70) & (F.col("subject") == "Math"))
df.filter((F.col("marks") > 70) | (F.col("name") == "Alice"))
df.filter(F.col("subject").isin("Math", "Science"))
df.filter(~F.col("name").contains("Alice"))
df.filter(F.col("marks").isNull()); df.filter(F.col("marks").between(60, 80))
# NULL comparisons: col == None is never true – use isNull() or eqNullSafe()
```

### Strings
```python
df = df.withColumn("name", F.trim("name"))        # also F.ltrim / F.rtrim
df = df.withColumn("name_upper", F.upper("name")).withColumn("name_lower", F.lower("name"))
df = df.withColumn("first_char", F.substring("name", 1, 1))   # 1-based
df = df.withColumn("full_info", F.concat_ws(" - ", "name", "subject"))   # concat_ws skips nulls; concat returns null if any is null
df = df.withColumn("name_parts", F.split("name", " "))
df = df.withColumn("first_name", F.split("name", " ").getItem(0))
df.filter(F.col("name").contains("Alice")); df.filter(F.col("name").startswith("A")); df.filter(F.col("name").endswith("e"))
df.filter(F.col("name").like("A%")); df.filter(F.col("email").rlike(r"^[\w.-]+@[\w.-]+\.\w+$"))
df = df.withColumn("phone_cleaned", F.regexp_replace("phone", r"\D", ""))
df = df.withColumn("area_code", F.regexp_extract("phone", r"(\d{3})", 1))
df = df.withColumn("name_length", F.length("name"))
df = df.withColumn("zip", F.lpad("zip", 5, "0"))
df = df.withColumn("ssn_masked", F.concat(F.lit("***-**-"), F.substring("ssn", -4, 4)))
df = df.withColumn("row_hash", F.sha2(F.concat_ws("||", "name", "subject"), 256))   # change detection
```

### Dates and timestamps
```python
df = df.withColumn("load_date", F.current_date()).withColumn("load_ts", F.current_timestamp())
df = df.withColumn("d", F.to_date("date_str", "yyyy-MM-dd"))
df = df.withColumn("ts", F.to_timestamp("ts_str", "yyyy-MM-dd HH:mm:ss"))
df = df.withColumn("date_plus_7", F.date_add("date_column", 7))
df = df.withColumn("date_minus_7", F.date_sub("date_column", 7))
df = df.withColumn("days_diff", F.datediff("end_date", "start_date"))
df = df.withColumn("months_diff", F.months_between("end_date", "start_date"))
df = df.withColumn("date_plus_3m", F.add_months("date_column", 3))
df = df.withColumn("year", F.year("date_column")).withColumn("month", F.month("date_column")) \
       .withColumn("day", F.dayofmonth("date_column")).withColumn("week", F.weekofyear("date_column"))
df = df.withColumn("formatted", F.date_format("date_column", "yyyyMMdd"))
df = df.withColumn("month_start", F.trunc("date_column", "month")).withColumn("month_end", F.last_day("date_column"))
df = df.withColumn("local_ts", F.from_utc_timestamp("ts", "America/New_York"))
```
Spark uses Java datetime patterns (`yyyy-MM-dd HH:mm:ss`): `MM` = month, `mm` = minute. Session time zone: `spark.sql.session.timeZone` (set to UTC for pipelines).

### Arrays, maps, structs and JSON
```python
df_exploded = df.select("name", F.explode("languages").alias("language"))        # drops rows with empty/null arrays
df_exploded = df.select("name", F.explode_outer("languages").alias("language"))  # keeps them (like LEFT JOIN)
df_pos      = df.select("name", F.posexplode("languages"))                       # with index
df.filter(F.array_contains("languages", "Python"))
df = df.withColumn("num_languages", F.size("languages"))
df = df.withColumn("languages_array", F.array("lang1", "lang2"))
df = df.withColumn("all_langs", F.concat("languages1", "languages2"))            # concat works on arrays too
df = df.withColumn("langs_str", F.concat_ws(",", "languages"))
df = df.withColumn("langs_upper", F.transform("languages", lambda x: F.upper(x)))  # higher-order functions
df = df.withColumn("py_only", F.filter("languages", lambda x: x.startswith("Py")))

# JSON strings
json_schema = "order_id INT, customer STRUCT<id: INT, name: STRING>, items ARRAY<STRUCT<sku: STRING, qty: INT>>"
df = df.withColumn("j", F.from_json("payload", json_schema))
df.select("j.order_id", "j.customer.name", F.explode("j.items").alias("item")).select("*", "item.sku")
df = df.withColumn("city", F.get_json_object("payload", "$.address.city"))
df = df.withColumn("as_json", F.to_json(F.struct("id", "name")))
```

### Numbers and sorting
```python
df = df.withColumn("abs_marks", F.abs("marks"))
df = df.withColumn("rounded", F.round("marks", 2))          # HALF_UP; F.bround = banker's rounding
df = df.withColumn("ceil_marks", F.ceil("marks")).withColumn("floor_marks", F.floor("marks"))
df = df.withColumn("marks_squared", F.pow("marks", 2))
df = df.withColumn("remainder", F.col("marks") % 5)

df.orderBy("marks"); df.orderBy(F.col("marks").desc())
df.orderBy(F.col("subject").asc(), F.col("marks").desc())
df.orderBy(F.col("marks").desc_nulls_first()); df.orderBy(F.col("marks").desc_nulls_last())
```
`orderBy` is a global sort (full shuffle) – avoid it unless the output must be ordered; `sortWithinPartitions` is cheaper.

---

## 6. Aggregations

```python
df.agg(F.sum("marks"), F.avg("marks"), F.max("marks"), F.min("marks"), F.count("*")).show()
df.agg(F.sum("marks").alias("total_marks"))

df_grouped = df.groupBy("subject").agg(
    F.count("*").alias("student_count"),           # counts rows
    F.count("marks").alias("marks_count"),         # counts NON-NULL values
    F.avg("marks").alias("avg_marks"),
    F.max("marks").alias("max_marks"),
    F.min("marks").alias("min_marks"),
    F.sum("marks").alias("total_marks"),
    F.stddev("marks").alias("std_marks"),
    F.variance("marks").alias("var_marks"),
)
df.groupBy("subject", "year").agg(F.count("*").alias("count"), F.avg("marks").alias("avg_marks"))

df.agg(F.countDistinct("subject").alias("unique_subjects"))
df.agg(F.approx_count_distinct("customer_id").alias("approx_customers"))   # much cheaper on big data
df.groupBy("year").agg(F.countDistinct("subject").alias("unique_subjects"))

df.groupBy("subject").agg(F.collect_list("name").alias("students"),        # keeps duplicates, order not guaranteed
                          F.collect_set("name").alias("unique_students"))  # unique values
df.groupBy("customer_id").agg(F.max_by("status", "updated_at").alias("latest_status"))   # 3.3+

# Conditional aggregation
df.groupBy("subject").agg(F.sum(F.when(F.col("marks") >= 80, 1).otherwise(0)).alias("excellent_cnt"))

# HAVING = filter after agg
df.groupBy("subject").agg(F.count("*").alias("cnt")).filter(F.col("cnt") > 2)

# Pivot (rows → columns) – pass the values to avoid an extra job that discovers them
df.groupBy("name").pivot("subject").agg(F.sum("marks"))
df.groupBy("name").pivot("subject", ["Math", "Science"]).agg(F.sum("marks"))

# Subtotals
df.rollup("region", "subject").agg(F.sum("marks"))     # hierarchical subtotals + grand total
df.cube("region", "subject").agg(F.sum("marks"))       # all combinations
```

---

## 7. Window Functions (very important)

A window computes a value per row using related rows, **without collapsing rows** (unlike `groupBy`).

```python
w = Window.partitionBy("subject").orderBy(F.col("marks").desc())

df = df.withColumn("row_num", F.row_number().over(w))       # 1,2,3,4 – unique
df = df.withColumn("rank", F.rank().over(w))                # 1,2,2,4 – gaps after ties
df = df.withColumn("dense_rank", F.dense_rank().over(w))    # 1,2,2,3 – no gaps
df = df.withColumn("previous_marks", F.lag("marks", 1).over(w))
df = df.withColumn("previous_marks", F.lag("marks", 1, 0).over(w))   # default when no previous row
df = df.withColumn("next_marks", F.lead("marks", 1).over(w))
df = df.withColumn("next_marks", F.lead("marks", 1, 0).over(w))
df = df.withColumn("cume_dist", F.cume_dist().over(w))
df = df.withColumn("percent_rank", F.percent_rank().over(w))
df = df.withColumn("quartile", F.ntile(4).over(w))

# Running total and moving average
w_running = Window.partitionBy("subject").orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df = df.withColumn("running_total", F.sum("marks").over(w_running))
w_moving = Window.partitionBy("subject").orderBy("id").rowsBetween(-2, Window.currentRow)   # current + 2 previous
df = df.withColumn("moving_avg", F.avg("marks").over(w_moving))

# Aggregate over the whole partition (no orderBy → whole partition is the frame)
df = df.withColumn("subject_avg", F.avg("marks").over(Window.partitionBy("subject")))

# Nth highest salary per department
w_dept = Window.partitionBy("department").orderBy(F.col("salary").desc())
df_nth = df.withColumn("rnk", F.dense_rank().over(w_dept)).filter(F.col("rnk") == 2)

# First and last value in the partition – needs an explicit full frame
w_full = w.rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
df = df.withColumn("first_marks", F.first("marks").over(w_full))
df = df.withColumn("last_marks", F.last("marks").over(w_full))
```

**Frame gotcha (common bug):** when a window has `orderBy`, the default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. So `F.last("marks").over(w)` returns the *current* row's value, not the partition's last – always specify the frame for `last`, running and moving calculations.

**ROWS vs RANGE**
```python
Window.partitionBy("subject").orderBy("id").rowsBetween(-1, 1)        # physical rows: previous, current, next
Window.partitionBy("subject").orderBy("id").rangeBetween(-10, 10)     # rows whose id is within ±10 of the current id
# RANGE treats ties (same order value) as one group; e.g. last 7 days by date:
Window.partitionBy("user").orderBy(F.col("event_date").cast("timestamp").cast("long")).rangeBetween(-6 * 86400, 0)
```

---

## 8. Joins (very important)

```python
df1.join(df2, df1.id == df2.id, "inner")          # keeps both id columns
df1.join(df2, "id", "inner")                      # same column name → single id column
df1.join(df2, ["id", "date"], "inner")            # multiple keys
df1.join(df2, "id", "left")                       # = leftouter
df1.join(df2, "id", "right")                      # = rightouter
df1.join(df2, "id", "outer")                      # = full / fullouter
df1.join(df2, "id", "left_semi")                  # rows of df1 that have a match (only df1 columns) – like EXISTS
df1.join(df2, "id", "left_anti")                  # rows of df1 with NO match – like NOT EXISTS
df1.crossJoin(df2)                                # Cartesian product – data explosion, use with care

# Multiple / non-equi conditions
df1.join(df2, (df1.id == df2.id) & (df1.date == df2.date), "inner")
events.join(ranges, (events.ts >= ranges.start_ts) & (events.ts < ranges.end_ts))

# Avoid ambiguous duplicate columns: alias the DataFrames or rename before joining
a, b = df1.alias("a"), df2.alias("b")
a.join(b, F.col("a.id") == F.col("b.id")).select("a.*", F.col("b.name").alias("b_name"))
df1.join(df2.select(F.col("id").alias("df2_id"), "name"), F.col("id") == F.col("df2_id"), "inner")

# Null-safe join (NULL keys match each other)
df1.join(df2, df1.key.eqNullSafe(df2.key))
```
Rows with NULL join keys never match in a normal equi-join.

### Join strategies
| Strategy | When Spark uses it | Notes |
|---|---|---|
| **Broadcast hash join** | One side smaller than `spark.sql.autoBroadcastJoinThreshold` (default 10 MB) or a `broadcast()` hint | No shuffle of the big table – fastest. The broadcast side must fit in driver and executor memory |
| **Sort-merge join** | Default for two large tables | Both sides shuffled and sorted by key |
| **Shuffle hash join** | Both large, one side's partitions fit in memory (or hint) | Shuffle, no sort |
| Broadcast nested loop / Cartesian | Non-equi joins / cross joins | Can be very slow |

```python
large_df.join(F.broadcast(small_df), "id")                  # explicit hint (ignores the threshold)
large_df.join(small_df.hint("shuffle_hash"), "id")          # other hints: merge, shuffle_replicate_nl
```

---

## 9. Performance Optimization

### Cache and persist
```python
from pyspark import StorageLevel
df.cache()                                  # DataFrame default level: MEMORY_AND_DISK
df.count()                                  # an action materializes the cache
df.persist(StorageLevel.MEMORY_AND_DISK)
df.persist(StorageLevel.DISK_ONLY)
df.persist(StorageLevel.MEMORY_ONLY)        # recompute partitions that don't fit
df.is_cached; df.storageLevel
df.unpersist()
```
- Cache only DataFrames **reused** by several actions (e.g. read once, write to two places), and unpersist afterwards.
- PySpark storage levels: `MEMORY_ONLY`, `MEMORY_AND_DISK`, `MEMORY_AND_DISK_DESER`, `DISK_ONLY`, `OFF_HEAP`, plus `_2` replicated variants. (`MEMORY_ONLY_SER` exists in Scala/Java, not PySpark – Python data is always serialized.)
- `df.checkpoint()` / `localCheckpoint()` truncate a very long lineage (iterative jobs).

### Partitioning
```python
df.rdd.getNumPartitions()
df.repartition(10)                 # full shuffle → even partitions; can increase or decrease
df.repartition("subject")          # hash-partition by column (co-locate keys)
df.repartition(50, "subject")
df.coalesce(5)                     # merge partitions WITHOUT a full shuffle; only decreases
```
| | `repartition(n)` | `coalesce(n)` |
|---|---|---|
| Shuffle | Full | No (merges local partitions) |
| Direction | Up or down | Down only |
| Result | Even sizes | Possibly uneven; can reduce parallelism of earlier steps |
| Use | Before a heavy join/write, fix skew | Reduce output file count at the end |

Rules of thumb: target **~128–256 MB per partition**; at least 2–3× the total executor cores; `spark.sql.files.maxPartitionBytes` (default 128 MB) controls input split size.

### Small-files problem
Too many small files → slow listing, task overhead, slow downstream reads. Fixes: `coalesce/repartition` before writing, `maxRecordsPerFile`, `repartition(partition_cols)` before `partitionBy`, periodic compaction (`OPTIMIZE` in Delta, `rewrite_data_files` in Iceberg).

### Broadcast variables and accumulators
```python
lookup = spark.sparkContext.broadcast({"key1": "value1", "key2": "value2"})   # read-only copy per executor
def lookup_func(key):
    return lookup.value.get(key, "Not Found")

bad_rows = spark.sparkContext.accumulator(0)   # executors add, only the driver reads
# Accumulators updated inside transformations can double-count on task retries – use them for metrics only
```

### Predicate pushdown, partition pruning, column pruning
```python
# Filters on partition columns skip whole folders (partition pruning);
# filters on other columns are pushed into the Parquet reader (row-group skipping using min/max stats)
df = spark.read.parquet("s3://bucket/sales/").filter(F.col("year") == 2026).select("id", "amount")
df.explain()   # look for PartitionFilters and PushedFilters in the scan node
```
Pushdown is lost when you filter on a UDF result or on a derived expression the reader can't evaluate.

### Bucketing
```python
df.write.bucketBy(10, "id").sortBy("id").saveAsTable("bucketed_table")
```
Joining two tables bucketed on the same key with the same bucket count avoids the shuffle. Only works with tables in a catalog (`saveAsTable`), not plain paths.

### Data skew
Symptoms: one or a few tasks run much longer than the rest; a huge shuffle-read size on a few tasks in the Spark UI.

1. **AQE skew join** (`spark.sql.adaptive.skewJoin.enabled=true`) splits skewed partitions automatically – try first.
2. **Broadcast** the smaller side if possible.
3. **Salting** – spread a hot key over N sub-keys:
```python
SALT = 10
# Aggregation: two-stage
partial = (df.withColumn("salt", (F.rand() * SALT).cast("int"))
             .groupBy("key", "salt").agg(F.sum("amount").alias("amt")))
result = partial.groupBy("key").agg(F.sum("amt").alias("amount"))

# Join: salt the big side randomly, replicate the small side for every salt value
big_s   = big.withColumn("salt", (F.rand() * SALT).cast("int"))
small_s = small.crossJoin(spark.range(SALT).withColumnRenamed("id", "salt"))
joined  = big_s.join(small_s, ["key", "salt"]).drop("salt")

# String-salt variant from the original guide (add, aggregate, then strip)
df = df.withColumn("salted_key", F.concat(F.col("key"), F.lit("_"), (F.rand() * 10).cast("int")))
df = df.withColumn("key", F.regexp_replace("salted_key", r"_\d+$", ""))
```
4. Filter out or process separately null/default keys (a common hidden skew source).

### Memory and tuning checklist
- Executor memory = heap (execution + storage, unified) + `spark.executor.memoryOverhead` (Python workers, off-heap; default max(384 MB, 10%)). PySpark UDF-heavy jobs often need more overhead.
- **OOM on driver:** `collect()`/`toPandas()` on big data, large broadcast. **OOM on executor:** skew, too few partitions, huge rows/explodes.
- **Spill** (shown in Spark UI) → more partitions or more memory.
- 4–5 cores per executor is a common balance; `spark.dynamicAllocation.enabled` scales executors with load (EMR default).
- Avoid: `collect()` on large data, Python UDFs where built-ins exist, `count()` just to check emptiness (use `df.isEmpty()` 3.3+ or `df.limit(1).count()`), unnecessary `orderBy`, repeated actions on uncached DataFrames.
```python
print(spark.sparkContext.getConf().getAll())   # effective configuration
spark.conf.get("spark.sql.shuffle.partitions")
```

---

## 10. Spark SQL

```python
df.createOrReplaceTempView("temp_view")              # session-scoped
df.createOrReplaceGlobalTempView("global_view")      # app-scoped; query as global_temp.global_view
spark.sql("SELECT * FROM global_temp.global_view")

spark.sql("SELECT * FROM temp_view WHERE marks > 70")
spark.sql("""
    SELECT subject, COUNT(*) AS cnt, AVG(marks) AS avg_marks
    FROM temp_view GROUP BY subject
""")
spark.sql("""
    SELECT t1.id, t1.name, t2.subject
    FROM temp_table1 t1 INNER JOIN temp_table2 t2 ON t1.id = t2.id
""")
spark.sql("""
    SELECT * FROM (
        SELECT name, marks,
               ROW_NUMBER() OVER (PARTITION BY subject ORDER BY marks DESC) AS rn
        FROM temp_view) t
    WHERE rn = 1            -- Databricks SQL also supports QUALIFY rn = 1
""")
spark.sql("""
    WITH filtered_data AS (SELECT * FROM temp_view WHERE marks > 60)
    SELECT subject, COUNT(*) AS cnt FROM filtered_data GROUP BY subject
""")

# Create a table from a query
spark.sql("CREATE TABLE my_table USING parquet AS SELECT * FROM temp_view")
# CREATE OR REPLACE TABLE ... requires a table format that supports it (Delta / Iceberg)

# Parameterized SQL (3.4+) – avoids string concatenation / SQL injection
spark.sql("SELECT * FROM temp_view WHERE marks > :min_marks", args={"min_marks": 70})
```
DataFrame API and SQL compile to the same plan – performance is identical.

---

## 11. UDFs

Order of preference: **built-in functions → SQL expressions → pandas UDF → Python UDF.**
Python UDFs serialize every row between the JVM and a Python worker and are opaque to Catalyst (no pushdown).

```python
@F.udf(StringType())
def get_grade(marks):
    if marks is None:                 # always handle NULLs in UDFs
        return None
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    return "C"

df = df.withColumn("grade", get_grade(F.col("marks")))

# Built-in equivalent (preferred – no UDF at all)
df = df.withColumn("grade", F.when(F.col("marks") >= 80, "A").when(F.col("marks") >= 60, "B")
                             .when(F.col("marks").isNotNull(), "C"))

# Pandas (vectorized) UDF – processes Arrow batches, much faster than a row UDF
import pandas as pd, numpy as np

@F.pandas_udf(StringType())
def get_grade_pandas(s: pd.Series) -> pd.Series:
    out = np.select([s >= 80, s >= 60, s.notna()], ["A", "B", "C"], default=None)
    return pd.Series(out, dtype="object")

df = df.withColumn("grade", get_grade_pandas("marks"))

# Multiple inputs
@F.udf(StringType())
def categorize(marks, subject):
    if marks is not None and marks >= 80 and subject == "Math":
        return "Top Math Student"
    if marks is not None and marks >= 80:
        return "Top Student"
    return "Regular Student"

df = df.withColumn("category", categorize("marks", "subject"))

# Register for SQL
spark.udf.register("get_grade_sql", get_grade)
spark.sql("SELECT name, marks, get_grade_sql(marks) AS grade FROM temp_view")
```

**Custom aggregate in PySpark** – `UserDefinedAggregateFunction` is a Scala/Java API (and deprecated); in Python use a Series → scalar pandas UDF:
```python
@F.pandas_udf(DoubleType())
def mean_udf(v: pd.Series) -> float:
    return float(v.mean()) if len(v) else None

df.groupBy("subject").agg(mean_udf("marks").alias("avg_marks"))
spark.udf.register("mean_udf", mean_udf)
```
Group-wise pandas logic: `df.groupBy("key").applyInPandas(func, schema=...)`.

---

## 12. RDD Operations

```python
sc = spark.sparkContext
rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd_from_file = sc.textFile("path/to/file.txt")

# Transformations (lazy)
rdd.map(lambda x: x * 2)
rdd.filter(lambda x: x > 2)
rdd.flatMap(lambda x: [x, x * 2])          # one input → many outputs
rdd.distinct()
rdd1.union(rdd2)

# Word count (classic)
word_counts = (sc.textFile("path/to/file.txt")
               .flatMap(lambda line: line.split())
               .map(lambda w: (w.lower(), 1))
               .reduceByKey(lambda a, b: a + b))

# Key-value operations need a PAIR RDD of (key, value) tuples
pairs = sc.parallelize([("a", 1), ("b", 2), ("a", 3)])
pairs.reduceByKey(lambda a, b: a + b)       # combines on each partition before the shuffle → preferred
pairs.groupByKey().mapValues(list)          # ships every value over the network → avoid for aggregations
pairs.sortByKey()
pairs.mapValues(lambda v: v * 10)

# Actions (trigger execution)
rdd.collect(); rdd.count(); rdd.take(5); rdd.first()
rdd.reduce(lambda a, b: a + b)
rdd.saveAsTextFile("path/to/output")

# RDD ↔ DataFrame
df = rdd.map(lambda x: (x,)).toDF(["value"])   # rows must be tuples/Row objects
rdd_rows = df.rdd                              # RDD of Row objects
```
`reduceByKey` vs `groupByKey` is a classic question: `reduceByKey` does a map-side combine, so far less data is shuffled.

---

## 13. Data Validation and Quality Checks

```python
# Nulls per column (one pass)
df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in df.columns]).show()

# NaN check (only for float/double columns)
float_cols = [f.name for f in df.schema.fields if isinstance(f.dataType, (FloatType, DoubleType))]
df.select([F.count(F.when(F.isnan(c), c)).alias(c) for c in float_cols]).show()

# Duplicates
duplicate_count = df.count() - df.dropDuplicates().count()
df.groupBy(df.columns).count().filter(F.col("count") > 1).show()          # full-row duplicates
df.groupBy("id").count().filter("count > 1").show()                        # duplicate keys

# Business rules
invalid_marks = df.filter((F.col("marks") < 0) | (F.col("marks") > 100)).count()
invalid_emails = df.filter(~F.col("email").rlike(r"^[\w.-]+@[\w.-]+\.\w+$")).count()
orphan_records = fact.join(dim, "foreign_key", "left_anti").count()        # referential integrity

# Completeness % per column
total = df.count()
completeness = df.select([(F.count(c) / F.lit(total) * 100).alias(c) for c in df.columns])   # count(c) ignores nulls

# Schema validation (compare names and types; == also compares nullability)
expected = {"id": IntegerType(), "name": StringType(), "marks": IntegerType()}
actual = {f.name: f.dataType for f in df.schema.fields}
missing  = expected.keys() - actual.keys()
mismatch = {c for c in expected.keys() & actual.keys() if expected[c] != actual[c]}
if missing or mismatch:
    raise ValueError(f"Schema mismatch | missing={missing}, type_mismatch={mismatch}")
```
Pattern: split into `valid_df` and `quarantine_df` (with a reason column), write both, and fail the job if the bad ratio exceeds a threshold. Tools: Great Expectations, Deequ/PyDeequ, Glue Data Quality, Delta constraints / DLT expectations.

---

## 14. Error Handling and Logging

```python
from pyspark.errors import AnalysisException          # Spark 3.4+; older: from pyspark.sql.utils import AnalysisException

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

try:
    df = spark.read.parquet("s3://bucket/missing/")     # "Path does not exist" → AnalysisException
except AnalysisException as e:
    logger.error("Read failed: %s", e)
    raise                                               # fail the job; don't silently continue with empty data

try:
    result = df.agg(F.sum("non_existent_column"))      # unresolved column fails at analysis time (immediately)
except AnalysisException as e:
    logger.error("Analysis error: %s", e)

def validate_and_process(df, required_columns):
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    null_counts = df.select([F.count(F.when(F.col(c).isNull(), c)).alias(c) for c in required_columns]).first().asDict()
    logger.info("Null counts: %s", null_counts)
    df_processed = df.dropDuplicates().na.drop(subset=required_columns)
    return df_processed
```
Key point: because of lazy evaluation, **runtime** errors (bad cast in ANSI mode, UDF exceptions, missing files at read time, OOM) surface at the **action**, not on the line that defined the transformation – wrap the action/write in the `try`.

---

## 15. AWS Integration (S3, Glue, EMR)

### boto3 with Spark jobs
```python
import boto3
s3 = boto3.client("s3")
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="my-bucket", Prefix="path/"):   # >1,000 keys
    for obj in page.get("Contents", []):
        print(obj["Key"])
s3.upload_file("local_file.txt", "my-bucket", "remote_file.txt")
s3.download_file("my-bucket", "remote_file.txt", "local_file.txt")
s3.delete_object(Bucket="my-bucket", Key="file.txt")

df = spark.read.parquet("s3://my-bucket/path/to/data/")
df.write.mode("overwrite").parquet("s3://my-bucket/path/to/output/")
```
Use boto3 on the driver for control-plane tasks (listing, moving markers); use Spark for reading/writing data.

### AWS Glue
```python
import sys
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from awsglue.transforms import ApplyMapping, ResolveChoice, DropFields, Filter
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)                      # required for job bookmarks

# From the Glue Data Catalog (transformation_ctx is required for bookmarks)
dyf = glueContext.create_dynamic_frame.from_catalog(
    database="my_database", table_name="my_table", transformation_ctx="src_orders",
    push_down_predicate="year='2026' AND month='10'")   # partition pruning at read time

# From S3
dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3", connection_options={"paths": ["s3://my-bucket/path/"]}, format="json")

df = dyf.toDF()                                        # DynamicFrame → DataFrame
dyf2 = DynamicFrame.fromDF(df, glueContext, "dyf2")    # DataFrame → DynamicFrame

mapped = ApplyMapping.apply(frame=dyf, mappings=[
    ("old_col1", "string", "new_col1", "string"),
    ("old_col2", "int", "new_col2", "long")])
resolved = ResolveChoice.apply(frame=dyf, choice="cast:long")                  # resolve all ambiguous types
resolved = ResolveChoice.apply(frame=dyf, specs=[("price", "cast:double")])   # per column
resolved = ResolveChoice.apply(frame=dyf, choice="match_catalog",
                               database="my_database", table_name="my_table")  # use catalog types
dropped  = DropFields.apply(frame=dyf, paths=["column_to_drop"])
filtered = Filter.apply(frame=dyf, f=lambda r: r["age"] > 30)

glueContext.write_dynamic_frame.from_options(
    frame=mapped, connection_type="s3",
    connection_options={"path": "s3://my-bucket/output/", "partitionKeys": ["year", "month"]},
    format="parquet")

job.commit()                                           # saves the bookmark state
```
**DynamicFrame vs DataFrame:** a DynamicFrame tolerates inconsistent schemas (a field can be a "choice" of types) and integrates with the Glue Catalog and bookmarks; a DataFrame has a fixed schema and the full Spark API. Common practice: read with DynamicFrame, convert with `toDF()`, transform with the DataFrame API.

**Job bookmarks** (incremental processing): Glue remembers which S3 files (or which JDBC key values) were already processed. Requires bookmarks enabled on the job, `job.init`, a `transformation_ctx` on sources, and `job.commit()`.
```python
glueContext.create_dynamic_frame.from_catalog(
    database="my_db", table_name="orders", transformation_ctx="orders",
    additional_options={"jobBookmarkKeys": ["order_id"], "jobBookmarkKeysSortOrder": "asc"})   # JDBC sources
```

**EMR:** run with `spark-submit` as an EMR step; use EMRFS `s3://` paths; enable dynamic allocation; spot instances for task nodes.

---

## 15a. Snowflake with PySpark and Running SQL Scripts

### Snowflake Spark connector – setup
Needs two JARs matching your Spark/Scala version: `spark-snowflake_2.12` and `snowflake-jdbc` (EMR: `--packages`; Glue: `--extra-jars`, or Glue 4.0+ native Snowflake connection).
```python
import json, boto3

secret = json.loads(boto3.client("secretsmanager")
                    .get_secret_value(SecretId="prod/snowflake/etl")["SecretString"])

sf_options = {
    "sfURL":       "myorg-myaccount.snowflakecomputing.com",
    "sfUser":      secret["user"],
    "pem_private_key": secret["private_key"],   # key-pair auth (key body without BEGIN/END lines); or "sfPassword"
    "sfRole":      "DATA_ENGINEER",
    "sfWarehouse": "TRANSFORM_WH",
    "sfDatabase":  "SALES_DB",
    "sfSchema":    "CURATED",
}
SF = "net.snowflake.spark.snowflake"            # short name "snowflake" also works on Databricks/Glue
```
Never hardcode credentials – read them from Secrets Manager (or a Glue connection).

### Read from Snowflake
```python
# Whole table
df = spark.read.format(SF).options(**sf_options).option("dbtable", "ORDERS").load()

# SQL query – executed IN Snowflake, only the result comes to Spark
df = (spark.read.format(SF).options(**sf_options)
      .option("query", """
          SELECT order_id, customer_id, amount, order_date
          FROM SALES_DB.CURATED.ORDERS
          WHERE order_date >= DATEADD(day, -7, CURRENT_DATE())
      """)
      .load())

# Filters/aggregations written in Spark are also pushed down to Snowflake ("autopushdown", on by default)
df.filter(F.col("AMOUNT") > 100).groupBy("CUSTOMER_ID").agg(F.sum("AMOUNT")).show()
```
Snowflake returns unquoted column names in UPPERCASE – reference them as `"AMOUNT"`, not `"amount"`.

### Write to Snowflake
```python
(df.write.format(SF).options(**sf_options)
   .option("dbtable", "STG_ORDERS")
   .mode("append")                       # append | overwrite | errorifexists | ignore
   .save())

# Overwrite drops and recreates the table by default; keep the table definition and grants with:
(df.write.format(SF).options(**sf_options)
   .option("dbtable", "STG_ORDERS")
   .option("truncate_table", "on")       # truncate instead of drop/recreate
   .option("usestagingtable", "on")      # load into a temp table, then swap → target untouched if the load fails
   .mode("overwrite").save())
```
Under the hood the connector stages data (internal stage or S3) and runs `COPY INTO`, so writes are bulk loads.

### Run DDL/DML in Snowflake from PySpark (no DataFrame returned)
```python
# Utils.runQuery executes any statement (CREATE, MERGE, CALL, TRUNCATE ...) in Snowflake
sf_utils = spark.sparkContext._jvm.net.snowflake.spark.snowflake.Utils
sf_utils.runQuery(sf_options, "TRUNCATE TABLE IF EXISTS SALES_DB.STAGE.STG_ORDERS")
sf_utils.runQuery(sf_options, """
    MERGE INTO SALES_DB.CURATED.ORDERS t
    USING SALES_DB.STAGE.STG_ORDERS s ON t.order_id = s.order_id
    WHEN MATCHED THEN UPDATE SET t.amount = s.amount
    WHEN NOT MATCHED THEN INSERT (order_id, amount) VALUES (s.order_id, s.amount)
""")
sf_utils.runQuery(sf_options, "CALL SALES_DB.CURATED.SP_PROCESS_ORDERS()")
```
Typical ELT pattern: Spark writes the batch to a staging table → `runQuery` runs the MERGE inside Snowflake (pushes the heavy work to Snowflake compute).

### Read a SQL script from S3
```python
import boto3
from string import Template

def read_sql_from_s3(bucket: str, key: str) -> str:
    obj = boto3.client("s3").get_object(Bucket=bucket, Key=key)
    return obj["Body"].read().decode("utf-8")

# Spark-only alternative (no boto3): whole file as one row
sql_text = spark.read.text("s3://code-bucket/sql/daily_orders.sql", wholetext=True).first()[0]

sql_text = read_sql_from_s3("code-bucket", "sql/daily_orders.sql")

# Substitute ${placeholders} – safe_substitute leaves unknown ${...} untouched
params = {"db_nm": "SALES_DB", "schema_nm": "CURATED", "run_date": "2026-10-29"}
sql_text = Template(sql_text).safe_substitute(params)
```
Only substitute trusted values (config, not user input) – string substitution in SQL is a SQL-injection risk.

### Run a SQL query or script directly
```python
# 1. Single SELECT from the S3 file → run in Snowflake, get a DataFrame
df = spark.read.format(SF).options(**sf_options).option("query", sql_text).load()

# 2. Multi-statement script → run each statement in Snowflake
def split_sql(script: str):
    # Simple splitter: assumes ';' never appears inside strings/procedure bodies.
    return [s.strip() for s in script.split(";") if s.strip()]

for stmt in split_sql(sql_text):
    logger.info("Running: %s", stmt[:100])
    sf_utils.runQuery(sf_options, stmt)

# 3. Script against Spark tables (Glue Catalog / Hive / temp views) → spark.sql per statement
for stmt in split_sql(sql_text):
    result = spark.sql(stmt)          # spark.sql runs ONE statement per call
result.show()                         # last statement's result (if it was a SELECT)
```

**Python connector alternative** (no Spark needed – good for control steps, procedures, or scripts with `;` inside procedure bodies):
```python
import snowflake.connector

with snowflake.connector.connect(
        account="myorg-myaccount", user=secret["user"], private_key_file="/tmp/rsa_key.p8",
        role="DATA_ENGINEER", warehouse="TRANSFORM_WH", database="SALES_DB", schema="CURATED") as conn:
    for cursor in conn.execute_string(sql_text):      # runs every statement in the script
        logger.info("Rows affected: %s", cursor.rowcount)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM ORDERS WHERE order_date = %s", ("2026-10-29",))   # bind variables
    print(cur.fetchone()[0])
```

**Interview points**
- `query` / `autopushdown` push work into Snowflake – don't pull a whole table into Spark just to filter it.
- `spark.sql()` runs one statement against **Spark** tables; Snowflake statements go through the connector (`runQuery`) or the Python connector.
- Load to a staging table, then MERGE in Snowflake → idempotent and transactional.
- Store SQL in S3/Git, parameterize with `${placeholders}`, log the resolved SQL, and fetch credentials from Secrets Manager.

---

## 16. Delta Lake, Incremental Loads and SCD

```python
from delta.tables import DeltaTable

spark = (SparkSession.builder.appName("DeltaLakeExample")
         .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
         .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
         .getOrCreate())                          # plus the delta-spark package on the classpath

path = "/path/to/delta/table"
df.write.format("delta").mode("overwrite").save(path)
df_delta = spark.read.format("delta").load(path)

# Upsert (MERGE)
target = DeltaTable.forPath(spark, path)
(target.alias("t")
   .merge(new_data.alias("s"), "t.id = s.id")
   .whenMatchedUpdateAll()
   .whenNotMatchedInsertAll()
   .execute())
# Dedupe new_data by id first – several source rows matching one target row makes MERGE fail

# Time travel and history
spark.read.format("delta").option("versionAsOf", 1).load(path)
spark.read.format("delta").option("timestampAsOf", "2026-10-01").load(path)
spark.sql(f"DESCRIBE HISTORY delta.`{path}`")
spark.sql(f"RESTORE TABLE delta.`{path}` TO VERSION AS OF 5")

# Maintenance
spark.sql(f"OPTIMIZE delta.`{path}`")                    # compact small files
spark.sql(f"OPTIMIZE delta.`{path}` ZORDER BY (id)")     # compact + co-locate data by id for data skipping
spark.sql(f"VACUUM delta.`{path}` RETAIN 168 HOURS")     # delete unreferenced files (default 7 days; limits time travel)

# Schema evolution on write
df.write.format("delta").mode("append").option("mergeSchema", "true").save(path)
```
Delta = Parquet files + a `_delta_log` transaction log → ACID writes, MERGE/UPDATE/DELETE, time travel, schema enforcement. **Iceberg** and **Hudi** provide similar features (Iceberg is common on AWS with Glue/Athena/EMR).

### Incremental load (high-watermark)
```python
last_wm = target_df.agg(F.max("updated_at")).first()[0] or "1900-01-01"   # no count() needed; empty → None
incremental_df = source_df.filter(F.col("updated_at") > F.lit(last_wm))
incremental_df.write.mode("append").parquet("/path/to/target/")
```
Make it idempotent: store the watermark in a control table only after a successful write, and prefer MERGE over append when the same rows can arrive again (late or re-sent data).

### SCD Type 2 with Delta MERGE
```python
# 1. Add effective dates and current flag to the incoming data
updates = (src.withColumn("effective_from", F.current_date())
              .withColumn("effective_to", F.lit("9999-12-31").cast("date"))
              .withColumn("is_current", F.lit(True)))

dim = DeltaTable.forPath(spark, dim_path)
current = dim.toDF().filter("is_current")

# 2. Rows whose tracked attributes changed → need a new version
changed = (updates.alias("s").join(current.alias("t"), "customer_id")
           .filter("s.row_hash <> t.row_hash").select("s.*"))

# 3. NULL merge_key rows never match → they are inserted as new versions;
#    real keys match → expire the current row (or insert brand-new customers)
staged = (changed.withColumn("merge_key", F.lit(None).cast("int"))
          .unionByName(updates.withColumn("merge_key", F.col("customer_id"))))

(dim.alias("t").merge(staged.alias("s"), "t.customer_id = s.merge_key AND t.is_current")
    .whenMatchedUpdate(condition="t.row_hash <> s.row_hash",
                       set={"is_current": "false", "effective_to": "current_date()"})
    .whenNotMatchedInsert(values={
        "customer_id": "s.customer_id", "name": "s.name", "city": "s.city", "row_hash": "s.row_hash",
        "effective_from": "s.effective_from", "effective_to": "s.effective_to", "is_current": "true"})
    .execute())
```
SCD Type 1 = simple MERGE that overwrites (`whenMatchedUpdateAll`).

---

## 17. Structured Streaming

A stream is treated as an **unbounded table**; Spark processes it in micro-batches with the same DataFrame API.

```python
# Socket source (demo only)
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
words = lines.select(F.explode(F.split("value", " ")).alias("word"))
query = (words.groupBy("word").count()
         .writeStream.outputMode("complete").format("console").start())
query.awaitTermination()

# Kafka → Parquet (needs the spark-sql-kafka package)
event_schema = "event_id STRING, user_id STRING, amount DOUBLE, event_ts TIMESTAMP"
df_kafka = (spark.readStream.format("kafka")
            .option("kafka.bootstrap.servers", "broker:9092")
            .option("subscribe", "topic_name")
            .option("startingOffsets", "latest")
            .load())
df_parsed = (df_kafka.select(F.from_json(F.col("value").cast("string"), event_schema).alias("data"))
             .select("data.*"))

query = (df_parsed.writeStream.format("parquet")
         .option("path", "/path/to/output")
         .option("checkpointLocation", "/path/to/checkpoint")   # offsets + state → exactly-once file output
         .trigger(processingTime="1 minute")                     # or availableNow=True for incremental batch runs
         .start())

# Windowed aggregation with a watermark (bounds state, handles late data)
agg = (df_parsed.withWatermark("event_ts", "10 minutes")
       .groupBy(F.window("event_ts", "5 minutes"), "user_id")
       .agg(F.sum("amount").alias("total")))

# foreachBatch – reuse batch code (e.g. MERGE into Delta) per micro-batch
def upsert(batch_df, batch_id):
    batch_df.dropDuplicates(["event_id"]).createOrReplaceTempView("updates")
    batch_df.sparkSession.sql("MERGE INTO events t USING updates s ON t.event_id = s.event_id "
                              "WHEN MATCHED THEN UPDATE SET * WHEN NOT MATCHED THEN INSERT *")
df_parsed.writeStream.foreachBatch(upsert).option("checkpointLocation", "/chk/events").start()
```
| Output mode | Meaning |
|---|---|
| `append` | Only new rows (default; aggregations need a watermark) |
| `update` | Only rows that changed since the last trigger |
| `complete` | Whole result table every trigger (aggregations only) |

Key facts: the **checkpoint** stores offsets and state – never share it between queries; deleting it restarts the stream. End-to-end exactly-once requires a replayable source (Kafka/files), checkpointing, and an idempotent or transactional sink (files, Delta, `foreachBatch` with MERGE).

---

## 18. Common Interview Problems

```python
# Q1. Employees earning more than their department average
w_dept = Window.partitionBy("department")
df.withColumn("dept_avg", F.avg("salary").over(w_dept)).filter(F.col("salary") > F.col("dept_avg"))

# Q2. Top N per group (row_number = exactly N; dense_rank = include ties)
w = Window.partitionBy("category").orderBy(F.col("sales").desc())
df.withColumn("rn", F.row_number().over(w)).filter(F.col("rn") <= 3)

# Q3. Running total
w_run = Window.partitionBy("user_id").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn("running_total", F.sum("amount").over(w_run))

# Q4. Consecutive login days (gaps and islands)
w_user = Window.partitionBy("user_id").orderBy("login_date")
streaks = (df.select("user_id", "login_date").distinct()
           .withColumn("grp", F.date_sub("login_date", F.row_number().over(w_user)))   # same grp = consecutive
           .groupBy("user_id", "grp")
           .agg(F.min("login_date").alias("start"), F.max("login_date").alias("end"), F.count("*").alias("days")))
streaks.filter(F.col("days") >= 3)
# Simpler variant: lag + datediff marks breaks
df.withColumn("prev_date", F.lag("login_date").over(w_user)) \
  .withColumn("days_diff", F.datediff("login_date", "prev_date"))

# Q5. Pivot
df.groupBy("student").pivot("subject").agg(F.sum("marks"))

# Q6. Skewed key → AQE skew join, broadcast, or salting (section 9)
df.withColumn("salted_key", F.concat(F.col("key"), F.lit("_"), (F.rand() * 10).cast("int")))

# Q7. Deduplicate keeping the latest record
w_latest = Window.partitionBy("id").orderBy(F.col("timestamp").desc())
df.withColumn("rn", F.row_number().over(w_latest)).filter("rn = 1").drop("rn")

# Q8. Percentage contribution
total_sales = df.agg(F.sum("sales")).first()[0]
df.withColumn("pct", F.col("sales") / F.lit(total_sales) * 100)
df.withColumn("pct", F.col("sales") / F.sum("sales").over(Window.partitionBy()) * 100)   # no collect (single partition)
df.withColumn("pct_in_region", F.col("sales") / F.sum("sales").over(Window.partitionBy("region")) * 100)

# Q9. Gaps in a sequence
df.withColumn("next_id", F.lead("id").over(Window.orderBy("id"))) \
  .filter(F.col("next_id") - F.col("id") > 1) \
  .select(F.col("id").alias("gap_after"), "next_id")

# Q10. Cumulative sum per group, and cumulative sum that RESETS when a flag is set
w_g = Window.partitionBy("group").orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn("cumulative_sum", F.sum("value").over(w_g))
df_reset = (df.withColumn("seg", F.sum(F.when(F.col("reset_flag"), 1).otherwise(0)).over(w_g))   # new segment at each reset
              .withColumn("cum_with_reset", F.sum("value").over(
                  Window.partitionBy("group", "seg").orderBy("date")
                        .rowsBetween(Window.unboundedPreceding, Window.currentRow))))

# Q11. Duplicate transactions by business rule (same customer + amount, keep first)
w_dup = Window.partitionBy("customer_id", "amount").orderBy("timestamp")
df.withColumn("rn", F.row_number().over(w_dup)).filter(F.col("rn") > 1)

# Q12. Unpivot (columns → rows)
id_cols = ["student_id"]
value_cols = [c for c in df.columns if c not in id_cols]
unpivoted = (df.select("student_id",
                       F.explode(F.array(*[F.struct(F.lit(c).alias("subject"), F.col(c).alias("marks"))
                                           for c in value_cols])).alias("d"))
               .select("student_id", "d.subject", "d.marks"))
unpivoted = df.unpivot(id_cols, value_cols, "subject", "marks")        # 3.4+ (alias: melt)
unpivoted = df.selectExpr("student_id",
    "stack(2, 'Math', Math, 'Science', Science) AS (subject, marks)")   # SQL stack()

# Q13. Second highest salary overall
(df.withColumn("rnk", F.dense_rank().over(Window.orderBy(F.col("salary").desc())))
   .filter("rnk = 2").select("salary").distinct())

# Q14. Customers who bought in every month of the year
months = df.select(F.month("order_date").alias("m")).distinct().count()
df.groupBy("customer_id").agg(F.countDistinct(F.month("order_date")).alias("m")).filter(F.col("m") == months)

# Q15. Compare two snapshots: inserted / deleted / changed rows
inserted = new.join(old, "id", "left_anti")
deleted  = old.join(new, "id", "left_anti")
changed  = (new.alias("n").join(old.alias("o"), "id")
            .filter(F.sha2(F.concat_ws("||", *[F.col(f"n.{c}") for c in cols]), 256) !=
                    F.sha2(F.concat_ws("||", *[F.col(f"o.{c}") for c in cols]), 256))
            .select("n.*"))

# Q16. Flatten nested JSON / struct columns automatically
def flatten(df):
    flat = []
    for f in df.schema.fields:
        if isinstance(f.dataType, StructType):
            flat += [F.col(f"{f.name}.{c.name}").alias(f"{f.name}_{c.name}") for c in f.dataType.fields]
        else:
            flat.append(F.col(f.name))
    out = df.select(flat)
    return flatten(out) if any(isinstance(f.dataType, StructType) for f in out.schema.fields) else out

# Q17. Sessionize clickstream (new session after 30 min of inactivity)
w_u = Window.partitionBy("user_id").orderBy("event_ts")
sessions = (df.withColumn("gap", F.col("event_ts").cast("long") - F.lag("event_ts").over(w_u).cast("long"))
              .withColumn("new_session", F.when(F.col("gap").isNull() | (F.col("gap") > 1800), 1).otherwise(0))
              .withColumn("session_id", F.sum("new_session").over(w_u.rowsBetween(Window.unboundedPreceding, 0))))
```

---

## 19. Quick Q&A

- **Transformation vs action?** Transformations are lazy and return a DataFrame; actions (`count`, `collect`, `show`, `write`) trigger execution.
- **What causes a shuffle?** Wide operations: `groupBy`, non-broadcast `join`, `distinct`, `orderBy`, `repartition`, windows with `partitionBy`.
- **repartition vs coalesce?** Full shuffle with even partitions vs merging partitions without a shuffle (decrease only).
- **cache vs persist?** `cache()` = `persist()` with the default level (MEMORY_AND_DISK for DataFrames); `persist` lets you choose the level.
- **Why is my job slow?** Check the Spark UI: skewed tasks, large shuffles, spill, too many/too few partitions, small files, Python UDFs, repeated recomputation of uncached data.
- **How does Spark recover from failures?** Recomputes lost partitions from lineage; failed tasks are retried (`spark.task.maxFailures`, default 4).
- **What is AQE?** Runtime re-optimization using shuffle statistics: coalesce partitions, switch join strategy, split skewed partitions.
- **What is predicate pushdown?** Filters are applied by the data source (Parquet row groups, JDBC WHERE, partition folders) so less data is read.
- **`collect()` vs `take()` vs `show()`?** `collect` brings all rows to the driver (OOM risk); `take(n)`/`show(n)` bring only n rows.
- **Client vs cluster mode?** Driver on the submitting machine vs inside the cluster.
- **How do you handle schema evolution?** Explicit schemas + `mergeSchema` for Parquet/Delta, Glue `ResolveChoice`, VARIANT/raw JSON landing, and alerting on unexpected columns.
- **How do you test PySpark code?** `pytest` with a local `SparkSession` fixture, small in-memory DataFrames, and DataFrame equality helpers (`pyspark.testing.assertDataFrameEqual` 3.5+, or chispa).
- **Explain a Spark job end to end.** `spark-submit` → driver starts → cluster manager launches executors → action creates a job → DAG scheduler splits stages at shuffles → task scheduler sends one task per partition → executors run tasks, write shuffle files → next stage reads them → results returned or written.
