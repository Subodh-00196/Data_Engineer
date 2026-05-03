# Python for Data Engineers - Part 2: OOP, Exception Handling & Logging

## Table of Contents
5. [Object-Oriented Programming for ETL](#5-object-oriented-programming-for-etl)
6. [Exception Handling & Logging](#6-exception-handling--logging)
7. [File Handling & OS Operations](#7-file-handling--os-operations)

---

# 5. Object-Oriented Programming for ETL

## 5.1 Classes for Reusable Pipeline Design

```python
class BasePipeline:
    """
    Base class for all ETL pipelines.
    Implements common patterns and template method.
    """
    
    def __init__(self, pipeline_name, config=None):
        self.pipeline_name = pipeline_name
        self.config = config or {}
        self.metrics = {
            'extracted': 0,
            'transformed': 0,
            'loaded': 0,
            'failed': 0
        }
    
    def extract(self):
        """Override this method in subclass"""
        raise NotImplementedError("Subclass must implement extract()")
    
    def transform(self, records):
        """Override this method in subclass"""
        raise NotImplementedError("Subclass must implement transform()")
    
    def load(self, records):
        """Override this method in subclass"""
        raise NotImplementedError("Subclass must implement load()")
    
    def validate(self, record):
        """Default validation - can be overridden"""
        return record is not None and len(record) > 0
    
    def run(self):
        """
        Template method - defines pipeline execution flow.
        Subclasses customize by overriding extract/transform/load.
        """
        print(f"Starting pipeline: {self.pipeline_name}")
        
        try:
            # Extract
            print("Step 1: Extracting data...")
            raw_data = self.extract()
            self.metrics['extracted'] = len(raw_data)
            print(f"Extracted {self.metrics['extracted']} records")
            
            # Transform
            print("Step 2: Transforming data...")
            transformed_data = self.transform(raw_data)
            self.metrics['transformed'] = len(transformed_data)
            print(f"Transformed {self.metrics['transformed']} records")
            
            # Load
            print("Step 3: Loading data...")
            self.load(transformed_data)
            self.metrics['loaded'] = self.metrics['transformed']
            print(f"Loaded {self.metrics['loaded']} records")
            
            print(f"Pipeline {self.pipeline_name} completed successfully")
            return self.metrics
            
        except Exception as e:
            print(f"Pipeline {self.pipeline_name} failed: {e}")
            raise
    
    def get_metrics(self):
        """Return pipeline execution metrics"""
        return self.metrics.copy()


class PostgresPipeline(BasePipeline):
    """
    Concrete pipeline for Postgres -> Transformation -> Storage.
    """
    
    def __init__(self, pipeline_name, source_config, target_config):
        super().__init__(pipeline_name)
        self.source_config = source_config
        self.target_config = target_config
    
    def extract(self):
        """Extract from Postgres database"""
        print(f"Connecting to Postgres: {self.source_config['host']}")
        
        # In production:
        # import psycopg2
        # conn = psycopg2.connect(**self.source_config)
        # cursor = conn.cursor()
        # cursor.execute(self.source_config['query'])
        # records = cursor.fetchall()
        
        # Simulated data
        records = [
            {'id': 1, 'name': 'Alice', 'amount': 100},
            {'id': 2, 'name': 'Bob', 'amount': 200},
            {'id': 3, 'name': 'Charlie', 'amount': 150}
        ]
        
        return records
    
    def transform(self, records):
        """Apply business transformations"""
        transformed = []
        
        for record in records:
            if not self.validate(record):
                self.metrics['failed'] += 1
                continue
            
            # Business logic transformations
            transformed_record = {
                'user_id': record['id'],
                'user_name': record['name'].upper(),
                'transaction_amount': round(record['amount'] * 1.1, 2),  # 10% markup
                'processed_date': '2024-01-01'
            }
            
            transformed.append(transformed_record)
        
        return transformed
    
    def load(self, records):
        """Load to target database"""
        print(f"Loading to target: {self.target_config['table']}")
        
        # In production:
        # db.insert_many(self.target_config['table'], records)
        
        # Simulated
        for record in records:
            print(f"Inserting: {record}")
        
        return len(records)


class SnowflakePipeline(BasePipeline):
    """Pipeline for Snowflake data warehouse"""
    
    def __init__(self, pipeline_name, account, warehouse, database, schema):
        super().__init__(pipeline_name)
        self.account = account
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
    
    def extract(self):
        """Extract from Snowflake"""
        print(f"Extracting from Snowflake: {self.database}.{self.schema}")
        
        # In production:
        # import snowflake.connector
        # conn = snowflake.connector.connect(
        #     account=self.account,
        #     warehouse=self.warehouse,
        #     database=self.database,
        #     schema=self.schema
        # )
        
        return [{'id': i, 'sale_amount': i * 100} for i in range(1, 6)]
    
    def transform(self, records):
        """Transform for analytics"""
        return [
            {
                'sale_id': r['id'],
                'amount_usd': r['sale_amount'],
                'amount_eur': round(r['sale_amount'] * 0.85, 2)
            }
            for r in records
        ]
    
    def load(self, records):
        """Load to Snowflake target table"""
        print(f"Loading {len(records)} records to Snowflake")
        pass


# Usage
if __name__ == "__main__":
    # Create and run Postgres pipeline
    pg_pipeline = PostgresPipeline(
        pipeline_name="postgres_etl",
        source_config={'host': 'localhost', 'database': 'source_db'},
        target_config={'table': 'target_table'}
    )
    
    metrics = pg_pipeline.run()
    print(f"Metrics: {metrics}")
```

## 5.2 Inheritance and Polymorphism

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DataSource(ABC):
    """Abstract base class for data sources"""
    
    @abstractmethod
    def connect(self):
        """Establish connection to data source"""
        pass
    
    @abstractmethod
    def read(self, query: str) -> List[Dict]:
        """Read data from source"""
        pass
    
    @abstractmethod
    def close(self):
        """Close connection"""
        pass


class PostgresSource(DataSource):
    """Postgres implementation"""
    
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
    
    def connect(self):
        """Connect to Postgres"""
        print(f"Connecting to Postgres: {self.host}:{self.port}/{self.database}")
        # import psycopg2
        # self.connection = psycopg2.connect(...)
        self.connection = "postgres_connection"
    
    def read(self, query: str) -> List[Dict]:
        """Execute SQL query"""
        if not self.connection:
            self.connect()
        
        print(f"Executing query: {query}")
        return [{'id': 1, 'data': 'sample'}]
    
    def close(self):
        """Close connection"""
        if self.connection:
            print("Closing Postgres connection")
            self.connection = None


class MongoDBSource(DataSource):
    """MongoDB implementation"""
    
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = None
        self.db = None
    
    def connect(self):
        """Connect to MongoDB"""
        print(f"Connecting to MongoDB: {self.host}:{self.port}/{self.database}")
        self.client = "mongo_client"
        self.db = "mongo_database"
    
    def read(self, query: str) -> List[Dict]:
        """Execute MongoDB query"""
        if not self.client:
            self.connect()
        
        print(f"Executing MongoDB query: {query}")
        return [{'_id': '123', 'data': 'sample'}]
    
    def close(self):
        """Close connection"""
        if self.client:
            print("Closing MongoDB connection")
            self.client = None


class APISource(DataSource):
    """REST API implementation"""
    
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = None
    
    def connect(self):
        """Initialize API session"""
        # import requests
        # self.session = requests.Session()
        # self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
        print(f"API session initialized for {self.base_url}")
    
    def read(self, query: str) -> List[Dict]:
        """Make API request"""
        if not self.session:
            self.connect()
        
        endpoint = query
        url = f"{self.base_url}/{endpoint}"
        print(f"Making API request: {url}")
        return [{'id': 1, 'data': 'api_data'}]
    
    def close(self):
        """Close session"""
        if self.session:
            # self.session.close()
            print("API session closed")


# Polymorphism in action - same interface, different implementations
class UniversalETL:
    """ETL that works with any DataSource"""
    
    def __init__(self, source: DataSource, destination: DataSource):
        self.source = source
        self.destination = destination
    
    def run(self, source_query: str, dest_query: str):
        """
        Run ETL from any source to any destination.
        Polymorphism allows this to work with Postgres, MongoDB, API, etc.
        """
        try:
            # Extract
            print("=== EXTRACT ===")
            data = self.source.read(source_query)
            print(f"Extracted {len(data)} records")
            
            # Transform (simplified)
            print("=== TRANSFORM ===")
            transformed = self.transform(data)
            print(f"Transformed {len(transformed)} records")
            
            # Load
            print("=== LOAD ===")
            print(f"Would load {len(transformed)} records to destination")
            
        finally:
            self.source.close()
            self.destination.close()
    
    def transform(self, records):
        """Simple transformation"""
        return [{'transformed': True, **record} for record in records]
```

## 5.3 Composition Over Inheritance

```python
# Instead of deep inheritance hierarchies, use composition

class Extractor:
    """Handles data extraction"""
    
    def __init__(self, source_config):
        self.source_config = source_config
    
    def extract(self):
        print(f"Extracting from {self.source_config['type']}")
        return [{'id': 1}, {'id': 2}]


class Transformer:
    """Handles data transformation"""
    
    def __init__(self, rules):
        self.rules = rules
    
    def transform(self, records):
        print(f"Applying {len(self.rules)} transformation rules")
        return records


class Loader:
    """Handles data loading"""
    
    def __init__(self, dest_config):
        self.dest_config = dest_config
    
    def load(self, records):
        print(f"Loading {len(records)} records to {self.dest_config['table']}")
        return len(records)


class ErrorHandler:
    """Handles errors and retries"""
    
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
    
    def execute_with_retry(self, func, *args, **kwargs):
        """Execute function with retry logic"""
        import time
        
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise
                print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                time.sleep(2 ** attempt)


class Logger:
    """Handles logging"""
    
    def __init__(self, name):
        self.name = name
    
    def log(self, message):
        print(f"[{self.name}] {message}")


class ComposedPipeline:
    """
    Pipeline built through composition.
    More flexible than inheritance - can mix and match components.
    """
    
    def __init__(
        self,
        extractor: Extractor,
        transformer: Transformer,
        loader: Loader,
        error_handler: ErrorHandler = None,
        logger: Logger = None
    ):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
        self.error_handler = error_handler or ErrorHandler()
        self.logger = logger or Logger("Pipeline")
    
    def run(self):
        """Execute pipeline using composed components"""
        self.logger.log("Starting pipeline")
        
        # Extract
        records = self.error_handler.execute_with_retry(self.extractor.extract)
        self.logger.log(f"Extracted {len(records)} records")
        
        # Transform
        transformed = self.error_handler.execute_with_retry(
            self.transformer.transform,
            records
        )
        self.logger.log(f"Transformed {len(transformed)} records")
        
        # Load
        loaded_count = self.error_handler.execute_with_retry(
            self.loader.load,
            transformed
        )
        self.logger.log(f"Loaded {loaded_count} records")
        
        self.logger.log("Pipeline completed")


# Usage - build custom pipeline from components
if __name__ == "__main__":
    extractor = Extractor({'type': 'postgres', 'host': 'localhost'})
    transformer = Transformer(['rule1', 'rule2', 'rule3'])
    loader = Loader({'table': 'target_table'})
    
    pipeline = ComposedPipeline(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )
    
    pipeline.run()
```

## 5.4 Design Patterns for Data Engineering

### Factory Pattern - Create different source connectors

```python
class SourceFactory:
    """Factory for creating data source connections"""
    
    @staticmethod
    def create_source(source_type: str, config: dict) -> DataSource:
        """Create appropriate data source based on type"""
        if source_type == 'postgres':
            return PostgresSource(
                host=config['host'],
                port=config.get('port', 5432),
                database=config['database'],
                user=config['user'],
                password=config['password']
            )
        elif source_type == 'mongodb':
            return MongoDBSource(
                host=config['host'],
                port=config.get('port', 27017),
                database=config['database']
            )
        elif source_type == 'api':
            return APISource(
                base_url=config['base_url'],
                api_key=config['api_key']
            )
        else:
            raise ValueError(f"Unknown source type: {source_type}")

# Usage
config = {
    'host': 'localhost',
    'port': 5432,
    'database': 'mydb',
    'user': 'user',
    'password': 'pass'
}

source = SourceFactory.create_source('postgres', config)
data = source.read("SELECT * FROM users")
source.close()
```

### Singleton Pattern - Database connection pool

```python
class ConnectionPool:
    """Singleton connection pool for database connections"""
    
    _instance = None
    _pool = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_connection(self, name: str, config: dict):
        """Get or create connection by name"""
        if name not in self._pool:
            print(f"Creating new connection: {name}")
            # In production: create actual connection
            self._pool[name] = f"connection_{name}"
        else:
            print(f"Reusing existing connection: {name}")
        
        return self._pool[name]
    
    def close_all(self):
        """Close all connections in pool"""
        for name, conn in self._pool.items():
            print(f"Closing connection: {name}")
        self._pool.clear()

# Usage - always returns same instance
pool1 = ConnectionPool()
pool2 = ConnectionPool()
print(pool1 is pool2)  # True - same instance

conn1 = pool1.get_connection('db1', {'host': 'localhost'})
conn2 = pool2.get_connection('db1', {'host': 'localhost'})  # Reuses same connection
```

---

# 6. Exception Handling & Logging

## 6.1 Try-Except-Finally Patterns

```python
# Basic exception handling
def read_file_safe(filepath):
    """Read file with error handling"""
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return None
    except Exception as e:
        print(f"Unexpected error reading {filepath}: {e}")
        return None

# Finally block - always executes
def process_with_cleanup(data_file):
    """Process data with guaranteed cleanup"""
    connection = None
    
    try:
        # Setup
        connection = connect_to_database()
        
        # Process
        data = read_file_safe(data_file)
        if data:
            load_data(connection, data)
        
        return True
        
    except Exception as e:
        print(f"Processing failed: {e}")
        return False
        
    finally:
        # Cleanup - always runs
        if connection:
            connection.close()
            print("Connection closed")

# Production pattern: Database transaction
def execute_transaction(queries):
    """Execute multiple queries in a transaction"""
    conn = None
    cursor = None
    
    try:
        # Begin transaction
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Execute queries
        for query in queries:
            cursor.execute(query)
        
        # Commit if all succeed
        conn.commit()
        print("Transaction committed successfully")
        return True
        
    except Exception as e:
        # Rollback on error
        if conn:
            conn.rollback()
            print(f"Transaction rolled back: {e}")
        return False
        
    finally:
        # Cleanup
        if cursor:
            cursor.close()
        if conn:
            conn.close()
```

## 6.2 Custom Exceptions

```python
# Define custom exceptions for your pipeline

class PipelineError(Exception):
    """Base exception for pipeline errors"""
    pass

class ExtractionError(PipelineError):
    """Raised when data extraction fails"""
    pass

class TransformationError(PipelineError):
    """Raised when data transformation fails"""
    pass

class LoadError(PipelineError):
    """Raised when data loading fails"""
    pass

class ValidationError(PipelineError):
    """Raised when data validation fails"""
    def __init__(self, message, invalid_records=None):
        super().__init__(message)
        self.invalid_records = invalid_records or []

# Usage in pipeline
def validate_batch(records):
    """Validate batch of records"""
    invalid = []
    
    for record in records:
        if not record.get('id'):
            invalid.append({'record': record, 'error': 'Missing ID'})
        if not record.get('amount') or record['amount'] < 0:
            invalid.append({'record': record, 'error': 'Invalid amount'})
    
    if invalid:
        raise ValidationError(
            f"Found {len(invalid)} invalid records",
            invalid_records=invalid
        )
    
    return True

def run_pipeline_with_custom_exceptions():
    """Pipeline with custom exception handling"""
    try:
        # Extract
        records = extract_data()
        if not records:
            raise ExtractionError("No records extracted from source")
        
        # Validate
        validate_batch(records)
        
        # Transform
        transformed = transform_data(records)
        if len(transformed) == 0:
            raise TransformationError("Transformation produced no records")
        
        # Load
        loaded_count = load_data(transformed)
        if loaded_count != len(transformed):
            raise LoadError(f"Loaded {loaded_count} but expected {len(transformed)}")
        
        print("Pipeline completed successfully")
        
    except ValidationError as e:
        print(f"Validation failed: {e}")
        print(f"Invalid records: {len(e.invalid_records)}")
        # Log invalid records to error table
        
    except ExtractionError as e:
        print(f"Extraction failed: {e}")
        # Alert data team
        
    except TransformationError as e:
        print(f"Transformation failed: {e}")
        # Rollback and retry
        
    except LoadError as e:
        print(f"Load failed: {e}")
        # Check data integrity
        
    except PipelineError as e:
        print(f"Pipeline error: {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise  # Re-raise unexpected errors
```

## 6.3 Logging Best Practices

```python
import logging
from datetime import datetime

# Configure logging
def setup_logging(name, log_file=None, level=logging.INFO):
    """Setup logging configuration"""
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

# Usage in pipeline
class ETLPipeline:
    """ETL Pipeline with comprehensive logging"""
    
    def __init__(self, name):
        self.name = name
        self.logger = setup_logging(f"pipeline.{name}", f"{name}.log")
        self.metrics = {
            'start_time': None,
            'end_time': None,
            'records_extracted': 0,
            'records_transformed': 0,
            'records_loaded': 0,
            'errors': []
        }
    
    def run(self):
        """Run pipeline with detailed logging"""
        self.metrics['start_time'] = datetime.now()
        self.logger.info(f"Starting pipeline: {self.name}")
        
        try:
            # Extract
            self.logger.info("Step 1: Extracting data")
            records = self.extract()
            self.metrics['records_extracted'] = len(records)
            self.logger.info(f"Extracted {len(records)} records")
            
            # Transform
            self.logger.info("Step 2: Transforming data")
            transformed = self.transform(records)
            self.metrics['records_transformed'] = len(transformed)
            self.logger.info(f"Transformed {len(transformed)} records")
            
            # Load
            self.logger.info("Step 3: Loading data")
            loaded = self.load(transformed)
            self.metrics['records_loaded'] = loaded
            self.logger.info(f"Loaded {loaded} records")
            
            self.metrics['end_time'] = datetime.now()
            duration = (self.metrics['end_time'] - self.metrics['start_time']).total_seconds()
            
            self.logger.info(f"Pipeline completed successfully in {duration:.2f} seconds")
            self.logger.info(f"Metrics: {self.metrics}")
            
        except Exception as e:
            self.metrics['end_time'] = datetime.now()
            self.logger.error(f"Pipeline failed: {e}", exc_info=True)
            self.metrics['errors'].append(str(e))
            raise
    
    def extract(self):
        """Extract data with logging"""
        self.logger.debug("Connecting to source database")
        # Extraction logic
        return [{'id': i} for i in range(100)]
    
    def transform(self, records):
        """Transform data with logging"""
        self.logger.debug(f"Applying transformation rules")
        
        transformed = []
        for idx, record in enumerate(records):
            try:
                # Transformation logic
                transformed_record = {'id': record['id'], 'processed': True}
                transformed.append(transformed_record)
                
                # Log progress every 1000 records
                if (idx + 1) % 1000 == 0:
                    self.logger.debug(f"Transformed {idx + 1} records")
                    
            except Exception as e:
                self.logger.warning(f"Failed to transform record {record}: {e}")
                continue
        
        return transformed
    
    def load(self, records):
        """Load data with logging"""
        self.logger.debug(f"Loading to target database")
        # Loading logic
        return len(records)

# Different log levels for different environments
def get_log_level(environment):
    """Get appropriate log level for environment"""
    levels = {
        'dev': logging.DEBUG,
        'staging': logging.INFO,
        'prod': logging.WARNING
    }
    return levels.get(environment, logging.INFO)

# Structured logging for production
def log_pipeline_metrics(logger, metrics):
    """Log metrics in structured format (JSON-like)"""
    logger.info(
        "Pipeline metrics",
        extra={
            'pipeline_name': metrics['name'],
            'records_processed': metrics['total'],
            'duration_seconds': metrics['duration'],
            'success_rate': metrics['success_rate']
        }
    )

# Context manager for logging
from contextlib import contextmanager

@contextmanager
def log_execution(logger, operation):
    """Context manager for logging operation execution"""
    logger.info(f"Starting: {operation}")
    start_time = datetime.now()
    
    try:
        yield
        duration = (datetime.now() - start_time).total_seconds()
        logger.info(f"Completed: {operation} in {duration:.2f}s")
    except Exception as e:
        duration = (datetime.now() - start_time).total_seconds()
        logger.error(f"Failed: {operation} after {duration:.2f}s - {e}")
        raise

# Usage
logger = setup_logging("my_pipeline")

with log_execution(logger, "Extract data from API"):
    data = fetch_from_api()

with log_execution(logger, "Transform and load"):
    transformed = transform(data)
    load(transformed)
```

---

# 7. File Handling & OS Operations

## 7.1 Reading and Writing Files

```python
import os
import csv
import json
from pathlib import Path

# CSV file handling
def read_csv_file(filepath):
    """Read CSV file into list of dictionaries"""
    records = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(dict(row))
        
        print(f"Read {len(records)} records from {filepath}")
        return records
        
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def write_csv_file(filepath, records, fieldnames=None):
    """Write list of dictionaries to CSV file"""
    if not records:
        print("No records to write")
        return False
    
    # Auto-detect fieldnames if not provided
    if fieldnames is None:
        fieldnames = list(records[0].keys())
    
    try:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        
        print(f"Wrote {len(records)} records to {filepath}")
        return True
        
    except Exception as e:
        print(f"Error writing CSV: {e}")
        return False

# JSON file handling
def read_json_file(filepath):
    """Read JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filepath}: {e}")
        return None

def write_json_file(filepath, data, indent=2):
    """Write data to JSON file"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        print(f"Wrote data to {filepath}")
        return True
    except Exception as e:
        print(f"Error writing JSON: {e}")
        return False

# Production pattern: Process large CSV in batches
def process_large_csv(filepath, batch_size=1000):
    """
    Process large CSV file in batches to manage memory.
    Generator pattern - yields batches.
    """
    batch = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for idx, row in enumerate(reader, start=1):
                batch.append(dict(row))
                
                # Yield batch when full
                if len(batch) >= batch_size:
                    yield batch
                    batch = []
                
                # Progress logging
                if idx % 10000 == 0:
                    print(f"Processed {idx} rows")
            
            # Yield remaining records
            if batch:
                yield batch
                
    except Exception as e:
        print(f"Error processing CSV: {e}")
        raise

# Usage
for batch in process_large_csv('large_file.csv', batch_size=5000):
    # Process each batch
    transform_and_load(batch)
    print(f"Processed batch of {len(batch)} records")
```

## 7.2 Directory Operations

```python
from pathlib import Path
import os
import shutil
from datetime import datetime

# List files in directory
def list_data_files(directory, extension='.csv'):
    """List all data files in directory"""
    path = Path(directory)
    
    if not path.exists():
        print(f"Directory not found: {directory}")
        return []
    
    # Get all files with extension
    files = list(path.glob(f'*{extension}'))
    
    print(f"Found {len(files)} {extension} files in {directory}")
    return [str(f) for f in files]

# Recursive file search
def find_files_recursive(directory, pattern='*.csv'):
    """Find all files matching pattern recursively"""
    path = Path(directory)
    files = list(path.rglob(pattern))
    return [str(f) for f in files]

# Create directory structure
def create_data_directories(base_path):
    """Create standard data pipeline directory structure"""
    directories = [
        'raw',
        'processed',
        'archive',
        'errors',
        'logs'
    ]
    
    base = Path(base_path)
    
    for dir_name in directories:
        dir_path = base / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created: {dir_path}")

# Archive old files
def archive_old_files(source_dir, archive_dir, days_old=7):
    """
    Move files older than specified days to archive directory.
    Common pattern in data pipelines.
    """
    from datetime import datetime, timedelta
    
    source_path = Path(source_dir)
    archive_path = Path(archive_dir)
    archive_path.mkdir(parents=True, exist_ok=True)
    
    cutoff_date = datetime.now() - timedelta(days=days_old)
    archived_count = 0
    
    for file_path in source_path.glob('*'):
        if file_path.is_file():
            # Get file modification time
            mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
            
            if mod_time < cutoff_date:
                # Move to archive
                dest_path = archive_path / file_path.name
                shutil.move(str(file_path), str(dest_path))
                print(f"Archived: {file_path.name}")
                archived_count += 1
    
    print(f"Archived {archived_count} files older than {days_old} days")
    return archived_count

# File cleanup
def cleanup_processed_files(directory, keep_latest=10):
    """Keep only the N most recent files, delete others"""
    path = Path(directory)
    
    # Get all files with modification time
    files = [(f, f.stat().st_mtime) for f in path.glob('*') if f.is_file()]
    
    # Sort by modification time (newest first)
    files.sort(key=lambda x: x[1], reverse=True)
    
    # Keep latest N, delete rest
    deleted_count = 0
    for file_path, _ in files[keep_latest:]:
        file_path.unlink()
        print(f"Deleted: {file_path.name}")
        deleted_count += 1
    
    print(f"Deleted {deleted_count} old files, kept {min(len(files), keep_latest)}")
    return deleted_count

# Safe file operations with temp files
def safe_write_csv(filepath, records):
    """
    Write CSV safely using temp file.
    Only replaces original if write succeeds.
    """
    import tempfile
    
    temp_file = None
    
    try:
        # Write to temporary file first
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            temp_file = f.name
            writer = csv.DictWriter(f, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)
        
        # If write succeeded, replace original
        shutil.move(temp_file, filepath)
        print(f"Safely wrote {len(records)} records to {filepath}")
        return True
        
    except Exception as e:
        # Clean up temp file on error
        if temp_file and os.path.exists(temp_file):
            os.unlink(temp_file)
        print(f"Error writing file: {e}")
        return False

# Production pattern: Process files in directory
def process_directory_batch(input_dir, output_dir, archive_dir):
    """
    Process all files in input directory:
    1. Read and transform each file
    2. Write to output directory
    3. Archive original file
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    archive_path = Path(archive_dir)
    
    # Create directories if needed
    output_path.mkdir(parents=True, exist_ok=True)
    archive_path.mkdir(parents=True, exist_ok=True)
    
    processed_count = 0
    error_count = 0
    
    # Process each CSV file
    for input_file in input_path.glob('*.csv'):
        try:
            # Read file
            records = read_csv_file(str(input_file))
            
            # Transform
            transformed = [
                {**record, 'processed_at': datetime.now().isoformat()}
                for record in records
            ]
            
            # Write to output
            output_file = output_path / input_file.name
            write_csv_file(str(output_file), transformed)
            
            # Archive original
            archive_file = archive_path / f"{input_file.stem}_{datetime.now():%Y%m%d_%H%M%S}.csv"
            shutil.move(str(input_file), str(archive_file))
            
            processed_count += 1
            print(f"Processed: {input_file.name}")
            
        except Exception as e:
            error_count += 1
            print(f"Error processing {input_file.name}: {e}")
    
    print(f"Batch complete: {processed_count} processed, {error_count} errors")
    return processed_count, error_count
```

## 7.3 Path Operations with pathlib

```python
from pathlib import Path

# Modern path operations using pathlib (recommended)
def demonstrate_pathlib():
    """Pathlib examples for data engineering"""
    
    # Create path object
    data_dir = Path('/data/warehouse')
    
    # Join paths (OS-independent)
    user_data = data_dir / 'users' / '2024' / '01' / 'data.csv'
    print(user_data)  # /data/warehouse/users/2024/01/data.csv
    
    # Get parts of path
    print(user_data.name)       # data.csv
    print(user_data.stem)       # data
    print(user_data.suffix)     # .csv
    print(user_data.parent)     # /data/warehouse/users/2024/01
    print(user_data.parts)      # ('/', 'data', 'warehouse', 'users', '2024', '01', 'data.csv')
    
    # Check existence
    if user_data.exists():
        print("File exists")
    
    # Check type
    if user_data.is_file():
        print("Is a file")
    if user_data.is_dir():
        print("Is a directory")
    
    # Get file info
    if user_data.exists():
        stat = user_data.stat()
        print(f"Size: {stat.st_size} bytes")
        print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
    
    # Create directories
    new_dir = Path('/data/processed/2024/01')
    new_dir.mkdir(parents=True, exist_ok=True)
    
    # Iterate over directory
    for item in data_dir.iterdir():
        print(f"{'DIR' if item.is_dir() else 'FILE'}: {item.name}")
    
    # Glob patterns
    csv_files = list(data_dir.glob('**/*.csv'))  # Recursive
    json_files = list(data_dir.glob('*.json'))    # Current dir only
    
    # Read/write using pathlib
    config_file = Path('config.json')
    
    # Write
    config_file.write_text(json.dumps({'key': 'value'}))
    
    # Read
    content = config_file.read_text()
    config = json.loads(content)

# Production example: Organize data by partition
def organize_by_date_partition(source_dir, target_dir):
    """
    Organize files into date-based partitions: year/month/day/
    Common pattern for data lakes.
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    for file_path in source_path.glob('*.csv'):
        # Get file modification date
        mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
        
        # Create partition path: year=2024/month=01/day=15/
        partition_path = target_path / f"year={mod_time.year}" / \
                        f"month={mod_time.month:02d}" / \
                        f"day={mod_time.day:02d}"
        
        # Create partition directory
        partition_path.mkdir(parents=True, exist_ok=True)
        
        # Copy file to partition
        dest_file = partition_path / file_path.name
        shutil.copy2(str(file_path), str(dest_file))
        
        print(f"Partitioned: {file_path.name} -> {partition_path}")
```
