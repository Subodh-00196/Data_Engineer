/*
================================================================================
                SNOWFLAKE - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive Snowflake examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. SNOWFLAKE ARCHITECTURE & KEY FEATURES
2. STORAGE INTEGRATION & STAGES
3. FILE FORMATS
4. DATA LOADING (COPY INTO)
5. TASKS & SCHEDULING
6. STREAMS (CDC - Change Data Capture)
7. STORED PROCEDURES
8. INCREMENTAL LOADS & MERGE
9. TIME TRAVEL & FAIL-SAFE
10. CLONING (ZERO-COPY CLONING)
11. SECURITY & ACCESS CONTROL
12. PERFORMANCE OPTIMIZATION
13. BEST PRACTICES
================================================================================
*/

-- ============================================================================
-- 1. SNOWFLAKE ARCHITECTURE & KEY FEATURES
-- ============================================================================

/*
SNOWFLAKE ARCHITECTURE (Hybrid):
1. Storage Layer: Cloud-based object storage (S3, Azure Blob, GCS)
   - Compressed, columnar format
   - Optimized for analytics
   - Automatic clustering

2. Compute Layer: Virtual Warehouses (MPP compute clusters)
   - Independent scaling
   - Multiple warehouses for different workloads
   - Auto-suspend and auto-resume

3. Cloud Services Layer: Metadata, authentication, query optimization
   - Query parsing and optimization
   - Metadata management
   - Security and access control

KEY FEATURES:
- Separation of Storage and Compute
- Virtual Warehouses (independent scaling)
- Time Travel (query historical data)
- Fail-Safe (7-day recovery)
- Data Sharing (secure, live data sharing)
- Automatic Clustering
- Zero-Copy Cloning
- Support for Semi-Structured Data (JSON, Avro, Parquet, XML)
- End-to-End Encryption
- Cross-Region Data Sharing
- Materialized Views
- External Tables
*/

-- ============================================================================
-- 2. STORAGE INTEGRATION & STAGES
-- ============================================================================

/* Create Storage Integration with Azure */
CREATE OR REPLACE STORAGE INTEGRATION azure_storage_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'AZURE'
  AZURE_TENANT_ID = '<your-tenant-id>'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('azure://<your-container>/<path>/');

/* Create Storage Integration with AWS S3 */
CREATE OR REPLACE STORAGE INTEGRATION my_s3_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  STORAGE_AWS_ROLE_ARN = '<your-aws-role-arn>'
  STORAGE_AWS_EXTERNAL_ID = '<external-id>'
  ENABLED = TRUE
  STORAGE_ALLOWED_LOCATIONS = ('s3://my-bucket/path/');

/* Describe Storage Integration (Get credentials for cloud provider) */
DESC STORAGE INTEGRATION azure_storage_integration;

/* Create External Stage with Azure */
CREATE OR REPLACE STAGE my_adls_stage
  URL = 'azure://my-container/path/'
  STORAGE_INTEGRATION = azure_storage_integration
  FILE_FORMAT = (TYPE = 'CSV');

/* Create External Stage with S3 */
CREATE OR REPLACE STAGE my_s3_stage
  URL = 's3://my-bucket/path/'
  STORAGE_INTEGRATION = my_s3_integration
  FILE_FORMAT = (TYPE = 'CSV');

/* Create Internal Stage (Snowflake-managed) */
CREATE OR REPLACE STAGE my_internal_stage
  FILE_FORMAT = (TYPE = 'CSV');

/* List Files in Stage */
LIST @my_s3_stage;
LIST @my_s3_stage/subfolder/;

/* Remove Files from Stage */
REMOVE @my_s3_stage/file.csv;

-- ============================================================================
-- 3. FILE FORMATS
-- ============================================================================

/* Create CSV File Format */
CREATE OR REPLACE FILE FORMAT csv_file_format
  TYPE = 'CSV'
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  NULL_IF = ('NULL', 'null', '')
  EMPTY_FIELD_AS_NULL = TRUE
  TRIM_SPACE = TRUE
  ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
  FIELD_OPTIONALLY_ENCLOSED_BY = '"'
  ESCAPE_UNENCLOSED_FIELD = NONE;

/* Create JSON File Format */
CREATE OR REPLACE FILE FORMAT json_file_format
  TYPE = 'JSON'
  STRIP_OUTER_ARRAY = TRUE
  COMPRESSION = 'AUTO';

/* Create Parquet File Format */
CREATE OR REPLACE FILE FORMAT parquet_file_format
  TYPE = 'PARQUET'
  COMPRESSION = 'SNAPPY';

