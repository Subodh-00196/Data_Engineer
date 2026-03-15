/*
================================================================================
                REDSHIFT - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive Amazon Redshift examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. REDSHIFT ARCHITECTURE & KEY FEATURES
2. DISTRIBUTION STYLES
3. SORT KEYS
4. COMPRESSION ENCODING
5. DATA LOADING (COPY COMMAND)
6. REDSHIFT SPECTRUM (Query S3)
7. UNLOAD DATA TO S3
8. VACUUM & ANALYZE
9. WORKLOAD MANAGEMENT (WLM)
10. SLOWLY CHANGING DIMENSIONS (SCD)
11. PERFORMANCE OPTIMIZATION
12. BEST PRACTICES
================================================================================
*/

-- ============================================================================
-- 1. REDSHIFT ARCHITECTURE & KEY FEATURES
-- ============================================================================

/*
REDSHIFT ARCHITECTURE:
- Leader Node: Manages client connections, query planning, and coordination
- Compute Nodes: Store data and execute queries in parallel
- Node Slices: Each compute node divided into slices (parallel processing units)

KEY FEATURES:
- Massively Parallel Processing (MPP)
- Columnar Storage (optimized for analytics)
- Data Compression (automatic compression)
- Distribution Styles (control data distribution)
- Sort Keys (optimize query performance)
- Redshift Spectrum (query S3 data)
- Concurrency Scaling (handle burst workloads)
- Result Caching
- Materialized Views
- Machine Learning Integration
- Zero-ETL Integration
- Encryption (at rest and in transit)
- Fine-grained Access Control

NODE TYPES:
- Dense Compute (DC2): SSD-based, compute-intensive workloads
- Dense Storage (DS2): HDD-based, large data volumes
- RA3: Managed storage, independent scaling of compute and storage
*/

-- ============================================================================
-- 2. DISTRIBUTION STYLES
-- ============================================================================

/*
DISTRIBUTION STYLES determine how data is distributed across compute nodes:

1. AUTO (Default): Redshift automatically selects optimal distribution
2. EVEN: Rows distributed evenly in round-robin fashion
3. KEY: Rows distributed based on values in distribution key column
4. ALL: Full copy of table on every node (for small dimension tables)
*/

/* AUTO Distribution (Recommended) */
CREATE TABLE sales_auto (
    sale_id INT,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
DISTSTYLE AUTO;

/* EVEN Distribution */
CREATE TABLE events_even (
    event_id BIGINT,
    event_type VARCHAR(50),
    event_timestamp TIMESTAMP
)
DISTSTYLE EVEN;

/* KEY Distribution (Best for large fact tables) */
CREATE TABLE sales (
    sale_id INT,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
DISTKEY(customer_id)
SORTKEY(sale_date);

/* ALL Distribution (Best for small dimension tables) */
CREATE TABLE dim_products (
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50)
)
DISTSTYLE ALL;

/* View Table Distribution */
SELECT 
    "table", 
    diststyle, 
    distkey
FROM SVV_TABLE_INFO
WHERE "schema" = 'public';

-- ============================================================================
-- 3. SORT KEYS
-- ============================================================================

/*
SORT KEYS determine the order in which data is stored on disk:

1. COMPOUND SORTKEY: Multi-column sort (order matters)
   - Best when queries filter on prefix of sort key columns
   
2. INTERLEAVED SORTKEY: Equal weight to all columns
   - Best when queries filter on different column combinations
*/

/* Compound Sort Key (Most Common) */
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    status VARCHAR(20),
    amount DECIMAL(10,2)
)
DISTKEY(customer_id)
COMPOUND SORTKEY(order_date, customer_id);

/* Interleaved Sort Key */
CREATE TABLE events (
    event_id BIGINT,
    user_id INT,
    event_type VARCHAR(50),
    event_date DATE,
    event_timestamp TIMESTAMP
)
INTERLEAVED SORTKEY(user_id, event_type, event_date);

/* Single Column Sort Key */
CREATE TABLE logs (
    log_id BIGINT,
    log_timestamp TIMESTAMP,
    message TEXT
)
SORTKEY(log_timestamp);

