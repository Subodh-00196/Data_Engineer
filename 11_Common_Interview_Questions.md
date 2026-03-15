# Common Data Engineer Interview Questions & Answers

## Table of Contents
1. [Conceptual Questions](#conceptual-questions)
2. [SQL Questions](#sql-questions)
3. [PySpark Questions](#pyspark-questions)
4. [Python Questions](#python-questions)
5. [Cloud & AWS Questions](#cloud--aws-questions)
6. [Data Modeling Questions](#data-modeling-questions)
7. [ETL/ELT Questions](#etlelt-questions)
8. [Performance & Optimization](#performance--optimization)
9. [Scenario-Based Questions](#scenario-based-questions)

---

## Conceptual Questions

### 1. What is the difference between Data Lake and Data Warehouse?

**Data Lake:**
- Stores raw, unstructured, semi-structured, and structured data
- Schema-on-read (schema applied when reading)
- Cheaper storage (object storage like S3)
- Used for big data, ML, data science
- Examples: AWS S3, Azure Data Lake, Google Cloud Storage

**Data Warehouse:**
- Stores processed, structured data
- Schema-on-write (schema defined before loading)
- Optimized for analytics and BI
- More expensive storage
- Examples: Snowflake, Redshift, BigQuery

### 2. Explain ACID Properties

- **Atomicity**: All or nothing - transaction either completes fully or not at all
- **Consistency**: Database remains in valid state before and after transaction
- **Isolation**: Concurrent transactions don't interfere with each other
- **Durability**: Committed changes are permanent, survive system failures

### 3. What is CAP Theorem?

CAP Theorem states that a distributed system can only guarantee 2 out of 3:
- **Consistency**: All nodes see the same data at the same time
- **Availability**: Every request receives a response
- **Partition Tolerance**: System continues despite network partitions

### 4. ETL vs ELT - What's the difference?

**ETL (Extract, Transform, Load):**
- Transform data before loading
- Traditional approach
- Used when target system has limited compute
- Example: Load from OLTP to Data Warehouse

**ELT (Extract, Load, Transform):**
- Load raw data first, transform later
- Modern approach with cloud data warehouses
- Leverages warehouse compute power
- More flexible, supports data lake architecture

### 5. What is Data Partitioning?

Partitioning divides large tables into smaller, manageable pieces based on column values (usually date).

**Benefits:**
- Improved query performance (partition pruning)
- Easier data management
- Parallel processing
- Faster data loading/deletion

**Example:** Partition sales table by year and month

### 6. Explain Star Schema vs Snowflake Schema

**Star Schema:**
- Fact table in center, dimension tables around it
- Denormalized dimensions
- Simpler queries, better performance
- More storage due to redundancy

**Snowflake Schema:**
- Normalized dimension tables
- Dimensions split into multiple related tables
- Less storage, more complex queries
- Better for data integrity

### 7. What are Slowly Changing Dimensions (SCD)?

Methods to track historical changes in dimension tables:

- **Type 0**: Fixed, never changes
- **Type 1**: Overwrite (no history)
- **Type 2**: Add new row (full history)
- **Type 3**: Add new column (limited history)
- **Type 4**: Separate history table
- **Type 6**: Hybrid (1+2+3)

---

## SQL Questions

### 1. Find Nth Highest Salary

```sql
-- Method 1: Using DENSE_RANK
SELECT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) ranked
WHERE rank = 2;

-- Method 2: Using subquery
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### 2. Find Duplicate Records

```sql
SELECT name, email, COUNT(*) as count
FROM employees
GROUP BY name, email
HAVING COUNT(*) > 1;
```

### 3. Delete Duplicates Keeping One Record

```sql
DELETE FROM employees
WHERE id NOT IN (
    SELECT MIN(id)
    FROM employees
    GROUP BY name, email
);
```

### 4. Running Total

```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales;
```

### 5. Find Employees with No Manager

```sql
SELECT e1.name AS employee
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id
WHERE e2.id IS NULL AND e1.manager_id IS NOT NULL;
```

---

## PySpark Questions

### 1. Explain Transformations vs Actions

**Transformations** (Lazy):
- Create new RDD/DataFrame from existing one
- Not executed immediately
- Examples: map, filter, select, join, groupBy

**Actions** (Eager):
- Trigger execution of transformations
- Return results to driver or write to storage
- Examples: collect, count, show, save

### 2. What is the difference between cache() and persist()?

- `cache()`: Stores data in memory with default storage level (MEMORY_ONLY)
- `persist()`: Allows custom storage level (MEMORY_ONLY, MEMORY_AND_DISK, DISK_ONLY, etc.)

### 3. Explain Broadcast Join

- Small table broadcasted to all executor nodes
- Avoids shuffle of large table
- Used when one table is small (< 10MB)
- Significantly improves performance

```python
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_df), "key")
```

### 4. What is Spark Lineage?

- DAG (Directed Acyclic Graph) of transformations
- Tracks how RDD/DataFrame was created
- Used for fault tolerance (recompute lost partitions)
- Can be viewed with `.toDebugString()`

### 5. Repartition vs Coalesce

- **Repartition**: Full shuffle, can increase or decrease partitions
- **Coalesce**: No full shuffle, only decrease partitions, more efficient

---

## Python Questions

### 1. Explain List Comprehension

```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
```

### 2. What is the difference between list and tuple?

**List:**
- Mutable (can be modified)
- Uses square brackets []
- Slower than tuple
- More memory

**Tuple:**
- Immutable (cannot be modified)
- Uses parentheses ()
- Faster than list
- Less memory

### 3. Explain *args and **kwargs

```python
def function(*args, **kwargs):
    # *args: variable number of positional arguments (tuple)
    # **kwargs: variable number of keyword arguments (dict)
    pass

function(1, 2, 3, name="John", age=30)
# args = (1, 2, 3)
# kwargs = {'name': 'John', 'age': 30}
```

### 4. What is a Generator?

- Function that yields values one at a time
- Memory efficient for large datasets
- Uses `yield` instead of `return`

```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

---

## Cloud & AWS Questions

### 1. What is AWS Glue?

- Fully managed ETL service
- Serverless, pay per use
- Components:
  - **Crawlers**: Discover schema and create metadata
  - **Data Catalog**: Central metadata repository
  - **Jobs**: ETL scripts (Python/Scala)
  - **Triggers**: Schedule or event-based execution

### 2. Explain DynamicFrame vs DataFrame

**DynamicFrame** (AWS Glue):
- Handles schema variations
- Self-describing
- Better for semi-structured data
- Glue-specific

**DataFrame** (Spark):
- Fixed schema
- Better performance
- Standard Spark API

### 3. What is S3 and its storage classes?

S3 is object storage service. Storage classes:
- **S3 Standard**: Frequent access
- **S3 Intelligent-Tiering**: Automatic cost optimization
- **S3 Standard-IA**: Infrequent access
- **S3 Glacier**: Archive, retrieval in minutes/hours
- **S3 Glacier Deep Archive**: Long-term archive, 12-hour retrieval

### 4. What is Lambda and when to use it?

- Serverless compute service
- Event-driven execution
- Pay per invocation
- Use cases:
  - Trigger Glue jobs on S3 upload
  - Data transformation
  - API backends
  - Scheduled tasks

---

## Data Modeling Questions

### 1. What is Normalization?

Process of organizing data to reduce redundancy:

- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies
- **3NF**: 2NF + no transitive dependencies
- **BCNF**: Every determinant is a candidate key

### 2. Fact Table vs Dimension Table

**Fact Table:**
- Contains measurable, quantitative data
- Foreign keys to dimension tables
- Large, grows quickly
- Example: Sales transactions

**Dimension Table:**
- Contains descriptive attributes
- Relatively static
- Smaller than fact tables
- Example: Products, Customers, Time

### 3. What is Surrogate Key?

- Artificial key (usually auto-increment integer)
- No business meaning
- Used instead of natural key
- Benefits: Performance, consistency, handles changes

---

## ETL/ELT Questions

### 1. How do you handle incremental loads?

**Methods:**
1. **Timestamp-based**: Load records where `updated_at > last_load_time`
2. **Change Data Capture (CDC)**: Track changes in source
3. **Watermarking**: Store last processed value
4. **Delta/Merge**: Compare source and target

### 2. How do you handle late-arriving data?

- Use watermarking with grace period
- Implement SCD Type 2 for historical accuracy
- Use event time vs processing time
- Reprocess affected partitions

### 3. Data Quality Checks

- **Completeness**: No missing values
- **Accuracy**: Data is correct
- **Consistency**: Data matches across systems
- **Timeliness**: Data is up-to-date
- **Validity**: Data conforms to rules
- **Uniqueness**: No duplicates

---

## Performance & Optimization

### 1. How to optimize Spark jobs?

1. **Partitioning**: Right number of partitions (2-4x cores)
2. **Caching**: Cache frequently used DataFrames
3. **Broadcast joins**: For small tables
4. **Avoid shuffles**: Use narrow transformations
5. **Predicate pushdown**: Filter early
6. **Column pruning**: Select only needed columns
7. **Use appropriate file formats**: Parquet, ORC
8. **Tune memory**: Executor and driver memory

### 2. How to optimize SQL queries?

1. Use indexes on frequently queried columns
2. Avoid SELECT *, specify columns
3. Use WHERE to filter early
4. Use appropriate joins
5. Avoid subqueries in SELECT
6. Use EXPLAIN to analyze query plan
7. Update statistics (ANALYZE)
8. Partition large tables

### 3. Why use Parquet over CSV?

**Parquet advantages:**
- Columnar storage (better for analytics)
- Better compression
- Schema embedded
- Predicate pushdown
- Column pruning
- Faster reads for analytical queries

---

## Scenario-Based Questions

### 1. Design a real-time data pipeline

**Architecture:**
1. **Source**: Application logs, events
2. **Ingestion**: Kafka, Kinesis
3. **Processing**: Spark Streaming, Flink
4. **Storage**: S3 (raw), Redshift/Snowflake (processed)
5. **Serving**: BI tools, APIs

**Considerations:**
- Exactly-once processing
- Fault tolerance
- Scalability
- Monitoring & alerting

### 2. Handle a failed ETL job

**Steps:**
1. Check logs for error details
2. Identify root cause (data quality, resource, code)
3. Fix the issue
4. Implement checkpointing/bookmarking
5. Rerun from last successful point
6. Validate data quality
7. Add monitoring/alerts

### 3. Migrate on-premise data warehouse to cloud

**Approach:**
1. **Assessment**: Data volume, dependencies, users
2. **Choose platform**: Snowflake, Redshift, BigQuery
3. **Pilot**: Migrate small dataset
4. **Data migration**: 
   - Historical: Bulk load
   - Incremental: CDC or scheduled loads
5. **ETL migration**: Rewrite or use tools
6. **Testing**: Validate data, performance
7. **Cutover**: Gradual or big bang
8. **Optimization**: Tune for cloud platform

### 4. Design data lake architecture

**Layers:**
1. **Raw/Bronze**: Unprocessed data (S3)
2. **Cleansed/Silver**: Validated, cleaned data
3. **Curated/Gold**: Business-ready, aggregated data

**Components:**
- Storage: S3, ADLS
- Catalog: Glue Data Catalog, Hive Metastore
- Processing: Spark, Glue, Databricks
- Governance: Data quality, lineage, security
- Consumption: Athena, Redshift Spectrum, BI tools

### 5. Handle PII/sensitive data

**Strategies:**
1. **Encryption**: At rest and in transit
2. **Masking**: Hide sensitive data from unauthorized users
3. **Tokenization**: Replace with tokens
4. **Access control**: Role-based, column-level
5. **Audit logging**: Track access
6. **Data retention**: Delete when not needed
7. **Compliance**: GDPR, HIPAA, CCPA

---

## Key Concepts to Remember

### Data Engineering Principles
- **Idempotency**: Same input produces same output
- **Scalability**: Handle growing data volumes
- **Fault Tolerance**: Recover from failures
- **Data Quality**: Ensure accuracy and completeness
- **Monitoring**: Track pipeline health
- **Documentation**: Maintain clear documentation

### Best Practices
- Version control for code
- Automated testing
- CI/CD pipelines
- Incremental processing
- Partitioning and bucketing
- Appropriate file formats
- Cost optimization
- Security first

### Common Tools & Technologies
- **Processing**: Spark, Flink, Beam
- **Orchestration**: Airflow, Dagster, Prefect
- **Storage**: S3, HDFS, ADLS
- **Warehouses**: Snowflake, Redshift, BigQuery
- **Streaming**: Kafka, Kinesis, Pub/Sub
- **Transformation**: dbt, Dataform
- **Cloud**: AWS, Azure, GCP

---

## Interview Tips

1. **Understand the problem**: Ask clarifying questions
2. **Think aloud**: Explain your thought process
3. **Start simple**: Begin with basic solution, then optimize
4. **Consider trade-offs**: Discuss pros/cons of approaches
5. **Use examples**: Provide concrete examples from experience
6. **Know your resume**: Be ready to discuss projects in detail
7. **Ask questions**: Show interest in the role and company
8. **Practice coding**: LeetCode, HackerRank for SQL/Python
9. **Stay current**: Know latest trends and tools
10. **Be honest**: Say "I don't know" if you don't, then explain how you'd find out

---

**Good luck with your Data Engineer interviews! 🚀**
