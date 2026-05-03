# Python for Data Engineers - Part 3: Concurrency & Libraries

## Table of Contents
8. [Multithreading & Multiprocessing](#8-multithreading--multiprocessing)
9. [Python for Data Engineering Libraries](#9-python-for-data-engineering-libraries)

---

# 8. Multithreading & Multiprocessing

## 8.1 Understanding the GIL (Global Interpreter Lock)

**Critical Concept:** Python's GIL allows only ONE thread to execute Python bytecode at a time.

```python
# GIL Impact:
# ✅ Threading GOOD for: I/O-bound tasks (API calls, file I/O, database queries)
# ❌ Threading BAD for: CPU-bound tasks (data transformations, calculations)
# ✅ Multiprocessing GOOD for: CPU-bound tasks (parallel processing)
# ⚠️ Multiprocessing OVERHEAD: Process creation is expensive

# I/O-bound example - Threading is beneficial
import threading
import time
import requests

def fetch_data_from_api(url):
    """I/O-bound: Waiting for network response"""
    response = requests.get(url)
    return response.json()

# CPU-bound example - Threading is NOT beneficial
def calculate_fibonacci(n):
    """CPU-bound: Intensive calculation"""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
```

## 8.2 Threading for I/O-Bound Tasks

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from queue import Queue
import time

# Pattern 1: ThreadPoolExecutor - Modern approach
def download_multiple_files(urls, max_workers=5):
    """
    Download multiple files concurrently using threads.
    Perfect for I/O-bound operations like API calls.
    """
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_url = {executor.submit(download_file, url): url for url in urls}
        
        # Process completed tasks
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results.append({'url': url, 'data': data, 'status': 'success'})
                print(f"Downloaded: {url}")
            except Exception as e:
                results.append({'url': url, 'error': str(e), 'status': 'failed'})
                print(f"Failed: {url} - {e}")
    
    return results

def download_file(url):
    """Simulate file download (I/O-bound)"""
    # In production: requests.get(url)
    time.sleep(0.5)  # Simulate network delay
    return f"data_from_{url}"

# Usage
urls = [
    'https://api.example.com/users',
    'https://api.example.com/products',
    'https://api.example.com/orders',
    'https://api.example.com/transactions',
    'https://api.example.com/analytics'
]

results = download_multiple_files(urls, max_workers=3)
print(f"Downloaded {len(results)} files")

# Pattern 2: Producer-Consumer with Queue
def producer_consumer_pattern():
    """
    Use Queue for thread-safe communication.
    Common in streaming data ingestion.
    """
    queue = Queue(maxsize=100)
    results = []
    
    def producer(queue, items):
        """Producer: Fetch data and put in queue"""
        for item in items:
            data = fetch_data(item)  # I/O operation
            queue.put(data)
            print(f"Produced: {item}")
        
        # Signal completion
        queue.put(None)
    
    def consumer(queue, results):
        """Consumer: Get from queue and process"""
        while True:
            data = queue.get()
            
            if data is None:  # Completion signal
                queue.task_done()
                break
            
            # Process data
            processed = transform_data(data)
            results.append(processed)
            print(f"Consumed: {data}")
            
            queue.task_done()
    
    # Create threads
    items = list(range(10))
    
    producer_thread = threading.Thread(target=producer, args=(queue, items))
    consumer_thread = threading.Thread(target=consumer, args=(queue, results))
    
    # Start threads
    producer_thread.start()
    consumer_thread.start()
    
    # Wait for completion
    producer_thread.join()
    consumer_thread.join()
    
    print(f"Processed {len(results)} items")
    return results

def fetch_data(item):
    """Simulate I/O operation"""
    time.sleep(0.1)
    return {'id': item, 'value': item * 10}

def transform_data(data):
    """Simulate transformation"""
    return {**data, 'transformed': True}

# Pattern 3: Parallel API Ingestion (Real-world example)
def ingest_from_multiple_apis(api_configs):
    """
    Ingest data from multiple APIs in parallel.
    Common in data engineering pipelines.
    """
    all_records = []
    errors = []
    
    def fetch_from_api(config):
        """Fetch data from single API"""
        try:
            # Simulate API call
            print(f"Fetching from {config['name']}")
            time.sleep(1)  # Network I/O
            
            # In production:
            # response = requests.get(
            #     config['url'],
            #     headers={'Authorization': f"Bearer {config['api_key']}"}
            # )
            # return response.json()
            
            return [{'source': config['name'], 'data': i} for i in range(10)]
            
        except Exception as e:
            return {'error': str(e), 'source': config['name']}
    
    with ThreadPoolExecutor(max_workers=len(api_configs)) as executor:
        futures = {executor.submit(fetch_from_api, config): config for config in api_configs}
        
        for future in as_completed(futures):
            config = futures[future]
            try:
                result = future.result()
                
                if isinstance(result, dict) and 'error' in result:
                    errors.append(result)
                else:
                    all_records.extend(result)
                    print(f"Fetched {len(result)} records from {config['name']}")
                    
            except Exception as e:
                errors.append({'source': config['name'], 'error': str(e)})
    
    print(f"Total records: {len(all_records)}, Errors: {len(errors)}")
    return all_records, errors

# Usage
api_configs = [
    {'name': 'UserAPI', 'url': 'https://api.example.com/users', 'api_key': 'key1'},
    {'name': 'ProductAPI', 'url': 'https://api.example.com/products', 'api_key': 'key2'},
    {'name': 'OrderAPI', 'url': 'https://api.example.com/orders', 'api_key': 'key3'}
]

records, errors = ingest_from_multiple_apis(api_configs)
```

## 8.3 Multiprocessing for CPU-Bound Tasks

```python
from multiprocessing import Pool, cpu_count, Process, Queue as MPQueue
import multiprocessing as mp

# Pattern 1: Process Pool for parallel processing
def process_large_dataset_parallel(records, num_workers=None):
    """
    Process large dataset using multiple CPU cores.
    Good for CPU-intensive transformations.
    """
    if num_workers is None:
        num_workers = cpu_count()
    
    # Split data into chunks
    chunk_size = len(records) // num_workers
    chunks = [records[i:i+chunk_size] for i in range(0, len(records), chunk_size)]
    
    print(f"Processing {len(records)} records using {num_workers} workers")
    
    # Process in parallel
    with Pool(processes=num_workers) as pool:
        results = pool.map(process_chunk, chunks)
    
    # Combine results
    all_results = []
    for chunk_result in results:
        all_results.extend(chunk_result)
    
    print(f"Processed {len(all_results)} records")
    return all_results

def process_chunk(chunk):
    """
    Process a chunk of data.
    This function runs in a separate process.
    """
    processed = []
    
    for record in chunk:
        # CPU-intensive transformation
        result = {
            'id': record['id'],
            'value': complex_calculation(record['value']),
            'processed_by': mp.current_process().name
        }
        processed.append(result)
    
    return processed

def complex_calculation(value):
    """Simulate CPU-intensive calculation"""
    result = 0
    for i in range(1000):
        result += (value * i) ** 0.5
    return round(result, 2)

# Usage
records = [{'id': i, 'value': i * 10} for i in range(1000)]
results = process_large_dataset_parallel(records, num_workers=4)

# Pattern 2: Process Pool with progress tracking
from multiprocessing import Manager

def process_with_progress(records):
    """Process data with shared progress counter"""
    num_workers = cpu_count()
    
    with Manager() as manager:
        # Shared counter
        progress = manager.Value('i', 0)
        lock = manager.Lock()
        
        # Create tasks with progress tracking
        tasks = [(chunk, progress, lock) for chunk in create_chunks(records, num_workers)]
        
        with Pool(processes=num_workers) as pool:
            results = pool.starmap(process_with_counter, tasks)
        
        return [item for sublist in results for item in sublist]

def process_with_counter(chunk, progress, lock):
    """Process chunk and update progress"""
    processed = []
    
    for record in chunk:
        result = process_single_record(record)
        processed.append(result)
        
        # Update progress (thread-safe)
        with lock:
            progress.value += 1
            if progress.value % 100 == 0:
                print(f"Processed {progress.value} records")
    
    return processed

def create_chunks(records, num_chunks):
    """Split records into roughly equal chunks"""
    chunk_size = len(records) // num_chunks
    return [records[i:i+chunk_size] for i in range(0, len(records), chunk_size)]

def process_single_record(record):
    """Process single record (CPU-intensive)"""
    return {**record, 'processed': True}

# Pattern 3: When NOT to use multiprocessing
def demonstrate_overhead():
    """
    Multiprocessing has overhead - not worth it for simple tasks.
    """
    import time
    
    def simple_task(x):
        return x * 2
    
    data = list(range(100))
    
    # Serial processing
    start = time.time()
    serial_results = [simple_task(x) for x in data]
    serial_time = time.time() - start
    
    # Parallel processing
    start = time.time()
    with Pool(processes=4) as pool:
        parallel_results = pool.map(simple_task, data)
    parallel_time = time.time() - start
    
    print(f"Serial: {serial_time:.4f}s")
    print(f"Parallel: {parallel_time:.4f}s")
    # Parallel is likely SLOWER due to process creation overhead!
    
    # Rule: Use multiprocessing when task duration >> process creation time

# Real-world example: Parallel file processing
def process_files_parallel(file_paths):
    """
    Process multiple large files in parallel.
    Each process handles one file.
    """
    num_workers = min(cpu_count(), len(file_paths))
    
    print(f"Processing {len(file_paths)} files with {num_workers} workers")
    
    with Pool(processes=num_workers) as pool:
        results = pool.map(process_single_file, file_paths)
    
    # Aggregate results
    total_records = sum(r['record_count'] for r in results)
    print(f"Total records processed: {total_records}")
    
    return results

def process_single_file(filepath):
    """
    Process a single file.
    Runs in separate process - has its own memory space.
    """
    import csv
    
    records = []
    
    # Read file
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CPU-intensive transformation
            processed = transform_record(dict(row))
            records.append(processed)
    
    return {
        'filepath': filepath,
        'record_count': len(records),
        'records': records
    }

def transform_record(record):
    """CPU-intensive transformation"""
    # Complex business logic
    return {**record, 'transformed': True}
```

## 8.4 Threading vs Multiprocessing Decision Guide

```python
"""
╔══════════════════════════════════════════════════════════════════╗
║  THREADING vs MULTIPROCESSING - DECISION GUIDE                   ║
╚══════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────┐
│ Use THREADING when:                                             │
├─────────────────────────────────────────────────────────────────┤
│ ✅ I/O-bound tasks (network, file, database)                    │
│ ✅ Multiple API calls                                           │
│ ✅ Downloading files                                            │
│ ✅ Database queries                                             │
│ ✅ Need shared memory between tasks                            │
│ ✅ Lightweight, fast to create threads                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Use MULTIPROCESSING when:                                       │
├─────────────────────────────────────────────────────────────────┤
│ ✅ CPU-bound tasks (calculations, transformations)              │
│ ✅ Data processing that uses significant CPU                    │
│ ✅ Need true parallelism                                        │
│ ✅ Processing large datasets                                    │
│ ✅ Complex transformations                                      │
│ ⚠️  High overhead - only worth it for substantial work          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ AVOID concurrency when:                                         │
├─────────────────────────────────────────────────────────────────┤
│ ❌ Tasks are very quick (overhead > benefit)                    │
│ ❌ Data must be processed sequentially                          │
│ ❌ Simple, fast operations                                      │
│ ❌ Complexity not worth the performance gain                    │
└─────────────────────────────────────────────────────────────────┘
"""

# Practical examples with timing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def compare_approaches():
    """Compare serial, threading, and multiprocessing"""
    
    # Test data
    data = list(range(100))
    
    # I/O-bound task
    def io_task(x):
        time.sleep(0.01)  # Simulate I/O
        return x * 2
    
    # CPU-bound task
    def cpu_task(x):
        return sum(i ** 2 for i in range(1000))
    
    print("=== I/O-BOUND TASK ===")
    
    # Serial
    start = time.time()
    [io_task(x) for x in data]
    print(f"Serial: {time.time() - start:.2f}s")
    
    # Threading
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(io_task, data))
    print(f"Threading: {time.time() - start:.2f}s")  # Much faster!
    
    # Multiprocessing
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(io_task, data))
    print(f"Multiprocessing: {time.time() - start:.2f}s")  # Slower due to overhead
    
    print("\n=== CPU-BOUND TASK ===")
    
    # Serial
    start = time.time()
    [cpu_task(x) for x in data]
    print(f"Serial: {time.time() - start:.2f}s")
    
    # Threading
    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(cpu_task, data))
    print(f"Threading: {time.time() - start:.2f}s")  # No improvement (GIL!)
    
    # Multiprocessing
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_task, data))
    print(f"Multiprocessing: {time.time() - start:.2f}s")  # Much faster!
