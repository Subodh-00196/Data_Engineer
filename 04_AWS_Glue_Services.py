"""
================================================================================
                AWS GLUE & SERVICES - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive AWS Glue, Lambda, and related services examples
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. AWS GLUE BASICS
2. GLUE CRAWLERS
3. GLUE JOBS & ETL
4. DYNAMICFRAMES
5. GLUE TRANSFORMATIONS
6. GLUE JOB BOOKMARKS
7. AWS LAMBDA FUNCTIONS
8. S3 OPERATIONS
9. GLUE TRIGGERS & WORKFLOWS
10. SCHEMA EVOLUTION & HANDLING
11. INCREMENTAL DATA PROCESSING
12. ERROR HANDLING & LOGGING
================================================================================
"""

import sys
import boto3
import json
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# ============================================================================
# 1. AWS GLUE BASICS
# ============================================================================

""" Initialize Glue Context """
# Get job parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Initialize Spark and Glue contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Your ETL logic here

# Commit the job
job.commit()

""" Glue Job with Parameters """
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'source_path',
    'target_path',
    'load_type'
])

source_path = args['source_path']
target_path = args['target_path']
load_type = args['load_type']

# ============================================================================
# 2. GLUE CRAWLERS
# ============================================================================

""" Create Glue Crawler """
import boto3

glue_client = boto3.client('glue')

response = glue_client.create_crawler(
    Name='my-data-crawler',
    Role='AWSGlueServiceRole',
    DatabaseName='my_database',
    Description='Crawler for S3 data',
    Targets={
        'S3Targets': [
            {
                'Path': 's3://my-bucket/my-data/',
                'Exclusions': ['*.tmp', '*.log']
            }
        ]
    },
    TablePrefix='raw_',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    Configuration=json.dumps({
        "Version": 1.0,
        "CrawlerOutput": {
            "Partitions": {"AddOrUpdateBehavior": "InheritFromTable"}
        }
    })
)

# Start crawler
glue_client.start_crawler(Name='my-data-crawler')

""" Crawler for Schema Detection with Schema Change Policy """
glue_client.create_crawler(
    Name='PMIDataCrawler',
    Role='AWSGlueServiceRoleDefault',
    DatabaseName='pmidata_db',
    Targets={'S3Targets': [{'Path': 's3://pmidata-ingestion-bucket/'}]},
    TablePrefix='raw_',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'LOG'
    }
)

# ============================================================================
# 3. GLUE JOBS & ETL
# ============================================================================

""" Basic Glue ETL Job """
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_database",
    table_name="my_table",
    transformation_ctx="datasource"
)

# Apply transformations
applymapping = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ("id", "long", "id", "long"),
        ("name", "string", "name", "string"),
        ("age", "long", "age", "int")
    ],
    transformation_ctx="applymapping"
)

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame=applymapping,
    connection_type="s3",
    connection_options={"path": "s3://my-bucket/output/"},
    format="parquet",
    transformation_ctx="datasink"
)

job.commit()

""" Read from S3 and Write to Snowflake """
# Read from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://pmidata-ingestion-bucket/"]},
    format="json",
    transformation_ctx="datasource"
)

# Handle schema evolution
datasource = datasource.resolveChoice(
    specs=[('signup_date', 'cast:string')],
    choiceOption='MATCH_CATALOG'
)

# Write to Snowflake
datasource.toDF().write \
    .format("snowflake") \
    .option("sfURL", "https://<account>.snowflakecomputing.com") \
    .option("dbtable", "PMI_USERS") \
    .option("sfUser", "<username>") \
    .option("sfPassword", "<password>") \
    .option("sfWarehouse", "<warehouse>") \
    .option("sfDatabase", "<database>") \
    .option("sfSchema", "<schema>") \
    .option("sfRole", "<role>") \
    .mode("append") \
    .save()

# ============================================================================
# 4. DYNAMICFRAMES
# ============================================================================

""" Create DynamicFrame from various sources """

# From Glue Data Catalog
df_catalog = glueContext.create_dynamic_frame.from_catalog(
    database="sample_database",
    table_name="customer_data",
    transformation_ctx="df_catalog"
)

# From S3
df_s3 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://my-bucket/data/"]},
    format="json",
    transformation_ctx="df_s3"
)

# From JDBC
df_jdbc = glueContext.create_dynamic_frame.from_options(
    connection_type="mysql",
    connection_options={
        "url": "jdbc:mysql://hostname:port/dbname",
        "dbtable": "table_name",
        "user": "username",
        "password": "password"
    },
    transformation_ctx="df_jdbc"
)

