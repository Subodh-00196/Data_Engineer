"""
================================================================================
                APACHE AIRFLOW - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive Apache Airflow examples for workflow orchestration
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. AIRFLOW BASICS & CONCEPTS
2. DAG DEFINITION
3. OPERATORS (BASH, PYTHON, SQL)
4. TASK DEPENDENCIES
5. XCOMS (CROSS-COMMUNICATION)
6. SENSORS
7. BRANCHING & CONDITIONAL LOGIC
8. DYNAMIC DAGS
9. TASKFLOW API (@task decorator)
10. BEST PRACTICES
================================================================================
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.task_group import TaskGroup
from airflow.decorators import dag, task

# ============================================================================
# 1. AIRFLOW BASICS & CONCEPTS
# ============================================================================

"""
AIRFLOW ARCHITECTURE:
- Scheduler: Triggers scheduled workflows
- Executor: Runs tasks (Local, Celery, Kubernetes, etc.)
- Web Server: UI for monitoring and management
- Metadata Database: Stores DAG and task state
- Workers: Execute tasks (in distributed executors)

KEY CONCEPTS:
- DAG: Directed Acyclic Graph (workflow definition)
- Task: Unit of work
- Operator: Template for a task
- Sensor: Waits for condition to be met
- Hook: Interface to external systems
- XCom: Cross-communication between tasks
- Pool: Limit concurrent tasks
- Connection: Store credentials for external systems

DAG STATES:
- running: Currently executing
- success: Completed successfully
- failed: Failed execution