```

---

# 9. Python for Data Engineering Libraries

## 9.1 Pandas - Data Manipulation

```python
import pandas as pd
import numpy as np

# Reading data
def read_data_sources():
    """Read from various sources"""
    
    # CSV
    df_csv = pd.read_csv('data.csv')
    
    # With specific options
    df = pd.read_csv(
        'data.csv',
        sep=',',
        encoding='utf-8',
        parse_dates=['timestamp'],
        dtype={'user_id': str},
        na_values=['NULL', 'N/A', ''],
        thousands=',',
        chunksize=10000  # Read in chunks for large files
    )
    
    # JSON
    df_json = pd.read_json('data.json')
    df_json_lines = pd.read_json('data.jsonl', lines=True)  # JSON Lines format
    
    # Excel
    df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
    
    # SQL
    # import sqlalchemy
    # engine = sqlalchemy.create_engine('postgresql://user:pass@localhost/db')
    # df_sql = pd.read_sql('SELECT * FROM users', engine)
    # df_sql = pd.read_sql_query('SELECT * FROM users WHERE active = true', engine)
    
    # Parquet
    df_parquet = pd.read_parquet('data.parquet')
    
    return df_csv

# Basic DataFrame operations
def basic_operations():
    """Essential Pandas operations for data engineering"""
    
    # Create sample data
    df = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5, 1, 2],
        'transaction_date': pd.date_range('2024-01-01', periods=7),
        'amount': [100, 200, 150, 300, 250, 120, 180],
        'status': ['success', 'success', 'failed', 'success', 'success', 'success', 'failed'],
        'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C']
    })
    
    # Inspect data
    print(df.head())           # First 5 rows
    print(df.tail(3))          # Last 3 rows
    print(df.info())           # Data types and memory usage
    print(df.describe())       # Statistical summary
    print(df.shape)            # (rows, columns)
    print(df.columns)          # Column names
    print(df.dtypes)           # Data types
    
    # Selection
    col = df['amount']                           # Single column (Series)
    cols = df[['user_id', 'amount']]            # Multiple columns (DataFrame)
    row = df.iloc[0]                            # First row by index
    row = df.loc[0]                             # First row by label
    subset = df.iloc[0:3, 0:2]                  # Rows 0-2, columns 0-1
    
    # Filtering
    successful = df[df['status'] == 'success']
    high_value = df[df['amount'] > 150]
    multiple_conditions = df[(df['amount'] > 150) & (df['status'] == 'success')]
    
    # Using isin
    category_filter = df[df['category'].isin(['A', 'B'])]
    
    # Using query (alternative syntax)
    filtered = df.query('amount > 150 and status == "success"')
    
    return df