/* Create Avro File Format */
CREATE OR REPLACE FILE FORMAT avro_file_format
  TYPE = 'AVRO'
  COMPRESSION = 'AUTO';

/* View File Format */
DESC FILE FORMAT csv_file_format;

-- ============================================================================
-- 4. DATA LOADING (COPY INTO)
-- ============================================================================

/* Create Target Table */
CREATE OR REPLACE TABLE my_table (
    id INTEGER,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP
);

/* Load Data from Stage */
COPY INTO my_table
FROM @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format')
ON_ERROR = 'CONTINUE';  -- Options: CONTINUE, SKIP_FILE, ABORT_STATEMENT

/* Load Specific Files */
COPY INTO my_table
FROM @my_s3_stage
FILES = ('file1.csv', 'file2.csv')
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

/* Load with Pattern Matching */
COPY INTO my_table
FROM @my_s3_stage
PATTERN = '.*sales_[0-9]{4}.csv'
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

/* Load with Column Mapping */
COPY INTO my_table (id, name, email)
FROM (
    SELECT 
        $1::INTEGER,
        $2::VARCHAR,
        $3::VARCHAR
    FROM @my_s3_stage
)
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

/* Load with Transformations */
COPY INTO my_table
FROM (
    SELECT 
        $1::INTEGER AS id,
        UPPER($2::VARCHAR) AS name,
        LOWER($3::VARCHAR) AS email,
        CURRENT_TIMESTAMP() AS created_at
    FROM @my_s3_stage
)
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

/* Load JSON Data */
CREATE OR REPLACE TABLE json_table (
    raw_data VARIANT
);

COPY INTO json_table
FROM @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'json_file_format');

/* Parse JSON and Load into Structured Table */
CREATE OR REPLACE TABLE structured_table (
    id INTEGER,
    name VARCHAR,
    email VARCHAR
);

COPY INTO structured_table
FROM (
    SELECT 
        $1:id::INTEGER,
        $1:name::VARCHAR,
        $1:email::VARCHAR
    FROM @my_s3_stage
)
FILE_FORMAT = (FORMAT_NAME = 'json_file_format');

/* Load with Metadata Columns */
COPY INTO my_table (id, name, email, filename, row_number)
FROM (
    SELECT 
        $1::INTEGER,
        $2::VARCHAR,
        $3::VARCHAR,
        METADATA$FILENAME AS filename,
        METADATA$FILE_ROW_NUMBER AS row_number
    FROM @my_s3_stage
)
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

/* Validate Data Before Loading */
COPY INTO my_table
FROM @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format')
VALIDATION_MODE = 'RETURN_ERRORS';  -- Options: RETURN_ERRORS, RETURN_n_ROWS

-- ============================================================================
-- 5. TASKS & SCHEDULING
-- ============================================================================

/* Create Simple Task */
CREATE OR REPLACE TASK my_daily_task
  WAREHOUSE = my_warehouse
  SCHEDULE = 'USING CRON 0 2 * * * UTC'  -- 2 AM UTC daily
  COMMENT = 'Daily data refresh task'
AS
  INSERT INTO target_table
  SELECT * FROM source_table
  WHERE date = CURRENT_DATE - 1;

/* Create Task with Multiple Statements */
CREATE OR REPLACE TASK my_etl_task
  WAREHOUSE = my_warehouse
  SCHEDULE = 'USING CRON 0 * * * * UTC'  -- Every hour
AS
BEGIN
  -- Truncate staging table
  TRUNCATE TABLE staging_table;
  
  -- Load new data
  COPY INTO staging_table
  FROM @my_s3_stage
  FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');
  
  -- Merge into target
  MERGE INTO target_table t
  USING staging_table s
  ON t.id = s.id
  WHEN MATCHED THEN UPDATE SET t.value = s.value
  WHEN NOT MATCHED THEN INSERT VALUES (s.id, s.value);
END;

/* Create Task that Runs After Another Task */
CREATE OR REPLACE TASK child_task
  WAREHOUSE = my_warehouse
  AFTER parent_task
AS
  SELECT * FROM processed_data;

/* Resume/Suspend Task */
ALTER TASK my_daily_task RESUME;
ALTER TASK my_daily_task SUSPEND;

/* View Task History */
SELECT *
FROM TABLE(INFORMATION_SCHEMA.TASK_HISTORY())
WHERE NAME = 'MY_DAILY_TASK'
ORDER BY SCHEDULED_TIME DESC
LIMIT 10;

