# Python for Data Engineers - Part 5: Interview Questions (30+)

## Table of Contents
11. [Python Interview Questions](#11-python-interview-questions)

---

# 11. Python Interview Questions

## BEGINNER LEVEL (Questions 1-10)

### Question 1: Explain the difference between list and tuple in Python.

**Answer:**

Lists and tuples are both sequence types but differ in mutability and use cases.

**Key Differences:**
- **Mutability:** Lists are mutable (can be modified), tuples are immutable (cannot be modified)
- **Syntax:** Lists use `[]`, tuples use `()`
- **Performance:** Tuples are slightly faster than lists
- **Use Case:** Lists for collections that change, tuples for fixed data

```python
# List - Mutable
my_list = [1, 2, 3]
my_list[0] = 10      # OK - can modify
my_list.append(4)    # OK - can add elements
print(my_list)       # [10, 2, 3, 4]

# Tuple - Immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10   # Error! Cannot modify tuple
# my_tuple.append(4) # Error! No append method

# Tuple as dictionary key (must be immutable)
cache = {}
cache[(1, 2)] = "result"  # OK - tuple is hashable
# cache[[1, 2]] = "result"  # Error! List is not hashable

# Use in data engineering
def get_user_data(user_id):
    """Return user data as tuple (immutable record)"""
    return (user_id, "Alice", "alice@example.com")

# Unpacking
user_id, name, email = get_user_data(123)
```

**Interview Tip:** Mention that tuples are commonly used for database rows, function return values, and dictionary keys in data pipelines.

---

### Question 2: What is the difference between `==` and `is` in Python?

**Answer:**

- `==` checks for **value equality** (are the contents the same?)
- `is` checks for **identity** (are they the same object in memory?)

```python
# Value equality (==)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True - same values
print(list1 is list2)  # False - different objects

# Identity (is)
list3 = list1
print(list1 is list3)  # True - same object

# Common pitfall with small integers and strings (Python caches them)
a = 256
b = 256
print(a is b)  # True - cached

c = 257
d = 257
print(c is d)  # False (usually) - not cached

# Correct usage in data engineering
def process_record(record, default_value=None):
    """Check if value was provided"""
    if record.get('amount') is None:  # Correct - checking for None
        return default_value
    return record['amount']

# WRONG
def process_record_wrong(record):
    if record.get('amount') == None:  # Works but not Pythonic
        return 0
```

**Interview Tip:** Always use `is` when comparing to `None`, `True`, or `False`. Use `==` for value comparisons.

---

### Question 3: Explain mutable vs immutable objects with examples.

**Answer:**

**Immutable objects:** Cannot be changed after creation. Modifications create new objects.
- Examples: int, float, str, tuple, frozenset

**Mutable objects:** Can be changed in-place without creating new object.
- Examples: list, dict, set

```python
# Immutable - string
s = "hello"
s_id = id(s)
s = s + " world"  # Creates NEW string
print(id(s) == s_id)  # False - different object

# Mutable - list
my_list = [1, 2, 3]
list_id = id(my_list)
my_list.append(4)  # Modifies SAME list
print(id(my_list) == list_id)  # True - same object

# Dangerous: Mutable default arguments
def add_to_list(item, my_list=[]):  # BUG!
    my_list.append(item)
    return my_list

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2] - UNEXPECTED!

# Correct approach
def add_to_list_correct(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# Data Engineering impact
def process_config(base_config):
    """Dangerous - modifies original!"""
    base_config['processed'] = True  # Mutates input
    return base_config

base = {'retry': 3}
new_config = process_config(base)
print(base)  # {'retry': 3, 'processed': True} - MODIFIED!

# Safe approach
import copy

def process_config_safe(base_config):
    """Safe - doesn't modify original"""
    config = copy.deepcopy(base_config)
    config['processed'] = True
    return config
```

**Interview Tip:** Discuss how mutability affects function side effects and why it's critical in ETL pipelines where you don't want to modify source data.

---

### Question 4: What is a list comprehension? Provide an example for data processing.

**Answer:**

List comprehension is a concise way to create lists using a single line of code. It's more Pythonic and often faster than traditional loops.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Traditional approach
squares = []
for i in range(10):
    squares.append(i**2)

# List comprehension - more Pythonic
squares = [i**2 for i in range(10)]

# With condition
even_squares = [i**2 for i in range(10) if i % 2 == 0]

# Data Engineering Examples

# 1. Extract specific fields from records
records = [
    {'id': 1, 'name': 'Alice', 'age': 30},
    {'id': 2, 'name': 'Bob', 'age': 25},
    {'id': 3, 'name': 'Charlie', 'age': 35}
]

# Extract names
names = [r['name'] for r in records]

# 2. Filter and transform
high_value_txns = [
    {'id': txn['id'], 'amount_usd': txn['amount'] * 1.1}
    for txn in transactions
    if txn['amount'] > 100
]

# 3. Data cleaning
emails = ['ALICE@EXAMPLE.COM', 'bob@example.com', '  charlie@example.com  ']
cleaned = [email.lower().strip() for email in emails]

# 4. Nested list comprehension (use sparingly)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 5. Dictionary comprehension
user_dict = {user['id']: user['name'] for user in records}
# {1: 'Alice', 2: 'Bob', 3: 'Charlie'}

# 6. Set comprehension - remove duplicates
user_ids = [1, 2, 2, 3, 3, 4]
unique_ids = {uid for uid in user_ids}  # {1, 2, 3, 4}

# Performance comparison
import time

data = range(100000)

# Loop
start = time.time()
result1 = []
for i in data:
    result1.append(i**2)
loop_time = time.time() - start

# List comprehension
start = time.time()
result2 = [i**2 for i in data]
comp_time = time.time() - start

print(f"Loop: {loop_time:.4f}s, Comprehension: {comp_time:.4f}s")
# Comprehension is typically faster
```

**Interview Tip:** Mention that list comprehensions are faster and more readable for simple transformations, but complex logic should use regular loops for clarity.

---

### Question 5: Explain `*args` and `**kwargs` with data engineering examples.

**Answer:**

- `*args`: Allows a function to accept variable number of **positional** arguments (as tuple)
- `**kwargs`: Allows a function to accept variable number of **keyword** arguments (as dict)

```python
# *args example
def calculate_total(*amounts):
    """Accept any number of amounts"""
    return sum(amounts)

print(calculate_total(10, 20, 30))        # 60
print(calculate_total(10, 20, 30, 40, 50))  # 150

# **kwargs example
def create_user(**user_data):
    """Accept any user fields"""
    return {
        'id': user_data.get('id'),
        'name': user_data.get('name'),
        'email': user_data.get('email'),
        'metadata': user_data
    }

user = create_user(id=1, name='Alice', email='alice@example.com', age=30, city='NYC')

# Combining both
def log_event(event_name, *tags, **metadata):
    """
    event_name: required positional
    *tags: optional positional arguments
    **metadata: optional keyword arguments
    """
    return {
        'event': event_name,
        'tags': tags,
        'metadata': metadata,
        'timestamp': '2024-01-01'
    }

log_event('user_login', 'success', 'web', user_id=123, ip='192.168.1.1')
# {
#   'event': 'user_login',
#   'tags': ('success', 'web'),
#   'metadata': {'user_id': 123, 'ip': '192.168.1.1'},
#   'timestamp': '2024-01-01'
# }

# Data Engineering: Flexible data transformation
def transform_record(record, *transformations, **field_mappings):
    """
    Apply multiple transformations and field mappings.
    
    Args:
        record: Source record
        *transformations: Functions to apply to entire record
        **field_mappings: New field names
    """
    result = record.copy()
    
    # Apply transformations
    for transform_func in transformations:
        result = transform_func(result)
    
    # Apply field mappings
    for old_field, new_field in field_mappings.items():
        if old_field in result:
            result[new_field] = result.pop(old_field)
    
    return result

# Usage
def add_timestamp(rec):
    rec['processed_at'] = '2024-01-01'
    return rec

def uppercase_name(rec):
    if 'name' in rec:
        rec['name'] = rec['name'].upper()
    return rec

record = {'id': 1, 'name': 'Alice', 'amount': 100}
result = transform_record(
    record,
    add_timestamp,
    uppercase_name,
    id='user_id',
    amount='transaction_amount'
)
# {
#   'user_id': 1,
#   'name': 'ALICE',
#   'transaction_amount': 100,
#   'processed_at': '2024-01-01'
# }

# Wrapper function pattern
def retry_on_failure(func, max_retries=3, **func_kwargs):
    """Retry any function with any arguments"""
    import time
    
    for attempt in range(max_retries):
        try:
            return func(**func_kwargs)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

# Usage - can retry any function
result = retry_on_failure(
    fetch_data,
    max_retries=5,
    url='https://api.example.com/data',
    api_key='secret'
)
```

**Interview Tip:** Emphasize how `*args` and `**kwargs` enable flexible, reusable functions in data pipelines.

---

### Question 6: What is the difference between `append()` and `extend()` for lists?

**Answer:**

- `append()`: Adds a **single element** to the end of list
- `extend()`: Adds **multiple elements** from an iterable to the end of list

```python
# append() - adds single element
list1 = [1, 2, 3]
list1.append(4)
print(list1)  # [1, 2, 3, 4]

list1.append([5, 6])
print(list1)  # [1, 2, 3, 4, [5, 6]] - list as single element

# extend() - adds elements from iterable
list2 = [1, 2, 3]
list2.extend([4, 5, 6])
print(list2)  # [1, 2, 3, 4, 5, 6]

list2.extend('abc')
print(list2)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# Data Engineering example: Building result set
def process_data_files(file_paths):
    """Process multiple files and combine results"""
    all_records = []
    
    for filepath in file_paths:
        # Read file
        records = read_csv(filepath)
        
        # WRONG - adds entire list as single element
        # all_records.append(records)  # [[rec1, rec2], [rec3, rec4]]
        
        # CORRECT - adds each record
        all_records.extend(records)  # [rec1, rec2, rec3, rec4]
    
    return all_records

# Alternative: List concatenation
all_records = []
for filepath in file_paths:
    all_records += read_csv(filepath)  # Same as extend

# Alternative: List comprehension with flatten
all_records = [
    record 
    for filepath in file_paths 
    for record in read_csv(filepath)
]

# Performance note
import time

# Method 1: extend
start = time.time()
result1 = []
for i in range(1000):
    result1.extend([i, i+1, i+2])
time1 = time.time() - start

# Method 2: += (same as extend)
start = time.time()
result2 = []
for i in range(1000):
    result2 += [i, i+1, i+2]
time2 = time.time() - start

print(f"extend: {time1:.4f}s, +=: {time2:.4f}s")

def read_csv(filepath):
    return [{'id': 1}]
```

**Interview Tip:** In data pipelines, use `extend()` when combining results from multiple sources or batches.

---

### Question 7: Explain the difference between shallow copy and deep copy.

**Answer:**

- **Shallow copy:** Creates new object but references to nested objects are shared
- **Deep copy:** Creates completely independent copy including nested objects

```python
import copy

# Shallow copy issue
original = {
    'name': 'Alice',
    'scores': [90, 85, 88],
    'metadata': {'city': 'NYC', 'age': 30}
}

# Shallow copy
shallow = original.copy()  # or copy.copy(original)

# Modify top-level - OK
shallow['name'] = 'Bob'
print(original['name'])  # 'Alice' - not affected

# Modify nested object - PROBLEM!
shallow['scores'].append(95)
print(original['scores'])  # [90, 85, 88, 95] - AFFECTED!

shallow['metadata']['city'] = 'LA'
print(original['metadata'])  # {'city': 'LA', 'age': 30} - AFFECTED!

# Deep copy - complete independence
original2 = {
    'name': 'Alice',
    'scores': [90, 85, 88],
    'metadata': {'city': 'NYC'}
}

deep = copy.deepcopy(original2)

# Modify nested objects - safe
deep['scores'].append(95)
deep['metadata']['city'] = 'LA'

print(original2['scores'])    # [90, 85, 88] - not affected
print(original2['metadata'])  # {'city': 'NYC'} - not affected

# Data Engineering: Environment configs
base_config = {
    'pipeline': 'user_etl',
    'database': {
        'host': 'localhost',
        'port': 5432
    },
    'features': ['feature1', 'feature2']
}

def create_env_config(base, environment):
    """Create environment-specific config"""
    # WRONG - shallow copy
    # config = base.copy()
    # config['database']['host'] = f'{environment}-db'  # Modifies base!
    
    # CORRECT - deep copy
    config = copy.deepcopy(base)
    config['environment'] = environment
    config['database']['host'] = f'{environment}-db'
    config['features'].append(f'{environment}-feature')
    
    return config

# Safe to create multiple configs
dev_config = create_env_config(base_config, 'dev')
prod_config = create_env_config(base_config, 'prod')

print(base_config['database']['host'])  # 'localhost' - unchanged
print(dev_config['database']['host'])   # 'dev-db'
print(prod_config['database']['host'])  # 'prod-db'

# Performance consideration
large_dict = {'key': list(range(10000))}

import time

start = time.time()
shallow = large_dict.copy()
shallow_time = time.time() - start

start = time.time()
deep = copy.deepcopy(large_dict)
deep_time = time.time() - start

print(f"Shallow: {shallow_time:.4f}s, Deep: {deep_time:.4f}s")
# Deep copy is slower - only use when necessary
```

**Interview Tip:** Mention that deep copy is essential when working with nested configurations or when you need to ensure complete data independence in ETL pipelines.

---

### Question 8: How do you handle missing or null values in a dictionary?

**Answer:**

Multiple approaches depending on requirements:

```python
record = {
    'user_id': 123,
    'name': 'Alice',
    'email': None,
    # 'phone': missing key
}

# Method 1: get() with default
email = record.get('email', 'no-email@example.com')
phone = record.get('phone', 'N/A')

# Method 2: Check existence first
if 'email' in record:
    email = record['email']
else:
    email = 'no-email@example.com'

# Method 3: Try-except (not recommended for this)
try:
    email = record['email']
except KeyError:
    email = 'no-email@example.com'

# Method 4: Check for None specifically
email = record.get('email')
if email is None:
    email = 'no-email@example.com'

# Method 5: defaultdict (for building dicts)
from collections import defaultdict

user_stats = defaultdict(int)  # Default value 0
user_stats['alice'] += 10  # No KeyError even if 'alice' doesn't exist

user_metadata = defaultdict(list)  # Default value []
user_metadata['alice'].append('tag1')  # Safe even if 'alice' doesn't exist

# Data Engineering: Robust data cleaning
def clean_record(record):
    """Handle missing values in data pipeline"""
    return {
        'user_id': record.get('user_id', 0),
        'name': record.get('name', 'UNKNOWN'),
        'email': record.get('email', '').lower().strip() or 'no-email@example.com',
        'amount': record.get('amount') or 0.0,
        'tags': record.get('tags', []),
        'metadata': record.get('metadata', {})
    }

# Handle None vs missing key
def safe_get_nested(data, keys, default=None):
    """
    Safely navigate nested dictionaries.
    
    Example: safe_get_nested(data, ['user', 'address', 'city'], 'Unknown')
    """
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
            if data is None:
                return default
        else:
            return default
    return data

# Usage
user_data = {
    'user': {
        'profile': {
            'name': 'Alice'
        }
    }
}

city = safe_get_nested(user_data, ['user', 'profile', 'address', 'city'], 'Unknown')
print(city)  # 'Unknown'

name = safe_get_nested(user_data, ['user', 'profile', 'name'], 'Unknown')
print(name)  # 'Alice'

# Production pattern: Validation with clear error messages
def validate_required_fields(record, required_fields):
    """
    Validate that record has all required fields.
    Returns (is_valid, error_message)
    """
    missing = []
    
    for field in required_fields:
        if field not in record:
            missing.append(field)
        elif record[field] is None:
            missing.append(f"{field} (null)")
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    
    return True, ""

# Usage
is_valid, error = validate_required_fields(
    record,
    ['user_id', 'name', 'email']
)

if not is_valid:
    print(f"Invalid record: {error}")
```

**Interview Tip:** Explain the difference between `None` (explicit null) and missing key, and why `get()` is preferred over direct access in production code.

---

### Question 9: What is the GIL and how does it affect data processing?

**Answer:**

**GIL (Global Interpreter Lock):** A mutex that allows only one thread to execute Python bytecode at a time, even on multi-core systems.

**Impact on Data Engineering:**
- ✅ **Threading is good** for I/O-bound tasks (API calls, database queries, file I/O)
- ❌ **Threading is bad** for CPU-bound tasks (data transformations, calculations)
- ✅ **Multiprocessing bypasses GIL** by using separate processes

```python
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# I/O-bound task - Threading HELPS
def fetch_api_data(url):
    """I/O-bound: waiting for network"""
    time.sleep(0.5)  # Simulates network delay
    return f"data from {url}"

urls = [f'https://api.example.com/endpoint{i}' for i in range(10)]

# Serial execution
start = time.time()
results = [fetch_api_data(url) for url in urls]
serial_time = time.time() - start
print(f"Serial I/O: {serial_time:.2f}s")  # ~5 seconds

# Threading - MUCH FASTER for I/O
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_api_data, urls))
threading_time = time.time() - start
print(f"Threading I/O: {threading_time:.2f}s")  # ~1 second