TASK STATES:
- none: Not yet scheduled
- scheduled: Scheduled to run
- queued: Waiting for executor
- running: Currently executing
- success: Completed successfully
- failed: Failed execution
- skipped: Skipped by branching
- upstream_failed: Upstream task failed
- up_for_retry: Will retry
- up_for_reschedule: Sensor rescheduling
"""

# ============================================================================
# 2. DAG DEFINITION
# ============================================================================

""" Basic DAG Definition """
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email': ['alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=1)
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='Example ETL DAG',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example', 'etl']
)

""" Schedule Intervals """
# Cron expressions
# '0 2 * * *'        # Daily at 2 AM
# '0 */4 * * *'      # Every 4 hours
# '0 0 * * 0'        # Weekly on Sunday
# '0 0 1 * *'        # Monthly on 1st

# Airflow presets
# '@once'            # Run once
# '@hourly'          # Every hour
# '@daily'           # Every day at midnight
# '@weekly'          # Every Sunday
# '@monthly'         # First day of month
# '@yearly'          # January 1st
# None               # Manual trigger only

""" DAG with Context Manager """
with DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    
    # Tasks defined here
    pass

# ============================================================================
# 3. OPERATORS
# ============================================================================

""" PythonOperator """
def extract_data(**context):
    """Extract data from source"""
    execution_date = context['execution_date']
    print(f"Extracting data for {execution_date}")
    
    # Simulate data extraction
    data = {'records': 1000, 'date': str(execution_date)}
    
    # Push to XCom
    context['task_instance'].xcom_push(key='extracted_data', value=data)
    
    return data

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    provide_context=True,
    dag=dag
)

""" BashOperator """
run_script = BashOperator(
    task_id='run_etl_script',
    bash_command='python /path/to/etl_script.py --date {{ ds }}',
    dag=dag
)

""" PostgresOperator """
create_table = PostgresOperator(
    task_id='create_table',
    postgres_conn_id='postgres_default',
    sql="""
        CREATE TABLE IF NOT EXISTS sales_summary (
            date DATE,
            total_sales DECIMAL(10,2),
            num_transactions INT
        );
    """,
    dag=dag
)

""" S3 Operator """
create_s3_bucket = S3CreateBucketOperator(
    task_id='create_s3_bucket',
    bucket_name='my-data-bucket',
    aws_conn_id='aws_default',
    dag=dag
)

""" DummyOperator (for structure) """
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# ============================================================================
# 4. TASK DEPENDENCIES
# ============================================================================

""" Linear Dependencies """
task1 >> task2 >> task3  # task1 then task2 then task3

""" Multiple Dependencies """
task1 >> [task2, task3]  # task1 then both task2 and task3 in parallel
[task2, task3] >> task4  # Both task2 and task3 then task4

""" Complex Dependencies """
start >> extract_task >> [transform_task1, transform_task2]
[transform_task1, transform_task2] >> load_task >> end

""" Using set_upstream and set_downstream """
task2.set_upstream(task1)  # Same as task1 >> task2
task3.set_downstream(task4)  # Same as task3 >> task4

# ============================================================================
# 5. XCOMS (CROSS-COMMUNICATION)
# ============================================================================

""" Push to XCom """
def push_function(**context):
    value = {'key': 'value', 'number': 42}
    context['task_instance'].xcom_push(key='my_key', value=value)
    return value  # Return value is automatically pushed to XCom

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_function,
    dag=dag
)

""" Pull from XCom """
def pull_function(**context):
    # Pull specific key
    value = context['task_instance'].xcom_pull(
        task_ids='push_task',
        key='my_key'
    )
    
    # Pull return value
    return_value = context['task_instance'].xcom_pull(task_ids='push_task')
    
    print(f"Pulled value: {value}")
    print(f"Return value: {return_value}")

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_function,
    dag=dag
)

push_task >> pull_task

# ============================================================================
# 6. SENSORS
# ============================================================================

""" FileSensor - Wait for file """
wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/path/to/file.csv',
    poke_interval=60,  # Check every 60 seconds
    timeout=3600,  # Timeout after 1 hour
    mode='poke',  # 'poke' or 'reschedule'
    dag=dag
)

""" S3KeySensor - Wait for S3 object """
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

wait_for_s3_file = S3KeySensor(
    task_id='wait_for_s3_file',
    bucket_name='my-bucket',
    bucket_key='data/file.csv',
    aws_conn_id='aws_default',
    timeout=3600,
    poke_interval=60,
    dag=dag
)

""" Custom Sensor """
from airflow.sensors.base import BaseSensorOperator

class CustomSensor(BaseSensorOperator):
    def poke(self, context):
        # Custom logic to check condition
        # Return True when condition is met
        return check_condition()

# ============================================================================
# 7. BRANCHING & CONDITIONAL LOGIC
# ============================================================================

""" BranchPythonOperator """
from airflow.operators.python import BranchPythonOperator

def choose_branch(**context):
    execution_date = context['execution_date']
    
    if execution_date.day == 1:
        return 'full_load_task'
    else:
        return 'incremental_load_task'

branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=choose_branch,
    dag=dag
)

full_load = DummyOperator(task_id='full_load_task', dag=dag)
incremental_load = DummyOperator(task_id='incremental_load_task', dag=dag)

branch_task >> [full_load, incremental_load]

""" ShortCircuitOperator """
from airflow.operators.python import ShortCircuitOperator

def check_condition(**context):
    # Return False to skip downstream tasks
    return True

check_task = ShortCircuitOperator(
    task_id='check_condition',
    python_callable=check_condition,
    dag=dag
)

# ============================================================================
# 8. DYNAMIC DAGS
# ============================================================================

""" Generate DAGs Dynamically """
# Create multiple DAGs from configuration
DATABASES = ['db1', 'db2', 'db3']

for db in DATABASES:
    dag_id = f'etl_{db}'
    
    default_args = {
        'owner': 'data_engineer',
        'start_date': datetime(2024, 1, 1)
    }
    
    dag = DAG(
        dag_id,
        default_args=default_args,
        schedule_interval='@daily',
        catchup=False
    )
    
    extract = PythonOperator(
        task_id='extract',
        python_callable=lambda db=db: print(f"Extracting from {db}"),
        dag=dag
    )
    
    globals()[dag_id] = dag

""" Dynamic Task Generation """
with DAG('dynamic_tasks', start_date=datetime(2024, 1, 1)) as dag:
    
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')
    
    # Generate tasks dynamically
    tables = ['customers', 'orders', 'products']
    
    for table in tables:
        task = PythonOperator(
            task_id=f'process_{table}',
            python_callable=lambda t=table: print(f"Processing {t}")
        )
        
        start >> task >> end

# ============================================================================
# 9. TASKFLOW API (@task decorator)
# ============================================================================

""" Modern TaskFlow API """
@dag(
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['taskflow']
)
def etl_taskflow():
    
    @task
    def extract():
        """Extract data"""
        data = {'records': 1000}
        return data
    
    @task
    def transform(data: dict):
        """Transform data"""
        data['transformed'] = True
        return data
    
    @task
    def load(data: dict):
        """Load data"""
        print(f"Loading {data}")
    
    # Define workflow
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

# Instantiate DAG
etl_dag = etl_taskflow()

""" TaskFlow with Multiple Outputs """
@dag(schedule_interval='@daily', start_date=datetime(2024, 1, 1))
def multi_output_dag():
    
    @task(multiple_outputs=True)
    def extract_multiple():
        return {
            'customers': [1, 2, 3],
            'orders': [10, 20, 30]
        }
    
    @task
    def process_customers(customers):
        print(f"Processing customers: {customers}")
    
    @task
    def process_orders(orders):
        print(f"Processing orders: {orders}")
    
    data = extract_multiple()
    process_customers(data['customers'])
    process_orders(data['orders'])

multi_dag = multi_output_dag()

# ============================================================================
# 10. BEST PRACTICES
# ============================================================================

"""
AIRFLOW BEST PRACTICES:

