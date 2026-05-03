"""
================================================================================
                 FUNCTIONAL PROGRAMMING FOR DATA ENGINEERS
================================================================================
Pure functions, higher-order functions, decorators, and function composition
Last Updated: May 2026
================================================================================

TABLE OF CONTENTS:
1. PURE FUNCTIONS & IMMUTABILITY
2. HIGHER-ORDER FUNCTIONS (map, filter, reduce)
3. LAMBDA FUNCTIONS
4. FUNCTION COMPOSITION
5. DECORATORS
6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
================================================================================
"""

from functools import reduce, wraps, lru_cache
from typing import Callable, List, Any, Optional, TypeVar, Generic
import time
import json

print("="*80)
print("FUNCTIONAL PROGRAMMING FOR DATA ENGINEERS")
print("="*80)

# ============================================================================
# 1. PURE FUNCTIONS & IMMUTABILITY
# ============================================================================

print("\n" + "="*80)
print("1. PURE FUNCTIONS & IMMUTABILITY")
print("="*80)

# ============================================================================
# Pure Functions vs Impure Functions
# ============================================================================

print("\n--- Pure vs Impure Functions ---")

# IMPURE: Has side effects (modifies external state)
global_counter = 0

def impure_increment(value):
    """Impure: Modifies global state"""
    global global_counter
    global_counter += 1
    return value + 1

print(f"Global counter: {global_counter}")
result1 = impure_increment(5)
print(f"Result: {result1}, Global counter: {global_counter}")
result2 = impure_increment(5)
print(f"Result: {result2}, Global counter: {global_counter}")

# PURE: No side effects, same input = same output
def pure_add(a, b):
    """Pure: Always returns same result for same input"""
    return a + b

print(f"\nPure function:")
print(f"pure_add(5, 3) = {pure_add(5, 3)}")
print(f"pure_add(5, 3) = {pure_add(5, 3)}")  # Same result

# ============================================================================
# Working with Immutable Data
# ============================================================================

print("\n--- Immutable Data Structures ---")

# MUTABLE: Lists and dicts can be modified in place
mutable_list = [1, 2, 3]
mutable_list.append(4)  # Modifies original
print(f"Mutable list after append: {mutable_list}")

# IMMUTABLE: Tuples and frozensets cannot be modified
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # TypeError

# Create new instead of modifying
new_tuple = immutable_tuple + (4,)
print(f"Original tuple: {immutable_tuple}")
print(f"New tuple: {new_tuple}")

# Using tuple unpacking and concatenation instead of mutation
def append_immutable(items, new_item):
    """Pure function: Creates new tuple instead of modifying"""
    return items + (new_item,)

original = (1, 2, 3)
result = append_immutable(original, 4)
print(f"Original: {original}, Result: {result}")

# ============================================================================
# Data transformation without side effects
# ============================================================================

print("\n--- Data Transformation (Pure vs Impure) ---")

# IMPURE: Modifies data in place
def scale_prices_impure(prices):
    """Impure: Modifies original data"""
    for i in range(len(prices)):
        prices[i] *= 1.1  # 10% increase
    return prices

prices = [100, 200, 300]
print(f"Original prices: {prices}")
scaled = scale_prices_impure(prices)
print(f"After impure scale: {prices}")  # Original modified!

# PURE: Creates new data
def scale_prices_pure(prices):
    """Pure: Returns new data without modifying original"""
    return tuple(price * 1.1 for price in prices)

prices = [100, 200, 300]
print(f"\nOriginal prices: {prices}")
scaled = scale_prices_pure(prices)
print(f"After pure scale (original): {prices}")  # Original unchanged
print(f"Scaled prices: {scaled}")

# ============================================================================
# 2. HIGHER-ORDER FUNCTIONS
# ============================================================================

print("\n" + "="*80)
print("2. HIGHER-ORDER FUNCTIONS")
print("="*80)

# ============================================================================
# map() - Apply function to each element
# ============================================================================

print("\n--- map() Function ---")

numbers = [1, 2, 3, 4, 5]

# Traditional approach
squares_traditional = []
for n in numbers:
    squares_traditional.append(n ** 2)
print(f"Squares (traditional): {squares_traditional}")

# Using map()
squares_map = list(map(lambda x: x ** 2, numbers))
print(f"Squares (map): {squares_map}")

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
summed = list(map(lambda x, y: x + y, list1, list2))
print(f"Sum pairs: {summed}")

# Real-world: Transform data records
def convert_to_uppercase(name):
    """Convert name to uppercase"""
    return name.upper()

names = ["alice", "bob", "charlie"]
upper_names = list(map(convert_to_uppercase, names))
print(f"Uppercase names: {upper_names}")