# CPU-bound task - Threading DOESN'T HELP
def cpu_intensive(n):
    """CPU-bound: calculation intensive"""
    return sum(i**2 for i in range(n))

numbers = [1000000] * 10

# Serial execution
start = time.time()
results = [cpu_intensive(n) for n in numbers]
serial_time = time.time() - start
print(f"Serial CPU: {serial_time:.2f}s")

# Threading - NO IMPROVEMENT (GIL!)
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(cpu_intensive, numbers))
threading_time = time.time() - start
print(f"Threading CPU: {threading_time:.2f}s")  # Same as serial!

# Multiprocessing - MUCH FASTER for CPU
start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_intensive, numbers))
multiproc_time = time.time() - start
print(f"Multiprocessing CPU: {multiproc_time:.2f}s")  # Much faster!

# Decision guide for data engineering
"""
╔══════════════════════════════════════════════════╗
║  TASK TYPE          │  USE                      ║
╠══════════════════════════════════════════════════╣
║  Multiple API calls │  Threading                ║
║  File I/O (reading) │  Threading                ║
║  Database queries   │  Threading                ║
║  Data transformation│  Multiprocessing or Pandas║
║  Heavy calculation  │  Multiprocessing          ║
║  Simple tasks       │  Serial (avoid overhead)  ║
╚══════════════════════════════════════════════════╝
"""