1. DAG DESIGN:
   - Keep DAGs simple and focused
   - Use meaningful task IDs
   - Set appropriate timeouts
   - Use tags for organization
   - Set catchup=False for new DAGs

2. TASK DESIGN:
   - Make tasks idempotent
   - Keep tasks atomic
   - Use appropriate operators
   - Set retries and retry_delay
   - Handle failures gracefully

3. DEPENDENCIES:
   - Minimize cross-DAG dependencies
   - Use sensors for external dependencies
   - Avoid circular dependencies
   - Use task groups for organization

4. PERFORMANCE:
   - Use pools to limit concurrency
   - Set appropriate parallelism
   - Use appropriate executor
   - Monitor task duration
   - Optimize SQL queries

5. XCOMS:
   - Limit XCom size (< 1MB)
   - Use external storage for large data
   - Clean up old XComs
   - Use meaningful keys

6. MONITORING:
   - Set up email alerts
   - Monitor DAG run duration
   - Track task failures
   - Use SLAs
   - Set up logging

7. TESTING:
   - Test DAGs locally
   - Use pytest for unit tests
   - Validate DAG structure
   - Test task logic separately

8. SECURITY:
   - Use Connections for credentials
   - Encrypt sensitive data
   - Use RBAC
   - Audit DAG changes
   - Limit access to production

9. MAINTENANCE:
   - Clean up old DAG runs
   - Archive completed DAGs
   - Update Airflow regularly
   - Monitor database size
   - Document DAGs

10. CODE ORGANIZATION:
    - Use separate files for DAGs
    - Create reusable functions
    - Use configuration files
    - Version control DAGs
    - Follow naming conventions
"""

""" Complete Example: Production ETL DAG """
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

default_args = {
    'owner': 'data_team',
    'depends_on_past': False,
    'email': ['data-alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=2)
}

@dag(
    dag_id='production_etl_pipeline',
    default_args=default_args,
    description='Production ETL pipeline for sales data',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['production', 'etl', 'sales']
)
def production_etl():
    
    @task
    def validate_source_data(**context):
        """Validate source data availability"""
        execution_date = context['execution_date']
        logger.info(f"Validating data for {execution_date}")
        
        # Validation logic
        is_valid = True  # Replace with actual validation
        
        if not is_valid:
            raise ValueError("Source data validation failed")
        
        return {'status': 'valid', 'date': str(execution_date)}
    
    @task
    def extract_from_source(**context):
        """Extract data from source system"""
        logger.info("Extracting data from source")
        
        # Extract logic
        record_count = 10000  # Replace with actual extraction
        
        return {'record_count': record_count}
    
    @task
    def transform_data(extract_result: dict):
        """Transform extracted data"""
        logger.info(f"Transforming {extract_result['record_count']} records")
        
        # Transformation logic
        transformed_count = extract_result['record_count']
        
        return {'transformed_count': transformed_count}
    
    @task
    def load_to_warehouse(transform_result: dict):
        """Load data to warehouse"""
        logger.info(f"Loading {transform_result['transformed_count']} records")
        
        # Load logic
        return {'status': 'success'}
    
    @task
    def send_notification(load_result: dict):
        """Send completion notification"""
        logger.info(f"ETL completed with status: {load_result['status']}")
        
        # Send notification (email, Slack, etc.)
        return True
    
    # Define workflow
    validation = validate_source_data()
    extraction = extract_from_source()
    transformation = transform_data(extraction)
    loading = load_to_warehouse(transformation)
    notification = send_notification(loading)
    
    validation >> extraction

# Instantiate DAG
prod_dag = production_etl()

"""
================================================================================
END OF AIRFLOW ORCHESTRATION GUIDE
================================================================================
"""
