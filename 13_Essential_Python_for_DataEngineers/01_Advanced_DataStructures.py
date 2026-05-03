"""
================================================================================
                    ADVANCED PYTHON DATA STRUCTURES
================================================================================
Essential Python data structures and techniques for Data Engineers
Last Updated: May 2026
================================================================================

TABLE OF CONTENTS:
1. COLLECTIONS MODULE - Advanced Dictionary Types
2. ITERATORS AND GENERATORS
3. LIST, DICT, SET COMPREHENSIONS
4. CONTEXT MANAGERS
5. COMMON INTERVIEW QUESTIONS & SOLUTIONS
================================================================================
"""

from collections import defaultdict, Counter, OrderedDict, namedtuple, deque, ChainMap
from typing import Generator, Iterator, List, Dict, Any, Tuple, Optional
import itertools

# ============================================================================
# 1. COLLECTIONS MODULE - Advanced Dictionary Types
# ============================================================================

print("="*80)
print("1. COLLECTIONS MODULE")
print("="*80)

# ============================================================================
# defaultdict - Avoids KeyError by providing default values
# ============================================================================

print("\n--- defaultdict Example ---")

# Problem without defaultdict
word_count_old = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for word in words:
    if word in word_count_old:
        word_count_old[word] += 1
    else:
        word_count_old[word] = 1

print(f"Traditional approach: {word_count_old}")

# Solution with defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1

print(f"Using defaultdict(int): {dict(word_count)}")

# defaultdict with list - for grouping values
data = [('A', 1), ('B', 2), ('A', 3), ('C', 4), ('B', 5)]
groups = defaultdict(list)

for key, value in data:
    groups[key].append(value)

print(f"Grouping with defaultdict(list): {dict(groups)}")

# Real-world example: Building index from data
records = [
    {'id': 1, 'category': 'electronics', 'price': 100},
    {'id': 2, 'category': 'clothing', 'price': 50},
    {'id': 3, 'category': 'electronics', 'price': 200},
]

category_index = defaultdict(list)
for record in records:
    category_index[record['category']].append(record)

print(f"Category index: {dict(category_index)}")

# ============================================================================
# Counter - Count occurrences of elements
# ============================================================================

print("\n--- Counter Example ---")

# Count word frequency
text = "the quick brown fox jumps over the lazy dog the"
word_counter = Counter(text.split())
print(f"Word counts: {word_counter}")

# Most common elements
print(f"Top 3 most common: {word_counter.most_common(3)}")

# Counting list elements
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
num_counter = Counter(numbers)
print(f"Number counts: {num_counter}")

# Counter arithmetic (very useful in data analysis)
counter1 = Counter(['a', 'b', 'c', 'a', 'b'])
counter2 = Counter(['a', 'c', 'd', 'a'])

# Addition
print(f"Counter1 + Counter2: {counter1 + counter2}")

# Subtraction
print(f"Counter1 - Counter2: {counter1 - counter2}")

# Intersection (minimum of counts)
print(f"Counter1 & Counter2: {counter1 & counter2}")

# Union (maximum of counts)
print(f"Counter1 | Counter2: {counter1 | counter2}")

# Real-world: Finding duplicate values in dataset
dataset = [10, 20, 30, 10, 40, 20, 10, 50]
duplicates = Counter(dataset)
duplicate_items = {item: count for item, count in duplicates.items() if count > 1}
print(f"Duplicate items: {duplicate_items}")

# ============================================================================
# OrderedDict - Maintains insertion order (useful for specific versions)
# ============================================================================

print("\n--- OrderedDict Example ---")

# Note: In Python 3.7+, regular dict maintains insertion order
# But OrderedDict has additional methods like move_to_end()

ordered = OrderedDict()
ordered['zebra'] = 1
ordered['apple'] = 2
ordered['mango'] = 3

print(f"OrderedDict: {ordered}")
print(f"Items: {list(ordered.items())}")

# Move item to end
ordered.move_to_end('apple')
print(f"After moving 'apple' to end: {ordered}")

# Move item to beginning
ordered.move_to_end('zebra', last=False)
print(f"After moving 'zebra' to beginning: {ordered}")

# ============================================================================
# namedtuple - Lightweight class for structured data
# ============================================================================

print("\n--- namedtuple Example ---")

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create instances
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