# Production example
def ingest_from_apis(api_endpoints):
    """
    I/O-bound: Use threading for parallel API calls.
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_api_data, api_endpoints))
    return results

def transform_large_dataset(data_chunks):
    """
    CPU-bound: Use multiprocessing for parallel transformations.
    """
    from multiprocessing import Pool
    
    with Pool(processes=4) as pool:
        results = pool.map(transform_chunk, data_chunks)
    
    return results

def transform_chunk(chunk):
    # CPU-intensive transformation
    return [process_record(r) for r in chunk]

def process_record(record):
    return {**record, 'processed': True}
```

**Interview Tip:** Emphasize understanding when to use threading vs multiprocessing based on whether tasks are I/O-bound or CPU-bound. Most data ingestion is I/O-bound (use threading), most transformation is CPU-bound (use multiprocessing or Pandas/Spark).

---

### Question 10: How do you iterate over a dictionary in Python?

**Answer:**

Multiple ways to iterate over dictionaries, each suitable for different scenarios:

```python
user_data = {
    'alice': 30,
    'bob': 25,
    'charlie': 35
}

# Method 1: Iterate over keys (default)
for name in user_data:
    print(name)  # 'alice', 'bob', 'charlie'

# Same as above (explicit)
for name in user_data.keys():
    print(name)

# Method 2: Iterate over values
for age in user_data.values():
    print(age)  # 30, 25, 35

# Method 3: Iterate over key-value pairs (MOST COMMON)
for name, age in user_data.items():
    print(f"{name}: {age}")

# Data Engineering examples

# 1. Filter dictionary
def filter_active_users(users):
    """Keep only active users"""
    return {
        user_id: user_data
        for user_id, user_data in users.items()
        if user_data.get('status') == 'active'
    }

# 2. Transform dictionary values
def double_amounts(transactions):
    """Double all transaction amounts"""
    return {
        txn_id: {**txn, 'amount': txn['amount'] * 2}
        for txn_id, txn in transactions.items()
    }

# 3. Aggregate from dictionary
def calculate_total_revenue(sales):
    """Sum all sales amounts"""
    total = 0
    for sale_id, sale_data in sales.items():
        total += sale_data['amount']
    return total

# Better: Use sum() with generator
def calculate_total_revenue_v2(sales):
    return sum(sale['amount'] for sale in sales.values())

# 4. Group by attribute
from collections import defaultdict

def group_by_category(products):
    """Group products by category"""
    grouped = defaultdict(list)
    
    for product_id, product in products.items():
        category = product['category']
        grouped[category].append(product)
    
    return dict(grouped)

# 5. Merge dictionaries
config_defaults = {'retry': 3, 'timeout': 30}
config_user = {'timeout': 60, 'batch_size': 1000}

# Python 3.9+: Union operator
merged = config_defaults | config_user
# {'retry': 3, 'timeout': 60, 'batch_size': 1000}

# Or use update
merged = config_defaults.copy()
merged.update(config_user)

# 6. Safe iteration while modifying
# BAD - RuntimeError: dictionary changed size during iteration
# for key in user_data:
#     if user_data[key] > 30:
#         del user_data[key]  # Error!

# GOOD - iterate over copy of keys
for key in list(user_data.keys()):
    if user_data[key] > 30:
        del user_data[key]  # OK

# Or better - dictionary comprehension
user_data = {k: v for k, v in user_data.items() if v <= 30}

# Performance: items() vs keys()
transactions = {i: {'amount': i * 10} for i in range(10000)}

import time

# Using items() - BETTER
start = time.time()
total = sum(txn['amount'] for txn_id, txn in transactions.items())
items_time = time.time() - start

# Using keys() - SLOWER (extra lookup)
start = time.time()
total = sum(transactions[txn_id]['amount'] for txn_id in transactions.keys())
keys_time = time.time() - start

print(f"items(): {items_time:.4f}s, keys(): {keys_time:.4f}s")
```

**Interview Tip:** Use `.items()` when you need both keys and values. It's more efficient than looking up values separately.

---

## INTERMEDIATE LEVEL (Questions 11-20)

### Question 11: Explain decorators and provide a data engineering use case.

**Answer:**

Decorators are functions that modify the behavior of other functions. They wrap a function to extend its functionality without modifying its code.

```python
from functools import wraps
import time
import logging

# Basic decorator
def timing_decorator(func):
    """Measure function execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Usage