# ============================================================================
# filter() - Keep elements matching condition
# ============================================================================

print("\n--- filter() Function ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# Filter with condition
def is_greater_than_5(x):
    return x > 5

greater_than_5 = list(filter(is_greater_than_5, numbers))
print(f"Greater than 5: {greater_than_5}")

# Real-world: Filter valid records
records = [
    {'id': 1, 'name': 'Alice', 'score': 85},
    {'id': 2, 'name': 'Bob', 'score': 45},
    {'id': 3, 'name': 'Charlie', 'score': 92},
    {'id': 4, 'name': 'Diana', 'score': 38},
]

def is_passing(record):
    """Filter passing records (score >= 70)"""
    return record['score'] >= 70

passing_records = list(filter(is_passing, records))
print(f"Passing records: {passing_records}")

# ============================================================================
# reduce() - Aggregate to single value
# ============================================================================

print("\n--- reduce() Function ---")

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(f"Sum: {total}")

# Product using reduce
product = reduce(lambda acc, x: acc * x, numbers, 1)
print(f"Product: {product}")

# Find maximum
max_value = reduce(lambda acc, x: x if x > acc else acc, numbers)
print(f"Maximum: {max_value}")

# Real-world: Merge dictionaries
records = [
    {'alice': 85},
    {'bob': 78},
    {'charlie': 92},
]

merged = reduce(lambda acc, record: {**acc, **record}, records, {})
print(f"Merged records: {merged}")

# ============================================================================
# Combining map, filter, reduce
# ============================================================================

print("\n--- Combining map, filter, reduce ---")

# Calculate average score of passing students
records = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 45},
    {'name': 'Charlie', 'score': 92},
    {'name': 'Diana', 'score': 38},
]

passing_scores = list(
    map(lambda r: r['score'],
        filter(lambda r: r['score'] >= 70, records))
)
average = reduce(lambda acc, x: acc + x, passing_scores, 0) / len(passing_scores)
print(f"Average score of passing students: {average}")

# ============================================================================
# 3. LAMBDA FUNCTIONS
# ============================================================================

print("\n" + "="*80)
print("3. LAMBDA FUNCTIONS")
print("="*80)

# ============================================================================
# Lambda Basics
# ============================================================================

print("\n--- Lambda Basics ---")

# Simple lambda
add = lambda x, y: x + y
print(f"Lambda add: {add(5, 3)}")

# Lambda in sorted
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
]

sorted_by_grade = sorted(students, key=lambda s: s['grade'], reverse=True)
print(f"Sorted by grade: {sorted_by_grade}")

# ============================================================================
# When NOT to use Lambda
# ============================================================================

print("\n--- When NOT to use Lambda ---")

# BAD: Complex logic in lambda (hard to read)
# result = list(map(lambda x: x**2 if x > 0 else -x**2, numbers))

# GOOD: Use named function for complex logic
def transform_number(x):
    """Transform number: square if positive, negate square if negative"""
    return x**2 if x > 0 else -x**2

result = list(map(transform_number, [-2, -1, 0, 1, 2]))
print(f"Transformed numbers: {result}")

# Lambda limitations
# - Can't contain multiple statements
# - Can't contain complex control flow
# - Hard to debug
# - Reduce code readability for complex logic

# ============================================================================
# 4. FUNCTION COMPOSITION
# ============================================================================

print("\n" + "="*80)
print("4. FUNCTION COMPOSITION")
print("="*80)

# ============================================================================
# Manual Function Composition
# ============================================================================

print("\n--- Manual Function Composition ---")

def add_10(x):
    return x + 10

def multiply_by_2(x):
    return x * 2

def square(x):
    return x ** 2

# Traditional nested approach (hard to read - inside out)
result = square(multiply_by_2(add_10(5)))
print(f"Result (nested): {result}")

# ============================================================================
# Pipe Pattern - Left to Right
# ============================================================================

print("\n--- Pipe Pattern ---")

def pipe(*functions):
    """Compose functions left to right"""
    def composed(value):
        for func in functions:
            value = func(value)
        return value
    return composed

pipeline = pipe(add_10, multiply_by_2, square)
result = pipeline(5)
print(f"Result (pipe): {result}")

# Real-world: Data processing pipeline
def parse_json(data):
    return json.loads(data)

def extract_users(data):
    return data.get('users', [])

def filter_active(users):
    return [u for u in users if u.get('active', True)]

def get_names(users):
    return [u['name'] for u in users]

data_pipeline = pipe(parse_json, extract_users, filter_active, get_names)

# Usage
json_data = '{"users": [{"name": "Alice", "active": true}, {"name": "Bob", "active": false}]}'
names = data_pipeline(json_data)
print(f"Active user names: {names}")

