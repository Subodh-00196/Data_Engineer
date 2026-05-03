"""
================================================================================
                    REGULAR EXPRESSIONS FOR DATA ENGINEERS
================================================================================
Pattern matching, validation, and text processing essentials
Last Updated: May 2026
================================================================================

TABLE OF CONTENTS:
1. REGEX BASICS & PATTERNS
2. MATCHING AND SEARCHING
3. GROUPING AND EXTRACTION
4. REPLACEMENT AND SUBSTITUTION
5. DATA VALIDATION PATTERNS
6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
================================================================================
"""

import re
from typing import List, Dict, Optional, Pattern, Match
import json

print("="*80)
print("REGULAR EXPRESSIONS FOR DATA ENGINEERS")
print("="*80)

# ============================================================================
# 1. REGEX BASICS & PATTERNS
# ============================================================================

print("\n" + "="*80)
print("1. REGEX BASICS & PATTERNS")
print("="*80)

# ============================================================================
# Basic Pattern Symbols
# ============================================================================

print("\n--- Basic Pattern Symbols ---")

patterns_info = {
    ".": "Matches any single character except newline",
    "*": "Matches 0 or more of the preceding element",
    "+": "Matches 1 or more of the preceding element",
    "?": "Matches 0 or 1 of the preceding element",
    "^": "Matches the start of string",
    "$": "Matches the end of string",
    "[]": "Character class - matches any character inside",
    "[^]": "Negated character class",
    "()": "Grouping - captures the matched text",
    "|": "Alternation - matches either pattern",
    "\\": "Escape character",
}

for pattern, description in patterns_info.items():
    print(f"  {pattern:10} -> {description}")

# ============================================================================
# Character Classes
# ============================================================================

print("\n--- Character Classes ---")

# \d = digit
print(f"\\d (digit):        {re.findall(r'\\d', 'a1b2c3')}")

# \D = non-digit
print(f"\\D (non-digit):    {re.findall(r'\\D', 'a1b2c3')}")

# \w = word character (alphanumeric + underscore)
print(f"\\w (word char):    {re.findall(r'\\w', 'hello_123')}")

# \W = non-word character
print(f"\\W (non-word):     {re.findall(r'\\W', 'hello-123')}")

# \s = whitespace
print(f"\\s (whitespace):   {re.findall(r'\\s', 'hello world\\t123')}")

# \S = non-whitespace
print(f"\\S (non-whitespace): {re.findall(r'\\S', 'hello world')}")

# ============================================================================
# Quantifiers
# ============================================================================

print("\n--- Quantifiers ---")

text = "aaa bb cccc"
print(f"Text: '{text}'")
print(f"a{{3}} (exactly 3):  {re.findall(r'a{3}', text)}")
print(f"b{{2,}} (2+):        {re.findall(r'b{2,}', text)}")
print(f"c{{2,3}} (2-3):      {re.findall(r'c{2,3}', text)}")

# Greedy vs Non-greedy
text = "<tag>content</tag>"
print(f"\nText: '{text}'")
print(f"<.*> (greedy):     {re.findall(r'<.*>', text)}")
print(f"<.*?> (non-greedy): {re.findall(r'<.*?>', text)}")

# ============================================================================
# 2. MATCHING AND SEARCHING
# ============================================================================

print("\n" + "="*80)
print("2. MATCHING AND SEARCHING")
print("="*80)

# ============================================================================
# re.match() - Match at beginning of string
# ============================================================================

print("\n--- re.match() ---")

pattern = r"^\d{3}-\d{3}-\d{4}$"  # Phone number format
phone1 = "123-456-7890"
phone2 = "abc-456-7890"

match1 = re.match(pattern, phone1)
match2 = re.match(pattern, phone2)

print(f"Phone pattern: {pattern}")
print(f"'{phone1}' matches: {bool(match1)}")
print(f"'{phone2}' matches: {bool(match2)}")