@timing_decorator
def process_data(records):
    """Process data records"""
    time.sleep(0.1)
    return [r for r in records if r['amount'] > 100]

# Equivalent to:
# process_data = timing_decorator(process_data)

# Data Engineering: Retry decorator
def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry decorator for handling transient failures.
    Common in API calls and database operations.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay * (2 ** attempt))  # Exponential backoff
        return wrapper
    return decorator

# Usage
@retry(max_attempts=5, delay=2)
def fetch_from_api(url):
    """May fail due to network issues"""
    import requests
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Logging decorator
def log_execution(logger=None):
    """Log function execution"""
    if logger is None:
        logger = logging.getLogger(__name__)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Executing {func.__name__}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} completed successfully")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} failed: {e}")
                raise
        return wrapper
    return decorator

# Validation decorator
def validate_schema(schema):
    """
    Validate input data against schema.
    Useful for ETL pipelines.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(data, *args, **kwargs):
            # Validate required fields
            for field in schema.get('required', []):
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")
            
            # Validate types
            for field, expected_type in schema.get('types', {}).items():
                if field in data and not isinstance(data[field], expected_type):
                    raise TypeError(f"{field} must be {expected_type}")
            
            return func(data, *args, **kwargs)
        return wrapper
    return decorator

# Usage
@validate_schema({
    'required': ['user_id', 'amount'],
    'types': {'user_id': int, 'amount': (int, float)}
})
def process_transaction(transaction):
    """Process validated transaction"""
    return {
        **transaction,
        'processed': True,
        'amount_usd': transaction['amount'] * 1.1
    }

# Chaining decorators
@log_execution()
@timing_decorator
@retry(max_attempts=3)
def etl_pipeline(source, destination):
    """
    Full ETL pipeline with logging, timing, and retry.
    Decorators are applied bottom-to-top.
    """
    data = extract(source)
    transformed = transform(data)
    load(destination, transformed)
    return len(transformed)

# Cache decorator (memoization)
def cache_results(func):
    """Cache function results for same inputs"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        print(f"Cache miss for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