print(f"Point 1: {p1}")
print(f"Access x: {p1.x}, y: {p1.y}, z: {p1.z}")

# Convert to dict
print(f"As dictionary: {p1._asdict()}")

# Real-world: Representing database records
StudentRecord = namedtuple('StudentRecord', ['id', 'name', 'marks', 'subject'])
student = StudentRecord(1, 'Alice', 85, 'Math')
print(f"Student: {student}")

# Using in data processing pipeline
students = [
    StudentRecord(1, 'Alice', 85, 'Math'),
    StudentRecord(2, 'Bob', 78, 'Science'),
    StudentRecord(3, 'Charlie', 92, 'Math'),
]

# Group by subject
subject_groups = defaultdict(list)
for student in students:
    subject_groups[student.subject].append(student)

print(f"Students by subject: {dict(subject_groups)}")

# ============================================================================
# deque - Double-ended queue (optimized for additions/removals at both ends)
# ============================================================================

print("\n--- deque Example ---")

# Create deque
queue = deque([1, 2, 3, 4, 5])
print(f"Initial deque: {queue}")

# Add to left (beginning)
queue.appendleft(0)
print(f"After appendleft(0): {queue}")

# Add to right (end)
queue.append(6)
print(f"After append(6): {queue}")

# Remove from left
queue.popleft()
print(f"After popleft(): {queue}")

# Remove from right
queue.pop()
print(f"After pop(): {queue}")

# Rotate
queue.rotate(2)  # Rotate right by 2 positions
print(f"After rotate(2): {queue}")

# Real-world: Sliding window for moving average
def moving_average(data, window_size):
    """Calculate moving average using deque"""
    window = deque(maxlen=window_size)
    result = []
    
    for value in data:
        window.append(value)
        if len(window) == window_size:
            result.append(sum(window) / window_size)
    
    return result

prices = [100, 102, 101, 103, 105, 104, 106, 108]
moving_avg = moving_average(prices, 3)
print(f"Moving average (window=3): {moving_avg}")

# ============================================================================
# ChainMap - Combine multiple dictionaries
# ============================================================================

print("\n--- ChainMap Example ---")

# Simulate configuration hierarchy
default_config = {'debug': False, 'timeout': 30, 'retries': 3}
user_config = {'debug': True, 'timeout': 60}
env_config = {'retries': 5}

# Without ChainMap - need to merge manually
config = {**default_config, **user_config, **env_config}
print(f"Merged config: {config}")

# With ChainMap - maintains separate dicts but provides unified view
configs = ChainMap(env_config, user_config, default_config)
print(f"ChainMap view: {dict(configs)}")
print(f"Get timeout: {configs['timeout']}")

# Real-world: Layered configuration system
class ConfigManager:
    def __init__(self):
        self.defaults = {'host': 'localhost', 'port': 5432, 'ssl': False}
        self.app_config = {}
        self.user_config = {}
    
    def get_config(self):
        return ChainMap(self.user_config, self.app_config, self.defaults)

# ============================================================================
# 2. ITERATORS AND GENERATORS
# ============================================================================

print("\n" + "="*80)
print("2. ITERATORS AND GENERATORS")
print("="*80)

# ============================================================================
# Custom Iterator
# ============================================================================

print("\n--- Custom Iterator Example ---")

class RangeIterator:
    """Custom iterator that generates numbers in range"""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Use custom iterator
custom_range = RangeIterator(0, 5)
print(f"Custom iterator: {list(custom_range)}")

# ============================================================================
# Generators - Memory efficient iterators
# ============================================================================

print("\n--- Generator Example ---")

# Generator function using yield
def simple_generator(n):
    """Generate numbers from 0 to n-1"""
    i = 0
    while i < n:
        print(f"  Yielding {i}")  # Shows lazy evaluation
        yield i
        i += 1

print("Generator (lazy evaluation):")
gen = simple_generator(3)
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")
print(f"Third value: {next(gen)}")

# Fibonacci generator
def fibonacci(max_count):
    """Generate Fibonacci sequence up to max_count"""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

print(f"Fibonacci sequence: {list(fibonacci(10))}")

# Generator expression (similar to list comprehension but lazy)
numbers = range(1, 11)

# List comprehension (creates full list immediately)
squares_list = [x**2 for x in numbers]
print(f"List comprehension: {squares_list}")

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in numbers)
print(f"Generator expression: {squares_gen}")
print(f"Values from generator: {list(squares_gen)}")

