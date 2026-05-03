# Python Data Engineering - Quick Reference Cheat Sheet

## 🎯 Data Structures - Time Complexity

| Operation | List | Set | Dict | Tuple |
|-----------|------|-----|------|-------|
| Access by index | O(1) | N/A | N/A | O(1) |
| Search | O(n) | O(1) | O(1) | O(n) |
| Insert | O(1)* | O(1) | O(1) | N/A |
| Delete | O(n) | O(1) | O(1) | N/A |
| Iteration | O(n) | O(n) | O(n) | O(n) |

*Append is O(1), insert at position is O(n)

## 🔧 Common Operations

### Dictionary
```python
# Create
d = {'key': 'value'}
d = dict(key='value')

# Access
d['key']           # Raises KeyError if missing
d.get('key', default)  # Returns default if missing

# Iterate
for key in d:              # Keys
for value in d.values():   # Values
for k, v in d.items():     # Key-value pairs

# Update
d.update({'new': 'value'})
d['key'] = 'new_value'
```

### List
```python
# Create
lst = [1, 2, 3]
lst = list(range(10))

# Operations
lst.append(4)          # Add to end - O(1)
lst.extend([5, 6])     # Add multiple - O(k)
lst.insert(0, 0)       # Insert at position - O(n)
lst.pop()              # Remove last - O(1)
lst.remove(2)          # Remove by value - O(n)

# Comprehension
[x**2 for x in range(10) if x % 2 == 0]
```

### Set
```python
# Create
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}

# Operations
s.add(4)               # O(1)
s.remove(2)            # O(1), raises KeyError
s.discard(2)           # O(1), no error

# Set operations
a | b    # Union
a & b    # Intersection
a - b    # Difference
a ^ b    # Symmetric difference
```

## 📊 Pandas Quick Reference

### Reading/Writing
```python
# Read
df = pd.read_csv('file.csv')
df = pd.read_parquet('file.parquet')
df = pd.read_json('file.json', lines=True)

# Write
df.to_csv('out.csv', index=False)
df.to_parquet('out.parquet', compression='snappy')
```

### Selection
```python
df['col']              # Single column (Series)
df[['col1', 'col2']]   # Multiple columns (DataFrame)
df[df['col'] > 5]      # Filter rows
df.loc[0]              # Row by label
df.iloc[0]             # Row by position
```

### Aggregation
```python
# Single aggregation
df['col'].sum()
df['col'].mean()
df['col'].max()

# GroupBy
df.groupby('category')['amount'].sum()
df.groupby('category').agg({
    'amount': ['sum', 'mean', 'count']
})
```

### Transformation
```python
# Add column
df['new_col'] = df['col'] * 2

# Apply function
df['col'].apply(lambda x: x * 2)  # Slow
df['col'] * 2                      # Fast (vectorized)

# String operations
df['email'].str.lower()
df['email'].str.strip()
```

## ⚡ PySpark Quick Reference

### Reading/Writing
```python
from pyspark.sql import functions as F

# Read
df = spark.read.csv('file.csv', header=True, inferSchema=True)
df = spark.read.parquet('file.parquet')

# Write
df.write.mode('overwrite').parquet('output/')
df.write.partitionBy('year', 'month').parquet('output/')
```

### Transformation
```python
# Select
df.select('col1', 'col2')
df.select(F.col('col1'), F.col('col2'))

# Filter
df.filter(F.col('amount') > 100)
df.filter("amount > 100")

# Add column
df.withColumn('new_col', F.col('col') * 2)

# Aggregation
df.groupBy('category').agg(
    F.sum('amount').alias('total'),
    F.avg('amount').alias('average')
)
```

## 🔄 Concurrency Decision Tree

```
Is the task CPU-bound or I/O-bound?
│
├─ I/O-bound (network, files, database)
│  └─ Use Threading (ThreadPoolExecutor)
│
└─ CPU-bound (calculations, transformations)
   └─ Use Multiprocessing (ProcessPoolExecutor)
```

### Threading Example
```python
from concurrent.futures import ThreadPoolExecutor

def fetch_data(url):
    # I/O operation
    return requests.get(url).json()

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_data, urls))
```

### Multiprocessing Example
```python
from multiprocessing import Pool

def process_chunk(chunk):
    # CPU-intensive operation
    return [transform(item) for item in chunk]

with Pool(processes=4) as pool:
    results = pool.map(process_chunk, chunks)
```

## 🎭 Common Patterns

### Retry Logic
```python
import time

def retry(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay * (2 ** attempt))
        return wrapper
    return decorator

@retry(max_retries=5)
def api_call():
    pass
```

### Context Manager
```python
from contextlib import contextmanager

@contextmanager
def database_connection(conn_str):
    conn = connect(conn_str)
    try:
        yield conn
    finally:
        conn.close()

with database_connection('db://localhost') as conn:
    data = conn.query("SELECT * FROM users")
```