# Aggregations and GroupBy
def aggregations_and_groupby():
    """Aggregation patterns for data engineering"""
    
    df = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 3, 3, 1],
        'date': pd.date_range('2024-01-01', periods=7),
        'amount': [100, 200, 150, 300, 250, 120, 180],
        'category': ['A', 'B', 'A', 'B', 'A', 'B', 'A']
    })
    
    # Basic aggregations
    print(df['amount'].sum())
    print(df['amount'].mean())
    print(df['amount'].max())
    print(df['amount'].min())
    print(df['amount'].count())
    
    # Multiple aggregations at once
    print(df['amount'].agg(['sum', 'mean', 'max', 'min', 'count']))
    
    # GroupBy - single column
    by_user = df.groupby('user_id')['amount'].sum()
    print(by_user)
    
    # GroupBy - multiple aggregations
    user_stats = df.groupby('user_id')['amount'].agg({
        'total': 'sum',
        'average': 'mean',
        'max': 'max',
        'count': 'count'
    })
    print(user_stats)
    
    # GroupBy - multiple columns
    category_user_stats = df.groupby(['user_id', 'category'])['amount'].sum()
    print(category_user_stats)
    
    # GroupBy with multiple aggregations per column
    multi_agg = df.groupby('user_id').agg({
        'amount': ['sum', 'mean', 'count'],
        'category': 'nunique'  # Number of unique categories
    })
    print(multi_agg)
    
    # Custom aggregation function
    def range_func(x):
        return x.max() - x.min()
    
    custom_agg = df.groupby('user_id')['amount'].agg([
        ('total', 'sum'),
        ('avg', 'mean'),
        ('range', range_func)
    ])
    print(custom_agg)
    
    # Pivot tables
    pivot = df.pivot_table(
        values='amount',
        index='user_id',
        columns='category',
        aggfunc='sum',
        fill_value=0
    )
    print(pivot)
    
    return user_stats