# Real-world: Efficient file processing
def read_large_file(file_path, chunk_size=1024):
    """Generator to read large files efficiently"""
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Example (requires actual file): 
# for chunk in read_large_file('large_file.txt'):
#     process(chunk)

# Real-world: Database result streaming
def fetch_records_from_db(query, batch_size=100):
    """Generator to fetch records from database in batches"""
    offset = 0
    while True:
        # In real scenario: execute query with LIMIT and OFFSET
        # records = db.execute(f"{query} LIMIT {batch_size} OFFSET {offset}")
        
        # Simulated records
        if offset >= 300:  # Assume 300 total records
            break
        
        records = [{'id': i, 'name': f'User{i}'} for i in range(offset, offset + batch_size)]
        offset += batch_size
        
        yield from records  # Python 3.3+ syntax

# Generator with send() - Two-way communication
def echo_generator():
    """Generator that receives and echoes values"""
    print("Echo generator started")
    while True:
        received = yield
        print(f"Received: {received}")

print("\n--- Generator with send() ---")
gen = echo_generator()
next(gen)  # Prime the generator
gen.send("Hello")
gen.send("World")

# ============================================================================
# 3. COMPREHENSIONS
# ============================================================================

print("\n" + "="*80)
print("3. COMPREHENSIONS")
print("="*80)

# ============================================================================
# List Comprehension
# ============================================================================

print("\n--- List Comprehension Examples ---")

# Basic
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(f"3x3 Matrix: {matrix}")

# With transformation
words = ["apple", "banana", "cherry"]
word_lengths = [len(word) for word in words]
print(f"Word lengths: {word_lengths}")

# Multiple conditions
numbers = range(1, 20)
result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"Numbers divisible by both 2 and 3: {result}")

# ============================================================================
# Dictionary Comprehension
# ============================================================================

print("\n--- Dictionary Comprehension Examples ---")

# Simple key-value mapping
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# From list with transformation
words = ["apple", "banana", "cherry"]
word_dict = {word: len(word) for word in words}
print(f"Word lengths dict: {word_dict}")

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# With condition
only_even = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Only even squares: {only_even}")

# ============================================================================
# Set Comprehension
# ============================================================================

print("\n--- Set Comprehension Examples ---")

# Simple set
unique_squares = {x**2 for x in range(-5, 6)}
print(f"Unique squares: {unique_squares}")

# With condition
even_set = {x for x in range(20) if x % 2 == 0}
print(f"Even set: {even_set}")

# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(f"Unique numbers: {unique}")

# ============================================================================
# Nested Comprehensions (Advanced)
# ============================================================================

print("\n--- Nested Comprehensions ---")

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]
print(f"Flattened: {flattened}")

# Cartesian product
list1 = [1, 2]
list2 = ['a', 'b']
cartesian = [(x, y) for x in list1 for y in list2]
print(f"Cartesian product: {cartesian}")

# Real-world: Data transformation
data = [
    {'name': 'Alice', 'scores': [85, 90, 88]},
    {'name': 'Bob', 'scores': [78, 82, 80]},
]

# Extract all scores
all_scores = [score for student in data for score in student['scores']]
print(f"All scores: {all_scores}")

# ============================================================================
# 4. CONTEXT MANAGERS
# ============================================================================

print("\n" + "="*80)
print("4. CONTEXT MANAGERS")
print("="*80)

# ============================================================================
# Using Context Managers (with statement)
# ============================================================================

print("\n--- Context Manager with File ---")

# Automatic file closing with 'with'
content = ""
with open('sample.txt', 'w') as f:
    f.write("Hello, World!")
    content = "File written"

print(f"Status: {content}")

# ============================================================================
# Creating Custom Context Manager - Class based
# ============================================================================

print("\n--- Custom Context Manager (Class) ---")