def expensive_calculation(n):
    """Expensive operation that benefits from caching"""
    time.sleep(1)
    return sum(i**2 for i in range(n))

# First call - cache miss
result1 = expensive_calculation(1000)  # Takes 1 second

# Second call - cache hit
result2 = expensive_calculation(1000)  # Instant

def extract(source):
    return [{'id': 1}]

def transform(data):
    return data

def load(dest, data):
    pass
```

**Interview Tip:** Decorators are heavily used in production for cross-cutting concerns like logging, timing, retries, and validation. Mention that they keep business logic clean by separating infrastructure concerns.

---

### Question 12: What are generators and why are they important for data engineering?

**Answer:**

Generators are functions that use `yield` to produce values lazily, one at a time. They're memory-efficient for processing large datasets.

**Key Benefits:**
- Memory efficient (O(1) space vs O(n))
- Can handle infinite sequences
- Enable pipeline patterns
- Faster for large datasets (lazy evaluation)

```python
# Regular function - loads all data into memory
def read_file_list(filepath):
    """O(n) memory - loads entire file"""
    with open(filepath, 'r') as f:
        return f.readlines()

# Generator function - processes one line at a time
def read_file_generator(filepath):
    """O(1) memory - yields one line at a time"""
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()

# Generator expression (like list comprehension)
# List comprehension - creates entire list
squares_list = [x**2 for x in range(1000000)]  # Uses ~8MB