/* Show Tasks */
SHOW TASKS;
DESC TASK my_daily_task;

-- ============================================================================
-- 6. STREAMS (CDC - Change Data Capture)
-- ============================================================================

/* Create Stream on Table */
CREATE OR REPLACE STREAM my_table_stream 
ON TABLE source_table;

/* View Stream Data */
SELECT * FROM my_table_stream;

/* Stream Metadata Columns */
SELECT 
    *,
    METADATA$ACTION,      -- INSERT, DELETE, or UPDATE
    METADATA$ISUPDATE,    -- TRUE if update
    METADATA$ROW_ID       -- Unique row identifier
FROM my_table_stream;

/* Consume Stream Data */
INSERT INTO target_table
SELECT id, name, email
FROM my_table_stream
WHERE METADATA$ACTION = 'INSERT';

/* Process Updates and Deletes */
MERGE INTO target_table t
USING my_table_stream s
ON t.id = s.id
WHEN MATCHED AND s.METADATA$ACTION = 'DELETE' THEN DELETE
WHEN MATCHED AND s.METADATA$ACTION = 'INSERT' AND s.METADATA$ISUPDATE THEN 
    UPDATE SET t.name = s.name, t.email = s.email
WHEN NOT MATCHED AND s.METADATA$ACTION = 'INSERT' THEN
    INSERT (id, name, email) VALUES (s.id, s.name, s.email);

/* Stream on View */
CREATE OR REPLACE STREAM view_stream
ON VIEW my_view;

/* Show Streams */
SHOW STREAMS;
DESC STREAM my_table_stream;

-- ============================================================================
-- 7. STORED PROCEDURES
-- ============================================================================

/* Create Stored Procedure for Incremental Load */
CREATE OR REPLACE PROCEDURE load_incremental_data()
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
    -- Merge new/updated records
    MERGE INTO target_table AS tgt
    USING source_table AS src
    ON tgt.id = src.id
    WHEN MATCHED AND src.last_updated > tgt.last_updated THEN
        UPDATE SET 
            tgt.column1 = src.column1,
            tgt.column2 = src.column2,
            tgt.last_updated = src.last_updated
    WHEN NOT MATCHED THEN
        INSERT (id, column1, column2, last_updated)
        VALUES (src.id, src.column1, src.column2, src.last_updated);
    
    RETURN 'Incremental data load completed successfully';
END;
$$;

/* Call Stored Procedure */
CALL load_incremental_data();

/* Stored Procedure with Parameters */
CREATE OR REPLACE PROCEDURE process_data(table_name VARCHAR, date_filter DATE)
RETURNS STRING
LANGUAGE SQL
AS
$$
DECLARE
    row_count INTEGER;