class DatabaseConnection:
    """Custom context manager for database connections"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}...")
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False  # Don't suppress exceptions

# Use custom context manager
with DatabaseConnection("MyDatabase") as conn:
    print(f"Using: {conn}")

# ============================================================================
# Creating Custom Context Manager - Function based
# ============================================================================

print("\n--- Custom Context Manager (Function) ---")

from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    """Decorator-based context manager"""
    print(f"Connecting to {db_name}...")
    connection = f"Connection to {db_name}"
    
    try:
        yield connection
    finally:
        print(f"Closing connection to {db_name}...")

# Use function-based context manager
with database_connection("MyDB") as conn:
    print(f"Using: {conn}")

# ============================================================================
# Real-world: Timer Context Manager
# ============================================================================

print("\n--- Timer Context Manager ---")

import time

@contextmanager
def timer(name="Operation"):
    """Context manager to measure execution time"""
    start_time = time.time()
    print(f"{name} started...")
    
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"{name} completed in {elapsed:.4f} seconds")

# Use timer
with timer("Data Processing"):
    time.sleep(0.5)
    print("Processing data...")

# ============================================================================
# Real-world: Suppress Exceptions
# ============================================================================

print("\n--- Suppress Exceptions ---")

from contextlib import suppress

# Suppress specific exceptions
with suppress(FileNotFoundError, KeyError):
    # This won't raise an error
    open('non_existent.txt', 'r')
    d = {}
    value = d['missing_key']

print("Exceptions were suppressed")

# ============================================================================
# Real-world: Resource Pool Manager
# ============================================================================

print("\n--- Resource Pool Manager ---")

class ConnectionPool:
    """Simple connection pool context manager"""
    def __init__(self, size=5):
        self.size = size
        self.pool = [f"Connection_{i}" for i in range(size)]
        self.available = self.pool.copy()
    
    def __enter__(self):
        if not self.available:
            raise RuntimeError("No connections available")
        conn = self.available.pop()
        self.current_conn = conn
        print(f"Allocated: {conn}")
        return conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.available.append(self.current_conn)
        print(f"Released: {self.current_conn}")

pool = ConnectionPool(size=3)
with pool as conn1:
    print(f"Using: {conn1}")
    with pool as conn2:
        print(f"Using: {conn2}")

# ============================================================================
# 5. COMMON INTERVIEW QUESTIONS & SOLUTIONS
# ============================================================================

print("\n" + "="*80)
print("5. COMMON INTERVIEW QUESTIONS & SOLUTIONS")
print("="*80)

# ============================================================================
# Q1: Find duplicate elements in list efficiently
# ============================================================================

print("\n--- Q1: Find Duplicate Elements ---")

def find_duplicates(arr):
    """Find duplicate elements efficiently"""
    counts = Counter(arr)
    return [item for item, count in counts.items() if count > 1]

test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Duplicates in {test_list}: {find_duplicates(test_list)}")

# ============================================================================
# Q2: Group data by key efficiently
# ============================================================================

print("\n--- Q2: Group Data by Key ---")

def group_by_key(data, key_func):
    """Group list of items by a key function"""
    groups = defaultdict(list)
    for item in data:
        key = key_func(item)
        groups[key].append(item)
    return dict(groups)

students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
]

grouped = group_by_key(students, lambda x: x['grade'])
print(f"Grouped by grade: {grouped}")

# ============================================================================
# Q3: Flatten nested list efficiently
# ============================================================================

print("\n--- Q3: Flatten Nested List ---")

def flatten_list(nested_list):
    """Flatten nested list using generator"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

nested = [[1, 2], [3, [4, 5]], [6, 7, [8, 9]]]
flattened_result = list(flatten_list(nested))
print(f"Flattened: {flattened_result}")

# ============================================================================
# Q4: Most frequent elements
# ============================================================================

print("\n--- Q4: Most Frequent Elements ---")

def top_k_frequent(arr, k):
    """Find top k most frequent elements"""
    counter = Counter(arr)
    return [item for item, count in counter.most_common(k)]

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Top 2 frequent: {top_k_frequent(numbers, 2)}")

# ============================================================================
# Q5: Memory-efficient large dataset processing
# ============================================================================

print("\n--- Q5: Efficient Large Dataset Processing ---")

def process_large_dataset(data_generator, batch_size=10):
    """Process large dataset in batches using generator"""
    batch = []
    for item in data_generator:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

def sample_data_generator():
    """Simulate data from external source"""
    for i in range(25):
        yield {'id': i, 'value': i * 2}

for batch in process_large_dataset(sample_data_generator(), 10):
    print(f"Processing batch of {len(batch)} items")

print("\n" + "="*80)
print("END OF ADVANCED PYTHON DATA STRUCTURES")
print("="*80)