### Generator for Memory Efficiency
```python
def read_large_file(filepath):
    """Process line by line - O(1) memory"""
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

for line in read_large_file('huge.txt'):
    process(line)  # Only one line in memory at a time
```

## 🐛 Error Handling

```python
try:
    # Code that may raise exception
    result = risky_operation()
except ValueError as e:
    # Handle specific exception
    logger.warning(f"Invalid value: {e}")
except (ConnectionError, TimeoutError) as e:
    # Handle multiple exceptions
    logger.error(f"Network error: {e}")
except Exception as e:
    # Catch-all (use sparingly)
    logger.error(f"Unexpected error: {e}")
    raise  # Re-raise if you can't handle
finally:
    # Always executes (cleanup)
    cleanup_resources()
```

## 📝 String Operations

```python
# Formatting
name = "Alice"
f"Hello, {name}"           # f-string (fastest)
"Hello, {}".format(name)   # format()
"Hello, " + name           # concatenation (slow)

# Join
','.join(['a', 'b', 'c'])  # 'a,b,c'

# Split
'a,b,c'.split(',')         # ['a', 'b', 'c']

# Strip
'  hello  '.strip()        # 'hello'
'  hello  '.lstrip()       # 'hello  '
'  hello  '.rstrip()       # '  hello'
```

## 🔍 List Comprehensions

```python
# Basic
[x**2 for x in range(10)]

# With condition
[x for x in range(10) if x % 2 == 0]

# Nested
[x*y for x in range(3) for y in range(3)]

# Dict comprehension
{k: v**2 for k, v in enumerate(range(5))}

# Set comprehension
{x % 3 for x in range(10)}
```

## 🎯 Performance Tips

### DO ✅
```python
# Use sets for membership testing
valid_ids = {1, 2, 3, 4, 5}
if user_id in valid_ids:  # O(1)
    pass

# Vectorized operations in Pandas
df['doubled'] = df['amount'] * 2

# Generator for large data
data = (process(line) for line in file)

# List comprehension
squares = [x**2 for x in range(1000)]
```

### DON'T ❌
```python
# Don't use list for lookups
valid_ids = [1, 2, 3, 4, 5]
if user_id in valid_ids:  # O(n)
    pass

# Don't use apply when vectorized exists
df['doubled'] = df['amount'].apply(lambda x: x * 2)

# Don't load entire file if streaming works
with open('huge.txt') as f:
    data = f.readlines()  # Loads all into memory

# Don't use loop when comprehension works
squares = []
for x in range(1000):
    squares.append(x**2)
```

## 🔧 Debugging Tips

```python
# Print debugging
print(f"Debug: value={value}, type={type(value)}")

# Check type
isinstance(obj, dict)
type(obj) == dict

# Check memory
import sys
sys.getsizeof(obj)

# Profile code
import cProfile
cProfile.run('my_function()')

# Time execution
import time
start = time.time()
# ... code ...
print(f"Took {time.time() - start:.2f}s")
```

## 📦 Import Patterns

```python
# Standard library
import os
import sys
from pathlib import Path
from typing import List, Dict
from datetime import datetime

# Data manipulation
import pandas as pd
import numpy as np

# PySpark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# API calls
import requests

# Concurrency
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
```

## 🎓 Interview Code Templates

### ETL Pipeline
```python
class ETLPipeline:
    def __init__(self, config):
        self.config = config
    
    def extract(self):
        # Read from source
        pass
    
    def transform(self, data):
        # Clean and transform
        pass
    
    def load(self, data):
        # Write to destination
        pass
    
    def run(self):
        data = self.extract()
        transformed = self.transform(data)
        self.load(transformed)
```

### Deduplication
```python
# Keep first occurrence
unique = list(dict.fromkeys(items))

# Using set (loses order)
unique = list(set(items))

# With condition
seen = set()
unique = [x for x in items if not (x in seen or seen.add(x))]
```

### Two Sum Problem
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
```

## 💾 File Format Decision

| Format | Use Case | Pros | Cons |
|--------|----------|------|------|
| CSV | Small data, human-readable | Universal, simple | Slow, large, no types |
| JSON | APIs, config | Human-readable, nested | Slow, verbose |
| Parquet | Big data, analytics | Fast, compressed, typed | Not human-readable |
| Avro | Streaming, Kafka | Schema evolution | Less common |

## 🚀 When to Use What

### Data Processing
- **< 1 GB:** Pandas
- **1-5 GB:** Pandas with chunking
- **> 5 GB:** PySpark

### Data Storage
- **Development:** CSV, JSON
- **Production:** Parquet, Avro

### Concurrency
- **API calls:** Threading
- **File I/O:** Threading
- **Transformations:** Multiprocessing
- **Simple tasks:** Serial

---

**Print this page and keep it handy during interviews!** 📄