# ============================================================================
# re.search() - Search anywhere in string
# ============================================================================

print("\n--- re.search() ---")

text = "Contact: 123-456-7890"
pattern = r"\d{3}-\d{3}-\d{4}"

result = re.search(pattern, text)
if result:
    print(f"Found: {result.group()}")
    print(f"Position: {result.span()}")

# ============================================================================
# re.findall() - Find all matches
# ============================================================================

print("\n--- re.findall() ---")

text = "Email: user1@example.com, user2@test.org, user3@mail.co.uk"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(email_pattern, text)
print(f"Emails found: {emails}")

# ============================================================================
# re.finditer() - Find all matches with iterator
# ============================================================================

print("\n--- re.finditer() ---")

text = "Prices: $10.50, $20.00, $5.99"
pattern = r"\$\d+\.\d{2}"

for match in re.finditer(pattern, text):
    print(f"Found: {match.group()} at position {match.span()}")

# ============================================================================
# 3. GROUPING AND EXTRACTION
# ============================================================================

print("\n" + "="*80)
print("3. GROUPING AND EXTRACTION")
print("="*80)

# ============================================================================
# Capturing Groups
# ============================================================================

print("\n--- Capturing Groups ---")

# Extract name and age
pattern = r"(\w+)\s+(\d+)\s+years\s+old"
text = "Alice 25 years old Bob 30 years old"

matches = re.findall(pattern, text)
print(f"Matches: {matches}")

# Using groups() to get all groups
pattern = r"(\w+),\s*(\d+),\s*(\w+)"
text = "Alice, 25, Engineer"

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")
    print(f"Group 1: {match.group(1)}")
    print(f"Group 2: {match.group(2)}")
    print(f"Group 3: {match.group(3)}")
    print(f"All groups: {match.groups()}")

# ============================================================================
# Named Groups
# ============================================================================

print("\n--- Named Groups ---")

# Named groups for clarity
pattern = r"(?P<name>\w+),\s*(?P<age>\d+),\s*(?P<job>\w+)"
text = "Alice, 25, Engineer"

match = re.search(pattern, text)
if match:
    print(f"Name: {match.group('name')}")
    print(f"Age: {match.group('age')}")
    print(f"Job: {match.group('job')}")
    print(f"As dictionary: {match.groupdict()}")

# Real-world: Parse log entries
log_pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2})\s+(?P<level>\w+)\s+(?P<message>.*)"
log_entry = "2026-05-03 ERROR Database connection failed"

log_match = re.search(log_pattern, log_entry)
if log_match:
    print(f"Parsed log: {log_match.groupdict()}")

# ============================================================================
# Non-capturing Groups
# ============================================================================

print("\n--- Non-capturing Groups ---")

# (?:...) creates a group but doesn't capture
pattern = r"(?:Mr|Ms|Dr)\.\s+(\w+)"
text = "Mr. Smith and Dr. Johnson"

matches = re.findall(pattern, text)
print(f"Names only: {matches}")

# ============================================================================
# 4. REPLACEMENT AND SUBSTITUTION
# ============================================================================

print("\n" + "="*80)
print("4. REPLACEMENT AND SUBSTITUTION")
print("="*80)

# ============================================================================
# re.sub() - Replace matches
# ============================================================================

print("\n--- re.sub() ---")

# Simple replacement
text = "The year is 2025, 2026, and 2027"
result = re.sub(r"\d{4}", "YEAR", text)
print(f"Original: {text}")
print(f"After sub: {result}")

# Replacement with groups
text = "John (john@example.com) and Jane (jane@example.com)"
result = re.sub(r"(\w+)\s+\(([^)]+)\)", r"\1 - \2", text)
print(f"\nOriginal: {text}")
print(f"After sub: {result}")

# ============================================================================
# re.sub() with function
# ============================================================================

print("\n--- re.sub() with Function ---")

def double_number(match):
    """Function to double matched numbers"""
    num = int(match.group())
    return str(num * 2)

