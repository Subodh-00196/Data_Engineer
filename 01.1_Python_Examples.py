"""
================================================================================
                    PYTHON - DATA ENGINEER INTERVIEW GUIDE
================================================================================
Comprehensive Python examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. STRING MANIPULATION
2. DATA STRUCTURES (LIST, DICT, SET, TUPLE)
3. FUNCTIONAL PROGRAMMING (MAP, FILTER, REDUCE, LAMBDA)
4. SORTING & SEARCHING ALGORITHMS
5. RECURSION
6. ITERATORS & GENERATORS
7. FILE HANDLING & I/O
8. REGULAR EXPRESSIONS
9. DATE & TIME OPERATIONS
10. ERROR HANDLING & EXCEPTIONS
11. OBJECT-ORIENTED PROGRAMMING
12. COMMON INTERVIEW PROBLEMS
13. AWS BOTO3 BASICS
================================================================================
"""

# ============================================================================
# 1. STRING MANIPULATION
# ============================================================================

""" Reverse a String """
# Method 1: Using slicing
original_string = "hello"
reversed_string = original_string[::-1]
print(reversed_string)  # Output: "olleh"

# Method 2: Using loop
reversed_string = ""
for char in original_string:
    reversed_string = char + reversed_string

# Method 3: Using reversed()
reversed_string = ''.join(reversed(original_string))

""" Check if String is Palindrome """
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama"))  # True

""" Count Character Occurrences """
# Method 1: Using dictionary
text = "GeeksforGeeks"
char_count = {}
for c in text:
    char_count[c] = char_count.get(c, 0) + 1

# Method 2: Using Counter
from collections import Counter
char_count = Counter(text)

# Find max and min occurrence
max_char = max(char_count, key=char_count.get)
min_char = min(char_count, key=char_count.get)

""" Find Duplicate Words """
def find_duplicate_words(sentence):
    words = sentence.split()
    word_counts = {}
    
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    duplicates = [word for word, count in word_counts.items() if count > 1]
    return duplicates

sentence = "this is a test sentence with duplicate words this is a test"
print(find_duplicate_words(sentence))

""" Remove Duplicates from String """
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

""" Anagram Check """
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(are_anagrams("listen", "silent"))  # True

""" String Compression """
def compress_string(s):
    if not s:
        return s
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    compressed = ''.join(result)
    
    return compressed if len(compressed) < len(s) else s

print(compress_string("aabcccccaaa"))  # a2b1c5a3

# ============================================================================
# 2. DATA STRUCTURES (LIST, DICT, SET, TUPLE)
# ============================================================================

""" List Operations """
# Create list
my_list = [1, 2, 3, 4, 5]

# Append, Insert, Remove
my_list.append(6)
my_list.insert(0, 0)
my_list.remove(3)
my_list.pop()
my_list.pop(0)

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]

""" Dictionary Operations """
# Create dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Get value with default
value = my_dict.get('d', 0)

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}

# Merge dictionaries (Python 3.9+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2

# Sort dictionary by key
sorted_dict = dict(sorted(my_dict.items()))

# Sort dictionary by value
sorted_by_value = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# Group by key
from itertools import groupby
data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped = {k: [v for _, v in g] for k, g in groupby(sorted(data), key=lambda x: x[0])}

""" Set Operations """
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union = set1 | set2
union = set1.union(set2)

# Intersection
intersection = set1 & set2
intersection = set1.intersection(set2)

# Difference
difference = set1 - set2
difference = set1.difference(set2)

# Symmetric difference
sym_diff = set1 ^ set2

""" Find Missing Number in Array """
def find_missing(arr, n):
    # Expected sum of 1 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing([1, 2, 4, 5], 5))  # 3

""" Two Sum Problem """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# ============================================================================
# 3. FUNCTIONAL PROGRAMMING
# ============================================================================

""" Map - Apply function to all items """
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))

""" Filter - Filter items based on condition """
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

""" Reduce - Reduce to single value """
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum using reduce
maximum = reduce(lambda x, y: x if x > y else y, numbers)

""" Lambda Functions """
# Sort by custom key
students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

# Filter and map combined
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))

""" Zip Function """
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 75, 90]
combined = list(zip(names, scores))
# [('Alice', 85), ('Bob', 75), ('Charlie', 90)]

# Unzip
names, scores = zip(*combined)

""" All and Any """
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)  # True
any_odd = any(x % 2 != 0 for x in numbers)   # False

# ============================================================================
# 4. SORTING & SEARCHING ALGORITHMS
# ============================================================================

""" Bubble Sort """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

""" Merge Sort (Recursive) """
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

""" Quick Sort """
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

""" Binary Search """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

""" Find Second Largest Element """
def second_largest(arr):
    if len(arr) < 2:
        return None
    
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second if second != float('-inf') else None

# ============================================================================
# 5. RECURSION
# ============================================================================

""" Factorial """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

""" Fibonacci """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fibonacci with memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

""" Reverse List Recursively """
def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return reverse_list(lst[1:]) + [lst[0]]

""" Sum of Digits """
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

""" Tower of Hanoi """
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# ============================================================================
# 6. ITERATORS & GENERATORS
# ============================================================================

""" Custom Iterator """
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration

# Usage
for num in MyIterator(1, 5):
    print(num)

""" Generator Function """
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

""" Generator Expression """
squares_gen = (x**2 for x in range(10))