# Data cleaning and transformation
def data_cleaning():
    """Common data cleaning operations"""
    
    df = pd.DataFrame({
        'user_id': [1, 2, None, 4, 5],
        'email': ['alice@example.com', 'BOB@EXAMPLE.COM', 'charlie@example.com', None, 'david@example.com'],
        'amount': [100, None, 150, 300, 250],
        'date': ['2024-01-01', '2024-01-02', 'invalid', '2024-01-04', '2024-01-05']
    })
    
    # Handle missing values
    print(df.isnull().sum())         # Count nulls per column
    print(df.isna().sum())           # Same as isnull()
    
    # Drop rows with any null
    df_dropped = df.dropna()
    
    # Drop rows where specific column is null
    df_dropped = df.dropna(subset=['user_id'])
    
    # Fill nulls
    df_filled = df.fillna({
        'user_id': 0,
        'amount': df['amount'].mean(),
        'email': 'unknown@example.com'
    })
    
    # Forward fill / backward fill
    df['amount'].fillna(method='ffill')  # Forward fill
    df['amount'].fillna(method='bfill')  # Backward fill
    
    # String operations
    df['email'] = df['email'].str.lower()           # Lowercase
    df['email'] = df['email'].str.strip()           # Remove whitespace
    df['domain'] = df['email'].str.split('@').str[1]  # Extract domain
    
    # Replace values
    df['amount'] = df['amount'].replace(0, np.nan)
    
    # Data type conversion
    df['user_id'] = df['user_id'].astype('Int64')  # Nullable integer
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Convert to datetime
    
    # Remove duplicates
    df_unique = df.drop_duplicates()
    df_unique = df.drop_duplicates(subset=['user_id'], keep='first')
    
    # Apply custom function
    df['amount_doubled'] = df['amount'].apply(lambda x: x * 2 if pd.notna(x) else x)
    
    # Apply function to multiple columns
    def categorize_amount(row):
        if pd.isna(row['amount']):
            return 'unknown'
        elif row['amount'] < 150:
            return 'low'
        elif row['amount'] < 250:
            return 'medium'
        else:
            return 'high'
    
    df['amount_category'] = df.apply(categorize_amount, axis=1)
    
    return df