BEGIN
    -- Dynamic SQL
    LET sql_stmt := 'INSERT INTO processed_' || table_name || 
                    ' SELECT * FROM ' || table_name || 
                    ' WHERE date = ''' || date_filter || '''';
    
    EXECUTE IMMEDIATE :sql_stmt;
    
    -- Get row count
    row_count := SQLROWCOUNT;
    
    RETURN 'Processed ' || row_count || ' rows';
END;
$$;

/* JavaScript Stored Procedure */
CREATE OR REPLACE PROCEDURE calculate_metrics()
RETURNS VARIANT
LANGUAGE JAVASCRIPT
AS
$$
    var result = {};
    
    // Query data
    var stmt = snowflake.createStatement({
        sqlText: "SELECT COUNT(*) as cnt FROM my_table"
    });
    var rs = stmt.execute();
    rs.next();
    result.total_count = rs.getColumnValue(1);
    
    // More processing...
    
    return result;
$$;

-- ============================================================================
-- 8. INCREMENTAL LOADS & MERGE
-- ============================================================================

/* Basic MERGE (Upsert) */
MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET 
        t.name = s.name,
        t.email = s.email,
        t.updated_at = CURRENT_TIMESTAMP()
WHEN NOT MATCHED THEN
    INSERT (id, name, email, created_at, updated_at)
    VALUES (s.id, s.name, s.email, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP());

/* MERGE with Conditions */
MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED AND s.status = 'DELETED' THEN DELETE
WHEN MATCHED AND s.updated_at > t.updated_at THEN
    UPDATE SET 
        t.name = s.name,
        t.email = s.email,
        t.updated_at = s.updated_at
WHEN NOT MATCHED THEN
    INSERT (id, name, email, created_at)
    VALUES (s.id, s.name, s.email, s.created_at);

/* Incremental Load Pattern */
-- Get max timestamp from target
CREATE OR REPLACE TEMPORARY TABLE watermark AS
SELECT MAX(updated_at) AS last_updated FROM target_table;

-- Load only new/updated records
INSERT INTO target_table
SELECT s.*
FROM source_table s
CROSS JOIN watermark w
WHERE s.updated_at > w.last_updated;

/* Incremental Load with QUALIFY */
INSERT INTO target_table
SELECT *
FROM source_table
WHERE updated_at > (SELECT MAX(updated_at) FROM target_table)
QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) = 1;

-- ============================================================================
-- 9. TIME TRAVEL & FAIL-SAFE
-- ============================================================================

/* Query Historical Data (Time Travel) */
-- Query as of specific timestamp
SELECT * FROM my_table 
AT(TIMESTAMP => '2024-01-01 12:00:00'::TIMESTAMP);

-- Query as of specific offset (seconds ago)
SELECT * FROM my_table 
AT(OFFSET => -3600);  -- 1 hour ago

-- Query before specific statement
SELECT * FROM my_table 
BEFORE(STATEMENT => '01a1b2c3-0000-0000-0000-000000000000');

/* Clone Table from Historical Point */
CREATE TABLE my_table_restored CLONE my_table
AT(TIMESTAMP => '2024-01-01 12:00:00'::TIMESTAMP);

/* Undrop Table */
UNDROP TABLE my_table;

/* Undrop Schema */
UNDROP SCHEMA my_schema;

/* Set Data Retention Period */
ALTER TABLE my_table SET DATA_RETENTION_TIME_IN_DAYS = 7;  -- Max 90 days (Enterprise)

/* View Data Retention */
SHOW PARAMETERS LIKE 'DATA_RETENTION_TIME_IN_DAYS' FOR TABLE my_table;

-- ============================================================================
-- 10. CLONING (ZERO-COPY CLONING)
-- ============================================================================

/* Clone Table */
CREATE TABLE my_table_clone CLONE my_table;

/* Clone Database */
CREATE DATABASE my_database_clone CLONE my_database;

/* Clone Schema */
CREATE SCHEMA my_schema_clone CLONE my_schema;

/* Clone at Specific Time */
CREATE TABLE my_table_clone CLONE my_table
AT(TIMESTAMP => '2024-01-01 12:00:00'::TIMESTAMP);

/* Clone for Development/Testing */
CREATE DATABASE dev_database CLONE prod_database;

-- ============================================================================
-- 11. SECURITY & ACCESS CONTROL
-- ============================================================================

/* Create Role */
CREATE ROLE data_engineer_role;
CREATE ROLE analyst_role;

/* Grant Privileges to Role */
GRANT USAGE ON DATABASE my_database TO ROLE data_engineer_role;
GRANT USAGE ON SCHEMA my_database.public TO ROLE data_engineer_role;
GRANT SELECT ON ALL TABLES IN SCHEMA my_database.public TO ROLE analyst_role;
GRANT INSERT, UPDATE, DELETE ON TABLE my_table TO ROLE data_engineer_role;

/* Grant Role to User */
GRANT ROLE data_engineer_role TO USER john_doe;

/* Create Row Access Policy */
CREATE OR REPLACE ROW ACCESS POLICY sales_policy
AS (region VARCHAR) RETURNS BOOLEAN ->
    CASE
        WHEN CURRENT_ROLE() = 'ADMIN_ROLE' THEN TRUE
        WHEN CURRENT_ROLE() = 'SALES_ROLE' AND region = 'US' THEN TRUE
        ELSE FALSE
    END;

/* Apply Row Access Policy */
ALTER TABLE sales ADD ROW ACCESS POLICY sales_policy ON (region);

/* Create Masking Policy */
CREATE OR REPLACE MASKING POLICY ssn_masking_policy AS (val STRING) RETURNS STRING ->
    CASE
        WHEN CURRENT_ROLE() IN ('ADMIN_ROLE', 'COMPLIANCE_ROLE') THEN val
        ELSE 'XXX-XX-XXXX'
    END;

/* Apply Masking Policy to Column */
ALTER TABLE employees MODIFY COLUMN ssn SET MASKING POLICY ssn_masking_policy;

/* Network Policy */
CREATE NETWORK POLICY my_network_policy
    ALLOWED_IP_LIST = ('192.168.1.0/24', '10.0.0.0/8')
    BLOCKED_IP_LIST = ('192.168.1.100');

ALTER ACCOUNT SET NETWORK_POLICY = my_network_policy;

-- ============================================================================
-- 12. PERFORMANCE OPTIMIZATION
-- ============================================================================

/* Create Clustered Table */
CREATE TABLE sales_clustered (
    sale_id INTEGER,
    sale_date DATE,
    customer_id INTEGER,
    amount DECIMAL(10,2)
)
CLUSTER BY (sale_date, customer_id);

/* Automatic Clustering */
ALTER TABLE sales_clustered RESUME RECLUSTER;
ALTER TABLE sales_clustered SUSPEND RECLUSTER;

/* Materialized View */
CREATE MATERIALIZED VIEW sales_summary AS
SELECT 
    DATE_TRUNC('month', sale_date) AS month,
    customer_id,
    SUM(amount) AS total_sales,
    COUNT(*) AS num_transactions
FROM sales
GROUP BY DATE_TRUNC('month', sale_date), customer_id;

/* Search Optimization Service */
ALTER TABLE my_table ADD SEARCH OPTIMIZATION;
ALTER TABLE my_table DROP SEARCH OPTIMIZATION;

/* Query Profiling */
ALTER SESSION SET USE_CACHED_RESULT = FALSE;
ALTER SESSION SET QUERY_TAG = 'performance_test';

/* View Query History */
SELECT *
FROM TABLE(INFORMATION_SCHEMA.QUERY_HISTORY())
WHERE QUERY_TAG = 'performance_test'
ORDER BY START_TIME DESC;

/* Warehouse Sizing */
CREATE WAREHOUSE small_wh WITH 
    WAREHOUSE_SIZE = 'SMALL'
    AUTO_SUSPEND = 300
    AUTO_RESUME = TRUE
    MIN_CLUSTER_COUNT = 1
    MAX_CLUSTER_COUNT = 3
    SCALING_POLICY = 'STANDARD';

/* Multi-Cluster Warehouse */
CREATE WAREHOUSE large_wh WITH
    WAREHOUSE_SIZE = 'LARGE'
    MIN_CLUSTER_COUNT = 2
    MAX_CLUSTER_COUNT = 10
    SCALING_POLICY = 'ECONOMY';

-- ============================================================================
-- 13. BEST PRACTICES
-- ============================================================================

/*
TABLE TYPES:
1. Permanent Table: Default, supports Time Travel and Fail-safe
2. Transient Table: No Fail-safe, limited Time Travel (1 day max)
3. Temporary Table: Session-based, automatically dropped
4. External Table: References data in external storage

BEST PRACTICES:

1. WAREHOUSE MANAGEMENT:
   - Use appropriate warehouse sizes
   - Enable auto-suspend and auto-resume
   - Use multi-cluster for concurrent workloads
   - Separate warehouses for different workloads

2. DATA LOADING:
   - Use COPY INTO for bulk loading
   - Load compressed files
   - Use file formats for consistency
   - Implement error handling (ON_ERROR)
   - Use pattern matching for selective loading

3. PERFORMANCE:
   - Use clustering for large tables
   - Create materialized views for complex queries
   - Use result caching
   - Partition data by date
   - Use appropriate data types

4. COST OPTIMIZATION:
   - Use transient tables for temporary data
   - Set appropriate data retention periods
   - Monitor warehouse usage
   - Use auto-suspend
   - Optimize query performance

5. SECURITY:
   - Use role-based access control
   - Implement row-level security
   - Use masking policies for PII
   - Enable MFA
   - Use network policies

6. DATA QUALITY:
   - Implement data validation
   - Use constraints where appropriate
   - Monitor data freshness
   - Implement error logging
   - Use streams for CDC

7. INCREMENTAL PROCESSING:
   - Use streams for CDC
   - Implement watermarking
   - Use MERGE for upserts
   - Process only changed data
   - Use tasks for scheduling

8. MONITORING:
   - Monitor query performance
   - Track warehouse usage
   - Monitor data loading
   - Set up alerts
   - Review query history
*/

/* Create Transient Table */
CREATE TRANSIENT TABLE temp_data (
    id INTEGER,
    value VARCHAR
);

/* Create Temporary Table */
CREATE TEMPORARY TABLE session_data (
    id INTEGER,
    value VARCHAR
);

/* Create External Table */
CREATE EXTERNAL TABLE external_sales
WITH LOCATION = @my_s3_stage
FILE_FORMAT = (FORMAT_NAME = 'parquet_file_format')
PATTERN = '.*sales.*[.]parquet';

/* Query External Table */
SELECT * FROM external_sales
WHERE sale_date >= '2024-01-01';

/*
================================================================================
END OF SNOWFLAKE INTERVIEW GUIDE
================================================================================
*/