""" Convert between DynamicFrame and DataFrame """
# DynamicFrame to DataFrame
df = dynamic_frame.toDF()

# DataFrame to DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

""" Print Schema """
dynamic_frame.printSchema()

""" Show Sample Data """
dynamic_frame.show(5)

""" Count Records """
count = dynamic_frame.count()

# ============================================================================
# 5. GLUE TRANSFORMATIONS
# ============================================================================

""" ApplyMapping - Rename and cast columns """
mapped_df = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ("old_col1", "string", "new_col1", "string"),
        ("old_col2", "int", "new_col2", "long"),
        ("old_col3", "string", "new_col3", "date")
    ],
    transformation_ctx="mapped_df"
)

""" ResolveChoice - Handle schema conflicts """
resolved_df = ResolveChoice.apply(
    frame=datasource,
    choice="cast:long",
    transformation_ctx="resolved_df"
)

# Resolve specific columns
resolved_df = datasource.resolveChoice(
    specs=[('signup_date', 'cast:string')],
    choiceOption='MATCH_CATALOG'
)

""" DropFields - Remove columns """
dropped_df = DropFields.apply(
    frame=datasource,
    paths=["column_to_drop", "another_column"],
    transformation_ctx="dropped_df"
)

""" SelectFields - Keep only specific columns """
selected_df = SelectFields.apply(
    frame=datasource,
    paths=["id", "name", "email"],
    transformation_ctx="selected_df"
)

""" RenameField - Rename a single field """
renamed_df = RenameField.apply(
    frame=datasource,
    old_name="old_column_name",
    new_name="new_column_name",
    transformation_ctx="renamed_df"
)

""" Filter - Filter records """
filtered_df = Filter.apply(
    frame=datasource,
    f=lambda x: x["age"] > 30,
    transformation_ctx="filtered_df"
)

""" DropDuplicates - Remove duplicate records """
deduplicated_df = DropDuplicates.apply(
    frame=datasource,
    transformation_ctx="deduplicated_df"
)

""" Join - Join two DynamicFrames """
joined_df = Join.apply(
    frame1=df1,
    frame2=df2,
    keys1=["id"],
    keys2=["customer_id"],
    transformation_ctx="joined_df"
)

""" SplitFields - Split DynamicFrame into multiple """
split_df = SplitFields.apply(
    frame=datasource,
    paths=[["id", "name"], ["email", "phone"]],
    transformation_ctx="split_df"
)

""" Relationalize - Flatten nested structures """
relationalized = datasource.relationalize(
    root_table_name="root",
    staging_path="s3://my-bucket/temp/"
)

# ============================================================================
# 6. GLUE JOB BOOKMARKS
# ============================================================================

""" Enable Job Bookmarks for Incremental Processing """
# Job bookmarks track processed data to avoid reprocessing

# Read with job bookmarks
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="my_db",
    table_name="orders",
    transformation_ctx="orders",
    additional_options={
        "jobBookmarkKeys": ["order_id"],
        "jobBookmarkKeysSortOrder": "asc"
    }
)

# Job bookmarks are automatically managed by Glue
# Enable in job configuration: --job-bookmark-option job-bookmark-enable

""" Reset Job Bookmark """
# AWS CLI command:
# aws glue reset-job-bookmark --job-name my-job-name

# ============================================================================
# 7. AWS LAMBDA FUNCTIONS
# ============================================================================

""" Lambda Function to Trigger Glue Job """
import boto3
import datetime

def lambda_handler(event, context):
    glue = boto3.client('glue')
    
    # Determine load type based on date
    today = datetime.datetime.now()
    load_type = 'full' if today.day == 1 else 'incremental'
    
    # Start Glue job
    response = glue.start_job_run(
        JobName='PMIDataGlueJob',
        Arguments={
            '--load_type': load_type,
            '--source_path': 's3://my-bucket/input/',
            '--target_path': 's3://my-bucket/output/'
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Triggered Glue job with {load_type} load',
            'jobRunId': response['JobRunId']
        })
    }

""" Lambda Function to Process S3 Events """
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    glue = boto3.client('glue')
    
    # Get bucket and key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"Processing file: s3://{bucket}/{key}")
    
    # Trigger Glue crawler or job
    response = glue.start_crawler(Name='my-crawler')
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processing initiated')
    }