# Joins and merges
def joins_and_merges():
    """Combining DataFrames - crucial for ETL"""
    
    # Sample data
    users = pd.DataFrame({
        'user_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David']
    })
    
    transactions = pd.DataFrame({
        'transaction_id': [101, 102, 103, 104, 105],
        'user_id': [1, 2, 1, 3, 5],  # Note: 5 doesn't exist in users
        'amount': [100, 200, 150, 300, 250]
    })
    
    # Inner join - only matching records
    inner = pd.merge(users, transactions, on='user_id', how='inner')
    print(f"Inner join: {len(inner)} records")
    
    # Left join - all users, matching transactions
    left = pd.merge(users, transactions, on='user_id', how='left')
    print(f"Left join: {len(left)} records")
    
    # Right join - all transactions, matching users
    right = pd.merge(users, transactions, on='user_id', how='right')
    print(f"Right join: {len(right)} records")
    
    # Outer join - all records from both
    outer = pd.merge(users, transactions, on='user_id', how='outer')
    print(f"Outer join: {len(outer)} records")
    
    # Join on different column names
    users2 = users.rename(columns={'user_id': 'id'})
    merged = pd.merge(users2, transactions, left_on='id', right_on='user_id')
    
    # Join on multiple columns
    df1 = pd.DataFrame({
        'key1': ['A', 'B', 'C'],
        'key2': [1, 2, 3],
        'value1': [10, 20, 30]
    })
    
    df2 = pd.DataFrame({
        'key1': ['A', 'B', 'D'],
        'key2': [1, 2, 4],
        'value2': [100, 200, 400]
    })
    
    multi_key_merge = pd.merge(df1, df2, on=['key1', 'key2'], how='inner')
    
    # Concatenate DataFrames
    df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)  # Stack vertically
    
    return inner

# Window functions and date operations
def window_and_date_operations():
    """Advanced operations for time-series data"""
    
    df = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=10),
        'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
        'amount': [100, 150, 200, 120, 180, 220, 90, 140, 160, 200]
    })
    
    # Sort by date
    df = df.sort_values('date')
    
    # Extract date components
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_of_week'] = df['date'].dt.dayofweek
    df['day_name'] = df['date'].dt.day_name()
    
    # Date arithmetic
    df['next_week'] = df['date'] + pd.Timedelta(days=7)
    df['days_since_start'] = (df['date'] - df['date'].min()).dt.days
    
    # Rolling window - moving average
    df['rolling_avg_3'] = df['amount'].rolling(window=3).mean()
    
    # Cumulative sum
    df['cumulative_amount'] = df['amount'].cumsum()
    
    # Rank
    df['amount_rank'] = df['amount'].rank(ascending=False)
    
    # Lag and lead
    df['previous_amount'] = df['amount'].shift(1)
    df['next_amount'] = df['amount'].shift(-1)
    
    # Percent change
    df['pct_change'] = df['amount'].pct_change()
    
    # Window functions by group
    df['user_total'] = df.groupby('user_id')['amount'].transform('sum')
    df['user_rank'] = df.groupby('user_id')['amount'].rank(ascending=False)
    df['user_cumsum'] = df.groupby('user_id')['amount'].cumsum()
    
    return df

# Writing data
def write_data():
    """Export data to various formats"""
    
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'value': [100, 200, 300]
    })
    
    # CSV
    df.to_csv('output.csv', index=False)
    
    # CSV with specific options
    df.to_csv(
        'output.csv',
        index=False,
        encoding='utf-8',
        sep=',',
        header=True,
        na_rep='NULL'
    )
    
    # JSON
    df.to_json('output.json', orient='records', lines=True)  # JSON Lines
    
    # Excel
    df.to_excel('output.xlsx', sheet_name='Data', index=False)
    
    # Parquet (recommended for big data)
    df.to_parquet('output.parquet', compression='snappy')
    
    # SQL
    # df.to_sql('table_name', engine, if_exists='append', index=False)
    
    return True

# Production example: Complete ETL with Pandas
def etl_with_pandas(input_file, output_file):
    """
    Complete ETL pipeline using Pandas.
    Extract -> Transform -> Load
    """
    print(f"Starting ETL: {input_file} -> {output_file}")
    
    # EXTRACT
    print("Extracting data...")
    df = pd.read_csv(input_file)
    print(f"Extracted {len(df)} records")
    
    # TRANSFORM
    print("Transforming data...")
    
    # 1. Clean data
    df = df.dropna(subset=['user_id', 'amount'])
    df['email'] = df['email'].str.lower().str.strip()
    
    # 2. Data type conversion
    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = df['amount'].astype(float)
    
    # 3. Add derived columns
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['amount_category'] = pd.cut(
        df['amount'],
        bins=[0, 100, 500, float('inf')],
        labels=['low', 'medium', 'high']
    )
    
    # 4. Aggregations
    user_summary = df.groupby('user_id').agg({
        'amount': ['sum', 'mean', 'count'],
        'date': ['min', 'max']
    }).reset_index()
    
    # 5. Deduplicate
    df = df.drop_duplicates(subset=['user_id', 'date'])
    
    print(f"Transformed to {len(df)} records")
    
    # LOAD
    print("Loading data...")
    df.to_parquet(output_file, index=False)
    print("ETL complete!")
    
    return df