/* View Sort Keys */
SELECT 
    tablename,
    sortkey1,
    sortkey_num
FROM SVV_TABLE_INFO
WHERE schemaname = 'public';

-- ============================================================================
-- 4. COMPRESSION ENCODING
-- ============================================================================

/*
COMPRESSION ENCODINGS reduce storage and improve performance:

- RAW: No compression
- AZ64: High compression ratio (default for many data types)
- BYTEDICT: Good for low-cardinality columns
- LZO: Good for text columns
- RUNLENGTH: Good for columns with many repeated values
- ZSTD: High compression, good performance
*/

/* Specify Compression Encoding */
CREATE TABLE customers (
    customer_id INT ENCODE AZ64,
    customer_name VARCHAR(100) ENCODE ZSTD,
    email VARCHAR(100) ENCODE ZSTD,
    status VARCHAR(20) ENCODE BYTEDICT,
    created_date DATE ENCODE AZ64
);

/* Analyze Compression */
ANALYZE COMPRESSION customers;

/* Apply Recommended Compression */
-- Redshift automatically applies compression when using COPY command
-- For existing tables, recreate with recommended encoding

-- ============================================================================
-- 5. DATA LOADING (COPY COMMAND)
-- ============================================================================

/* Basic COPY from S3 */
COPY sales
FROM 's3://my-bucket/sales/sales_data.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV
IGNOREHEADER 1
REGION 'us-east-1';

/* COPY with Delimiter */
COPY sales
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
DELIMITER '|'
IGNOREHEADER 1;

/* COPY JSON Data */
COPY events
FROM 's3://my-bucket/events/events.json'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
JSON 'auto'
GZIP;

/* COPY with Manifest File */
COPY sales
FROM 's3://my-bucket/manifest.json'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
MANIFEST
CSV;

/* COPY Parquet Data */
COPY sales
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
FORMAT AS PARQUET;

/* COPY with Error Handling */
COPY sales
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV
MAXERROR 100  -- Allow up to 100 errors
ACCEPTINVCHARS;  -- Replace invalid characters

/* COPY with Column Mapping */
COPY sales (sale_id, customer_id, amount, sale_date)
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV;

/* COPY with Date Format */
COPY sales
FROM 's3://my-bucket/sales/'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV
DATEFORMAT 'YYYY-MM-DD'
TIMEFORMAT 'YYYY-MM-DD HH:MI:SS';

/* Monitor COPY Progress */
SELECT 
    query,
    filename,
    line_number,
    colname,
    err_reason
FROM STL_LOAD_ERRORS
ORDER BY starttime DESC
LIMIT 10;

/* Python Example: COPY from S3 */
/*
import psycopg2

conn = psycopg2.connect(
    dbname='your_db_name',
    host='your_redshift_cluster_endpoint',
    port='5439',
    user='your_username',
    password='your_password'
)

cur = conn.cursor()

copy_cmd = """
COPY sales_data
FROM 's3://my-redshift-data/sales_data.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV
IGNOREHEADER 1;
"""

cur.execute(copy_cmd)
conn.commit()
cur.close()
conn.close()
*/

-- ============================================================================
-- 6. REDSHIFT SPECTRUM (Query S3 Data)
-- ============================================================================

/*
Redshift Spectrum allows querying data in S3 without loading it into Redshift
*/

/* Create External Schema */
CREATE EXTERNAL SCHEMA spectrum_schema
FROM DATA CATALOG
DATABASE 'spectrum_db'
IAM_ROLE 'arn:aws:iam::123456789012:role/MySpectrumRole'
CREATE EXTERNAL DATABASE IF NOT EXISTS;