""" Lambda Function with Error Handling """
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        glue = boto3.client('glue')
        
        response = glue.start_job_run(
            JobName='my-etl-job',
            Arguments={'--param1': 'value1'}
        )
        
        logger.info(f"Job started successfully: {response['JobRunId']}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'jobRunId': response['JobRunId']})
        }
        
    except Exception as e:
        logger.error(f"Error starting job: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

# ============================================================================
# 8. S3 OPERATIONS
# ============================================================================

""" S3 Client Operations """
import boto3

s3_client = boto3.client('s3')

# Create bucket
s3_client.create_bucket(
    Bucket='my-new-bucket',
    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
)

# Upload file
s3_client.upload_file('local_file.txt', 'my-bucket', 'remote_file.txt')

# Download file
s3_client.download_file('my-bucket', 'remote_file.txt', 'local_file.txt')

# List buckets
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# List objects in bucket
response = s3_client.list_objects_v2(Bucket='my-bucket', Prefix='path/')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Delete object
s3_client.delete_object(Bucket='my-bucket', Key='remote_file.txt')

# Put object
s3_client.put_object(
    Bucket='my-bucket',
    Key='new_file.txt',
    Body='Hello, World!'
)

# Copy object
s3_client.copy_object(
    Bucket='destination-bucket',
    CopySource={'Bucket': 'source-bucket', 'Key': 'file.txt'},
    Key='copied_file.txt'
)

""" List all CSV files in S3 bucket """
def list_csv_files(bucket_name, prefix=''):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    files = [content['Key'] for content in response.get('Contents', []) 
             if content['Key'].endswith('.csv')]
    return files

# ============================================================================
# 9. GLUE TRIGGERS & WORKFLOWS
# ============================================================================

""" Create Scheduled Trigger """
glue_client.create_trigger(
    Name='daily-trigger',
    Type='SCHEDULED',
    Schedule='cron(0 12 * * ? *)',  # 12:00 PM UTC every day
    Actions=[
        {
            'JobName': 'my-glue-job',
            'Arguments': {
                '--load_type': 'incremental'
            }
        }
    ],
    StartOnCreation=True
)

""" Create On-Demand Trigger """
glue_client.create_trigger(
    Name='on-demand-trigger',
    Type='ON_DEMAND',
    Actions=[
        {'JobName': 'my-glue-job'}
    ]
)

""" Create Conditional Trigger """
glue_client.create_trigger(
    Name='conditional-trigger',
    Type='CONDITIONAL',
    Predicate={
        'Logical': 'AND',
        'Conditions': [
            {
                'LogicalOperator': 'EQUALS',
                'JobName': 'job1',
                'State': 'SUCCEEDED'
            }
        ]
    },
    Actions=[
        {'JobName': 'job2'}
    ],
    StartOnCreation=True
)

""" Create Workflow """
glue_client.create_workflow(
    Name='my-etl-workflow',
    Description='ETL workflow for data processing'
)

# ============================================================================
# 10. SCHEMA EVOLUTION & HANDLING
# ============================================================================

""" Handle Schema Changes """
# Use ResolveChoice to handle schema conflicts
datasource = datasource.resolveChoice(
    specs=[
        ('column1', 'cast:string'),
        ('column2', 'cast:long')
    ],
    choiceOption='MATCH_CATALOG'
)

# Use schema change policy in crawler
SchemaChangePolicy = {
    'UpdateBehavior': 'UPDATE_IN_DATABASE',  # Update schema in catalog
    'DeleteBehavior': 'LOG'  # Log deleted columns
}

""" Add Missing Columns """
# Convert to DataFrame, add columns, convert back
df = dynamic_frame.toDF()

# Add missing columns with default values
if 'new_column' not in df.columns:
    df = df.withColumn('new_column', lit(None).cast('string'))

# Convert back to DynamicFrame
dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

# ============================================================================
# 11. INCREMENTAL DATA PROCESSING
# ============================================================================

""" Incremental Load with Load Type Parameter """
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'load_type'])
load_type = args['load_type']

# Read from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="pmidata_db",
    table_name="raw_pmidata_ingestion_bucket",
    transformation_ctx="datasource"
)

# Apply incremental filter if needed
if load_type == 'incremental':
    filtered_df = Filter.apply(
        frame=datasource,
        f=lambda x: x['ingestion_date'] >= '2025-08-15',
        transformation_ctx="filtered_df"
    )
else:
    filtered_df = datasource

