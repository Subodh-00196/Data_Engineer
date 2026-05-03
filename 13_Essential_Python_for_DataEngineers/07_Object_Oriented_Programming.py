"""
================================================================================
          OBJECT-ORIENTED PROGRAMMING FOR DATA ENGINEERS
================================================================================
Classes, inheritance, design patterns, and data-oriented design
Last Updated: May 2026
================================================================================

TABLE OF CONTENTS:
1. CLASSES AND OBJECTS
2. INHERITANCE AND POLYMORPHISM
3. ENCAPSULATION
4. DESIGN PATTERNS
5. DATA CLASSES
6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
================================================================================
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Dict, Any
from datetime import datetime
import json

print("="*80)
print("OBJECT-ORIENTED PROGRAMMING FOR DATA ENGINEERS")
print("="*80)

# ============================================================================
# 1. CLASSES AND OBJECTS
# ============================================================================

print("\n" + "="*80)
print("1. CLASSES AND OBJECTS")
print("="*80)

# ============================================================================
# Basic Class Definition
# ============================================================================

print("\n--- Basic Class Definition ---")

class Student:
    """Student class with attributes and methods"""
    
    # Class variable (shared by all instances)
    institution = "University"
    
    def __init__(self, name, age, marks):
        """Constructor to initialize student"""
        self.name = name
        self.age = age
        self.marks = marks
    
    def __str__(self):
        """String representation"""
        return f"Student({self.name}, {self.age}, {self.marks})"
    
    def __repr__(self):
        """Developer-friendly representation"""
        return f"Student(name='{self.name}', age={self.age}, marks={self.marks})"
    
    def get_grade(self):
        """Calculate student grade"""
        if self.marks >= 80:
            return 'A'
        elif self.marks >= 60:
            return 'B'
        else:
            return 'C'

# Create instances
student1 = Student("Alice", 20, 85)
student2 = Student("Bob", 21, 75)

print(f"Student 1: {student1}")
print(f"Student 2 repr: {repr(student2)}")
print(f"Alice's grade: {student1.get_grade()}")

# ============================================================================
# Properties and Methods
# ============================================================================

print("\n--- Properties and Methods ---")

class Employee:
    """Employee with property decorators"""
    
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        """Property getter"""
        return self._name
    
    @name.setter
    def name(self, value):
        """Property setter"""
        if not value or len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self._name = value
    
    @property
    def salary(self):
        """Read-only property"""
        return self._salary
    
    def give_raise(self, percent):
        """Calculate raise"""
        self._salary *= (1 + percent / 100)

emp = Employee("Alice", 50000)
print(f"Employee: {emp.name}, Salary: ${emp.salary:,.2f}")
emp.give_raise(10)
print(f"After 10% raise: ${emp.salary:,.2f}")

# ============================================================================
# Class Methods and Static Methods
# ============================================================================

print("\n--- Class Methods and Static Methods ---")

class DataProcessor:
    """Data processor with class and static methods"""
    
    total_processed = 0
    
    def __init__(self, name):
        self.name = name
    
    def process_data(self, count):
        """Instance method"""
        DataProcessor.total_processed += count
        print(f"{self.name} processed {count} records")
    
    @classmethod
    def from_file(cls, filename):
        """Class method - alternative constructor"""
        name = filename.replace('.txt', '')
        return cls(name)
    
    @classmethod
    def get_total_processed(cls):
        """Class method to access class variable"""
        return cls.total_processed
    
    @staticmethod
    def validate_file(filename):
        """Static method - doesn't need instance or class"""
        return filename.endswith('.txt')

# Use class method
processor = DataProcessor.from_file("data.txt")
processor.process_data(100)

print(f"Total processed: {DataProcessor.get_total_processed()}")
print(f"Valid file: {DataProcessor.validate_file('data.txt')}")

# ============================================================================
# 2. INHERITANCE AND POLYMORPHISM
# ============================================================================

print("\n" + "="*80)
print("2. INHERITANCE AND POLYMORPHISM")
print("="*80)

# ============================================================================
# Single Inheritance
# ============================================================================

print("\n--- Single Inheritance ---")

