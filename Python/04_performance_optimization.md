# Python for Data Engineers - Part 4: Performance & Optimization

## Table of Contents
10. [Performance & Optimization](#10-performance--optimization)

---

# 10. Performance & Optimization

## 10.1 Time Complexity Analysis

```python
"""
Common Time Complexities (Best to Worst):
O(1)        - Constant time
O(log n)    - Logarithmic time
O(n)        - Linear time
O(n log n)  - Linearithmic time
O(n²)       - Quadratic time
O(2ⁿ)       - Exponential time
"""

# O(1) - Constant time
def get_first_element(arr):
    """Always takes same time regardless of input size"""
    return arr[0] if arr else None

# Dictionary/Set lookup - O(1) average
def check_user_exists(user_id, user_set):
    """O(1) average case"""
    return user_id in user_set

# O(n) - Linear time
def find_max_amount(transactions):
    """Must check every element once"""
    max_amount = float('-inf')
    for txn in transactions:
        if txn['amount'] > max_amount:
            max_amount = txn['amount']
    return max_amount

# O(n²) - Quadratic time (AVOID IN PRODUCTION!)
def find_duplicates_slow(records):
    """Nested loops - O(n²) - BAD for large data!"""
    duplicates = []
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if records[i]['id'] == records[j]['id']:
                duplicates.append(records[i])
    return duplicates

# O(n) - Better approach using set
def find_duplicates_fast(records):
    """Using set - O(n) - MUCH BETTER!"""
    seen = set()
    duplicates = []
    
    for record in records:
        record_id = record['id']
        if record_id in seen:
            duplicates.append(record)
        else:
            seen.add(record_id)
    
    return duplicates

# Sorting - O(n log n)
def sort_records(records):
    """Built-in sort is O(n log n)"""
    return sorted(records, key=lambda x: x['amount'])

# Interview Example: Two Sum Problem
def two_sum_slow(numbers, target):
    """
    O(n²) - Nested loops
    Find two numbers that sum to target.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None

def two_sum_fast(numbers, target):
    """
    O(n) - Using hash map
    Much better for large datasets!
    """
    seen = {}
    
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

# Usage comparison
import time

numbers = list(range(10000))
target = 19997

# Slow version
start = time.time()
result1 = two_sum_slow(numbers, target)
slow_time = time.time() - start

# Fast version
start = time.time()
result2 = two_sum_fast(numbers, target)
fast_time = time.time() - start

print(f"Slow O(n²): {slow_time:.4f}s")
print(f"Fast O(n): {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.0f}x faster")
```

## 10.2 Space Complexity Analysis

```python
"""
Space Complexity - Memory usage patterns
"""

# O(1) - Constant space
def sum_array(arr):
    """Uses same amount of memory regardless of input size"""
    total = 0
    for num in arr:
        total += num
    return total

# O(n) - Linear space
def copy_array(arr):
    """Creates new array of same size as input"""
    return arr.copy()

def filter_records(records, condition):
    """Worst case: returns copy of all records - O(n) space"""
    return [r for r in records if condition(r)]

# Trade-off: Time vs Space
def process_large_file_memory_intensive(filepath):
    """
    Fast but memory intensive - O(n) space
    Loads entire file into memory
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()  # Loads ALL lines into memory
    
    processed = []
    for line in lines:
        processed.append(line.strip().upper())
    
    return processed

def process_large_file_memory_efficient(filepath):
    """
    Slower but memory efficient - O(1) space
    Processes one line at a time
    """
    processed = []
    
    with open(filepath, 'r') as f:
        for line in f:  # Generator - one line at a time
            processed.append(line.strip().upper())
    
    return processed

# In-place modification - O(1) extra space
def deduplicate_in_place(arr):
    """
    Modify original array instead of creating new one.
    O(1) extra space (only uses a set for tracking)
    """
    seen = set()
    write_index = 0
    
    for read_index in range(len(arr)):
        if arr[read_index] not in seen:
            seen.add(arr[read_index])
            arr[write_index] = arr[read_index]
            write_index += 1
    
    # Truncate array
    del arr[write_index:]
    return arr
```

## 10.3 Generators vs Lists

```python
# List - stores all values in memory
def get_numbers_list(n):
    """O(n) space - stores all numbers"""
    return [i for i in range(n)]

# Generator - lazy evaluation, O(1) space
def get_numbers_generator(n):
    """O(1) space - generates one at a time"""
    for i in range(n):
        yield i

# Memory comparison
import sys

n = 1_000_000

# List - large memory footprint
numbers_list = get_numbers_list(n)
print(f"List size: {sys.getsizeof(numbers_list):,} bytes")

# Generator - tiny memory footprint
numbers_gen = get_numbers_generator(n)
print(f"Generator size: {sys.getsizeof(numbers_gen):,} bytes")

# Production example: Process large dataset with generator
def process_large_csv_generator(filepath):
    """
    Memory efficient - processes one record at a time.
    Suitable for files that don't fit in memory.
    """
    import csv
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Transform row
            transformed = {
                'id': int(row['id']),
                'amount': float(row['amount']) * 1.1,
                'processed': True
            }
            
            yield transformed  # Yield instead of append

# Usage - memory efficient
for record in process_large_csv_generator('huge_file.csv'):
    # Process one record at a time
    save_to_database(record)
    # Previous records are garbage collected

# Generator expressions vs List comprehensions
# List comprehension - creates entire list
squares_list = [x**2 for x in range(1_000_000)]  # Uses ~8MB

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(1_000_000))   # Uses ~200 bytes

# Use generator when you only need to iterate once
total = sum(x**2 for x in range(1_000_000))  # Memory efficient!

# Chaining generators
def read_records(filepath):
    """Generator: Read records from file"""
    with open(filepath) as f:
        for line in f:
            yield json.loads(line)

def filter_valid(records):
    """Generator: Filter valid records"""
    for record in records:
        if record.get('amount') and record['amount'] > 0:
            yield record

def transform(records):
    """Generator: Transform records"""
    for record in records:
        yield {
            **record,
            'amount': record['amount'] * 1.1,
            'processed': True
        }

# Chain generators - memory efficient pipeline
records = read_records('data.jsonl')
valid_records = filter_valid(records)
transformed = transform(valid_records)

# Only now do we start processing (lazy evaluation)
for record in transformed:
    save_to_db(record)
```

## 10.4 Efficient Looping Patterns

```python
# BAD: Inefficient patterns
def bad_loop_patterns():
    """Common mistakes that slow down code"""
    
    data = list(range(10000))
    
    # BAD: Repeatedly calling len()
    for i in range(len(data)):
        if i < len(data) - 1:  # len() called every iteration!
            print(data[i])
    
    # BAD: Building string with concatenation
    result = ""
    for item in data:
        result += str(item)  # Creates new string each time!
    
    # BAD: Appending to list inside loop when size is known
    squares = []
    for i in range(10000):
        squares.append(i**2)  # List grows dynamically
    
    # BAD: Multiple lookups of same value
    users = {'alice': {'age': 30}, 'bob': {'age': 25}}
    for name in users:
        print(users[name]['age'])  # Lookup users[name] multiple times

# GOOD: Optimized patterns
def good_loop_patterns():
    """Efficient loop patterns"""
    
    data = list(range(10000))
    
    # GOOD: Store len() result
    data_len = len(data)
    for i in range(data_len):
        if i < data_len - 1:
            print(data[i])
    
    # GOOD: Use join for string concatenation
    result = ''.join(str(item) for item in data)
    
    # GOOD: List comprehension (pre-allocated size)
    squares = [i**2 for i in range(10000)]
    
    # GOOD: Store lookup result in variable
    users = {'alice': {'age': 30}, 'bob': {'age': 25}}
    for name, user_data in users.items():
        print(user_data['age'])  # Single lookup

# Enumerate instead of range(len())
records = [{'id': 1}, {'id': 2}, {'id': 3}]

# BAD
for i in range(len(records)):
    print(f"Index {i}: {records[i]}")

# GOOD
for i, record in enumerate(records):
    print(f"Index {i}: {record}")

# Zip for parallel iteration
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]

# BAD
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

# GOOD
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Dictionary iteration
user_data = {'alice': 30, 'bob': 25, 'charlie': 35}

# BAD - creates intermediate list
for name in list(user_data.keys()):
    print(name)

# GOOD - direct iteration
for name in user_data:
    print(name)

# GOOD - when you need both
for name, age in user_data.items():
    print(f"{name}: {age}")

# Sets for membership testing
# BAD - O(n) for each lookup
valid_ids_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_ids = [1, 5, 8, 15, 20]

valid_users = []
for user_id in user_ids:
    if user_id in valid_ids_list:  # O(n) lookup!
        valid_users.append(user_id)

# GOOD - O(1) for each lookup
valid_ids_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
valid_users = []
for user_id in user_ids:
    if user_id in valid_ids_set:  # O(1) lookup!
        valid_users.append(user_id)

# Even better - list comprehension with set
valid_users = [uid for uid in user_ids if uid in valid_ids_set]
```

## 10.5 Memory Optimization Techniques

```python
import sys

# Use __slots__ to reduce memory for classes
class RecordWithSlots:
    """
    __slots__ prevents dynamic __dict__ creation.
    Saves ~50% memory per instance!
    """
    __slots__ = ['user_id', 'amount', 'timestamp']
    
    def __init__(self, user_id, amount, timestamp):
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp

class RecordWithoutSlots:
    """Regular class - uses __dict__ for attributes"""
    
    def __init__(self, user_id, amount, timestamp):
        self.user_id = user_id
        self.amount = amount
        self.timestamp = timestamp

# Memory comparison
with_slots = RecordWithSlots(1, 100.0, '2024-01-01')
without_slots = RecordWithoutSlots(1, 100.0, '2024-01-01')

print(f"With __slots__: {sys.getsizeof(with_slots)} bytes")
print(f"Without __slots__: {sys.getsizeof(without_slots)} bytes")

# Use appropriate data types
import numpy as np
import pandas as pd

# Python list of integers
python_list = list(range(1_000_000))
print(f"Python list: {sys.getsizeof(python_list):,} bytes")

# NumPy array - much more memory efficient
numpy_array = np.arange(1_000_000)
print(f"NumPy array: {numpy_array.nbytes:,} bytes")

# Pandas categorical for repetitive string data
df = pd.DataFrame({
    'user_id': range(1_000_000),
    'category': ['A', 'B', 'C'] * 333334  # Repeated values
})

print(f"String dtype: {df['category'].memory_usage(deep=True):,} bytes")

# Convert to categorical - saves memory!
df['category'] = df['category'].astype('category')
print(f"Category dtype: {df['category'].memory_usage(deep=True):,} bytes")

# Use generators for large sequences
def get_fibonacci_list(n):
    """Returns list - O(n) space"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def get_fibonacci_generator(n):
    """Returns generator - O(1) space"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Delete large objects when done
large_dataframe = pd.DataFrame(np.random.randn(1_000_000, 100))
# ... process dataframe ...
del large_dataframe  # Free memory immediately

# Use context managers for automatic cleanup
import tempfile

# BAD - manual file handling
f = open('data.txt', 'r')
data = f.read()
f.close()  # Might not execute if error occurs

# GOOD - automatic cleanup
with open('data.txt', 'r') as f:
    data = f.read()
# File automatically closed, even if exception occurs
```

## 10.6 Profiling and Benchmarking

```python
import time
import cProfile
import pstats
from functools import wraps

# Simple timing decorator
def timeit(func):
    """Decorator to measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Usage
@timeit
def process_data(records):
    """Some data processing function"""
    return [r for r in records if r['amount'] > 100]

# More detailed timing
import timeit as timeit_module

# Compare different approaches
def approach1():
    return [i**2 for i in range(1000)]

def approach2():
    return list(map(lambda x: x**2, range(1000)))

# Run each 1000 times and get average
time1 = timeit_module.timeit(approach1, number=1000)
time2 = timeit_module.timeit(approach2, number=1000)

print(f"Approach 1: {time1:.4f}s")
print(f"Approach 2: {time2:.4f}s")

# Profile with cProfile
def profile_function():
    """Profile this function to find bottlenecks"""
    data = list(range(100000))
    
    # Some operations
    result = []
    for num in data:
        if num % 2 == 0:
            result.append(num ** 2)
    
    return result

# Run profiler
profiler = cProfile.Profile()
profiler.enable()

profile_function()

profiler.disable()

# Print stats
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)  # Top 10 time-consuming functions

# Line profiler (requires line_profiler package)
# from line_profiler import LineProfiler
#
# def function_to_profile():
#     result = []
#     for i in range(100000):
#         result.append(i ** 2)
#     return result
#
# profiler = LineProfiler()
# profiler.add_function(function_to_profile)
# profiler.run('function_to_profile()')
# profiler.print_stats()

# Memory profiling
import tracemalloc

def memory_intensive_function():
    """Function that uses a lot of memory"""
    large_list = [i for i in range(1_000_000)]
    large_dict = {i: i**2 for i in range(1_000_000)}
    return len(large_list) + len(large_dict)

# Track memory usage
tracemalloc.start()

result = memory_intensive_function()

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

## 10.7 Optimization Checklist for Data Engineering

```python
"""
OPTIMIZATION CHECKLIST FOR DATA ENGINEERS
==========================================

1. ALGORITHM COMPLEXITY
   ✓ Use O(1) lookups (dict/set) instead of O(n) (list)
   ✓ Avoid nested loops (O(n²)) when possible
   ✓ Use built-in functions (usually optimized in C)
   ✓ Sort once, not repeatedly

2. MEMORY USAGE
   ✓ Use generators for large datasets
   ✓ Process data in chunks/batches
   ✓ Delete large objects when done
   ✓ Use appropriate data types (int64 vs int32, category for strings)
   ✓ Use __slots__ for classes with many instances

3. I/O OPTIMIZATION
   ✓ Batch database operations
   ✓ Use connection pooling
   ✓ Read/write in larger chunks
   ✓ Use binary formats (Parquet) instead of text (CSV)
   ✓ Compress data for transfer

4. PANDAS OPTIMIZATION
   ✓ Use vectorized operations (avoid apply when possible)
   ✓ Use category dtype for repetitive strings
   ✓ Read CSV in chunks for large files
   ✓ Filter early to reduce data size
   ✓ Use inplace=True when appropriate

5. SPARK OPTIMIZATION
   ✓ Use partitioning wisely
   ✓ Avoid shuffle operations when possible
   ✓ Use broadcast for small datasets in joins
   ✓ Cache intermediate results when reused
   ✓ Use appropriate file formats (Parquet, ORC)

6. GENERAL BEST PRACTICES
   ✓ Profile before optimizing (don't guess!)
   ✓ Optimize bottlenecks, not everything
   ✓ Readability > premature optimization
   ✓ Use proven libraries (NumPy, Pandas) over custom code
   ✓ Test performance with production-like data volumes
"""

# Example: Optimizing a real data pipeline

# BEFORE - Slow version
def process_transactions_slow(transactions):
    """Multiple inefficiencies"""
    results = []
    
    # Inefficiency 1: Not using set for lookup
    valid_users = [1, 2, 3, 4, 5]  # Should be set
    
    for txn in transactions:
        # Inefficiency 2: Multiple lookups
        if txn['user_id'] in valid_users:  # O(n) lookup
            # Inefficiency 3: String concatenation in loop
            desc = ""
            desc += txn['type']
            desc += " - "
            desc += str(txn['amount'])
            
            # Inefficiency 4: Creating new dict every time
            result = {}
            result['id'] = txn['id']
            result['amount'] = txn['amount'] * 1.1
            result['description'] = desc
            
            results.append(result)
    
    return results

# AFTER - Optimized version
def process_transactions_fast(transactions):
    """Optimized version"""
    # Fix 1: Use set for O(1) lookup
    valid_users = {1, 2, 3, 4, 5}
    
    # Fix 2-4: Use list comprehension with efficient operations
    return [
        {
            'id': txn['id'],
            'amount': txn['amount'] * 1.1,
            'description': f"{txn['type']} - {txn['amount']}"  # f-string
        }
        for txn in transactions
        if txn['user_id'] in valid_users  # O(1) lookup
    ]

# Benchmark
transactions = [
    {'id': i, 'user_id': i % 10, 'type': 'purchase', 'amount': i * 10}
    for i in range(10000)
]

import time

start = time.time()
result1 = process_transactions_slow(transactions)
slow_time = time.time() - start

start = time.time()
result2 = process_transactions_fast(transactions)
fast_time = time.time() - start

print(f"Slow: {slow_time:.4f}s")
print(f"Fast: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")
```

## 10.8 Common Performance Anti-Patterns

```python
# ANTI-PATTERN 1: Growing list in loop when size is known
# BAD
def create_squares_bad(n):
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares

# GOOD
def create_squares_good(n):
    return [i**2 for i in range(n)]

# ANTI-PATTERN 2: Repeated string concatenation
# BAD - Creates new string each iteration!
def join_strings_bad(items):
    result = ""
    for item in items:
        result += str(item) + ","
    return result

# GOOD - Single allocation
def join_strings_good(items):
    return ",".join(str(item) for item in items)

# ANTI-PATTERN 3: Loading entire file when streaming would work
# BAD - Memory intensive
def process_file_bad(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()  # Loads everything
    
    for line in lines:
        process_line(line)

# GOOD - Memory efficient
def process_file_good(filepath):
    with open(filepath, 'r') as f:
        for line in f:  # Streams one line at a time
            process_line(line)

# ANTI-PATTERN 4: Multiple database queries in loop
# BAD - N+1 query problem
def get_user_orders_bad(user_ids):
    results = []
    for user_id in user_ids:
        # Separate query for each user - SLOW!
        orders = db.query(f"SELECT * FROM orders WHERE user_id = {user_id}")
        results.append({'user_id': user_id, 'orders': orders})
    return results

# GOOD - Single query
def get_user_orders_good(user_ids):
    # One query for all users - FAST!
    all_orders = db.query(f"SELECT * FROM orders WHERE user_id IN ({','.join(map(str, user_ids))})")
    
    # Group by user_id
    from collections import defaultdict
    orders_by_user = defaultdict(list)
    for order in all_orders:
        orders_by_user[order['user_id']].append(order)
    
    return [{'user_id': uid, 'orders': orders_by_user[uid]} for uid in user_ids]

# ANTI-PATTERN 5: Not using vectorization in Pandas
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'amount': np.random.randn(10000)
})

# BAD - Apply with simple operation (slow)
df['doubled'] = df['amount'].apply(lambda x: x * 2)

# GOOD - Vectorized operation (fast)
df['doubled'] = df['amount'] * 2

# BAD - Iterating over DataFrame rows
total = 0
for index, row in df.iterrows():
    total += row['amount']

# GOOD - Using vectorized sum
total = df['amount'].sum()

def process_line(line):
    pass

def db_query(query):
    pass
```