```

## 9.2 PySpark - Big Data Processing

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.window import Window

# Initialize Spark
def create_spark_session(app_name="DataEngineering"):
    """Create Spark session with configurations"""
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "2g") \
        .getOrCreate()
    
    return spark

# Reading data in PySpark
def read_spark_data(spark):
    """Read data from various sources"""
    
    # CSV
    df = spark.read.csv(
        'data.csv',
        header=True,
        inferSchema=True,  # Automatically infer data types
        sep=',',
        nullValue='NULL'
    )
    
    # With explicit schema (better performance)
    schema = StructType([
        StructField("user_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("amount", DoubleType(), True)
    ])
    
    df = spark.read.csv('data.csv', schema=schema, header=True)
    
    # JSON
    df_json = spark.read.json('data.json')
    
    # Parquet (recommended for big data)
    df_parquet = spark.read.parquet('data.parquet')
    
    # Multiple files
    df_multi = spark.read.parquet('/data/year=2024/month=*/day=*/')
    
    # SQL database
    # df_sql = spark.read \
    #     .format("jdbc") \
    #     .option("url", "jdbc:postgresql://localhost:5432/db") \
    #     .option("dbtable", "users") \
    #     .option("user", "username") \
    #     .option("password", "password") \
    #     .load()
    
    return df

# Basic DataFrame operations in Spark
def spark_operations(spark):
    """Essential PySpark operations"""
    
    # Create sample data
    data = [
        (1, "Alice", 100, "2024-01-01"),
        (2, "Bob", 200, "2024-01-02"),
        (3, "Charlie", 150, "2024-01-03"),
        (1, "Alice", 120, "2024-01-04"),
        (2, "Bob", 180, "2024-01-05")
    ]
    
    df = spark.createDataFrame(data, ["user_id", "name", "amount", "date"])
    
    # Show data
    df.show()
    df.show(5, truncate=False)
    
    # Schema
    df.printSchema()
    
    # Select columns
    df.select("user_id", "amount").show()
    df.select(F.col("user_id"), F.col("amount") * 2).show()
    
    # Filter
    df.filter(F.col("amount") > 150).show()
    df.filter((F.col("amount") > 150) & (F.col("user_id") == 1)).show()
    df.where(F.col("amount") > 150).show()  # Same as filter
    
    # Add columns
    df = df.withColumn("amount_doubled", F.col("amount") * 2)
    df = df.withColumn("is_high_value", F.when(F.col("amount") > 150, True).otherwise(False))
    
    # Rename columns
    df = df.withColumnRenamed("name", "user_name")
    
    # Drop columns
    df = df.drop("amount_doubled")
    
    # Sort
    df.orderBy("amount").show()
    df.orderBy(F.col("amount").desc()).show()
    df.orderBy(F.desc("amount")).show()
    
    # Distinct
    df.select("user_id").distinct().show()
    
    # Count
    print(f"Total records: {df.count()}")
    
    return df

# Aggregations in Spark
def spark_aggregations(spark):
    """Aggregation operations in PySpark"""
    
    data = [
        (1, "A", 100),
        (1, "B", 200),
        (2, "A", 150),
        (2, "B", 300),
        (3, "A", 250)
    ]
    
    df = spark.createDataFrame(data, ["user_id", "category", "amount"])
    
    # Basic aggregations
    df.agg(
        F.sum("amount").alias("total"),
        F.avg("amount").alias("average"),
        F.max("amount").alias("max"),
        F.min("amount").alias("min"),
        F.count("amount").alias("count")
    ).show()
    
    # GroupBy
    df.groupBy("user_id").agg(
        F.sum("amount").alias("total_amount"),
        F.avg("amount").alias("avg_amount"),
        F.count("*").alias("transaction_count")
    ).show()
    
    # GroupBy multiple columns
    df.groupBy("user_id", "category").agg(
        F.sum("amount").alias("total")
    ).show()
    
    # Multiple aggregations
    df.groupBy("user_id").agg(
        F.sum("amount").alias("total"),
        F.avg("amount").alias("average"),
        F.max("amount").alias("max"),
        F.min("amount").alias("min"),
        F.countDistinct("category").alias("unique_categories")
    ).show()
    
    return df

# Window functions in Spark
def spark_window_functions(spark):
    """Window functions for analytics"""
    
    data = [
        (1, "2024-01-01", 100),
        (1, "2024-01-02", 150),
        (1, "2024-01-03", 200),
        (2, "2024-01-01", 120),
        (2, "2024-01-02", 180)
    ]
    
    df = spark.createDataFrame(data, ["user_id", "date", "amount"])
    
    # Define window spec
    window_by_user = Window.partitionBy("user_id").orderBy("date")
    
    # Running total
    df = df.withColumn("running_total", F.sum("amount").over(window_by_user))
    
    # Row number
    df = df.withColumn("row_num", F.row_number().over(window_by_user))
    
    # Rank
    df = df.withColumn("rank", F.rank().over(window_by_user.orderBy(F.desc("amount"))))
    
    # Lag/Lead
    df = df.withColumn("previous_amount", F.lag("amount", 1).over(window_by_user))
    df = df.withColumn("next_amount", F.lead("amount", 1).over(window_by_user))
    
    # Moving average
    window_3_rows = Window.partitionBy("user_id").orderBy("date").rowsBetween(-2, 0)
    df = df.withColumn("moving_avg_3", F.avg("amount").over(window_3_rows))
    
    df.show()
    
    return df

# Joins in Spark
def spark_joins(spark):
    """Join operations in PySpark"""
    
    users = spark.createDataFrame([
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie")
    ], ["user_id", "name"])
    
    transactions = spark.createDataFrame([
        (101, 1, 100),
        (102, 2, 200),
        (103, 1, 150),
        (104, 4, 300)  # user_id 4 doesn't exist
    ], ["txn_id", "user_id", "amount"])
    
    # Inner join
    inner = users.join(transactions, "user_id", "inner")
    inner.show()
    
    # Left join
    left = users.join(transactions, "user_id", "left")
    left.show()
    
    # Right join
    right = users.join(transactions, "user_id", "right")
    right.show()
    
    # Full outer join
    outer = users.join(transactions, "user_id", "outer")
    outer.show()
    
    # Join on different column names
    users2 = users.withColumnRenamed("user_id", "id")
    joined = users2.join(transactions, users2.id == transactions.user_id, "inner")
    joined.show()
    
    return inner

# Writing data in Spark
def spark_write_data(df):
    """Write data to various formats"""
    
    # Parquet (recommended)
    df.write.mode("overwrite").parquet("/output/data.parquet")
    
    # Partitioned parquet
    df.write.mode("overwrite").partitionBy("year", "month").parquet("/output/partitioned/")
    
    # CSV
    df.write.mode("overwrite").option("header", "true").csv("/output/data.csv")
    
    # JSON
    df.write.mode("overwrite").json("/output/data.json")
    
    # SQL database
    # df.write \
    #     .format("jdbc") \
    #     .option("url", "jdbc:postgresql://localhost:5432/db") \
    #     .option("dbtable", "output_table") \
    #     .option("user", "username") \
    #     .option("password", "password") \
    #     .mode("append") \
    #     .save()
    
    return True

# Complete ETL with PySpark
def pyspark_etl(spark, input_path, output_path):
    """
    Production ETL pipeline with PySpark.
    Handles big data efficiently.
    """
    print("Starting PySpark ETL...")
    
    # EXTRACT
    print("Reading data...")
    df = spark.read.parquet(input_path)
    print(f"Records: {df.count()}")
    
    # TRANSFORM
    print("Transforming...")
    
    # 1. Filter out nulls
    df = df.filter(F.col("user_id").isNotNull() & F.col("amount").isNotNull())
    
    # 2. Add derived columns
    df = df.withColumn("year", F.year(F.col("date")))
    df = df.withColumn("month", F.month(F.col("date")))
    df = df.withColumn(
        "amount_category",
        F.when(F.col("amount") < 100, "low")
         .when(F.col("amount") < 500, "medium")
         .otherwise("high")
    )
    
    # 3. Deduplicate
    df = df.dropDuplicates(["user_id", "date"])
    
    # 4. Aggregations
    user_summary = df.groupBy("user_id").agg(
        F.sum("amount").alias("total_amount"),
        F.avg("amount").alias("avg_amount"),
        F.count("*").alias("transaction_count")
    )
    
    # LOAD
    print("Writing data...")
    df.write.mode("overwrite").partitionBy("year", "month").parquet(output_path)
    
    print("ETL complete!")
    
    return df
```