# ============================================================================
# Compose Pattern - Right to Left
# ============================================================================

print("\n--- Compose Pattern ---")

def compose(*functions):
    """Compose functions right to left (mathematical composition)"""
    def composed(value):
        for func in reversed(functions):
            value = func(value)
        return value
    return composed

composed_fn = compose(square, multiply_by_2, add_10)
result = composed_fn(5)
print(f"Result (compose): {result}")

# ============================================================================
# 5. DECORATORS
# ============================================================================

print("\n" + "="*80)
print("5. DECORATORS")
print("="*80)

# ============================================================================
# Simple Decorator
# ============================================================================

print("\n--- Simple Decorator ---")

def simple_decorator(func):
    """Simple decorator that adds behavior"""
    def wrapper(*args, **kwargs):
        print(f"Before calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"After calling {func.__name__}")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# ============================================================================
# Decorator with Arguments
# ============================================================================

print("\n--- Decorator with Arguments ---")

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()

# ============================================================================
# Timing Decorator
# ============================================================================

print("\n--- Timing Decorator ---")

def timer(func):
    """Decorator to measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

slow_function()

# ============================================================================
# Caching Decorator (Memoization)
# ============================================================================

print("\n--- Caching Decorator ---")

def memoize(func):
    """Decorator to cache function results"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        print(f"Computing for {args}")
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(5): {fibonacci(5)}")
print(f"Fibonacci(5): {fibonacci(5)}")  # From cache

# Using built-in lru_cache
@lru_cache(maxsize=128)
def fibonacci_builtin(n):
    """Calculate fibonacci using lru_cache"""
    if n <= 1:
        return n
    return fibonacci_builtin(n - 1) + fibonacci_builtin(n - 2)

# ============================================================================
# Validation Decorator
# ============================================================================

print("\n--- Validation Decorator ---")

def validate_positive(*arg_names):
    """Decorator to validate arguments are positive"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameters
            import inspect
            sig = inspect.signature(func)
            params = sig.parameters
            
            # Check specified arguments
            for arg_name in arg_names:
                if arg_name in params:
                    param_index = list(params.keys()).index(arg_name)
                    if param_index < len(args):
                        if args[param_index] < 0:
                            raise ValueError(f"{arg_name} must be positive")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_positive('x', 'y')
def divide(x, y):
    return x / y

print(f"divide(10, 2) = {divide(10, 2)}")
try:
    divide(-10, 2)
except ValueError as e:
    print(f"Error: {e}")

# ============================================================================
# 6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
# ============================================================================

print("\n" + "="*80)
print("6. COMMON INTERVIEW QUESTIONS & SOLUTIONS")
print("="*80)

# ============================================================================
# Q1: Implement curry function
# ============================================================================

print("\n--- Q1: Curry Function ---")

def curry(func):
    """Convert function to curried version"""
    def curried(*args):
        if len(args) == func.__code__.co_argcount:
            return func(*args)
        return lambda arg: curried(*(args + (arg,)))
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

# Curried usage
result = add_three(1)(2)(3)
print(f"Curried add_three: {result}")

# ============================================================================
# Q2: Implement partial application
# ============================================================================

print("\n--- Q2: Partial Application ---")

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(f"double(5) = {double(5)}")

# Real-world: Data transformation pipeline
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

apply_10_percent_discount = partial(apply_discount, discount_percent=10)
print(f"Price with 10% discount: {apply_10_percent_discount(100)}")

# ============================================================================
# Q3: Chain operations
# ============================================================================

print("\n--- Q3: Chain Operations ---")

class Chain:
    """Chainable operations"""
    def __init__(self, value):
        self.value = value
    
    def add(self, n):
        self.value += n
        return self
    
    def multiply(self, n):
        self.value *= n
        return self
    
    def square(self):
        self.value = self.value ** 2
        return self
    
    def get(self):
        return self.value

result = Chain(5).add(3).multiply(2).square().get()
print(f"Chained operations: {result}")

# ============================================================================
# Q4: Filter and transform in single pass
# ============================================================================

print("\n--- Q4: Filter and Transform ---")

def filter_and_transform(items, predicate, transform):
    """Combine filter and transform efficiently"""
    return [transform(item) for item in items if predicate(item)]

numbers = range(1, 11)
result = filter_and_transform(
    numbers,
    predicate=lambda x: x % 2 == 0,  # Even numbers
    transform=lambda x: x ** 2  # Square them
)
print(f"Even numbers squared: {result}")

print("\n" + "="*80)
print("END OF FUNCTIONAL PROGRAMMING")
print("="*80)
