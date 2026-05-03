# Python for Data Engineers - Part 1: Fundamentals to Functions

## Table of Contents
1. [Python Fundamentals](#1-python-fundamentals-de-focus)
2. [Control Flow & Logic](#2-control-flow--logic)
3. [Core Data Structures](#3-core-data-structures)
4. [Functions & Functional Patterns](#4-functions--functional-patterns)

---

# 1. Python Fundamentals (DE Focus)

## 1.1 Variables and Data Types

In data engineering, understanding how Python manages memory is critical for building efficient pipelines.

```python
# Variables in Python are references to objects
source_table = "users"  # String object
batch_size = 1000       # Integer object
is_incremental = True   # Boolean object
processing_date = None  # NoneType

# Type checking - important for data validation
def validate_config(config):
    """Validate pipeline configuration"""
    if not isinstance(config.get('batch_size'), int):
        raise TypeError(f"batch_size must be int, got {type(config.get('batch_size'))}")
    if not isinstance(config.get('table_name'), str):
        raise TypeError(f"table_name must be str")
    return True

# Example usage in ETL
config = {
    'table_name': 'transactions',
    'batch_size': 5000,
    'partition_column': 'created_date'
}
validate_config(config)
```

## 1.2 Mutable vs Immutable (Critical for Data Engineering)

Understanding mutability prevents bugs in data pipelines where shared state can cause race conditions.

```python
# IMMUTABLE types: int, float, str, tuple, frozenset
# Changes create NEW objects

partition_key = "2024-01-01"  # String is immutable
new_partition = partition_key.replace("2024", "2025")
print(partition_key)  # Still "2024-01-01"
print(new_partition)  # "2025-01-01"

# MUTABLE types: list, dict, set
# Changes modify the SAME object

# DANGEROUS in data pipelines!
def process_records(records, failed_records=[]):  # BUG: mutable default argument
    """DON'T DO THIS - default argument is shared across calls!"""
    for record in records:
        if not record.get('id'):
            failed_records.append(record)
    return failed_records

# First call
result1 = process_records([{'name': 'Alice'}])
print(result1)  # [{'name': 'Alice'}]

# Second call - BUG! Shares same list
result2 = process_records([{'name': 'Bob'}])
print(result2)  # [{'name': 'Alice'}, {'name': 'Bob'}] - UNEXPECTED!

# CORRECT approach
def process_records_correct(records, failed_records=None):
    """Use None as default, create new list inside function"""
    if failed_records is None:
        failed_records = []
    
    for record in records:
        if not record.get('id'):
            failed_records.append(record)
    return failed_records

# Now each call gets its own list
result1 = process_records_correct([{'name': 'Alice'}])
result2 = process_records_correct([{'name': 'Bob'}])
print(result1)  # [{'name': 'Alice'}]
print(result2)  # [{'name': 'Bob'}] - CORRECT!
```

## 1.3 Memory References and Deep Copy

Critical when transforming data to avoid mutating source data.

```python
import copy

# Shallow copy - nested objects are still shared
original_config = {
    'pipeline': 'user_etl',
    'sources': ['db1', 'db2'],
    'settings': {'retry': 3}
}

shallow = original_config.copy()
shallow['sources'].append('db3')  # Modifies original too!
print(original_config['sources'])  # ['db1', 'db2', 'db3'] - UNEXPECTED!

# Deep copy - complete independence
deep = copy.deepcopy(original_config)
deep['sources'].append('db4')
print(original_config['sources'])  # ['db1', 'db2', 'db3'] - Not affected
print(deep['sources'])  # ['db1', 'db2', 'db3', 'db4']

# Production example: Creating environment-specific configs
def create_env_config(base_config, env):
    """Create environment-specific config without mutating base"""
    env_config = copy.deepcopy(base_config)
    env_config['environment'] = env
    env_config['settings']['parallel_jobs'] = 10 if env == 'prod' else 2
    return env_config

base = {'pipeline': 'etl', 'settings': {'retry': 3}}
prod_config = create_env_config(base, 'prod')
dev_config = create_env_config(base, 'dev')
```

## 1.4 Type Hints (Modern Python for Production)

Type hints improve code readability and catch bugs early with tools like `mypy`.

```python
from typing import List, Dict, Optional, Tuple, Union
from datetime import datetime

def extract_records(
    table_name: str,
    start_date: datetime,
    end_date: datetime,
    batch_size: int = 1000
) -> List[Dict[str, Union[str, int, float]]]:
    """
    Extract records from table within date range.
    
    Args:
        table_name: Source table name
        start_date: Start of extraction window
        end_date: End of extraction window
        batch_size: Number of records per batch
        
    Returns:
        List of record dictionaries
    """
    # Implementation
    return []

def get_latest_partition(table: str) -> Optional[str]:
    """
    Get latest partition for table.
    
    Returns:
        Partition string or None if table is empty
    """
    # Implementation
    return "2024-01-01"

# Type hints for complex ETL structures
RecordBatch = List[Dict[str, any]]
PipelineConfig = Dict[str, Union[str, int, bool, List[str]]]

def transform_batch(batch: RecordBatch, config: PipelineConfig) -> RecordBatch:
    """Transform a batch of records"""
    transformed = []
    for record in batch:
        # transformation logic
        transformed.append(record)
    return transformed
```

---

# 2. Control Flow & Logic

## 2.1 Conditional Logic for Data Validation

```python
def validate_record(record: Dict) -> Tuple[bool, str]:
    """
    Validate a single record against business rules.
    Returns (is_valid, error_message)
    """
    # Required fields check
    required_fields = ['user_id', 'transaction_amount', 'timestamp']
    
    for field in required_fields:
        if field not in record:
            return False, f"Missing required field: {field}"
    
    # Data type validation
    if not isinstance(record['user_id'], (int, str)):
        return False, f"Invalid user_id type: {type(record['user_id'])}"
    
    # Business logic validation
    amount = record['transaction_amount']
    if not isinstance(amount, (int, float)):
        return False, f"Invalid amount type: {type(amount)}"
    
    if amount < 0:
        return False, "Amount cannot be negative"
    
    if amount > 1000000:
        return False, "Amount exceeds maximum limit"
    
    # Date validation
    timestamp = record.get('timestamp')
    if timestamp:
        try:
            from datetime import datetime
            if isinstance(timestamp, str):
                datetime.fromisoformat(timestamp)
        except ValueError:
            return False, f"Invalid timestamp format: {timestamp}"
    
    return True, ""

# Usage in ETL pipeline
records = [
    {'user_id': 123, 'transaction_amount': 50.0, 'timestamp': '2024-01-01T10:00:00'},
    {'user_id': 456, 'transaction_amount': -10.0, 'timestamp': '2024-01-01T11:00:00'},
    {'transaction_amount': 100.0, 'timestamp': '2024-01-01T12:00:00'}  # Missing user_id
]

valid_records = []
invalid_records = []

for record in records:
    is_valid, error = validate_record(record)
    if is_valid:
        valid_records.append(record)
    else:
        invalid_records.append({'record': record, 'error': error})

print(f"Valid: {len(valid_records)}, Invalid: {len(invalid_records)}")
```

## 2.2 Loops and Iteration Patterns

```python
# Pattern 1: Processing batches of data
def process_in_batches(records, batch_size=1000):
    """Process records in batches to manage memory"""
    for i in range(0, len(records), batch_size):
        batch = records[i:i + batch_size]
        yield batch  # Generator pattern - memory efficient

# Pattern 2: Enumerate for tracking progress
def transform_with_tracking(records):
    """Transform records with progress tracking"""
    total = len(records)
    transformed = []
    
    for idx, record in enumerate(records, start=1):
        # Transform logic
        transformed_record = {**record, 'processed': True}
        transformed.append(transformed_record)
        
        # Progress logging
        if idx % 1000 == 0:
            print(f"Processed {idx}/{total} records ({idx/total*100:.1f}%)")
    
    return transformed

# Pattern 3: Dictionary iteration for config
def apply_transformations(record, transformations):
    """
    Apply multiple transformations to a record.
    transformations = {'field_name': transformation_function}
    """
    result = record.copy()
    
    for field, transform_func in transformations.items():
        if field in result:
            result[field] = transform_func(result[field])
    
    return result

# Usage
transformations = {
    'email': str.lower,
    'amount': lambda x: round(x, 2),
    'name': str.strip
}

record = {'email': 'USER@EXAMPLE.COM', 'amount': 10.567, 'name': '  John  '}
cleaned = apply_transformations(record, transformations)
print(cleaned)  # {'email': 'user@example.com', 'amount': 10.57, 'name': 'John'}

# Pattern 4: While loops for polling/retries
import time

def wait_for_file(filepath, max_wait_seconds=300, check_interval=5):
    """Wait for a file to appear (common in batch ETL)"""
    import os
    elapsed = 0
    
    while elapsed < max_wait_seconds:
        if os.path.exists(filepath):
            print(f"File found: {filepath}")
            return True
        
        print(f"Waiting for {filepath}... ({elapsed}s elapsed)")
        time.sleep(check_interval)
        elapsed += check_interval
    
    raise TimeoutError(f"File {filepath} not found after {max_wait_seconds}s")
```

## 2.3 Break and Continue

```python
def find_first_error(records):
    """Find first record with error and stop processing"""
    for idx, record in enumerate(records):
        if not record.get('user_id'):
            print(f"Found error at index {idx}")
            return record  # Implicit break
        
        # Validate other fields
        if record.get('amount', 0) < 0:
            print(f"Negative amount at index {idx}")
            break  # Explicit break
    
    return None

def process_valid_only(records):
    """Skip invalid records, continue with valid ones"""
    processed_count = 0
    
    for record in records:
        # Skip records without required fields
        if not record.get('user_id') or not record.get('amount'):
            print(f"Skipping invalid record: {record}")
            continue  # Skip to next iteration
        
        # Skip negative amounts
        if record['amount'] < 0:
            continue
        
        # Process valid record
        print(f"Processing: {record}")
        processed_count += 1
    
    return processed_count

# Real example: File processing with error handling
def process_data_files(file_list, max_errors=5):
    """
    Process multiple files, stop if too many errors.
    Skip individual bad files but continue processing.
    """
    error_count = 0
    processed_files = []
    
    for filepath in file_list:
        try:
            # Simulate file processing
            if 'corrupted' in filepath:
                raise ValueError(f"Corrupted file: {filepath}")
            
            # Process file
            print(f"Processing: {filepath}")
            processed_files.append(filepath)
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            error_count += 1
            
            # Stop if too many errors
            if error_count >= max_errors:
                print(f"Stopping: {error_count} errors encountered")
                break
            
            # Continue with next file
            continue
    
    return processed_files

files = ['data1.csv', 'data2.csv', 'corrupted_data.csv', 'data3.csv']
processed = process_data_files(files, max_errors=2)
```

---

# 3. Core Data Structures

## 3.1 Lists - Dynamic Arrays

**Time Complexity:**
- Access by index: O(1)
- Append: O(1) amortized
- Insert at beginning: O(n)
- Search: O(n)
- Delete: O(n)

**Space Complexity:** O(n)

```python
# Lists for ETL - storing records
records = [
    {'id': 1, 'name': 'Alice', 'amount': 100},
    {'id': 2, 'name': 'Bob', 'amount': 200}
]

# Append - O(1) - most common in streaming data
new_record = {'id': 3, 'name': 'Charlie', 'amount': 150}
records.append(new_record)

# Extend - O(k) where k is length of added list
batch = [
    {'id': 4, 'name': 'David', 'amount': 300},
    {'id': 5, 'name': 'Eve', 'amount': 250}
]
records.extend(batch)  # Better than multiple appends

# List comprehension - Pythonic and fast
# Filter records with amount > 150
high_value_records = [r for r in records if r['amount'] > 150]

# Transform - extract specific fields
user_ids = [r['id'] for r in records]
names = [r['name'] for r in records]

# List comprehension with condition and transformation
# Get uppercase names for amounts > 150
high_value_names = [r['name'].upper() for r in records if r['amount'] > 150]

# Slicing - O(k) where k is slice size
first_two = records[:2]
last_two = records[-2:]
every_other = records[::2]

# Sorting - O(n log n)
# Sort by amount
sorted_records = sorted(records, key=lambda x: x['amount'])
# Sort descending
sorted_desc = sorted(records, key=lambda x: x['amount'], reverse=True)

# In-place sort
records.sort(key=lambda x: x['id'])

# Production example: Deduplication
def deduplicate_records(records, key='id'):
    """
    Remove duplicates based on key, keeping first occurrence.
    Time: O(n), Space: O(n)
    """
    seen = set()
    unique_records = []
    
    for record in records:
        record_key = record.get(key)
        if record_key not in seen:
            seen.add(record_key)
            unique_records.append(record)
    
    return unique_records

# Usage
duplicate_data = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 1, 'name': 'Alice Duplicate'},  # Duplicate
    {'id': 3, 'name': 'Charlie'}
]
unique = deduplicate_records(duplicate_data)
print(f"Original: {len(duplicate_data)}, Unique: {len(unique)}")
```

## 3.2 Tuples - Immutable Sequences

**When to use:**
- Fixed data that shouldn't change (e.g., database row)
- Dictionary keys (must be immutable)
- Function return values
- Slightly faster than lists

```python
# Tuple for database row representation
db_row = (1, 'Alice', 'alice@example.com', '2024-01-01')

# Unpacking - very useful in ETL
user_id, name, email, created_date = db_row

# Named tuples - better than regular tuples for readability
from collections import namedtuple

# Define schema
UserRecord = namedtuple('UserRecord', ['id', 'name', 'email', 'created_date'])

# Create instance
user = UserRecord(1, 'Alice', 'alice@example.com', '2024-01-01')

# Access by name (readable) or index
print(user.name)  # 'Alice'
print(user[1])    # 'Alice'

# Named tuples as lightweight data classes
TransactionRecord = namedtuple('TransactionRecord', [
    'transaction_id',
    'user_id',
    'amount',
    'timestamp',
    'status'
])

# Create from database query result
def parse_db_row(row):
    """Convert database row to named tuple"""
    return TransactionRecord(*row)

# Production example: Return multiple values
def get_data_quality_metrics(records):
    """
    Analyze data quality and return metrics as tuple.
    Tuple ensures return values can't be accidentally modified.
    """
    total = len(records)
    null_count = sum(1 for r in records if r.get('value') is None)
    negative_count = sum(1 for r in records if r.get('value', 0) < 0)
    avg_value = sum(r.get('value', 0) for r in records) / total if total > 0 else 0
    
    return (total, null_count, negative_count, round(avg_value, 2))

# Usage with unpacking
total, nulls, negatives, average = get_data_quality_metrics(records)
print(f"Total: {total}, Nulls: {nulls}, Negatives: {negatives}, Avg: {average}")

# Tuples as dictionary keys (common in caching)
partition_cache = {}

# Cache key: (table_name, partition_date)
cache_key = ('users', '2024-01-01')
partition_cache[cache_key] = {'row_count': 1000, 'file_path': '/data/users/2024-01-01'}

# Lookup
cached_data = partition_cache.get(('users', '2024-01-01'))
```

## 3.3 Sets - Unique Collections

**Time Complexity:**
- Add: O(1)
- Remove: O(1)
- Membership test: O(1)
- Union/Intersection: O(min(len(s), len(t)))

**When to use:**
- Removing duplicates
- Membership testing
- Set operations (union, intersection, difference)

```python
# Deduplication - most common use case
user_ids = [1, 2, 3, 2, 1, 4, 5, 3]
unique_ids = set(user_ids)  # {1, 2, 3, 4, 5}
unique_list = list(unique_ids)  # Convert back to list if needed

# Fast membership testing - O(1) vs O(n) for list
valid_user_ids = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Set

# O(1) lookup
if user_id in valid_user_ids:  # Fast!
    print("Valid user")

# VS list lookup - O(n)
valid_ids_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List
if user_id in valid_ids_list:  # Slow for large lists!
    print("Valid user")

# Set operations - powerful for data engineering
# Example: Compare two data sources

source_a_ids = {1, 2, 3, 4, 5}
source_b_ids = {4, 5, 6, 7, 8}

# Union - IDs in either source
all_ids = source_a_ids | source_b_ids  # {1, 2, 3, 4, 5, 6, 7, 8}
# OR: source_a_ids.union(source_b_ids)

# Intersection - IDs in both sources
common_ids = source_a_ids & source_b_ids  # {4, 5}
# OR: source_a_ids.intersection(source_b_ids)

# Difference - IDs in A but not in B
only_in_a = source_a_ids - source_b_ids  # {1, 2, 3}
# OR: source_a_ids.difference(source_b_ids)

# Symmetric difference - IDs in either A or B but not both
unique_to_each = source_a_ids ^ source_b_ids  # {1, 2, 3, 6, 7, 8}

# Production example: Data reconciliation
def reconcile_data_sources(source_a_records, source_b_records, key='id'):
    """
    Compare two data sources and identify differences.
    Returns: (only_in_a, only_in_b, in_both)
    """
    ids_a = {record[key] for record in source_a_records}
    ids_b = {record[key] for record in source_b_records}
    
    only_in_a = ids_a - ids_b
    only_in_b = ids_b - ids_a
    in_both = ids_a & ids_b
    
    return (only_in_a, only_in_b, in_both)

# Usage
db_records = [{'id': 1}, {'id': 2}, {'id': 3}]
api_records = [{'id': 2}, {'id': 3}, {'id': 4}]

only_db, only_api, both = reconcile_data_sources(db_records, api_records)
print(f"Only in DB: {only_db}")      # {1}
print(f"Only in API: {only_api}")    # {4}
print(f"In both: {both}")            # {2, 3}

# Set comprehension
emails = [
    'user1@example.com',
    'user2@example.com',
    'user1@example.com',  # Duplicate
    'user3@EXAMPLE.COM'   # Case variation
]

# Get unique domains
unique_domains = {email.split('@')[1].lower() for email in emails}
print(unique_domains)  # {'example.com'}

# Filter duplicates while preserving order (advanced pattern)
def unique_preserve_order(items):
    """Remove duplicates while preserving original order"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

ordered_unique = unique_preserve_order([1, 2, 3, 2, 1, 4, 5, 3])
print(ordered_unique)  # [1, 2, 3, 4, 5]
```

## 3.4 Dictionaries - Hash Maps

**Time Complexity:**
- Access: O(1) average
- Insert: O(1) average
- Delete: O(1) average
- Iteration: O(n)

**Space Complexity:** O(n)

**Most important data structure in Python data engineering!**

```python
# Basic dictionary - JSON-like structure
user = {
    'id': 123,
    'name': 'Alice',
    'email': 'alice@example.com',
    'metadata': {
        'created_at': '2024-01-01',
        'source': 'api'
    }
}

# Safe access with get() - prevents KeyError
email = user.get('email')  # Returns value or None
phone = user.get('phone', 'N/A')  # Returns 'N/A' if key doesn't exist

# Dictionary methods
keys = user.keys()      # dict_keys(['id', 'name', 'email', 'metadata'])
values = user.values()  # dict_values([123, 'Alice', ...])
items = user.items()    # dict_items([('id', 123), ...])

# Iteration patterns
for key in user:
    print(f"{key}: {user[key]}")

for key, value in user.items():
    print(f"{key}: {value}")

# Dictionary comprehension
# Transform values
amounts = {'jan': 100, 'feb': 200, 'mar': 300}
doubled = {month: amount * 2 for month, amount in amounts.items()}

# Filter dictionary
high_amounts = {month: amount for month, amount in amounts.items() if amount > 150}

# Merging dictionaries (Python 3.9+)
default_config = {'retry': 3, 'timeout': 30}
user_config = {'timeout': 60, 'batch_size': 1000}

# Merge - user_config overrides default_config
merged = default_config | user_config
# Result: {'retry': 3, 'timeout': 60, 'batch_size': 1000}

# Update in place
default_config.update(user_config)

# Production pattern: Grouping records
def group_by_key(records, key):
    """
    Group records by a specific key.
    Time: O(n), Space: O(n)
    """
    grouped = {}
    for record in records:
        key_value = record.get(key)
        if key_value not in grouped:
            grouped[key_value] = []
        grouped[key_value].append(record)
    return grouped

transactions = [
    {'user_id': 1, 'amount': 100},
    {'user_id': 2, 'amount': 200},
    {'user_id': 1, 'amount': 150},
    {'user_id': 3, 'amount': 300},
]

by_user = group_by_key(transactions, 'user_id')
# {
#   1: [{'user_id': 1, 'amount': 100}, {'user_id': 1, 'amount': 150}],
#   2: [{'user_id': 2, 'amount': 200}],
#   3: [{'user_id': 3, 'amount': 300}]
# }

# Better approach using defaultdict
from collections import defaultdict

def group_by_key_v2(records, key):
    """Group records using defaultdict"""
    grouped = defaultdict(list)
    for record in records:
        grouped[record.get(key)].append(record)
    return dict(grouped)

# Counter - frequency counting (very useful!)
from collections import Counter

# Count occurrences
statuses = ['success', 'failed', 'success', 'success', 'failed', 'pending']
status_counts = Counter(statuses)
print(status_counts)  # Counter({'success': 3, 'failed': 2, 'pending': 1})

# Most common
print(status_counts.most_common(2))  # [('success', 3), ('failed', 2)]

# Production example: Aggregations
def aggregate_transactions(transactions):
    """
    Aggregate transaction metrics by user.
    Returns dict with user_id -> metrics
    """
    user_metrics = defaultdict(lambda: {
        'total_amount': 0,
        'transaction_count': 0,
        'transactions': []
    })
    
    for txn in transactions:
        user_id = txn['user_id']
        user_metrics[user_id]['total_amount'] += txn['amount']
        user_metrics[user_id]['transaction_count'] += 1
        user_metrics[user_id]['transactions'].append(txn)
    
    return dict(user_metrics)

metrics = aggregate_transactions(transactions)
print(metrics[1])  # {'total_amount': 250, 'transaction_count': 2, 'transactions': [...]}

# Nested dictionary access - safe pattern
def safe_get_nested(data, keys, default=None):
    """
    Safely access nested dictionary.
    safe_get_nested(data, ['user', 'address', 'city'], 'Unknown')
    """
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
    return data if data is not None else default

nested_data = {
    'user': {
        'profile': {
            'address': {
                'city': 'New York'
            }
        }
    }
}

city = safe_get_nested(nested_data, ['user', 'profile', 'address', 'city'])
print(city)  # 'New York'

missing = safe_get_nested(nested_data, ['user', 'profile', 'phone'], 'N/A')
print(missing)  # 'N/A'
```

## 3.5 When to Use Which Data Structure

| Use Case | Data Structure | Reason |
|----------|---------------|--------|
| Store ordered records | `list` | Maintain insertion order, indexed access |
| Remove duplicates | `set` | O(1) membership testing |
| Fast lookup by key | `dict` | O(1) key-value access |
| Immutable record | `tuple` or `namedtuple` | Hashable, can be dict key |
| Count frequencies | `Counter` (dict) | Built-in counting functionality |
| Group by key | `defaultdict` | Avoid key existence checks |
| Priority processing | `heapq` or `queue.PriorityQueue` | Efficient min/max retrieval |
| FIFO processing | `collections.deque` | O(1) append/pop from both ends |
| Lookup table | `dict` | Fast constant-time lookup |

---

# 4. Functions & Functional Patterns

## 4.1 Function Design for ETL

```python
def extract_data(
    source: str,
    start_date: str,
    end_date: str,
    batch_size: int = 1000,
    retry_count: int = 3
) -> list:
    """
    Extract data from source within date range.
    
    Design principles:
    1. Single Responsibility: Only extraction logic
    2. Type hints: Clear input/output types
    3. Docstring: What it does, args, returns
    4. Default arguments: Sensible defaults
    5. Return value: Consistent type
    
    Args:
        source: Data source identifier
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        batch_size: Records per batch (default: 1000)
        retry_count: Number of retries on failure (default: 3)
        
    Returns:
        List of extracted records
        
    Raises:
        ValueError: If date format is invalid
        ConnectionError: If source is unreachable
    """
    # Validation
    if not source:
        raise ValueError("Source cannot be empty")
    
    # Implementation
    records = []
    # ... extraction logic ...
    return records

# Good function: Single purpose, clear name
def validate_email(email: str) -> bool:
    """Check if email format is valid"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def transform_record(record: dict) -> dict:
    """Apply transformations to a single record"""
    return {
        'user_id': record['id'],
        'email': record['email'].lower(),
        'signup_date': record['created_at'][:10],  # Extract date part
        'is_active': record.get('status') == 'active'
    }

def load_to_database(records: list, table_name: str) -> int:
    """Load records to database table"""
    # ... loading logic ...
    return len(records)
```

## 4.2 Default Arguments and Edge Cases

```python
# WRONG: Mutable default argument
def process_batch(records, failed=[], config={}):  # BUG!
    """Don't do this - defaults are shared across calls!"""
    pass

# CORRECT: Use None as default
def process_batch(records, failed=None, config=None):
    """Correct approach with immutable defaults"""
    if failed is None:
        failed = []
    if config is None:
        config = {}
    
    # Now safe to use
    for record in records:
        try:
            # process record
            pass
        except Exception as e:
            failed.append({'record': record, 'error': str(e)})
    
    return failed

# Default arguments evaluation time
def get_timestamp(ts=None):
    """Get timestamp, use current time if not provided"""
    from datetime import datetime
    if ts is None:
        ts = datetime.now()  # Evaluated at call time
    return ts

# WRONG: Default argument evaluated at definition time
from datetime import datetime
def broken_timestamp(ts=datetime.now()):  # BUG!
    """Don't do this - ts is evaluated once when function is defined!"""
    return ts

# Keyword-only arguments (Python 3+)
def create_pipeline(
    name: str,
    source: str,
    *,  # Everything after * is keyword-only
    batch_size: int = 1000,
    parallel: bool = False,
    retry_count: int = 3
):
    """
    Create ETL pipeline.
    Forces clarity for optional parameters.
    """
    config = {
        'name': name,
        'source': source,
        'batch_size': batch_size,
        'parallel': parallel,
        'retry_count': retry_count
    }
    return config

# Must use keyword arguments
pipeline = create_pipeline(
    'user_etl',
    'postgres',
    batch_size=5000,
    parallel=True
)
```

## 4.3 *args and **kwargs

```python
def extract_from_multiple_sources(*sources, batch_size=1000, **options):
    """
    Extract from multiple sources.
    
    *sources: Variable number of source names
    **options: Arbitrary keyword arguments for source-specific options
    """
    all_records = []
    
    for source in sources:
        print(f"Extracting from {source}")
        # Use options if provided
        source_config = options.get(f"{source}_config", {})
        # ... extraction logic ...
    
    return all_records

# Usage
records = extract_from_multiple_sources(
    'postgres',
    'mongodb',
    'api',
    batch_size=5000,
    postgres_config={'host': 'localhost', 'port': 5432},
    mongodb_config={'host': 'localhost', 'port': 27017}
)
```

## 4.4 Lambda Functions

```python
# Lambda: Anonymous functions for simple operations

# Sort records by multiple fields
records = [
    {'name': 'Alice', 'age': 30, 'salary': 50000},
    {'name': 'Bob', 'age': 25, 'salary': 60000},
    {'name': 'Charlie', 'age': 30, 'salary': 55000}
]

# Sort by age, then by salary
sorted_records = sorted(records, key=lambda x: (x['age'], x['salary']))

# Filter with lambda
high_earners = list(filter(lambda x: x['salary'] > 55000, records))

# Map with lambda - transform each element
salaries = list(map(lambda x: x['salary'], records))

# But list comprehension is more Pythonic:
salaries = [r['salary'] for r in records]  # Preferred!

# Practical use: Dynamic field transformations
field_transforms = {
    'email': lambda x: x.lower().strip(),
    'phone': lambda x: ''.join(filter(str.isdigit, x)),
    'amount': lambda x: round(float(x), 2)
}

def apply_transforms(record, transforms):
    """Apply lambda transformations to record fields"""
    result = record.copy()
    for field, transform in transforms.items():
        if field in result:
            result[field] = transform(result[field])
    return result

raw_record = {
    'email': '  USER@EXAMPLE.COM  ',
    'phone': '+1 (555) 123-4567',
    'amount': '123.456'
}

cleaned = apply_transforms(raw_record, field_transforms)
print(cleaned)
# {'email': 'user@example.com', 'phone': '15551234567', 'amount': 123.46}
```

## 4.5 Pure vs Impure Functions

```python
# PURE FUNCTION:
# - Same input always produces same output
# - No side effects (doesn't modify external state)
# - Doesn't depend on external state
# - Easy to test, reason about, parallelize

def calculate_total(amounts):
    """Pure function - same input, same output"""
    return sum(amounts)

def transform_record_pure(record):
    """Pure function - returns new dict, doesn't modify input"""
    return {
        'user_id': record['id'],
        'email': record['email'].lower(),
        'processed': True
    }

# IMPURE FUNCTION:
# - Reads/writes files
# - Makes network calls
# - Uses random numbers or current time
# - Modifies input arguments
# - Depends on global state

processed_count = 0  # Global state

def transform_record_impure(record):
    """Impure - modifies global state"""
    global processed_count
    processed_count += 1  # Side effect!
    
    record['processed'] = True  # Modifies input! Side effect!
    record['timestamp'] = datetime.now()  # Non-deterministic!
    
    return record

# Best practice: Separate pure and impure functions

# Pure: Business logic
def calculate_user_metrics(transactions):
    """Pure function - calculation only"""
    total = sum(t['amount'] for t in transactions)
    count = len(transactions)
    average = total / count if count > 0 else 0
    
    return {
        'total': total,
        'count': count,
        'average': round(average, 2)
    }

# Impure: I/O operations
def save_metrics_to_db(metrics, table_name):
    """Impure function - database I/O"""
    # Database write
    return db.write(table_name, metrics)

# Compose: Pure logic + Impure I/O
def process_user_transactions(user_id):
    """Main function - orchestrates pure and impure"""
    # Impure: Read from database
    transactions = db.query(f"SELECT * FROM transactions WHERE user_id = {user_id}")
    
    # Pure: Calculate metrics
    metrics = calculate_user_metrics(transactions)
    
    # Impure: Write to database
    save_metrics_to_db(metrics, 'user_metrics')
    
    return metrics
```