class Person:
    """Base class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def describe(self):
        return f"{self.name}, {self.age} years old"

class DataEngineer(Person):
    """Derived class"""
    def __init__(self, name, age, programming_languages):
        super().__init__(name, age)
        self.programming_languages = programming_languages
    
    def describe(self):
        """Override method"""
        base_desc = super().describe()
        return f"{base_desc}, Skills: {', '.join(self.programming_languages)}"

engineer = DataEngineer("Alice", 28, ["Python", "SQL", "Scala"])
print(f"Engineer: {engineer.describe()}")

# ============================================================================
# Multiple Inheritance
# ============================================================================

print("\n--- Multiple Inheritance ---")

class Writer:
    def write(self):
        return "Writing documentation"

class Coder:
    def code(self):
        return "Writing code"

class TechnicalWriter(Writer, Coder):
    """Inherits from both Writer and Coder"""
    pass

tech_writer = TechnicalWriter()
print(f"Tech writer can: {tech_writer.write()}")
print(f"Tech writer can: {tech_writer.code()}")

# Method Resolution Order (MRO)
print(f"MRO: {TechnicalWriter.__mro__}")

# ============================================================================
# Abstract Base Classes
# ============================================================================

print("\n--- Abstract Base Classes ---")

class DataSource(ABC):
    """Abstract base class for data sources"""
    
    @abstractmethod
    def connect(self):
        """Connect to data source"""
        pass
    
    @abstractmethod
    def read_data(self):
        """Read data from source"""
        pass
    
    def validate(self):
        """Concrete method"""
        return True

class CSVDataSource(DataSource):
    """CSV data source implementation"""
    def connect(self):
        print("Connecting to CSV file")
    
    def read_data(self):
        print("Reading data from CSV")
        return ["row1", "row2"]

class DatabaseDataSource(DataSource):
    """Database data source implementation"""
    def connect(self):
        print("Connecting to database")
    
    def read_data(self):
        print("Reading data from database")
        return ["record1", "record2"]

# Can't instantiate abstract class
# source = DataSource()  # TypeError

# Can instantiate concrete implementations
csv_source = CSVDataSource()
csv_source.connect()
csv_source.read_data()

# ============================================================================
# 3. ENCAPSULATION
# ============================================================================

print("\n" + "="*80)
print("3. ENCAPSULATION")
print("="*80)

# ============================================================================
# Access Control
# ============================================================================

print("\n--- Access Control ---")

class BankAccount:
    """Bank account with access control"""
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private
        self._pin = "1234"  # Protected
    
    def get_balance(self):
        """Controlled access to balance"""
        return self.__balance
    
    def deposit(self, amount):
        """Public method to modify balance"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            raise ValueError("Amount must be positive")
    
    def withdraw(self, amount):
        """Public method with validation"""
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrawn: ${amount}")

account = BankAccount("123456", 1000)
print(f"Balance: ${account.get_balance()}")
account.deposit(500)
print(f"Balance after deposit: ${account.get_balance()}")

# Can't access private attribute directly
# print(account.__balance)  # AttributeError

# ============================================================================
# 4. DESIGN PATTERNS
# ============================================================================

print("\n" + "="*80)
print("4. DESIGN PATTERNS")
print("="*80)

# ============================================================================
# Singleton Pattern
# ============================================================================

print("\n--- Singleton Pattern ---")