""" Read Large File with Generator """
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# ============================================================================
# 7. FILE HANDLING & I/O
# ============================================================================

""" Read File """
# Method 1: Read entire file
with open('file.txt', 'r') as f:
    content = f.read()

# Method 2: Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Method 3: Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()

""" Write File """
with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")

# Append to file
with open('output.txt', 'a') as f:
    f.write("New line\n")

""" CSV Operations """
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])

# Write CSV
data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

""" JSON Operations """
import json

# Read JSON
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON
data = {'name': 'Alice', 'age': 25}
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)

# ============================================================================
# 8. REGULAR EXPRESSIONS
# ============================================================================

import re

""" Pattern Matching """
text = "My phone number is 123-456-7890"

# Find all digits
digits = re.findall(r'\d+', text)

# Replace digits with asterisks
masked = re.sub(r'\d', '*', text)

# Match email pattern
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
is_valid_email = bool(re.match(email_pattern, "user@example.com"))

# Extract groups
phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(phone_pattern, text)
if match:
    area_code = match.group(1)

# Split by pattern
parts = re.split(r'[,\s]+', "apple, banana orange")

# ============================================================================
# 9. DATE & TIME OPERATIONS
# ============================================================================

from datetime import datetime, timedelta, date

""" Current Date and Time """
now = datetime.now()
today = date.today()

""" Format Date """
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
formatted = now.strftime('%B %d, %Y')  # January 01, 2024

""" Parse Date String """
date_str = "2024-01-15"
parsed_date = datetime.strptime(date_str, '%Y-%m-%d')

""" Date Arithmetic """
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
next_month = today + timedelta(days=30)

""" Calculate Date Difference """
date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)
difference = date2 - date1
print(f"Days: {difference.days}")

""" Calculate Average Time """
def parse_time(time_str):
    try:
        return datetime.strptime(time_str, '%H:%M:%S')
    except ValueError:
        return datetime.strptime(time_str, '%H:%M:%S.%f')

def calculate_average_time(times):
    total_seconds = sum(t.hour * 3600 + t.minute * 60 + t.second + t.microsecond / 1e6 for t in times)
    average_seconds = total_seconds / len(times)
    hours = int(average_seconds // 3600)
    minutes = int((average_seconds % 3600) // 60)
    seconds = average_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:05.2f}"

# ============================================================================
# 10. ERROR HANDLING & EXCEPTIONS
# ============================================================================

""" Try-Except Block """
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No errors occurred")
finally:
    print("This always executes")

""" Custom Exception """
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 0 and 120"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    return True

""" Context Manager """
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage
with FileManager('test.txt', 'w') as f:
    f.write('Hello')

# ============================================================================
# 11. OBJECT-ORIENTED PROGRAMMING
# ============================================================================

""" Class Definition """
class Employee:
    # Class variable
    company = "TechCorp"
    
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"{self.name} earns ${self.salary}"
    
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))
    
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

""" Inheritance """
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def get_details(self):
        return f"{self.name} manages {self.department}"

""" Property Decorator """
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

# ============================================================================
# 12. COMMON INTERVIEW PROBLEMS
# ============================================================================

""" FizzBuzz """
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

""" Find Pairs with Given Sum """
def find_pairs(numbers, target_sum):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))
    return pairs

# Optimized version using hash set
def find_pairs_optimized(numbers, target_sum):
    seen = set()
    pairs = []
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

""" Longest Substring Without Repeating Characters """
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

""" Valid Parentheses """
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

""" Candy Problem (Wrapper Exchange) """
def max_candies(amount):
    candies = amount
    wrappers = amount
    
    while wrappers >= 3:
        additional_candies = wrappers // 3
        candies += additional_candies
        wrappers = wrappers % 3 + additional_candies
    
    return candies

""" Word Pattern Matching """
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

""" Group Anagrams """
def group_anagrams(words):
    from collections import defaultdict
    anagram_groups = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    return list(anagram_groups.values())

# ============================================================================
# 13. AWS BOTO3 BASICS
# ============================================================================

""" S3 Operations """
import boto3

# Create S3 client
s3_client = boto3.client('s3')

# List buckets
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# List objects in bucket
response = s3_client.list_objects_v2(Bucket='my-bucket', Prefix='path/')
for obj in response.get('Contents', []):
    print(obj['Key'])

# Upload file
s3_client.upload_file('local_file.txt', 'my-bucket', 'remote_file.txt')

# Download file
s3_client.download_file('my-bucket', 'remote_file.txt', 'local_file.txt')

# Delete object
s3_client.delete_object(Bucket='my-bucket', Key='file.txt')

# Put object
s3_client.put_object(Bucket='my-bucket', Key='new_file.txt', Body='Hello, World!')

""" Secrets Manager """
secrets_client = boto3.client('secretsmanager')

# Create secret
response = secrets_client.create_secret(
    Name='my-secret',
    SecretString='my-secret-value'
)

# Get secret
response = secrets_client.get_secret_value(SecretId='my-secret')
secret = response['SecretString']

""" Token Vault Example """
import random
import string

def create_token(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_token_vault(sensitive_data):
    token_vault = {}
    for data in sensitive_data:
        token = create_token()
        token_vault[token] = data
    return token_vault

def detokenize(token, token_vault):
    return token_vault.get(token, "Token not found")

# ============================================================================
# END OF PYTHON INTERVIEW GUIDE
# ============================================================================