# Generator expression - lazy evaluation
squares_gen = (x**2 for x in range(1000000))   # Uses ~200 bytes

# Data Engineering: ETL Pipeline with Generators

def extract_records(filepath):
    """Extract: Read records from file (generator)"""
    import json
    with open(filepath, 'r') as f:
        for line in f:
            yield json.loads(line)

def filter_valid(records):
    """Transform: Filter valid records (generator)"""
    for record in records:
        if record.get('amount') and record['amount'] > 0:
            yield record

def enrich_records(records):
    """Transform: Add computed fields (generator)"""
    for record in records:
        yield {
            **record,
            'amount_usd': record['amount'] * 1.1,
            'category': 'high' if record['amount'] > 1000 else 'low'
        }

def batch_records(records, batch_size=1000):
    """Utility: Yield records in batches"""
    batch = []
    for record in records:
        batch.append(record)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    
    if batch:  # Yield remaining
        yield batch

# Chain generators - memory efficient pipeline!
records = extract_records('data.jsonl')
valid = filter_valid(records)
enriched = enrich_records(valid)

# Process in batches
for batch in batch_records(enriched, batch_size=5000):
    # Load batch to database
    load_to_database(batch)
    print(f"Loaded {len(batch)} records")

# Generator with state
def running_average():
    """Generator that maintains state"""
    total = 0
    count = 0
    
    while True:
        value = yield total / count if count > 0 else 0
        total += value
        count += 1