/* Create External Table */
CREATE EXTERNAL TABLE spectrum_schema.sales_external (
    sale_id INT,
    product_id INT,
    customer_id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
STORED AS PARQUET
LOCATION 's3://my-bucket/sales/';

/* Query External Table */
SELECT 
    sale_date,
    COUNT(*) AS num_sales,
    SUM(amount) AS total_sales
FROM spectrum_schema.sales_external
WHERE sale_date >= '2024-01-01'
GROUP BY sale_date
ORDER BY sale_date;

/* Join External and Internal Tables */
SELECT 
    s.sale_date,
    p.product_name,
    SUM(s.amount) AS total_sales
FROM spectrum_schema.sales_external s
JOIN dim_products p ON s.product_id = p.product_id
GROUP BY s.sale_date, p.product_name;

/* Create Partitioned External Table */
CREATE EXTERNAL TABLE spectrum_schema.sales_partitioned (
    sale_id INT,
    product_id INT,
    customer_id INT,
    amount DECIMAL(10,2)
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET
LOCATION 's3://my-bucket/sales_partitioned/';

/* Add Partitions */
ALTER TABLE spectrum_schema.sales_partitioned
ADD PARTITION (year=2024, month=1) 
LOCATION 's3://my-bucket/sales_partitioned/year=2024/month=01/';

ALTER TABLE spectrum_schema.sales_partitioned
ADD PARTITION (year=2024, month=2) 
LOCATION 's3://my-bucket/sales_partitioned/year=2024/month=02/';

-- ============================================================================
-- 7. UNLOAD DATA TO S3
-- ============================================================================

/* Basic UNLOAD */
UNLOAD ('SELECT * FROM sales WHERE sale_date >= ''2024-01-01''')
TO 's3://my-bucket/unload/sales_'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
PARALLEL OFF
GZIP;

/* UNLOAD with Partitioning */
UNLOAD ('SELECT * FROM sales')
TO 's3://my-bucket/unload/sales_'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
PARTITION BY (sale_date)
INCLUDE;

/* UNLOAD as Parquet */
UNLOAD ('SELECT * FROM sales')
TO 's3://my-bucket/unload/sales_'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
FORMAT AS PARQUET;

/* UNLOAD with Manifest */
UNLOAD ('SELECT * FROM sales')
TO 's3://my-bucket/unload/sales_'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
MANIFEST
GZIP;

/* UNLOAD with Header */
UNLOAD ('SELECT * FROM sales')
TO 's3://my-bucket/unload/sales_'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
HEADER
CSV;

-- ============================================================================
-- 8. VACUUM & ANALYZE
-- ============================================================================

/*
VACUUM: Reclaims space and sorts rows
ANALYZE: Updates table statistics for query optimizer
*/

/* VACUUM Full */
VACUUM sales;

/* VACUUM Delete Only */
VACUUM DELETE ONLY sales;

/* VACUUM Sort Only */
VACUUM SORT ONLY sales;

/* VACUUM Reindex */
VACUUM REINDEX sales;

/* ANALYZE Table */
ANALYZE sales;

/* ANALYZE Specific Columns */
ANALYZE sales (customer_id, sale_date);

/* Check if VACUUM is Needed */
SELECT 
    "table",
    unsorted,
    vacuum_sort_benefit
FROM SVV_TABLE_INFO
WHERE unsorted > 5  -- More than 5% unsorted
ORDER BY vacuum_sort_benefit DESC;

/* Check if ANALYZE is Needed */
SELECT 
    schemaname,
    tablename,
    last_vacuum,
    last_analyze
FROM SVV_TABLE_INFO
WHERE schemaname = 'public'
ORDER BY last_analyze;

-- ============================================================================
-- 9. WORKLOAD MANAGEMENT (WLM)
-- ============================================================================

/*
WLM manages query concurrency and resource allocation
*/

/* View WLM Configuration */
SELECT * FROM STV_WLM_CLASSIFICATION_CONFIG;

/* View Query Queue Assignment */
SELECT 
    query,
    service_class,
    slot_count,
    wlm_start_time,
    state
FROM STL_WLM_QUERY
WHERE userid > 1
ORDER BY wlm_start_time DESC
LIMIT 10;

/* Set Query Group (Route to specific queue) */
SET query_group TO 'reporting';

/* Reset Query Group */
RESET query_group;

/* View Running Queries */
SELECT 
    pid,
    user_name,
    starttime,
    duration,
    trim(query) AS query
FROM STV_RECENTS
WHERE status = 'Running'
ORDER BY starttime;

/* Cancel Query */
CANCEL 12345;  -- Replace with actual PID

-- ============================================================================
-- 10. SLOWLY CHANGING DIMENSIONS (SCD)
-- ============================================================================

/*
SCD Type 0: Fixed, never changes
SCD Type 1: Overwrite old data
SCD Type 2: Add new row, preserve history
SCD Type 3: Add new column for previous value
SCD Type 4: Separate history table
SCD Type 6: Hybrid (1+2+3)
*/

/* SCD Type 1: Overwrite */
UPDATE dim_customers
SET 
    customer_name = 'John Updated',
    email = 'john.updated@example.com',
    updated_at = CURRENT_TIMESTAMP
WHERE customer_id = 123;

/* SCD Type 2: Add New Row with History */
CREATE TABLE dim_customers_scd2 (
    customer_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    effective_from DATE,
    effective_to DATE,
    is_current BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
DISTKEY(customer_id)
SORTKEY(customer_id, effective_from);

/* Insert New Version (SCD Type 2) */
BEGIN TRANSACTION;

-- Expire current record
UPDATE dim_customers_scd2
SET 
    effective_to = CURRENT_DATE - 1,
    is_current = FALSE
WHERE customer_id = 123 
  AND is_current = TRUE;

-- Insert new record
INSERT INTO dim_customers_scd2 (
    customer_id, 
    customer_name, 
    email, 
    effective_from, 
    effective_to, 
    is_current
)
VALUES (
    123,
    'John Updated',
    'john.updated@example.com',
    CURRENT_DATE,
    '9999-12-31',
    TRUE
);

COMMIT;

/* Query Current Records */
SELECT * 
FROM dim_customers_scd2
WHERE is_current = TRUE;

/* Query Historical Records */
SELECT * 
FROM dim_customers_scd2
WHERE customer_id = 123
ORDER BY effective_from;

/* Query as of Specific Date */
SELECT * 
FROM dim_customers_scd2
WHERE customer_id = 123
  AND '2024-01-15' BETWEEN effective_from AND effective_to;

-- ============================================================================
-- 11. PERFORMANCE OPTIMIZATION
-- ============================================================================

/* Create Materialized View */
CREATE MATERIALIZED VIEW mv_sales_summary AS
SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    product_id,
    SUM(amount) AS total_sales,
    COUNT(*) AS num_transactions
FROM sales
GROUP BY DATE_TRUNC('month', sale_date), product_id;

/* Refresh Materialized View */
REFRESH MATERIALIZED VIEW mv_sales_summary;

/* Use Result Caching */
-- Redshift automatically caches results for identical queries
-- Cache is valid for 24 hours

/* Optimize Join Performance */
-- Use distribution keys to co-locate join data
-- Use sort keys on join columns
-- Use ANALYZE to update statistics

/* Query Performance Monitoring */
SELECT 
    query,
    TRIM(querytxt) AS sql,
    starttime,
    endtime,
    DATEDIFF(seconds, starttime, endtime) AS duration_seconds
FROM STL_QUERY
WHERE userid > 1
  AND starttime >= DATEADD(hour, -1, CURRENT_TIMESTAMP)
ORDER BY duration_seconds DESC
LIMIT 10;

/* Explain Plan */
EXPLAIN
SELECT 
    c.customer_name,
    SUM(s.amount) AS total_sales
FROM sales s
JOIN dim_customers c ON s.customer_id = c.customer_id
WHERE s.sale_date >= '2024-01-01'
GROUP BY c.customer_name;

/* View Table Statistics */
SELECT 
    "table",
    size AS size_mb,
    tbl_rows,
    unsorted,
    stats_off
FROM SVV_TABLE_INFO
WHERE schemaname = 'public'
ORDER BY size DESC;

/* Identify Long-Running Queries */
SELECT 
    pid,
    user_name,
    starttime,
    DATEDIFF(seconds, starttime, CURRENT_TIMESTAMP) AS runtime_seconds,
    TRIM(query) AS query
FROM STV_RECENTS
WHERE status = 'Running'
  AND DATEDIFF(seconds, starttime, CURRENT_TIMESTAMP) > 300
ORDER BY runtime_seconds DESC;

-- ============================================================================
-- 12. BEST PRACTICES
-- ============================================================================

/*
DISTRIBUTION STRATEGY:
- Use KEY distribution for large fact tables (distribute on join key)
- Use ALL distribution for small dimension tables (< 1M rows)
- Use EVEN distribution for tables without clear join pattern
- Use AUTO to let Redshift decide

SORT KEY STRATEGY:
- Use columns frequently used in WHERE, JOIN, ORDER BY
- Put most selective columns first in compound sort key
- Use date/timestamp columns for time-series data
- Consider interleaved sort keys for multiple query patterns

COMPRESSION:
- Let Redshift auto-compress during COPY
- Use ANALYZE COMPRESSION for existing tables
- Reapply compression after major data changes

DATA LOADING:
- Use COPY command (not INSERT)
- Load compressed files (GZIP, BZIP2)
- Load multiple files in parallel
- Use manifest files for consistency
- Monitor STL_LOAD_ERRORS

MAINTENANCE:
- Run VACUUM regularly (weekly for active tables)
- Run ANALYZE after significant data changes
- Monitor table statistics
- Set up automated maintenance

QUERY OPTIMIZATION:
- Use WHERE clause to filter early
- Avoid SELECT *
- Use appropriate join types
- Use EXPLAIN to analyze query plans
- Monitor query performance

WORKLOAD MANAGEMENT:
- Configure WLM queues for different workloads
- Set appropriate memory and concurrency
- Use query groups to route queries
- Enable concurrency scaling for bursts

SECURITY:
- Use IAM roles (not access keys)
- Enable encryption at rest
- Enable encryption in transit (SSL)
- Use VPC for network isolation
- Implement column-level security

COST OPTIMIZATION:
- Use RA3 nodes for independent scaling
- Pause clusters when not in use
- Use Redshift Spectrum for cold data
- Monitor and optimize queries
- Right-size your cluster
*/

/* Example: Optimized Table Design */
CREATE TABLE fact_sales (
    sale_id BIGINT ENCODE AZ64,
    customer_id INT ENCODE AZ64,
    product_id INT ENCODE AZ64,
    sale_date DATE ENCODE AZ64,
    sale_timestamp TIMESTAMP ENCODE AZ64,
    quantity INT ENCODE AZ64,
    unit_price DECIMAL(10,2) ENCODE AZ64,
    total_amount DECIMAL(10,2) ENCODE AZ64,
    region VARCHAR(50) ENCODE ZSTD,
    status VARCHAR(20) ENCODE BYTEDICT
)
DISTKEY(customer_id)
COMPOUND SORTKEY(sale_date, customer_id);

/* Example: Incremental Load Pattern */
BEGIN TRANSACTION;

-- Create staging table
CREATE TEMP TABLE staging_sales (LIKE fact_sales);

-- Load new data
COPY staging_sales
FROM 's3://my-bucket/incremental/sales_20240115.csv'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CSV;

-- Merge into target
DELETE FROM fact_sales
USING staging_sales
WHERE fact_sales.sale_id = staging_sales.sale_id;

INSERT INTO fact_sales
SELECT * FROM staging_sales;

-- Clean up
DROP TABLE staging_sales;

COMMIT;

/* Example: Monitoring Query */
SELECT 
    schemaname,
    tablename,
    size AS size_mb,
    tbl_rows,
    unsorted AS pct_unsorted,
    stats_off AS pct_stats_off,
    CASE 
        WHEN unsorted > 10 THEN 'VACUUM recommended'
        WHEN stats_off > 10 THEN 'ANALYZE recommended'
        ELSE 'OK'
    END AS recommendation
FROM SVV_TABLE_INFO
WHERE schemaname = 'public'
ORDER BY size DESC;

/*
================================================================================
END OF REDSHIFT INTERVIEW GUIDE
================================================================================
*/