text = "Numbers: 10, 20, 30"
result = re.sub(r"\d+", double_number, text)
print(f"Original: {text}")
print(f"After sub: {result}")

# Real-world: Mask sensitive data
def mask_email(match):
    """Mask email addresses"""
    email = match.group()
    name, domain = email.split('@')
    return f"***@{domain}"

text = "Contact: user1@example.com or user2@test.org"
result = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", mask_email, text)
print(f"\nOriginal: {text}")
print(f"Masked: {result}")

# ============================================================================
# re.subn() - Replace and count
# ============================================================================

print("\n--- re.subn() ---")

text = "apple, apple, banana, apple"
result, count = re.subn(r"apple", "orange", text)
print(f"Original: {text}")
print(f"After sub: {result}")
print(f"Replacements made: {count}")

# ============================================================================
# 5. DATA VALIDATION PATTERNS
# ============================================================================

print("\n" + "="*80)
print("5. DATA VALIDATION PATTERNS")
print("="*80)

# ============================================================================
# Common Validation Patterns
# ============================================================================

print("\n--- Common Validation Patterns ---")

validation_patterns = {
    "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
    "phone_us": r"^(\+1)?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$",
    "url": r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "ipv4": r"^(\d{1,3}\.){3}\d{1,3}$",
    "zipcode_us": r"^\d{5}(?:-\d{4})?$",
    "date_yyyy_mm_dd": r"^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$",
    "time_hh_mm_ss": r"^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$",
    "hex_color": r"^#(?:[0-9a-fA-F]{3}){1,2}$",
}

test_data = {
    "email": ["user@example.com", "invalid.email@.com"],
    "phone_us": ["123-456-7890", "555-123-4567"],
    "url": ["https://example.com", "http://test.org"],
    "ipv4": ["192.168.1.1", "256.1.1.1"],
    "zipcode_us": ["12345", "12345-6789"],
    "date_yyyy_mm_dd": ["2026-05-03", "2026-13-45"],
    "time_hh_mm_ss": ["14:30:45", "25:60:60"],
    "hex_color": ["#FF5733", "#fff"],
}

for pattern_name, test_values in test_data.items():
    pattern = validation_patterns[pattern_name]
    print(f"\n{pattern_name}:")
    for value in test_values:
        is_valid = bool(re.match(pattern, value))
        print(f"  '{value}' -> {is_valid}")

# ============================================================================
# Validator Classes
# ============================================================================

print("\n--- Validator Classes ---")