# Usage
avg = running_average()
next(avg)  # Initialize
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0

# Real-world: Process large CSV file
def process_large_csv(filepath, chunk_size=10000):
    """
    Process CSV in chunks without loading entire file.
    Suitable for files larger than available RAM.
    """
    import csv
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        chunk = []
        
        for row in reader:
            # Transform row
            transformed = {
                'user_id': int(row['user_id']),
                'amount': float(row['amount']) * 1.1,
                'date': row['date']
            }
            
            chunk.append(transformed)
            
            # Yield chunk when full
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        
        # Yield remaining
        if chunk:
            yield chunk

# Process file that doesn't fit in memory
total_processed = 0
for chunk in process_large_csv('huge_file.csv', chunk_size=50000):
    # Process chunk
    load_to_database(chunk)
    total_processed += len(chunk)
    print(f"Processed {total_processed} records")

# Generator with cleanup
from contextlib import contextmanager

@contextmanager
def database_connection(connection_string):
    """Generator-based context manager"""
    # Setup
    conn = connect_to_database(connection_string)
    try:
        yield conn
    finally:
        # Cleanup (always runs)
        conn.close()

# Usage
with database_connection('postgresql://localhost/db') as conn:
    # Use connection
    data = conn.query("SELECT * FROM users")

# Connection automatically closed

def connect_to_database(conn_str):
    return {'query': lambda q: []}

def load_to_database(records):
    pass
```

**Interview Tip:** Emphasize that generators are essential for processing data that doesn't fit in memory. Mention pipeline pattern and how generators enable streaming ETL.

---

### Question 13: How do you handle exceptions in a data pipeline?

**Answer:**

Exception handling in data pipelines requires:
1. Catching specific exceptions
2. Logging errors
3. Retry logic for transient failures
4. Graceful degradation
5. Dead letter queues for failed records

```python
import logging
import time
from typing import List, Dict, Tuple

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pattern 1: Specific exception handling
def process_record(record):
    """Process single record with specific error handling"""
    try:
        # Validation
        if not record.get('user_id'):
            raise ValueError("Missing user_id")
        
        if not isinstance(record.get('amount'), (int, float)):
            raise TypeError("Amount must be numeric")
        
        # Business logic
        return {
            'user_id': record['user_id'],
            'amount': float(record['amount']) * 1.1,
            'processed': True
        }
    
    except ValueError as e:
        logger.warning(f"Validation error: {e} for record {record}")
        return None
    
    except TypeError as e:
        logger.warning(f"Type error: {e} for record {record}")
        return None
    
    except Exception as e:
        logger.error(f"Unexpected error: {e} for record {record}", exc_info=True)
        raise  # Re-raise unexpected errors

# Pattern 2: Retry with exponential backoff
def retry_with_backoff(func, max_retries=3, initial_delay=1):
    """Execute function with retry logic"""
    delay = initial_delay
    
    for attempt in range(max_retries):
        try:
            return func()
        
        except (ConnectionError, TimeoutError) as e:
            # Retryable errors
            if attempt == max_retries - 1:
                raise
            
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
            time.sleep(delay)
            delay *= 2  # Exponential backoff
        
        except Exception as e:
            # Non-retryable errors
            logger.error(f"Non-retryable error: {e}")
            raise