class DatabaseConnection:
    """Singleton database connection"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance
    
    def connect(self):
        if not self.connected:
            print("Connecting to database...")
            self.connected = True

# Only one instance
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance: {db1 is db2}")
db1.connect()
db2.connect()  # Won't connect again

# ============================================================================
# Factory Pattern
# ============================================================================

print("\n--- Factory Pattern ---")

class DataFormat(Enum):
    CSV = "csv"
    JSON = "json"
    PARQUET = "parquet"

class DataReader:
    """Factory for creating data readers"""
    
    @staticmethod
    def create_reader(format_type):
        """Factory method"""
        if format_type == DataFormat.CSV:
            return CSVReader()
        elif format_type == DataFormat.JSON:
            return JSONReader()
        elif format_type == DataFormat.PARQUET:
            return ParquetReader()
        else:
            raise ValueError(f"Unknown format: {format_type}")

class CSVReader:
    def read(self, filename):
        return f"Reading CSV: {filename}"

class JSONReader:
    def read(self, filename):
        return f"Reading JSON: {filename}"

class ParquetReader:
    def read(self, filename):
        return f"Reading Parquet: {filename}"

# Use factory
reader = DataReader.create_reader(DataFormat.CSV)
print(reader.read("data.csv"))

# ============================================================================
# 5. DATA CLASSES
# ============================================================================

print("\n" + "="*80)
print("5. DATA CLASSES")
print("="*80)

# ============================================================================
# Basic Data Class
# ============================================================================

print("\n--- Data Class ---")

@dataclass
class Record:
    """Simple data class"""
    id: int
    name: str
    value: float
    
    def display(self):
        return f"Record {self.id}: {self.name} = {self.value}"

record = Record(1, "Item A", 100.50)
print(record)
print(record.display())

# ============================================================================
# Data Class with Default Values
# ============================================================================

print("\n--- Data Class with Defaults ---")

@dataclass
class Configuration:
    """Configuration with default values"""
    host: str
    port: int = 5432
    timeout: int = 30
    retry_count: int = 3
    enabled: bool = True

config = Configuration("localhost")
print(config)

# ============================================================================
# Data Class with Field Configuration
# ============================================================================

print("\n--- Data Class with Field Configuration ---")

@dataclass
class DataPipeline:
    """Data pipeline configuration"""
    name: str
    source: str
    destination: str
    records_processed: int = field(default=0, init=False)
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    
    def process(self, count):
        self.records_processed += count

pipeline = DataPipeline(
    name="ETL Pipeline",
    source="S3",
    destination="Snowflake",
    tags=["production", "daily"]
)
print(pipeline)
pipeline.process(1000)
print(f"Records processed: {pipeline.records_processed}")

# ============================================================================
# 6. COMMON INTERVIEW QUESTIONS & SOLUTIONS
# ============================================================================

print("\n" + "="*80)
print("6. COMMON INTERVIEW QUESTIONS & SOLUTIONS")
print("="*80)

# ============================================================================
# Q1: Design a caching layer
# ============================================================================

print("\n--- Q1: Caching Layer ---")

class CacheLayer:
    """Simple caching layer"""
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {}
        self.access_count = {}
    
    def get(self, key):
        if key in self.cache:
            self.access_count[key] += 1
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if len(self.cache) >= self.max_size:
            # Evict least accessed key
            lru_key = min(self.access_count, key=self.access_count.get)
            del self.cache[lru_key]
            del self.access_count[lru_key]
        
        self.cache[key] = value
        self.access_count[key] = 0
    
    def size(self):
        return len(self.cache)

cache = CacheLayer(max_size=3)
cache.put("key1", "value1")
cache.put("key2", "value2")
print(f"Cache size: {cache.size()}")
print(f"Get key1: {cache.get('key1')}")

# ============================================================================
# Q2: Design a data validator
# ============================================================================

print("\n--- Q2: Data Validator ---")

class Validator(ABC):
    """Abstract validator"""
    @abstractmethod
    def validate(self, value):
        pass

class TypeValidator(Validator):
    """Validate data type"""
    def __init__(self, expected_type):
        self.expected_type = expected_type
    
    def validate(self, value):
        return isinstance(value, self.expected_type)

class RangeValidator(Validator):
    """Validate value range"""
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
    
    def validate(self, value):
        return self.min_val <= value <= self.max_val

class CompositeValidator:
    """Composite validator combining multiple validators"""
    def __init__(self):
        self.validators = []
    
    def add_validator(self, validator):
        self.validators.append(validator)
        return self
    
    def validate(self, value):
        return all(v.validate(value) for v in self.validators)

# Use validators
validator = CompositeValidator()
validator.add_validator(TypeValidator(int))
validator.add_validator(RangeValidator(0, 100))

print(f"Validate 50: {validator.validate(50)}")
print(f"Validate 150: {validator.validate(150)}")
print(f"Validate 'string': {validator.validate('string')}")

# ============================================================================
# Q3: Design a data transformation pipeline
# ============================================================================

print("\n--- Q3: Data Transformation Pipeline ---")

@dataclass
class Transform:
    """Represents a transformation step"""
    name: str
    func: callable

class TransformationPipeline:
    """Pipeline to chain transformations"""
    def __init__(self):
        self.transforms = []
    
    def add_transform(self, name, func):
        self.transforms.append(Transform(name, func))
        return self
    
    def execute(self, data):
        result = data
        for transform in self.transforms:
            result = transform.func(result)
            print(f"After {transform.name}: {result}")
        return result

# Build pipeline
pipeline = TransformationPipeline()
pipeline.add_transform("Parse", lambda x: json.loads(x))
pipeline.add_transform("Extract", lambda x: x.get('value'))
pipeline.add_transform("Multiply", lambda x: x * 2)

data = '{"value": 10}'
result = pipeline.execute(data)
print(f"Final result: {result}")

print("\n" + "="*80)
print("END OF OBJECT-ORIENTED PROGRAMMING")
print("="*80)