# Write to target
glueContext.write_dynamic_frame.from_options(
    frame=filtered_df,
    connection_type="s3",
    connection_options={"path": "s3://output-bucket/data/"},
    format="parquet",
    transformation_ctx="datasink"
)

""" Incremental Load using Watermark """
# Read watermark from S3 or DynamoDB
watermark_path = "s3://my-bucket/watermark/last_processed.txt"

# Get last processed timestamp
try:
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket='my-bucket', Key='watermark/last_processed.txt')
    last_processed = obj['Body'].read().decode('utf-8')
except:
    last_processed = '1970-01-01 00:00:00'

# Filter for new records
df = datasource.toDF()
incremental_df = df.filter(col("updated_at") > last_processed)

# Process incremental data
# ... processing logic ...

# Update watermark
current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
s3.put_object(
    Bucket='my-bucket',
    Key='watermark/last_processed.txt',
    Body=current_timestamp
)

# ============================================================================
# 12. ERROR HANDLING & LOGGING
# ============================================================================

""" Error Handling in Glue Job """
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    # Read data
    datasource = glueContext.create_dynamic_frame.from_catalog(
        database="my_database",
        table_name="my_table"
    )
    
    logger.info(f"Successfully read {datasource.count()} records")
    
    # Apply transformations
    transformed = ApplyMapping.apply(
        frame=datasource,
        mappings=[("id", "long", "id", "long")]
    )
    
    # Write data
    glueContext.write_dynamic_frame.from_options(
        frame=transformed,
        connection_type="s3",
        connection_options={"path": "s3://my-bucket/output/"},
        format="parquet"
    )
    
    logger.info("Job completed successfully")
    
except Exception as e:
    logger.error(f"Job failed with error: {str(e)}")
    raise

""" Write Error Records to Separate Location """
from pyspark.sql.functions import col

# Separate good and bad records
df = datasource.toDF()

# Define validation rules
good_records = df.filter(
    (col("id").isNotNull()) &
    (col("email").rlike(r'^[\w\.-]+@[\w\.-]+\.\w+$'))
)

bad_records = df.subtract(good_records)

# Write good records to main output
DynamicFrame.fromDF(good_records, glueContext, "good").write \
    .mode("append") \
    .parquet("s3://my-bucket/output/")

# Write bad records to error location
DynamicFrame.fromDF(bad_records, glueContext, "bad").write \
    .mode("append") \
    .parquet("s3://my-bucket/errors/")

""" CloudWatch Metrics """
# Glue automatically sends metrics to CloudWatch
# Custom metrics can be added using boto3

cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_data(
    Namespace='GlueJobs',
    MetricData=[
        {
            'MetricName': 'RecordsProcessed',
            'Value': record_count,
            'Unit': 'Count',
            'Timestamp': datetime.now()
        }
    ]
)

# ============================================================================
# COMPLETE EXAMPLE: END-TO-END ETL JOB
# ============================================================================

"""
Complete Glue Job Example:
- Read from S3
- Apply transformations
- Handle schema changes
- Write to multiple targets
- Error handling
- Logging
"""

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import *
import logging

# Initialize
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'source_path', 'target_path'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    # Read from S3
    logger.info(f"Reading data from {args['source_path']}")
    datasource = glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [args['source_path']]},
        format="json"
    )
    
    record_count = datasource.count()
    logger.info(f"Read {record_count} records")
    
    # Apply transformations
    mapped = ApplyMapping.apply(
        frame=datasource,
        mappings=[
            ("id", "long", "customer_id", "long"),
            ("name", "string", "customer_name", "string"),
            ("email", "string", "email", "string"),
            ("created_at", "string", "created_at", "timestamp")
        ]
    )
    
    # Filter valid records
    filtered = Filter.apply(
        frame=mapped,
        f=lambda x: x["customer_id"] is not None and x["email"] is not None
    )
    
    # Remove duplicates
    deduplicated = DropDuplicates.apply(frame=filtered)
    
    # Write to S3 as Parquet
    logger.info(f"Writing data to {args['target_path']}")
    glueContext.write_dynamic_frame.from_options(
        frame=deduplicated,
        connection_type="s3",
        connection_options={"path": args['target_path']},
        format="parquet",
        format_options={"compression": "snappy"}
    )
    
    logger.info("Job completed successfully")
    
except Exception as e:
    logger.error(f"Job failed: {str(e)}")
    raise
    
finally:
    job.commit()

"""
================================================================================
END OF AWS GLUE & SERVICES GUIDE
================================================================================
"""