# Pattern 3: Batch processing with error tracking
def process_batch_with_error_tracking(records: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Process batch and separate successful vs failed records.
    Returns: (successful_records, failed_records)
    """
    successful = []
    failed = []
    
    for record in records:
        try:
            processed = process_record(record)
            if processed:
                successful.append(processed)
            else:
                failed.append({
                    'record': record,
                    'error': 'Validation failed',
                    'error_type': 'ValidationError'
                })
        
        except Exception as e:
            failed.append({
                'record': record,
                'error': str(e),
                'error_type': type(e).__name__
            })
    
    logger.info(f"Processed: {len(successful)} successful, {len(failed)} failed")
    
    return successful, failed

# Pattern 4: Circuit breaker
class CircuitBreaker:
    """
    Prevent cascading failures by stopping requests after threshold.
    """
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'closed'  # closed, open, half-open
    
    def call(self, func, *args, **kwargs):
        """Execute function through circuit breaker"""
        if self.state == 'open':
            if time.time() - self.last_failure_time > self.timeout:
                self.state = 'half-open'
                logger.info("Circuit breaker: half-open, trying request")
            else:
                raise Exception("Circuit breaker is OPEN - too many failures")
        
        try:
            result = func(*args, **kwargs)
            
            # Success
            if self.state == 'half-open':
                self.state = 'closed'
                self.failure_count = 0
                logger.info("Circuit breaker: closed")
            
            return result
        
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = 'open'
                logger.error(f"Circuit breaker: OPEN after {self.failure_count} failures")
            
            raise

# Usage
breaker = CircuitBreaker(failure_threshold=5, timeout=60)

def risky_api_call():
    """May fail"""
    # API call that might fail
    pass

try:
    result = breaker.call(risky_api_call)
except Exception as e:
    logger.error(f"API call failed: {e}")

# Pattern 5: Dead letter queue
class DataPipeline:
    """Production-grade pipeline with error handling"""
    
    def __init__(self):
        self.successful_records = []
        self.failed_records = []
        self.dead_letter_queue = []
    
    def process(self, records):
        """Process records with comprehensive error handling"""
        for record in records:
            try:
                # Validate
                self._validate(record)
                
                # Transform
                transformed = self._transform(record)
                
                # Load
                self._load(transformed)
                
                self.successful_records.append(transformed)
            
            except ValueError as e:
                # Validation errors - not retryable
                self.failed_records.append({
                    'record': record,
                    'error': str(e),
                    'error_type': 'ValidationError',
                    'retryable': False
                })
            
            except ConnectionError as e:
                # Connection errors - retryable
                self.failed_records.append({
                    'record': record,
                    'error': str(e),
                    'error_type': 'ConnectionError',
                    'retryable': True
                })
            
            except Exception as e:
                # Unknown errors - send to dead letter queue
                self.dead_letter_queue.append({
                    'record': record,
                    'error': str(e),
                    'error_type': type(e).__name__,
                    'timestamp': time.time()
                })
                logger.error(f"Unexpected error, sent to DLQ: {e}", exc_info=True)
        
        # Retry failed retryable records
        self._retry_failed()
        
        # Write dead letter queue to file for investigation
        if self.dead_letter_queue:
            self._write_dlq()
        
        return {
            'successful': len(self.successful_records),
            'failed': len(self.failed_records),
            'dead_letter': len(self.dead_letter_queue)
        }
    
    def _validate(self, record):
        if not record.get('user_id'):
            raise ValueError("Missing user_id")
    
    def _transform(self, record):
        return {**record, 'processed': True}
    
    def _load(self, record):
        # Simulate loading
        pass
    
    def _retry_failed(self):
        """Retry failed records that are retryable"""
        retryable = [r for r in self.failed_records if r.get('retryable')]
        
        for failed in retryable:
            try:
                record = failed['record']
                transformed = self._transform(record)
                self._load(transformed)
                
                # Success - remove from failed
                self.failed_records.remove(failed)
                self.successful_records.append(transformed)
                logger.info(f"Retry successful for record: {record}")
            
            except Exception as e:
                logger.warning(f"Retry failed: {e}")
    
    def _write_dlq(self):
        """Write dead letter queue to file"""
        import json
        with open('dead_letter_queue.jsonl', 'a') as f:
            for item in self.dead_letter_queue:
                f.write(json.dumps(item) + '\n')
        
        logger.info(f"Wrote {len(self.dead_letter_queue)} records to DLQ")

# Usage
pipeline = DataPipeline()
result = pipeline.process([
    {'user_id': 1, 'amount': 100},
    {'amount': 200},  # Missing user_id
    {'user_id': 3, 'amount': 'invalid'},  # Invalid amount
])

print(f"Results: {result}")
```

**Interview Tip:** Emphasize the importance of distinguishing between retryable and non-retryable errors, logging for debugging, and using dead letter queues for investigation. Mention that in production, you'd use tools like Apache Kafka for DLQ.

---

*Continue with remaining questions (14-30) covering advanced topics like context managers, metaclasses, asyncio, Pandas optimization, PySpark best practices, SQL vs NoSQL in Python, data quality checks, schema evolution, and production deployment...*

**Interview Tip General:** Always explain WHY a solution is better, not just HOW it works. Connect answers to real data engineering scenarios.