## 9.3 Requests - API Integration

```python
import requests
import json
from typing import Dict, List, Optional
import time

# Basic HTTP requests
def basic_api_calls():
    """Basic API operations"""
    
    base_url = "https://api.example.com"
    
    # GET request
    response = requests.get(f"{base_url}/users")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Retrieved {len(data)} users")
    else:
        print(f"Error: {response.status_code}")
    
    # GET with query parameters
    params = {
        'page': 1,
        'limit': 100,
        'status': 'active'
    }
    response = requests.get(f"{base_url}/users", params=params)
    
    # POST request
    new_user = {
        'name': 'Alice',
        'email': 'alice@example.com'
    }
    response = requests.post(f"{base_url}/users", json=new_user)
    
    # PUT request (update)
    updated_user = {'name': 'Alice Updated'}
    response = requests.put(f"{base_url}/users/123", json=updated_user)
    
    # DELETE request
    response = requests.delete(f"{base_url}/users/123")
    
    return response

# Authentication patterns
def authenticated_requests():
    """Different authentication methods"""
    
    base_url = "https://api.example.com"
    
    # 1. API Key in header
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
    response = requests.get(f"{base_url}/data", headers=headers)
    
    # 2. API Key in query parameter
    params = {'api_key': 'YOUR_API_KEY'}
    response = requests.get(f"{base_url}/data", params=params)
    
    # 3. Basic Authentication
    from requests.auth import HTTPBasicAuth
    response = requests.get(
        f"{base_url}/data",
        auth=HTTPBasicAuth('username', 'password')
    )
    
    # 4. OAuth 2.0 (simplified)
    # First get token
    token_response = requests.post(
        f"{base_url}/oauth/token",
        data={
            'grant_type': 'client_credentials',
            'client_id': 'YOUR_CLIENT_ID',
            'client_secret': 'YOUR_CLIENT_SECRET'
        }
    )
    
    access_token = token_response.json()['access_token']
    
    # Use token
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{base_url}/data", headers=headers)
    
    return response

# Error handling and retries
def robust_api_call(url, max_retries=3, backoff_factor=2):
    """
    Make API call with retries and exponential backoff.
    Production-ready pattern.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            
            # Check for success
            response.raise_for_status()  # Raises HTTPError for bad status codes
            
            return response.json()
            
        except requests.exceptions.Timeout:
            print(f"Timeout on attempt {attempt + 1}")
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff_factor ** attempt)
            
        except requests.exceptions.HTTPError as e:
            status_code = e.response.status_code
            
            # Retry on server errors (5xx)
            if 500 <= status_code < 600:
                print(f"Server error {status_code} on attempt {attempt + 1}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(backoff_factor ** attempt)
            
            # Don't retry on client errors (4xx)
            else:
                print(f"Client error {status_code}: {e}")
                raise
                
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff_factor ** attempt)
    
    raise Exception(f"Failed after {max_retries} attempts")

# Paginated API ingestion
def fetch_all_pages(base_url, endpoint, api_key, page_size=100):
    """
    Fetch all pages from a paginated API.
    Common pattern in data ingestion.
    """
    all_records = []
    page = 1
    
    headers = {'Authorization': f'Bearer {api_key}'}
    
    while True:
        print(f"Fetching page {page}...")
        
        params = {
            'page': page,
            'limit': page_size
        }
        
        try:
            response = requests.get(
                f"{base_url}/{endpoint}",
                headers=headers,
                params=params,
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            # Handle different pagination response formats
            
            # Format 1: Array of records
            if isinstance(data, list):
                records = data
            
            # Format 2: {results: [...], next: url}
            elif 'results' in data:
                records = data['results']
            
            # Format 3: {data: [...], pagination: {...}}
            elif 'data' in data:
                records = data['data']
            
            else:
                records = []
            
            if not records:
                print(f"No more records. Total: {len(all_records)}")
                break
            
            all_records.extend(records)
            print(f"Fetched {len(records)} records. Total: {len(all_records)}")
            
            # Check if there are more pages
            # Different APIs use different indicators
            if isinstance(data, list) and len(data) < page_size:
                break  # Last page
            
            if isinstance(data, dict):
                if not data.get('has_more', True):
                    break
                if not data.get('next'):
                    break
            
            page += 1
            
            # Rate limiting - be nice to the API
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            break
    
    return all_records

# Session for multiple requests
def use_session_for_efficiency():
    """
    Use Session for multiple requests to same host.
    Reuses TCP connection - much faster!
    """
    with requests.Session() as session:
        # Set common headers
        session.headers.update({
            'Authorization': 'Bearer YOUR_API_KEY',
            'Content-Type': 'application/json'
        })
        
        # All requests use same session
        users = session.get('https://api.example.com/users').json()
        products = session.get('https://api.example.com/products').json()
        orders = session.get('https://api.example.com/orders').json()
    
    return users, products, orders

# Complete API ingestion pipeline
class APIIngestionPipeline:
    """
    Production-ready API ingestion pipeline.
    """
    
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def fetch_endpoint(self, endpoint, params=None, max_retries=3):
        """Fetch single endpoint with retry logic"""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(max_retries):
            try:
                response = self.session.get(url, params=params, timeout=30)
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.RequestException as e:
                if attempt == max_retries - 1:
                    raise
                print(f"Retry {attempt + 1}/{max_retries} for {endpoint}")
                time.sleep(2 ** attempt)
    
    def fetch_paginated(self, endpoint, page_size=100):
        """Fetch all pages from endpoint"""
        all_data = []
        page = 1
        
        while True:
            params = {'page': page, 'limit': page_size}
            data = self.fetch_endpoint(endpoint, params)
            
            if not data:
                break
            
            all_data.extend(data)
            
            if len(data) < page_size:
                break
            
            page += 1
            time.sleep(0.5)  # Rate limiting
        
        return all_data
    
    def ingest_all(self, endpoints):
        """Ingest from multiple endpoints"""
        results = {}
        
        for endpoint in endpoints:
            print(f"Ingesting {endpoint}...")
            try:
                data = self.fetch_paginated(endpoint)
                results[endpoint] = {
                    'status': 'success',
                    'record_count': len(data),
                    'data': data
                }
                print(f"✓ {endpoint}: {len(data)} records")
                
            except Exception as e:
                results[endpoint] = {
                    'status': 'failed',
                    'error': str(e)
                }
                print(f"✗ {endpoint}: {e}")
        
        return results
    
    def close(self):
        """Close session"""
        self.session.close()

# Usage
pipeline = APIIngestionPipeline(
    base_url='https://api.example.com',
    api_key='YOUR_API_KEY'
)

results = pipeline.ingest_all(['users', 'products', 'orders'])
pipeline.close()
```