class DataValidator:
    """Reusable data validator using regex"""
    
    patterns = {
        "email": r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",
        "phone": r"^\+?1?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$",
        "url": r"^https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    }
    
    @classmethod
    def validate_email(cls, email):
        """Validate email format"""
        return bool(re.match(cls.patterns["email"], email))
    
    @classmethod
    def validate_phone(cls, phone):
        """Validate phone number"""
        return bool(re.match(cls.patterns["phone"], phone))
    
    @classmethod
    def validate_url(cls, url):
        """Validate URL format"""
        return bool(re.match(cls.patterns["url"], url))
    
    @classmethod
    def validate_batch(cls, data, field, validator_method):
        """Validate batch of data"""
        results = []
        for item in data:
            is_valid = validator_method(item[field])
            results.append({
                'value': item[field],
                'valid': is_valid
            })
        return results

# Use validator
print("Email validation:")
print(f"  'user@example.com' -> {DataValidator.validate_email('user@example.com')}")
print(f"  'invalid.email' -> {DataValidator.validate_email('invalid.email')}")

# ============================================================================
# 6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
# ============================================================================

print("\n" + "="*80)
print("6. COMMON INTERVIEW QUESTIONS & SOLUTIONS")
print("="*80)

# ============================================================================
# Q1: Extract all numbers from text
# ============================================================================

print("\n--- Q1: Extract All Numbers ---")

def extract_numbers(text):
    """Extract all numbers from text"""
    return [int(x) for x in re.findall(r'-?\d+', text)]

text = "The values are -10, 25, and 100 degrees"
numbers = extract_numbers(text)
print(f"Text: {text}")
print(f"Numbers: {numbers}")

# ============================================================================
# Q2: Validate and parse CSV data
# ============================================================================

print("\n--- Q2: Validate and Parse CSV Data ---")

def validate_csv_row(row, schema):
    """Validate CSV row against schema"""
    fields = row.split(',')
    if len(fields) != len(schema):
        return False, "Field count mismatch"
    
    for value, field_type in zip(fields, schema):
        if field_type == 'email':
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", value):
                return False, f"Invalid email: {value}"
        elif field_type == 'int':
            if not re.match(r"^-?\d+$", value):
                return False, f"Invalid integer: {value}"
        elif field_type == 'float':
            if not re.match(r"^-?\d+\.?\d*$", value):
                return False, f"Invalid float: {value}"
    
    return True, "Valid"

# Test data
schema = ['name', 'email', 'age']
csv_data = [
    "Alice,alice@example.com,25",
    "Bob,invalid-email,30",
    "Charlie,charlie@example.com,35",
]

for row in csv_data:
    is_valid, message = validate_csv_row(row, schema)
    print(f"'{row}' -> {is_valid} ({message})")

# ============================================================================
# Q3: Extract structured data from unstructured text
# ============================================================================

print("\n--- Q3: Extract Structured Data from Unstructured Text ---")

def parse_log_entry(log_line):
    """Parse structured data from log entry"""
    pattern = r"\[(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\]\s+\[(?P<level>\w+)\]\s+(?P<component>\w+):\s+(?P<message>.*)"
    
    match = re.search(pattern, log_line)
    if match:
        return match.groupdict()
    return None

log_entries = [
    "[2026-05-03 14:30:45] [ERROR] Database: Connection timeout",
    "[2026-05-03 14:30:46] [INFO] API: Request processed",
]

for entry in log_entries:
    parsed = parse_log_entry(entry)
    if parsed:
        print(f"Parsed: {parsed}")

# ============================================================================
# Q4: Clean and standardize phone numbers
# ============================================================================

print("\n--- Q4: Clean and Standardize Phone Numbers ---")

def standardize_phone(phone):
    """Standardize phone number to (XXX) XXX-XXXX format"""
    # Remove all non-digits
    digits = re.sub(r'\D', '', phone)
    
    # Handle US phone numbers
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    elif len(digits) == 11 and digits[0] == '1':
        return f"({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
    else:
        return None

phone_numbers = [
    "123-456-7890",
    "(123) 456-7890",
    "1-123-456-7890",
    "123.456.7890",
]

for phone in phone_numbers:
    standardized = standardize_phone(phone)
    print(f"'{phone}' -> '{standardized}'")

# ============================================================================
# Q5: Split text by multiple delimiters
# ============================================================================

print("\n--- Q5: Split by Multiple Delimiters ---")

def split_by_multiple_delimiters(text, delimiters=None):
    """Split text by multiple delimiters"""
    if delimiters is None:
        delimiters = [',', ';', '|', '\t']
    
    pattern = '|'.join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)

text = "apple,banana;orange|grape\tblueberry"
result = split_by_multiple_delimiters(text)
print(f"Text: {text}")
print(f"Split result: {result}")

# ============================================================================
# Q6: Find and remove duplicate words
# ============================================================================

print("\n--- Q6: Remove Duplicate Words ---")

def remove_duplicate_words(text):
    """Remove duplicate consecutive words"""
    return re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', text, flags=re.IGNORECASE)

text = "The the quick quick brown fox fox jumps"
result = remove_duplicate_words(text)
print(f"Original: {text}")
print(f"Cleaned: {result}")

print("\n" + "="*80)
print("END OF REGULAR EXPRESSIONS")
print("="*80)
