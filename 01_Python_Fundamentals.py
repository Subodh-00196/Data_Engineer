# Python for Data Engineers – The Complete Interview Handbook

A standalone guide that takes you from Python basics to advanced, production-grade Data Engineering. It is written for **learning, revision, coding practice, and interview preparation**.

**Version baseline:** Python **3.10+**. Where a feature needs a newer version (or did not exist in older ones), the guide says so.

---

## How to Use This Guide

| If you want to… | Read |
|---|---|
| Learn Python from scratch | Chapters 1 → 7 in order |
| Prepare for Data Engineer coding rounds | Chapters 2, 3, 6, 20 |
| Prepare for design and scenario rounds | Chapters 13, 14, 15, 19, 21 |
| Revise the night before an interview | The **Chapter Review** at the end of every chapter, then Chapter 22 |

**Conventions used in this guide**

- Code blocks marked `python` are valid Python 3. Most can be run as-is. Examples that need a third-party package (pandas, NumPy, requests, pytest, a database driver) say so in a comment at the top.
- An **Output:** block shows the exact text the preceding example prints.
- **Educational** examples keep things short to explain an idea. **Production-style** examples (labelled as such) add type hints, logging, error handling and resource cleanup.
- "Representative interview question" means a question typical of Data Engineer interviews. It is not a claim about any specific company.

---

## Table of Contents

- [1. Python Foundations](#1-python-foundations)
  - [1.1 Python Features and Use Cases in Data Engineering](#11-python-features-and-use-cases-in-data-engineering)
  - [1.2 Python Execution Model](#12-python-execution-model)
  - [1.3 Interpreted versus Compiled Behaviour](#13-interpreted-versus-compiled-behaviour)
  - [1.4 Installation, Virtual Environments, pip and Dependency Management](#14-installation-virtual-environments-pip-and-dependency-management)
  - [1.5 Variables, Identifiers, Keywords, Indentation, Comments and Naming](#15-variables-identifiers-keywords-indentation-comments-and-naming)
  - [1.6 Mutable versus Immutable Objects](#16-mutable-versus-immutable-objects)
  - [1.7 Dynamic Typing and Strong Typing](#17-dynamic-typing-and-strong-typing)
  - [1.8 Object Identity, Value Equality and References](#18-object-identity-value-equality-and-references)
  - [1.9 id(), type(), isinstance(), == and is](#19-id-type-isinstance--and-is)
  - [1.10 Truthy and Falsy Values](#110-truthy-and-falsy-values)
  - [1.11 Input and Output](#111-input-and-output)
  - [1.12 Operators and Operator Precedence](#112-operators-and-operator-precedence)
  - [1.13 Type Conversion and Type Checking](#113-type-conversion-and-type-checking)
  - [Chapter 1 Review](#chapter-1-review)
- [2. Built-in Data Types](#2-built-in-data-types)
  - [2.1 Scalar Types: int, float, complex, bool and None](#21-scalar-types-int-float-complex-bool-and-none)
  - [2.2 Sequence and Binary Types: str, bytes, bytearray and range](#22-sequence-and-binary-types-str-bytes-bytearray-and-range)
  - [2.3 Lists](#23-lists)
  - [2.4 Tuples](#24-tuples)
  - [2.5 Sets and Frozensets](#25-sets-and-frozensets)
  - [2.6 Dictionaries](#26-dictionaries)
  - [2.7 Comparing list, tuple, set and dict](#27-comparing-list-tuple-set-and-dict)
  - [2.8 Hashable versus Unhashable Objects](#28-hashable-versus-unhashable-objects)
  - [2.9 Shallow Copy versus Deep Copy](#29-shallow-copy-versus-deep-copy)
  - [2.10 Nested Collections](#210-nested-collections)
  - [2.11 Time and Space Complexity of Collection Operations](#211-time-and-space-complexity-of-collection-operations)
  - [2.12 Choosing the Right Data Structure in Production](#212-choosing-the-right-data-structure-in-production)
  - [Chapter 2 Review](#chapter-2-review)
- [3. Strings](#3-strings)
  - [3.1 Creation, Indexing, Slicing and Immutability](#31-creation-indexing-slicing-and-immutability)
  - [3.2 String Formatting: f-strings, format() and % formatting](#32-string-formatting-f-strings-format-and--formatting)
  - [3.3 Common String Methods](#33-common-string-methods)
  - [3.4 String Validation Methods](#34-string-validation-methods)
  - [3.5 Data-Cleaning Examples with Strings](#35-data-cleaning-examples-with-strings)
  - [3.6 Unicode, Encoding and Decoding](#36-unicode-encoding-and-decoding)
  - [3.7 Regular Expressions (the re Module)](#37-regular-expressions-the-re-module)
  - [3.8 Representative String Coding Problems](#38-representative-string-coding-problems)
  - [Chapter 3 Review](#chapter-3-review)
- [4. Conditionals and Loops](#4-conditionals-and-loops)
  - [4.1 if, elif and else](#41-if-elif-and-else)
  - [4.2 for and while Loops](#42-for-and-while-loops)
  - [4.3 range(), enumerate() and zip()](#43-range-enumerate-and-zip)
  - [4.4 break, continue, pass and the Loop else Clause](#44-break-continue-pass-and-the-loop-else-clause)
  - [4.5 Nested Loops](#45-nested-loops)
  - [4.6 Comprehensions](#46-comprehensions)
  - [4.7 Generator Expressions](#47-generator-expressions)
  - [4.8 When Comprehensions Reduce Readability](#48-when-comprehensions-reduce-readability)
  - [4.9 Representative Looping Problems](#49-representative-looping-problems)
  - [Chapter 4 Review](#chapter-4-review)
- [5. Functions](#5-functions)
  - [5.1 Defining and Calling Functions](#51-defining-and-calling-functions)
  - [5.2 Parameters versus Arguments](#52-parameters-versus-arguments)
  - [5.3 Positional, Keyword and Default Arguments](#53-positional-keyword-and-default-arguments)
  - [5.4 Return Values, Multiple Returns and Argument Passing](#54-return-values-multiple-returns-and-argument-passing)
  - [5.5 *args and **kwargs](#55-args-and-kwargs)
  - [5.6 Keyword-Only and Positional-Only Parameters](#56-keyword-only-and-positional-only-parameters)
  - [5.7 Variable Scope and the LEGB Rule](#57-variable-scope-and-the-legb-rule)
  - [5.8 global and nonlocal](#58-global-and-nonlocal)
  - [5.9 Lambda Functions](#59-lambda-functions)
  - [5.10 map(), filter(), reduce(), sorted(), any() and all()](#510-map-filter-reduce-sorted-any-and-all)
  - [5.11 First-Class Functions](#511-first-class-functions)
  - [5.12 Higher-Order Functions](#512-higher-order-functions)
  - [5.13 Closures](#513-closures)
  - [5.14 Recursion](#514-recursion)
  - [5.15 Function Annotations and Type Hints](#515-function-annotations-and-type-hints)
  - [5.16 Pure Functions and Side Effects](#516-pure-functions-and-side-effects)
  - [Chapter 5 Review](#chapter-5-review)
- [6. Iterators and Generators](#6-iterators-and-generators)
  - [6.1 Iterable versus Iterator](#61-iterable-versus-iterator)
  - [6.2 iter(), next() and the Iterator Protocol](#62-iter-next-and-the-iterator-protocol)
  - [6.3 Creating a Custom Iterator](#63-creating-a-custom-iterator)
  - [6.4 Generator Functions and yield](#64-generator-functions-and-yield)
  - [6.5 Generator Expressions](#65-generator-expressions)
  - [6.6 yield from](#66-yield-from)
  - [6.7 send(), close() and Generator State](#67-send-close-and-generator-state)
  - [6.8 Lazy Evaluation and Memory: Lists versus Generators](#68-lazy-evaluation-and-memory-lists-versus-generators)
  - [6.9 Reading and Processing Large Files with Generators](#69-reading-and-processing-large-files-with-generators)
  - [6.10 Generator-Based Data Pipelines](#610-generator-based-data-pipelines)
  - [6.11 Interview Questions and Common Traps](#611-interview-questions-and-common-traps)
  - [Chapter 6 Review](#chapter-6-review)
- [7. Object-Oriented Programming](#7-object-oriented-programming)
  - [7.1 Classes and Objects](#71-classes-and-objects)
  - [7.2 Constructors and `__init__`](#72-constructors-and-__init__)
  - [7.3 self and cls](#73-self-and-cls)
  - [7.4 Instance, Class and "Static" Variables](#74-instance-class-and-static-variables)
  - [7.5 Instance Methods, Class Methods and Static Methods](#75-instance-methods-class-methods-and-static-methods)
  - [7.6 Inheritance and Method Overriding](#76-inheritance-and-method-overriding)
  - [7.7 super()](#77-super)
  - [7.8 Multiple Inheritance and MRO](#78-multiple-inheritance-and-mro)
  - [7.9 Polymorphism and Duck Typing](#79-polymorphism-and-duck-typing)
  - [7.10 Encapsulation](#710-encapsulation)
  - [7.11 Abstraction and Abstract Base Classes](#711-abstraction-and-abstract-base-classes)
  - [7.12 Composition versus Inheritance](#712-composition-versus-inheritance)
  - [7.13 Properties, Getters and Setters](#713-properties-getters-and-setters)
  - [7.14 Dataclasses](#714-dataclasses)
  - [7.15 Dunder (Magic) Methods](#715-dunder-magic-methods)
  - [7.16 SOLID Principles with Python Examples](#716-solid-principles-with-python-examples)
  - [7.17 Data Engineering OOP Design Example](#717-data-engineering-oop-design-example)
  - [Chapter 7 Review](#chapter-7-review)
- [8. Exception Handling](#8-exception-handling)
  - [8.1 Syntax Errors versus Runtime Exceptions](#81-syntax-errors-versus-runtime-exceptions)
  - [8.2 try, except, else and finally](#82-try-except-else-and-finally)
  - [8.3 Catching Specific Exceptions](#83-catching-specific-exceptions)
  - [8.4 Raising Exceptions](#84-raising-exceptions)
  - [8.5 Custom Exceptions](#85-custom-exceptions)
  - [8.6 Exception Chaining](#86-exception-chaining)
  - [8.7 Logging Exceptions](#87-logging-exceptions)
  - [8.8 Retry Handling](#88-retry-handling)
  - [8.9 Resource Cleanup](#89-resource-cleanup)
  - [8.10 Anti-Patterns](#810-anti-patterns)
  - [8.11 Production Examples: Database, File and API Failures](#811-production-examples-database-file-and-api-failures)
  - [Chapter 8 Review](#chapter-8-review)
- [9. File Handling](#9-file-handling)
  - [9.1 Opening, Reading, Writing and Appending Files](#91-opening-reading-writing-and-appending-files)
  - [9.2 File Modes](#92-file-modes)
  - [9.3 The with Statement for Files](#93-the-with-statement-for-files)
  - [9.4 Reading Large Files Efficiently](#94-reading-large-files-efficiently)
  - [9.5 Encoding and Newline Handling](#95-encoding-and-newline-handling)
  - [9.6 CSV Files](#96-csv-files)
  - [9.7 JSON and JSON Lines](#97-json-and-json-lines)
  - [9.8 XML](#98-xml)
  - [9.9 YAML](#99-yaml)
  - [9.10 Parquet](#910-parquet)
  - [9.11 Compressed Files: gzip, bz2 and zipfile](#911-compressed-files-gzip-bz2-and-zipfile)
  - [9.12 pathlib versus os.path](#912-pathlib-versus-ospath)
  - [9.13 shutil, glob and tempfile](#913-shutil-glob-and-tempfile)
  - [9.14 File Validation](#914-file-validation)
  - [9.15 Record-Count Reconciliation](#915-record-count-reconciliation)
  - [9.16 Chunk-Based Processing](#916-chunk-based-processing)
  - [9.17 Safe and Atomic File Writing](#917-safe-and-atomic-file-writing)
  - [9.18 File-Processing Interview Scenarios](#918-file-processing-interview-scenarios)
  - [Chapter 9 Review](#chapter-9-review)
- [10. Modules, Packages and Environments](#10-modules-packages-and-environments)
  - [10.1 Modules and Packages](#101-modules-and-packages)
  - [10.2 How import Works](#102-how-import-works)
  - [10.3 Absolute versus Relative Imports](#103-absolute-versus-relative-imports)
  - [10.4 `__name__ == "__main__"`](#104-__name__--__main__)
  - [10.5 The Module Search Path](#105-the-module-search-path)
  - [10.6 requirements.txt](#106-requirementstxt)
  - [10.7 pyproject.toml](#107-pyprojecttoml)
  - [10.8 Virtual Environments in Practice](#108-virtual-environments-in-practice)
  - [10.9 Package Structure](#109-package-structure)
  - [10.10 Circular Imports](#1010-circular-imports)
  - [10.11 Building a Reusable Data Engineering Utility Package](#1011-building-a-reusable-data-engineering-utility-package)
  - [Chapter 10 Review](#chapter-10-review)
- [11. Decorators and Context Managers](#11-decorators-and-context-managers)
  - [11.1 Decorator Fundamentals](#111-decorator-fundamentals)
  - [11.2 functools.wraps](#112-functoolswraps)
  - [11.3 Timing and Logging Decorators](#113-timing-and-logging-decorators)
  - [11.4 Caching Decorators](#114-caching-decorators)
  - [11.5 Decorators with Arguments](#115-decorators-with-arguments)
  - [11.6 Validation and Authorization Decorators](#116-validation-and-authorization-decorators)
  - [11.7 Class Decorators and Decorator Classes](#117-class-decorators-and-decorator-classes)
  - [11.8 Stacking Decorators](#118-stacking-decorators)
  - [11.9 The Context Manager Protocol](#119-the-context-manager-protocol)
  - [11.10 contextlib and @contextmanager](#1110-contextlib-and-contextmanager)
  - [11.11 Production Context Managers: Database Connections and Files](#1111-production-context-managers-database-connections-and-files)
  - [Chapter 11 Review](#chapter-11-review)
- [12. Advanced Python](#12-advanced-python)
  - [12.1 Memory Management in CPython](#121-memory-management-in-cpython)
  - [12.2 Stack versus Heap](#122-stack-versus-heap)
  - [12.3 Reference Counting](#123-reference-counting)
  - [12.4 Garbage Collection and Cyclic References](#124-garbage-collection-and-cyclic-references)
  - [12.5 Weak References](#125-weak-references)
  - [12.6 Copy Semantics](#126-copy-semantics)
  - [12.7 Interning](#127-interning)
  - [12.8 `__slots__`](#128-__slots__)
  - [12.9 Dynamic Attribute Access](#129-dynamic-attribute-access)
  - [12.10 Descriptors and @property Internals](#1210-descriptors-and-property-internals)
  - [12.11 Metaclasses](#1211-metaclasses)
  - [12.12 Monkey Patching](#1212-monkey-patching)
  - [12.13 Duck Typing in Depth](#1213-duck-typing-in-depth)
  - [12.14 Method Resolution Order Revisited](#1214-method-resolution-order-revisited)
  - [12.15 EAFP versus LBYL](#1215-eafp-versus-lbyl)
  - [12.16 Serialization and Deserialization](#1216-serialization-and-deserialization)
  - [12.17 Pickle Risks and Safer Alternatives](#1217-pickle-risks-and-safer-alternatives)
  - [12.18 functools Module](#1218-functools-module)
  - [12.19 itertools Module](#1219-itertools-module)
  - [12.20 collections Module](#1220-collections-module)
  - [12.21 operator Module](#1221-operator-module)
  - [Chapter 12 Review](#chapter-12-review)
- [13. Concurrency and Parallelism](#13-concurrency-and-parallelism)
  - [13.1 Process versus Thread](#131-process-versus-thread)
  - [13.2 Concurrency versus Parallelism](#132-concurrency-versus-parallelism)
  - [13.3 The Global Interpreter Lock (GIL)](#133-the-global-interpreter-lock-gil)
  - [13.4 CPU-Bound versus I/O-Bound Workloads](#134-cpu-bound-versus-io-bound-workloads)
  - [13.5 threading Module](#135-threading-module)
  - [13.6 Race Conditions and Locks](#136-race-conditions-and-locks)
  - [13.7 Deadlocks](#137-deadlocks)
  - [13.8 Semaphores and Rate Limiting](#138-semaphores-and-rate-limiting)
  - [13.9 Queues and the Producer-Consumer Pattern](#139-queues-and-the-producer-consumer-pattern)
  - [13.10 multiprocessing Module](#1310-multiprocessing-module)
  - [13.11 concurrent.futures: ThreadPoolExecutor and ProcessPoolExecutor](#1311-concurrentfutures-threadpoolexecutor-and-processpoolexecutor)
  - [13.12 asyncio: Coroutines, Tasks and the Event Loop](#1312-asyncio-coroutines-tasks-and-the-event-loop)
  - [13.13 Choosing Between threading, multiprocessing and asyncio](#1313-choosing-between-threading-multiprocessing-and-asyncio)
  - [13.14 Parallel File and API Processing Examples](#1314-parallel-file-and-api-processing-examples)
  - [13.15 Error Handling and Safe Shutdown](#1315-error-handling-and-safe-shutdown)
  - [Chapter 13 Review](#chapter-13-review)
- [14. Database Programming](#14-database-programming)
  - [14.1 Connecting Python to Relational Databases](#141-connecting-python-to-relational-databases)
  - [14.2 DB-API 2.0 Concepts](#142-db-api-20-concepts)
  - [14.3 Executing Parameterized SQL](#143-executing-parameterized-sql)
  - [14.4 SQL Injection Prevention](#144-sql-injection-prevention)
  - [14.5 Transactions, Commits and Rollbacks](#145-transactions-commits-and-rollbacks)
  - [14.6 Connection Pooling](#146-connection-pooling)
  - [14.7 Batch Inserts and executemany()](#147-batch-inserts-and-executemany)
  - [14.8 Fetching Results Efficiently](#148-fetching-results-efficiently)
  - [14.9 Processing Large Result Sets in Batches](#149-processing-large-result-sets-in-batches)
  - [14.10 Context Managers for Database Connections](#1410-context-managers-for-database-connections)
  - [14.11 PostgreSQL, MySQL and Snowflake Connector Examples](#1411-postgresql-mysql-and-snowflake-connector-examples)
  - [14.12 Production-Safe Incremental Extraction](#1412-production-safe-incremental-extraction)
  - [14.13 Retry, Timeout, Logging and Cleanup Practices](#1413-retry-timeout-logging-and-cleanup-practices)
  - [Chapter 14 Review](#chapter-14-review)
- [15. Data Engineering with Python](#15-data-engineering-with-python)
  - [15.1 ETL versus ELT](#151-etl-versus-elt)
  - [15.2 The Extract, Transform, Validate and Load Pattern](#152-the-extract-transform-validate-and-load-pattern)
  - [15.3 Full Load versus Incremental Load](#153-full-load-versus-incremental-load)
  - [15.4 Watermarks and Checkpoints](#154-watermarks-and-checkpoints)
  - [15.5 CDC Fundamentals](#155-cdc-fundamentals)
  - [15.6 Idempotency](#156-idempotency)
  - [15.7 Deduplication](#157-deduplication)
  - [15.8 Schema Validation](#158-schema-validation)
  - [15.9 Data-Quality Checks](#159-data-quality-checks)
  - [15.10 NULL and Empty-String Handling](#1510-null-and-empty-string-handling)
  - [15.11 Audit Logging](#1511-audit-logging)
  - [15.12 Batch and Chunk Processing](#1512-batch-and-chunk-processing)
  - [15.13 Source-to-Target Reconciliation](#1513-source-to-target-reconciliation)
  - [15.14 API Pagination](#1514-api-pagination)
  - [15.15 File Ingestion Pipelines](#1515-file-ingestion-pipelines)
  - [15.16 Database-to-File and File-to-Database Pipelines](#1516-database-to-file-and-file-to-database-pipelines)
  - [15.17 Retry with Exponential Backoff](#1517-retry-with-exponential-backoff)
  - [15.18 Rate Limiting](#1518-rate-limiting)
  - [15.19 Configuration-Driven Pipeline Design](#1519-configuration-driven-pipeline-design)
  - [15.20 Environment-Based Configuration](#1520-environment-based-configuration)
  - [15.21 Structured Logging](#1521-structured-logging)
  - [15.22 Error Handling and Alerting](#1522-error-handling-and-alerting)
  - [15.23 Secrets Management Principles](#1523-secrets-management-principles)
  - [15.24 Restartability and Recovery](#1524-restartability-and-recovery)
  - [15.25 Unit Testing ETL Logic](#1525-unit-testing-etl-logic)
  - [Chapter 15 Review](#chapter-15-review)
- [16. Important Libraries](#16-important-libraries)
  - [16.1 os](#161-os)
  - [16.2 pathlib](#162-pathlib)
  - [16.3 sys and argparse](#163-sys-and-argparse)
  - [16.4 shutil](#164-shutil)
  - [16.5 glob](#165-glob)
  - [16.6 re](#166-re)
  - [16.7 json](#167-json)
  - [16.8 csv](#168-csv)
  - [16.9 datetime](#169-datetime)
  - [16.10 zoneinfo](#1610-zoneinfo)
  - [16.11 logging](#1611-logging)
  - [16.12 collections](#1612-collections)
  - [16.13 itertools](#1613-itertools)
  - [16.14 functools](#1614-functools)
  - [16.15 typing](#1615-typing)
  - [16.16 dataclasses](#1616-dataclasses)
  - [16.17 decimal](#1617-decimal)
  - [16.18 tempfile](#1618-tempfile)
  - [16.19 gzip and zipfile](#1619-gzip-and-zipfile)
  - [16.20 hashlib](#1620-hashlib)
  - [16.21 requests](#1621-requests)
  - [16.22 pandas](#1622-pandas)
  - [16.23 NumPy](#1623-numpy)
  - [16.24 pytest](#1624-pytest)
  - [16.25 unittest and unittest.mock](#1625-unittest-and-unittestmock)
  - [16.26 boto3 (AWS SDK) for S3](#1626-boto3-aws-sdk-for-s3)
  - [Chapter 16 Review](#chapter-16-review)
- [17. pandas for Data Engineers](#17-pandas-for-data-engineers)
  - [17.1 Series and DataFrame](#171-series-and-dataframe)
  - [17.2 Reading Data: CSV, JSON, Excel, SQL and Parquet](#172-reading-data-csv-json-excel-sql-and-parquet)
  - [17.3 Selecting and Filtering Data](#173-selecting-and-filtering-data)
  - [17.4 loc versus iloc](#174-loc-versus-iloc)
  - [17.5 Handling Missing Values](#175-handling-missing-values)
  - [17.6 Data-Type Conversion](#176-data-type-conversion)
  - [17.7 Duplicates](#177-duplicates)
  - [17.8 Sorting](#178-sorting)
  - [17.9 groupby and Aggregation](#179-groupby-and-aggregation)
  - [17.10 merge, join and concat](#1710-merge-join-and-concat)
  - [17.11 apply, map and Vectorized Operations](#1711-apply-map-and-vectorized-operations)
  - [17.12 Pivot and Melt](#1712-pivot-and-melt)
  - [17.13 Datetime Processing](#1713-datetime-processing)
  - [17.14 Chunk-Based File Reading](#1714-chunk-based-file-reading)
  - [17.15 Memory Optimization](#1715-memory-optimization)
  - [17.16 Common Performance Problems](#1716-common-performance-problems)
  - [17.17 Pandas versus PySpark](#1717-pandas-versus-pyspark)
  - [17.18 Interview Coding Examples](#1718-interview-coding-examples)
  - [Chapter 17 Review](#chapter-17-review)
- [18. Testing, Logging and Code Quality](#18-testing-logging-and-code-quality)
  - [18.1 Unit, Integration and End-to-End Testing](#181-unit-integration-and-end-to-end-testing)
  - [18.2 pytest Basics](#182-pytest-basics)
  - [18.3 Fixtures and Parameterized Tests](#183-fixtures-and-parameterized-tests)
  - [18.4 Mocking](#184-mocking)
  - [18.5 Testing Files, Databases and APIs](#185-testing-files-databases-and-apis)
  - [18.6 Logging Levels](#186-logging-levels)
  - [18.7 Structured and Contextual Logging](#187-structured-and-contextual-logging)
  - [18.8 Avoiding Sensitive Information in Logs](#188-avoiding-sensitive-information-in-logs)
  - [18.9 PEP 8 and Formatting](#189-pep-8-and-formatting)
  - [18.10 Type Hints and Static Analysis](#1810-type-hints-and-static-analysis)
  - [18.11 Docstrings](#1811-docstrings)
  - [18.12 Code Organization](#1812-code-organization)
  - [18.13 Defensive Programming](#1813-defensive-programming)
  - [18.14 Production-Readiness Checklist](#1814-production-readiness-checklist)
  - [Chapter 18 Review](#chapter-18-review)
- [19. Design Patterns for Data Engineering](#19-design-patterns-for-data-engineering)
  - [19.1 Factory](#191-factory)
  - [19.2 Strategy](#192-strategy)
  - [19.3 Singleton and Its Limitations](#193-singleton-and-its-limitations)
  - [19.4 Builder](#194-builder)
  - [19.5 Adapter](#195-adapter)
  - [19.6 Template Method](#196-template-method)
  - [19.7 Dependency Injection](#197-dependency-injection)
  - [19.8 Repository Pattern](#198-repository-pattern)
  - [19.9 Pipeline Pattern](#199-pipeline-pattern)
  - [19.10 When Patterns Become Overengineering](#1910-when-patterns-become-overengineering)
  - [Chapter 19 Review](#chapter-19-review)
- [20. Interview Coding Problems](#20-interview-coding-problems)
  - [20.1 String Problems](#201-string-problems)
  - [20.2 List and Tuple Problems](#202-list-and-tuple-problems)
  - [20.3 Set and Dictionary Problems](#203-set-and-dictionary-problems)
  - [20.4 Sorting and Searching Problems](#204-sorting-and-searching-problems)
  - [20.5 Recursion Problems](#205-recursion-problems)
  - [20.6 Grouping, Joining and Aggregation Problems](#206-grouping-joining-and-aggregation-problems)
  - [20.7 File, CSV and JSON Problems](#207-file-csv-and-json-problems)
  - [20.8 Date and Log Problems](#208-date-and-log-problems)
  - [20.9 Generator and Decorator Problems](#209-generator-and-decorator-problems)
  - [20.10 API and Database Problems](#2010-api-and-database-problems)
  - [20.11 Memory, Missing-Value and Complexity Problems](#2011-memory-missing-value-and-complexity-problems)
  - [20.12 Design Problems](#2012-design-problems)
  - [20.13 Classic Algorithm Problems](#2013-classic-algorithm-problems)
  - [Chapter 20 Review](#chapter-20-review)
- [21. Scenario-Based Interview Questions](#21-scenario-based-interview-questions)
  - [21.1 Processing a File Larger Than Available Memory](#211-processing-a-file-larger-than-available-memory)
  - [21.2 Handling Malformed Rows](#212-handling-malformed-rows)
  - [21.3 Handling Duplicate Records](#213-handling-duplicate-records)
  - [21.4 Recovering from Partial Pipeline Failures](#214-recovering-from-partial-pipeline-failures)
  - [21.5 Designing an Idempotent Pipeline](#215-designing-an-idempotent-pipeline)
  - [21.6 Reading Millions of Database Rows](#216-reading-millions-of-database-rows)
  - [21.7 Handling API Pagination and Rate Limits](#217-handling-api-pagination-and-rate-limits)
  - [21.8 Retrying Transient Errors Without Duplicating Records](#218-retrying-transient-errors-without-duplicating-records)
  - [21.9 Tracking Watermarks](#219-tracking-watermarks)
  - [21.10 Handling Schema Changes](#2110-handling-schema-changes)
  - [21.11 Maintaining Audit Counts](#2111-maintaining-audit-counts)
  - [21.12 Handling NULL versus Empty Strings](#2112-handling-null-versus-empty-strings)
  - [21.13 Avoiding the Small-File Problem](#2113-avoiding-the-small-file-problem)
  - [21.14 Designing Configuration-Driven Pipelines](#2114-designing-configuration-driven-pipelines)
  - [21.15 Protecting Credentials](#2115-protecting-credentials)
  - [21.16 Improving Slow Python Transformation Code](#2116-improving-slow-python-transformation-code)
  - [21.17 Choosing Python, pandas or PySpark](#2117-choosing-python-pandas-or-pyspark)
  - [Chapter 21 Review](#chapter-21-review)
- [22. Rapid Revision Material](#22-rapid-revision-material)
  - [22.1 Python Interview Cheat Sheet](#221-python-interview-cheat-sheet)
  - [22.2 Data Structure Comparison Summary](#222-data-structure-comparison-summary)
  - [22.3 Complexity Summary](#223-complexity-summary)
  - [22.4 Common Built-in Functions Summary](#224-common-built-in-functions-summary)
  - [22.5 Common Exception Types](#225-common-exception-types)
  - [22.6 Important Library Summary](#226-important-library-summary)
  - [22.7 Top Python Data Engineer Interview Questions](#227-top-python-data-engineer-interview-questions)
  - [22.8 Last-Minute Revision Checklist](#228-last-minute-revision-checklist)
  - [22.9 Production-Readiness Checklist (Short Form)](#229-production-readiness-checklist-short-form)
  - [22.10 Practice Assignments](#2210-practice-assignments)

---

## 1. Python Foundations

### 1.1 Python Features and Use Cases in Data Engineering

**Definition:** Python is a high-level, general-purpose language. It is dynamically typed, uses automatic memory management, and has a very large standard library and package ecosystem.

**Why it matters for a Data Engineer:** Python is the "glue" language of modern data platforms:

| Use case | Typical tools |
|---|---|
| Orchestration (scheduling pipelines) | Airflow, Dagster, Prefect – the DAGs themselves are Python |
| Distributed processing | PySpark, Dask, Ray |
| Single-machine processing | pandas, Polars, DuckDB, NumPy |
| Cloud automation | boto3 (AWS), google-cloud-*, azure-* SDKs |
| Database access | psycopg (PostgreSQL), mysql-connector, snowflake-connector-python, SQLAlchemy |
| API ingestion | requests, httpx, aiohttp |
| Data quality and testing | pytest, Great Expectations, pydantic |

**Key features to mention in an interview:**
- **Readable syntax** – indentation defines blocks, so code is easy to review.
- **Batteries included** – `csv`, `json`, `datetime`, `logging`, `pathlib` and more come built in.
- **Dynamic but strongly typed** (see [1.7](#17-dynamic-typing-and-strong-typing)).
- **Multi-paradigm** – procedural, object-oriented and functional styles.
- **Trade-off** – pure Python loops are slow compared with C/Java. Heavy work is pushed down to optimised engines (NumPy, pandas, Spark, the database itself).

**Interview question:** *Why is Python popular for data engineering even though it is "slow"?*
**Answer:** Most of the heavy lifting happens in optimised native code (C/C++ in NumPy and pandas, the JVM in Spark, the SQL engine in the warehouse). Python orchestrates that work. Developer productivity, the ecosystem and integration with every cloud and database matter more than raw loop speed.

---

### 1.2 Python Execution Model

**Definition:** When you run `python script.py`, CPython (the standard implementation):

1. **Reads** the source code.
2. **Compiles** it to **bytecode** – a low-level, platform-independent instruction set. Imported modules are cached as `.pyc` files in `__pycache__/`.
3. **Executes** the bytecode on the **Python Virtual Machine (PVM)**, an interpreter loop inside CPython.

```text
script.py  --compile-->  bytecode (.pyc)  --interpret-->  Python Virtual Machine  -->  result
```

**How it works:** You can see the bytecode with the `dis` module. The exact instructions differ between Python versions.

```python
import dis

def add(first: int, second: int) -> int:
    return first + second

dis.dis(add)   # prints instructions such as LOAD_FAST and BINARY_OP (names vary by version)
```

**Other implementations:** PyPy (JIT-compiled, often faster for pure-Python loops), Jython (JVM), MicroPython. "Python" in interviews almost always means **CPython**.

---

### 1.3 Interpreted versus Compiled Behaviour

**Definition:**
- A **compiled** language (C, Go) is translated ahead of time into machine code for a specific CPU.
- An **interpreted** language is executed by another program at run time.

Python is **both**: it is *compiled to bytecode* and then *interpreted* by the PVM. That is why it is usually called "interpreted" while still producing `.pyc` files.

**Why it matters for a Data Engineer:**
- Errors such as a `NameError` or a `TypeError` only appear **when that line runs**. A pipeline can fail 3 hours in on a branch that was never tested. That is why tests, linters and type checkers matter (Chapter 18).
- A `SyntaxError` is caught at compile time, so the file never starts running.

**Interview question:** *Is Python compiled or interpreted?*
**Answer:** CPython compiles source code to bytecode and interprets that bytecode on a virtual machine. It does not compile to native machine code ahead of time.

---

### 1.4 Installation, Virtual Environments, pip and Dependency Management

**Definition:**
- **pip** installs packages from PyPI (the Python Package Index).
- A **virtual environment (venv)** is an isolated folder with its own Python interpreter link and its own installed packages.

**Why it matters for a Data Engineer:** Pipeline A may need `pandas==1.5` and pipeline B `pandas==2.2`. Without isolation they break each other. Production jobs must also install **exactly the same versions** as were tested.

**Syntax (command line):**

```text
# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

# Install, freeze and reproduce
python -m pip install pandas==2.2.2 requests
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

deactivate
```

**Best practices:**
- Use `python -m pip` instead of plain `pip`, so you install into the interpreter you are actually running.
- **Pin versions** for applications (`requests==2.32.3`). Libraries you publish declare compatible ranges instead.
- Declare project metadata and dependencies in `pyproject.toml` (see [10.7](#107-pyprojecttoml)). Tools like `pip-tools`, Poetry and uv generate **lock files** with exact versions.
- Never install packages into the system Python on a server. Use a venv or a container image.

**Common mistakes:** committing the `.venv` folder to Git, forgetting to activate the venv, and unpinned dependencies that change silently between deployments.

---

### 1.5 Variables, Identifiers, Keywords, Indentation, Comments and Naming

**Definition:**
- A **variable** is a **name bound to an object**. The name does not "contain" the value; it refers to an object in memory.
- An **identifier** is any name (variable, function, class). It must start with a letter or `_`, contain only letters, digits and `_`, and is case-sensitive.
- **Keywords** are reserved words that cannot be identifiers: `if`, `for`, `class`, `def`, `return`, `None`, `True`, `lambda`, `with`, `yield`, `async`, `await` and others (`import keyword; print(keyword.kwlist)`).
- **Indentation** (4 spaces by convention) defines code blocks. Mixing tabs and spaces raises `TabError`.
- **Comments** start with `#`. A **docstring** is a string literal placed first in a module, function or class and is available at run time via `__doc__`.

```python
import keyword

row_count = 10          # variable: snake_case
MAX_RETRIES = 3         # constant: UPPER_CASE (a convention; Python does not enforce it)


class FileLoader:       # class: PascalCase
    """Load files from a landing folder."""   # docstring


def _internal_helper():  # leading underscore: "internal use"
    pass


print(keyword.iskeyword("class"), keyword.iskeyword("row_count"))
print(FileLoader.__doc__)
```

**Output:**

```text
True False
Load files from a landing folder.
```

**PEP 8 naming conventions:**

| Kind | Style | Example |
|---|---|---|
| Variable, function, module | `snake_case` | `load_orders`, `row_count` |
| Class, exception | `PascalCase` | `OrderLoader`, `DataValidationError` |
| Constant | `UPPER_SNAKE_CASE` | `BATCH_SIZE` |
| Internal | `_leading_underscore` | `_parse_row` |
| Avoid clashing with keywords | `trailing_underscore_` | `class_`, `type_` |

**Common mistakes:** shadowing built-ins (`list = [1, 2]` and then `list("abc")` fails), and naming a file `csv.py` or `json.py`, which hides the standard library module of the same name.

---

### 1.6 Mutable versus Immutable Objects

**Definition:**
- **Mutable** objects can be changed in place after creation: `list`, `dict`, `set`, `bytearray`, and most user-defined objects.
- **Immutable** objects cannot be changed. Any "modification" creates a new object: `int`, `float`, `complex`, `bool`, `str`, `bytes`, `tuple`, `frozenset`, `range`, `None`.

**Why it matters for a Data Engineer:**
- Only **hashable** objects can be dict keys or set members. Composite keys such as `(customer_id, order_date)` must be tuples, not lists.
- Changing a shared mutable object (a config dict, a list of records) affects every piece of code holding a reference. This is a common source of silent data corruption.

**How it works:** An immutable "change" rebinds the name to a **new object**; a mutable change modifies the **same object**. `id()` shows the object's identity.

```python
text = "data"
text_id_before = id(text)
text += "_lake"                       # creates a new string
print(text, id(text) == text_id_before)

columns = ["id"]
columns_id_before = id(columns)
columns.append("name")                # modifies the same list
print(columns, id(columns) == columns_id_before)
```

**Output:**

```text
data_lake False
['id', 'name'] True
```

**Important subtlety:** "immutable" is not the same as "hashable". A tuple is immutable, but a tuple **containing a list** is not hashable, because its contents can change.

```python
print(hash((1, 2)) == hash((1, 2)))
try:
    hash((1, [2, 3]))
except TypeError as error:
    print("TypeError:", error)
```

**Output:**

```text
True
TypeError: unhashable type: 'list'
```

**Interview question:** *Can a tuple be modified?*
**Answer:** The tuple itself cannot (you cannot add, remove or reassign items). If it contains a mutable object such as a list, that inner object can still be changed, and such a tuple is not hashable.

---

### 1.7 Dynamic Typing and Strong Typing

**Definition:**
- **Dynamic typing:** types belong to **objects**, not variables. A name can refer to an `int` now and a `str` later. Types are checked at run time.
- **Strong typing:** Python does **not** silently convert between unrelated types. `"5" + 5` raises `TypeError` (JavaScript, a weakly typed language, would return `"55"`).

```python
value = 42
print(type(value).__name__)
value = "forty-two"
print(type(value).__name__)

try:
    print("5" + 5)
except TypeError as error:
    print("TypeError:", error)

print("5" + str(5), int("5") + 5)
```

**Output:**

```text
int
str
TypeError: can only concatenate str (not "int") to str
55 10
```

**Why it matters for a Data Engineer:** Data from CSV files, APIs and environment variables arrives **as strings**. You must convert types explicitly (`int(row["qty"])`); Python will not guess for you. Implicit numeric widening still happens: `1 + 2.5` gives `3.5` and `True + 1` gives `2` (because `bool` is a subclass of `int`).

**Follow-up question:** *Do type hints make Python statically typed?* No. Hints are not enforced at run time. Tools such as mypy or pyright check them before running (see [5.15](#515-function-annotations-and-type-hints)).

---

### 1.8 Object Identity, Value Equality and References

**Definition:**
- **Identity** – *which* object it is. `id(obj)` returns a unique integer for the object's lifetime (in CPython, its memory address).
- **Equality** – whether two objects have the same **value**, decided by `__eq__`.
- **Reference** – a name, list slot or dict value that points to an object. Several references can point to the same object.

```python
original = {"env": "dev"}
alias = original               # second reference, same object
alias["env"] = "prod"
print(original)

copy_of = dict(original)       # new object with the same value
print(copy_of == original, copy_of is original)
```

**Output:**

```text
{'env': 'prod'}
True False
```

**Why it matters for a Data Engineer:** Assignment never copies. `config_for_job = base_config` followed by an edit changes `base_config` for every other job too.

---

### 1.9 id(), type(), isinstance(), == and is

| Tool | Answers | Typical use |
|---|---|---|
| `id(obj)` | What is this object's identity? | Debugging aliasing |
| `type(obj)` | What is the exact class? | Printing or logging types |
| `isinstance(obj, cls)` | Is it this class **or a subclass**? | Type checks in validation code |
| `a == b` | Same value? | Almost all comparisons |
| `a is b` | Same object? | Only for singletons: `None`, `True`, `False`, sentinels |

```python
class Event:
    pass


class ClickEvent(Event):
    pass


click = ClickEvent()
print(type(click) is Event, isinstance(click, Event))
print(isinstance(True, int), isinstance(3.0, (int, float)))

result = None
print(result is None)
```

**Output:**

```text
False True
True True
True
```

**Common mistakes:**
- `if value is 0:` or `if name is "abc":` – may work by accident because of caching (see [12.7](#127-interning)), then fail with other values. Python 3.8+ emits `SyntaxWarning: "is" with a literal`.
- `type(x) == int` rejects subclasses, and `isinstance(True, int)` is `True`. When validating a numeric column, exclude booleans explicitly if needed: `isinstance(x, int) and not isinstance(x, bool)`.

**Interview question:** *Difference between `==` and `is`?*
**Answer:** `==` compares values via `__eq__`. `is` compares identity (same object). Use `is` only for `None` and other singletons.

---

### 1.10 Truthy and Falsy Values

**Definition:** Every object has a truth value in `if`/`while`. **Falsy:** `None`, `False`, `0`, `0.0`, `0j`, `Decimal(0)`, `''`, `b''`, `[]`, `()`, `{}`, `set()`, `range(0)`. Everything else is **truthy**, unless a class defines `__bool__` or `__len__` that says otherwise.

**Data Engineering example – the zero-versus-missing bug:**

```python
records = [
    {"id": 1, "amount": 0},       # valid: a zero-value refund
    {"id": 2, "amount": None},    # missing
    {"id": 3},                    # missing key
]

wrong = [r["id"] for r in records if not r.get("amount")]
right = [r["id"] for r in records if r.get("amount") is None]
print("rejected (wrong):", wrong)
print("rejected (right):", right)
```

**Output:**

```text
rejected (wrong): [1, 2, 3]
rejected (right): [2, 3]
```

**Best practice:** Use truthiness for "is this collection empty?" (`if rows:`). Use explicit checks (`is None`, `== ""`) for **data values**, where `0`, `False` and `""` can be legitimate.

---

### 1.11 Input and Output

**Definition:** `input()` reads a line from standard input as a **string**. `print()` writes to standard output.

```python
import sys

print("rows", 100, sep="=", end=";\n")
print("warning: 3 rows rejected", file=sys.stderr)   # goes to the error stream
print(f"{'table':<10}|{'rows':>6}")
print(f"{'orders':<10}|{1250:>6}")
```

**Output (standard output only):**

```text
rows=100;
table     |  rows
orders    |  1250
```

**Why it matters for a Data Engineer:** Batch jobs rarely use `input()`. Configuration comes from command-line arguments (`argparse`, `sys.argv`), environment variables (`os.environ`) or config files. Diagnostics go to **logging**, not `print` (see [18.6](#186-logging-levels)). Schedulers capture stdout and stderr separately and use the **exit code** (`sys.exit(1)`) to decide success or failure.

---

### 1.12 Operators and Operator Precedence

| Category | Operators |
|---|---|
| Arithmetic | `+ - * / // % **` (`/` always returns float; `//` floor division) |
| Comparison | `== != < <= > >=` (can be chained: `0 <= x < 10`) |
| Logical | `and or not` (short-circuit, return one of the operands) |
| Membership / identity | `in`, `not in`, `is`, `is not` |
| Bitwise | `&`, `\|`, `^`, `~`, `<<`, `>>` (`&`, `\|`, `^` are also set operations) |
| Assignment | `= += -= *= /= //= %= **=` and the walrus `:=` (3.8+) |

**Precedence (high → low):** `**` → unary `-x`, `~x` → `* / // %` → `+ -` → shifts → `&` → `^` → `|` → comparisons, `in`, `is` → `not` → `and` → `or` → `if/else` expression → `lambda` → `:=`.

```python
print(2 + 3 * 4 ** 2)        # 4**2 first, then *, then +
print(-2 ** 2)               # ** binds tighter than unary minus
print(10 // 3, -10 // 3)     # floor division rounds toward negative infinity
print(10 % 3, -10 % 3)       # result has the sign of the divisor
print(not True or True)      # (not True) or True
print(0 or "default", "" and "never")   # and/or return operands
print(0.1 + 0.2 == 0.3, round(0.1 + 0.2, 10) == 0.3)
```

**Output:**

```text
50
-4
3 -4
1 2
True
default 
False True
```

**Common mistakes:**
- Comparing floats with `==`. Use `math.isclose` or `decimal.Decimal` for money (see [16.17](#1617-decimal)).
- `value = user_value or 10` replaces a legitimate `0` with `10`. Use `10 if user_value is None else user_value`.
- `round(2.5)` returns `2` (round half to even, "banker's rounding").

---

### 1.13 Type Conversion and Type Checking

**Definition:** **Explicit conversion** (casting) uses constructors: `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()`. **Implicit conversion** happens only between numeric types (`int` → `float` → `complex`).

```python
print(int("42"), float("3.5"), int(3.99), int("ff", 16))
print(bool("False"), bool(""), str(None))
print(list("abc"), tuple([1, 2]), set([1, 1, 2]))

try:
    int("3.5")
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
42 3.5 3 255
True False None
['a', 'b', 'c'] (1, 2) {1, 2}
ValueError: invalid literal for int() with base 10: '3.5'
```

**Data Engineering example – safe conversion of CSV fields:**

```python
from decimal import Decimal, InvalidOperation


def to_int(raw: str | None) -> int | None:
    """Convert a CSV field to int; blank or missing becomes None, bad values raise."""
    if raw is None or raw.strip() == "":
        return None
    return int(raw.strip())


def to_bool(raw: str) -> bool:
    """Convert common text flags to bool. bool('false') would be True, so map explicitly."""
    normalized = raw.strip().lower()
    if normalized in {"true", "t", "yes", "y", "1"}:
        return True
    if normalized in {"false", "f", "no", "n", "0"}:
        return False
    raise ValueError(f"not a boolean: {raw!r}")


def to_money(raw: str) -> Decimal:
    """Parse a money amount exactly (no float rounding)."""
    try:
        return Decimal(raw.strip())
    except InvalidOperation as error:
        raise ValueError(f"not a decimal: {raw!r}") from error


print(to_int(" 7 "), to_int(""), to_bool("No"), to_money("19.99"))
```

**Output:**

```text
7 None False 19.99
```

**Common mistakes:** `bool("False")` is `True` (any non-empty string is truthy). `int(3.99)` truncates instead of rounding. Using `float` for currency causes rounding errors.

---

### Chapter 1 Review

**Key takeaways**
- CPython compiles source to bytecode and interprets it; most type errors only appear at run time.
- Variables are names bound to objects. Assignment never copies.
- Python is dynamically **and** strongly typed.
- Use `==` for values and `is` only for `None` and other singletons.
- Use explicit `is None` checks for data values; `0` and `""` are falsy but often valid.
- Isolate every project in a virtual environment with pinned dependencies.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Is Python pass-by-value or pass-by-reference? | Neither exactly: **pass-by-object-reference**. The function receives a reference to the same object (see [5.4](#54-return-values-multiple-returns-and-argument-passing)). |
| Why is `-10 // 3` equal to `-4`? | `//` floors toward negative infinity. |
| What does `isinstance(True, int)` return? | `True`; `bool` is a subclass of `int`. |
| What is in `__pycache__`? | Cached bytecode (`.pyc`) of imported modules. |
| Why `python -m pip`? | It guarantees pip installs into the interpreter you are running. |

**Common traps:** `is` with literals, `bool("False")`, float equality, shadowing built-ins, a file named after a standard library module.

**Practice exercise:** Write `parse_flag(raw)` that returns `True`/`False` for `"Y"`, `"n"`, `"TRUE"`, `"0"` and raises `ValueError` for anything else. Then explain why `bool(raw)` is wrong.

---

## 2. Built-in Data Types

### 2.1 Scalar Types: int, float, complex, bool and None

**Definition:**

| Type | Meaning | Example | Notes |
|---|---|---|---|
| `int` | whole numbers, **arbitrary precision** | `10**30` | never overflows |
| `float` | 64-bit IEEE 754 double | `3.14`, `1e-9`, `float("nan")` | binary approximation: `0.1 + 0.2 != 0.3` |
| `complex` | real + imaginary | `3 + 4j` | rarely used in data engineering |
| `bool` | `True` / `False` | `is_active = True` | a subclass of `int` (`True == 1`) |
| `NoneType` | absence of a value | `None` | the only instance; compare with `is None` |

```python
import math

print(10**20 + 1)
print(7 / 2, 7 // 2, 7 % 2, divmod(7, 2))
print(abs(3 + 4j), True + True)
nan = float("nan")
print(nan == nan, math.isnan(nan))
print(math.isclose(0.1 + 0.2, 0.3))
```

**Output:**

```text
100000000000000000001
3.5 3 1 (3, 1)
5.0 2
False True
True
```

**Why it matters for a Data Engineer:**
- `NaN` is not equal to itself, so `value == float("nan")` never finds missing values. Use `math.isnan` (or `pandas.isna`).
- `None` (SQL `NULL`) and `NaN` (a float "not a number") are different things. pandas uses both, which surprises many people.
- Use `decimal.Decimal` for money and `int` cents for exact totals.

---

### 2.2 Sequence and Binary Types: str, bytes, bytearray and range

| Type | Mutable | Holds | Example |
|---|---|---|---|
| `str` | No | Unicode text | `"café"` |
| `bytes` | No | raw bytes 0–255 | `b"\x00\xff"`, file contents opened in `"rb"` mode |
| `bytearray` | Yes | raw bytes | building binary buffers |
| `range` | No | a lazy sequence of integers | `range(0, 10, 2)` uses constant memory |

```python
text = "café"
encoded = text.encode("utf-8")
print(len(text), len(encoded), encoded)
print(encoded.decode("utf-8"))

buffer = bytearray(b"abc")
buffer[0] = ord("X")
print(buffer)

numbers = range(0, 10, 3)
print(list(numbers), len(numbers), 9 in numbers)
```

**Output:**

```text
4 5 b'caf\xc3\xa9'
café
bytearray(b'Xbc')
[0, 3, 6, 9] 4 True
```

**Key point:** `str` is **text** (characters) and `bytes` is **binary** (what is actually stored on disk or sent over the network). You convert between them with `encode()` and `decode()` (see [3.6](#36-unicode-encoding-and-decoding)).

---

### 2.3 Lists

**Definition:** An **ordered, mutable** sequence that can hold any objects, including duplicates. Internally it is a dynamic array of references.

**Why it matters for a Data Engineer:** Lists are used for batches of records, column names and ordered results. They are **not** good for membership tests on large data (O(n)) or for queues (`pop(0)` is O(n)).

**Create, read, update, delete:**

```python
columns = ["id", "name", "email"]      # create
print(columns[0], columns[-1], columns[1:])   # read: index, negative index, slice
columns[1] = "full_name"               # update
del columns[2]                         # delete by index
print(columns, len(columns))
```

**Output:**

```text
id email ['name', 'email']
['id', 'full_name'] 2
```

**Important methods:**

```python
statuses = ["new", "paid"]
statuses.append("shipped")               # add one item at the end
statuses.extend(["paid", "returned"])    # add each item of an iterable
statuses.insert(0, "draft")              # insert at a position (O(n))
print(statuses)

statuses.remove("paid")                  # remove the FIRST matching value
last = statuses.pop()                    # remove and return the last item
first = statuses.pop(0)                  # remove and return by index (O(n))
print(statuses, last, first)

print(statuses.index("paid"), statuses.count("paid"))
statuses.sort()                          # in place, returns None
print(statuses)
statuses.reverse()                       # in place, returns None
print(statuses)

nested = []
nested.append([1, 2])                    # one item: a list
nested.extend([3, 4])                    # two items
print(nested)
statuses.clear()
print(statuses)
```

**Output:**

```text
['draft', 'new', 'paid', 'shipped', 'paid', 'returned']
['new', 'shipped', 'paid'] returned draft
2 1
['new', 'paid', 'shipped']
['shipped', 'paid', 'new']
[[1, 2], 3, 4]
[]
```

**Common mistakes:**
- `items = items.sort()` sets `items` to `None`. Use `items.sort()` **or** `items = sorted(items)`.
- `remove()` and `index()` raise `ValueError` if the value is missing.
- `grid = [[0] * 3] * 2` creates **two references to the same inner list**. Use `[[0] * 3 for _ in range(2)]`.
- Removing items from a list while looping over it skips elements. Build a new list instead.

---

### 2.4 Tuples

**Definition:** An **ordered, immutable** sequence. It is hashable if all its items are hashable.

```python
point = (10, 20)
single = (5,)                 # the comma makes a tuple; (5) is just the int 5
latitude, longitude = point   # unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(type(single).__name__, latitude, middle, last)
print(point.count(10), point.index(20))

daily_totals = {("2026-01-01", "EU"): 1500}   # tuple as a composite key
print(daily_totals[("2026-01-01", "EU")])
```

**Output:**

```text
tuple 10 [2, 3, 4] 5
1 1
1500
```

**Why it matters for a Data Engineer:** Tuples are used for **composite keys**, rows returned by database cursors (DB-API drivers return tuples by default), and fixed records. `collections.namedtuple` and `typing.NamedTuple` add field names (see [12.20](#1220-collections-module)).

---

### 2.5 Sets and Frozensets

**Definition:** A **set** is an unordered collection of **unique, hashable** items with O(1) average membership tests. A **frozenset** is an immutable, hashable set, so it can itself be a dict key or a set member.

```python
seen_ids = {1, 2, 3}
seen_ids.add(4)                 # add one item
seen_ids.update([5, 6])         # add many
seen_ids.discard(99)            # no error if missing
seen_ids.remove(6)              # KeyError if missing
print(seen_ids)

yesterday = {1, 2, 3}
today = {3, 4}
print(yesterday.union(today), yesterday | today)
print(yesterday.intersection(today), yesterday & today)
print(yesterday.difference(today), yesterday - today)
print(yesterday.symmetric_difference(today), yesterday ^ today)
print({1, 2} <= {1, 2, 3}, yesterday.isdisjoint({9}))

empty = set()                   # {} is an empty DICT, not a set
frozen = frozenset({"read", "write"})
permissions = {frozen: "editor"}
print(type({}).__name__, type(empty).__name__, permissions[frozenset({"write", "read"})])
```

**Output:**

```text
{1, 2, 3, 4, 5}
{1, 2, 3, 4} {1, 2, 3, 4}
{3} {3}
{1, 2} {1, 2}
{1, 2, 4} {1, 2, 4}
True True
dict set editor
```

`set.pop()` removes and returns an **arbitrary** item. Never rely on the order of a set. Sort it when you need stable output (`sorted(my_set)`).

**Data Engineering example – comparing two extracts:**

```python
source_ids = {101, 102, 103, 104}
target_ids = {101, 103, 105}
print("missing in target:", sorted(source_ids - target_ids))
print("unexpected in target:", sorted(target_ids - source_ids))
print("matched:", len(source_ids & target_ids))
```

**Output:**

```text
missing in target: [102, 104]
unexpected in target: [105]
matched: 2
```

---

### 2.6 Dictionaries

**Definition:** A mapping from **unique hashable keys** to values, implemented as a hash table. Lookups, inserts and deletes are O(1) on average. Since Python 3.7, dicts **preserve insertion order** (a language guarantee).

**Why it matters for a Data Engineer:** Dicts are the workhorse for records (JSON objects), lookups (hash joins), grouping, deduplication, configuration and caches.

**Create, read, update, delete:**

```python
order = {"id": 1, "status": "new"}          # create
order_from_pairs = dict([("id", 2), ("status", "paid")])
print(order["status"], order.get("amount"), order.get("amount", 0))   # read
order["status"] = "paid"                     # update
order["amount"] = 99.5                       # insert
del order["amount"]                          # delete
print(order, "status" in order, len(order_from_pairs))
```

**Output:**

```text
new None 0
{'id': 1, 'status': 'paid'} True 2
```

**Important methods:**

```python
config = {"host": "localhost", "port": 5432}
print(list(config.keys()), list(config.values()), list(config.items()))

config.update({"port": 6543, "db": "sales"})       # merge in place, right side wins
port = config.pop("port")                          # remove and return
missing = config.pop("timeout", 30)                # default instead of KeyError
last_item = config.popitem()                       # remove the LAST inserted pair (LIFO)
print(port, missing, last_item, config)

groups = {}
groups.setdefault("EU", []).append("order-1")      # create the key only if missing
groups.setdefault("EU", []).append("order-2")
print(groups)

flags = dict.fromkeys(["load", "validate"], False)
print(flags)

defaults = {"retries": 3, "timeout": 30}
overrides = {"timeout": 60}
print(defaults | overrides)                        # 3.9+: new merged dict
print({**defaults, **overrides})                   # works on older versions too
```

**Output:**

```text
['host', 'port'] ['localhost', 5432] [('host', 'localhost'), ('port', 5432)]
6543 30 ('db', 'sales') {'host': 'localhost'}
{'EU': ['order-1', 'order-2']}
{'load': False, 'validate': False}
{'retries': 3, 'timeout': 60}
{'retries': 3, 'timeout': 60}
```

**Common mistakes:**
- `dict.fromkeys(keys, [])` makes **every key share the same list**. Use `{key: [] for key in keys}` or `defaultdict(list)`.
- Changing a dict's size while iterating over it raises `RuntimeError: dictionary changed size during iteration`. Iterate over `list(d)` instead.
- `d[key]` raises `KeyError` for a missing key. Choose deliberately between `d[key]` (missing is a bug), `d.get(key)` (missing is normal) and `defaultdict`.
- `keys()`, `values()` and `items()` return **views**. They reflect later changes to the dict. Wrap them in `list()` for a snapshot.

**Interview question:** *How does a dict achieve O(1) lookup?*
**Answer:** It hashes the key to find a slot in an internal array, then compares the key with `==` to confirm it. Many keys with colliding hashes can degrade it to O(n), but that is rare with good hash functions.

---

### 2.7 Comparing list, tuple, set and dict

| Feature | list | tuple | set | dict |
|---|---|---|---|---|
| Ordered | Yes | Yes | **No** | Yes (insertion order, 3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys unique |
| Indexing | `lst[0]` | `tup[0]` | Not supported | by key `d["k"]` |
| `x in` cost | O(n) | O(n) | **O(1)** avg | **O(1)** avg (keys) |
| Hashable | No | Yes (if items are) | No (`frozenset` is) | No |
| Typical DE use | batches, ordered rows | composite keys, DB rows | dedupe, membership, diffs | records, lookups, grouping |

**Ordered vs unordered:** "ordered" means the iteration order is predictable (insertion order). A `set` has no guaranteed order. The order of string items in a set can even change between runs, because string hashing is randomised per process.

---

### 2.8 Hashable versus Unhashable Objects

**Definition:** An object is **hashable** if it has a hash value that never changes during its lifetime (`__hash__`) and can be compared for equality (`__eq__`). Objects that are equal must have equal hashes.

| Hashable | Unhashable |
|---|---|
| `int`, `float`, `str`, `bytes`, `bool`, `None`, `frozenset`, tuples of hashables, frozen dataclasses | `list`, `dict`, `set`, `bytearray`, tuples containing unhashables |

```python
records = [{"id": 1, "tags": ["a"]}, {"id": 1, "tags": ["a"]}]
unique = {(r["id"], tuple(r["tags"])) for r in records}   # convert to hashable form
print(unique)
```

**Output:**

```text
{(1, ('a',))}
```

**Interview question:** *Why can't a list be a dict key?*
**Answer:** A list can change after it is inserted. Its hash would then change and the dict could no longer find it. Convert it to a tuple first.

---

### 2.9 Shallow Copy versus Deep Copy

**Definition:**
- **Assignment** (`b = a`) creates no copy, just another name.
- **Shallow copy** creates a new outer container whose items are the **same objects**: `copy.copy(a)`, `a.copy()`, `list(a)`, `a[:]`, `dict(a)`.
- **Deep copy** (`copy.deepcopy(a)`) recursively copies all nested objects.

```python
import copy

template = {"columns": ["id"], "options": {"header": True}}
shallow = copy.copy(template)
deep = copy.deepcopy(template)

shallow["columns"].append("name")        # changes the shared inner list
deep["options"]["header"] = False        # changes only the deep copy
print(template)
print(shallow is template, shallow["columns"] is template["columns"])
```

**Output:**

```text
{'columns': ['id', 'name'], 'options': {'header': True}}
False True
```

**Why it matters for a Data Engineer:** A per-table config built from a shared template with a shallow copy will leak changes between tables. Deep copying is slower and copies everything, so only use it for nested data you intend to change.

---

### 2.10 Nested Collections

**Definition:** Collections inside collections. JSON from APIs maps directly to nested dicts and lists.

```python
response = {
    "page": 1,
    "results": [
        {"id": 1, "customer": {"name": "Asha", "tags": ["vip"]}},
        {"id": 2, "customer": {"name": "Ben", "tags": []}},
    ],
}

names = [item["customer"]["name"] for item in response["results"]]
vip_ids = [item["id"] for item in response["results"] if "vip" in item["customer"]["tags"]]
city = response["results"][0]["customer"].get("address", {}).get("city", "unknown")
print(names, vip_ids, city)
```

**Output:**

```text
['Asha', 'Ben'] [1] unknown
```

**Best practice:** Chain `.get(key, {})` for optional nested fields, or validate the structure once with a schema (dataclasses or pydantic) instead of scattering checks everywhere.

---

### 2.11 Time and Space Complexity of Collection Operations

**Big-O in one sentence:** how the running time (or memory) grows as the input size *n* grows. O(1) means constant, O(n) linear, O(n log n) "sort-like", and O(n²) usually means a loop inside a loop.

| Operation | list | dict | set | deque |
|---|---|---|---|---|
| Access by index / key | O(1) | O(1) avg | – | O(n) in the middle |
| `x in container` | O(n) | O(1) avg | O(1) avg | O(n) |
| Append at end | O(1) amortised | O(1) avg | O(1) avg (`add`) | O(1) |
| Insert / delete at front | O(n) | – | – | **O(1)** |
| Pop from end | O(1) | O(1) (`popitem`) | – | O(1) |
| Delete by value / key | O(n) | O(1) avg | O(1) avg | O(n) |
| Sort | O(n log n) | – | – | – |
| Copy | O(n) | O(n) | O(n) | O(n) |
| Slice of length k | O(k) | – | – | – |
| Union / intersection | – | – | O(m + n) / O(min(m, n)) | – |

"Amortised O(1)" means a list occasionally resizes (copying all items), but averaged over many appends each append costs O(1). "avg" means average case; with pathological hash collisions dict and set operations degrade to O(n).

**Space:** a list of *n* items needs O(n) memory. A dict or set needs noticeably more per item than a list, because of its hash table.

**Data Engineering example – the most important optimisation:**

```python
import time

valid_ids_list = list(range(5_000))
valid_ids_set = set(valid_ids_list)
incoming = list(range(-5_000, 5_000))

start = time.perf_counter()
matches_list = sum(1 for record_id in incoming if record_id in valid_ids_list)   # O(n*m)
list_seconds = time.perf_counter() - start

start = time.perf_counter()
matches_set = sum(1 for record_id in incoming if record_id in valid_ids_set)     # O(n)
set_seconds = time.perf_counter() - start

print(matches_list == matches_set == 5_000, set_seconds < list_seconds)
```

**Output:**

```text
True True
```

On a typical machine the list version takes seconds and the set version milliseconds. At millions of rows the difference is hours versus seconds.

---

### 2.12 Choosing the Right Data Structure in Production

| Requirement | Use | Why |
|---|---|---|
| "Have I seen this ID?" | `set` | O(1) membership |
| Look up a record by key / hash join | `dict` | O(1) by key |
| Count occurrences | `collections.Counter` | built-in counting and `most_common` |
| Group records by key | `collections.defaultdict(list)` | no missing-key checks |
| FIFO queue, sliding window, last N items | `collections.deque` | O(1) at both ends, `maxlen` |
| Top-N of a large stream | `heapq` | O(n log k), keeps only k items |
| Fixed, readable record | `dataclass` / `NamedTuple` | named fields, type hints |
| Composite key | `tuple` | hashable |
| Ordered batch to write | `list` | cheap append, keeps order |
| Data larger than memory | generator / iterator | constant memory (Chapter 6) |
| Columnar numeric data | NumPy array / pandas / Arrow | vectorised, compact |

---

### Chapter 2 Review

**Key takeaways**
- Use `set`/`dict` for membership and lookups; a list `in` check inside a loop is O(n²).
- Dicts keep insertion order (3.7+); sets do not.
- Hashable ≈ "immutable all the way down"; equal objects must have equal hashes.
- Shallow copies share nested objects; deep copies do not.
- `sort()`, `reverse()`, `append()` and the like return `None`; they work in place.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| `append` vs `extend`? | `append` adds one object (even a list); `extend` adds each item of an iterable. |
| `remove` vs `pop` vs `del`? | `remove(value)` deletes the first match; `pop(i)` deletes and returns by index; `del lst[i]` deletes by index or slice. |
| `discard` vs `remove` on a set? | `discard` ignores a missing item; `remove` raises `KeyError`. |
| `dict.get` vs `d[key]`? | `get` returns `None`/a default; `d[key]` raises `KeyError`. |
| `popitem()` order? | Removes the last inserted pair (LIFO) since 3.7. |
| Is `{}` a set? | No, it is an empty dict. Use `set()`. |

**Common traps:** `[[0]*3]*2`, `dict.fromkeys(keys, [])`, changing a dict while iterating, relying on set order, `x = x.sort()`.

**Practice exercise:** Given `old = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}]` and `new = [{"id": 2, "v": "B"}, {"id": 3, "v": "c"}]`, use dicts and set algebra to print the inserted, updated and deleted IDs. (Expected: `[3] [2] [1]`.)

---

## 3. Strings

### 3.1 Creation, Indexing, Slicing and Immutability

**Definition:** A `str` is an **immutable sequence of Unicode characters**.

**Syntax:** `'single'`, `"double"`, `"""triple-quoted multi-line"""`, raw strings `r"C:\path\n"` (backslashes are not escapes, which is useful for regex and Windows paths).

**How slicing works:** `text[start:stop:step]`. `start` is included and `stop` is excluded. Negative indexes count from the end. Out-of-range slices never raise errors.

```python
file_name = "orders_2026-10-29.csv"
print(file_name[0], file_name[-1])        # first and last character
print(file_name[:6], file_name[7:17])     # 'orders' and the date
print(file_name[-4:], file_name[::-1][:4])
print(file_name[100:] == "")              # out-of-range slice is just empty

try:
    file_name[0] = "O"
except TypeError as error:
    print("TypeError:", error)
print("O" + file_name[1:])                # build a new string instead
```

**Output:**

```text
o v
orders 2026-10-29
.csv vsc.
True
TypeError: 'str' object does not support item assignment
Orders_2026-10-29.csv
```

**Why it matters for a Data Engineer:** Every "change" creates a new string. Building a large string with `+=` in a loop can copy the data repeatedly (O(n²) in the worst case). Collect the pieces in a list and call `"".join(pieces)` once.

---

### 3.2 String Formatting: f-strings, format() and % formatting

| Style | Example | When to use |
|---|---|---|
| f-string (3.6+) | `f"{table}: {rows:,} rows"` | default choice: readable and fast |
| `str.format` | `"{}: {:,} rows".format(table, rows)` | templates stored in config files |
| `%` formatting | `"%s: %d rows" % (table, rows)` | legacy code, and **`logging` calls** (lazy formatting) |

**Format specification mini-language:** `{value:[fill][align][width][,][.precision][type]}`

```python
table, rows, ratio, amount = "orders", 1234567, 0.0732, 3.14159
print(f"{table}: {rows:,} rows")             # thousands separator
print(f"{ratio:.1%} rejected")               # percentage
print(f"{amount:.2f} | {42:05d} | {'x':>5} | {'x':<5}|")
print(f"{table!r} {rows=}")                  # !r uses repr(); = (3.8+) shows the expression
print("{0}-{1}-{0}".format("a", "b"))
print("%s has %d rows" % (table, rows))
part_number = 7
print(f"part_{part_number:04d}.csv")
```

**Output:**

```text
orders: 1,234,567 rows
7.3% rejected
3.14 | 00042 |     x | x    |
'orders' rows=1234567
a-b-a
orders has 1234567 rows
part_0007.csv
```

**Best practice:** **Never** use any string formatting to build SQL queries with user or data values. Use parameterised queries (see [14.3](#143-executing-parameterized-sql)).

---

### 3.3 Common String Methods

```python
raw = "  Order-ID, Customer Name ,Amount  "
print(raw.strip())                          # remove surrounding whitespace
print(raw.strip().lower().replace(" ", "_"))
print([part.strip() for part in raw.split(",")])
print("a,b,,c".split(","), "a  b".split(), "k=v=w".split("=", 1))
print("|".join(["id", "name", "amount"]))

path = "landing/2026/orders.csv"
print(path.find("orders"), path.find("missing"))   # -1 when not found
try:
    path.index("missing")                           # raises instead of returning -1
except ValueError as error:
    print("ValueError:", error)
print(path.startswith("landing/"), path.endswith((".csv", ".csv.gz")))
print(path.rsplit("/", 1), path.partition("/"))
print(path.removeprefix("landing/"), "orders.csv".removesuffix(".csv"))   # 3.9+
print("abc".upper(), "Hello World".swapcase(), "data engineer".title())
print("ab".center(6, "*"), "7".zfill(3), "a-b-a".count("a"))
```

**Output:**

```text
Order-ID, Customer Name ,Amount
order-id,_customer_name_,amount
['Order-ID', 'Customer Name', 'Amount']
['a', 'b', '', 'c'] ['a', 'b'] ['k', 'v=w']
id|name|amount
13 -1
ValueError: substring not found
True True
['landing/2026', 'orders.csv'] ('landing', '/', '2026/orders.csv')
2026/orders.csv orders
ABC hELLO wORLD Data Engineer
**ab** 007 2
```

**Key differences:**
- `split()` with no argument splits on any run of whitespace and drops empty strings. `split(",")` keeps empty fields.
- `strip("xy")` removes **any of these characters** from both ends, not the substring. To remove a prefix, use `removeprefix`.
- `find` returns `-1` when the substring is missing; `index` raises `ValueError`.

---

### 3.4 String Validation Methods

| Method | True when | Gotcha |
|---|---|---|
| `isdigit()` | all characters are digits | `"-5".isdigit()` and `"3.5".isdigit()` are `False` |
| `isdecimal()` | decimal digits only | strictest numeric check |
| `isnumeric()` | digits including Unicode numerals | `"½".isnumeric()` is `True` |
| `isalpha()` | letters only | `"José".isalpha()` is `True` |
| `isalnum()` | letters or digits | |
| `isspace()` | whitespace only | `"".isspace()` is `False` |
| `isupper()` / `islower()` | cased characters are all upper/lower | |

```python
def is_valid_quantity(raw: str) -> bool:
    """Accept integers like '5', '-2', ' 10 '. isdigit() alone rejects negatives."""
    try:
        int(raw)
    except ValueError:
        return False
    return True


print("42".isdigit(), "-42".isdigit(), is_valid_quantity("-42"), is_valid_quantity("4.2"))
```

**Output:**

```text
True False True False
```

**Best practice:** For numbers, **try the conversion** (EAFP, see [12.15](#1215-eafp-versus-lbyl)) rather than relying on `isdigit()`.

---

### 3.5 Data-Cleaning Examples with Strings

```python
import unicodedata


def normalize_column_name(name: str) -> str:
    """'  Customer Name (EUR) ' -> 'customer_name_eur'"""
    cleaned = "".join(ch if ch.isalnum() else " " for ch in name.strip().lower())
    return "_".join(cleaned.split())


def strip_accents(text: str) -> str:
    """'José Müller' -> 'Jose Muller' (useful for matching names)."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def clean_phone(raw: str) -> str | None:
    """Keep digits only; return None when fewer than 10 digits remain."""
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits if len(digits) >= 10 else None


print(normalize_column_name("  Customer Name (EUR) "))
print(strip_accents("José Müller"))
print(clean_phone("+1 (555) 123-4567"), clean_phone("12-34"))
```

**Output:**

```text
customer_name_eur
Jose Muller
15551234567 None
```

---

### 3.6 Unicode, Encoding and Decoding

**Definition:**
- **Unicode** assigns every character a number (a *code point*): `ord("é") == 233`.
- An **encoding** turns code points into bytes. **UTF-8** is the standard: 1 byte for ASCII, 2–4 bytes for other characters.
- `str.encode(encoding)` turns text into bytes; `bytes.decode(encoding)` turns bytes into text.

**Why it matters for a Data Engineer:** Files from different systems arrive in different encodings (UTF-8, UTF-8 with a BOM from Excel, Windows-1252, Latin-1). Reading with the wrong encoding either raises `UnicodeDecodeError` or silently produces garbage ("mojibake": `cafÃ©`).

```python
text = "café"
utf8_bytes = text.encode("utf-8")
print(ord("é"), utf8_bytes, len(utf8_bytes))
print(utf8_bytes.decode("latin-1"))                  # wrong encoding: mojibake

try:
    utf8_bytes.decode("ascii")
except UnicodeDecodeError as error:
    print("UnicodeDecodeError:", error.reason)

print(b"caf\xe9".decode("utf-8", errors="replace"))   # invalid byte replaced with U+FFFD
bom_file_bytes = "\ufeffid,name".encode("utf-8")
print(bom_file_bytes.decode("utf-8-sig"))             # utf-8-sig strips the Excel BOM
```

**Output:**

```text
233 b'caf\xc3\xa9' 5
cafÃ©
UnicodeDecodeError: ordinal not in range(128)
caf�
id,name
```

**Best practices:**
- Always pass `encoding=` when opening text files. The default depends on the OS (often `cp1252` on Windows).
- Use `encoding="utf-8-sig"` for CSVs exported from Excel. Otherwise the first column name becomes `"\ufeffid"`.
- Use `errors="replace"` only when you knowingly accept data loss. Log how many rows were affected.

---

### 3.7 Regular Expressions (the re Module)

**Definition:** A regular expression is a pattern for matching text.

| Pattern | Meaning | Pattern | Meaning |
|---|---|---|---|
| `\d` | digit | `\D` | non-digit |
| `\w` | letter, digit or `_` | `\s` | whitespace |
| `.` | any character except newline | `^` / `$` | start / end of string |
| `*` / `+` / `?` | 0+, 1+, 0 or 1 | `{3}` / `{2,4}` | exactly 3 / between 2 and 4 |
| `[abc]` / `[^abc]` | one of / none of | `a\|b` | a or b |
| `( )` | capture group | `(?P<name> )` | named group |
| `(?: )` | non-capturing group | `(?=...)` | lookahead (check without consuming) |
| `*?` / `+?` | non-greedy (shortest match) | `\b` | word boundary |

| Function | Behaviour |
|---|---|
| `re.match(p, s)` | matches only at the **start** of `s` |
| `re.search(p, s)` | finds the **first** match anywhere |
| `re.fullmatch(p, s)` | the **entire** string must match (best for validation) |
| `re.findall(p, s)` | list of all matches (or of group tuples if the pattern has groups) |
| `re.finditer(p, s)` | lazy iterator of match objects (memory-friendly) |
| `re.sub(p, repl, s)` | replace matches |
| `re.split(p, s)` | split on a pattern |
| `re.compile(p)` | pre-compile a pattern to reuse it |

```python
import re

text = "Call 123-456-7890 or 987-654-3210"
print(re.findall(r"\d{3}-\d{3}-\d{4}", text))
print(re.sub(r"\d(?=\d{4})", "*", "4111111111111111"))   # mask all but the last 4 digits
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", text)
print(match.group(1) if match else None, match.span() if match else None)
print(re.split(r"[,\s]+", "apple, banana  orange"))
print(re.match(r"\d+", "abc123"), re.search(r"\d+", "abc123").group())
print(bool(re.fullmatch(r"[A-Z]{3}-\d{4}", "ORD-2026")), bool(re.fullmatch(r"[A-Z]{3}-\d{4}", "ORD-2026x")))
print(re.findall(r"<.+>", "<a><b>"), re.findall(r"<.+?>", "<a><b>"))   # greedy vs non-greedy
```

**Output:**

```text
['123-456-7890', '987-654-3210']
************1111
123 (5, 17)
['apple', 'banana', 'orange']
None 123
True False
['<a><b>'] ['<a>', '<b>']
```

**Data Engineering example – parse structured log lines with named groups:**

```python
import re

LOG_PATTERN = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"(?P<level>INFO|WARNING|ERROR) "
    r"(?P<message>.*)$"
)

lines = [
    "2026-10-29 14:05:01 ERROR db timeout after 30s",
    "2026-10-29 14:05:02 INFO batch 7 loaded",
    "malformed line",
]
for line in lines:
    parsed = LOG_PATTERN.match(line)
    if parsed is None:
        print("unparsed:", line)
        continue
    print(parsed["level"], "|", parsed["message"])
```

**Output:**

```text
ERROR | db timeout after 30s
INFO | batch 7 loaded
unparsed: malformed line
```

**Common mistakes:**
- Forgetting the `r` prefix: `"\b"` is a backspace character, `r"\b"` is a word boundary.
- Using `re.match` when you meant `re.search`.
- Using `findall` with groups and expecting full matches (it returns the groups).
- Using regex where a simple `split` or `startswith` is clearer and faster.
- Writing patterns with nested quantifiers like `(a+)+` on untrusted input, which can cause catastrophic backtracking.

---

### 3.8 Representative String Coding Problems

The full worked versions (sample input, step-by-step explanation, complexity, edge cases) are in [20.1](#201-string-problems). Here is a quick reference:

```python
from collections import Counter
from itertools import groupby


def is_palindrome(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def are_anagrams(first: str, second: str) -> bool:
    return Counter(first.replace(" ", "").lower()) == Counter(second.replace(" ", "").lower())


def compress(text: str) -> str:
    """'aabcccccaaa' -> 'a2b1c5a3'; returns the original if not shorter."""
    encoded = "".join(f"{char}{len(list(run))}" for char, run in groupby(text))
    return encoded if len(encoded) < len(text) else text


def longest_unique_substring(text: str) -> int:
    """Length of the longest substring without repeating characters (sliding window)."""
    last_seen: dict[str, int] = {}
    window_start = best = 0
    for index, char in enumerate(text):
        if last_seen.get(char, -1) >= window_start:
            window_start = last_seen[char] + 1
        last_seen[char] = index
        best = max(best, index - window_start + 1)
    return best


print(is_palindrome("A man, a plan, a canal: Panama"), are_anagrams("Listen", "Silent"))
print(compress("aabcccccaaa"), compress("abc"), longest_unique_substring("abcabcbb"))
```

**Output:**

```text
True True
a2b1c5a3 abc 3
```

**How the sliding window works** (`"abcabcbb"`): keep a window with no repeated character. When a character repeats **inside** the current window, move the window start just past its previous position. Each character is processed once, so it is O(n) instead of O(n²) for checking all substrings. The same technique powers rolling metrics and sessionisation.

---

### Chapter 3 Review

**Key takeaways**
- Strings are immutable. Build big strings with `"".join(...)`.
- Prefer f-strings, but use `%s`-style lazy arguments in `logging` calls and **never** format SQL.
- `find` returns -1; `index` raises. `strip(chars)` removes characters, not substrings.
- Always specify encodings; use `utf-8-sig` for Excel CSVs.
- Use `re.fullmatch` for validation and `re.compile` for patterns used in loops.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Why are strings immutable? | Safety (sharing, hashing as dict keys) and the ability to intern/cache them. |
| `str` vs `bytes`? | Text (Unicode) vs raw binary; convert with `encode`/`decode`. |
| `re.match` vs `re.search`? | Start of string vs anywhere. |
| Greedy vs non-greedy? | `.*` takes as much as possible; `.*?` as little as possible. |
| How to reverse a string? | `text[::-1]` or `"".join(reversed(text))`. |

**Common traps:** `"-5".isdigit()` is `False`; `split(",")` keeps empty fields; a BOM in the first CSV header; a missing `r` prefix in regex.

**Practice exercise:** Write `mask_email("john.smith@example.com")` that returns `"j********h@example.com"` (keep the first and last character of the local part). Handle local parts with fewer than 3 characters by masking everything except the first character.

---

## 4. Conditionals and Loops

### 4.1 if, elif and else

**Definition:** Runs the first block whose condition is truthy. `elif` and `else` are optional.

```python
def classify_file(size_bytes: int) -> str:
    if size_bytes == 0:
        return "empty"
    elif size_bytes < 1_000_000:
        return "small"
    else:
        return "large"


status = "ok" if classify_file(500) != "empty" else "skip"   # conditional expression
print(classify_file(0), classify_file(500), classify_file(5_000_000), status)
```

**Output:**

```text
empty small large ok
```

**Structural pattern matching (3.10+)** – useful for routing records by shape:

```python
def route(event: dict) -> str:
    match event:
        case {"type": "order", "amount": amount} if amount > 1000:
            return "high_value_orders"
        case {"type": "order"}:
            return "orders"
        case {"type": "refund" | "chargeback"}:
            return "refunds"
        case _:
            return "dead_letter"


print(route({"type": "order", "amount": 5000}), route({"type": "order", "amount": 5}))
print(route({"type": "chargeback"}), route({"kind": "unknown"}))
```

**Output:**

```text
high_value_orders orders
refunds dead_letter
```

**Best practice:** Replace long `if/elif` chains that map a value to an action with a **dict lookup**, e.g. `handlers = {"csv": read_csv, "json": read_json}` and then `handlers[file_type](path)`.

---

### 4.2 for and while Loops

**Definition:**
- `for` iterates over any **iterable** (list, dict, file, generator…).
- `while` repeats while a condition is truthy. Use it when the number of iterations is unknown (polling, pagination, retries).

```python
for column in ["id", "name"]:
    print("column:", column)

for key, value in {"rows": 10, "errors": 0}.items():
    print(key, value)

attempt = 0
while attempt < 3:
    attempt += 1
print("attempts:", attempt)
```

**Output:**

```text
column: id
column: name
rows 10
errors 0
attempts: 3
```

**Data Engineering example – polling until a job finishes (with a safety limit):**

```python
import time

statuses = iter(["RUNNING", "RUNNING", "SUCCEEDED"])   # stands in for an API call


def get_job_status() -> str:
    return next(statuses)


max_polls, poll_seconds = 10, 0.01
for poll_number in range(1, max_polls + 1):
    status = get_job_status()
    if status in {"SUCCEEDED", "FAILED"}:
        break
    time.sleep(poll_seconds)
print(f"final status {status} after {poll_number} polls")
```

**Output:**

```text
final status SUCCEEDED after 3 polls
```

**Common mistake:** `while True` loops with no exit limit. Always have a timeout or a maximum attempt count in production.

---

### 4.3 range(), enumerate() and zip()

```python
print(list(range(5)), list(range(2, 10, 3)), list(range(5, 0, -2)))

for line_number, line in enumerate(["id,name", "1,Asha"], start=1):
    print(line_number, line)

header = ["id", "name", "city"]
row = ["1", "Asha", "Pune"]
print(dict(zip(header, row)))

print(list(zip([1, 2, 3], ["a", "b"])))          # stops at the shortest
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))  # 3.10+: fail on length mismatch
except ValueError as error:
    print("ValueError:", error)

from itertools import zip_longest
print(list(zip_longest([1, 2, 3], ["a"], fillvalue=None)))
```

**Output:**

```text
[0, 1, 2, 3, 4] [2, 5, 8] [5, 3, 1]
1 id,name
2 1,Asha
{'id': '1', 'name': 'Asha', 'city': 'Pune'}
[(1, 'a'), (2, 'b')]
ValueError: zip() argument 2 is shorter than argument 1
[(1, 'a'), (2, None), (3, None)]
```

**Why it matters for a Data Engineer:** `dict(zip(header, row))` turns CSV rows into records. A short row silently loses columns with plain `zip`, so use `strict=True` (3.10+) or validate row lengths. `enumerate(..., start=1)` gives line numbers for error messages ("bad value on line 5,231").

---

### 4.4 break, continue, pass and the Loop else Clause

| Statement | Effect |
|---|---|
| `break` | exit the innermost loop immediately |
| `continue` | skip to the next iteration |
| `pass` | do nothing (placeholder for an empty block) |
| `for/while ... else` | the `else` runs **only if the loop finished without `break`** |

```python
rows = ["1,ok", "", "# comment", "2,ok", "STOP", "3,ok"]
loaded = []
for row in rows:
    if not row or row.startswith("#"):
        continue                      # skip blanks and comments
    if row == "STOP":
        break
    loaded.append(row)
print(loaded)

for column in ["id", "name"]:
    if column == "email":
        print("found email")
        break
else:
    print("email column missing")     # runs because no break happened


class PlaceholderLoader:
    pass                              # empty class body
```

**Output:**

```text
['1,ok', '2,ok']
email column missing
```

**Interview question:** *When does a loop's `else` run?* When the loop ends normally (the iterable is exhausted or the `while` condition becomes false), but **not** when it exits via `break`. It is handy for "search, and if not found…" logic.

---

### 4.5 Nested Loops

**Definition:** A loop inside a loop. The inner loop runs completely for each iteration of the outer loop. Work is O(n × m).

```python
regions = ["EU", "US"]
products = ["A", "B"]
for region in regions:
    for product in products:
        print(region, product, end="; ")
print()
```

**Output:**

```text
EU A; EU B; US A; US B; 
```

**Why it matters for a Data Engineer:** A nested loop that matches rows between two datasets is a "nested-loop join", which is O(n × m). Replacing the inner loop with a dict lookup makes it O(n + m) (a **hash join**, see [20.6](#206-grouping-joining-and-aggregation-problems)). To exit both loops at once, put them in a function and `return`.

---

### 4.6 Comprehensions

**Definition:** A compact expression that builds a list, set or dict from an iterable, optionally with a filter.

**Syntax:**

```text
[expression for item in iterable if condition]          # list
{expression for item in iterable if condition}          # set
{key_expr: value_expr for item in iterable if condition} # dict
(expression for item in iterable if condition)          # generator expression (lazy)
```

```python
amounts = [120, -5, 0, 300]
positive = [amount for amount in amounts if amount > 0]                 # filter: if at the END
labels = ["refund" if amount < 0 else "sale" for amount in amounts]    # choose: if/else at the FRONT
matrix = [[1, 2], [3, 4]]
flat = [value for row in matrix for value in row]                      # same order as nested loops
lengths = {len(word) for word in ["a", "bb", "cc"]}                    # set comprehension
inverted = {code: name for name, code in {"India": "IN", "Spain": "ES"}.items()}
total_squares = sum(value * value for value in range(1_000))           # generator: no list built
print(positive, labels, flat, lengths, inverted, total_squares)
```

**Output:**

```text
[120, 300] ['sale', 'refund', 'sale', 'sale'] [1, 2, 3, 4] {1, 2} {'IN': 'India', 'ES': 'Spain'} 332833500
```

**Data Engineering example – clean a batch of records:**

```python
raw_records = [
    {"id": "1", "email": " A@X.COM "},
    {"id": "2", "email": ""},
    {"id": "3", "email": "c@y.com"},
]
cleaned = [
    {"id": int(record["id"]), "email": record["email"].strip().lower()}
    for record in raw_records
    if record["email"].strip()
]
email_by_id = {record["id"]: record["email"] for record in cleaned}
print(cleaned)
print(email_by_id)
```

**Output:**

```text
[{'id': 1, 'email': 'a@x.com'}, {'id': 3, 'email': 'c@y.com'}]
{1: 'a@x.com', 3: 'c@y.com'}
```

---

### 4.7 Generator Expressions

**Definition:** Like a list comprehension but with parentheses. It produces items **lazily**, one at a time, and can be consumed **once**.

```python
import sys

as_list = [value for value in range(1_000_000)]
as_generator = (value for value in range(1_000_000))
print(sys.getsizeof(as_list) > 1_000_000, sys.getsizeof(as_generator) < 1_000)
print(sum(as_generator), sum(as_generator))   # second sum: already exhausted
```

**Output:**

```text
True True
499999500000 0
```

**When to use which:** Use a list when you need to index, reuse or `len()` the result. Use a generator expression when you only stream the items once into `sum`, `max`, `any`, `"".join`, a file write or another pipeline stage. More in Chapter 6.

---

### 4.8 When Comprehensions Reduce Readability

Comprehensions should be **one idea per line**. Switch to a normal loop when:
- there is more than one level of nesting plus conditions,
- you need `try/except` for each item (comprehensions cannot contain statements),
- you need side effects (logging, writing). Never write `[print(x) for x in items]`,
- the expression needs a comment to be understood.

```python
# Hard to read
pairs = [(a, b) for a in range(4) if a % 2 for b in range(a) if (a + b) % 3]

# Clearer
pairs_clear = []
for a in range(4):
    if a % 2 == 0:
        continue
    for b in range(a):
        if (a + b) % 3:
            pairs_clear.append((a, b))
print(pairs == pairs_clear, pairs)
```

**Output:**

```text
True [(1, 0), (3, 1), (3, 2)]
```

---

### 4.9 Representative Looping Problems

```python
def fizzbuzz(limit: int) -> list[str]:
    output = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            output.append("FizzBuzz")
        elif number % 3 == 0:
            output.append("Fizz")
        elif number % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(number))
    return output


def running_total(values: list[int]) -> list[int]:
    totals, current = [], 0
    for value in values:
        current += value
        totals.append(current)
    return totals


def pairs_with_sum(values: list[int], target: int) -> list[tuple[int, int]]:
    """Unique value pairs adding up to target, O(n) using a set."""
    seen, pairs = set(), set()
    for value in values:
        if target - value in seen:
            pairs.add((min(value, target - value), max(value, target - value)))
        seen.add(value)
    return sorted(pairs)


print(fizzbuzz(15)[-3:], running_total([5, 10, -3]), pairs_with_sum([1, 5, 3, 7, 5, 9], 10))
```

**Output:**

```text
['13', '14', 'FizzBuzz'] [5, 15, 12] [(1, 9), (3, 7), (5, 5)]
```

---

### Chapter 4 Review

**Key takeaways**
- `for` iterates over any iterable; `while` needs a guaranteed exit.
- `enumerate` for line numbers; `zip(strict=True)` to catch length mismatches (3.10+).
- A loop's `else` runs only when no `break` happened.
- Comprehensions: `if` at the end filters; `if/else` at the front chooses a value.
- A generator expression is lazy and single-use.
- Replace nested-loop matching with dict/set lookups.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| `break` vs `continue`? | Exit the loop vs skip to the next iteration. |
| What is `pass` for? | A syntactic placeholder that does nothing. |
| List comprehension vs generator expression? | Builds the full list in memory vs yields lazily, single pass. |
| Are comprehensions faster than loops? | Usually somewhat, because appending is optimised, but readability matters more. |
| How do you exit nested loops? | Put them in a function and `return`, or use a flag. |

**Common traps:** changing a list while looping over it; `[print(x) for x in xs]`; reusing an exhausted generator; `zip` silently truncating.

**Practice exercise:** Given `lines = ["a,1", "b,x", "", "c,3"]`, write a loop that skips blank lines, converts the second field to `int`, collects rejects as `(line_number, line)` and prints `{'a': 1, 'c': 3}` and `[(2, 'b,x')]`.

---

## 5. Functions

### 5.1 Defining and Calling Functions

**Definition:** A function is a named, reusable block of code. `def` creates a function object and binds it to a name. A function without an explicit `return` returns `None`.

**Syntax:**

```text
def function_name(parameters) -> return_type:
    """Docstring: what it does, arguments, return value."""
    body
    return value
```

```python
def row_count_message(table: str, rows: int) -> str:
    """Return a human-readable load summary."""
    return f"{table}: {rows} rows loaded"


def log_only(message: str) -> None:
    print(message)


result = log_only(row_count_message("orders", 42))
print(result)
```

**Output:**

```text
orders: 42 rows loaded
None
```

**Why it matters for a Data Engineer:** Small, single-purpose functions (`extract`, `validate_row`, `transform`, `load_batch`) can each be unit tested and reused across pipelines.

---

### 5.2 Parameters versus Arguments

- **Parameter** – the variable name in the function **definition** (`def load(path)` → `path`).
- **Argument** – the actual value passed in the **call** (`load("orders.csv")` → `"orders.csv"`).

---

### 5.3 Positional, Keyword and Default Arguments

```python
def connect(host: str, port: int = 5432, timeout: int = 30) -> str:
    return f"{host}:{port} (timeout={timeout}s)"


print(connect("db1"))                         # defaults used
print(connect("db1", 6543))                   # positional
print(connect("db1", timeout=5))              # keyword: skip port, clear meaning
print(connect(port=1, host="db2"))            # keyword order does not matter
```

**Output:**

```text
db1:5432 (timeout=30s)
db1:6543 (timeout=30s)
db1:5432 (timeout=5s)
db2:1 (timeout=30s)
```

**The mutable default argument pitfall (very common in interviews):**

Default values are evaluated **once, when the function is defined**, not on each call. A mutable default is therefore shared by every call.

```python
def add_bad(item, bucket=[]):
    bucket.append(item)
    return bucket


def add_good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket


print(add_bad(1), add_bad(2))      # same list reused!
print(add_good(1), add_good(2))
print(add_bad.__defaults__)        # the shared default is stored on the function
```

**Output:**

```text
[1, 2] [1, 2]
[1] [2]
([1, 2],)
```

**Why it matters for a Data Engineer:** In a long-running worker (Airflow, Celery, a web service) the shared default keeps growing. That leaks data between jobs and slowly leaks memory. The same rule applies to `dataclasses` (use `field(default_factory=list)`).

**Related trap:** `def run(ts=datetime.now())` freezes the timestamp at import time. Use `ts=None` and compute it inside.

---

### 5.4 Return Values, Multiple Returns and Argument Passing

**Multiple return values** are really one tuple, unpacked by the caller:

```python
def split_valid(values: list[str]) -> tuple[list[int], list[str]]:
    good: list[int] = []
    bad: list[str] = []
    for value in values:
        if value.isdigit():
            good.append(int(value))
        else:
            bad.append(value)
    return good, bad


valid, rejected = split_valid(["1", "x", "3"])
print(valid, rejected, type(split_valid([])).__name__)
```

**Output:**

```text
[1, 3] ['x'] tuple
```

**Argument passing – "pass-by-object-reference":** The function receives a **reference to the same object** the caller passed.
- **Mutating** the object (`append`, `update`, item assignment) is visible to the caller.
- **Rebinding** the parameter name (`param = ...`) is not.

```python
def mutate(records: list) -> None:
    records.append("added")


def rebind(records: list) -> None:
    records = ["replaced"]


batch = ["original"]
mutate(batch)
rebind(batch)
print(batch)
```

**Output:**

```text
['original', 'added']
```

**Best practice:** Transformation functions should **return new objects** instead of mutating their inputs (`{**record, "amount": float(record["amount"])}`). Then a retry or another consumer still sees the original data.

---

### 5.5 *args and **kwargs

- `*args` collects extra **positional** arguments into a **tuple**.
- `**kwargs` collects extra **keyword** arguments into a **dict**.
- At call time, `*` unpacks an iterable into positional arguments and `**` unpacks a dict into keyword arguments.

```python
def log_event(event: str, *tags: str, **fields: object) -> str:
    return f"{event} tags={tags} fields={fields}"


print(log_event("load", "daily", "orders", rows=10, status="ok"))

options = {"rows": 5}
labels = ["hourly"]
print(log_event("load", *labels, **options))
```

**Output:**

```text
load tags=('daily', 'orders') fields={'rows': 10, 'status': 'ok'}
load tags=('hourly',) fields={'rows': 5}
```

**Why it matters for a Data Engineer:** Wrapper functions and decorators accept `*args, **kwargs` so they can wrap any function. Utility functions pass options through to libraries: `read_file(path, **reader_options)` → `pd.read_csv(path, **reader_options)`.

**Common mistake:** Accepting `**kwargs` and never validating it. Then typos like `timeuot=5` are silently ignored.

---

### 5.6 Keyword-Only and Positional-Only Parameters

**Syntax:** `def f(pos_only, /, normal, *, kw_only)`
- Parameters **before `/`** are positional-only (3.8+).
- Parameters **after `*`** (or after `*args`) are keyword-only.

```python
def write_table(frame_name, /, table, *, mode="append", partition=None):
    return f"{frame_name} -> {table} mode={mode} partition={partition}"


print(write_table("df", "sales", mode="overwrite", partition="2026-10-29"))

try:
    write_table("df", "sales", "overwrite")
except TypeError as error:
    print("TypeError:", error)
```

**Output:**

```text
df -> sales mode=overwrite partition=2026-10-29
TypeError: write_table() takes 2 positional arguments but 3 were given
```

**Why it matters for a Data Engineer:** Keyword-only flags prevent dangerous, unreadable calls like `write_table(df, "sales", True)`. Is `True` "overwrite" or "create"? Forcing `mode="overwrite"` makes destructive behaviour explicit.

---

### 5.7 Variable Scope and the LEGB Rule

**Definition:** When Python looks up a name it searches four scopes in order:
1. **L**ocal – inside the current function
2. **E**nclosing – inside any outer (enclosing) function
3. **G**lobal – at the module level
4. **B**uilt-in – names like `len`, `print`, `Exception`

```python
batch_size = 100                    # global


def outer():
    batch_size = 50                 # enclosing (for inner)

    def inner():
        return batch_size           # found in the enclosing scope
    return inner()


print(outer(), batch_size, len("abc"))   # len comes from the built-in scope
```

**Output:**

```text
50 100 3
```

**Common mistake – `UnboundLocalError`:** assigning to a name anywhere in a function makes it local for the **whole** function.

```python
counter = 0


def increment():
    try:
        counter += 1                # counter is local here, but not yet assigned
    except UnboundLocalError as error:
        return f"UnboundLocalError: {error}"


print(increment())
```

**Output:**

```text
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

(The exact message wording differs slightly before Python 3.11.)

---

### 5.8 global and nonlocal

- `global name` – assignments inside the function rebind the **module-level** name.
- `nonlocal name` – assignments rebind the name in the nearest **enclosing function**.

```python
processed_files = 0


def mark_processed() -> None:
    global processed_files
    processed_files += 1


def make_counter():
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


mark_processed()
mark_processed()
next_id = make_counter()
print(processed_files, next_id(), next_id(), next_id())
```

**Output:**

```text
2 1 2 3
```

**Best practice:** Avoid `global` state in pipelines. It makes functions hard to test and unsafe with threads. Pass values in and return results, or keep state in an object.

---

### 5.9 Lambda Functions

**Definition:** A small anonymous function written as one expression: `lambda parameters: expression`.

```python
orders = [
    {"id": 1, "region": "US", "amount": 50},
    {"id": 2, "region": "EU", "amount": 200},
    {"id": 3, "region": "EU", "amount": 75},
]
by_amount_desc = sorted(orders, key=lambda order: order["amount"], reverse=True)
print([order["id"] for order in by_amount_desc])
```

**Output:**

```text
[2, 3, 1]
```

**When not to use:** Do not assign a lambda to a name (`clean = lambda s: s.strip()`). Use `def`, which gives a proper name in tracebacks. Lambdas cannot contain statements (`try`, assignments other than `:=`).

---

### 5.10 map(), filter(), reduce(), sorted(), any() and all()

| Function | Returns | Notes |
|---|---|---|
| `map(func, iterable)` | lazy iterator of `func(item)` | often clearer as a comprehension |
| `filter(func, iterable)` | lazy iterator of items where `func(item)` is truthy | `filter(None, xs)` drops falsy values |
| `functools.reduce(func, iterable[, initial])` | one accumulated value | prefer `sum`, `max`, `math.prod` where they exist |
| `sorted(iterable, key=None, reverse=False)` | **new** list | stable; works on any iterable |
| `any(iterable)` / `all(iterable)` | bool | short-circuit; `all([])` is `True`, `any([])` is `False` |
| `min` / `max` (`key=`, `default=`) | one item | `default` avoids `ValueError` on empty input |

```python
from functools import reduce
from operator import itemgetter

print(list(map(str.upper, ["eu", "us"])))
print(list(filter(None, [0, 1, "", "x", None])))
print(reduce(lambda total, value: total * value, [1, 2, 3, 4], 1))
print(any(amount < 0 for amount in [5, -1]), all([]), any([]))
print(max([], default=0), min(["bb", "a", "ccc"], key=len))

employees = [
    {"dept": "IT", "name": "Bo", "salary": 70},
    {"dept": "HR", "name": "Al", "salary": 60},
    {"dept": "IT", "name": "Cy", "salary": 90},
]
by_dept_then_salary_desc = sorted(employees, key=lambda emp: (emp["dept"], -emp["salary"]))
print([emp["name"] for emp in by_dept_then_salary_desc])
print([emp["name"] for emp in sorted(employees, key=itemgetter("name"))])
```

**Output:**

```text
['EU', 'US']
[1, 'x']
24
True True False
0 a
['Al', 'Cy', 'Bo']
['Al', 'Bo', 'Cy']
```

**Multi-key sorting where a key cannot be negated (e.g. strings descending):** sort twice, using the fact that `sorted` is **stable**. Sort by the secondary key first, then by the primary key.

```python
people = [("IT", "Bo"), ("HR", "Al"), ("IT", "Cy")]
step1 = sorted(people, key=lambda person: person[1], reverse=True)   # name descending
step2 = sorted(step1, key=lambda person: person[0])                   # dept ascending
print(step2)
```

**Output:**

```text
[('HR', 'Al'), ('IT', 'Cy'), ('IT', 'Bo')]
```

---

### 5.11 First-Class Functions

**Definition:** Functions are objects. They can be assigned to variables, stored in containers, passed as arguments and returned from other functions.

**Data Engineering example – a configuration-driven transform registry:**

```python
def trim(value: str) -> str:
    return value.strip()


def upper(value: str) -> str:
    return value.upper()


TRANSFORMS = {"trim": trim, "upper": upper}
column_config = {"country": ["trim", "upper"], "name": ["trim"]}

row = {"country": " in ", "name": " Asha "}
for column, steps in column_config.items():
    for step in steps:
        row[column] = TRANSFORMS[step](row[column])
print(row)
```

**Output:**

```text
{'country': 'IN', 'name': 'Asha'}
```

---

### 5.12 Higher-Order Functions

**Definition:** A function that **takes** a function as an argument or **returns** one. `map`, `filter`, `sorted(key=...)` and decorators are all higher-order functions.

```python
from typing import Callable


def apply_to_column(rows: list[dict], column: str, func: Callable[[object], object]) -> list[dict]:
    """Return new rows with func applied to one column (inputs are not mutated)."""
    return [{**row, column: func(row[column])} for row in rows]


rows = [{"amount": "10.5"}, {"amount": "3"}]
print(apply_to_column(rows, "amount", float), rows)
```

**Output:**

```text
[{'amount': 10.5}, {'amount': 3.0}] [{'amount': '10.5'}, {'amount': '3'}]
```

---

### 5.13 Closures

**Definition:** A closure is an inner function that **remembers variables from its enclosing scope** even after the outer function has returned. The remembered variables are stored in the function's `__closure__` cells.

```python
def make_threshold_validator(column: str, minimum: float):
    def validate(row: dict) -> bool:
        return row.get(column) is not None and row[column] >= minimum
    return validate


non_negative_amount = make_threshold_validator("amount", 0)
adult = make_threshold_validator("age", 18)
print(non_negative_amount({"amount": 5}), non_negative_amount({"amount": -1}), adult({"age": 17}))
print(non_negative_amount.__closure__[0].cell_contents)
```

**Output:**

```text
True False False
amount
```

**Late-binding trap (a classic interview question):** closures look up variables **when called**, not when created.

```python
late = [lambda value: value * factor for factor in range(3)]
print([func(10) for func in late])                 # every lambda sees factor == 2

early = [lambda value, factor=factor: value * factor for factor in range(3)]
print([func(10) for func in early])                # default argument captures the value now
```

**Output:**

```text
[20, 20, 20]
[0, 10, 20]
```

**Why it matters for a Data Engineer:** Closures build configurable validators and transformers, and they are the basis of decorators (Chapter 11). The late-binding trap appears when generating Airflow tasks or callbacks in a loop.

---

### 5.14 Recursion

**Definition:** A function that calls itself on a smaller version of the problem. It needs:
1. a **base case** that stops the recursion, and
2. a **recursive step** that moves toward the base case.

```python
import sys


def factorial(number: int) -> int:
    return 1 if number <= 1 else number * factorial(number - 1)


def sum_of_digits(number: int) -> int:
    return 0 if number == 0 else number % 10 + sum_of_digits(number // 10)


def flatten_list(nested: list) -> list:
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def hanoi(disks: int, source: str = "A", target: str = "C", spare: str = "B", moves=None) -> list:
    """Return the moves to transfer `disks` disks; always 2**disks - 1 moves."""
    moves = [] if moves is None else moves
    if disks == 0:
        return moves
    hanoi(disks - 1, source, spare, target, moves)    # move the smaller disks out of the way
    moves.append((disks, source, target))            # move the largest disk
    hanoi(disks - 1, spare, target, source, moves)    # put the smaller disks back on top
    return moves


print(factorial(5), sum_of_digits(1234), flatten_list([1, [2, [3, [4]]], 5]))
moves = hanoi(3)
print(len(moves), moves[:3])
print(sys.getrecursionlimit())
```

**Output:**

```text
120 10 [1, 2, 3, 4, 5]
7 [(1, 'A', 'C'), (2, 'A', 'B'), (1, 'C', 'B')]
1000
```

**How it works:** Each call adds a **stack frame**. CPython's default limit is about 1000 frames (`RecursionError` beyond that), and Python does **not** optimise tail calls. Deeply nested inputs (a 5,000-level JSON tree, a long parent-child chain) should be processed **iteratively** with an explicit stack:

```python
def flatten_list_iterative(nested: list) -> list:
    stack, flat = [iter(nested)], []
    while stack:
        for item in stack[-1]:
            if isinstance(item, list):
                stack.append(iter(item))
                break
            flat.append(item)
        else:
            stack.pop()
    return flat


deep = current = []
for _ in range(5_000):
    child = []
    current.append(child)
    current = child
current.append("leaf")
print(flatten_list_iterative(deep), flatten_list_iterative([1, [2, [3]], 4]))
```

**Output:**

```text
['leaf'] [1, 2, 3, 4]
```

**Why it matters for a Data Engineer:** Tree-shaped data is everywhere: nested JSON, folder hierarchies, org charts, bill-of-materials. Know both the recursive and the iterative solution.

---

### 5.15 Function Annotations and Type Hints

**Definition:** Annotations describe expected types. They are stored in `__annotations__` and **not enforced at run time**. Static checkers (mypy, pyright) and IDEs use them.

```python
from typing import Any, Callable, Iterable, Iterator, Optional, TypedDict


class OrderRow(TypedDict):
    order_id: int
    amount: float


def parse_rows(lines: Iterable[str]) -> Iterator[OrderRow]:
    for line in lines:
        order_id, amount = line.split(",")
        yield {"order_id": int(order_id), "amount": float(amount)}


def first_or_none(values: list[int]) -> Optional[int]:     # same as int | None (3.10+)
    return values[0] if values else None


Handler = Callable[[dict[str, Any]], None]                 # a type alias

print(list(parse_rows(["1,9.5"])), first_or_none([]))
print(first_or_none.__annotations__)
```

**Output:**

```text
[{'order_id': 1, 'amount': 9.5}] None
{'values': list[int], 'return': typing.Optional[int]}
```

**Version notes:** `list[int]` and `dict[str, int]` in annotations need 3.9+. `int | None` needs 3.10+, or `from __future__ import annotations` on older versions. Before 3.9, use `typing.List` and `typing.Dict`.

**Best practice:** Type-hint all public functions in pipeline code and run mypy in CI. Validate **external data at run time** with explicit checks or a library like pydantic. Hints do not check incoming JSON.

---

### 5.16 Pure Functions and Side Effects

**Definition:**
- A **pure function** always returns the same output for the same input and changes nothing outside itself.
- A **side effect** is anything else: writing files, calling APIs, changing globals, mutating arguments, logging, reading the clock.

```python
from datetime import date


def add_tax(amount: float, rate: float) -> float:          # pure: easy to test
    return round(amount * (1 + rate), 2)


def build_output_path(run_date: date, table: str) -> str:   # pure: the date is passed in
    return f"s3://lake/{table}/dt={run_date:%Y-%m-%d}/"


print(add_tax(100, 0.18), build_output_path(date(2026, 10, 29), "sales"))
```

**Output:**

```text
118.0 s3://lake/sales/dt=2026-10-29/
```

**Why it matters for a Data Engineer:** Keep transformation logic **pure** and push I/O to the edges ("functional core, imperative shell"). Pure transforms are trivially unit tested, safe to retry and safe to parallelise. Passing `run_date` in, instead of calling `date.today()` inside, makes backfills (re-running for past dates) work.

---

### Chapter 5 Review

**Key takeaways**
- Default argument values are evaluated once. Never use a mutable default.
- Arguments are passed by object reference: mutation is visible to the caller, rebinding is not.
- `*args` is a tuple, `**kwargs` is a dict. Use `*` to force keyword-only flags.
- LEGB decides name lookup. Assigning a name makes it local for the whole function.
- Closures capture variables, not values (late binding).
- Recursion needs a base case. Python's limit is ~1000 frames, so go iterative for deep data.
- Keep transforms pure; pass dates and config in.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| What does a function return without `return`? | `None`. |
| `*args` vs `**kwargs`? | Extra positional arguments as a tuple vs extra keyword arguments as a dict. |
| What is a closure? | An inner function that remembers variables from its enclosing scope. |
| `global` vs `nonlocal`? | Rebind a module-level name vs a name in the enclosing function. |
| Are type hints enforced? | No; they are checked by static tools only. |
| Does Python do tail-call optimisation? | No. |
| What is a higher-order function? | One that takes or returns a function. |

**Common traps:** mutable defaults; `datetime.now()` as a default; late binding in loops; `UnboundLocalError`; lambdas assigned to names.

**Practice exercise:** Write `make_range_validator(column, low, high)` that returns a function checking `low <= row[column] <= high` and returning `False` for a missing or `None` value. Create validators for `age` (0–120) and `discount` (0–1) and test them on three rows.

---

## 6. Iterators and Generators

### 6.1 Iterable versus Iterator

**Definition:**
- An **iterable** is anything you can loop over. It implements `__iter__()`, which returns an iterator. Examples: `list`, `tuple`, `str`, `dict`, `set`, file objects, `range`.
- An **iterator** is the object that produces values one at a time. It implements `__next__()` (raising `StopIteration` when finished) **and** `__iter__()` returning itself. An iterator is **single-pass**: once exhausted, it stays exhausted.

**Analogy:** an iterable is a **book**; an iterator is a **bookmark** in that book. You can create many bookmarks for one book, but each bookmark only moves forward.

| | Iterable (e.g. list) | Iterator (e.g. generator, file) |
|---|---|---|
| Can loop multiple times | Yes | No (single pass) |
| Supports `len()` / indexing | Often | No |
| Memory | Usually holds all items | Produces items on demand |

---

### 6.2 iter(), next() and the Iterator Protocol

**How a `for` loop really works:**

```python
regions = ["EU", "US"]
iterator = iter(regions)          # calls regions.__iter__()
print(type(iterator).__name__)
print(next(iterator), next(iterator))
print(next(iterator, "done"))     # default instead of StopIteration

# What `for region in regions:` does internally
iterator = iter(regions)
while True:
    try:
        region = next(iterator)
    except StopIteration:
        break
    print("processing", region)
```

**Output:**

```text
list_iterator
EU US
done
processing EU
processing US
```

**Interview question:** *Is a list an iterator?*
**Answer:** No. A list is an **iterable**: `iter(list)` returns a new `list_iterator` each time, which is why you can loop over a list many times. `next([1, 2])` raises `TypeError`.

---

### 6.3 Creating a Custom Iterator

```python
class CountUp:
    """Iterator over integers start..end-1 (single-pass)."""

    def __init__(self, start: int, end: int) -> None:
        self.current, self.end = start, end

    def __iter__(self) -> "CountUp":
        return self

    def __next__(self) -> int:
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


class PageRange:
    """Reusable ITERABLE: each loop gets a fresh generator."""

    def __init__(self, pages: int) -> None:
        self.pages = pages

    def __iter__(self):
        for page in range(1, self.pages + 1):
            yield page


counter = CountUp(1, 4)
print(list(counter), list(counter))     # second pass is empty
pages = PageRange(3)
print(list(pages), list(pages))         # iterable can be reused
```

**Output:**

```text
[1, 2, 3] []
[1, 2, 3] [1, 2, 3]
```

**Best practice:** If users of your class need to loop more than once, make it an **iterable** whose `__iter__` returns a new generator (like `PageRange`), not an iterator.

---

### 6.4 Generator Functions and yield

**Definition:** A function containing `yield` is a **generator function**. Calling it does **not** run the body. It returns a generator object (an iterator). Each `next()` runs the body until the next `yield`, hands out that value, and **pauses**, keeping all local variables. When the function ends, `StopIteration` is raised.

```python
def numbered(prefix: str):
    print("  started")
    yield f"{prefix}-1"
    print("  resumed")
    yield f"{prefix}-2"
    print("  finishing")


generator = numbered("batch")
print("created, nothing ran yet")
print(next(generator))
print(next(generator))
print(next(generator, "exhausted"))
```

**Output:**

```text
created, nothing ran yet
  started
batch-1
  resumed
batch-2
  finishing
exhausted
```

**`return` inside a generator** ends iteration. The returned value is attached to `StopIteration.value` (used by `yield from`).

---

### 6.5 Generator Expressions

`(expression for item in iterable if condition)` – a lazy, single-use generator in one line. When it is the only argument to a function, the extra parentheses can be dropped: `sum(row["amount"] for row in rows)`.

---

### 6.6 yield from

**Definition:** `yield from sub_iterable` yields every item from another iterable or generator and returns the sub-generator's return value.

```python
def read_partition(name: str, rows: int):
    for row_number in range(1, rows + 1):
        yield f"{name}:{row_number}"
    return rows                                 # becomes the value of `yield from`


def read_all(partitions: dict[str, int]):
    total = 0
    for name, rows in partitions.items():
        total += yield from read_partition(name, rows)
    print("total rows:", total)


print(list(read_all({"p1": 2, "p2": 1})))
```

**Output:**

```text
total rows: 3
['p1:1', 'p1:2', 'p2:1']
```

---

### 6.7 send(), close() and Generator State

- `generator.send(value)` resumes the generator and makes the paused `yield` expression evaluate to `value`. The generator must first be "primed" with `next()`.
- `generator.close()` raises `GeneratorExit` at the paused `yield`, so `finally` blocks run (cleanup).
- `generator.throw(exc)` raises an exception at the paused `yield`.
- `inspect.getgeneratorstate()` reports `GEN_CREATED`, `GEN_RUNNING`, `GEN_SUSPENDED` or `GEN_CLOSED`.

```python
import inspect


def running_average():
    total = count = 0
    average = None
    try:
        while True:
            value = yield average
            total += value
            count += 1
            average = total / count
    finally:
        print("cleanup: average generator closed")


averager = running_average()
print(inspect.getgeneratorstate(averager))
next(averager)                                  # prime: run to the first yield
print(averager.send(10), averager.send(20), averager.send(60))
print(inspect.getgeneratorstate(averager))
averager.close()
print(inspect.getgeneratorstate(averager))
```

**Output:**

```text
GEN_CREATED
10.0 15.0 30.0
GEN_SUSPENDED
cleanup: average generator closed
GEN_CLOSED
```

**Interview note:** `send()`-based coroutines were the foundation of the older `asyncio` style. Modern code uses `async def` / `await` (Chapter 13). Interviewers ask about `send` mainly to check that you understand generators pause and resume.

---

### 6.8 Lazy Evaluation and Memory: Lists versus Generators

**Definition:** **Lazy evaluation** means values are computed only when requested. A list stores every element (O(n) memory). A generator stores only its current state (O(1) memory).

```python
import sys
import tracemalloc

squares_list = [number * number for number in range(1_000_000)]
squares_gen = (number * number for number in range(1_000_000))
print("list object > 8 MB:", sys.getsizeof(squares_list) > 8_000_000)
print("generator object < 1 KB:", sys.getsizeof(squares_gen) < 1_000)

tracemalloc.start()
total = sum(number * number for number in range(1_000_000))
_, peak_lazy = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
total_eager = sum([number * number for number in range(1_000_000)])
_, peak_eager = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(total == total_eager, peak_lazy < peak_eager / 100)
```

**Output:**

```text
list object > 8 MB: True
generator object < 1 KB: True
True True
```

(`sys.getsizeof` on a list counts only the array of references, not the integer objects themselves. The real memory use is even higher.)

**Trade-off:** generators are not faster per item and cannot be indexed, sliced, measured with `len()` or reused. Use them for **streaming**; use lists when you need random access or multiple passes.

---

### 6.9 Reading and Processing Large Files with Generators

**Why it matters for a Data Engineer:** "How do you process a 50 GB file on a machine with 8 GB of RAM?" Iterate over the file object (it reads line by line with buffering) and keep the processing lazy.

```python
from pathlib import Path


def read_lines(path: Path):
    """Yield lines without trailing newlines; memory stays constant."""
    with path.open(encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


def read_in_blocks(path: Path, block_size: int = 1024 * 1024):
    """Yield fixed-size binary blocks (for files without line structure, e.g. hashing)."""
    with path.open("rb") as file:
        while block := file.read(block_size):
            yield block


sample = Path("events.log")
sample.write_text("INFO start\nERROR disk full\nINFO end\n", encoding="utf-8", newline="\n")
print([line for line in read_lines(sample) if line.startswith("ERROR")])
print(sum(len(block) for block in read_in_blocks(sample, block_size=8)))
```

**Output:**

```text
['ERROR disk full']
36
```

**Trap:** returning a generator from inside a `with` block in a *normal* function closes the file before the caller consumes the data. A generator function like `read_lines` is safe, because the `with` stays open until iteration finishes (or the generator is closed).

---

### 6.10 Generator-Based Data Pipelines

**Definition:** Chain generators so each record flows through every stage one at a time, like an assembly line. Nothing runs until the final consumer pulls data. This is the same lazy model as Spark transformations versus actions.

```python
import csv
import io
from itertools import islice
from typing import Iterable, Iterator

RAW_CSV = """order_id,region,amount
1,EU,100.50
2,US,not_a_number
3,EU,25
4,APAC,75.25
5,US,10
"""


def read_records(text_stream) -> Iterator[dict]:
    yield from csv.DictReader(text_stream)


def parse_amounts(records: Iterable[dict], rejects: list) -> Iterator[dict]:
    for record in records:
        try:
            yield {**record, "amount": float(record["amount"])}
        except ValueError:
            rejects.append(record["order_id"])


def only_regions(records: Iterable[dict], regions: set[str]) -> Iterator[dict]:
    return (record for record in records if record["region"] in regions)


def chunked(items: Iterable, size: int) -> Iterator[list]:
    """Group any iterable into lists of `size` items (the last may be shorter)."""
    iterator = iter(items)
    while batch := list(islice(iterator, size)):
        yield batch


rejected_ids: list[str] = []
pipeline = only_regions(parse_amounts(read_records(io.StringIO(RAW_CSV)), rejected_ids), {"EU", "US"})
for batch_number, batch in enumerate(chunked(pipeline, 2), start=1):
    print(f"load batch {batch_number}:", [record["order_id"] for record in batch])
print("rejected:", rejected_ids)
```

**Output:**

```text
load batch 1: ['1', '3']
load batch 2: ['5']
rejected: ['2']
```

`itertools.batched(iterable, n)` (Python 3.12+) does the same as `chunked` but yields tuples.

---

### 6.11 Interview Questions and Common Traps

| Question | Answer |
|---|---|
| Iterable vs iterator? | Iterable has `__iter__` (can produce iterators); iterator has `__next__` and is single-pass. |
| What does `yield` do? | Produces a value and pauses the function, keeping its state until the next `next()`. |
| `return` vs `yield`? | `return` ends the function once; `yield` can produce many values lazily. |
| Why is a generator memory-efficient? | It holds only its current state, not all values. |
| What happens when a generator is exhausted? | `next()` raises `StopIteration`; `for` loops stop quietly; it cannot be restarted. |
| How do you get the length of a generator? | You cannot without consuming it (`sum(1 for _ in gen)`). |
| Difference between a generator and a list comprehension? | Lazy and single-use vs eager and reusable. |
| What is `yield from`? | Delegation to a sub-iterator, including its return value. |

**Common traps**
1. Iterating an exhausted generator a second time returns nothing, **silently**.
2. `list(generator)` on a huge stream defeats the purpose and loads everything.
3. Checking `if generator:` is always `True`, even when it will yield nothing.
4. Passing the same iterator to two consumers: they steal items from each other. Use `itertools.tee` (which buffers) or recreate the generator.
5. Exceptions inside a generator surface only when it is consumed, possibly far from where it was created.

**Follow-up questions**
- *How would you count records while streaming?* Wrap the generator in a counting stage, or use `enumerate`, and log the count at the end.
- *How would you read the first 10 rows of a 100 GB file?* `list(islice(read_lines(path), 10))`.

---

### Chapter 6 Review

**Key takeaways**
- `for` calls `iter()` once and `next()` until `StopIteration`.
- Generators pause at `yield` and keep their state; they are lazy and single-pass.
- Chain generators into pipelines for constant-memory processing; batch with `islice`.
- `send`, `close` and `throw` control a paused generator; `close` triggers `finally` cleanup.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How do you make a reusable iterable? | Implement `__iter__` that returns a new generator each time. |
| How do you take the first N items lazily? | `itertools.islice(iterable, n)`. |
| Is a file object an iterator? | Yes; it yields lines and is single-pass. |
| What exception ends iteration? | `StopIteration`. |

**Common traps:** a second pass over a generator; `len()` on a generator; `if gen:`; sharing one iterator between consumers.

**Practice exercise:** Write a generator `dedupe_stream(records, key)` that yields only the first record for each key value. Then explain its memory cost: it is O(number of unique keys), not O(1).

---

## 7. Object-Oriented Programming

### 7.1 Classes and Objects

**Definition:** A **class** is a blueprint that bundles **data (attributes)** and **behaviour (methods)**. An **object** (instance) is one concrete thing created from the class. Everything in Python is an object, including integers, functions and classes themselves.

**Why it matters for a Data Engineer:** Classes model connectors (`S3Source`, `PostgresSink`), pipeline steps, configuration and records. Interfaces such as "every source has `read()`" let you swap implementations, and use fakes in tests.

```python
class TableLoader:
    """Load rows into a named table (educational example)."""

    def __init__(self, table: str) -> None:
        self.table = table          # instance attribute
        self.rows_loaded = 0

    def load(self, rows: list[dict]) -> int:
        self.rows_loaded += len(rows)
        return self.rows_loaded


orders_loader = TableLoader("orders")      # create an object
orders_loader.load([{"id": 1}, {"id": 2}])
print(orders_loader.table, orders_loader.rows_loaded, isinstance(orders_loader, TableLoader))
```

**Output:**

```text
orders 2 True
```

---

### 7.2 Constructors and `__init__`

**Definition:** `__init__` **initialises** a newly created object (sets its attributes). The object itself is created just before by `__new__`, which you rarely override (immutable types, singletons). `__init__` must return `None`.

```python
class Connection:
    def __init__(self, host: str, port: int = 5432, *, timeout: int = 30) -> None:
        if not host:
            raise ValueError("host is required")
        self.host, self.port, self.timeout = host, port, timeout

    def __repr__(self) -> str:
        return f"Connection(host={self.host!r}, port={self.port}, timeout={self.timeout})"


print(Connection("db.internal", timeout=5))
```

**Output:**

```text
Connection(host='db.internal', port=5432, timeout=5)
```

**Best practice:** Validate arguments in `__init__` so invalid objects can never exist ("fail fast"). Keep it cheap: do **not** open network connections there. Use an explicit `connect()` or a context manager.

---

### 7.3 self and cls

- `self` is the **instance** a method was called on. `loader.load(rows)` is really `TableLoader.load(loader, rows)`.
- `cls` is the **class** a class method was called on. It is used to build new instances and works correctly with subclasses.
- Both are conventions, not keywords, but always use these names.

---

### 7.4 Instance, Class and "Static" Variables

- **Instance variables** live on each object (`self.table`).
- **Class variables** are defined in the class body and **shared by all instances**. Python has no separate "static variable" keyword; class variables play that role.

```python
class Job:
    default_retries = 3            # class variable (shared)
    run_count = 0
    shared_tags = []               # DANGER: mutable class variable

    def __init__(self, name: str) -> None:
        self.name = name           # instance variable
        Job.run_count += 1


first, second = Job("a"), Job("b")
second.default_retries = 5         # creates an INSTANCE attribute that hides the class one
first.shared_tags.append("x")      # mutates the shared list: visible from every instance
print(Job.run_count, first.default_retries, second.default_retries, Job.default_retries)
print(second.shared_tags, vars(second))
```

**Output:**

```text
2 3 5 3
['x'] {'name': 'b', 'default_retries': 5}
```

**Common mistake:** a mutable class attribute (`shared_tags = []`) used as if it were per instance. Initialise per-instance containers in `__init__`.

---

### 7.5 Instance Methods, Class Methods and Static Methods

| Type | Decorator | First argument | Use it for |
|---|---|---|---|
| Instance method | none | `self` | behaviour that uses or changes instance state |
| Class method | `@classmethod` | `cls` | alternative constructors (`from_uri`, `from_config`), class-level state |
| Static method | `@staticmethod` | none | a helper that logically belongs to the class but needs neither `self` nor `cls` |

```python
class S3Location:
    def __init__(self, bucket: str, prefix: str = "") -> None:
        self.bucket, self.prefix = bucket, prefix

    @classmethod
    def from_uri(cls, uri: str) -> "S3Location":
        """Alternative constructor: 's3://bucket/a/b' -> S3Location('bucket', 'a/b')."""
        if not uri.startswith("s3://"):
            raise ValueError(f"not an S3 URI: {uri}")
        bucket, _, prefix = uri.removeprefix("s3://").partition("/")
        return cls(bucket, prefix)

    @staticmethod
    def is_folder_key(key: str) -> bool:
        return key.endswith("/")

    def uri(self) -> str:
        return f"s3://{self.bucket}/{self.prefix}"


location = S3Location.from_uri("s3://lake/raw/orders/")
print(location.bucket, location.prefix, location.uri(), S3Location.is_folder_key("raw/"))
```

**Output:**

```text
lake raw/orders/ s3://lake/raw/orders/ True
```

**Interview question:** *Why use `cls(...)` in a class method instead of `S3Location(...)`?*
**Answer:** So that `SubClass.from_uri(...)` returns a `SubClass` instance. The constructor follows inheritance.

---

### 7.6 Inheritance and Method Overriding

**Definition:** A **child class** inherits attributes and methods from a **parent class** and can **override** (replace) or extend them.

```python
class Reader:
    def read(self) -> list[str]:
        return ["raw"]

    def describe(self) -> str:
        return f"{type(self).__name__} returning {len(self.read())} row(s)"


class CsvReader(Reader):
    def read(self) -> list[str]:          # override
        return ["id,name", "1,Asha"]


print(Reader().describe())
print(CsvReader().describe())             # inherited describe() calls the overridden read()
print(issubclass(CsvReader, Reader))
```

**Output:**

```text
Reader returning 1 row(s)
CsvReader returning 2 row(s)
True
```

---

### 7.7 super()

**Definition:** `super()` returns a proxy that calls the **next class in the MRO** (see [7.8](#78-multiple-inheritance-and-mro)). In single inheritance that means the parent. It is used to extend, rather than replace, parent behaviour, especially `__init__`.

```python
class BaseSource:
    def __init__(self, name: str) -> None:
        self.name = name


class ApiSource(BaseSource):
    def __init__(self, name: str, base_url: str) -> None:
        super().__init__(name)                 # let the parent set its attributes
        self.base_url = base_url.rstrip("/")


source = ApiSource("crm", "https://api.example.com/")
print(source.name, source.base_url)
```

**Output:**

```text
crm https://api.example.com
```

**Common mistake:** forgetting `super().__init__(...)`, so the parent's attributes never exist and you get an `AttributeError` later.

---

### 7.8 Multiple Inheritance and MRO

**Definition:** A class can inherit from several parents. The **Method Resolution Order (MRO)** is the order Python searches classes for an attribute. It is computed with the **C3 linearisation** algorithm. The rules: a child comes before its parents, the parents keep the order they were listed in, and each class appears once.

```python
class Base:
    def describe(self) -> str:
        return "Base"


class Retrying(Base):
    def describe(self) -> str:
        return "Retrying>" + super().describe()


class Logging(Base):
    def describe(self) -> str:
        return "Logging>" + super().describe()


class ResilientClient(Retrying, Logging):
    def describe(self) -> str:
        return "Client>" + super().describe()


print(ResilientClient().describe())
print([cls.__name__ for cls in ResilientClient.__mro__])
```

**Output:**

```text
Client>Retrying>Logging>Base
['ResilientClient', 'Retrying', 'Logging', 'Base', 'object']
```

**Key insight:** in `Retrying`, `super()` calls `Logging`, **not** `Base`. `super()` follows the MRO of the actual object, which is what makes cooperative **mixins** work.

**Best practice:** Use multiple inheritance only for small, focused **mixins** (`LoggingMixin`, `RetryMixin`). Otherwise prefer composition (see [7.12](#712-composition-versus-inheritance)).

---

### 7.9 Polymorphism and Duck Typing

**Definition:**
- **Polymorphism** means "same interface, different behaviour": code calls `source.read()` without knowing the concrete class.
- **Duck typing:** "if it walks like a duck and quacks like a duck, it's a duck." Python cares whether an object **has** the method, not what class it inherits from.

```python
class CsvSource:
    def read(self) -> list[dict]:
        return [{"id": 1}]


class ApiSource:
    def read(self) -> list[dict]:
        return [{"id": 2}, {"id": 3}]


def ingest(source) -> int:          # works with anything that has .read()
    return len(source.read())


print([ingest(source) for source in (CsvSource(), ApiSource())])
```

**Output:**

```text
[1, 2]
```

**Formalising duck typing:** `typing.Protocol` (3.8+) lets static type checkers verify "has a `read()` method" without inheritance:

```python
from typing import Protocol


class SupportsRead(Protocol):
    def read(self) -> list[dict]: ...


def count_rows(source: SupportsRead) -> int:
    return len(source.read())


class FakeSource:
    def read(self) -> list[dict]:
        return [{"id": 1}]


print(count_rows(FakeSource()))
```

**Output:**

```text
1
```

---

### 7.10 Encapsulation

**Definition:** Bundling data with the methods that operate on it, and hiding internal details behind a public interface. Python has **no truly private attributes**. It uses conventions:

| Name | Meaning |
|---|---|
| `name` | public |
| `_name` | internal: "don't use from outside" (not enforced) |
| `__name` | **name mangling**: renamed to `_ClassName__name` to avoid accidental clashes in subclasses |

```python
class Checkpoint:
    def __init__(self) -> None:
        self._last_id = 0                 # internal state
        self.__secret_token = "t0k3n"     # name-mangled

    def advance(self, new_id: int) -> None:
        if new_id < self._last_id:
            raise ValueError("checkpoint cannot move backwards")
        self._last_id = new_id

    @property
    def last_id(self) -> int:             # read-only public view
        return self._last_id


checkpoint = Checkpoint()
checkpoint.advance(10)
print(checkpoint.last_id, hasattr(checkpoint, "__secret_token"), checkpoint._Checkpoint__secret_token)
```

**Output:**

```text
10 False t0k3n
```

**Why it matters for a Data Engineer:** The `advance` method protects an **invariant** (a watermark must never move backwards). Callers cannot bypass the rule by accident. Name mangling is **not security**: never treat it as a way to hide credentials.

---

### 7.11 Abstraction and Abstract Base Classes

**Definition:** **Abstraction** exposes *what* an object does and hides *how*. An **abstract base class** (ABC) defines a contract: subclasses **must** implement every `@abstractmethod`, and the ABC itself cannot be instantiated.

```python
from abc import ABC, abstractmethod


class Sink(ABC):
    @abstractmethod
    def write(self, rows: list[dict]) -> int:
        """Write rows and return how many were written."""

    def write_all(self, batches: list[list[dict]]) -> int:   # concrete method shared by all sinks
        return sum(self.write(batch) for batch in batches)


class ListSink(Sink):
    def __init__(self) -> None:
        self.rows: list[dict] = []

    def write(self, rows: list[dict]) -> int:
        self.rows.extend(rows)
        return len(rows)


class BrokenSink(Sink):
    pass


print(ListSink().write_all([[{"id": 1}], [{"id": 2}, {"id": 3}]]))
for cls in (Sink, BrokenSink):
    try:
        cls()
    except TypeError as error:
        print("TypeError:", str(error).split(" with")[0])
```

**Output:**

```text
3
TypeError: Can't instantiate abstract class Sink
TypeError: Can't instantiate abstract class BrokenSink
```

**ABC vs Protocol:** an ABC requires explicit inheritance and is checked at **run time** (on instantiation). A `Protocol` is structural and checked by **static type checkers**.

---

### 7.12 Composition versus Inheritance

- **Inheritance = "is-a"**: `CsvSource` *is a* `Source`.
- **Composition = "has-a"**: a `Pipeline` *has a* source, a list of transforms and a sink.

**Why composition is usually preferred:** deep inheritance trees (`S3CsvGzipIncrementalSource`) explode in number and are fragile, because a change in a parent breaks children. Composition lets you mix any source with any sink at run time and inject fakes in tests. See the full example in [7.17](#717-data-engineering-oop-design-example).

**Rule of thumb:** inherit to share an **interface**; compose to combine **behaviour**.

---

### 7.13 Properties, Getters and Setters

**Definition:** `@property` turns a method into an attribute-style accessor. You can add validation or computed values **without changing the public interface** (`obj.batch_size` keeps working).

```python
class LoaderConfig:
    def __init__(self, batch_size: int) -> None:
        self.batch_size = batch_size           # goes through the setter below

    @property
    def batch_size(self) -> int:               # getter
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value: int) -> None:  # setter with validation
        if not 1 <= value <= 50_000:
            raise ValueError(f"batch_size must be 1..50000, got {value}")
        self._batch_size = value

    @property
    def max_rows_per_commit(self) -> int:      # computed, read-only (no setter)
        return self._batch_size * 10


config = LoaderConfig(1_000)
config.batch_size = 2_500
print(config.batch_size, config.max_rows_per_commit)
try:
    config.max_rows_per_commit = 1
except AttributeError:
    print("AttributeError: read-only property")
try:
    config.batch_size = 0
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
2500 25000
AttributeError: read-only property
ValueError: batch_size must be 1..50000, got 0
```

**Pythonic note:** don't write Java-style `get_x()` / `set_x()` methods. Start with a plain attribute and switch to `@property` later if you need validation; callers won't have to change. How `@property` works internally is covered in [12.10](#1210-descriptors-and-property-internals).

---

### 7.14 Dataclasses

**Definition:** `@dataclass` (3.7+) generates `__init__`, `__repr__` and `__eq__` from type-annotated fields. Options: `frozen=True` (immutable and hashable), `order=True` (comparison operators), `slots=True` (3.10+, less memory), `kw_only=True` (3.10+).

```python
from dataclasses import asdict, dataclass, field, replace
from datetime import date


@dataclass(frozen=True)
class Order:
    order_id: int
    amount: float
    order_date: date
    tags: tuple[str, ...] = ()                       # immutable default is safe

    def __post_init__(self) -> None:                 # validation after __init__
        if self.amount < 0:
            raise ValueError(f"order {self.order_id}: negative amount")


@dataclass
class BatchStats:
    source: str
    errors: list[str] = field(default_factory=list)   # new list per instance


order = Order(1, 99.5, date(2026, 10, 29))
print(order)
print(asdict(order)["amount"], order == Order(1, 99.5, date(2026, 10, 29)), hash(order) == hash(replace(order)))
print(replace(order, amount=10.0).amount)            # copy with changes (objects are frozen)

stats_a, stats_b = BatchStats("a"), BatchStats("b")
stats_a.errors.append("row 3 bad")
print(stats_a.errors, stats_b.errors)

try:
    Order(2, -1, date(2026, 10, 29))
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
Order(order_id=1, amount=99.5, order_date=datetime.date(2026, 10, 29), tags=())
99.5 True True
10.0
['row 3 bad'] []
ValueError: order 2: negative amount
```

**Dataclass vs alternatives:**

| Tool | Best for |
|---|---|
| `dict` | loose, schema-less JSON |
| `NamedTuple` | small immutable records that should also behave like tuples |
| `dataclass` | typed internal records, configuration objects |
| pydantic (third-party) | **validating and parsing external input** (API payloads, configs) with type coercion |

---

### 7.15 Dunder (Magic) Methods

**Definition:** "Double underscore" methods let your objects work with Python syntax and built-ins.

| Method | Triggered by | Notes |
|---|---|---|
| `__init__` | `Cls(...)` | initialise |
| `__repr__` | `repr(obj)`, debugger, containers | unambiguous, ideally valid code |
| `__str__` | `str(obj)`, `print(obj)` | user-friendly; falls back to `__repr__` |
| `__len__` | `len(obj)` | also used for truthiness if no `__bool__` |
| `__bool__` | `if obj:` | |
| `__eq__` | `==` | defining it sets `__hash__ = None` unless you also define `__hash__` |
| `__hash__` | `hash(obj)`, dict keys, sets | must agree with `__eq__` |
| `__lt__` etc. | `<`, `sorted()` | `functools.total_ordering` fills in the rest |
| `__iter__` | `for x in obj` | |
| `__contains__` | `x in obj` | |
| `__getitem__` | `obj[key]` | |
| `__call__` | `obj()` | callable objects |
| `__enter__` / `__exit__` | `with obj:` | Chapter 11 |

```python
class Batch:
    def __init__(self, batch_id: str, rows: list[dict]) -> None:
        self.batch_id, self.rows = batch_id, rows

    def __repr__(self) -> str:
        return f"Batch(batch_id={self.batch_id!r}, rows=<{len(self.rows)} rows>)"

    def __str__(self) -> str:
        return f"batch {self.batch_id} ({len(self)} rows)"

    def __len__(self) -> int:
        return len(self.rows)

    def __iter__(self):
        return iter(self.rows)

    def __getitem__(self, index: int) -> dict:
        return self.rows[index]

    def __contains__(self, order_id: int) -> bool:
        return any(row["id"] == order_id for row in self.rows)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Batch) and self.batch_id == other.batch_id

    def __hash__(self) -> int:
        return hash(self.batch_id)


batch = Batch("b-001", [{"id": 1}, {"id": 2}])
print(repr(batch))
print(batch, len(batch), batch[0], 2 in batch, bool(Batch("empty", [])))
print([row["id"] for row in batch], len({batch, Batch("b-001", [])}))
```

**Output:**

```text
Batch(batch_id='b-001', rows=<2 rows>)
batch b-001 (2 rows) 2 {'id': 1} True False
[1, 2] 1
```

**Interview question:** *`__str__` vs `__repr__`?*
**Answer:** `__repr__` is for developers: unambiguous, used in logs, the REPL and inside containers. `__str__` is for end users. If only one is defined, define `__repr__`.

---

### 7.16 SOLID Principles with Python Examples

| Principle | Meaning | Data Engineering example |
|---|---|---|
| **S**ingle Responsibility | A class has one reason to change | Separate `OrderExtractor`, `OrderValidator` and `OrderLoader`, not one `OrderPipeline` that does everything |
| **O**pen/Closed | Open for extension, closed for modification | Add `ParquetWriter` as a new class registered in a factory, without editing `if format == ...` chains |
| **L**iskov Substitution | Subclasses must work wherever the parent is expected | Every `Sink.write()` returns the row count and raises on failure; a sink that silently drops rows breaks callers |
| **I**nterface Segregation | Prefer small, focused interfaces | `Readable` and `Writable` protocols instead of one giant `Storage` with 20 methods |
| **D**ependency Inversion | Depend on abstractions, inject concrete classes | `Pipeline(source: Source, sink: Sink)` receives objects; it does not create `PostgresSink()` internally |

```python
from typing import Protocol


class Writer(Protocol):
    def write(self, rows: list[dict]) -> int: ...


class CsvWriter:
    def write(self, rows: list[dict]) -> int:
        return len(rows)


class JsonWriter:
    def write(self, rows: list[dict]) -> int:
        return len(rows)


WRITERS: dict[str, type] = {"csv": CsvWriter, "json": JsonWriter}   # Open/Closed: register, don't edit


def export(rows: list[dict], writer: Writer) -> int:                # Dependency Inversion
    return writer.write(rows)


print(export([{"id": 1}], WRITERS["json"]()))
```

**Output:**

```text
1
```

---

### 7.17 Data Engineering OOP Design Example

**Production-style:** a small, testable pipeline built with abstraction, composition and dependency injection.

```python
import csv
import io
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, Iterable, Iterator

logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(message)s")
logger = logging.getLogger("pipeline")

Transform = Callable[[dict], dict]


class Source(ABC):
    @abstractmethod
    def read(self) -> Iterator[dict]:
        """Yield records one at a time."""


class Sink(ABC):
    @abstractmethod
    def write(self, rows: list[dict]) -> int:
        """Persist rows; return the number written."""


class CsvTextSource(Source):
    def __init__(self, text: str) -> None:
        self._text = text

    def read(self) -> Iterator[dict]:
        yield from csv.DictReader(io.StringIO(self._text))


class MemorySink(Sink):
    def __init__(self) -> None:
        self.rows: list[dict] = []

    def write(self, rows: list[dict]) -> int:
        self.rows.extend(rows)
        return len(rows)


@dataclass
class RunStats:
    read: int = 0
    written: int = 0
    rejected: list[str] = field(default_factory=list)


class Pipeline:
    """Composition: a pipeline HAS a source, transforms and a sink."""

    def __init__(self, source: Source, sink: Sink, transforms: Iterable[Transform], batch_size: int = 500) -> None:
        self.source, self.sink = source, sink
        self.transforms = list(transforms)
        self.batch_size = batch_size

    def run(self) -> RunStats:
        stats, batch = RunStats(), []
        for record in self.source.read():
            stats.read += 1
            try:
                for transform in self.transforms:
                    record = transform(record)
            except (KeyError, ValueError) as error:
                stats.rejected.append(f"{record.get('id')}: {error}")
                logger.warning("rejected record %s: %s", record.get("id"), error)
                continue
            batch.append(record)
            if len(batch) >= self.batch_size:
                stats.written += self.sink.write(batch)
                batch = []
        if batch:
            stats.written += self.sink.write(batch)
        return stats


def cast_amount(record: dict) -> dict:
    return {**record, "amount": float(record["amount"])}


def uppercase_country(record: dict) -> dict:
    return {**record, "country": record["country"].strip().upper()}


source = CsvTextSource("id,amount,country\n1,10.5,in\n2,oops,us\n3,7,es\n")
sink = MemorySink()
result = Pipeline(source, sink, [cast_amount, uppercase_country], batch_size=2).run()
print(result)
print(sink.rows)
```

**Output:**

```text
RunStats(read=3, written=2, rejected=["2: could not convert string to float: 'oops'"])
[{'id': '1', 'amount': 10.5, 'country': 'IN'}, {'id': '3', 'amount': 7.0, 'country': 'ES'}]
```

(The `WARNING rejected record 2: …` log line goes to standard error.)

**Why this design works:**
- Adding an `S3Source` or a `PostgresSink` needs **no change** to `Pipeline` (Open/Closed).
- Tests pass an in-memory source and sink: no AWS, no database.
- Transforms are pure functions, so they are easy to test and reorder.
- Batching bounds memory and reduces the number of write calls.

---

### Chapter 7 Review

**Key takeaways**
- `__init__` initialises; `__new__` creates. `self` is the instance, `cls` the class.
- Class attributes are shared; never use a mutable class attribute as per-instance state.
- `@classmethod` for alternative constructors; `@staticmethod` for helpers.
- `super()` follows the MRO (C3 linearisation), not simply "the parent".
- Python privacy is by convention; `__name` mangling avoids clashes, it is not security.
- Prefer composition and dependency injection; inherit for interfaces.
- Dataclasses remove boilerplate; use `field(default_factory=...)` for mutable defaults.
- If you define `__eq__`, define `__hash__` too (or the object becomes unhashable).

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Does Python support method overloading? | Not by signature; the last definition wins. Use default or optional arguments, or `functools.singledispatch`. |
| What is MRO? | The order Python searches classes for attributes; see `Cls.__mro__`. |
| ABC vs interface? | An ABC is Python's way to declare an interface with enforced abstract methods. |
| `@property` purpose? | Attribute-style access with validation or computation, keeping the interface stable. |
| What does `dataclass(frozen=True)` give you? | Immutability and an automatically generated `__hash__`. |
| Composition vs inheritance? | "has-a" vs "is-a"; composition is more flexible. |

**Common traps:** mutable class attributes; forgetting `super().__init__()`; defining `__eq__` without `__hash__`; deep inheritance hierarchies; doing I/O in `__init__`.

**Practice exercise:** Create an ABC `Validator` with `validate(row) -> list[str]` (a list of error messages). Implement `RequiredFields(fields)` and `PositiveAmount()`. Write `CompositeValidator(validators)` that runs all of them and returns all errors for a row.

---

## 8. Exception Handling

### 8.1 Syntax Errors versus Runtime Exceptions

**Definition:**
- A **syntax error** is invalid Python (`if x = 1:`). It is detected when the file is **compiled**, so *nothing* in that file runs.
- An **exception** is an error raised **while the code runs** (dividing by zero, a missing key, a network timeout). It can be caught and handled.

**The exception hierarchy (simplified):**

```text
BaseException
 ├── SystemExit, KeyboardInterrupt, GeneratorExit   <- do NOT catch these casually
 └── Exception                                      <- catch from here down
      ├── ArithmeticError → ZeroDivisionError, OverflowError
      ├── LookupError → KeyError, IndexError
      ├── ValueError → UnicodeDecodeError, json.JSONDecodeError
      ├── TypeError, AttributeError, NameError → UnboundLocalError
      ├── OSError → FileNotFoundError, PermissionError, TimeoutError, ConnectionError
      ├── RuntimeError → RecursionError, NotImplementedError
      └── ImportError → ModuleNotFoundError
```

Catching a parent class catches all of its children: `except LookupError` handles both `KeyError` and `IndexError`.

---

### 8.2 try, except, else and finally

| Block | Runs when |
|---|---|
| `try` | always, first |
| `except SomeError` | an exception matching `SomeError` was raised in `try` |
| `else` | `try` finished **without** an exception (keep the `try` block minimal) |
| `finally` | **always**, even after `return`, `break` or an unhandled exception |

```python
def safe_divide(total: float, count: int) -> float | str:
    try:
        average = total / count
    except ZeroDivisionError:
        print("  except: no rows")
        return "n/a"
    else:
        print("  else: success")
        return average
    finally:
        print("  finally: always runs")


print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

**Output:**

```text
  else: success
  finally: always runs
5.0
  except: no rows
  finally: always runs
n/a
```

**Trap:** a `return` inside `finally` overrides any earlier `return` **and silently discards an in-flight exception**. Never return from `finally`; Python 3.14 even warns about it.

---

### 8.3 Catching Specific Exceptions

**Definition:** Catch only the exceptions you expect **and know how to handle**. Let everything else propagate.

```python
import json

raw_messages = ['{"id": 1, "amount": "9.5"}', "{broken json", '{"id": 3}', '{"id": 4, "amount": "abc"}']
for raw in raw_messages:
    try:
        message = json.loads(raw)
        amount = float(message["amount"])
    except json.JSONDecodeError as error:
        print(f"bad JSON at char {error.pos}: {raw!r}")
    except KeyError as error:
        print(f"message {message['id']}: missing field {error}")
    except ValueError as error:                      # after JSONDecodeError (its subclass)
        print(f"message {message['id']}: {error}")
    else:
        print(f"message {message['id']}: amount={amount}")
```

**Output:**

```text
message 1: amount=9.5
bad JSON at char 1: '{broken json'
message 3: missing field 'amount'
message 4: could not convert string to float: 'abc'
```

**Order matters:** Python uses the **first** matching `except`. Put subclasses (`JSONDecodeError`) before parent classes (`ValueError`). Several exceptions can share one handler: `except (ValueError, TypeError) as error:`.

---

### 8.4 Raising Exceptions

```python
def validate_batch_size(batch_size: int) -> int:
    if not isinstance(batch_size, int):
        raise TypeError(f"batch_size must be int, got {type(batch_size).__name__}")
    if batch_size <= 0:
        raise ValueError(f"batch_size must be positive, got {batch_size}")
    return batch_size


for candidate in (100, 0, "10"):
    try:
        print("ok:", validate_batch_size(candidate))
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
```

**Output:**

```text
ok: 100
ValueError: batch_size must be positive, got 0
TypeError: batch_size must be int, got str
```

- `raise` with no argument inside `except` **re-raises** the current exception and keeps the original traceback.
- Choose the right built-in type: `ValueError` (right type, bad value), `TypeError` (wrong type), `KeyError` (missing key), `NotImplementedError` (abstract behaviour), `RuntimeError` (invalid state).

---

### 8.5 Custom Exceptions

**Definition:** Your own exception classes, inheriting from `Exception` (or from one shared base exception for your project).

**Why it matters for a Data Engineer:** Custom types let callers decide **what to do** with a failure:
- `DataValidationError` → quarantine the record and continue,
- `TransientError` → retry,
- `ConfigurationError` → fail the job immediately.

```python
class PipelineError(Exception):
    """Base class for all pipeline errors."""


class ConfigurationError(PipelineError):
    """Invalid or missing configuration: fail fast, do not retry."""


class TransientError(PipelineError):
    """Temporary failure (timeout, throttling): safe to retry."""


class DataValidationError(PipelineError):
    """A record failed validation: quarantine it and continue."""

    def __init__(self, record_id: object, reason: str) -> None:
        super().__init__(f"record {record_id}: {reason}")
        self.record_id, self.reason = record_id, reason


def validate(record: dict) -> dict:
    if record.get("amount") is None or record["amount"] < 0:
        raise DataValidationError(record.get("id"), "invalid amount")
    return record


quarantine = []
for record in [{"id": 1, "amount": 5}, {"id": 2, "amount": -3}, {"id": 3}]:
    try:
        validate(record)
    except DataValidationError as error:
        quarantine.append({"id": error.record_id, "reason": error.reason})
print(quarantine)
print(issubclass(DataValidationError, PipelineError))
```

**Output:**

```text
[{'id': 2, 'reason': 'invalid amount'}, {'id': 3, 'reason': 'invalid amount'}]
True
```

---

### 8.6 Exception Chaining

**Definition:** `raise NewError(...) from original` records the original exception as `__cause__`. The traceback then shows both, joined by "The above exception was the direct cause of the following exception". Without `from`, an exception raised inside `except` is still linked implicitly (`__context__`). `raise ... from None` hides the original (use it rarely).

```python
class LoadError(Exception):
    pass


def load_config(text: str) -> dict:
    import json
    try:
        return json.loads(text)
    except json.JSONDecodeError as error:
        raise LoadError("config file is not valid JSON") from error


try:
    load_config("{not json}")
except LoadError as error:
    print(error, "| caused by:", type(error.__cause__).__name__)
```

**Output:**

```text
config file is not valid JSON | caused by: JSONDecodeError
```

**Best practice:** translate low-level errors into domain errors at layer boundaries (driver → repository → pipeline) and **always chain** with `from`, so the root cause is never lost.

---

### 8.7 Logging Exceptions

- `logger.exception("message")` logs at ERROR level **with the full traceback**. Use it inside an `except` block.
- `logger.error("message", exc_info=True)` does the same at any level.
- Log **once**, where you handle the error. Logging and re-raising at every layer produces duplicate tracebacks.

```python
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("loader")


def load_file(path: str) -> None:
    try:
        with open(path, encoding="utf-8") as file:
            file.read()
    except FileNotFoundError:
        logger.error("input missing: %s", path)      # expected condition: no traceback needed
        raise


try:
    load_file("does_not_exist.csv")
except FileNotFoundError:
    logger.info("job marked as failed; exit code 1")
```

**Output:**

```text
ERROR loader: input missing: does_not_exist.csv
INFO loader: job marked as failed; exit code 1
```

Use `logger.exception(...)` for **unexpected** errors, where the traceback is essential for debugging.

---

### 8.8 Retry Handling

**Definition:** Re-attempting an operation that failed for a **transient** reason (network blip, throttling, deadlock, timeout).

**Rules for safe retries:**
1. Retry only **transient** errors. A `ValueError` from bad data will fail every time.
2. Use **exponential backoff** (1s, 2s, 4s…) with **jitter** (randomness), so many workers don't retry at the same instant.
3. Cap the number of attempts and the maximum delay; **re-raise** after the final attempt.
4. Retried operations must be **idempotent**, otherwise a retry may duplicate data (see [15.6](#156-idempotency)).

```python
import random
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def call_with_retry(func: Callable[[], T], *, attempts: int = 4, base_delay: float = 0.5,
                    max_delay: float = 30.0, retry_on: tuple[type[BaseException], ...] = (ConnectionError, TimeoutError)) -> T:
    """Call func, retrying transient errors with exponential backoff and full jitter."""
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except retry_on as error:
            if attempt == attempts:
                raise
            delay = random.uniform(0, min(max_delay, base_delay * 2 ** (attempt - 1)))
            print(f"attempt {attempt} failed ({error}); retrying")
            time.sleep(delay)
    raise AssertionError("unreachable")


outcomes = iter([ConnectionError("reset"), TimeoutError("slow"), "payload"])


def flaky_fetch() -> str:
    outcome = next(outcomes)
    if isinstance(outcome, Exception):
        raise outcome
    return outcome


print(call_with_retry(flaky_fetch, base_delay=0.001))
```

**Output:**

```text
attempt 1 failed (reset); retrying
attempt 2 failed (slow); retrying
payload
```

A reusable decorator version is in [11.5](#115-decorators-with-arguments). In production you may use the `tenacity` library or the retry support built into SDKs (boto3, `urllib3.Retry`).

---

### 8.9 Resource Cleanup

Resources (files, DB connections, locks, temp directories) must be released even when an error happens. Prefer `with` (context managers, Chapter 11) over manual `try/finally`.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as connection:          # always closed
    with connection:                                            # commit on success, rollback on error
        connection.execute("CREATE TABLE t (id INTEGER PRIMARY KEY)")
    print(connection.execute("SELECT count(*) FROM t").fetchone())
```

**Output:**

```text
(0,)
```

Note: a `sqlite3` connection used as a context manager manages the **transaction**; it does **not** close the connection. That is why `closing()` is added.

---

### 8.10 Anti-Patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| `except:` (bare) | also catches `KeyboardInterrupt` and `SystemExit`; hides bugs such as `NameError` | catch specific exceptions |
| `except Exception: pass` | silently swallows every failure: the job "succeeds" with missing data | handle, log with context, or re-raise |
| Catching too much in one `try` | you can't tell which line failed | keep `try` blocks small; use `else` |
| `raise Exception("failed")` | callers cannot distinguish error types | raise a specific or custom type |
| `raise NewError(str(e))` without `from` | the original traceback is lost | `raise NewError(...) from e` |
| Logging and re-raising at every layer | duplicate tracebacks | log once, where it is handled |
| Retrying non-transient errors | wastes time; may duplicate side effects | retry only known transient types |
| Using exceptions for normal control flow in hot loops | slow and unclear | check cheaply when the failure case is common |

**Acceptable broad catch:** at the **top level** of a job, to log, alert and set a non-zero exit code, always followed by a re-raise or `sys.exit(1)`:

```python
# Exits with code 1 by design: demonstrates top-level failure handling.
import logging
import sys

logger = logging.getLogger("job")


def main() -> int:
    raise RuntimeError("simulated failure")


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        logger.exception("job failed")      # full traceback in the logs
        sys.exit(1)                          # scheduler sees the failure
```

---

### 8.11 Production Examples: Database, File and API Failures

**Production-style – database load with transaction rollback:**

```python
import logging
import sqlite3
from contextlib import closing

logger = logging.getLogger("db_load")


def load_orders(connection: sqlite3.Connection, rows: list[tuple[int, float]]) -> int:
    """Insert all rows atomically: either every row is committed or none is."""
    try:
        with connection:                                     # one transaction
            connection.executemany("INSERT INTO orders (id, amount) VALUES (?, ?)", rows)
    except sqlite3.IntegrityError as error:
        raise ValueError(f"load rejected, transaction rolled back: {error}") from error
    return len(rows)


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amount REAL NOT NULL)")
    print(load_orders(conn, [(1, 10.0), (2, 20.0)]))
    try:
        load_orders(conn, [(3, 30.0), (1, 99.0)])            # duplicate key 1
    except ValueError as error:
        print(error)
    print(conn.execute("SELECT count(*) FROM orders").fetchone()[0])   # row 3 was NOT kept
```

**Output:**

```text
2
load rejected, transaction rolled back: UNIQUE constraint failed: orders.id
2
```

**Production-style – file failures, classified:**

```python
import json
from pathlib import Path


def read_json_config(path: Path) -> dict:
    """Read a JSON config file, turning low-level errors into clear messages."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise RuntimeError(f"config not found: {path}") from error
    except PermissionError as error:
        raise RuntimeError(f"no permission to read: {path}") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"config is not valid UTF-8 JSON: {path}: {error}") from error


Path("good.json").write_text('{"batch_size": 500}', encoding="utf-8")
Path("bad.json").write_text('{"batch_size": }', encoding="utf-8")
for name in ("good.json", "bad.json", "missing.json"):
    try:
        print(read_json_config(Path(name)))
    except RuntimeError as error:
        print("RuntimeError:", error)
```

**Output:**

```text
{'batch_size': 500}
RuntimeError: config is not valid UTF-8 JSON: bad.json: Expecting value: line 1 column 16 (char 15)
RuntimeError: config not found: missing.json
```

**Production-style – API failures, classified by HTTP status:**

```python
# Requires: pip install requests
import logging

import requests

logger = logging.getLogger("api")
TRANSIENT_STATUS = {429, 500, 502, 503, 504}


class TransientApiError(Exception):
    """Retry-able API failure."""


class PermanentApiError(Exception):
    """Non-retry-able API failure (bad request, auth, not found)."""


def fetch_json(session: requests.Session, url: str, params: dict) -> dict:
    try:
        response = session.get(url, params=params, timeout=(5, 30))   # (connect, read) seconds
    except (requests.ConnectionError, requests.Timeout) as error:
        raise TransientApiError(f"network error calling {url}") from error
    if response.status_code in TRANSIENT_STATUS:
        raise TransientApiError(f"{url} returned {response.status_code}")
    if response.status_code >= 400:
        raise PermanentApiError(f"{url} returned {response.status_code}: {response.text[:200]}")
    try:
        return response.json()
    except ValueError as error:
        raise PermanentApiError(f"{url} returned non-JSON body") from error
```

Combine `fetch_json` with `call_with_retry(..., retry_on=(TransientApiError,))` from [8.8](#88-retry-handling).

**Exception groups (3.11+):** when several concurrent tasks fail together, `ExceptionGroup` bundles the errors and `except*` handles each type:

```python
try:
    raise ExceptionGroup("batch failures", [ValueError("row 3"), TimeoutError("s3")])
except* ValueError as group:
    print("validation:", [str(error) for error in group.exceptions])
except* TimeoutError as group:
    print("transient:", [str(error) for error in group.exceptions])
```

**Output:**

```text
validation: ['row 3']
transient: ['s3']
```

---

### Chapter 8 Review

**Key takeaways**
- Catch specific exceptions; put subclasses before parents.
- `else` runs on success, `finally` always runs; never `return` inside `finally`.
- Create a small hierarchy of custom exceptions to signal *what to do* (retry, quarantine, fail).
- Chain with `raise ... from error`; log once with `logger.exception` for unexpected errors.
- Retry only transient errors, with backoff, jitter and a cap, and only for idempotent operations.
- Use transactions so a failed load leaves no partial data.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Why avoid bare `except:`? | It catches `SystemExit`/`KeyboardInterrupt` and hides real bugs. |
| `Exception` vs `BaseException`? | Application errors derive from `Exception`; `BaseException` also covers exit signals. |
| What does `raise` alone do? | Re-raises the current exception, keeping the traceback. |
| `__cause__` vs `__context__`? | Explicit `from` vs implicit chaining while handling another error. |
| When does `finally` not run? | Only if the process is killed (`os._exit`, SIGKILL, power loss). |
| EAFP or LBYL? | Python prefers EAFP (see [12.15](#1215-eafp-versus-lbyl)). |

**Common traps:** `except Exception: pass`; catching `ValueError` before `JSONDecodeError`; `return` in `finally`; retrying `ValueError`.

**Practice exercise:** Write `parse_rows(lines)` that returns `(good, bad)`. A bad entry should be `(line_number, line, reason)` for wrong column counts and for non-numeric amounts. A line containing only `"FATAL"` should raise a custom `CorruptFileError`, which must stop processing.

---

## 9. File Handling

### 9.1 Opening, Reading, Writing and Appending Files

**Definition:** `open(path, mode, encoding=...)` returns a **file object**. Text mode returns `str`; binary mode returns `bytes`. Always close files, ideally with `with`, which closes them automatically.

```python
from pathlib import Path

with open("report.txt", "w", encoding="utf-8") as file:      # create / overwrite
    file.write("line 1\n")
    file.writelines(["line 2\n", "line 3\n"])

with open("report.txt", "a", encoding="utf-8") as file:      # append
    print("line 4", file=file)

with open("report.txt", encoding="utf-8") as file:           # read everything (small files only)
    print(repr(file.read()))

with open("report.txt", encoding="utf-8") as file:
    print(file.readline().rstrip())                          # one line
    print([line.rstrip() for line in file])                  # the remaining lines, streamed

print(Path("report.txt").read_text(encoding="utf-8").count("\n"))   # pathlib shortcut
```

**Output:**

```text
'line 1\nline 2\nline 3\nline 4\n'
line 1
['line 2', 'line 3', 'line 4']
4
```

| Method | Returns | Memory |
|---|---|---|
| `file.read()` | whole file as one string | O(file size) |
| `file.readline()` | the next line | O(line) |
| `file.readlines()` | list of all lines | O(file size) |
| `for line in file` | one line at a time | **O(line)** – preferred |
| `file.read(n)` | up to *n* characters / bytes | O(n) – for binary chunking |

---

### 9.2 File Modes

| Mode | Meaning | If the file exists | If it doesn't |
|---|---|---|---|
| `"r"` | read (default) | read from start | `FileNotFoundError` |
| `"w"` | write | **truncated (emptied)** | created |
| `"a"` | append | write at end | created |
| `"x"` | exclusive create | `FileExistsError` | created |
| `"r+"` | read and write | no truncation | `FileNotFoundError` |
| `"b"` suffix | binary (`"rb"`, `"wb"`) | bytes instead of str | |
| `"t"` suffix | text (default) | | |

**Data Engineering tip:** `"x"` mode prevents two job runs from overwriting the same output file. `"w"` on the wrong path silently destroys data.

---

### 9.3 The with Statement for Files

`with open(...) as file:` guarantees `file.close()` runs even if an exception happens inside the block. Unflushed buffered data is written and the OS file handle is released. Several files can be opened in one statement:

```python
with open("source.txt", "w", encoding="utf-8") as file:
    file.write("a\nb\n")

with open("source.txt", encoding="utf-8") as source, open("copy.txt", "w", encoding="utf-8") as target:
    for line in source:
        target.write(line.upper())

with open("copy.txt", encoding="utf-8") as file:
    print(file.read().split())
print(file.closed)
```

**Output:**

```text
['A', 'B']
True
```

---

### 9.4 Reading Large Files Efficiently

| Technique | When |
|---|---|
| `for line in file` | line-based text (logs, CSV, JSON Lines) |
| `file.read(chunk_size)` in a loop | binary files, hashing, uploads |
| `csv.reader` / `csv.DictReader` on the open file | CSV of any size (streams rows) |
| `itertools.islice(file, n)` | peek at the first *n* lines |
| `pandas.read_csv(..., chunksize=...)` | DataFrame logic on chunks (see [17.14](#1714-chunk-based-file-reading)) |
| `mmap` | random access to huge binary files |

**Production-style – hash a large file in constant memory (for checksums and deduplication):**

```python
import hashlib
from pathlib import Path


def file_sha256(path: Path, block_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 hex digest of a file of any size."""
    digest = hashlib.sha256()
    with path.open("rb") as file:
        while block := file.read(block_size):
            digest.update(block)
    return digest.hexdigest()


Path("blob.bin").write_bytes(b"hello")
print(file_sha256(Path("blob.bin")))
```

**Output:**

```text
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

---

### 9.5 Encoding and Newline Handling

**Encoding:** always pass `encoding="utf-8"` (or the source's documented encoding). Without it, Python uses the platform default (`locale.getpreferredencoding()`, often `cp1252` on Windows). Python 3.15 makes UTF-8 the default; until then, be explicit.

**Newlines:**
- In **text mode**, Python translates `\r\n` and `\r` into `\n` when reading ("universal newlines") and writes `os.linesep` (`\r\n` on Windows) when writing.
- `newline=""` disables translation. It is **required for the `csv` module**, which handles line endings itself, including newlines inside quoted fields.
- `newline="\n"` forces Unix line endings on any OS (useful for files consumed by Linux tools).

```python
from pathlib import Path

Path("windows.txt").write_bytes(b"a\r\nb\r\n")
with open("windows.txt", encoding="utf-8") as file:
    print(repr(file.read()))                      # translated
with open("windows.txt", encoding="utf-8", newline="") as file:
    print(repr(file.read()))                      # untouched
```

**Output:**

```text
'a\nb\n'
'a\r\nb\r\n'
```

---

### 9.6 CSV Files

**Definition:** The `csv` module correctly handles delimiters, quoting, embedded commas and quotes, and newlines inside fields. **Never** parse CSV with `line.split(",")`.

```python
import csv

with open("customers.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "city"])
    writer.writeheader()
    writer.writerows([
        {"id": 1, "name": "Smith, John", "city": "Pune"},
        {"id": 2, "name": 'Ana "AJ" Lopez', "city": "Madrid"},
    ])

with open("customers.csv", encoding="utf-8") as file:     # raw text view (not parsing)
    print(file.read())

with open("customers.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["id"], "|", row["name"], "|", row["city"])
```

**Output:**

```text
id,name,city
1,"Smith, John",Pune
2,"Ana ""AJ"" Lopez",Madrid

1 | Smith, John | Pune
2 | Ana "AJ" Lopez | Madrid
```

**Delimiter, quoting and escaping options:**

| Option | Meaning |
|---|---|
| `delimiter="\|"` | field separator (`,`, `\t`, `\|`, `;`) |
| `quotechar='"'` | character used to quote fields |
| `quoting=csv.QUOTE_MINIMAL` | quote only when needed (default) |
| `quoting=csv.QUOTE_ALL` / `QUOTE_NONNUMERIC` / `QUOTE_NONE` | quote every field / non-numeric fields / never |
| `doublequote=True` | a quote inside a field is written as `""` (default) |
| `escapechar="\\"` | escape character, needed with `QUOTE_NONE` |
| `skipinitialspace=True` | ignore spaces after the delimiter |
| `csv.QUOTE_NOTNULL`, `csv.QUOTE_STRINGS` (3.12+) | distinguish `None` from `""` when writing and reading |

```python
import csv
import io

pipe_data = "id|comment\n1|ok\n2|has \\| pipe\n"
reader = csv.reader(io.StringIO(pipe_data), delimiter="|", quoting=csv.QUOTE_NONE, escapechar="\\")
print(list(reader))

sample = "id;amount\n1;9,50\n"
dialect = csv.Sniffer().sniff(sample)          # guess the delimiter
print(repr(dialect.delimiter))
```

**Output:**

```text
[['id', 'comment'], ['1', 'ok'], ['2', 'has | pipe']]
';'
```

**NULL versus empty string – an important data-quality question:** CSV has no native NULL. By default `csv` writes `None` as an empty field, so after a round trip `None` and `""` are indistinguishable. Agree on an explicit convention with the consumer. `\N` (used by PostgreSQL `COPY` and MySQL) is a common NULL marker.

```python
import csv
import io

NULL_MARKER = r"\N"
rows = [{"id": "1", "note": None}, {"id": "2", "note": ""}, {"id": "3", "note": 'says "hi", ok'}]

buffer = io.StringIO()
writer = csv.DictWriter(buffer, fieldnames=["id", "note"], lineterminator="\n")
writer.writeheader()
for row in rows:
    writer.writerow({key: NULL_MARKER if value is None else value for key, value in row.items()})
print(buffer.getvalue())

buffer.seek(0)
restored = [
    {key: None if value == NULL_MARKER else value for key, value in row.items()}
    for row in csv.DictReader(buffer)
]
print(restored)
```

**Output:**

```text
id,note
1,\N
2,
3,"says ""hi"", ok"

[{'id': '1', 'note': None}, {'id': '2', 'note': ''}, {'id': '3', 'note': 'says "hi", ok'}]
```

**Other CSV pitfalls:** every value is read as a **string** (convert explicitly). Excel exports may include a BOM (use `utf-8-sig`). Leading zeros (`00123`) must stay strings. Very large fields need `csv.field_size_limit(...)`.

---

### 9.7 JSON and JSON Lines

| Function | Direction | Notes |
|---|---|---|
| `json.loads(text)` / `json.load(file)` | JSON → Python | objects → `dict`, arrays → `list`, `null` → `None` |
| `json.dumps(obj)` / `json.dump(obj, file)` | Python → JSON | `indent=2`, `sort_keys=True`, `ensure_ascii=False`, `default=str` |

```python
import json
from datetime import date
from decimal import Decimal

record = {"id": 1, "amount": Decimal("9.99"), "day": date(2026, 10, 29), "name": "José", "tags": None}
try:
    json.dumps(record)
except TypeError as error:
    print("TypeError:", error)

print(json.dumps(record, default=str, ensure_ascii=False))
print(json.loads('{"a": [1, 2.5, null, true]}'))
print(json.loads('{"amount": 1.10}', parse_float=Decimal))      # exact decimals
```

**Output:**

```text
TypeError: Object of type Decimal is not JSON serializable
{"id": 1, "amount": "9.99", "day": "2026-10-29", "name": "José", "tags": null}
{'a': [1, 2.5, None, True]}
{'amount': Decimal('1.10')}
```

**JSON Lines (`.jsonl`, also called NDJSON):** one JSON object per line. It can be **streamed**, appended and split, and one bad record doesn't break the whole file. It is the standard format for logs, event exports and data-lake raw zones. A regular JSON array must be parsed in full before you can use it.

```python
import json
from pathlib import Path

events = [{"event": "click", "user": 1}, {"event": "view", "user": 2}]
with open("events.jsonl", "w", encoding="utf-8") as file:
    for event in events:
        file.write(json.dumps(event) + "\n")

with open("events.jsonl", "a", encoding="utf-8") as file:
    file.write("{corrupted\n")

good, bad = [], []
with open("events.jsonl", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        try:
            good.append(json.loads(line))
        except json.JSONDecodeError:
            bad.append(line_number)
print(len(good), bad, Path("events.jsonl").stat().st_size > 0)
```

**Output:**

```text
2 [3] True
```

---

### 9.8 XML

**Definition:** `xml.etree.ElementTree` parses XML into a tree of elements. For large files, `iterparse` streams elements and lets you free memory as you go.

```python
import io
import xml.etree.ElementTree as ET

xml_text = """<orders>
  <order id="1"><amount currency="EUR">10.50</amount></order>
  <order id="2"><amount currency="USD">7</amount></order>
</orders>"""

root = ET.fromstring(xml_text)
for order in root.findall("order"):
    amount = order.find("amount")
    print(order.get("id"), float(amount.text), amount.get("currency"))

total = 0.0
for event, element in ET.iterparse(io.StringIO(xml_text), events=("end",)):   # streaming
    if element.tag == "order":
        total += float(element.findtext("amount"))
        element.clear()                       # release memory for processed elements
print(total)
```

**Output:**

```text
1 10.5 EUR
2 7.0 USD
17.5
```

**Security:** the standard library XML parsers are vulnerable to some malicious constructs (e.g. "billion laughs" entity expansion). Parse **untrusted** XML with the `defusedxml` package.

---

### 9.9 YAML

**Definition:** YAML is a human-friendly configuration format. It needs the third-party **PyYAML** package. **Always use `yaml.safe_load`**. `yaml.load` with the full loader can construct arbitrary Python objects from untrusted input.

```python
# Third-party: pip install pyyaml
import yaml

config_text = """
pipeline: orders_daily
source:
  type: s3
  prefix: raw/orders/
batch_size: 5000
enabled: true
tables: [orders, order_items]
"""
config = yaml.safe_load(config_text)
print(config["source"]["type"], config["batch_size"] * 2, config["tables"], config["enabled"])
```

**Output:**

```text
s3 10000 ['orders', 'order_items'] True
```

**YAML gotchas:** `no`, `off` and `yes` may be parsed as booleans (YAML 1.1). Unquoted `08` may not be what you expect. Quote values when in doubt.

---

### 9.10 Parquet

**Definition:** Parquet is a **columnar**, compressed, typed file format and the standard for data lakes and warehouses (Spark, Snowflake, BigQuery, Athena, DuckDB).

| Property | CSV | Parquet |
|---|---|---|
| Layout | row-based text | columnar binary |
| Schema / types | none (all strings) | embedded schema with types |
| Compression | external (gzip) | built-in per column (Snappy, ZSTD) |
| Read only some columns | must read all | **column pruning** |
| Skip rows by filter | no | **predicate pushdown** using row-group statistics |
| Human-readable | yes | no |

```python
# Requires: pip install pandas pyarrow
import pandas as pd
import pyarrow.parquet as pq

frame = pd.DataFrame({"order_id": [1, 2, 3], "region": ["EU", "US", "EU"], "amount": [10.5, 7.0, 3.2]})
frame.to_parquet("orders.parquet", index=False, compression="snappy")

only_two_columns = pd.read_parquet("orders.parquet", columns=["order_id", "amount"])
eu_rows = pd.read_parquet("orders.parquet", filters=[("region", "==", "EU")])
print(only_two_columns.shape, len(eu_rows))       # (3, 2) 2

parquet_file = pq.ParquetFile("orders.parquet")
print(parquet_file.schema_arrow)                  # column names and types
for batch in parquet_file.iter_batches(batch_size=2):   # stream large files in batches
    print(batch.num_rows)
```

**Interview question:** *Why is Parquet faster than CSV for analytics?* Queries usually read a few columns of many rows. A columnar layout reads only those columns, compresses better (similar values sit together) and skips row groups using min/max statistics.

---

### 9.11 Compressed Files: gzip, bz2 and zipfile

```python
import bz2
import gzip
import zipfile

lines = ["id,amount\n", "1,10\n", "2,20\n"]

with gzip.open("orders.csv.gz", "wt", encoding="utf-8", newline="") as file:   # "t" = text
    file.writelines(lines)
with gzip.open("orders.csv.gz", "rt", encoding="utf-8", newline="") as file:
    print(sum(1 for _ in file) - 1, "data rows (gzip)")

with bz2.open("orders.csv.bz2", "wt", encoding="utf-8") as file:
    file.writelines(lines)
with bz2.open("orders.csv.bz2", "rt", encoding="utf-8") as file:
    print(file.readline().strip(), "(bz2 header)")

with zipfile.ZipFile("bundle.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
    archive.writestr("orders.csv", "".join(lines))
    archive.writestr("readme.txt", "daily export")
with zipfile.ZipFile("bundle.zip") as archive:
    print(archive.namelist())
    with archive.open("orders.csv") as member:            # stream one member, binary
        print(member.read().decode("utf-8").splitlines()[1])
```

**Output:**

```text
2 data rows (gzip)
id,amount (bz2 header)
['orders.csv', 'readme.txt']
1,10
```

| Format | Speed | Ratio | Splittable for parallel reads | Notes |
|---|---|---|---|---|
| gzip | fast | good | **No** | most common for CSV/JSON exports |
| bz2 | slow | better | Yes (in Hadoop/Spark) | |
| zip | fast | good | per member | an archive of many files |
| Snappy / ZSTD inside Parquet | very fast | good | Yes (by row group) | preferred for lakes |

**Security:** never call `extractall` on untrusted archives without checking member names; `../../` paths can write outside the target folder ("zip slip").

---

### 9.12 pathlib versus os.path

| Task | `os.path` / `os` (older, string-based) | `pathlib` (modern, object-based) |
|---|---|---|
| Join | `os.path.join("data", "raw", "a.csv")` | `Path("data") / "raw" / "a.csv"` |
| File name / stem / extension | `os.path.basename(p)`, `os.path.splitext(p)` | `p.name`, `p.stem`, `p.suffix` |
| Parent folder | `os.path.dirname(p)` | `p.parent` |
| Exists / is file | `os.path.exists(p)`, `os.path.isfile(p)` | `p.exists()`, `p.is_file()` |
| Create folders | `os.makedirs(d, exist_ok=True)` | `d.mkdir(parents=True, exist_ok=True)` |
| List matching files | `glob.glob("raw/**/*.csv", recursive=True)` | `Path("raw").rglob("*.csv")` |
| Read text | `open(p).read()` | `p.read_text(encoding="utf-8")` |
| Size / modified time | `os.path.getsize(p)` | `p.stat().st_size`, `p.stat().st_mtime` |

```python
from pathlib import Path

base = Path("landing")
(base / "2026" / "10").mkdir(parents=True, exist_ok=True)
for name in ("orders_1.csv", "orders_2.csv", "notes.txt"):
    (base / "2026" / "10" / name).write_text("id\n1\n", encoding="utf-8", newline="\n")

csv_files = sorted(base.rglob("*.csv"))
for path in csv_files:
    print(path.as_posix(), path.stem, path.suffix, path.stat().st_size)
print(csv_files[0].with_suffix(".parquet").name, csv_files[0].parent.name)
```

**Output:**

```text
landing/2026/10/orders_1.csv orders_1 .csv 5
landing/2026/10/orders_2.csv orders_2 .csv 5
orders_1.parquet 10
```

(`newline="\n"` keeps the size identical on every OS; without it, Windows writes `\r\n` and each file would be 7 bytes.)

**Recommendation:** use `pathlib` in new code. Cloud object stores (S3, GCS) are not file systems; use their SDKs, or `fsspec`/`s3fs` for a file-like interface.

---

### 9.13 shutil, glob and tempfile

```python
import glob
import shutil
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as work_dir:            # deleted automatically afterwards
    work = Path(work_dir)
    (work / "in").mkdir()
    for name in ("a.csv", "b.csv", "c.json"):
        (work / "in" / name).write_text("x", encoding="utf-8")

    print(sorted(Path(p).name for p in glob.glob(str(work / "in" / "*.csv"))))
    shutil.copy2(work / "in" / "a.csv", work / "a_copy.csv")     # copy with metadata
    shutil.move(str(work / "in" / "b.csv"), str(work / "b.csv"))  # move (rename across devices)
    shutil.copytree(work / "in", work / "backup")                 # copy a whole folder
    archive = shutil.make_archive(str(work / "backup_zip"), "zip", work / "backup")
    shutil.rmtree(work / "backup")                                # delete a folder tree: be careful
    print(sorted(p.name for p in work.iterdir()), Path(archive).suffix)

    with tempfile.NamedTemporaryFile("w", suffix=".csv", dir=work, delete=False, encoding="utf-8") as tmp:
        tmp.write("id\n")
    print(Path(tmp.name).suffix, Path(tmp.name).exists())
```

**Output:**

```text
['a.csv', 'b.csv']
['a_copy.csv', 'b.csv', 'backup_zip.zip', 'in'] .zip
.csv True
```

**Best practices:** use `tempfile` for scratch space instead of fixed paths like `/tmp/data.csv`, which collide when two jobs run in parallel. Guard `shutil.rmtree` with path checks. Note that `glob` results are **not sorted**; sort them for deterministic processing order.

---

### 9.14 File Validation

**Why it matters for a Data Engineer:** validating a file **before** loading it prevents half-loaded tables and bad data reaching downstream reports.

**Typical checks:** the file exists and is not empty, the name matches the expected pattern and date, the encoding decodes, the header matches the expected schema, every row has the right number of columns, a trailer record count matches, the checksum matches, and the file has not been processed before.

```python
import csv
from pathlib import Path

EXPECTED_HEADER = ["order_id", "amount", "order_date"]


def validate_csv_file(path: Path, expected_header: list[str]) -> list[str]:
    """Return a list of problems (an empty list means the file is valid)."""
    problems: list[str] = []
    if not path.is_file():
        return [f"missing file: {path}"]
    if path.stat().st_size == 0:
        return ["file is empty"]
    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header != expected_header:
                problems.append(f"header mismatch: expected {expected_header}, got {header}")
            for line_number, row in enumerate(reader, start=2):
                if len(row) != len(expected_header):
                    problems.append(f"line {line_number}: expected {len(expected_header)} fields, got {len(row)}")
    except UnicodeDecodeError as error:
        problems.append(f"not valid UTF-8: {error.reason} at byte {error.start}")
    return problems


Path("good.csv").write_text("order_id,amount,order_date\n1,9.5,2026-10-29\n", encoding="utf-8")
Path("bad.csv").write_text("order_id,amount\n1,9.5\n2,3.0,2026-10-29,extra\n", encoding="utf-8")
print(validate_csv_file(Path("good.csv"), EXPECTED_HEADER))
for problem in validate_csv_file(Path("bad.csv"), EXPECTED_HEADER):
    print(problem)
print(validate_csv_file(Path("nope.csv"), EXPECTED_HEADER))
```

**Output:**

```text
[]
header mismatch: expected ['order_id', 'amount', 'order_date'], got ['order_id', 'amount']
line 2: expected 3 fields, got 2
line 3: expected 3 fields, got 4
['missing file: nope.csv']
```

A file checksum (for example `file_sha256` from [9.4](#94-reading-large-files-efficiently)) stored in a manifest lets you detect a file that has already been processed.

---

### 9.15 Record-Count Reconciliation

**Definition:** proving that **no records were lost or duplicated**: `source_count == loaded_count + rejected_count`, checked for every run and recorded in an audit table.

```python
import csv
import io

source_text = "id,amount\n1,10\n2,x\n3,30\n"
loaded, rejected = [], []
source_count = 0
for row in csv.DictReader(io.StringIO(source_text)):
    source_count += 1
    try:
        loaded.append({"id": int(row["id"]), "amount": float(row["amount"])})
    except ValueError:
        rejected.append(row)

audit = {"source": source_count, "loaded": len(loaded), "rejected": len(rejected)}
audit["reconciled"] = audit["source"] == audit["loaded"] + audit["rejected"]
print(audit)
```

**Output:**

```text
{'source': 3, 'loaded': 2, 'rejected': 1, 'reconciled': True}
```

In production, also compare the **target table count** after the load, and **sums** of key numeric columns (control totals). See [15.13](#1513-source-to-target-reconciliation).

---

### 9.16 Chunk-Based Processing

**Definition:** process a large input in fixed-size pieces, so memory is bounded and each piece can be written, committed or retried independently.

```python
import csv
from itertools import islice
from pathlib import Path


def split_csv(path: Path, rows_per_file: int, output_dir: Path) -> list[Path]:
    """Split a CSV into numbered part files, repeating the header in each."""
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    with path.open(newline="", encoding="utf-8") as source:
        reader = csv.reader(source)
        header = next(reader)
        part_number = 0
        while batch := list(islice(reader, rows_per_file)):
            part_number += 1
            part_path = output_dir / f"part_{part_number:04d}.csv"
            with part_path.open("w", newline="", encoding="utf-8") as target:
                writer = csv.writer(target)
                writer.writerow(header)
                writer.writerows(batch)
            outputs.append(part_path)
    return outputs


Path("big.csv").write_text("id\n" + "".join(f"{n}\n" for n in range(1, 8)), encoding="utf-8")
parts = split_csv(Path("big.csv"), rows_per_file=3, output_dir=Path("parts"))
print([p.name for p in parts], parts[-1].read_text(encoding="utf-8").split())
```

**Output:**

```text
['part_0001.csv', 'part_0002.csv', 'part_0003.csv'] ['id', '7']
```

---

### 9.17 Safe and Atomic File Writing

**Problem:** if a job crashes while writing `output.csv`, readers may see a **half-written file**.

**Solution:** write to a temporary file **in the same directory**, flush it to disk, then atomically rename it over the target with `os.replace`. Readers see either the old file or the complete new one, never a partial file. (A rename is atomic only within the same file system.)

```python
import os
import tempfile
from pathlib import Path


def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    """Write content to path atomically (same-filesystem rename)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(file_descriptor, "w", encoding=encoding, newline="") as temp_file:
            temp_file.write(content)
            temp_file.flush()
            os.fsync(temp_file.fileno())          # make sure the bytes are on disk
        os.replace(temp_name, path)               # atomic replace, also works on Windows
    except BaseException:
        Path(temp_name).unlink(missing_ok=True)   # clean up the partial temp file, then re-raise
        raise


target = Path("out") / "summary.csv"
atomic_write_text(target, "region,total\nEU,100\n")
print(target.read_text(encoding="utf-8").splitlines(), [p.name for p in target.parent.iterdir()])
```

**Output:**

```text
['region,total', 'EU,100'] ['summary.csv']
```

**Object stores:** S3 uploads are atomic per object (a reader never sees a partial object). For multi-file outputs, write to a staging prefix and then publish: write a `_SUCCESS` marker, swap a pointer, or use a table format such as Delta Lake or Iceberg.

---

### 9.18 File-Processing Interview Scenarios

| Scenario | Short answer (full treatment in Chapter 21) |
|---|---|
| A 50 GB CSV on an 8 GB machine | Stream rows with `csv.reader`; aggregate incrementally; write output in chunks. |
| Some rows have extra columns | Validate the field count per row; route bad rows with line numbers to a reject file; reconcile counts. |
| The same file arrives twice | Track processed files by name and checksum in a manifest or audit table; skip known checksums. |
| A downstream job reads half-written files | Atomic writes (temp + rename) or a `_SUCCESS` marker. |
| Thousands of tiny files are slow to query | Compact them into fewer, larger files (e.g. 128 MB–1 GB Parquet). |
| A file is in an unknown encoding | Try UTF-8 strictly; fall back to a documented encoding; count replacement characters; never silently guess. |

---

### Chapter 9 Review

**Key takeaways**
- Always use `with`, and always pass `encoding`; use `newline=""` for CSV.
- Stream line by line or in blocks; avoid `read()` and `readlines()` on big files.
- Use the `csv` module, define a NULL convention, and remember that every CSV value is a string.
- JSON Lines for streamable records; Parquet for analytics; gzip for exchange.
- Validate files before loading; reconcile counts after loading.
- Write atomically: temp file + `os.replace`.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| `"w"` vs `"a"` vs `"x"`? | Truncate vs append vs fail if the file exists. |
| Why `newline=""` with csv? | The csv module handles line endings itself; translation corrupts quoted newlines. |
| `json.load` vs `json.loads`? | From a file object vs from a string. |
| Why JSON Lines over a JSON array? | It can be streamed, appended, split, and isolates bad records. |
| pathlib or os.path? | pathlib for new code: readable and cross-platform. |
| How do you avoid partial files? | Write to a temp file in the same directory, then `os.replace`. |

**Common traps:** `"w"` on the wrong path; the default encoding on Windows; parsing CSV with `split`; `yaml.load`; `extractall` on untrusted zips; unsorted `glob` results.

**Practice exercise:** Write `csv_to_jsonl(csv_path, jsonl_path)` that streams rows, converts `amount` to float, writes valid rows as JSON Lines, writes invalid rows to `rejects.csv` with a `reason` column, and returns `{"read": n, "written": w, "rejected": r}`.

---

## 10. Modules, Packages and Environments

### 10.1 Modules and Packages

**Definition:**
- A **module** is a single `.py` file. Its name is the file name without `.py`.
- A **package** is a directory of modules, usually containing an `__init__.py` file. `__init__.py` runs when the package is first imported and can expose a public API. Directories without it are "namespace packages" (an advanced feature, mainly for splitting one package across several folders).
- A **library / distribution** is a package published to PyPI and installed with pip (e.g. `pandas`).

**Why it matters for a Data Engineer:** Shared code (connectors, validators, logging setup) belongs in an importable package that every pipeline uses, not in copy-pasted scripts.

**Import forms:**

```python
import json                                # the module object; use json.loads
import datetime as dt                      # alias
from pathlib import Path                   # one name
from collections import Counter, deque     # several names
from os import path as os_path             # alias for an imported name

print(json.dumps({"a": 1}), dt.date(2026, 1, 1).year, Path("a/b.csv").suffix, Counter("aab")["a"], os_path.sep in "/\\")
```

**Output:**

```text
{"a": 1} 2026 .csv 2 True
```

**Avoid `from module import *`:** it pollutes the namespace, hides where names come from and can silently overwrite your own names. A module can limit what `*` exports with `__all__ = ["public_name"]`.

---

### 10.2 How import Works

When you write `import orders_utils`, Python:
1. checks the cache **`sys.modules`**. If the module is already imported, it reuses that object, so **module code runs only once per process**;
2. otherwise **finds** the module by searching `sys.path` (see [10.5](#105-the-module-search-path));
3. **loads** it: compiles it (using the `.pyc` cache when valid), creates a module object and executes the module's top-level code;
4. binds the name in the importing namespace.

```python
import sys
import json

print("json" in sys.modules, sys.modules["json"] is json)
import json as json_again                       # no re-execution: the same cached object
print(json_again is json)
```

**Output:**

```text
True True
True
```

**Why it matters for a Data Engineer:**
- Top-level code runs at **import time**. A module that opens a DB connection or reads a large file at the top level slows every import and breaks unit tests. Put such work inside functions.
- Airflow parses DAG files frequently, so heavy top-level imports and computation in DAG files slow down the scheduler.
- Module-level objects behave like singletons (one per process), which is useful for a shared config or logger.

---

### 10.3 Absolute versus Relative Imports

```text
de_utils/
├── __init__.py
├── io/
│   ├── __init__.py
│   ├── readers.py
│   └── writers.py
└── quality/
    ├── __init__.py
    └── checks.py
```

| Style | Inside `de_utils/io/writers.py` | Notes |
|---|---|---|
| Absolute | `from de_utils.io.readers import read_csv` | clear and recommended by PEP 8 |
| Relative | `from .readers import read_csv` | `.` = same package |
| Relative | `from ..quality.checks import not_null` | `..` = parent package |

**Rules:** relative imports work only **inside a package**. Running a file directly (`python de_utils/io/writers.py`) makes it `__main__` without a package, so relative imports fail with `ImportError: attempted relative import with no known parent package`. Run it as a module instead: `python -m de_utils.io.writers`.

---

### 10.4 `__name__ == "__main__"`

**Definition:** Every module has a `__name__`. It is `"__main__"` when the file is run directly, and the module's import name when it is imported. The guard lets a file be both a **reusable module** and a **runnable script**.

```python
def run_pipeline(run_date: str) -> str:
    return f"pipeline ran for {run_date}"


def main() -> int:
    print(run_pipeline("2026-10-29"))
    return 0


print("module name:", __name__)
if __name__ == "__main__":       # True only when executed directly
    raise SystemExit(main())
```

**Output:**

```text
module name: __main__
pipeline ran for 2026-10-29
```

**Why it matters for a Data Engineer:**
- Tests can import `run_pipeline` without starting the job.
- With `multiprocessing` on Windows and macOS (the "spawn" start method), child processes re-import the main module. Without the guard, they would start the job again, recursively.
- `raise SystemExit(main())` returns a proper **exit code** to the scheduler.

---

### 10.5 The Module Search Path

`sys.path` is the list of directories searched in order:
1. the directory of the script being run (or the current directory for `-m`, `-c` and the REPL);
2. directories listed in the **`PYTHONPATH`** environment variable;
3. the standard library;
4. `site-packages` of the active environment (installed packages).

```python
import json
import sys

print(type(sys.path).__name__, len(sys.path) > 0)
print(json.__file__.endswith("__init__.py"))      # json is a package: its file is __init__.py
```

**Output:**

```text
list True
True
```

**Common problems:**
- **Shadowing:** a local file named `csv.py`, `json.py`, `logging.py` or `pandas.py` is found **before** the real module. Errors like `module 'csv' has no attribute 'reader'` usually mean exactly this.
- `sys.path.append("../lib")` hacks break when the working directory changes. **Install your package** (`pip install -e .`) instead.
- To check which file was imported: `import module; print(module.__file__)`.

---

### 10.6 requirements.txt

**Definition:** a plain-text list of packages for `pip install -r requirements.txt`.

```text
# requirements.txt  (application: pin exact versions)
pandas==2.2.2
pyarrow==16.1.0
requests==2.32.3
psycopg[binary]==3.2.1
```

**Best practices:**
- **Pin exact versions** for deployable pipelines, so every environment gets the same code.
- Keep dev tools (pytest, ruff, mypy) in a separate file such as `requirements-dev.txt`.
- Generate pins from a smaller "top-level" list with `pip-tools` (`pip-compile`) or `uv pip compile`, which also pins **transitive** dependencies.
- Update dependencies regularly and deliberately, and check for vulnerabilities (`pip-audit`).

---

### 10.7 pyproject.toml

**Definition:** the standard configuration file for Python projects (PEP 517/518/621). It declares build-system requirements, project metadata, dependencies and tool settings in one place.

```text
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "de-utils"
version = "1.4.0"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.31,<3",
    "pyyaml>=6,<7",
]

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.5", "mypy>=1.10"]
pandas = ["pandas>=2.1,<3", "pyarrow>=15"]

[project.scripts]
run-ingest = "de_utils.cli:main"        # installs a `run-ingest` command

[tool.ruff]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

**Libraries vs applications:** a **library** declares compatible **ranges** (`requests>=2.31,<3`) so it can coexist with other packages. An **application** additionally uses a **lock file** with exact versions (Poetry `poetry.lock`, uv `uv.lock`, or a compiled `requirements.txt`).

```text
python -m pip install -e ".[dev]"        # editable install with dev extras
python -m build                          # build a wheel (.whl) for distribution
```

---

### 10.8 Virtual Environments in Practice

| Tool | What it is | Typical use |
|---|---|---|
| `venv` | standard library environment manager | default choice |
| `virtualenv` | faster, more featureful third-party venv | legacy or CI |
| `conda` | environment and package manager, including non-Python libraries | data science, native dependencies |
| Poetry / uv / PDM | project managers with lock files | modern application workflows |
| Docker image | an OS-level environment | production deployment (Airflow workers, ECS, Kubernetes jobs) |

```python
import sys

in_virtualenv = sys.prefix != sys.base_prefix
print(type(in_virtualenv).__name__)
```

**Output:**

```text
bool
```

**Best practices:** one environment per project; never commit `.venv`; rebuild environments from the lock file in CI; keep the Python version consistent between dev and production (state it in `requires-python` and the container image).

---

### 10.9 Package Structure

A widely used **src layout** for a data engineering project:

```text
orders-pipeline/
├── pyproject.toml
├── README.md
├── src/
│   └── orders_pipeline/
│       ├── __init__.py
│       ├── cli.py              # entry point: argument parsing, calls main()
│       ├── config.py           # load and validate configuration
│       ├── extract.py
│       ├── transform.py        # pure functions: easy to test
│       ├── load.py
│       └── quality.py
├── tests/
│   ├── conftest.py             # shared pytest fixtures
│   ├── test_transform.py
│   └── data/sample_orders.csv
└── configs/
    ├── dev.yaml
    └── prod.yaml
```

**Why the src layout:** tests run against the **installed** package, not files that happen to be on the current path. This catches packaging mistakes (for example a missing `__init__.py` or data file) before deployment.

---

### 10.10 Circular Imports

**Definition:** module A imports module B while B (directly or indirectly) imports A. Because modules are cached **partially initialised** while they run, one of them may try to use a name that does not exist yet, giving `ImportError: cannot import name 'X' from partially initialized module`.

```python
import subprocess
import sys
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as folder:
    Path(folder, "config.py").write_text(
        "from validators import validate\nSETTINGS = {'min': 0}\n", encoding="utf-8")
    Path(folder, "validators.py").write_text(
        "from config import SETTINGS\n\ndef validate(value):\n    return value >= SETTINGS['min']\n", encoding="utf-8")
    result = subprocess.run([sys.executable, "-c", "import config"], cwd=folder, capture_output=True, text=True)
    print(result.stderr.strip().splitlines()[-1].split(" (")[0])
```

**Output:**

```text
ImportError: cannot import name 'SETTINGS' from partially initialized module 'config'
```

**Fixes, in order of preference:**
1. **Restructure:** move the shared code into a third module (e.g. `settings.py`) that both import. Circular imports usually signal unclear responsibilities.
2. **Dependency injection:** pass the settings into `validate(value, settings)` instead of importing them.
3. Import **inside the function** that needs it (a local, deferred import).
4. Use `import module` and access `module.name` at call time instead of `from module import name` at import time.
5. For type hints only: `from typing import TYPE_CHECKING` with `if TYPE_CHECKING: import ...`.

---

### 10.11 Building a Reusable Data Engineering Utility Package

**Production-style:** what a small shared package typically contains, with a runnable demonstration that builds the package in a temporary folder and imports it.

```python
import sys
import tempfile
import textwrap
from pathlib import Path

PACKAGE_FILES = {
    "de_utils/__init__.py": '''
        """Shared data engineering helpers."""
        from .batching import chunked
        from .quality import require_columns

        __all__ = ["chunked", "require_columns"]
        __version__ = "1.0.0"
    ''',
    "de_utils/batching.py": '''
        from itertools import islice
        from typing import Iterable, Iterator


        def chunked(items: Iterable, size: int) -> Iterator[list]:
            """Yield lists of at most `size` items."""
            if size <= 0:
                raise ValueError("size must be positive")
            iterator = iter(items)
            while batch := list(islice(iterator, size)):
                yield batch
    ''',
    "de_utils/quality.py": '''
        class SchemaError(ValueError):
            """Raised when required columns are missing."""


        def require_columns(row: dict, required: set[str]) -> None:
            missing = required - row.keys()
            if missing:
                raise SchemaError(f"missing columns: {sorted(missing)}")
    ''',
}

with tempfile.TemporaryDirectory() as root:
    for relative_path, source in PACKAGE_FILES.items():
        file_path = Path(root, relative_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(textwrap.dedent(source), encoding="utf-8")

    sys.path.insert(0, root)              # demo only: real projects use `pip install -e .`
    import de_utils
    from de_utils.quality import SchemaError

    print(de_utils.__version__, [len(batch) for batch in de_utils.chunked(range(7), 3)])
    try:
        de_utils.require_columns({"id": 1}, {"id", "amount"})
    except SchemaError as error:
        print("SchemaError:", error)
    sys.path.remove(root)
```

**Output:**

```text
1.0.0 [3, 3, 1]
SchemaError: missing columns: ['amount']
```

**What belongs in a shared utility package:** logging setup, configuration loading, retry and backoff helpers, connector wrappers, batching and chunking, schema and data-quality checks, audit-record helpers, date and partition helpers. Version it (semantic versioning), test it, and release it like any other library.

---

### Chapter 10 Review

**Key takeaways**
- A module executes once per process; it is then cached in `sys.modules`.
- Prefer absolute imports; run package modules with `python -m`.
- Guard script entry points with `if __name__ == "__main__":`.
- Don't name files after standard library or third-party modules.
- Pin application dependencies; libraries declare ranges in `pyproject.toml`.
- Break circular imports by restructuring or injecting dependencies.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Module vs package? | A `.py` file vs a directory of modules (usually with `__init__.py`). |
| What does `__init__.py` do? | Marks a regular package and runs on first import; can define the public API. |
| How does Python find modules? | Through `sys.path`: script directory, `PYTHONPATH`, stdlib, site-packages. |
| What is `python -m`? | Runs a module by import name, with package context (relative imports work). |
| `requirements.txt` vs `pyproject.toml`? | A pip install list vs the standard project metadata and configuration file. |
| How do you reload a module? | `importlib.reload(module)` (rarely needed outside notebooks). |

**Common traps:** shadowing (`csv.py`); `sys.path` hacks; heavy top-level code; `import *`; relative imports in scripts run directly.

**Practice exercise:** Lay out a package `ingest` with `readers.py`, `writers.py` and `cli.py`, where `cli.main()` reads a CSV path from `sys.argv`, counts its rows using `readers.count_rows`, and returns exit code 0 or 1. Show how to run it with `python -m ingest.cli path.csv`.

---

## 11. Decorators and Context Managers

### 11.1 Decorator Fundamentals

**Definition:** A decorator is a callable that **takes a function and returns a replacement function** (usually a wrapper that adds behaviour before and/or after the original). The `@` syntax is shorthand:

```text
@decorator
def func(): ...

# is exactly the same as
def func(): ...
func = decorator(func)
```

**Why it matters for a Data Engineer:** cross-cutting concerns (timing, logging, retries, input validation, caching, metrics, permission checks) are written **once** and applied to many functions, without cluttering business logic.

**How it works:** decorators rely on first-class functions and closures ([5.11](#511-first-class-functions), [5.13](#513-closures)). The wrapper accepts `*args, **kwargs` so it can wrap any signature.

```python
def announce(func):
    def wrapper(*args, **kwargs):
        print(f"-> calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__} returned {result!r}")
        return result
    return wrapper


@announce
def add_rows(existing: int, new: int) -> int:
    return existing + new


add_rows(10, 5)
print(add_rows.__name__)          # metadata lost: see 11.2
```

**Output:**

```text
-> calling add_rows(10, 5)
<- add_rows returned 15
wrapper
```

**Decorators run at definition (import) time;** the wrapper runs at call time.

---

### 11.2 functools.wraps

**Definition:** `@functools.wraps(func)` copies the wrapped function's `__name__`, `__doc__`, `__module__`, `__qualname__` and annotations onto the wrapper, and sets `__wrapped__` to the original.

**Why it matters:** without it, logs, tracebacks, documentation tools, pytest output and frameworks that inspect function names (Airflow tasks, CLI libraries) all see `wrapper`.

```python
import functools


def announce(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@announce
def load_orders(day: str) -> int:
    """Load one day of orders."""
    return 42


print(load_orders.__name__, "|", load_orders.__doc__, "|", load_orders.__wrapped__("x"))
```

**Output:**

```text
load_orders | Load one day of orders. | 42
```

---

### 11.3 Timing and Logging Decorators

**Production-style:**

```python
import functools
import logging
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("etl")


def log_call(func):
    """Log start, success (with duration) and failure of each call."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("start %s", func.__name__)
        started = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception:
            logger.error("failed %s", func.__name__)
            raise                                  # never swallow the error
        elapsed_ms = (time.perf_counter() - started) * 1000
        logger.info("done %s (%s ms)", func.__name__, "<100" if elapsed_ms < 100 else f"{elapsed_ms:.0f}")
        return result
    return wrapper


@log_call
def transform(rows: list[int]) -> list[int]:
    return [row * 2 for row in rows]


@log_call
def load(rows: list[int]) -> None:
    raise ConnectionError("warehouse unavailable")


print(transform([1, 2]))
try:
    load([1])
except ConnectionError as error:
    print("caught:", error)
```

**Output:**

```text
INFO start transform
INFO done transform (<100 ms)
[2, 4]
INFO start load
ERROR failed load
caught: warehouse unavailable
```

(In real code you would log the exact duration. This example rounds it so the output is reproducible.)

Use `time.perf_counter()` for measuring durations (monotonic, high resolution). Use `time.time()` only for wall-clock timestamps.

---

### 11.4 Caching Decorators

`functools.lru_cache(maxsize=N)` remembers results keyed by the arguments, which must be **hashable**. `functools.cache` (3.9+) is an unbounded version.

```python
import functools
import time


@functools.lru_cache(maxsize=1024)
def currency_rate(currency: str, day: str) -> float:
    """Pretend this is a slow API call."""
    time.sleep(0.01)
    return {"EUR": 1.08, "INR": 0.012}[currency]


rows = [("EUR", "2026-10-29")] * 1000 + [("INR", "2026-10-29")] * 1000
total = sum(currency_rate(currency, day) for currency, day in rows)
print(round(total, 2), currency_rate.cache_info())
currency_rate.cache_clear()
```

**Output:**

```text
1092.0 CacheInfo(hits=1998, misses=2, maxsize=1024, currsize=2)
```

**A time-to-live (TTL) cache** – for values that change, such as auth tokens or reference data:

```python
import functools
import time


def ttl_cache(seconds: float):
    """Cache results per argument tuple for `seconds` (positional, hashable arguments only)."""
    def decorator(func):
        store: dict[tuple, tuple[float, object]] = {}

        @functools.wraps(func)
        def wrapper(*args):
            now = time.monotonic()
            if args in store and now - store[args][0] < seconds:
                return store[args][1]
            value = func(*args)
            store[args] = (now, value)
            return value
        return wrapper
    return decorator


calls = []


@ttl_cache(seconds=0.05)
def get_token(service: str) -> str:
    calls.append(service)
    return f"token-{len(calls)}"


print(get_token("crm"), get_token("crm"))
time.sleep(0.06)
print(get_token("crm"), len(calls))
```

**Output:**

```text
token-1 token-1
token-2 2
```

**Cautions:** caches are per process and not shared between workers. Unbounded caches can leak memory. `lru_cache` on a method keeps `self` alive (a memory leak for many instances). Never cache results that depend on time unless they expire.

---

### 11.5 Decorators with Arguments

**Definition:** `@retry(times=3)` first **calls** `retry(times=3)`, which returns the real decorator. That gives three levels of nesting: **factory → decorator → wrapper**.

**Production-style – retry with exponential backoff and jitter:**

```python
import functools
import logging
import random
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.WARNING, format="%(levelname)s %(message)s")
logger = logging.getLogger("retry")


def retry(*, attempts: int = 3, base_delay: float = 1.0, max_delay: float = 30.0,
          exceptions: tuple[type[BaseException], ...] = (ConnectionError, TimeoutError)):
    """Retry the decorated function on the given transient exceptions."""
    if attempts < 1:
        raise ValueError("attempts must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    if attempt == attempts:
                        logger.error("%s failed after %d attempts: %s", func.__name__, attempts, error)
                        raise
                    delay = min(max_delay, base_delay * 2 ** (attempt - 1)) * random.uniform(0.5, 1.0)
                    logger.warning("%s attempt %d/%d failed: %s", func.__name__, attempt, attempts, error)
                    time.sleep(delay)
        return wrapper
    return decorator


failures_left = 2


@retry(attempts=4, base_delay=0.001)
def upload_part(part: int) -> str:
    global failures_left
    if failures_left:
        failures_left -= 1
        raise ConnectionError("connection reset")
    return f"part {part} uploaded"


print(upload_part(7))


@retry(attempts=2, base_delay=0.001)
def always_down() -> None:
    raise TimeoutError("read timed out")


try:
    always_down()
except TimeoutError:
    print("gave up and re-raised")
```

**Output:**

```text
WARNING upload_part attempt 1/4 failed: connection reset
WARNING upload_part attempt 2/4 failed: connection reset
part 7 uploaded
WARNING always_down attempt 1/2 failed: read timed out
ERROR always_down failed after 2 attempts: read timed out
gave up and re-raised
```

(The global counter only simulates a flaky service in this example.)

**Interview follow-ups:**
- *Why jitter?* Without it, many workers that failed together retry together ("thundering herd") and overload the service again.
- *What must be true of a retried function?* It must be **idempotent**, or the retry may duplicate a write.
- *How do you respect the server's guidance?* Honour a `Retry-After` header on HTTP 429/503 responses.

---

### 11.6 Validation and Authorization Decorators

**Validation** – check arguments before the function runs, using `inspect.signature` to map positional and keyword arguments to parameter names:

```python
import functools
import inspect


def validate_args(**rules):
    """rules: parameter name -> (predicate, message)."""
    def decorator(func):
        signature = inspect.signature(func)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            for name, (predicate, message) in rules.items():
                if not predicate(bound.arguments[name]):
                    raise ValueError(f"{func.__name__}: {name}={bound.arguments[name]!r} {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@validate_args(batch_size=(lambda v: 0 < v <= 10_000, "must be 1..10000"),
               table=(lambda v: v.isidentifier(), "must be a valid identifier"))
def load(table: str, batch_size: int = 500) -> str:
    return f"loading {table} in batches of {batch_size}"


print(load("orders"))
for bad_call in (lambda: load("orders", 0), lambda: load(table="drop table;")):
    try:
        bad_call()
    except ValueError as error:
        print("ValueError:", error)
```

**Output:**

```text
loading orders in batches of 500
ValueError: load: batch_size=0 must be 1..10000
ValueError: load: table='drop table;' must be a valid identifier
```

**Authorization** – guard dangerous operations:

```python
import functools


class PermissionDenied(Exception):
    pass


def require_role(role: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user: dict, *args, **kwargs):
            if role not in user.get("roles", ()):
                raise PermissionDenied(f"{user.get('name')} lacks role {role!r} for {func.__name__}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


@require_role("data_admin")
def drop_partition(user: dict, table: str, day: str) -> str:
    return f"{user['name']} dropped {table}/{day}"


print(drop_partition({"name": "ana", "roles": ["data_admin"]}, "sales", "2026-10-01"))
try:
    drop_partition({"name": "bob", "roles": ["analyst"]}, "sales", "2026-10-01")
except PermissionDenied as error:
    print("PermissionDenied:", error)
```

**Output:**

```text
ana dropped sales/2026-10-01
PermissionDenied: bob lacks role 'data_admin' for drop_partition
```

---

### 11.7 Class Decorators and Decorator Classes

**A class decorator** takes a **class** and returns a class (often the same one, registered or modified). `@dataclass` is the best-known example. A registry decorator implements a plug-in pattern:

```python
READERS: dict[str, type] = {}


def register_reader(file_format: str):
    def decorator(cls: type) -> type:
        READERS[file_format] = cls
        return cls
    return decorator


@register_reader("csv")
class CsvReader:
    def read(self, path: str) -> str:
        return f"csv rows from {path}"


@register_reader("json")
class JsonReader:
    def read(self, path: str) -> str:
        return f"json rows from {path}"


print(sorted(READERS), READERS["json"]().read("events.json"))
```

**Output:**

```text
['csv', 'json'] json rows from events.json
```

**A decorator implemented as a class** – useful when the decorator needs state:

```python
import functools


class CountCalls:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func, self.calls = func, 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)


@CountCalls
def fetch_page(page: int) -> list[int]:
    return [page]


fetch_page(1)
fetch_page(2)
print(fetch_page.calls, fetch_page.__name__)
```

**Output:**

```text
2 fetch_page
```

---

### 11.8 Stacking Decorators

Decorators are **applied bottom-up** (the one closest to the function first) and **run top-down** at call time (the outermost wrapper runs first).

```python
import functools


def tag(label: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"enter {label}")
            result = func(*args, **kwargs)
            print(f"exit {label}")
            return result
        return wrapper
    return decorator


@tag("retry")      # outermost: applied last, runs first
@tag("timer")      # innermost: applied first
def extract() -> str:
    print("extracting")
    return "ok"


extract()          # equivalent to tag("retry")(tag("timer")(extract))()
```

**Output:**

```text
enter retry
enter timer
extracting
exit timer
exit retry
```

**Why order matters:** with `@retry` outside `@timer`, **each attempt** is timed separately. With `@timer` outside `@retry`, the **total time including retries** is measured.

---

### 11.9 The Context Manager Protocol

**Definition:** an object usable in a `with` statement. It implements:
- `__enter__(self)` – setup; its return value is bound to the `as` target;
- `__exit__(self, exc_type, exc_value, traceback)` – cleanup; it **always** runs. The three arguments are `None` if no exception happened. Returning `True` **suppresses** the exception; returning `False` or `None` lets it propagate.

```text
with manager as resource:     # resource = manager.__enter__()
    body                      # if body raises, __exit__ receives the exception
                              # manager.__exit__(...) always runs
```

```python
class Timer:
    """Measure a block's duration; never suppresses exceptions."""

    def __enter__(self) -> "Timer":
        import time
        self._time = time
        self.started = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.elapsed = self._time.perf_counter() - self.started
        status = "failed" if exc_type else "ok"
        print(f"block {status}; exception type: {exc_type.__name__ if exc_type else None}")
        return False


with Timer() as timer:
    total = sum(range(1000))
print(total, timer.elapsed >= 0)

try:
    with Timer():
        raise KeyError("id")
except KeyError:
    print("KeyError propagated")
```

**Output:**

```text
block ok; exception type: None
499500 True
block failed; exception type: KeyError
KeyError propagated
```

**Interview question:** *What happens if `__exit__` returns `True`?* The exception is swallowed and execution continues after the `with` block. Do this only for exceptions you deliberately want to ignore.

---

### 11.10 contextlib and @contextmanager

`@contextlib.contextmanager` builds a context manager from a generator. The code before `yield` is setup, the yielded value is the `as` target, and the code after `yield` (in `finally`) is cleanup.

```python
import contextlib
import os


@contextlib.contextmanager
def temporary_env(name: str, value: str):
    """Set an environment variable for the duration of the block, then restore it."""
    previous = os.environ.get(name)
    os.environ[name] = value
    try:
        yield value
    finally:
        if previous is None:
            os.environ.pop(name, None)
        else:
            os.environ[name] = previous


with temporary_env("PIPELINE_ENV", "test") as env:
    print("inside:", os.environ["PIPELINE_ENV"], env)
print("after:", os.environ.get("PIPELINE_ENV"))

with contextlib.suppress(FileNotFoundError):              # ignore one specific error
    os.remove("file_that_does_not_exist.tmp")
print("suppress: continued")

with contextlib.ExitStack() as stack:                     # a dynamic number of resources
    files = [stack.enter_context(open(f"part_{n}.txt", "w", encoding="utf-8")) for n in range(3)]
    for number, file in enumerate(files):
        file.write(str(number))
print("all closed:", all(file.closed for file in files))
```

**Output:**

```text
inside: test test
after: None
suppress: continued
all closed: True
```

| contextlib tool | Use |
|---|---|
| `@contextmanager` | write a context manager as a generator |
| `closing(obj)` | call `obj.close()` on exit (for objects without `__exit__`) |
| `suppress(*exceptions)` | ignore specific exceptions |
| `ExitStack` | manage a variable number of resources |
| `nullcontext(value)` | a do-nothing placeholder when a context manager is optional |
| `redirect_stdout(file)` | capture prints (useful in tests) |
| `asynccontextmanager` | async version for `async with` |

**Trap:** without `try/finally` around `yield`, the cleanup code is **skipped** when the block raises.

---

### 11.11 Production Context Managers: Database Connections and Files

**Production-style – connection plus transaction management (DB-API, demonstrated with sqlite3):**

```python
import logging
import sqlite3
import sys
from contextlib import contextmanager
from typing import Callable, Iterator

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("db")


@contextmanager
def managed_connection(connect: Callable[[], sqlite3.Connection]) -> Iterator[sqlite3.Connection]:
    """Open a connection and always close it."""
    connection = connect()
    try:
        yield connection
    finally:
        connection.close()
        logger.info("connection closed")


@contextmanager
def transaction(connection: sqlite3.Connection) -> Iterator[sqlite3.Cursor]:
    """Commit if the block succeeds, roll back if it raises, always close the cursor."""
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
        logger.info("committed")
    except Exception:
        connection.rollback()
        logger.warning("rolled back")
        raise
    finally:
        cursor.close()


with managed_connection(lambda: sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE audit (run_id TEXT PRIMARY KEY, row_count INTEGER)")
    with transaction(conn) as cur:
        cur.execute("INSERT INTO audit VALUES (?, ?)", ("run-1", 100))
    try:
        with transaction(conn) as cur:
            cur.execute("INSERT INTO audit VALUES (?, ?)", ("run-2", 50))
            cur.execute("INSERT INTO audit VALUES (?, ?)", ("run-1", 1))   # duplicate key
    except sqlite3.IntegrityError as error:
        logger.error("load failed: %s", error)
    print(conn.execute("SELECT run_id, row_count FROM audit").fetchall())
```

**Output:**

```text
INFO committed
WARNING rolled back
ERROR load failed: UNIQUE constraint failed: audit.run_id
[('run-1', 100)]
INFO connection closed
```

**Production-style – atomic file output as a context manager:**

```python
import os
import tempfile
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def atomic_output(path: Path, encoding: str = "utf-8"):
    """Yield a temp file handle; on success replace `path` atomically, on failure delete the temp file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline="") as handle:
            yield handle
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except BaseException:
        Path(temp_name).unlink(missing_ok=True)
        raise


target = Path("exports/daily.csv")
with atomic_output(target) as out:
    out.write("id,total\n1,99\n")

try:
    with atomic_output(target) as out:
        out.write("partial")
        raise RuntimeError("crash mid-write")
except RuntimeError:
    pass
print(target.read_text(encoding="utf-8").splitlines(), sorted(p.name for p in target.parent.iterdir()))
```

**Output:**

```text
['id,total', '1,99'] ['daily.csv']
```

The failed second write left the previous good file untouched and no temp files behind.

---

### Chapter 11 Review

**Key takeaways**
- `@decorator` is `func = decorator(func)`; decorators with arguments add a factory level.
- Always use `functools.wraps`.
- Decorators are applied bottom-up and run outermost-first.
- Never swallow exceptions in a decorator; log and re-raise.
- Context managers guarantee cleanup; `__exit__` returning `True` suppresses exceptions.
- With `@contextmanager`, wrap the `yield` in `try/finally`.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| What is a decorator? | A callable that takes a function and returns an enhanced replacement. |
| Why `functools.wraps`? | Keeps the name, docstring and `__wrapped__` for logs, debugging and tools. |
| How do you pass arguments to a decorator? | Add an outer factory function that returns the decorator. |
| Can decorators be applied to classes? | Yes; class decorators receive and return a class (e.g. `@dataclass`). |
| What are `__enter__`/`__exit__`? | Setup and cleanup hooks of the `with` protocol. |
| How do you manage N files at once? | `contextlib.ExitStack`. |

**Common traps:** forgetting `return result` in a wrapper; forgetting `wraps`; caching non-hashable arguments; `yield` without `finally`; returning `True` from `__exit__` by accident.

**Practice exercise:** Write a decorator `@count_rows(log_every=1000)` for generator functions that yields every row unchanged and logs a running count every N rows and a final total. Write a context manager `audit_run(run_id)` that records the start time, end time, status (`success`/`failed`) and error message into a list of audit records.

---

## 12. Advanced Python

### 12.1 Memory Management in CPython

**Definition:** Python manages memory automatically. All objects live in a **private heap** managed by the interpreter. CPython uses:
1. **reference counting**, which frees most objects immediately when nothing refers to them;
2. a **cyclic garbage collector**, which finds groups of objects that refer only to each other;
3. **pymalloc**, a fast allocator for small objects (≤ 512 bytes) that keeps memory pools for reuse.

**Why it matters for a Data Engineer:**
- Memory is often **not returned to the OS** immediately after objects are freed (the allocator keeps pools). A long-running worker that once loaded a huge list may keep a high RSS (resident memory). Process big batches in **subprocesses**, or stream the data.
- Python objects carry overhead. A small `int` takes about 28 bytes, and a list of a million floats is roughly 8 MB of pointers plus 24 MB of float objects. Columnar libraries (NumPy, Arrow, pandas) store raw values compactly.

```python
import sys

print(sys.getsizeof(1), sys.getsizeof(1.0), sys.getsizeof(""), sys.getsizeof([]))
print(sys.getsizeof([0] * 1000) > sys.getsizeof([]) + 7_999)
```

**Output:**

```text
28 24 41 56
True
```

(Sizes are for 64-bit CPython 3.12 and differ slightly between versions. `sys.getsizeof` measures only the object itself, not the objects it refers to.)

---

### 12.2 Stack versus Heap

| | Call stack | Heap |
|---|---|---|
| Holds | **frames**: one per active function call, with references to local names | **all objects** (ints, lists, your classes…) |
| Lifetime | a frame is removed when its function returns | an object lives while something references it |
| Limit | the recursion limit (~1000 frames by default) | available RAM |

In Python, a local variable on the stack is just a **reference**; the object it points to is on the heap. That is why returning a list from a function is cheap (no copy) and why deep recursion fails with `RecursionError` long before memory runs out.

---

### 12.3 Reference Counting

**Definition:** every object keeps a count of the references pointing to it. Assignments, container insertions and argument passing increment it; `del`, rebinding and leaving a scope decrement it. When the count reaches **0**, the object is freed **immediately**.

```python
import sys

payload = ["large", "batch"]
before = sys.getrefcount(payload)        # includes a temporary reference from the call itself
alias = payload
holder = {"batch": payload}
print(sys.getrefcount(payload) - before)
del alias
holder.clear()
print(sys.getrefcount(payload) - before)
```

**Output:**

```text
2
0
```

**Interview point:** reference counting gives **deterministic** cleanup in CPython (files are closed as soon as the last reference disappears). Don't rely on it: other implementations (PyPy) behave differently. Use `with` for resources.

---

### 12.4 Garbage Collection and Cyclic References

**Problem:** objects that reference each other (a parent ↔ child, a node ↔ neighbour) never reach a count of 0, even when unreachable.

**Solution:** the **generational cyclic garbage collector** (`gc` module) periodically scans container objects, finds unreachable cycles and frees them.

```python
import gc
import weakref


class Node:
    def __init__(self, name: str) -> None:
        self.name, self.partner = name, None


standalone = Node("x")
weakref.finalize(standalone, print, "x freed immediately (refcount hit 0)")
del standalone
print("after del x")

gc.disable()                                  # make the demo deterministic
first, second = Node("a"), Node("b")
first.partner, second.partner = second, first # a reference cycle
weakref.finalize(first, print, "cycle freed by the garbage collector")
del first, second
print("after del a, b (cycle still in memory)")
print("collected objects > 0:", gc.collect() > 0)
gc.enable()
```

**Output:**

```text
x freed immediately (refcount hit 0)
after del x
after del a, b (cycle still in memory)
cycle freed by the garbage collector
collected objects > 0: True
```

**Production notes:** `gc.collect()` is rarely needed. Some batch jobs call `gc.freeze()` or adjust thresholds for performance, but measure first. Large leaks usually come from **live references** (global caches, ever-growing lists, closures), not from the GC failing.

---

### 12.5 Weak References

**Definition:** a weak reference points to an object **without increasing its reference count**, so it does not keep the object alive. Use it for caches and registries that should not prevent cleanup.

```python
import weakref


class Schema:
    def __init__(self, name: str) -> None:
        self.name = name


cache: weakref.WeakValueDictionary[str, Schema] = weakref.WeakValueDictionary()
orders_schema = Schema("orders")
cache["orders"] = orders_schema
print("orders" in cache)
del orders_schema                     # last strong reference gone
print("orders" in cache)

ref = weakref.ref(Schema("temp"))
print(ref())                          # None: the object was already freed
```

**Output:**

```text
True
False
None
```

Not every object supports weak references: `int`, `str`, `tuple` and `list` do not.

---

### 12.6 Copy Semantics

| Operation | New outer object? | Nested objects | Example |
|---|---|---|---|
| Assignment | No | shared | `b = a` |
| Shallow copy | Yes | **shared** | `copy.copy(a)`, `a.copy()`, `list(a)`, `a[:]`, `{**a}` |
| Deep copy | Yes | recursively copied | `copy.deepcopy(a)` |

- Immutable objects are never really copied: `copy.copy((1, 2))` returns the same tuple.
- `deepcopy` handles cycles (it keeps a memo of already-copied objects) and can be customised with `__copy__` / `__deepcopy__`.
- **Production tip:** prefer **immutable** data (tuples, frozen dataclasses) and functions that return new objects. Then copying is rarely necessary.

See [2.9](#29-shallow-copy-versus-deep-copy) for the worked example.

---

### 12.7 Interning

**Definition:** **interning** reuses a single object for equal immutable values to save memory and speed up comparisons.
- CPython pre-creates the **small integers -5 to 256**.
- Identifier-like **string literals** are interned automatically; other strings can be interned with `sys.intern()`.
- Equal constants in the same compiled code block may also be shared.

```python
import sys

print(int("100") is int("100"))        # small-int cache
print(int("1000") is int("1000"))      # separate objects created at run time
literal = "data_lake"
built = "".join(["data", "_lake"])
print(built == literal, built is literal)      # equal value, different objects
print(sys.intern(built) is literal)            # interning returns the canonical object
```

**Output:**

```text
True
False
True False
True
```

**Interview point:** this is **why `is` must not be used to compare values**. The results depend on implementation details. Interning large numbers of repeated strings (e.g. country codes in millions of records) with `sys.intern` can save memory; pandas `category` dtype does the same for columns.

---

### 12.8 `__slots__`

**Definition:** declaring `__slots__` tells Python to store a fixed set of attributes in a compact array instead of a per-instance `__dict__`. Instances use less memory, attribute access is slightly faster, and **new attributes cannot be added**.

```python
import sys


class RowDict:
    def __init__(self, order_id: int, amount: float) -> None:
        self.order_id, self.amount = order_id, amount


class RowSlots:
    __slots__ = ("order_id", "amount")

    def __init__(self, order_id: int, amount: float) -> None:
        self.order_id, self.amount = order_id, amount


regular, slotted = RowDict(1, 9.5), RowSlots(1, 9.5)
regular_size = sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)
print(hasattr(slotted, "__dict__"), sys.getsizeof(slotted) < regular_size)
try:
    slotted.typo_field = 1
except AttributeError as error:
    print("AttributeError:", error)
```

**Output:**

```text
False True
AttributeError: 'RowSlots' object has no attribute 'typo_field'
```

**When to use:** classes with **millions of instances** (records, graph nodes), or when you want to forbid accidental attributes. `@dataclass(slots=True)` (3.10+) does this for you. **Limitations:** no dynamic attributes, multiple inheritance with slots is tricky, and you need `"__weakref__"` in the slots to support weak references.

---

### 12.9 Dynamic Attribute Access

`getattr`, `setattr`, `hasattr` and `delattr` work with attribute names held in strings. `__getattr__` is called **only when normal lookup fails**, which is useful for proxies and wrappers.

```python
class Settings:
    def __init__(self, values: dict) -> None:
        self._values = values

    def __getattr__(self, name: str):
        try:
            return self._values[name]
        except KeyError:
            raise AttributeError(f"no setting {name!r}") from None


settings = Settings({"batch_size": 500, "region": "eu-west-1"})
print(settings.batch_size, getattr(settings, "region"), getattr(settings, "timeout", 30))
setattr(settings, "env", "prod")
print(settings.env, hasattr(settings, "missing"))
```

**Output:**

```text
500 eu-west-1 30
prod False
```

---

### 12.10 Descriptors and @property Internals

**Definition:** a **descriptor** is an object, stored as a **class attribute**, that defines `__get__`, and optionally `__set__` / `__delete__`. It controls what happens when the attribute is read or written **on instances**.
- **Data descriptor**: defines `__set__` or `__delete__`. It takes priority over the instance `__dict__`. `property` is one.
- **Non-data descriptor**: only `__get__`. The instance `__dict__` wins. **Functions** are non-data descriptors; that is how `obj.method` becomes a bound method.

**Attribute lookup order for `obj.name`:** data descriptor on the class → `obj.__dict__` → non-data descriptor or class attribute → `__getattr__`.

**Data Engineering example – reusable validated fields:**

```python
class PositiveNumber:
    """A data descriptor that validates on assignment."""

    def __set_name__(self, owner: type, name: str) -> None:
        self.public_name, self.private_name = name, f"_{name}"

    def __get__(self, instance, owner=None):
        if instance is None:
            return self                      # accessed on the class itself
        return getattr(instance, self.private_name)

    def __set__(self, instance, value) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
            raise ValueError(f"{self.public_name} must be a positive number, got {value!r}")
        setattr(instance, self.private_name, value)


class LoadConfig:
    batch_size = PositiveNumber()
    timeout_seconds = PositiveNumber()

    def __init__(self, batch_size: int, timeout_seconds: float) -> None:
        self.batch_size = batch_size          # goes through PositiveNumber.__set__
        self.timeout_seconds = timeout_seconds


config = LoadConfig(1000, 2.5)
print(config.batch_size, config.timeout_seconds, type(LoadConfig.batch_size).__name__)
try:
    config.timeout_seconds = -1
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
1000 2.5 PositiveNumber
ValueError: timeout_seconds must be a positive number, got -1
```

**How `@property` works:** `property(fget, fset, fdel)` is a built-in data descriptor class. `@property` creates one with your getter, and `@x.setter` returns a **new** property object with the setter added. Writing a descriptor is "property, but reusable across many attributes and classes". ORMs (SQLAlchemy columns) and validation libraries are built this way.

---

### 12.11 Metaclasses

**Definition:** a **metaclass** is the "class of a class": it creates and configures classes, just as a class creates instances. The default metaclass is `type`. `class Foo: ...` is roughly `Foo = type("Foo", (object,), {...namespace...})`.

```python
DynamicRecord = type("DynamicRecord", (), {"source": "api", "describe": lambda self: f"from {self.source}"})
print(DynamicRecord().describe(), type(DynamicRecord).__name__, type(type).__name__)


class PluginRegistry(type):
    """Metaclass that registers every concrete subclass by its `name`."""
    plugins: dict[str, type] = {}

    def __new__(mcs, class_name, bases, namespace):
        cls = super().__new__(mcs, class_name, bases, namespace)
        if bases:                                   # skip the abstract base itself
            mcs.plugins[namespace["name"]] = cls
        return cls


class Connector(metaclass=PluginRegistry):
    name = "base"


class SnowflakeConnector(Connector):
    name = "snowflake"


class PostgresConnector(Connector):
    name = "postgres"


print(sorted(PluginRegistry.plugins))
```

**Output:**

```text
from api type type
['postgres', 'snowflake']
```

**Simpler alternative (preferred in most code): `__init_subclass__` (3.6+):**

```python
class Connector:
    registry: dict[str, type] = {}

    def __init_subclass__(cls, *, name: str, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        Connector.registry[name] = cls


class S3Connector(Connector, name="s3"):
    pass


print(Connector.registry)
```

**Output:**

```text
{'s3': <class '__main__.S3Connector'>}
```

**Interview-level answer:** metaclasses customise **class creation** (registration, validation of class definitions, automatic method generation). Frameworks such as Django models, SQLAlchemy and ABCs (`ABCMeta`) use them. In application code, class decorators and `__init_subclass__` are simpler and usually enough.

---

### 12.12 Monkey Patching

**Definition:** replacing attributes of modules or classes **at run time**.

```python
import json


class ApiClient:
    def fetch(self) -> dict:
        raise ConnectionError("real network call")


def fake_fetch(self) -> dict:
    return {"status": "ok"}


original = ApiClient.fetch
ApiClient.fetch = fake_fetch           # monkey patch (affects every instance)
print(json.dumps(ApiClient().fetch()))
ApiClient.fetch = original             # always restore
```

**Output:**

```text
{"status": "ok"}
```

**When it's acceptable:** in **tests**, and there you should prefer `unittest.mock.patch` or pytest's `monkeypatch` fixture, which restore the original automatically (see [18.4](#184-mocking)). Also for urgent hot-fixes of third-party bugs (documented and temporary). **In production code it is a smell:** it causes action at a distance, depends on import order, and is hard to debug.

---

### 12.13 Duck Typing in Depth

Python code typically checks **behaviour, not type**: "does it have `.read()`?" rather than "is it a `FileReader`?". This lets file objects, `io.StringIO`, `gzip` files and S3 streaming bodies all be passed to the same function. Make the expected behaviour explicit with `typing.Protocol` (see [7.9](#79-polymorphism-and-duck-typing)), and use `isinstance` checks only at system boundaries (validating input) or when behaviour truly differs by type (`functools.singledispatch`, [12.18](#1218-functools-module)).

---

### 12.14 Method Resolution Order Revisited

- The MRO is computed with **C3 linearisation**: a child before its parents, parents in the order listed, and a consistent order across the hierarchy. If no consistent order exists, the class definition fails with `TypeError: Cannot create a consistent method resolution order (MRO)`.
- `super()` delegates to the **next class in the MRO of the instance**, not necessarily the parent written in the source.
- Inspect it with `ClassName.__mro__` or `ClassName.mro()`.

```python
class A: ...
class B(A): ...
class C(A): ...
class D(B, C): ...


print([cls.__name__ for cls in D.mro()])
try:
    class Broken(A, B):     # A listed before its own subclass B: impossible order
        pass
except TypeError as error:
    print("TypeError:", " ".join(str(error).split()))   # the message contains a line break
```

**Output:**

```text
['D', 'B', 'C', 'A', 'object']
TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
```

---

### 12.15 EAFP versus LBYL

| Style | Meaning | Example |
|---|---|---|
| **LBYL** – Look Before You Leap | check conditions first | `if key in row: value = row[key]` |
| **EAFP** – Easier to Ask Forgiveness than Permission | try it and handle the failure | `try: value = row[key] except KeyError: ...` |

**Why Python prefers EAFP:**
- It avoids **race conditions** (time-of-check vs time-of-use). A file can be deleted between `os.path.exists(path)` and `open(path)`.
- It is often faster when failures are rare (one operation instead of check plus operation).
- It handles every failure mode, not just the ones you thought to check.

```python
import os

path = "maybe_missing.csv"

# LBYL: racy, because the file may disappear between the check and the open
if os.path.exists(path):
    with open(path, encoding="utf-8") as file:
        content = file.read()
else:
    content = None

# EAFP: one atomic attempt
try:
    with open(path, encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    content = None
print(content)
```

**Output:**

```text
None
```

**When LBYL is better:** when failure is **common** (exceptions are relatively expensive in hot loops), or when the check is cheap and clearer (`if not rows: return`).

---

### 12.16 Serialization and Deserialization

**Definition:** **serialization** turns in-memory objects into bytes or text for storage or transmission; **deserialization** reverses it.

| Format | Human-readable | Typed schema | Language-neutral | Typical DE use |
|---|---|---|---|---|
| JSON / JSON Lines | Yes | No | Yes | APIs, events, configs |
| CSV | Yes | No | Yes | exchange with business systems |
| YAML | Yes | No | Yes | configuration |
| Parquet / ORC | No | Yes (columnar) | Yes | data lakes, analytics |
| Avro | No | Yes (row-based, schema evolution) | Yes | Kafka, streaming |
| Protocol Buffers | No | Yes | Yes | gRPC, compact events |
| pickle | No | Python objects | **No** | short-lived Python-to-Python transfer, caches |

```python
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class Event:
    event_id: int
    occurred_at: datetime


def encode(event: Event) -> str:
    payload = asdict(event)
    payload["occurred_at"] = event.occurred_at.isoformat()
    return json.dumps(payload)


def decode(text: str) -> Event:
    payload = json.loads(text)
    return Event(payload["event_id"], datetime.fromisoformat(payload["occurred_at"]))


original = Event(7, datetime(2026, 10, 29, 14, 5, tzinfo=timezone.utc))
wire = encode(original)
print(wire)
print(decode(wire) == original)
```

**Output:**

```text
{"event_id": 7, "occurred_at": "2026-10-29T14:05:00+00:00"}
True
```

---

### 12.17 Pickle Risks and Safer Alternatives

**Definition:** `pickle` serialises almost any Python object to a binary format. It is used internally by `multiprocessing` and by some caches.

**The risk:** **unpickling runs code.** A pickle can instruct Python to call any function during loading (via `__reduce__`). **Never unpickle data from an untrusted or unauthenticated source.** This harmless demonstration shows that code runs during `pickle.loads`:

```python
import pickle


class Surprise:
    def __reduce__(self):
        return (print, ("this ran during unpickling!",))


blob = pickle.dumps(Surprise())
pickle.loads(blob)
```

**Output:**

```text
this ran during unpickling!
```

**Other limitations:** pickles are Python-only, can break across library or Python versions, and are not suitable for long-term storage or for exchange between systems.

**Safer alternatives:** JSON (with explicit encode/decode), Parquet or Arrow for tabular data, Avro or Protobuf for typed messages. If you must use pickle across a trust boundary, sign it (`hmac`) and verify the signature before loading.

---

### 12.18 functools Module

```python
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from functools import cached_property, partial, reduce, singledispatch, total_ordering


def load(table: str, *, mode: str, batch_size: int) -> str:
    return f"{table}:{mode}:{batch_size}"


overwrite_loader = partial(load, mode="overwrite", batch_size=1000)   # pre-fill arguments
print(overwrite_loader("sales"))

print(reduce(lambda acc, part: f"{acc}/{part}", ["s3:", "", "lake", "raw"]))


@singledispatch
def to_sql_literal(value) -> str:                 # dispatch on the type of the first argument
    raise TypeError(f"unsupported type {type(value).__name__}")


@to_sql_literal.register
def _(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


@to_sql_literal.register
def _(value: int | Decimal) -> str:               # union types are accepted in 3.11+
    return str(value)


@to_sql_literal.register
def _(value: date) -> str:
    return f"DATE '{value.isoformat()}'"


@to_sql_literal.register(type(None))
def _(value) -> str:
    return "NULL"


print([to_sql_literal(v) for v in ("O'Brien", 42, Decimal("9.99"), date(2026, 1, 2), None)])


@total_ordering
@dataclass(frozen=True)
class SchemaVersion:
    major: int
    minor: int

    def __lt__(self, other: "SchemaVersion") -> bool:
        return (self.major, self.minor) < (other.major, other.minor)


print(SchemaVersion(1, 10) > SchemaVersion(1, 9), max(SchemaVersion(2, 0), SchemaVersion(1, 99)))


class Report:
    def __init__(self, rows: list[int]) -> None:
        self.rows = rows

    @cached_property
    def total(self) -> int:                       # computed once, then stored on the instance
        print("computing total...")
        return sum(self.rows)


report = Report([1, 2, 3])
print(report.total, report.total)
```

**Output:**

```text
sales:overwrite:1000
s3://lake/raw
["'O''Brien'", '42', '9.99', "DATE '2026-01-02'", 'NULL']
True SchemaVersion(major=2, minor=0)
computing total...
6 6
```

| Tool | Purpose |
|---|---|
| `partial` | fix some arguments of a function (callbacks, configured loaders) |
| `reduce` | fold a sequence into one value |
| `lru_cache` / `cache` | memoise results ([11.4](#114-caching-decorators)) |
| `cached_property` | compute an attribute once per instance |
| `singledispatch` | function overloading by argument type |
| `total_ordering` | derive all comparisons from `__eq__` and one of `__lt__`/`__gt__`… |
| `wraps` | preserve metadata in decorators |

The `to_sql_literal` function illustrates `singledispatch`. **To pass values into real SQL statements, always use parameterised queries** ([14.3](#143-executing-parameterized-sql)).

---

### 12.19 itertools Module

```python
from itertools import (accumulate, batched, chain, combinations, count, dropwhile, groupby, islice,
                       pairwise, permutations, product, starmap, takewhile, tee)

print(list(chain([1, 2], [3])), list(chain.from_iterable([[1], [2, 3]])))
print(list(islice(count(10, 5), 3)))
print(list(accumulate([1, 2, 3, 4])), list(accumulate([3, 1, 4], max)))
print(list(product("ab", [1, 2])))
print(list(combinations("abc", 2)), list(permutations("ab")))
print(list(pairwise([10, 12, 15])))                                # 3.10+
print(list(takewhile(lambda v: v < 3, [1, 2, 5, 1])), list(dropwhile(lambda v: v < 3, [1, 2, 5, 1])))
print(list(starmap(pow, [(2, 3), (3, 2)])))
print(list(batched(range(5), 2)))                                  # 3.12+

regions = ["EU", "EU", "US", "EU"]
print([(key, len(list(group))) for key, group in groupby(regions)])            # consecutive only!
print([(key, len(list(group))) for key, group in groupby(sorted(regions))])

first_reader, second_reader = tee(iter([1, 2, 3]))
print(list(first_reader), list(second_reader))
```

**Output:**

```text
[1, 2, 3] [1, 2, 3]
[10, 15, 20]
[1, 3, 6, 10] [3, 3, 4]
[('a', 1), ('a', 2), ('b', 1), ('b', 2)]
[('a', 'b'), ('a', 'c'), ('b', 'c')] [('a', 'b'), ('b', 'a')]
[(10, 12), (12, 15)]
[1, 2] [5, 1]
[8, 9]
[(0, 1), (2, 3), (4,)]
[('EU', 2), ('US', 1), ('EU', 1)]
[('EU', 3), ('US', 1)]
[1, 2, 3] [1, 2, 3]
```

| Tool | Data Engineering use |
|---|---|
| `chain` / `chain.from_iterable` | read many files or pages as one stream |
| `islice` | batching, previewing the first N rows |
| `groupby` | streaming group-by over **sorted** input (e.g. `ORDER BY` results) |
| `accumulate` | running totals, running max |
| `pairwise` | differences between consecutive events (gaps, durations) |
| `product` / `combinations` | parameter grids, comparing every pair of datasets |
| `batched` | fixed-size batches (3.12+; use `islice` on older versions) |
| `tee` | split one iterator into several (buffers items in memory) |

**Trap:** `groupby` groups only **adjacent** equal keys. Sort by the same key first, or make sure the input is already ordered.

---

### 12.20 collections Module

```python
from collections import ChainMap, Counter, OrderedDict, defaultdict, deque, namedtuple

# Counter: counting and top-N
status_counts = Counter(["ok", "error", "ok", "ok", "timeout"])
print(status_counts.most_common(2), status_counts["missing"])
print(Counter("mississippi").most_common(2))
print(Counter(a=3, b=1) - Counter(a=1, b=2), Counter(a=1) + Counter(a=2, b=1))

# defaultdict: grouping without key checks
orders_by_region = defaultdict(list)
for region, order_id in [("EU", 1), ("US", 2), ("EU", 3)]:
    orders_by_region[region].append(order_id)
print(dict(orders_by_region))

# deque: O(1) at both ends, bounded windows
recent = deque(maxlen=3)
recent.extend([1, 2, 3, 4])
recent.appendleft(0)
print(recent)
print(recent.popleft(), recent)

# namedtuple: immutable record with field names
Row = namedtuple("Row", ["order_id", "amount"])
row = Row(1, 9.5)
print(row.amount, row._asdict(), row._replace(amount=0.0))

# OrderedDict: order-aware operations (LRU caches)
lru = OrderedDict(a=1, b=2, c=3)
lru.move_to_end("a")
print(list(lru), lru.popitem(last=False))

# ChainMap: layered configuration lookup (first mapping wins)
defaults = {"batch_size": 500, "env": "dev"}
env_vars = {"env": "prod"}
cli_args = {"batch_size": 2000}
config = ChainMap(cli_args, env_vars, defaults)
print(config["batch_size"], config["env"], dict(config))
```

**Output:**

```text
[('ok', 3), ('error', 1)] 0
[('i', 4), ('s', 4)]
Counter({'a': 2}) Counter({'a': 3, 'b': 1})
{'EU': [1, 3], 'US': [2]}
deque([0, 2, 3], maxlen=3)
0 deque([2, 3], maxlen=3)
9.5 {'order_id': 1, 'amount': 9.5} Row(order_id=1, amount=0.0)
['b', 'c', 'a'] ('b', 2)
2000 prod {'batch_size': 2000, 'env': 'prod'}
```

| Type | Key behaviour | DE use |
|---|---|---|
| `Counter` | missing keys count as 0; `most_common`; `+`/`-` arithmetic | frequencies, profiling, top-N |
| `defaultdict(factory)` | creates a default value on first access | grouping, adjacency lists |
| `deque(maxlen=n)` | O(1) append/pop at both ends; drops the oldest items | sliding windows, queues, BFS |
| `namedtuple` | tuple with named fields | lightweight immutable rows |
| `OrderedDict` | `move_to_end`, `popitem(last=False)`, order-sensitive equality | LRU caches |
| `ChainMap` | searches several dicts in order | CLI > env > defaults configuration |

Note: `appendleft(0)` on a full deque with `maxlen=3` drops the item at the **right** end, which is why the result is `[0, 2, 3]`.

---

### 12.21 operator Module

`operator` provides fast, picklable functions for common operations. They are clearer than lambdas for keys and reductions.

```python
from functools import reduce
from operator import add, attrgetter, itemgetter, methodcaller, mul
from collections import namedtuple

rows = [{"region": "US", "amount": 5}, {"region": "EU", "amount": 9}, {"region": "EU", "amount": 2}]
print([r["amount"] for r in sorted(rows, key=itemgetter("region", "amount"))])
print(itemgetter("region", "amount")(rows[0]))

Employee = namedtuple("Employee", "name salary")
staff = [Employee("Bo", 70), Employee("Al", 90)]
print(max(staff, key=attrgetter("salary")).name)

print(list(map(methodcaller("strip"), [" a ", "b "])), reduce(add, [1, 2, 3]), reduce(mul, [2, 3, 4]))
```

**Output:**

```text
[2, 9, 5]
('US', 5)
Al
['a', 'b'] 6 24
```

---

### Chapter 12 Review

**Key takeaways**
- CPython uses reference counting plus a cyclic GC; freed memory is not always returned to the OS.
- Never use `is` for values; interning and small-int caching are implementation details.
- `__slots__` saves memory for many small objects; `dataclass(slots=True)` makes it easy.
- `property` is a data descriptor; descriptors power validated fields and ORMs.
- Metaclasses customise class creation; prefer `__init_subclass__` or decorators.
- EAFP is idiomatic and avoids races; LBYL is fine when failures are common.
- Never unpickle untrusted data.
- Know Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap, partial, singledispatch, groupby (sorted!), islice.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How does Python free memory? | Reference counting, plus a generational GC for cycles. |
| What is a memory leak in Python? | Usually objects kept alive by lingering references (caches, globals, closures). |
| What is a descriptor? | A class attribute with `__get__`/`__set__` that controls attribute access. |
| What is a metaclass? | The class of a class (`type` by default); it controls class creation. |
| What does `__slots__` do? | Removes the per-instance `__dict__`, saving memory and forbidding new attributes. |
| Why is pickle dangerous? | Loading a pickle can execute arbitrary code. |
| Monkey patching? | Replacing attributes at run time; acceptable in tests via `mock.patch`. |

**Common traps:** `groupby` without sorting; `lru_cache` on methods; `tee` buffering huge streams; relying on `sys.getsizeof` for total memory; pickling across versions.

**Practice exercise:** Implement an `LRUCache(capacity)` class with `get(key)` and `put(key, value)` using `OrderedDict` (both O(1)). Then write a variant that also expires entries older than `ttl_seconds`. A solution for the first part is in [20.12](#2012-design-problems).

---

## 13. Concurrency and Parallelism

### 13.1 Process versus Thread

| | Process | Thread |
|---|---|---|
| What it is | an independent running program with its **own memory space** | a path of execution **inside** a process, sharing its memory |
| Creation cost | higher (new interpreter, imports) | low |
| Sharing data | explicit: pickling, pipes, queues, shared memory | implicit: same objects (needs locks) |
| Crash isolation | a crash kills only that process | an unhandled crash can affect the whole process |
| Python GIL | each process has its own GIL → **true parallel CPU work** | threads share one GIL → one runs Python bytecode at a time |

---

### 13.2 Concurrency versus Parallelism

- **Concurrency** is *dealing with* many tasks at once by interleaving them. One cook switches between pots while each simmers.
- **Parallelism** is *doing* many tasks at the same instant on multiple CPU cores. Several cooks each work on their own pot.

Threads and `asyncio` give **concurrency**: great when tasks spend time **waiting**. Multiple processes give **parallelism**: needed when tasks spend time **computing**.

---

### 13.3 The Global Interpreter Lock (GIL)

**Definition:** in CPython, the GIL is a mutex that allows **only one thread at a time to execute Python bytecode** in a process. It simplifies memory management (reference counts don't need fine-grained locks).

**How it works – what interviewers want to hear:**
- A thread **releases the GIL while waiting on I/O** (socket reads, file reads, `time.sleep`, database calls), so other threads run in the meantime. Threads therefore **do** speed up I/O-bound work.
- Pure-Python **CPU-bound** threads take turns holding the GIL, so they get no speed-up, and switching even adds overhead.
- C extensions (NumPy, pandas internals, compression, hashing libraries, `hashlib` on large data) can release the GIL during heavy computation.
- **Python 3.13+** offers an experimental **free-threaded build** (PEP 703) without the GIL. Standard builds still have it, so the classic advice still applies in production.

**Interview question:** *Does the GIL make Python code thread-safe?*
**Answer:** No. The GIL protects the interpreter's internals, not your logic. A read-modify-write such as `counter += 1` is several bytecode steps, and a thread switch can happen between them. Use locks (see [13.6](#136-race-conditions-and-locks)).

---

### 13.4 CPU-Bound versus I/O-Bound Workloads

| Workload type | Bottleneck | Data Engineering examples | Best tool |
|---|---|---|---|
| **I/O-bound** | waiting on network or disk | downloading S3 objects, calling REST APIs, DB queries, uploading files | threads (`ThreadPoolExecutor`) or `asyncio` |
| **CPU-bound** | computation in Python code | parsing / transforming millions of records in pure Python, compression, hashing, regex over huge text | processes (`ProcessPoolExecutor`), vectorised libraries, Spark |
| Mixed | both | download a file, then parse it | threads for the download stage, processes (or vectorisation) for parsing |

**First question in practice:** can the work be **pushed down** to a faster engine (SQL in the warehouse, pandas/Polars vectorisation, Spark)? That often beats any amount of Python-level parallelism.

---

### 13.5 threading Module

```python
import threading
import time

results: dict[str, str] = {}


def fetch(source: str) -> None:
    time.sleep(0.2)                         # simulated I/O wait (releases the GIL)
    results[source] = f"{source}: done"     # each thread writes a different key


started = time.perf_counter()
threads = [threading.Thread(target=fetch, args=(name,), name=f"fetch-{name}") for name in ("crm", "erp", "web")]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()                           # wait for all threads to finish
elapsed = time.perf_counter() - started
print(sorted(results.values()), elapsed < 0.5)  # ~0.2s total, not 0.6s
```

**Output:**

```text
['crm: done', 'erp: done', 'web: done'] True
```

- `daemon=True` threads are killed abruptly when the main program exits. Never use them for work that must complete (writes, uploads).
- Exceptions inside a `Thread` target **do not propagate** to the caller of `join()`; they are only printed. `concurrent.futures` (see [13.11](#1311-concurrentfutures-threadpoolexecutor-and-processpoolexecutor)) solves this, so prefer it.

---

### 13.6 Race Conditions and Locks

**Definition:** a **race condition** happens when the result depends on the unpredictable timing of threads that access shared, mutable data. A **lock** (mutex) makes a block of code **mutually exclusive**: only one thread at a time.

```python
import threading
import time

counter = 0
lock = threading.Lock()


def unsafe_increment(times: int) -> None:
    global counter
    for _ in range(times):
        current = counter          # read
        time.sleep(0)              # a thread switch here exposes the race
        counter = current + 1      # write (may overwrite another thread's update)


def safe_increment(times: int) -> None:
    global counter
    for _ in range(times):
        with lock:                 # acquire ... release, even on exceptions
            current = counter
            time.sleep(0)
            counter = current + 1


for worker in (unsafe_increment, safe_increment):
    counter = 0
    threads = [threading.Thread(target=worker, args=(500,)) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(worker.__name__, "lost updates:", counter < 2000, "| final:", counter if worker is safe_increment else "varies")
```

**Output:**

```text
unsafe_increment lost updates: True | final: varies
safe_increment lost updates: False | final: 2000
```

**Other synchronisation tools:**

| Tool | Purpose |
|---|---|
| `Lock` | mutual exclusion |
| `RLock` | a lock the **same thread** can acquire repeatedly (re-entrant) |
| `Semaphore(n)` | at most *n* threads inside a block (connection or rate limits) |
| `Event` | one thread signals others (e.g. "stop now") |
| `Condition` | wait until some state changes |
| `Barrier(n)` | wait until *n* threads reach a point |
| `queue.Queue` | thread-safe hand-off of work (often removes the need for explicit locks) |

**Best practice:** avoid sharing mutable state. Have each task **return** its result (futures) or communicate through a `Queue`.

---

### 13.7 Deadlocks

**Definition:** two or more threads each hold a lock and wait for a lock held by the other, so neither can continue. Classic cause: **acquiring the same locks in different orders**.

```python
import threading

lock_orders, lock_inventory = threading.Lock(), threading.Lock()
both_hold_first_lock = threading.Barrier(2)
outcomes: dict[str, str] = {}


def worker(name: str, first: threading.Lock, second: threading.Lock) -> None:
    with first:
        both_hold_first_lock.wait()                 # force the bad interleaving
        if second.acquire(timeout=0.2):             # a timeout prevents hanging forever
            second.release()
            outcomes[name] = "finished"
        else:
            outcomes[name] = "timed out: possible deadlock"


t1 = threading.Thread(target=worker, args=("t1", lock_orders, lock_inventory))
t2 = threading.Thread(target=worker, args=("t2", lock_inventory, lock_orders))   # opposite order!
t1.start(); t2.start(); t1.join(); t2.join()
print(outcomes["t1"], "|", outcomes["t2"])
```

**Output:**

```text
timed out: possible deadlock | timed out: possible deadlock
```

**Prevention:**
1. Always acquire locks in **one global order**.
2. Hold locks for the shortest possible time; never do I/O while holding a lock if you can avoid it.
3. Use timeouts (`acquire(timeout=...)`) and log when they fire.
4. Prefer higher-level tools (queues, futures) that avoid manual locking.

The same idea applies to **databases**: two transactions updating the same rows in opposite orders deadlock. The database kills one of them, which your code should retry.

---

### 13.8 Semaphores and Rate Limiting

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

api_slots = threading.Semaphore(2)          # at most 2 concurrent calls to the API
active = peak = 0
state_lock = threading.Lock()


def call_api(page: int) -> int:
    global active, peak
    with api_slots:
        with state_lock:
            active += 1
            peak = max(peak, active)
        time.sleep(0.05)                    # simulated request
        with state_lock:
            active -= 1
    return page


with ThreadPoolExecutor(max_workers=8) as pool:
    pages = list(pool.map(call_api, range(10)))
print(pages, "peak concurrency:", peak)
```

**Output:**

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] peak concurrency: 2
```

`pool.map` returns results **in input order**, even though tasks finish in any order. A semaphore limits **concurrency**. To limit **requests per second**, use a token bucket or a fixed sleep between calls (see [15.18](#1518-rate-limiting)).

---

### 13.9 Queues and the Producer-Consumer Pattern

**Definition:** producers put work items on a thread-safe `queue.Queue`; consumers take them off. A bounded queue (`maxsize`) provides **backpressure**: fast producers block instead of filling memory.

```python
import queue
import threading

work: queue.Queue = queue.Queue(maxsize=5)
results: list[int] = []
results_lock = threading.Lock()
STOP = object()                                   # sentinel that tells consumers to exit


def producer(count: int) -> None:
    for record_id in range(1, count + 1):
        work.put(record_id)                       # blocks when the queue is full


def consumer() -> None:
    while True:
        item = work.get()
        try:
            if item is STOP:
                return
            with results_lock:
                results.append(item * 10)
        finally:
            work.task_done()


consumers = [threading.Thread(target=consumer) for _ in range(3)]
for thread in consumers:
    thread.start()
producer(12)
for _ in consumers:
    work.put(STOP)                                # one sentinel per consumer
for thread in consumers:
    thread.join()
print(sorted(results)[:4], len(results))
```

**Output:**

```text
[10, 20, 30, 40] 12
```

`multiprocessing.Queue` and `asyncio.Queue` follow the same pattern for processes and coroutines.

---

### 13.10 multiprocessing Module

**Definition:** runs functions in **separate processes**, each with its own interpreter and GIL, so CPU-bound Python code runs in parallel on several cores.

```python
import multiprocessing as mp


def checksum(chunk: range) -> int:
    """CPU-bound work: pure Python arithmetic."""
    return sum(value * value % 7 for value in chunk)


if __name__ == "__main__":                       # REQUIRED with the spawn start method
    chunks = [range(start, start + 250_000) for start in range(0, 1_000_000, 250_000)]
    with mp.Pool(processes=4) as pool:
        partials = pool.map(checksum, chunks)
    print(len(partials), sum(partials) == checksum(range(1_000_000)))
```

**Output:**

```text
4 True
```

**Key facts:**
- **Start methods:** `spawn` (the default on Windows and macOS) starts a fresh interpreter and **re-imports your main module**, hence the `if __name__ == "__main__":` guard. `fork` (the Linux default until Python 3.14) copies the parent process, which is fast but unsafe with threads.
- Arguments and results are **pickled** to cross process boundaries. Send small inputs (file paths, offsets), not big DataFrames. Lambdas and locally defined functions cannot be pickled.
- Process start-up costs from milliseconds to seconds, so give each process substantial work (use `chunksize` with many small items).
- Shared state is explicit: `multiprocessing.Value`, `Array`, `Manager`, or `shared_memory`.

---

### 13.11 concurrent.futures: ThreadPoolExecutor and ProcessPoolExecutor

**Definition:** a high-level, uniform API for running callables in a pool of threads or processes. `submit()` returns a **Future**, a handle to a result that will be available later. `Future.result()` returns the value **or re-raises the task's exception**.

| API | Behaviour |
|---|---|
| `pool.submit(fn, *args)` | schedule one call; returns a `Future` |
| `pool.map(fn, iterable, timeout=None, chunksize=1)` | results in **input order**; an exception is raised when you reach that result |
| `as_completed(futures, timeout=None)` | yields futures **as they finish** |
| `wait(futures, return_when=FIRST_EXCEPTION)` | wait for a condition |
| `future.result(timeout)` / `future.exception()` | get the value or re-raise / inspect the error |
| `pool.shutdown(wait=True, cancel_futures=False)` | stop the pool (called automatically by `with`) |

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import time


def download(key: str) -> int:
    time.sleep(0.05)                                  # I/O simulation
    if key.endswith("bad.csv"):
        raise ConnectionError(f"timeout downloading {key}")
    return len(key)


def parse(size: int) -> int:                          # CPU simulation
    return sum(range(size * 10_000))


if __name__ == "__main__":
    keys = ["raw/a.csv", "raw/b.csv", "raw/bad.csv", "raw/c.csv"]
    sizes, failures = {}, {}
    with ThreadPoolExecutor(max_workers=4) as pool:
        future_to_key = {pool.submit(download, key): key for key in keys}
        for future in as_completed(future_to_key):
            key = future_to_key[future]
            try:
                sizes[key] = future.result()
            except ConnectionError as error:
                failures[key] = str(error)
    print(sorted(sizes), failures)

    with ProcessPoolExecutor(max_workers=2) as pool:
        parsed = list(pool.map(parse, sizes.values()))
    print(len(parsed), all(value > 0 for value in parsed))
```

**Output:**

```text
['raw/a.csv', 'raw/b.csv', 'raw/c.csv'] {'raw/bad.csv': 'timeout downloading raw/bad.csv'}
3 True
```

**Choosing `max_workers`:** for I/O-bound threads, start around 8–32 and stay below the remote service's limits (S3, API rate limits, the DB connection pool size). For CPU-bound processes, use about the number of CPU cores (`os.cpu_count()`).

---

### 13.12 asyncio: Coroutines, Tasks and the Event Loop

**Definitions:**
- **Coroutine** – a function defined with `async def`. Calling it returns a coroutine object; nothing runs until it is awaited or scheduled.
- **`await`** – pauses the current coroutine until the awaited operation completes, giving control back to the event loop so **other coroutines run meanwhile**.
- **Event loop** – a single-threaded scheduler that runs coroutines, switching between them at `await` points. `asyncio.run(main())` creates it and runs it.
- **Task** – a coroutine scheduled to run concurrently (`asyncio.create_task`, `asyncio.TaskGroup` in 3.11+, `asyncio.gather`).

**Why it matters for a Data Engineer:** one thread can manage **thousands** of concurrent network calls (APIs, websockets, async DB drivers) with low memory, which suits high-fan-out API ingestion. Every library involved must be **async-aware** (`aiohttp`/`httpx`, `asyncpg`, `aioboto3`). One blocking call (`requests.get`, `time.sleep`) freezes the whole loop.

```python
import asyncio
import time


async def fetch_page(page: int, limiter: asyncio.Semaphore) -> dict:
    async with limiter:                               # at most N requests in flight
        await asyncio.sleep(0.1)                      # stands in for `await client.get(...)`
        if page == 4:
            raise TimeoutError(f"page {page} timed out")
        return {"page": page, "rows": page * 10}


async def main() -> None:
    limiter = asyncio.Semaphore(5)
    started = time.perf_counter()
    results = await asyncio.gather(*(fetch_page(page, limiter) for page in range(1, 11)),
                                   return_exceptions=True)        # collect errors, don't cancel the rest
    elapsed = time.perf_counter() - started
    rows = sum(result["rows"] for result in results if isinstance(result, dict))
    errors = [str(result) for result in results if isinstance(result, Exception)]
    print(rows, errors, "fast:", elapsed < 0.5)        # 10 pages x 0.1s with 5 in parallel ≈ 0.2s

    try:
        async with asyncio.timeout(0.05):             # 3.11+; use asyncio.wait_for on older versions
            await asyncio.sleep(1)
    except TimeoutError:
        print("operation cancelled after timeout")


asyncio.run(main())
```

**Output:**

```text
510 ['page 4 timed out'] fast: True
operation cancelled after timeout
```

**Running blocking code from async code:** `await asyncio.to_thread(blocking_function, arg)` (3.9+) runs it in a thread without blocking the loop.

**TaskGroup (3.11+)** gives structured concurrency: if one task fails, the others are cancelled and the errors are raised together as an `ExceptionGroup`.

---

### 13.13 Choosing Between threading, multiprocessing and asyncio

| Situation | Choose | Why |
|---|---|---|
| Tens to hundreds of blocking I/O calls with sync libraries (boto3, requests, DB drivers) | `ThreadPoolExecutor` | simple; the GIL is released during I/O |
| Thousands of concurrent network calls, async libraries available | `asyncio` | lowest overhead per connection |
| CPU-heavy pure-Python transformation | `ProcessPoolExecutor` / `multiprocessing` | bypasses the GIL |
| Heavy numeric or tabular work | NumPy / pandas / Polars / DuckDB | vectorised native code, often multi-threaded internally |
| Data larger than one machine | Spark / Dask / Ray | distributed execution |
| Simple, low-volume job | sequential code | easiest to debug; parallelism adds complexity |

---

### 13.14 Parallel File and API Processing Examples

**Production-style – process many files in parallel, bounded, with per-file error isolation:**

```python
import csv
import logging
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("parallel")


@dataclass(frozen=True)
class FileResult:
    path: str
    rows: int
    total_amount: float


def summarize_file(path: str) -> FileResult:
    """CPU-ish work per file; runs in a worker process. Receives only a path (cheap to pickle)."""
    rows, total = 0, 0.0
    with open(path, newline="", encoding="utf-8") as file:
        for record in csv.DictReader(file):
            rows += 1
            total += float(record["amount"])
    return FileResult(Path(path).name, rows, round(total, 2))


def main() -> int:
    folder = Path("landing")
    folder.mkdir(exist_ok=True)
    for number in range(1, 4):
        (folder / f"orders_{number}.csv").write_text(
            "id,amount\n" + "".join(f"{n},{n * number}.5\n" for n in range(1, 4)), encoding="utf-8")
    (folder / "orders_bad.csv").write_text("id,amount\n1,abc\n", encoding="utf-8")

    results, failed = [], []
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = {pool.submit(summarize_file, str(path)): path.name for path in sorted(folder.glob("*.csv"))}
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except (ValueError, KeyError, OSError) as error:
                failed.append(futures[future])
                logger.error("file %s failed: %s", futures[future], error)
    for result in sorted(results, key=lambda r: r.path):
        logger.info("%s rows=%d total=%.2f", result.path, result.rows, result.total_amount)
    return 1 if failed else 0


if __name__ == "__main__":
    print("exit code:", main())
```

**Output:**

```text
ERROR file orders_bad.csv failed: could not convert string to float: 'abc'
INFO orders_1.csv rows=3 total=7.50
INFO orders_2.csv rows=3 total=13.50
INFO orders_3.csv rows=3 total=19.50
exit code: 1
```

Design points: workers receive **paths** (not data); each file succeeds or fails independently; failures are reported and turn into a **non-zero exit code**, so the scheduler notices. In production, write each file's output separately (idempotent per file) and record processed files in a manifest.

---

### 13.15 Error Handling and Safe Shutdown

**Rules:**
1. **Always retrieve results** (`future.result()`), otherwise exceptions in workers are silently lost.
2. Decide the **failure policy**: fail fast (cancel the remaining work) or isolate failures (continue and report).
3. Handle **SIGTERM / Ctrl+C**. Containers and schedulers send SIGTERM before killing a job. Stop taking new work, finish or checkpoint in-flight work, close resources.
4. Use **timeouts** everywhere (`future.result(timeout=...)`, HTTP timeouts, `asyncio.timeout`).

```python
import signal
import threading
import time
from concurrent.futures import FIRST_EXCEPTION, ThreadPoolExecutor, wait

stop_requested = threading.Event()


def handle_sigterm(signum, frame) -> None:
    stop_requested.set()                       # workers check this flag and exit cleanly


signal.signal(signal.SIGTERM, handle_sigterm)  # call from the main thread at start-up


def process_partition(partition: int) -> int:
    for _ in range(5):
        if stop_requested.is_set():
            return -1                          # stop early; the partition will be re-run later
        time.sleep(0.01)
    if partition == 3:
        raise ValueError(f"partition {partition} has corrupt data")
    return partition


with ThreadPoolExecutor(max_workers=2) as pool:
    futures = [pool.submit(process_partition, p) for p in range(8)]
    done, not_done = wait(futures, return_when=FIRST_EXCEPTION)   # fail fast
    cancelled = sum(future.cancel() for future in not_done)      # only not-yet-started tasks can be cancelled
    stop_requested.set()                                          # ask running tasks to stop
errors = [str(f.exception()) for f in done if f.exception()]
print(errors, "cancelled some pending tasks:", cancelled > 0)
```

**Output:**

```text
['partition 3 has corrupt data'] cancelled some pending tasks: True
```

`pool.shutdown(cancel_futures=True)` (3.9+) cancels everything still queued in one call. Threads cannot be killed from outside; they must cooperate by checking a flag such as `stop_requested`.

---

### Chapter 13 Review

**Key takeaways**
- The GIL allows one thread to run Python bytecode at a time; it is released during I/O.
- Threads or asyncio for I/O-bound work; processes for CPU-bound work; vectorise or push down where possible.
- The GIL does not make your code thread-safe; protect shared state or avoid sharing it.
- Prevent deadlocks with consistent lock ordering and timeouts.
- `concurrent.futures` propagates exceptions through `Future.result()`.
- Guard multiprocessing code with `if __name__ == "__main__":`; pass small, picklable arguments.
- Plan for failure: timeouts, cancellation, SIGTERM handling, non-zero exit codes.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Thread vs process? | Shared memory with one GIL vs separate memory with a GIL each. |
| Concurrency vs parallelism? | Interleaving tasks vs executing simultaneously on several cores. |
| Why doesn't threading speed up CPU work? | The GIL serialises bytecode execution. |
| `map` vs `as_completed`? | Input order vs completion order. |
| What happens to an exception in a worker? | It is stored in the Future and re-raised by `result()`. |
| asyncio vs threads? | Cooperative single-threaded switching at `await` vs OS-scheduled threads. |
| What is a race condition? | A result that depends on thread timing when shared state is accessed without synchronisation. |

**Common traps:** blocking calls inside `async def`; forgetting `future.result()`; no `__main__` guard; pickling lambdas; too many workers overwhelming a database; daemon threads for important work.

**Practice exercise:** You must download 2,000 S3 objects (I/O) and then parse each (CPU, about 2 s each in pure Python). Design a two-stage solution using a `ThreadPoolExecutor` for downloads and a `ProcessPoolExecutor` for parsing. Write down the worker counts, how failures are recorded, and how a re-run skips completed files.

---

## 14. Database Programming

### 14.1 Connecting Python to Relational Databases

| Database | Common driver (DB-API compliant) | Placeholder style |
|---|---|---|
| SQLite | `sqlite3` (standard library) | `?` or `:name` |
| PostgreSQL | `psycopg` (v3) / `psycopg2` | `%s` or `%(name)s` |
| MySQL / MariaDB | `mysql-connector-python`, `PyMySQL` | `%s` or `%(name)s` |
| Snowflake | `snowflake-connector-python` | `%s` / `%(name)s` (default) or `?` / `:1` (qmark/numeric) |
| SQL Server | `pyodbc` | `?` |
| Oracle | `oracledb` | `:name` / `:1` |

**SQLAlchemy** sits on top of these drivers and adds connection pooling, a portable SQL expression language and an ORM. pandas' `read_sql` and `to_sql` accept a SQLAlchemy engine.

All runnable examples in this chapter use the built-in `sqlite3`, so they work anywhere. The same DB-API patterns apply to the other drivers.

---

### 14.2 DB-API 2.0 Concepts

**Definition:** PEP 249 (DB-API 2.0) is the standard interface that Python database drivers implement, so the core code looks the same for every database.

| Object / method | Purpose |
|---|---|
| `connect(...)` | open a **connection** (network session, transaction scope) |
| `connection.cursor()` | create a **cursor** to execute statements and fetch results |
| `cursor.execute(sql, params)` | run one statement with **bound parameters** |
| `cursor.executemany(sql, seq_of_params)` | run one statement for many parameter sets |
| `cursor.fetchone()` / `fetchmany(n)` / `fetchall()` | retrieve rows (tuples by default) |
| `cursor.description` | column metadata (names, types) of the last query |
| `cursor.rowcount` | rows affected by the last DML (driver-dependent for SELECT) |
| `connection.commit()` / `rollback()` | end the current transaction |
| `connection.close()` | release the connection |
| `module.paramstyle` | the driver's placeholder style (`qmark`, `format`, `pyformat`, `named`, `numeric`) |

```python
import sqlite3

connection = sqlite3.connect(":memory:")
try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, country TEXT)")
    cursor.execute("INSERT INTO customers (name, country) VALUES (?, ?)", ("Asha", "IN"))
    connection.commit()
    cursor.execute("SELECT id, name, country FROM customers")
    print([column[0] for column in cursor.description], cursor.fetchall(), sqlite3.paramstyle)
finally:
    connection.close()
```

**Output:**

```text
['id', 'name', 'country'] [(1, 'Asha', 'IN')] qmark
```

---

### 14.3 Executing Parameterized SQL

**Definition:** **parameterised (prepared) queries** send the SQL text and the values **separately**. The driver or database binds values as data. They are never interpreted as SQL.

**Why it matters for a Data Engineer:** parameters prevent SQL injection, handle quoting and escaping correctly (`O'Brien`), convert types (dates, decimals, `None` → `NULL`), and let the database reuse query plans.

```python
import sqlite3
from contextlib import closing
from datetime import date

with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE orders (id INTEGER, customer TEXT, order_date TEXT, discount REAL)")
    conn.execute(
        "INSERT INTO orders VALUES (:id, :customer, :order_date, :discount)",      # named style
        {"id": 1, "customer": "O'Brien", "order_date": date(2026, 10, 29).isoformat(), "discount": None},
    )
    rows = conn.execute(
        "SELECT id, customer, discount FROM orders WHERE customer = ? AND order_date >= ?",  # qmark style
        ("O'Brien", "2026-10-01"),
    ).fetchall()
    print(rows)
```

**Output:**

```text
[(1, "O'Brien", None)]
```

**Common mistakes:**
- Building SQL with f-strings or `%` formatting: `f"... WHERE name = '{name}'"` is an injection risk and breaks on quotes.
- Quoting placeholders yourself: write `WHERE name = %s`, **not** `'%s'`.
- A single parameter must still be a sequence: `(value,)` with a trailing comma, not `(value)`.
- Placeholders work for **values only**, not for table or column names (see 14.4).

---

### 14.4 SQL Injection Prevention

**Definition:** SQL injection happens when untrusted input changes the **structure** of a SQL statement.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE users (name TEXT, is_admin INTEGER)")
    conn.executemany("INSERT INTO users VALUES (?, ?)", [("ana", 1), ("bob", 0)])
    malicious = "nobody' OR '1'='1"

    unsafe_sql = f"SELECT name FROM users WHERE name = '{malicious}'"      # NEVER do this
    print("unsafe:", conn.execute(unsafe_sql).fetchall())
    print("safe:  ", conn.execute("SELECT name FROM users WHERE name = ?", (malicious,)).fetchall())
```

**Output:**

```text
unsafe: [('ana',), ('bob',)]
safe:   []
```

**Dynamic identifiers (table or column names) cannot be bound as parameters.** Validate them against an **allowlist**, or use the driver's identifier-quoting helper:

```python
import re

ALLOWED_TABLES = {"orders", "customers", "order_items"}
IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]{0,62}$")


def safe_table_name(name: str) -> str:
    if name not in ALLOWED_TABLES or not IDENTIFIER.fullmatch(name):
        raise ValueError(f"table not allowed: {name!r}")
    return name


print(f"SELECT COUNT(*) FROM {safe_table_name('orders')}")
try:
    safe_table_name("orders; DROP TABLE customers")
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
SELECT COUNT(*) FROM orders
ValueError: table not allowed: 'orders; DROP TABLE customers'
```

With PostgreSQL, `psycopg.sql.SQL("SELECT * FROM {}").format(sql.Identifier(table))` quotes identifiers safely.

**Defence in depth:** give pipeline database users **least privilege** (no `DROP` rights for a reader), and keep credentials out of code ([15.23](#1523-secrets-management-principles)).

---

### 14.5 Transactions, Commits and Rollbacks

**Definition:** a **transaction** groups statements into one **atomic** unit. `COMMIT` makes all the changes permanent; `ROLLBACK` discards all of them. The ACID properties are Atomicity, Consistency, Isolation and Durability.

**DB-API behaviour:** drivers start a transaction implicitly. **Nothing is saved until you `commit()`.** Closing a connection without committing usually rolls back. Some drivers and settings use **autocommit**, where every statement commits immediately. Know which mode you are in.

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE balances (account TEXT PRIMARY KEY, amount INTEGER CHECK (amount >= 0))")
    conn.executemany("INSERT INTO balances VALUES (?, ?)", [("a", 100), ("b", 0)])
    conn.commit()


    def transfer(amount: int) -> str:
        try:
            with conn:                                   # BEGIN ... COMMIT, or ROLLBACK on error
                conn.execute("UPDATE balances SET amount = amount + ? WHERE account = 'b'", (amount,))
                conn.execute("UPDATE balances SET amount = amount - ? WHERE account = 'a'", (amount,))
            return "committed"
        except sqlite3.IntegrityError as error:
            return f"rolled back ({error})"


    print(transfer(30), conn.execute("SELECT * FROM balances ORDER BY account").fetchall())
    print(transfer(500), conn.execute("SELECT * FROM balances ORDER BY account").fetchall())
```

**Output:**

```text
committed [('a', 70), ('b', 30)]
rolled back (CHECK constraint failed: amount >= 0) [('a', 70), ('b', 30)]
```

The second transfer had already credited `b` before the debit failed, and the rollback undid that credit too. That is atomicity.

**Data Engineering patterns:**
- Load a batch (or a whole partition) **in one transaction**, so a failure leaves no partial data.
- For very large loads, commit **per batch** *and* track progress (a checkpoint), so a restart continues instead of starting over.
- Combine "delete partition + insert partition" or a `MERGE` in one transaction for idempotent reloads.

---

### 14.6 Connection Pooling

**Definition:** a **pool** keeps a set of open connections and lends them out, instead of opening a new connection (TCP + TLS + authentication, often 10–100+ ms) for every operation.

**Why it matters for a Data Engineer:** API services and multi-threaded loaders that open a connection per request can exhaust the database's connection limit and waste time. Batch jobs that run one long session need a pool less, but still need correct cleanup.

```python
# Requires: pip install "psycopg[binary,pool]"
import os

from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo=os.environ["WAREHOUSE_DSN"],   # from the environment / secrets manager, never hardcoded
    min_size=1,
    max_size=10,                            # stay below the server's max_connections budget
    timeout=30,                             # seconds to wait for a free connection
    kwargs={"options": "-c statement_timeout=60000"},   # 60 s server-side statement timeout
)

with pool.connection() as conn:             # borrowed, then returned (commit/rollback handled)
    with conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM orders WHERE order_date = %s", ("2026-10-29",))
        print(cur.fetchone())
pool.close()
```

**SQLAlchemy equivalent:** `create_engine(url, pool_size=5, max_overflow=5, pool_pre_ping=True, pool_recycle=1800)`. `pool_pre_ping` detects stale connections that were dropped by firewalls or idle timeouts.

**Rules:** size pools against the **database's** limit (workers × pool size ≤ the budget). Always return connections (use `with`). Never share one connection between threads unless the driver documents it as thread-safe.

---

### 14.7 Batch Inserts and executemany()

**Definition:** sending rows in **batches** instead of one statement (and one network round trip) per row.

| Method | Relative speed | Notes |
|---|---|---|
| `execute` per row in a loop | slowest | one round trip per row |
| `executemany(sql, rows)` | faster | driver-dependent; psycopg3 pipelines it efficiently |
| Multi-row `VALUES (...), (...)` | fast | e.g. `psycopg2.extras.execute_values` |
| Bulk load (`COPY`, `LOAD DATA`, Snowflake `PUT` + `COPY INTO`) | **fastest** | for large volumes, stage a file and bulk-load it |

```python
import sqlite3
import time
from contextlib import closing
from itertools import islice

rows = [(order_id, order_id * 1.5) for order_id in range(1, 50_001)]


def batches(items, size):
    iterator = iter(items)
    while batch := list(islice(iterator, size)):
        yield batch


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amount REAL)")
    started = time.perf_counter()
    for batch in batches(rows, 10_000):
        with conn:                                          # one transaction per batch
            conn.executemany("INSERT INTO orders (id, amount) VALUES (?, ?)", batch)
    elapsed = time.perf_counter() - started
    print(conn.execute("SELECT COUNT(*), SUM(amount) FROM orders").fetchone(), elapsed < 5)
```

**Output:**

```text
(50000, 1875037500.0) True
```

**Choosing a batch size:** typically 1,000–10,000 rows per batch. Too small means many round trips; too large means huge transactions, lock contention and memory spikes. Make it configurable and measure.

---

### 14.8 Fetching Results Efficiently

| Method | Memory | Use |
|---|---|---|
| `fetchall()` | entire result in memory | small results only |
| `fetchone()` | one row | single-row lookups |
| `fetchmany(n)` | n rows at a time | **large results** (batch processing) |
| `for row in cursor` | driver-buffered rows | convenient streaming (drivers differ in buffering) |

**Important:** many drivers (psycopg2's default client-side cursors, MySQL's default cursors) **download the entire result set into memory on `execute()`**, even if you then call `fetchmany`. For truly large results, use a **server-side cursor**:
- psycopg2: `conn.cursor(name="extract_cursor")` with `itersize`; psycopg3: `conn.cursor(name=...)`;
- MySQL: `SSCursor` / unbuffered cursors;
- Snowflake: `fetch_pandas_batches()` or `get_result_batches()`.

---

### 14.9 Processing Large Result Sets in Batches

**Production-style:**

```python
import sqlite3
from contextlib import closing
from typing import Iterator, Sequence


def stream_query(conn: sqlite3.Connection, sql: str, params: Sequence = (), batch_size: int = 1000) -> Iterator[list[dict]]:
    """Yield lists of row dicts; memory is bounded by batch_size (with a streaming cursor)."""
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        columns = [column[0] for column in cursor.description]
        while rows := cursor.fetchmany(batch_size):
            yield [dict(zip(columns, row)) for row in rows]
    finally:
        cursor.close()


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE events (id INTEGER PRIMARY KEY, kind TEXT)")
    with conn:
        conn.executemany("INSERT INTO events (kind) VALUES (?)", [("click" if n % 3 else "view",) for n in range(2_500)])
    batch_sizes, views = [], 0
    for batch in stream_query(conn, "SELECT id, kind FROM events WHERE id > ? ORDER BY id", (0,), batch_size=1_000):
        batch_sizes.append(len(batch))
        views += sum(1 for row in batch if row["kind"] == "view")
    print(batch_sizes, views)
```

**Output:**

```text
[1000, 1000, 500] 834
```

**Keyset pagination** – an alternative that also lets you **resume**: instead of `OFFSET` (which gets slower on every page and can skip or duplicate rows when data changes), query `WHERE id > :last_seen_id ORDER BY id LIMIT :batch_size` and remember the last ID of each batch.

---

### 14.10 Context Managers for Database Connections

| Driver | `with connection:` means | `with cursor:` |
|---|---|---|
| `sqlite3` | commit or rollback the **transaction**; does **not** close the connection | not supported (use `closing`) |
| `psycopg` (v3) | commit or rollback, **then close** the connection | closes the cursor |
| `psycopg2` | commit or rollback; does **not** close | closes the cursor |
| `snowflake.connector` | closes the connection (commits unless an exception occurred) | closes the cursor |

These differences are a common source of leaked connections. Wrap them in your own helper with explicit, documented semantics (see [11.11](#1111-production-context-managers-database-connections-and-files)).

---

### 14.11 PostgreSQL, MySQL and Snowflake Connector Examples

**PostgreSQL (psycopg 3):**

```python
# Requires: pip install "psycopg[binary]"
import os

import psycopg

with psycopg.connect(os.environ["PG_DSN"], connect_timeout=10) as conn:      # commits/closes on exit
    with conn.cursor() as cur:
        cur.execute("SET statement_timeout = '60s'")
        cur.executemany(
            "INSERT INTO staging.orders (id, amount) VALUES (%s, %s) "
            "ON CONFLICT (id) DO UPDATE SET amount = EXCLUDED.amount",          # idempotent upsert
            [(1, 10.5), (2, 20.0)],
        )
    with conn.cursor(name="big_extract") as server_cursor:                    # server-side cursor
        server_cursor.itersize = 5000
        server_cursor.execute("SELECT id, amount FROM staging.orders WHERE amount > %s", (0,))
        for row in server_cursor:
            pass
```

**MySQL (mysql-connector-python):**

```python
# Requires: pip install mysql-connector-python
import os
from contextlib import closing

import mysql.connector

with closing(mysql.connector.connect(
        host=os.environ["MYSQL_HOST"], user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"], database="sales", connection_timeout=10)) as conn:
    with closing(conn.cursor(dictionary=True)) as cur:
        cur.execute("SELECT id, status FROM orders WHERE updated_at >= %s", ("2026-10-29",))
        for row in cur:
            pass
    conn.commit()
```

**Snowflake (snowflake-connector-python):**

```python
# Requires: pip install snowflake-connector-python
import os

import snowflake.connector

with snowflake.connector.connect(
        account=os.environ["SF_ACCOUNT"], user=os.environ["SF_USER"],
        authenticator="SNOWFLAKE_JWT", private_key_file=os.environ["SF_KEY_PATH"],   # key-pair auth, no password
        warehouse="LOAD_WH", database="RAW", schema="SALES", role="LOADER") as conn:
    with conn.cursor() as cur:
        cur.execute("PUT file:///tmp/orders_2026-10-29.csv.gz @%ORDERS AUTO_COMPRESS=FALSE OVERWRITE=TRUE")
        cur.execute("COPY INTO ORDERS FROM @%ORDERS FILE_FORMAT=(TYPE=CSV SKIP_HEADER=1) ON_ERROR=ABORT_STATEMENT")
        cur.execute("SELECT COUNT(*) FROM ORDERS WHERE LOAD_DATE = %s", ("2026-10-29",))
        print(cur.fetchone())
```

For warehouses, **bulk loading from staged files** (`COPY INTO`) is far faster and cheaper than row-by-row `INSERT`s.

---

### 14.12 Production-Safe Incremental Extraction

**Goal:** extract only rows that changed since the last successful run, using a **watermark** (high-water mark). The run must be **restartable** and **idempotent**.

**Design:**
1. Read the last committed watermark `(updated_at, id)` from a state table.
2. Query `WHERE (updated_at, id) > (watermark)` ordered by `updated_at, id`, in batches. The `id` tie-breaker prevents skipping rows that share a timestamp.
3. **Upsert** each batch into the target (re-running a batch has no side effects).
4. Advance the watermark **only after** the batch is committed. Here target and state are in the same transaction.
5. Optionally re-read a small **lookback window** to catch late-committed rows (upserts make this safe).

```python
import sqlite3
from contextlib import closing

BATCH_SIZE = 2


def setup(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE source_orders (id INTEGER PRIMARY KEY, amount REAL, updated_at TEXT);
        CREATE TABLE target_orders (id INTEGER PRIMARY KEY, amount REAL, updated_at TEXT);
        CREATE TABLE etl_state (pipeline TEXT PRIMARY KEY, wm_updated_at TEXT, wm_id INTEGER);
        INSERT INTO source_orders VALUES
            (1, 10.0, '2026-10-29T10:00:00'), (2, 20.0, '2026-10-29T10:00:00'),
            (3, 30.0, '2026-10-29T11:00:00'), (4, 40.0, '2026-10-29T12:00:00'),
            (5, 50.0, '2026-10-29T12:00:00');
    """)


def get_watermark(conn: sqlite3.Connection, pipeline: str) -> tuple[str, int]:
    row = conn.execute("SELECT wm_updated_at, wm_id FROM etl_state WHERE pipeline = ?", (pipeline,)).fetchone()
    return row if row else ("1970-01-01T00:00:00", 0)


def run_incremental(conn: sqlite3.Connection, pipeline: str = "orders") -> int:
    """Copy changed rows in batches; return the number of rows processed."""
    processed = 0
    while True:
        wm_ts, wm_id = get_watermark(conn, pipeline)
        rows = conn.execute(
            """SELECT id, amount, updated_at FROM source_orders
               WHERE updated_at > ? OR (updated_at = ? AND id > ?)
               ORDER BY updated_at, id LIMIT ?""",
            (wm_ts, wm_ts, wm_id, BATCH_SIZE),
        ).fetchall()
        if not rows:
            return processed
        last_id, _, last_ts = rows[-1]
        with conn:                                    # target upsert + watermark: one atomic commit
            conn.executemany(
                """INSERT INTO target_orders (id, amount, updated_at) VALUES (?, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET amount = excluded.amount, updated_at = excluded.updated_at""",
                rows,
            )
            conn.execute(
                """INSERT INTO etl_state (pipeline, wm_updated_at, wm_id) VALUES (?, ?, ?)
                   ON CONFLICT(pipeline) DO UPDATE SET wm_updated_at = excluded.wm_updated_at, wm_id = excluded.wm_id""",
                (pipeline, last_ts, last_id),
            )
        processed += len(rows)


with closing(sqlite3.connect(":memory:")) as conn:
    setup(conn)
    print("first run:", run_incremental(conn))
    print("second run (nothing new):", run_incremental(conn))
    with conn:
        conn.execute("UPDATE source_orders SET amount = 99.0, updated_at = '2026-10-29T13:00:00' WHERE id = 2")
    print("third run (one change):", run_incremental(conn))
    print(conn.execute("SELECT id, amount FROM target_orders ORDER BY id").fetchall())
    print(get_watermark(conn, "orders"))
```

**Output:**

```text
first run: 5
second run (nothing new): 0
third run (one change): 1
[(1, 10.0), (2, 99.0), (3, 30.0), (4, 40.0), (5, 50.0)]
('2026-10-29T13:00:00', 2)
```

**Production considerations:**
- When the source and target are **different systems**, you cannot commit both atomically. Load first, then save the watermark. A crash between the two causes a **re-read** of the last batch, and the **upsert** makes that harmless ("at-least-once delivery + idempotent writes = effectively exactly-once").
- The watermark column must be **reliable**: indexed, always updated on change, and in a known timezone (UTC).
- **Deletes** are invisible to `updated_at` extraction. Use soft-delete flags, CDC ([15.5](#155-cdc-fundamentals)) or periodic full reconciliation.
- Long-running source transactions can commit rows with an *older* `updated_at` after you have read past it. A lookback window (e.g. re-read the last 10 minutes) covers this.

---

### 14.13 Retry, Timeout, Logging and Cleanup Practices

| Practice | How |
|---|---|
| **Connect timeout** | `connect_timeout=10` (psycopg), `connection_timeout` (MySQL), `login_timeout` (Snowflake) |
| **Statement timeout** | `SET statement_timeout` (PostgreSQL), `STATEMENT_TIMEOUT_IN_SECONDS` (Snowflake), `MAX_EXECUTION_TIME` (MySQL) |
| **Retry transient errors only** | connection resets, deadlocks (PostgreSQL SQLSTATE `40P01`), serialization failures (`40001`), throttling. **Not** syntax or constraint errors |
| **Retry whole transactions** | after a rollback, replay the entire unit of work, not a single statement |
| **Idempotent writes** | upsert or `MERGE`; delete+insert per partition; unique load IDs |
| **Logging** | log the query **name**, row counts, duration and batch number; never log credentials or full sensitive rows |
| **Cleanup** | context managers for connections and cursors; close pools on shutdown |
| **Observability** | tag sessions (`application_name` in PostgreSQL, `QUERY_TAG` in Snowflake) so DBAs can identify your job |

```python
import logging
import sqlite3
import sys
import time
from contextlib import closing

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("db")
TRANSIENT_MESSAGES = ("database is locked", "deadlock", "connection reset")


def run_transaction_with_retry(conn: sqlite3.Connection, work, attempts: int = 3, base_delay: float = 0.01):
    """Run work(conn) inside a transaction, retrying the WHOLE transaction on transient errors."""
    for attempt in range(1, attempts + 1):
        try:
            with conn:
                return work(conn)
        except sqlite3.OperationalError as error:
            transient = any(message in str(error).lower() for message in TRANSIENT_MESSAGES)
            if not transient or attempt == attempts:
                raise
            logger.warning("transient DB error (attempt %d/%d): %s", attempt, attempts, error)
            time.sleep(base_delay * 2 ** (attempt - 1))


simulated_failures = iter([sqlite3.OperationalError("database is locked")])


def load_batch(conn: sqlite3.Connection) -> int:
    failure = next(simulated_failures, None)
    if failure:
        raise failure
    conn.executemany("INSERT INTO t VALUES (?)", [(1,), (2,)])
    return 2


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE t (id INTEGER)")
    rows = run_transaction_with_retry(conn, load_batch)
    logger.info("loaded rows=%d table=t", rows)
```

**Output:**

```text
WARNING transient DB error (attempt 1/3): database is locked
INFO loaded rows=2 table=t
```

---

### Chapter 14 Review

**Key takeaways**
- DB-API: connect → cursor → execute (with parameters) → fetch → commit/rollback → close.
- **Always** use bound parameters; validate identifiers against an allowlist.
- Nothing is saved until `commit()`; use transactions for atomic batch loads.
- Batch writes (`executemany`, bulk `COPY`) and stream reads (`fetchmany`, server-side cursors).
- Incremental extraction: a compound watermark `(updated_at, id)`, upserts, and advancing the watermark after a successful load.
- Timeouts everywhere; retry only transient errors, and retry the whole transaction.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How do you prevent SQL injection? | Parameterised queries plus allowlisted identifiers plus least privilege. |
| `fetchall` vs `fetchmany`? | All rows in memory vs bounded batches. |
| Why is `OFFSET` pagination bad for big tables? | It gets slower per page and is unstable under concurrent changes; use keyset pagination. |
| What is connection pooling? | Reusing open connections to avoid connection overhead and limits. |
| How do you make a load idempotent? | Upsert/MERGE by key, or delete+insert per partition inside one transaction. |
| Why is `executemany` faster? | Fewer round trips and less statement preparation. |

**Common traps:** forgetting `commit()`; `(value)` instead of `(value,)`; client-side cursors loading everything; assuming `with conn:` closes the connection; an unindexed watermark column; ignoring deletes.

**Practice exercise:** Extend `run_incremental` so it writes an audit row `(run_id, started_at, finished_at, rows_processed, status)` to an `etl_audit` table, with status `failed` and the error message when an exception occurs. The watermark must not advance for a failed batch.

---

## 15. Data Engineering with Python

### 15.1 ETL versus ELT

| | ETL (Extract → Transform → Load) | ELT (Extract → Load → Transform) |
|---|---|---|
| Where transforms run | in a processing engine **before** loading (Python, Spark) | **inside the warehouse** after loading raw data (SQL, dbt) |
| Raw data kept? | often not | yes: a raw/bronze layer can be replayed |
| Strengths | sensitive data can be masked before landing; complex non-SQL logic | scalable warehouse compute; simpler re-processing; analysts can change transforms in SQL |
| Typical stack | Python/Spark jobs writing curated tables | Fivetran/Airbyte/Python loaders + Snowflake/BigQuery + dbt |

**Interview answer:** modern cloud platforms mostly use **ELT** (cheap storage, elastic warehouse compute). Python still does extraction, API ingestion, file handling, complex transformations, ML features and orchestration. Many real pipelines are hybrids: light cleaning in Python, heavy modelling in SQL.

---

### 15.2 The Extract, Transform, Validate and Load Pattern

A robust batch step separates concerns:

```text
extract  ->  validate (schema)  ->  transform  ->  validate (quality)  ->  load  ->  reconcile + audit
   |                |                                    |                  |
 raw copy     reject/quarantine                    fail if threshold   idempotent write
```

```python
from typing import Iterable, Iterator


def extract(lines: Iterable[str]) -> Iterator[dict]:
    header = None
    for line in lines:
        values = line.rstrip("\n").split(",")
        if header is None:
            header = values
            continue
        yield dict(zip(header, values))


def validate(rows: Iterable[dict], rejects: list[dict]) -> Iterator[dict]:
    for row in rows:
        if not row.get("id") or not row.get("amount"):
            rejects.append({**row, "_reason": "missing id or amount"})
            continue
        yield row


def transform(rows: Iterable[dict]) -> Iterator[dict]:
    for row in rows:
        yield {"id": int(row["id"]), "amount_cents": round(float(row["amount"]) * 100)}


def load(rows: Iterable[dict], target: list[dict]) -> int:
    before = len(target)
    target.extend(rows)
    return len(target) - before


source = ["id,amount\n", "1,10.50\n", ",3\n", "3,7\n"]
rejected: list[dict] = []
warehouse: list[dict] = []
loaded = load(transform(validate(extract(source), rejected)), warehouse)
print(warehouse, loaded, rejected)
```

**Output:**

```text
[{'id': 1, 'amount_cents': 1050}, {'id': 3, 'amount_cents': 700}] 2 [{'id': '', 'amount': '3', '_reason': 'missing id or amount'}]
```

(This educational example splits on commas for brevity; real code uses the `csv` module.)

---

### 15.3 Full Load versus Incremental Load

| | Full load | Incremental load |
|---|---|---|
| What | reload the whole dataset each run | load only new or changed data |
| Simplicity | simple, self-healing | needs watermarks, CDC or partitions |
| Cost | grows with total size | grows with change volume |
| Deletes | handled naturally (the snapshot replaces everything) | need special handling (soft deletes, CDC, reconciliation) |
| Good for | small dimension tables, data without reliable change tracking | large fact tables, event streams, APIs with `updated_since` |

**Common hybrid:** daily incremental loads plus a periodic (weekly) full reconciliation or reload to catch drift.

---

### 15.4 Watermarks and Checkpoints

**Definitions:**
- A **watermark** is the "high-water mark" of data already processed: a max timestamp, max ID, log offset or API cursor. The next run starts after it.
- A **checkpoint** is the persisted progress of a run (watermark, list of processed files/partitions), saved so a failed run can **resume**.

**Rules:**
1. Persist the checkpoint **after** the corresponding data is durably written, never before.
2. Write checkpoints **atomically** (see [9.17](#917-safe-and-atomic-file-writing)).
3. Store them durably (a DB table, an S3 object), not on a worker's local disk.
4. Watermarks on timestamps need a tie-breaker (`id`) and possibly a lookback window ([14.12](#1412-production-safe-incremental-extraction)).

```python
import json
import os
import tempfile
from pathlib import Path


class FileCheckpoint:
    """Track processed files and a watermark in a JSON document (atomic saves)."""

    def __init__(self, path: Path) -> None:
        self.path = path
        state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        self.processed: set[str] = set(state.get("processed", []))
        self.watermark: str | None = state.get("watermark")

    def mark_done(self, file_name: str, watermark: str) -> None:
        self.processed.add(file_name)
        self.watermark = max(filter(None, [self.watermark, watermark]))
        self._save()

    def _save(self) -> None:
        payload = json.dumps({"processed": sorted(self.processed), "watermark": self.watermark})
        fd, temp = tempfile.mkstemp(dir=self.path.parent, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
        os.replace(temp, self.path)


checkpoint_path = Path("orders_checkpoint.json")
first_run = FileCheckpoint(checkpoint_path)
for name, max_ts in [("orders_01.csv", "2026-10-29T01:00"), ("orders_02.csv", "2026-10-29T02:00")]:
    if name not in first_run.processed:
        first_run.mark_done(name, max_ts)          # only after the file's data is committed

resumed = FileCheckpoint(checkpoint_path)          # e.g. the next run, or after a crash
todo = [name for name in ["orders_01.csv", "orders_02.csv", "orders_03.csv"] if name not in resumed.processed]
print(todo, resumed.watermark)
```

**Output:**

```text
['orders_03.csv'] 2026-10-29T02:00
```

---

### 15.5 CDC Fundamentals

**Definition:** **Change Data Capture** delivers each insert, update and delete from a source system as an event, so targets can stay in sync without full reloads.

| CDC method | How | Pros / cons |
|---|---|---|
| **Log-based** | read the DB transaction log (PostgreSQL WAL, MySQL binlog) with tools like Debezium or AWS DMS | captures deletes and every change, low source impact; more infrastructure |
| **Trigger-based** | DB triggers write changes to an audit table | simple; adds write overhead to the source |
| **Query-based** | poll `WHERE updated_at > watermark` | easy; misses hard deletes and intermediate changes; needs a reliable column |
| **Snapshot diff** | compare full snapshots | works with any source; expensive for large tables |

**Applying CDC events correctly:**
- Events have an operation (`c`/`u`/`d` or `I`/`U`/`D`), a key, the new row image and an **ordering field** (log sequence number, commit timestamp, offset).
- Apply them **in order per key**. Within a batch, keep only the **latest** event per key.
- Deletes remove the row (or set `is_deleted = true` for a soft delete).
- Events can arrive **more than once** (at-least-once delivery), so applying them must be idempotent: ignore events whose sequence number is ≤ the last applied one for that key.

```python
def apply_cdc(target: dict[int, dict], last_seq: dict[int, int], events: list[dict]) -> dict[int, dict]:
    """Apply CDC events idempotently. target: key -> row; last_seq: key -> last applied sequence."""
    latest: dict[int, dict] = {}
    for event in events:                                   # keep the newest event per key in this batch
        key = event["key"]
        if key not in latest or event["seq"] > latest[key]["seq"]:
            latest[key] = event
    for key, event in latest.items():
        if event["seq"] <= last_seq.get(key, -1):          # duplicate or out-of-date replay: skip
            continue
        if event["op"] == "d":
            target.pop(key, None)
        else:                                              # "c" (create) or "u" (update) = upsert
            target[key] = event["row"]
        last_seq[key] = event["seq"]
    return target


table: dict[int, dict] = {}
sequence_state: dict[int, int] = {}
batch = [
    {"seq": 1, "op": "c", "key": 1, "row": {"id": 1, "status": "new"}},
    {"seq": 2, "op": "c", "key": 2, "row": {"id": 2, "status": "new"}},
    {"seq": 3, "op": "u", "key": 1, "row": {"id": 1, "status": "paid"}},
    {"seq": 4, "op": "d", "key": 2, "row": None},
]
apply_cdc(table, sequence_state, batch)
apply_cdc(table, sequence_state, batch)                    # replaying the same batch changes nothing
print(table, sequence_state)
```

**Output:**

```text
{1: {'id': 1, 'status': 'paid'}} {1: 3, 2: 4}
```

**SCD (Slowly Changing Dimension) types**, a common follow-up: **Type 1** overwrites (no history; what `apply_cdc` does). **Type 2** keeps history rows with `valid_from` / `valid_to` / `is_current`.

---

### 15.6 Idempotency

**Definition:** an operation is **idempotent** if running it once or many times with the same input leaves the system in the **same state**.

**Why it matters for a Data Engineer:** pipelines are retried automatically, backfilled and re-run by hand. A non-idempotent load (plain `INSERT`, appending files) **duplicates data** on every retry, which silently inflates revenue and counts.

**Techniques:**

| Technique | Example |
|---|---|
| Deterministic output location | `s3://lake/sales/dt=2026-10-29/` derived from the **logical run date**, not the current time or a random UUID |
| Overwrite a partition | replace `dt=2026-10-29` entirely; delete+insert in one transaction |
| Upsert / MERGE by business key | `INSERT ... ON CONFLICT DO UPDATE`, `MERGE INTO` |
| Deduplicate on load | unique constraints; keep the latest per key |
| Track processed inputs | a manifest of file checksums or message IDs |
| Idempotency keys for APIs | send a unique request ID so the server ignores duplicates |

```python
import sqlite3
from contextlib import closing
from datetime import date


def load_daily_partition(conn: sqlite3.Connection, run_date: date, rows: list[tuple[int, float]]) -> int:
    """Replace one day's data atomically: safe to run any number of times."""
    day = run_date.isoformat()
    with conn:
        conn.execute("DELETE FROM daily_sales WHERE sale_date = ?", (day,))
        conn.executemany("INSERT INTO daily_sales (sale_date, order_id, amount) VALUES (?, ?, ?)",
                         [(day, order_id, amount) for order_id, amount in rows])
    return conn.execute("SELECT COUNT(*) FROM daily_sales WHERE sale_date = ?", (day,)).fetchone()[0]


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE daily_sales (sale_date TEXT, order_id INTEGER, amount REAL)")
    rows = [(1, 10.0), (2, 25.5)]
    for attempt in range(3):                                        # e.g. retries or manual re-runs
        count = load_daily_partition(conn, date(2026, 10, 29), rows)
    print("rows after 3 runs:", count, "| total rows:", conn.execute("SELECT COUNT(*) FROM daily_sales").fetchone()[0])
```

**Output:**

```text
rows after 3 runs: 2 | total rows: 2
```

**Interview follow-up – "exactly-once":** true exactly-once delivery is hard across systems. The practical approach is **at-least-once processing + idempotent writes**, which gives exactly-once *results*.

---

### 15.7 Deduplication

| Duplicate type | Detection | Resolution |
|---|---|---|
| Exact duplicate rows | hash of all columns | keep one |
| Same business key, different versions | key + ordering column (`updated_at`, sequence) | keep the latest (or the first, if the business rule says so) |
| Duplicates across batches or runs | persistent store of seen keys or hashes; target unique constraint | upsert / skip |
| Fuzzy duplicates ("Jon Smith" vs "John Smith") | normalisation, matching rules | entity resolution (out of scope for most interviews) |

```python
import hashlib
import json


def row_hash(row: dict) -> str:
    """Stable content hash: sorted keys, compact separators, UTF-8."""
    canonical = json.dumps(row, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def drop_exact_duplicates(rows: list[dict]) -> list[dict]:
    seen: set[str] = set()
    unique = []
    for row in rows:
        digest = row_hash(row)
        if digest not in seen:
            seen.add(digest)
            unique.append(row)
    return unique


def latest_per_key(rows: list[dict], key: str, order_by: str) -> list[dict]:
    latest: dict = {}
    for row in rows:
        current = latest.get(row[key])
        if current is None or row[order_by] > current[order_by]:
            latest[row[key]] = row
    return list(latest.values())


events = [
    {"id": 1, "status": "new", "ts": "10:00"},
    {"status": "new", "id": 1, "ts": "10:00"},          # same content, different key order
    {"id": 1, "status": "paid", "ts": "11:00"},
    {"id": 2, "status": "new", "ts": "09:00"},
]
print(len(drop_exact_duplicates(events)))
print(latest_per_key(events, key="id", order_by="ts"))
```

**Output:**

```text
3
[{'id': 1, 'status': 'paid', 'ts': '11:00'}, {'id': 2, 'status': 'new', 'ts': '09:00'}]
```

**Memory note:** a `seen` set grows with the number of unique keys. For huge streams, deduplicate per partition, use the database (unique constraints, `ROW_NUMBER()`), or use probabilistic structures (Bloom filters), which accept a small false-positive rate.

---

### 15.8 Schema Validation

**Definition:** checking that incoming data has the **expected columns, types and nullability** before it is processed. **Schema drift** means the source added, removed, renamed or retyped columns.

```python
from dataclasses import dataclass
from datetime import date
from typing import Any, Callable


@dataclass(frozen=True)
class Column:
    name: str
    parse: Callable[[str], Any]
    nullable: bool = False


ORDER_SCHEMA = [
    Column("order_id", int),
    Column("amount", float),
    Column("order_date", date.fromisoformat),
    Column("coupon", str, nullable=True),
]


def check_header(header: list[str], schema: list[Column]) -> dict[str, list[str]]:
    expected = [column.name for column in schema]
    return {"missing": [c for c in expected if c not in header], "unexpected": [c for c in header if c not in expected]}


def parse_row(raw: dict[str, str], schema: list[Column]) -> tuple[dict | None, list[str]]:
    """Return (typed_row, errors). typed_row is None if any error occurred."""
    typed, errors = {}, []
    for column in schema:
        value = (raw.get(column.name) or "").strip()
        if value == "":
            if column.nullable:
                typed[column.name] = None
            else:
                errors.append(f"{column.name}: required")
            continue
        try:
            typed[column.name] = column.parse(value)
        except ValueError as error:
            errors.append(f"{column.name}: {error}")
    return (None if errors else typed), errors


print(check_header(["order_id", "amount", "order_date", "channel"], ORDER_SCHEMA))
print(parse_row({"order_id": "7", "amount": "9.5", "order_date": "2026-10-29", "coupon": ""}, ORDER_SCHEMA))
print(parse_row({"order_id": "x", "amount": "", "order_date": "2026-13-01"}, ORDER_SCHEMA))
```

**Output:**

```text
{'missing': ['coupon'], 'unexpected': ['channel']}
({'order_id': 7, 'amount': 9.5, 'order_date': datetime.date(2026, 10, 29), 'coupon': None}, [])
(None, ["order_id: invalid literal for int() with base 10: 'x'", 'amount: required', 'order_date: month must be in 1..12'])
```

**Schema drift policy (decide it explicitly):**
- **New optional column:** allow it and log a warning (or add it to the target automatically, if that's the agreed policy).
- **Missing required column, or a type change:** fail fast, before loading anything.
- Version schemas, and use contracts (pydantic models, JSON Schema, Avro schema registry) for shared interfaces.

---

### 15.9 Data-Quality Checks

| Check | Example rule |
|---|---|
| Completeness | `customer_id` not null in 100% of rows |
| Uniqueness | `order_id` unique |
| Validity | `amount >= 0`; `status in {"new", "paid", "shipped"}`; email matches a pattern |
| Consistency | `ship_date >= order_date` |
| Referential integrity | every `orders.customer_id` exists in `customers` |
| Freshness | the latest `event_time` is less than 2 hours old |
| Volume | today's row count is within ±50% of the 7-day average |

```python
from collections import Counter
from dataclasses import dataclass


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str


def check_not_null(rows: list[dict], column: str) -> CheckResult:
    nulls = sum(1 for row in rows if row.get(column) in (None, ""))
    return CheckResult(f"not_null({column})", nulls == 0, f"{nulls} null(s)")


def check_unique(rows: list[dict], column: str) -> CheckResult:
    duplicates = [value for value, count in Counter(row[column] for row in rows).items() if count > 1]
    return CheckResult(f"unique({column})", not duplicates, f"duplicates={duplicates}")


def check_allowed(rows: list[dict], column: str, allowed: set) -> CheckResult:
    bad = sorted({row[column] for row in rows if row[column] not in allowed})
    return CheckResult(f"allowed({column})", not bad, f"invalid={bad}")


def check_volume(row_count: int, history: list[int], tolerance: float = 0.5) -> CheckResult:
    baseline = sum(history) / len(history)
    within = abs(row_count - baseline) <= tolerance * baseline
    return CheckResult("volume", within, f"count={row_count} baseline={baseline:.0f}")


orders = [
    {"order_id": 1, "customer_id": 10, "status": "paid"},
    {"order_id": 2, "customer_id": None, "status": "paid"},
    {"order_id": 2, "customer_id": 11, "status": "lost"},
]
results = [
    check_not_null(orders, "customer_id"),
    check_unique(orders, "order_id"),
    check_allowed(orders, "status", {"new", "paid", "shipped"}),
    check_volume(len(orders), history=[100, 120, 110]),
]
for result in results:
    print(f"{'PASS' if result.passed else 'FAIL'} {result.name}: {result.detail}")
```

**Output:**

```text
FAIL not_null(customer_id): 1 null(s)
FAIL unique(order_id): duplicates=[2]
FAIL allowed(status): invalid=['lost']
FAIL volume: count=3 baseline=110
```

**Severity levels:** **blocking** checks stop the load (duplicate primary keys, a missing required column); **warning** checks alert but continue (volume anomalies). Frameworks such as Great Expectations, Soda and dbt tests provide these checks declaratively.

---

### 15.10 NULL and Empty-String Handling

**Definitions:** `NULL` / `None` means "unknown or missing". `""` means "known to be empty". They are **different**, and conflating them corrupts data.

| Where | NULL | Empty string |
|---|---|---|
| Python | `None` | `""` |
| SQL | `NULL` (`col IS NULL`; `NULL = NULL` is not true) | `''` (Oracle treats `''` as NULL!) |
| CSV | no native representation (convention: empty, `\N`, `NULL`) | `""` or an empty field |
| JSON | `null` or a missing key | `""` |
| pandas | `None` / `NaN` / `pd.NA` / `NaT` | `""` |

```python
NULL_TOKENS = {"", "null", "none", "n/a", "na", "\\n", "nil"}


def normalize_value(raw: object, *, empty_is_null: bool = True) -> object:
    """Trim strings; map agreed NULL tokens to None. Keep 0 / False as real values."""
    if raw is None:
        return None
    if isinstance(raw, str):
        stripped = raw.strip()
        if stripped.lower() in NULL_TOKENS and (stripped or empty_is_null):
            return None
        return stripped
    return raw


values = [None, "", "  ", "NULL", "N/A", " Asha ", 0, False, "0"]
print([normalize_value(value) for value in values])
print([normalize_value(value, empty_is_null=False) for value in ["", "NULL"]])
print(str(None), f"{None}")          # the classic bug: None becoming the text "None"
```

**Output:**

```text
[None, None, None, None, None, 'Asha', 0, False, '0']
['', None]
None None
```

**Best practices:**
- Define the NULL tokens per source **in configuration**, and document them.
- Never write `str(value)` blindly: `None` becomes the literal string `"None"` in your warehouse.
- Use `is None`, not truthiness, when checking values ([1.10](#110-truthy-and-falsy-values)).
- In SQL use `IS NULL`, `COALESCE` and `NULLIF(col, '')`. Remember that `NOT IN (subquery)` returns no rows if the subquery contains a NULL.
- Count NULLs per column in data-quality metrics. A sudden jump signals an upstream change.

---

### 15.11 Audit Logging

**Definition:** a durable record of **every pipeline run**: what ran, on what input, how many records were read, written and rejected, how long it took, and whether it succeeded. It is used for reconciliation, debugging, SLAs and compliance.

```python
import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone


@dataclass
class AuditRecord:
    pipeline: str
    run_date: str
    run_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat(timespec="seconds"))
    finished_at: str | None = None
    status: str = "running"
    rows_read: int = 0
    rows_written: int = 0
    rows_rejected: int = 0
    error: str | None = None

    def finish(self, status: str, error: str | None = None) -> None:
        self.status, self.error = status, error
        self.finished_at = datetime.now(timezone.utc).isoformat(timespec="seconds")


audit = AuditRecord(pipeline="orders_daily", run_date="2026-10-29")
audit.rows_read, audit.rows_written, audit.rows_rejected = 1000, 990, 10
audit.finish("success")
record = asdict(audit)
print(sorted(record), record["status"], record["rows_read"] == record["rows_written"] + record["rows_rejected"])
print(json.dumps({k: record[k] for k in ("pipeline", "status", "rows_written")}))
```

**Output:**

```text
['error', 'finished_at', 'pipeline', 'rows_read', 'rows_rejected', 'rows_written', 'run_date', 'run_id', 'started_at', 'status'] success True
{"pipeline": "orders_daily", "status": "success", "rows_written": 990}
```

Write the audit row at **start** (status `running`) and **update** it at the end. A row stuck in `running` then reveals a crashed job.

---

### 15.12 Batch and Chunk Processing

| Mode | Latency | Typical tools |
|---|---|---|
| Batch (hourly / daily) | minutes to hours | Airflow + Python/Spark/SQL |
| Micro-batch | seconds to minutes | Spark Structured Streaming, scheduled small batches |
| Streaming | milliseconds to seconds | Kafka consumers, Flink, Kinesis |

**Chunking inside a batch** bounds memory and makes progress restartable: read *N* rows → process → write → checkpoint. The `chunked` helper from [6.10](#610-generator-based-data-pipelines), `fetchmany` ([14.9](#149-processing-large-result-sets-in-batches)) and `pandas.read_csv(chunksize=...)` ([17.14](#1714-chunk-based-file-reading)) all implement this idea.

**Choosing a chunk size:** large enough to amortise per-call overhead, small enough to fit in memory with headroom and keep retries cheap. Make it configurable.

---

### 15.13 Source-to-Target Reconciliation

**Definition:** proving that the target matches the source after a load. Common levels, from cheapest to most thorough:

| Level | Check |
|---|---|
| Count | `source_rows == target_rows + rejected_rows` |
| Control totals | `SUM(amount)`, `MIN/MAX(date)` match per partition |
| Key sets | the same set of primary keys (find missing and extra keys) |
| Row hashes | a per-row hash of the business columns matches (finds changed values) |

```python
import hashlib


def row_fingerprint(row: dict, columns: list[str]) -> str:
    joined = "\x1f".join("" if row.get(column) is None else str(row[column]) for column in columns)
    return hashlib.md5(joined.encode("utf-8")).hexdigest()   # md5 is fine for comparison, not for security


def reconcile(source: list[dict], target: list[dict], key: str, columns: list[str]) -> dict:
    source_by_key = {row[key]: row for row in source}
    target_by_key = {row[key]: row for row in target}
    common = source_by_key.keys() & target_by_key.keys()
    return {
        "source_count": len(source),
        "target_count": len(target),
        "missing_in_target": sorted(source_by_key.keys() - target_by_key.keys()),
        "unexpected_in_target": sorted(target_by_key.keys() - source_by_key.keys()),
        "mismatched": sorted(k for k in common
                             if row_fingerprint(source_by_key[k], columns) != row_fingerprint(target_by_key[k], columns)),
        "amount_diff": round(sum(r["amount"] for r in source) - sum(r["amount"] for r in target), 2),
    }


source_rows = [{"id": 1, "amount": 10.0}, {"id": 2, "amount": 20.0}, {"id": 3, "amount": 30.0}]
target_rows = [{"id": 1, "amount": 10.0}, {"id": 2, "amount": 25.0}, {"id": 4, "amount": 5.0}]
print(reconcile(source_rows, target_rows, key="id", columns=["amount"]))
```

**Output:**

```text
{'source_count': 3, 'target_count': 3, 'missing_in_target': [3], 'unexpected_in_target': [4], 'mismatched': [2], 'amount_diff': 20.0}
```

Note that the counts match (3 = 3) even though the data is wrong. **Counts alone are not enough.** For large tables, compute counts, sums and hashes **inside each database** with SQL (grouped by partition) and compare only the aggregates.

---

### 15.14 API Pagination

| Style | Request | Stop condition | Pitfalls |
|---|---|---|---|
| Page number | `?page=3&per_page=100` | empty page, or `page > total_pages` | rows shift if data changes during paging |
| Offset / limit | `?offset=200&limit=100` | fewer than `limit` rows | same as above; slow for deep offsets |
| **Cursor / token** | `?cursor=eyJpZCI6MTAwfQ` | no `next_cursor` | the most robust; cursors may expire |
| Link header | `Link: <...page=4>; rel="next"` | no `next` link | `requests` parses it into `response.links` |
| Time window | `?updated_since=...&until=...` | window end reached | combine with a watermark |

```python
from typing import Callable, Iterator

DATASET = [{"id": number} for number in range(1, 8)]


def fake_api(cursor: str | None, limit: int = 3) -> dict:
    """Stands in for GET /orders?cursor=...: returns a page plus the next cursor."""
    start = int(cursor or 0)
    end = start + limit
    return {"data": DATASET[start:end], "next_cursor": str(end) if end < len(DATASET) else None}


def paginate(fetch_page: Callable[[str | None], dict], max_pages: int = 10_000) -> Iterator[dict]:
    """Yield records from every page; guard against infinite loops."""
    cursor, seen_cursors = None, set()
    for _ in range(max_pages):
        response = fetch_page(cursor)
        yield from response["data"]
        cursor = response.get("next_cursor")
        if not cursor:
            return
        if cursor in seen_cursors:
            raise RuntimeError(f"API returned a repeated cursor {cursor!r}")
        seen_cursors.add(cursor)
    raise RuntimeError(f"stopped after {max_pages} pages: possible pagination bug")


pages_called: list[str | None] = []


def counting_fetch(cursor: str | None) -> dict:
    pages_called.append(cursor)
    return fake_api(cursor)


records = list(paginate(counting_fetch))
print([record["id"] for record in records], "pages:", len(pages_called))
```

**Output:**

```text
[1, 2, 3, 4, 5, 6, 7] pages: 3
```

**Production-style with `requests`** – pagination, timeouts, retries on 429/5xx with `Retry-After`, and streaming output:

```python
# Requires: pip install requests
import logging
import os
import time
from typing import Iterator

import requests

logger = logging.getLogger("api_ingest")
RETRYABLE = {429, 500, 502, 503, 504}


def get_with_retry(session: requests.Session, url: str, params: dict, attempts: int = 5) -> dict:
    for attempt in range(1, attempts + 1):
        try:
            response = session.get(url, params=params, timeout=(5, 60))
        except (requests.ConnectionError, requests.Timeout) as error:
            if attempt == attempts:
                raise
            wait_seconds = 2 ** attempt
            logger.warning("network error %s; retry in %ss", error, wait_seconds)
        else:
            if response.status_code not in RETRYABLE:
                response.raise_for_status()                      # 4xx other than 429: do not retry
                return response.json()
            if attempt == attempts:
                response.raise_for_status()
            wait_seconds = int(response.headers.get("Retry-After", 2 ** attempt))
            logger.warning("HTTP %s; retry in %ss", response.status_code, wait_seconds)
        time.sleep(wait_seconds)
    raise RuntimeError("unreachable")


def fetch_orders(updated_since: str) -> Iterator[dict]:
    with requests.Session() as session:
        session.headers["Authorization"] = f"Bearer {os.environ['ORDERS_API_TOKEN']}"   # from a secret store
        params = {"updated_since": updated_since, "limit": 500}
        while True:
            payload = get_with_retry(session, "https://api.example.com/v1/orders", params)
            yield from payload["data"]
            if not payload.get("next_cursor"):
                break
            params = {**params, "cursor": payload["next_cursor"]}
```

---

### 15.15 File Ingestion Pipelines

**Typical flow:** `landing/` → validate → load → move to `archive/` (success) or `quarantine/` (failure), with a **manifest** of checksums so re-delivered files are skipped.

**Production-style (runnable, using local folders and SQLite):**

```python
import csv
import hashlib
import json
import shutil
import sqlite3
from contextlib import closing
from pathlib import Path

ROOT = Path("ingest_demo")
LANDING, ARCHIVE, QUARANTINE = ROOT / "landing", ROOT / "archive", ROOT / "quarantine"
MANIFEST = ROOT / "manifest.json"
EXPECTED_HEADER = ["order_id", "amount"]


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_file(conn: sqlite3.Connection, path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        if next(reader, None) != EXPECTED_HEADER:
            raise ValueError("unexpected header")
        rows = [(int(order_id), float(amount)) for order_id, amount in reader]
    with conn:                                               # all rows of a file, or none
        conn.executemany("INSERT INTO orders VALUES (?, ?) ON CONFLICT(order_id) DO UPDATE SET amount = excluded.amount", rows)
    return len(rows)


def ingest(conn: sqlite3.Connection) -> dict[str, str]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    outcome = {}
    for path in sorted(LANDING.glob("*.csv")):
        checksum = sha256_of(path)
        if checksum in manifest.values():
            outcome[path.name] = "skipped duplicate"
            shutil.move(str(path), ARCHIVE / path.name)
            continue
        try:
            rows = load_file(conn, path)
        except (ValueError, csv.Error) as error:
            outcome[path.name] = f"quarantined: {error}"
            shutil.move(str(path), QUARANTINE / path.name)
            continue
        manifest[path.name] = checksum
        MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        shutil.move(str(path), ARCHIVE / path.name)
        outcome[path.name] = f"loaded {rows} rows"
    return outcome


for folder in (LANDING, ARCHIVE, QUARANTINE):
    folder.mkdir(parents=True, exist_ok=True)
(LANDING / "orders_01.csv").write_text("order_id,amount\n1,10\n2,20\n", encoding="utf-8")
(LANDING / "orders_02.csv").write_text("order_id,amount\n1,10\n2,20\n", encoding="utf-8")   # re-delivery
(LANDING / "orders_03.csv").write_text("id,value\n3,30\n", encoding="utf-8")                 # bad header

with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE orders (order_id INTEGER PRIMARY KEY, amount REAL)")
    for name, result in ingest(conn).items():
        print(f"{name}: {result}")
    print("rows in table:", conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
print(sorted(p.name for p in QUARANTINE.iterdir()), len(list(LANDING.iterdir())))
```

**Output:**

```text
orders_01.csv: loaded 2 rows
orders_02.csv: skipped duplicate
orders_03.csv: quarantined: unexpected header
rows in table: 2
['orders_03.csv'] 0
```

**Production notes:** in S3, "moving" means copy + delete (or using prefixes and lifecycle rules). Wait for file-completion signals (a `_SUCCESS` marker, a size that stays stable, or event notifications) before ingesting. Store the manifest in a database table, not a local file, when several workers run.

---

### 15.16 Database-to-File and File-to-Database Pipelines

```python
import csv
import sqlite3
from contextlib import closing
from itertools import islice
from pathlib import Path

EXPORT = Path("orders_export.csv")

with closing(sqlite3.connect(":memory:")) as source, closing(sqlite3.connect(":memory:")) as target:
    source.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT, amount REAL)")
    with source:
        source.executemany("INSERT INTO orders VALUES (?, ?, ?)",
                           [(n, f"cust_{n % 4}", n * 2.5) for n in range(1, 1001)])

    # --- database -> file: stream with fetchmany, never fetchall on big tables
    cursor = source.execute("SELECT id, customer, amount FROM orders ORDER BY id")
    exported = 0
    with EXPORT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([column[0] for column in cursor.description])
        while rows := cursor.fetchmany(250):
            writer.writerows(rows)
            exported += len(rows)

    # --- file -> database: stream the CSV and insert in batches
    target.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT, amount REAL)")
    loaded = 0
    with EXPORT.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        while batch := list(islice(reader, 300)):
            with target:
                target.executemany("INSERT INTO orders VALUES (:id, :customer, :amount)", batch)
            loaded += len(batch)

    source_total = source.execute("SELECT COUNT(*), ROUND(SUM(amount), 2) FROM orders").fetchone()
    target_total = target.execute("SELECT COUNT(*), ROUND(SUM(amount), 2) FROM orders").fetchone()
    print(exported, loaded, source_total, target_total, source_total == target_total)
```

**Output:**

```text
1000 1000 (1000, 1251250.0) (1000, 1251250.0) True
```

(SQLite converts the CSV text values to the declared column types on insert. With stricter databases, convert types in Python before inserting, or use the database's bulk-load command with an explicit file format.)

---

### 15.17 Retry with Exponential Backoff

Covered in depth in [8.8](#88-retry-handling) (function) and [11.5](#115-decorators-with-arguments) (decorator). A production checklist:
- retry only **transient** failures (timeouts, connection resets, HTTP 429/5xx, DB deadlocks);
- **exponential backoff + jitter**, capped delays and capped attempts;
- honour **`Retry-After`**;
- make the retried operation **idempotent** (upserts, idempotency keys, deterministic paths);
- log every retry with its attempt number; alert if retries are frequent;
- set an **overall deadline**, so retries can't exceed the job's SLA.

---

### 15.18 Rate Limiting

**Definition:** limiting how many requests per time unit you send, to respect API quotas and avoid HTTP 429 responses. The **token bucket** algorithm allows short bursts up to `capacity` and then a steady `rate` per second.

```python
import threading
import time


class TokenBucket:
    """Thread-safe token bucket: `rate` tokens per second, bursts up to `capacity`."""

    def __init__(self, rate: float, capacity: int) -> None:
        self.rate, self.capacity = rate, capacity
        self.tokens = float(capacity)
        self.updated = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self) -> None:
        while True:
            with self.lock:
                now = time.monotonic()
                self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
                self.updated = now
                if self.tokens >= 1:
                    self.tokens -= 1
                    return
                wait_seconds = (1 - self.tokens) / self.rate
            time.sleep(wait_seconds)                # sleep outside the lock


bucket = TokenBucket(rate=50, capacity=5)
started = time.perf_counter()
for _ in range(30):                                 # 5 burst + 25 at 50/s ≈ 0.5 s
    bucket.acquire()
elapsed = time.perf_counter() - started
print(0.4 < elapsed < 1.5)
```

**Output:**

```text
True
```

Combine a **concurrency** limit (semaphore, worker count) with a **rate** limit (token bucket). For distributed workers sharing one quota, keep the bucket in a shared store (e.g. Redis) or give each worker a fraction of the quota.

---

### 15.19 Configuration-Driven Pipeline Design

**Definition:** describe *what* to process (sources, targets, keys, transforms, schedules) in **configuration**, and keep one generic, tested engine for *how*. Adding a new feed becomes a config change instead of new code.

```python
from dataclasses import dataclass, field
from typing import Callable

TRANSFORMS: dict[str, Callable[[dict], dict]] = {
    "trim_strings": lambda row: {k: v.strip() if isinstance(v, str) else v for k, v in row.items()},
    "uppercase_country": lambda row: {**row, "country": row["country"].upper()},
}

RAW_CONFIG = {                                   # normally loaded from YAML / JSON
    "pipelines": [
        {"name": "customers", "source": "landing/customers/*.csv", "target": "dim_customer",
         "key": ["customer_id"], "load_mode": "merge", "transforms": ["trim_strings", "uppercase_country"]},
        {"name": "orders", "source": "landing/orders/*.csv", "target": "fct_orders",
         "key": ["order_id"], "load_mode": "partition_overwrite", "transforms": ["trim_strings"]},
    ]
}


@dataclass(frozen=True)
class PipelineConfig:
    name: str
    source: str
    target: str
    key: list[str]
    load_mode: str
    transforms: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.load_mode not in {"merge", "partition_overwrite", "append"}:
            raise ValueError(f"{self.name}: unknown load_mode {self.load_mode!r}")
        unknown = [t for t in self.transforms if t not in TRANSFORMS]
        if unknown:
            raise ValueError(f"{self.name}: unknown transforms {unknown}")
        if not self.key:
            raise ValueError(f"{self.name}: a key is required")


configs = [PipelineConfig(**item) for item in RAW_CONFIG["pipelines"]]   # validate everything up front
for config in configs:
    print(f"{config.name}: {config.source} -> {config.target} [{config.load_mode}] steps={config.transforms}")

row = {"customer_id": 1, "country": " in "}
for step in configs[0].transforms:
    row = TRANSFORMS[step](row)
print(row)
```

**Output:**

```text
customers: landing/customers/*.csv -> dim_customer [merge] steps=['trim_strings', 'uppercase_country']
orders: landing/orders/*.csv -> fct_orders [partition_overwrite] steps=['trim_strings']
{'customer_id': 1, 'country': 'IN'}
```

**Best practices:** validate the whole configuration **at start-up** (fail fast); keep configuration in version control; don't turn config into a programming language (complex logic belongs in tested code); keep secrets **out** of config files.

---

### 15.20 Environment-Based Configuration

**Principle (from the "12-factor app"):** the same code artefact runs in dev, test and prod. Only **configuration** changes, supplied through environment variables or environment-specific files.

```python
import os
from dataclasses import dataclass


class ConfigError(RuntimeError):
    pass


@dataclass(frozen=True)
class Settings:
    env: str
    db_host: str
    batch_size: int
    dry_run: bool

    @classmethod
    def from_env(cls) -> "Settings":
        def required(name: str) -> str:
            value = os.environ.get(name)
            if not value:
                raise ConfigError(f"missing required environment variable {name}")
            return value

        env = os.environ.get("PIPELINE_ENV", "dev")
        if env not in {"dev", "test", "prod"}:
            raise ConfigError(f"invalid PIPELINE_ENV {env!r}")
        return cls(
            env=env,
            db_host=required("DB_HOST"),
            batch_size=int(os.environ.get("BATCH_SIZE", "1000")),
            dry_run=os.environ.get("DRY_RUN", "false").strip().lower() in {"1", "true", "yes"},
        )


os.environ.pop("DB_HOST", None)
try:
    Settings.from_env()
except ConfigError as error:
    print("ConfigError:", error)

os.environ.update({"PIPELINE_ENV": "prod", "DB_HOST": "warehouse.internal", "DRY_RUN": "False"})
print(Settings.from_env())
```

**Output:**

```text
ConfigError: missing required environment variable DB_HOST
Settings(env='prod', db_host='warehouse.internal', batch_size=1000, dry_run=False)
```

Note the explicit boolean parsing: `bool("False")` would be `True`. Libraries like `pydantic-settings` provide typed settings with validation.

---

### 15.21 Structured Logging

**Definition:** logs emitted as **machine-parseable records** (usually JSON), with consistent fields such as `run_id`, `pipeline`, `table`, `batch` and `rows`. Log platforms (CloudWatch, Datadog, ELK, Splunk) can then filter, aggregate and alert on them.

```python
import json
import logging
import sys


class JsonFormatter(logging.Formatter):
    """Render each log record as one JSON line. (Add a timestamp field in production.)"""

    def format(self, record: logging.LogRecord) -> str:
        payload = {"level": record.levelname, "logger": record.name, "message": record.getMessage()}
        payload.update(getattr(record, "context", {}))
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info).splitlines()[-1]
        return json.dumps(payload)


handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
base_logger = logging.getLogger("orders_pipeline")
base_logger.addHandler(handler)
base_logger.setLevel(logging.INFO)
base_logger.propagate = False


class ContextAdapter(logging.LoggerAdapter):
    """Attach run-level context to every message."""

    def process(self, msg, kwargs):
        kwargs["extra"] = {"context": {**self.extra, **kwargs.pop("context", {})}}
        return msg, kwargs


log = ContextAdapter(base_logger, {"run_id": "r-20261029-01", "pipeline": "orders"})
log.info("batch loaded", context={"batch": 3, "rows": 5000})
try:
    1 / 0
except ZeroDivisionError:
    log.exception("aggregation failed", context={"step": "aggregate"})
```

**Output:**

```text
{"level": "INFO", "logger": "orders_pipeline", "message": "batch loaded", "run_id": "r-20261029-01", "pipeline": "orders", "batch": 3, "rows": 5000}
{"level": "ERROR", "logger": "orders_pipeline", "message": "aggregation failed", "run_id": "r-20261029-01", "pipeline": "orders", "step": "aggregate", "exception": "ZeroDivisionError: division by zero"}
```

---

### 15.22 Error Handling and Alerting

**Decide the policy per failure type:**

| Failure | Policy |
|---|---|
| Transient (network, throttling) | retry with backoff |
| Bad records below a threshold | quarantine them, continue, report the count |
| Bad records above the threshold (e.g. > 1%) | **fail the run**: upstream is probably broken |
| Schema break, missing input, bad config | fail fast, before writing anything |
| Data-quality check failure (blocking) | fail and alert; do not publish downstream |

```python
class DataQualityError(RuntimeError):
    pass


def enforce_reject_threshold(total: int, rejected: int, max_ratio: float = 0.01) -> float:
    ratio = rejected / total if total else 0.0
    if ratio > max_ratio:
        raise DataQualityError(f"reject ratio {ratio:.1%} exceeds limit {max_ratio:.1%} ({rejected}/{total})")
    return ratio


def send_alert(message: str) -> None:
    print("ALERT ->", message)          # in production: Slack/PagerDuty/SNS/email via a notifier


for total, rejected in [(10_000, 40), (10_000, 250)]:
    try:
        print(f"ok: reject ratio {enforce_reject_threshold(total, rejected):.2%}")
    except DataQualityError as error:
        send_alert(f"orders_daily failed: {error}")
```

**Output:**

```text
ok: reject ratio 0.40%
ALERT -> orders_daily failed: reject ratio 2.5% exceeds limit 1.0% (250/10000)
```

**Alerting best practices:** alert on **actionable** conditions (failures, SLA misses, freshness, volume anomalies), include context (run ID, step, counts, a link to the logs), deduplicate alerts to avoid fatigue, and make the job exit **non-zero** so the orchestrator marks it failed and can retry or notify.

---

### 15.23 Secrets Management Principles

1. **Never hardcode** credentials in code, notebooks, config files or Docker images. Never commit `.env` files.
2. Store secrets in a **secrets manager** (AWS Secrets Manager / SSM Parameter Store, Azure Key Vault, GCP Secret Manager, HashiCorp Vault) and fetch them at run time, or have the platform inject them as environment variables.
3. Prefer **identity-based access** (IAM roles, workload identity, key-pair or OAuth authentication) over long-lived passwords and access keys.
4. Apply **least privilege**: a reader role can't drop tables, and each pipeline gets its own credentials.
5. **Rotate** secrets, and make code tolerate rotation (re-fetch on authentication failure).
6. **Never log secrets.** Redact them from logs, exceptions and connection strings.

```python
# Requires: pip install boto3   (credentials come from the IAM role, not from code)
import json

import boto3
from botocore.exceptions import ClientError


def get_db_credentials(secret_id: str, region: str = "us-east-1") -> dict:
    client = boto3.client("secretsmanager", region_name=region)
    try:
        response = client.get_secret_value(SecretId=secret_id)
    except ClientError as error:
        code = error.response["Error"]["Code"]          # e.g. ResourceNotFoundException, AccessDeniedException
        raise RuntimeError(f"cannot read secret {secret_id}: {code}") from error
    return json.loads(response["SecretString"])
```

**Redacting secrets in logs (runnable):**

```python
import logging
import re
import sys

SECRET_PATTERN = re.compile(r"(password|passwd|pwd|token|secret|api_key)=([^\s&;]+)", re.IGNORECASE)


class RedactSecrets(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.msg = SECRET_PATTERN.sub(r"\1=***", record.getMessage())
        record.args = ()
        return True


logger = logging.getLogger("secure")
handler = logging.StreamHandler(sys.stdout)
handler.addFilter(RedactSecrets())
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.info("connecting with %s", "host=db1 user=etl password=S3cr3t! sslmode=require")
logger.info("calling https://api.example.com/v1?api_key=abc123&page=2")
```

**Output:**

```text
connecting with host=db1 user=etl password=*** sslmode=require
calling https://api.example.com/v1?api_key=***&page=2
```

For random tokens and passwords, use the `secrets` module (`secrets.token_urlsafe(32)`), never `random`, which is predictable.

---

### 15.24 Restartability and Recovery

**Definition:** after a failure, the pipeline can be **re-run safely** and **resumes** without duplicating or losing data.

**Ingredients:** idempotent steps ([15.6](#156-idempotency)), durable checkpoints ([15.4](#154-watermarks-and-checkpoints)), small units of work (a partition, a file, a batch), and the ability to re-run any **logical date** (backfills).

```python
import json
from pathlib import Path

STATE = Path("partition_state.json")
target: dict[str, int] = {}


def process_partition(day: str, crash_on: str | None) -> int:
    if day == crash_on:
        raise RuntimeError(f"worker lost while processing {day}")
    target[day] = 100                    # idempotent: overwrite the partition
    return 100


def run(days: list[str], crash_on: str | None = None) -> None:
    done = set(json.loads(STATE.read_text(encoding="utf-8"))) if STATE.exists() else set()
    for day in days:
        if day in done:
            print(f"skip {day} (already done)")
            continue
        process_partition(day, crash_on)
        done.add(day)
        STATE.write_text(json.dumps(sorted(done)), encoding="utf-8")   # checkpoint after success
        print(f"done {day}")


days = ["2026-10-27", "2026-10-28", "2026-10-29"]
try:
    run(days, crash_on="2026-10-28")
except RuntimeError as error:
    print("run 1 failed:", error)
run(days)                                        # restart: resumes where it stopped
print(sorted(target))
```

**Output:**

```text
done 2026-10-27
run 1 failed: worker lost while processing 2026-10-28
skip 2026-10-27 (already done)
done 2026-10-28
done 2026-10-29
['2026-10-27', '2026-10-28', '2026-10-29']
```

**Recovery runbook questions to answer for every pipeline:** How do I re-run one day? How do I backfill a month? What happens if two runs overlap (use locks or orchestrator concurrency limits)? How do I roll back a bad load (time travel, table snapshots, partition overwrite from raw data)?

---

### 15.25 Unit Testing ETL Logic

**Principle:** keep transformations **pure** ([5.16](#516-pure-functions-and-side-effects)) so they can be tested with small in-memory inputs. Test I/O with temporary files, in-memory databases and mocks (Chapter 18).

```python
# Requires: pip install pytest      Run with: pytest test_transforms.py -q
import pytest


def normalize_order(raw: dict) -> dict:
    """Pure transform under test."""
    amount = raw.get("amount")
    if amount in (None, ""):
        raise ValueError("amount is required")
    return {"order_id": int(raw["order_id"]), "amount": round(float(amount), 2),
            "country": (raw.get("country") or "UNKNOWN").strip().upper()}


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ({"order_id": "1", "amount": "10.456", "country": " in "}, {"order_id": 1, "amount": 10.46, "country": "IN"}),
        ({"order_id": "2", "amount": "0", "country": None}, {"order_id": 2, "amount": 0.0, "country": "UNKNOWN"}),
    ],
)
def test_normalize_order_valid(raw, expected):
    assert normalize_order(raw) == expected


@pytest.mark.parametrize("bad_amount", [None, ""])
def test_normalize_order_requires_amount(bad_amount):
    with pytest.raises(ValueError, match="amount is required"):
        normalize_order({"order_id": "3", "amount": bad_amount})
```

**What to test in ETL code:** happy paths; **edge cases** (empty input, NULLs, zero, negative values, unicode, duplicates, boundary dates and timezones); error paths (bad rows are rejected with the right reason); **idempotency** (running twice gives the same result); and reconciliation logic.

---

### Chapter 15 Review

**Key takeaways**
- ELT dominates in cloud warehouses; Python handles ingestion, orchestration and complex transforms.
- Incremental loads need watermarks (with tie-breakers), checkpoints and a plan for deletes.
- Idempotency (deterministic paths, partition overwrite, upserts) makes retries and backfills safe.
- Validate the schema and data quality; quarantine bad rows; fail above a threshold.
- Reconcile counts **and** sums/keys; audit every run.
- Paginate safely (cursor-based, loop guards), rate-limit, retry with backoff.
- Configuration-driven design + environment-based settings + secrets in a secrets manager.
- Structured, redacted logs; actionable alerts; non-zero exit codes on failure.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| What is idempotency? | Same input, run N times → same final state. |
| Full vs incremental load? | Reload everything vs load only changes (needs a watermark or CDC). |
| How do you handle late-arriving data? | A lookback window plus idempotent upserts; partition by event date and reprocess the affected partitions. |
| How do you detect deleted records? | CDC, soft-delete flags, or comparing key sets with the source. |
| What goes in an audit table? | Run ID, pipeline, run date, times, status, read/written/rejected counts, watermarks, error. |
| How do you protect credentials? | Secrets manager or IAM roles, least privilege, rotation, never in code or logs. |

**Common traps:** advancing the watermark before the load commits; timestamp watermarks without a tie-breaker; `str(None)`; count-only reconciliation; unbounded pagination loops; secrets in logs.

**Practice exercise:** Design (and partly code) a pipeline that ingests daily `orders_YYYYMMDD.csv` files from a landing folder into a `fct_orders` table. It should skip duplicate files by checksum, quarantine files with a bad header, reject rows with invalid amounts (failing the run above 2%), upsert by `order_id`, write an audit record, and be safely re-runnable for any date.

---

## 16. Important Libraries

This chapter summarises the libraries most relevant to Data Engineer interviews: their **purpose, key APIs, typical questions, limitations and use cases**. Topics already covered in depth link back to their chapters.

### 16.1 os

**Purpose:** an interface to the operating system: environment variables, processes, files and directories.

| API | Use |
|---|---|
| `os.environ`, `os.getenv(name, default)` | read configuration and injected secrets |
| `os.scandir(path)`, `os.walk(top)` | list directories efficiently / recursively |
| `os.makedirs(path, exist_ok=True)` | create nested folders |
| `os.replace(src, dst)` | atomic rename (overwrites the destination) |
| `os.remove`, `os.rmdir` | delete a file / an empty directory |
| `os.cpu_count()`, `os.getpid()` | sizing worker pools, logging the process ID |
| `os.sep`, `os.linesep` | platform path separator, line ending |

```python
import os
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as root:
    for relative in ("raw/2026/a.csv", "raw/2026/b.csv", "raw/c.json"):
        path = Path(root, relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"x" * 10)

    total_bytes, csv_count = 0, 0
    for directory, subdirectories, files in os.walk(root):
        for name in files:
            total_bytes += os.path.getsize(os.path.join(directory, name))
            csv_count += name.endswith(".csv")
    print(total_bytes, csv_count)

print(os.getenv("SURELY_NOT_SET_VARIABLE", "default-value"), os.cpu_count() >= 1)
```

**Output:**

```text
30 2
default-value True
```

**Interview notes:** `os.environ[name]` raises `KeyError` when the variable is missing; `os.getenv` returns `None` or the default. Environment values are always **strings**, so convert and validate them ([15.20](#1520-environment-based-configuration)). `os.scandir` is faster than `os.listdir` + `os.stat`, because it returns file type information with each entry.

---

### 16.2 pathlib

**Purpose:** object-oriented file system paths. Covered in [9.12](#912-pathlib-versus-ospath). Key APIs: `Path / "child"`, `.name`, `.stem`, `.suffix`, `.parent`, `.exists()`, `.is_file()`, `.glob()`, `.rglob()`, `.mkdir(parents=True, exist_ok=True)`, `.read_text()`, `.write_text()`, `.stat()`, `.with_suffix()`, `.resolve()`, `.unlink(missing_ok=True)`.

**Limitation:** paths are for **local or mounted** file systems. For S3/GCS use SDKs or `fsspec`-based libraries (`s3fs`, `gcsfs`), which pandas and PyArrow understand (`pd.read_parquet("s3://bucket/key")`).

---

### 16.3 sys and argparse

**Purpose:** `sys` gives access to the interpreter: `sys.argv` (command-line arguments), `sys.exit(code)`, `sys.path`, `sys.stdin`/`stdout`/`stderr`, `sys.version_info`, `sys.getsizeof`, `sys.getrecursionlimit()`. Pipelines are usually started from a command line, so **`argparse`** (standard library) is the standard way to parse arguments.

```python
import argparse
import sys
from datetime import date


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load one day of orders.")
    parser.add_argument("--run-date", type=date.fromisoformat, required=True, help="logical date, YYYY-MM-DD")
    parser.add_argument("--batch-size", type=int, default=1000)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--tables", nargs="+", default=["orders"])
    return parser.parse_args(argv)


args = parse_args(["--run-date", "2026-10-29", "--dry-run", "--tables", "orders", "items"])
print(args.run_date, args.batch_size, args.dry_run, args.tables)
print(sys.version_info >= (3, 10))
```

**Output:**

```text
2026-10-29 1000 True ['orders', 'items']
True
```

**Interview notes:** `sys.exit(0)` means success and non-zero means failure; schedulers rely on this. `sys.exit()` raises `SystemExit`, so `finally` blocks still run. Passing `argv` explicitly (as above) makes the CLI easy to test.

---

### 16.4 shutil

**Purpose:** high-level file operations: `copy`, `copy2` (keeps metadata), `copytree`, `move`, `rmtree`, `make_archive`, `unpack_archive`, `disk_usage`, `which`. See [9.13](#913-shutil-glob-and-tempfile).

```python
import shutil

usage = shutil.disk_usage(".")
print(usage.total > 0, usage.free <= usage.total)
```

**Output:**

```text
True True
```

**Use cases:** archiving processed files, checking free disk space before downloading a large file, cleaning temporary work areas. **Danger:** `shutil.rmtree` deletes recursively with no recycle bin. Validate the path first (never let it be `""`, `/` or a user-supplied value).

---

### 16.5 glob

**Purpose:** find paths matching shell-style wildcards: `*` (any characters), `?` (one character), `[0-9]` (character ranges), `**` (any depth, with `recursive=True`). `glob.iglob` returns a lazy iterator.

```python
import glob
from pathlib import Path

for name in ("orders_20261028.csv", "orders_20261029.csv", "orders_backup.csv", "items_20261029.csv"):
    Path(name).write_text("x", encoding="utf-8")
print(sorted(glob.glob("orders_2026102[0-9].csv")))
print(sorted(glob.glob("*_20261029.csv")))
```

**Output:**

```text
['orders_20261028.csv', 'orders_20261029.csv']
['items_20261029.csv', 'orders_20261029.csv']
```

**Limitations:** results are **unordered** (sort them); hidden files are skipped by default; it is local-only (S3 needs prefix listing with pagination).

---

### 16.6 re

**Purpose:** regular expressions. Covered in [3.7](#37-regular-expressions-the-re-module). Useful extras: flags and verbose patterns.

```python
import re

TIMESTAMPED_LINE = re.compile(
    r"""
    ^(?P<date>\d{4}-\d{2}-\d{2})   # ISO date
    \s+(?P<level>[a-z]+)           # level, matched case-insensitively
    \s+(?P<message>.+)$            # rest of the line
    """,
    re.VERBOSE | re.IGNORECASE | re.MULTILINE,
)
log_text = "2026-10-29 ERROR disk full\n2026-10-29 info started\nbad line"
print([(m["level"].upper(), m["message"]) for m in TIMESTAMPED_LINE.finditer(log_text)])
```

**Output:**

```text
[('ERROR', 'disk full'), ('INFO', 'started')]
```

**Limitations:** regex can't parse nested formats reliably (JSON, HTML, XML); use real parsers. Badly written patterns on untrusted input can backtrack catastrophically.

---

### 16.7 json

**Purpose:** JSON encoding and decoding. Covered in [9.7](#97-json-and-json-lines). A custom encoder centralises type handling:

```python
import json
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID


class PipelineEncoder(json.JSONEncoder):
    def default(self, value):
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        if isinstance(value, Decimal):
            return str(value)              # keep exact precision as a string
        if isinstance(value, UUID):
            return str(value)
        if isinstance(value, set):
            return sorted(value)
        return super().default(value)      # raises TypeError for unknown types


payload = {"day": date(2026, 10, 29), "amount": Decimal("10.10"), "tags": {"b", "a"},
           "id": UUID("12345678-1234-5678-1234-567812345678")}
print(json.dumps(payload, cls=PipelineEncoder, sort_keys=True))
```

**Output:**

```text
{"amount": "10.10", "day": "2026-10-29", "id": "12345678-1234-5678-1234-567812345678", "tags": ["a", "b"]}
```

**Interview notes:** JSON has no date, decimal or set types. JSON numbers become Python `float`, which loses precision for money (use `parse_float=Decimal`). Very large files: use JSON Lines, or a streaming parser such as `ijson`. For speed, `orjson` is a popular third-party alternative.

---

### 16.8 csv

**Purpose:** reading and writing delimited files correctly. Covered in [9.6](#96-csv-files). Handling **ragged rows** (too many or too few fields) with `DictReader`:

```python
import csv
import io

ragged = "id,name,city\n1,Asha,Pune\n2,Ben\n3,Cy,Rome,EXTRA\n"
reader = csv.DictReader(io.StringIO(ragged), restkey="_extra", restval=None)
for line_number, row in enumerate(reader, start=2):
    problems = []
    if row.get("_extra"):
        problems.append(f"extra fields {row['_extra']}")
    if None in (row["name"], row["city"]):
        problems.append("missing fields")
    print(line_number, row["id"], problems or "ok")
```

**Output:**

```text
2 1 ok
3 2 ['missing fields']
4 3 ["extra fields ['EXTRA']"]
```

**Limitations:** no type inference (everything is a string) and no native NULL. It is single-threaded pure Python, which is slower than pandas or PyArrow CSV readers for huge files.

---

### 16.9 datetime

**Purpose:** dates, times, durations and time zones. Getting them wrong is one of the most common causes of wrong daily totals.

**Core types:** `date` (calendar date), `time`, `datetime` (date + time, optionally with `tzinfo`), `timedelta` (a duration), `timezone` (a fixed UTC offset).

**Naive vs aware:**
- A **naive** datetime has no time zone: `2026-10-29 14:05`, but *where*?
- An **aware** datetime carries a `tzinfo`: `2026-10-29 14:05+00:00`.
- **Rule:** store and process timestamps as **aware UTC**; convert to local time only for display or for business-day boundaries.

```python
from datetime import date, datetime, timedelta, timezone

naive = datetime(2026, 10, 29, 14, 5)
aware_utc = naive.replace(tzinfo=timezone.utc)                 # declare: "this naive value is UTC"
india = timezone(timedelta(hours=5, minutes=30), "IST")
print(aware_utc.isoformat(), "->", aware_utc.astimezone(india).isoformat())
print(naive.tzinfo, aware_utc.utcoffset())

try:
    print(naive < aware_utc)
except TypeError as error:
    print("TypeError:", error)

parsed = datetime.strptime("29/10/2026 14:05", "%d/%m/%Y %H:%M")    # str -> datetime (parse)
print(parsed, "|", parsed.strftime("%Y%m%d"), "|", parsed.strftime("%A %d %B %Y"))   # datetime -> str
print(datetime.fromisoformat("2026-10-29T14:05:00Z"))           # 'Z' accepted since 3.11
print(datetime.fromtimestamp(aware_utc.timestamp(), tz=timezone.utc) == aware_utc)
print(date(2026, 10, 29).isocalendar(), date(2026, 10, 29).weekday())   # ISO week; Monday == 0
```

**Output:**

```text
2026-10-29T14:05:00+00:00 -> 2026-10-29T19:35:00+05:30
None 0:00:00
TypeError: can't compare offset-naive and offset-aware datetimes
2026-10-29 14:05:00 | 20261029 | Thursday 29 October 2026
2026-10-29 14:05:00+00:00
True
datetime.IsoCalendarDate(year=2026, week=44, weekday=4) 3
```

**Common format codes:** `%Y` year, `%m` month, `%d` day, `%H` 24-hour, `%M` minute, `%S` second, `%f` microseconds, `%z` UTC offset, `%j` day of year, `%a`/`%A` weekday name, `%b`/`%B` month name.

**Date arithmetic for pipelines:**

```python
import calendar
from datetime import date, timedelta
from typing import Iterator


def month_bounds(day: date) -> tuple[date, date]:
    """First and last day of the month containing `day`."""
    first = day.replace(day=1)
    last = day.replace(day=calendar.monthrange(day.year, day.month)[1])
    return first, last


def add_months(day: date, months: int) -> date:
    """Calendar-aware month arithmetic; clamps to the month end (Jan 31 + 1 month -> Feb 28/29)."""
    month_index = day.month - 1 + months
    year, month = day.year + month_index // 12, month_index % 12 + 1
    return date(year, month, min(day.day, calendar.monthrange(year, month)[1]))


def date_range(start: date, end: date) -> Iterator[date]:
    """Inclusive daily range: the backbone of backfills."""
    for offset in range((end - start).days + 1):
        yield start + timedelta(days=offset)


run_date = date(2026, 3, 1)
print(run_date - timedelta(days=1))                        # "yesterday" relative to the logical run date
print(month_bounds(date(2026, 2, 10)), month_bounds(date(2028, 2, 10))[1])
print(add_months(date(2026, 1, 31), 1), add_months(date(2026, 11, 15), 3))
print([d.isoformat() for d in date_range(date(2026, 10, 30), date(2026, 11, 2))])
print((date(2026, 12, 31) - date(2026, 1, 1)).days)
```

**Output:**

```text
2026-02-28
(datetime.date(2026, 2, 1), datetime.date(2026, 2, 28)) 2028-02-29
2026-02-28 2027-02-15
['2026-10-30', '2026-10-31', '2026-11-01', '2026-11-02']
364
```

**Common mistakes:**
- `timedelta(days=30)` is **not** "one month". Use calendar logic like `add_months` or `dateutil.relativedelta(months=1)`.
- Using `datetime.now()` / `date.today()` inside transforms. Pass a **logical run date** in, so backfills and retries produce the same results.
- `datetime.utcnow()` returns a **naive** value (and is deprecated since 3.12). Use `datetime.now(timezone.utc)`.
- Parsing ambiguous formats like `03/04/2026` without knowing whether the source is day-first or month-first.
- Comparing naive and aware values, or mixing local and UTC timestamps in one column.

---

### 16.10 zoneinfo

**Purpose:** IANA time zones (`"America/New_York"`, `"Asia/Kolkata"`, `"Europe/London"`) with correct **daylight saving time (DST)** rules (3.9+). On **Windows**, install the `tzdata` package (`pip install tzdata`), because Windows has no system IANA database.

```python
# Requires: pip install tzdata   (on Windows; Linux and macOS use the system time zone database)
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

new_york = ZoneInfo("America/New_York")

# Convert UTC event times to local business time (e.g. for "orders per local day")
event_utc = datetime(2026, 7, 1, 3, 30, tzinfo=timezone.utc)
print(event_utc.astimezone(new_york))                 # 2026-06-30 23:30:00-04:00  (previous local day!)

# DST gap: on 2026-03-08 New York clocks jump from 02:00 to 03:00
before_gap = datetime(2026, 3, 8, 1, 30, tzinfo=new_york)
wall_clock = before_gap + timedelta(hours=1)          # wall-clock arithmetic -> 02:30, a time that never existed
elapsed = (before_gap.astimezone(timezone.utc) + timedelta(hours=1)).astimezone(new_york)
print(wall_clock, "|", elapsed)                       # do duration arithmetic in UTC: 03:30-04:00

# DST overlap: on 2026-11-01 01:30 happens twice; `fold` chooses which one
first = datetime(2026, 11, 1, 1, 30, tzinfo=new_york, fold=0)
second = datetime(2026, 11, 1, 1, 30, tzinfo=new_york, fold=1)
print(first.utcoffset(), second.utcoffset())          # -1 day, 20:00:00 (EDT) and -1 day, 19:00:00 (EST)
```

**Why it matters for a Data Engineer:**
- A "daily" report in local time has a **23-hour** day in spring and a **25-hour** day in autumn.
- Hourly partitions in local time can collide (the repeated hour) or have gaps. **Partition by UTC.**
- Never use fixed offsets such as `-05:00` for a region that observes DST; use the IANA zone name.

**Interview question:** *How do you compute "orders per day" for a business in New York from UTC timestamps?* Convert each UTC timestamp to `America/New_York`, take `.date()`, and group by it. Query each local day's UTC boundaries (`[local midnight → next local midnight)` converted to UTC), not a fixed 24-hour window.

---

### 16.11 logging

**Purpose:** the standard, configurable logging framework. Logging levels and best practices are in [18.6](#186-logging-levels); structured JSON logging is in [15.21](#1521-structured-logging).

**Architecture:**

| Component | Role |
|---|---|
| **Logger** (`logging.getLogger(__name__)`) | the object your code calls; loggers are hierarchical (`etl.extract` is a child of `etl`) |
| **Handler** | where records go: console, file, rotating file, syslog, HTTP, cloud agents |
| **Formatter** | the layout of each record (text or JSON) |
| **Filter** | drop or modify records (e.g. redact secrets, add context) |
| **Propagation** | records bubble up to the parent loggers' handlers (beware of duplicate lines) |

```python
import logging
import logging.config
import sys

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"plain": {"format": "%(levelname)s %(name)s: %(message)s"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "stream": "ext://sys.stdout", "formatter": "plain"}},
    "loggers": {"etl": {"level": "INFO", "handlers": ["console"], "propagate": False}},
}
logging.config.dictConfig(LOGGING)

extract_logger = logging.getLogger("etl.extract")          # child of "etl": inherits its handler
extract_logger.debug("not shown: below INFO")
extract_logger.info("read %d rows from %s", 1500, "orders.csv")   # lazy %-formatting
logging.getLogger("etl.load").warning("slow insert: %.1fs", 12.34)
print(extract_logger.getEffectiveLevel() == logging.INFO, file=sys.stdout)
```

**Output:**

```text
INFO etl.extract: read 1500 rows from orders.csv
WARNING etl.load: slow insert: 12.3s
True
```

**Interview notes:**
- Use `logger = logging.getLogger(__name__)` in every module. Configure handlers **once**, in the application entry point, never inside library code.
- Pass arguments lazily, `logger.info("rows=%d", count)`, instead of an f-string. Formatting is then skipped when the level is disabled.
- `RotatingFileHandler` / `TimedRotatingFileHandler` stop log files from growing without bound. In containers, log to **stdout** and let the platform collect it.

---

### 16.12 collections

**Purpose:** specialised containers: `Counter`, `defaultdict`, `deque`, `namedtuple`, `OrderedDict`, `ChainMap`. Covered with examples in [12.20](#1220-collections-module).

**Representative interview questions:**
- *How do you find the top 3 most frequent values?* `Counter(values).most_common(3)`.
- *How do you group without checking for missing keys?* `defaultdict(list)`.
- *Which structure gives O(1) appends and pops at both ends?* `deque`.
- *How do you build an LRU cache by hand?* `OrderedDict` with `move_to_end` and `popitem(last=False)` ([20.12](#2012-design-problems)).

**Limitations:** all of them are in-memory structures, so a `Counter` over billions of distinct keys will not fit in RAM. Aggregate in the database or Spark, or use approximate algorithms (HyperLogLog for distinct counts, Count-Min Sketch for frequencies).

---

### 16.13 itertools

**Purpose:** fast, memory-efficient iterator building blocks: `chain`, `islice`, `groupby`, `accumulate`, `product`, `combinations`, `permutations`, `pairwise`, `batched`, `tee`, `zip_longest`, `count`, `cycle`, `repeat`, `takewhile`, `dropwhile`, `starmap`. Covered in [12.19](#1219-itertools-module).

**Most important for interviews:** `islice` (batching, taking the first N items lazily), `groupby` (only **consecutive** keys, so sort first), `chain.from_iterable` (flattening one level), and `pairwise` (consecutive differences).

---

### 16.14 functools

**Purpose:** higher-order function tools: `lru_cache`, `cache`, `cached_property`, `partial`, `reduce`, `wraps`, `singledispatch`, `total_ordering`. Covered in [12.18](#1218-functools-module) and [11.4](#114-caching-decorators).

**Representative interview question:** *What are the requirements for `lru_cache`?* The arguments must be hashable. The function should be pure (the same inputs always give the same output). Bound the size in long-running processes, and remember that cached values are shared and must not be mutated by callers.

---

### 16.15 typing

**Purpose:** type hints for static analysis and documentation. They are not enforced at run time ([5.15](#515-function-annotations-and-type-hints)).

| Construct | Meaning | Example |
|---|---|---|
| `list[int]`, `dict[str, float]` | generic built-ins (3.9+) | `def total(values: list[float]) -> float` |
| `X \| None` / `Optional[X]` | may be `None` | `def find(id_: int) -> dict \| None` |
| `Union[A, B]` / `A \| B` | one of several types | `int \| str` |
| `Literal["a", "b"]` | only these exact values | `mode: Literal["append", "overwrite"]` |
| `Final` | must not be reassigned | `MAX_BATCH: Final = 10_000` |
| `TypedDict` | a dict with a fixed set of typed keys (JSON records) | `class OrderRow(TypedDict): ...` |
| `Protocol` | structural interface (duck typing) | `class Sink(Protocol): def write(...)` |
| `Callable[[A], R]` | a function type | `transform: Callable[[dict], dict]` |
| `Iterable[T]`, `Iterator[T]` | streams | generator return types |
| `TypeVar`, `Generic` | generic functions and classes | `def first(items: Iterable[T]) -> T` |
| `NewType` | a distinct name for an existing type | `CustomerId = NewType("CustomerId", int)` |
| `Any` | opt out of checking | use sparingly |

```python
from typing import Final, Generic, Iterable, Literal, NewType, Protocol, TypedDict, TypeVar

T = TypeVar("T")
LoadMode = Literal["append", "overwrite", "merge"]
MAX_BATCH: Final = 10_000
CustomerId = NewType("CustomerId", int)


class OrderRow(TypedDict):
    order_id: int
    customer_id: CustomerId
    amount: float


class Writer(Protocol):
    def write(self, rows: list[OrderRow], mode: LoadMode) -> int: ...


class Batch(Generic[T]):
    def __init__(self, items: list[T]) -> None:
        self.items = items

    def first(self, default: T) -> T:
        return self.items[0] if self.items else default


def first_or(items: Iterable[T], default: T) -> T:
    return next(iter(items), default)


row: OrderRow = {"order_id": 1, "customer_id": CustomerId(42), "amount": 9.5}
print(first_or([], "none"), Batch([row]).first(row)["amount"], MAX_BATCH, type(row).__name__)
```

**Output:**

```text
none 9.5 10000 dict
```

**Notes:** Python 3.12 adds the shorter generic syntax `def first_or[T](items: Iterable[T], default: T) -> T`. Run **mypy** or **pyright** in CI to get value from type hints. Use **pydantic** when you need run-time validation of external data against types.

---

### 16.16 dataclasses

**Purpose:** generate boilerplate for record-like classes ([7.14](#714-dataclasses)). Key APIs: `@dataclass(frozen=, slots=, kw_only=, order=)`, `field(default_factory=..., repr=False, compare=False)`, `__post_init__`, `asdict`, `astuple`, `replace`, `fields`.

```python
from dataclasses import dataclass, field, fields


@dataclass(kw_only=True)                     # 3.10+: every field must be passed by name
class S3Target:
    bucket: str
    prefix: str
    access_token: str = field(repr=False)    # keep secrets out of repr() and logs
    tags: dict[str, str] = field(default_factory=dict)


target = S3Target(bucket="lake", prefix="curated/orders/", access_token="t0k3n")
print(target)
print([f.name for f in fields(target)])
```

**Output:**

```text
S3Target(bucket='lake', prefix='curated/orders/', tags={})
['bucket', 'prefix', 'access_token', 'tags']
```

**Limitations:** no run-time type validation (use `__post_init__` or pydantic); `asdict` deep-copies nested structures, which can be slow for big objects.

---

### 16.17 decimal

**Purpose:** exact **decimal** arithmetic with controllable precision and rounding. It is essential for **money**, where binary `float` rounding errors are unacceptable.

```python
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal, InvalidOperation, localcontext

print(0.1 + 0.2, Decimal("0.1") + Decimal("0.2"))
print(Decimal(0.1))                                   # constructed from a float: inherits its error
print(round(2.675, 2), Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

price = Decimal("19.985")
cents = Decimal("0.01")
print(price.quantize(cents, rounding=ROUND_HALF_UP), price.quantize(cents, rounding=ROUND_HALF_EVEN))

line_items = ["19.99", "5.01", "0.10"]
print(sum((Decimal(item) for item in line_items), Decimal("0")), sum(float(item) for item in line_items))

with localcontext() as context:
    context.prec = 6                                  # significant digits for this block only
    print(Decimal(1) / Decimal(7))

try:
    Decimal("12,50")
except InvalidOperation:
    print("InvalidOperation: '12,50' is not a decimal literal")
```

**Output:**

```text
0.30000000000000004 0.3
0.1000000000000000055511151231257827021181583404541015625
2.67 2.68
19.99 19.98
25.10 25.099999999999998
0.142857
InvalidOperation: '12,50' is not a decimal literal
```

**Best practices:**
- Construct from **strings** (`Decimal("19.99")`), never from floats.
- Round explicitly with `quantize` and a named rounding mode that matches the business rule (`ROUND_HALF_UP` is common for invoices; `ROUND_HALF_EVEN` is "banker's rounding").
- Map database `NUMERIC`/`DECIMAL` columns to `Decimal` (most drivers do this automatically). JSON needs `parse_float=Decimal` when reading and string encoding when writing.
- **Alternative:** store integer **cents** (or the smallest currency unit) as `int`.

**Limitation:** `Decimal` is slower than `float`. For large numeric datasets, use pandas/Arrow decimal types or integer cents.

---

### 16.18 tempfile

**Purpose:** create temporary files and directories safely, with unique names and automatic cleanup. See [9.13](#913-shutil-glob-and-tempfile) and the atomic-write pattern in [9.17](#917-safe-and-atomic-file-writing).

| API | Use |
|---|---|
| `TemporaryDirectory()` | scratch folder, deleted on exit |
| `NamedTemporaryFile(delete=...)` | a temp file with a visible name (on Windows it can't be reopened while open unless `delete=False`, or `delete_on_close=False` in 3.12+) |
| `mkstemp(dir=...)` | low-level unique file creation (atomic-write pattern) |
| `SpooledTemporaryFile(max_size=...)` | stays in memory until it grows beyond `max_size`, then spills to disk |
| `gettempdir()` | the system temp location |

**Use cases:** download → process → upload staging; isolated workspaces for parallel jobs; test fixtures.

---

### 16.19 gzip and zipfile

**Purpose:** compressed file I/O. See [9.11](#911-compressed-files-gzip-bz2-and-zipfile).
- `gzip.open(path, "rt"/"wt", encoding=...)` – stream-compress a single file (the most common format for CSV/JSON exports).
- `gzip.compress(bytes)` / `gzip.decompress(bytes)` – in-memory compression (e.g. for an HTTP body or an S3 `put_object`).
- `zipfile.ZipFile` – archives with many members: `namelist()`, `open(member)` for streaming, `writestr`, `extract` (validate member names to avoid path traversal).

```python
import gzip
import json

events = [{"id": number, "type": "click"} for number in range(1000)]
raw = "\n".join(json.dumps(event) for event in events).encode("utf-8")
compressed = gzip.compress(raw)
print(len(compressed) < len(raw) / 5, json.loads(gzip.decompress(compressed).decode("utf-8").splitlines()[-1]))
```

**Output:**

```text
True {'id': 999, 'type': 'click'}
```

**Interview point:** gzip files are **not splittable**, so a single 50 GB `.csv.gz` can be read by only one Spark task. Prefer many moderately sized files or splittable columnar formats (Parquet).

---

### 16.20 hashlib

**Purpose:** cryptographic hash functions (SHA-256, SHA-1, MD5, BLAKE2), used for checksums, deduplication, surrogate keys and change detection. `hmac` adds keyed signatures.

```python
import hashlib
import hmac

print(hashlib.sha256(b"abc").hexdigest()[:16], hashlib.md5(b"abc").hexdigest())


def surrogate_key(*parts: object) -> str:
    """Deterministic key from business columns (NULL-safe, delimiter-safe)."""
    normalized = "\x1f".join("<NULL>" if part is None else str(part).strip().lower() for part in parts)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:32]


print(surrogate_key("IN", "Cust-001") == surrogate_key(" in ", "cust-001"), surrogate_key("a", None) != surrogate_key("a", ""))

secret_key = b"from-a-secrets-manager"
message = b'{"event": "order_created", "id": 7}'
signature = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
print(hmac.compare_digest(signature, hmac.new(secret_key, message, hashlib.sha256).hexdigest()))
print(len(hashlib.blake2b(b"row", digest_size=8).hexdigest()))
```

**Output:**

```text
ba7816bf8f01cfea 900150983cd24fb0d6963f7d28e17f72
True True
True
16
```

**Interview notes:**
- MD5 and SHA-1 are **broken for security** (collisions can be manufactured), but acceptable for non-adversarial change detection. Use SHA-256 when in doubt.
- **Never** store passwords with a plain hash. Use `hashlib.scrypt`, `bcrypt` or `argon2` with a salt.
- Use `hmac.compare_digest` to compare signatures in constant time (it prevents timing attacks).
- Hash large files in chunks ([9.4](#94-reading-large-files-efficiently)).

---

### 16.21 requests

**Purpose:** the de-facto standard synchronous HTTP client (third-party). Key APIs: `requests.Session()`, `.get/.post(url, params=, json=, headers=, timeout=)`, `response.status_code`, `.json()`, `.raise_for_status()`, `.iter_content()`, `response.links`.

```python
# Requires: pip install requests
import os
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def build_session() -> requests.Session:
    """Session with connection pooling and automatic retries for transient failures."""
    retry = Retry(total=5, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["GET"], respect_retry_after_header=True)
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry, pool_maxsize=20))
    session.headers.update({"Authorization": f"Bearer {os.environ['API_TOKEN']}", "Accept": "application/json"})
    return session


def download_file(session: requests.Session, url: str, destination: Path) -> int:
    """Stream a large download to disk without loading it into memory."""
    written = 0
    with session.get(url, stream=True, timeout=(5, 120)) as response:
        response.raise_for_status()
        with destination.open("wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                file.write(chunk)
                written += len(chunk)
    return written
```

**Representative interview questions:**
- *Why use a `Session`?* It reuses TCP/TLS connections (connection pooling) and shares headers, auth and retry configuration.
- *What is the default timeout?* **None**, so requests can hang forever. Always pass `timeout=`.
- *How do you download a 5 GB file?* `stream=True` + `iter_content`, writing chunks to disk.
- *How do you handle 429?* Back off, honouring `Retry-After`, and add rate limiting.

**Limitations:** synchronous only. For thousands of concurrent calls use `httpx` (sync and async) or `aiohttp` with `asyncio` ([13.12](#1312-asyncio-coroutines-tasks-and-the-event-loop)).

---

### 16.22 pandas

**Purpose:** in-memory tabular data analysis and transformation (`DataFrame`, `Series`). It is the most common single-machine tool for medium-sized data. Covered in depth in **Chapter 17**.

| Strength | Limitation |
|---|---|
| expressive API: filter, join, group, pivot, time series | the whole dataset must fit in **memory** (often 2–10× the file size) |
| vectorised operations in C | row-wise `apply`/`iterrows` is slow |
| readers/writers for CSV, Parquet, JSON, Excel, SQL | mostly single-threaded |
| | dtype surprises (`int` + NaN → `float`; object columns) |

**Alternatives for bigger data:** Polars (multi-threaded, lazy), DuckDB (SQL on files), PySpark (distributed) ([17.17](#1717-pandas-versus-pyspark)).

---

### 16.23 NumPy

**Purpose:** fast, typed N-dimensional arrays and vectorised math. It is the foundation of pandas, scikit-learn and many other libraries.

```python
# Requires: pip install numpy
import numpy as np

amounts = np.array([120.0, -5.0, 0.0, 300.0, np.nan])
print(amounts.dtype, amounts.shape)                            # float64 (5,)
print(np.nansum(amounts), np.nanmean(amounts))                 # 415.0 103.75 (NaN ignored)
print(np.where(amounts < 0, "refund", "sale"))                 # vectorised if/else (NaN -> "sale")
print(amounts[~np.isnan(amounts) & (amounts > 0)])             # boolean mask: [120. 300.]
rates = np.array([1.0, 1.1, 0.9, 1.2, 1.0])
print(np.round(amounts * rates, 2))                            # element-wise, no Python loop
matrix = np.arange(6).reshape(2, 3)
print(matrix.sum(axis=0), matrix + np.array([10, 20, 30]))     # column sums; broadcasting
```

**Interview notes:**
- **Vectorisation** replaces Python loops with array operations executed in C, which is often 10–100× faster.
- **Broadcasting** applies operations between arrays of compatible shapes without copying data.
- Arrays have a **single dtype**: mixing strings and numbers creates slow `object` arrays.
- `NaN` propagates through calculations (`np.sum` → `nan`); use the `nan*` functions or masks.

---

### 16.24 pytest

**Purpose:** the most widely used Python testing framework: plain `assert` statements, fixtures, parametrisation, rich failure output, and plugins (coverage, mocking, xdist for parallel runs). Covered in **Chapter 18** ([18.2](#182-pytest-basics)).

```text
pytest -q                          # run all tests quietly
pytest tests/test_transform.py -k "null and not slow" -x    # filter by name, stop at the first failure
pytest --cov=orders_pipeline       # coverage (pytest-cov plugin)
```

---

### 16.25 unittest and unittest.mock

**Purpose:** `unittest` is the standard library's xUnit-style framework (`TestCase` classes, `setUp`/`tearDown`, `assert*` methods). `unittest.mock` replaces real dependencies (APIs, databases, clocks) with controllable fakes. It is used with pytest too.

| mock API | Use |
|---|---|
| `Mock()` / `MagicMock()` | a flexible fake object; records how it was called |
| `.return_value` | what a call returns |
| `.side_effect` | raise an exception, or return values from a sequence on successive calls |
| `assert_called_once_with(...)`, `call_count`, `call_args_list` | verify interactions |
| `patch("module.name")` | temporarily replace an attribute **where it is looked up** |
| `create_autospec(func_or_class)` / `spec=` | the fake enforces the real signature (catches typos) |

```python
import io
import unittest
from unittest import mock


def fetch_rate(client, currency: str) -> float:
    response = client.get(f"/rates/{currency}")
    if response["status"] != 200:
        raise RuntimeError(f"rate service returned {response['status']}")
    return response["rate"]


def convert(amount: float, currency: str, client) -> float:
    return round(amount * fetch_rate(client, currency), 2)


class ConvertTests(unittest.TestCase):
    def test_uses_rate_from_client(self):
        client = mock.Mock()
        client.get.return_value = {"status": 200, "rate": 1.1}
        self.assertEqual(convert(10, "EUR", client), 11.0)
        client.get.assert_called_once_with("/rates/EUR")

    def test_error_status_raises(self):
        client = mock.Mock()
        client.get.return_value = {"status": 503}
        with self.assertRaisesRegex(RuntimeError, "503"):
            convert(1, "EUR", client)

    def test_transient_failure_then_success(self):
        client = mock.Mock()
        client.get.side_effect = [ConnectionError("reset"), {"status": 200, "rate": 2.0}]
        with self.assertRaises(ConnectionError):
            convert(1, "EUR", client)
        self.assertEqual(convert(1, "EUR", client), 2.0)
        self.assertEqual(client.get.call_count, 2)

    def test_patch_the_clock(self):
        with mock.patch("time.time", return_value=1_800_000_000.0):
            import time
            self.assertEqual(time.time(), 1_800_000_000.0)


suite = unittest.defaultTestLoader.loadTestsFromTestCase(ConvertTests)
result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
print(result.testsRun, result.wasSuccessful(), len(result.failures), len(result.errors))
```

**Output:**

```text
4 True 0 0
```

**The most common mocking mistake – patching the wrong place:** if `pipeline.py` does `from requests import get`, patch **`pipeline.get`**, not `requests.get`, because `pipeline` holds its own reference. Patch where the name is **used**, not where it is defined.

---

### 16.26 boto3 (AWS SDK) for S3

**Purpose:** the AWS SDK for Python. Data engineers use it mostly for **S3** (the object store behind most data lakes), plus Secrets Manager, SQS, Glue and Athena.

**Key facts for interviews:**
- S3 is an **object store**, not a file system: "folders" are just key **prefixes**, and renaming means copy + delete.
- `list_objects_v2` returns **at most 1,000 keys per call**. Always use a **paginator**, or you will silently process only the first 1,000 files.
- `upload_file` / `download_file` automatically use **multipart transfers** for large files (parallel parts, per-part retries).
- **Stream** large objects (`get_object()["Body"].iter_lines()` or `iter_chunks()`) instead of `.read()`-ing gigabytes into memory.
- Credentials come from the **IAM role** or environment; never hardcode access keys ([15.23](#1523-secrets-management-principles)).
- Handle `botocore.exceptions.ClientError` and inspect `error.response["Error"]["Code"]` (`NoSuchKey`, `AccessDenied`, `SlowDown`, …).

```python
# Requires: pip install boto3   (uses the IAM role / environment credentials)
import json

import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

s3 = boto3.client("s3", config=Config(retries={"max_attempts": 10, "mode": "adaptive"}))


def list_keys(bucket: str, prefix: str):
    """Yield every key under a prefix, page by page (1,000 keys per page maximum)."""
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):               # an empty prefix has no "Contents"
            yield obj["Key"], obj["Size"]


def stream_jsonl(bucket: str, key: str):
    """Stream a JSON Lines object line by line without loading it into memory."""
    body = s3.get_object(Bucket=bucket, Key=key)["Body"]
    for line in body.iter_lines():
        if line:
            yield json.loads(line)


def object_exists(bucket: str, key: str) -> bool:
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError as error:
        if error.response["Error"]["Code"] in {"404", "NoSuchKey", "NotFound"}:
            return False
        raise                                               # AccessDenied etc. are real problems


s3.upload_file("local/orders.csv", "my-bucket", "landing/orders/dt=2026-10-29/orders.csv")
s3.download_file("my-bucket", "landing/orders/dt=2026-10-29/orders.csv", "/tmp/orders.csv")
s3.put_object(Bucket="my-bucket", Key="landing/orders/dt=2026-10-29/_SUCCESS", Body=b"")   # completion marker
```

**Representative interview questions:**
- *Why did your job process only 1,000 files?* No pagination on `list_objects_v2`.
- *How do you know a producer has finished writing a partition?* A `_SUCCESS` marker, a manifest file or event notifications, not "the folder exists".
- *How do you avoid listing millions of keys every run?* S3 event notifications (S3 → SQS/EventBridge), S3 Inventory, or partitioned prefixes plus a watermark of processed keys.

---

### Chapter 16 Review

**Key takeaways**
- `os`/`sys`/`argparse` connect the pipeline to its environment (config, arguments, exit codes).
- `pathlib`, `shutil`, `glob`, `tempfile`, `gzip`, `zipfile` cover local file handling; sort glob results.
- `datetime` + `zoneinfo`: aware UTC internally, IANA zones for local logic, calendar-aware month arithmetic, a logical run date passed in.
- `decimal` for money, constructed from strings and rounded explicitly.
- `hashlib` for checksums and surrogate keys; `hmac` for signatures; never plain-hash passwords.
- `requests`: Session, timeouts, retries, streaming.
- `unittest.mock`: patch where the name is looked up; use `spec`/`autospec`.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| `os.environ[k]` vs `os.getenv(k)`? | `KeyError` vs `None`/default. |
| Naive vs aware datetime? | No tzinfo vs tzinfo attached; store aware UTC. |
| Why not `float` for money? | Binary floats can't represent most decimals exactly; use `Decimal` or integer cents. |
| MD5 for deduplication? | Acceptable for non-adversarial change detection; SHA-256 for anything security-related. |
| Default timeout in requests? | None (wait forever); always set one. |
| `Mock` vs `MagicMock`? | `MagicMock` also supports magic methods (`__len__`, `__iter__`, …). |

**Common traps:** `datetime.utcnow()` (naive); `timedelta(days=30)` as a month; `Decimal(0.1)`; missing `tzdata` on Windows; patching the wrong module path.

**Practice exercise:** Write `business_day_bounds(local_day, tz_name)` that returns the UTC start (inclusive) and end (exclusive) of a local calendar day. Test it for New York on 2026-03-08 (a 23-hour day) and 2026-11-01 (a 25-hour day).

---

## 17. pandas for Data Engineers

All examples in this chapter need `pip install pandas` (and `pyarrow` for Parquet). They were written for **pandas 2.x**.

### 17.1 Series and DataFrame

**Definition:**
- A **Series** is a one-dimensional labelled array: values plus an **index**.
- A **DataFrame** is a two-dimensional table of columns, where each column is a Series with one dtype, sharing one row index.

```python
# Requires: pip install pandas
import pandas as pd

amounts = pd.Series([120.0, 75.5, 300.0], index=["o1", "o2", "o3"], name="amount")
print(amounts["o2"], amounts.sum(), amounts.index.tolist())

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "region": ["EU", "US", "EU", "APAC"],
    "amount": [120.0, 75.5, 300.0, 42.0],
})
print(orders.shape, orders.columns.tolist(), orders.dtypes.astype(str).tolist())
print(orders.head(2))
```

**Output:**

```text
75.5 495.5 ['o1', 'o2', 'o3']
(4, 3) ['order_id', 'region', 'amount'] ['int64', 'object', 'float64']
   order_id region  amount
0         1     EU   120.0
1         2     US    75.5
```

**Quick inspection:** `df.head()`, `df.tail()`, `df.info()` (dtypes, non-null counts, memory), `df.describe()`, `df.shape`, `df.dtypes`, `df["col"].value_counts()`, `df.isna().sum()`.

---

### 17.2 Reading Data: CSV, JSON, Excel, SQL and Parquet

| Source | Read | Write | Important options |
|---|---|---|---|
| CSV | `pd.read_csv` | `df.to_csv(index=False)` | `dtype=`, `parse_dates=`, `usecols=`, `na_values=`, `keep_default_na=`, `sep=`, `encoding=`, `chunksize=` |
| JSON / JSON Lines | `pd.read_json(path, lines=True)` | `df.to_json(orient="records", lines=True)` | `pd.json_normalize` for nested JSON |
| Excel | `pd.read_excel(path, sheet_name=...)` | `df.to_excel` | needs `openpyxl`; slow for big files |
| SQL | `pd.read_sql(query, con, params=..., chunksize=...)` | `df.to_sql(name, con, if_exists=..., method="multi", chunksize=...)` | use a SQLAlchemy engine or a sqlite3 connection |
| Parquet | `pd.read_parquet(path, columns=..., filters=...)` | `df.to_parquet(index=False)` | needs `pyarrow`; column pruning and predicate pushdown |

```python
# Requires: pip install pandas pyarrow
import io
import sqlite3

import pandas as pd

csv_text = "order_id,zip,order_ts,amount,status\n1,01234,2026-10-29 10:00,10.5,paid\n2,98765,2026-10-29 11:30,N/A,new\n"
frame = pd.read_csv(
    io.StringIO(csv_text),
    dtype={"zip": "string", "status": "category"},   # keep leading zeros; low-cardinality text as category
    parse_dates=["order_ts"],
    na_values=["N/A"],
)
print(frame.dtypes.astype(str).to_dict())
print(frame["zip"].tolist(), frame["amount"].isna().tolist())

nested = [{"id": 1, "customer": {"name": "Asha", "address": {"city": "Pune"}}, "items": [1, 2]}]
print(pd.json_normalize(nested, sep="_").columns.tolist())

connection = sqlite3.connect(":memory:")
frame.to_sql("orders", connection, index=False)
print(pd.read_sql("SELECT order_id, status FROM orders WHERE order_id = ?", connection, params=(2,)).to_dict("records"))
connection.close()

frame.to_parquet("orders.parquet", index=False)
print(pd.read_parquet("orders.parquet", columns=["order_id", "zip"]).dtypes.astype(str).to_dict())
```

**Output:**

```text
{'order_id': 'int64', 'zip': 'string', 'order_ts': 'datetime64[ns]', 'amount': 'float64', 'status': 'category'}
['01234', '98765'] [False, True]
['id', 'items', 'customer_name', 'customer_address_city']
[{'order_id': 2, 'status': 'new'}]
{'order_id': 'int64', 'zip': 'string'}
```

**Key point:** **always specify dtypes for identifiers** (zip codes, account numbers, phone numbers). Otherwise pandas infers numbers and silently drops leading zeros.

---

### 17.3 Selecting and Filtering Data

```python
# Requires: pip install pandas
import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "region": ["EU", "US", "EU", "APAC", "US"],
    "status": ["paid", "new", "paid", "cancelled", "paid"],
    "amount": [120.0, 75.5, 300.0, 42.0, 15.0],
})

print(orders["amount"].tolist())                              # one column -> Series
print(orders[["order_id", "amount"]].shape)                   # list of columns -> DataFrame
big_eu = orders[(orders["region"] == "EU") & (orders["amount"] > 200)]   # use & | ~ with parentheses
print(big_eu["order_id"].tolist())
print(orders[orders["status"].isin(["paid", "new"])]["order_id"].tolist())
print(orders.query("region == 'US' and amount < 50")["order_id"].tolist())
print(orders[~orders["status"].eq("cancelled")].shape[0], orders["amount"].between(40, 130).sum())
```

**Output:**

```text
[120.0, 75.5, 300.0, 42.0, 15.0]
(5, 2)
[3]
[1, 2, 3, 5]
[5]
4 3
```

**Common mistakes:** using `and`/`or` instead of `&`/`|` (raises `ValueError: The truth value of a Series is ambiguous`); missing parentheses around each condition (`&` binds tighter than `==`).

---

### 17.4 loc versus iloc

| | `loc` | `iloc` |
|---|---|---|
| Selects by | **labels** (index labels, column names) and boolean masks | **integer positions** |
| Slice end | **inclusive** (`loc["a":"c"]` includes "c") | **exclusive** (like Python) |
| Example | `df.loc[df["amount"] > 100, ["order_id", "amount"]]` | `df.iloc[0:2, [0, 2]]` |

```python
# Requires: pip install pandas
import pandas as pd

frame = pd.DataFrame({"amount": [10, 20, 30, 40]}, index=["a", "b", "c", "d"])
print(frame.loc["b":"c", "amount"].tolist(), frame.iloc[1:3, 0].tolist())   # same rows, different rules
print(frame.loc["d", "amount"], frame.iloc[-1, 0])

frame.loc[frame["amount"] > 25, "tier"] = "high"           # conditional assignment: the safe way
frame["tier"] = frame["tier"].fillna("low")
print(frame["tier"].tolist())
```

**Output:**

```text
[20, 30] [20, 30]
40 40
['low', 'low', 'high', 'high']
```

**The `SettingWithCopyWarning` / chained-assignment trap:** `df[df["a"] > 1]["b"] = 0` may modify a **temporary copy** and leave `df` unchanged. Use a single `.loc[row_mask, column] = value`, or take an explicit `.copy()` when you create a subset you will modify. pandas 2.x "Copy-on-Write" mode (the default in pandas 3.0) makes the behaviour consistent: chained assignment never modifies the original.

---

### 17.5 Handling Missing Values

pandas represents missing data as `NaN` (float), `None` (object columns), `NaT` (datetimes) or `pd.NA` (nullable dtypes).

| Method | Purpose |
|---|---|
| `isna()` / `notna()` | detect missing values |
| `dropna(subset=[...], how="any"/"all")` | drop rows with missing values in key columns |
| `fillna(value or {col: value})` | replace missing values |
| `ffill()` / `bfill()` | carry the previous / next value |
| `interpolate()` | numeric interpolation |
| `replace({"": pd.NA, "N/A": pd.NA})` | normalise placeholder tokens |

```python
# Requires: pip install pandas
import pandas as pd

raw = pd.DataFrame({
    "customer_id": [1, 2, None, 4],
    "email": ["a@x.com", "", None, "N/A"],
    "amount": [10.0, None, 5.0, 0.0],
})
clean = raw.replace({"email": {"": pd.NA, "N/A": pd.NA}})
print(clean.isna().sum().to_dict())
print(clean.dropna(subset=["customer_id"]).shape[0])
filled = clean.fillna({"amount": 0.0, "email": "unknown"})
print(filled["email"].tolist(), filled["amount"].tolist())
print(raw["amount"].sum(), raw["amount"].mean())           # NaN is skipped by default
```

**Output:**

```text
{'customer_id': 1, 'email': 3, 'amount': 1}
3
['a@x.com', 'unknown', 'unknown', 'unknown'] [10.0, 0.0, 5.0, 0.0]
15.0 5.0
```

**Data engineering judgement:** don't `fillna(0)` blindly. A missing amount is not the same as a zero amount. Record or quarantine missing required fields, and only fill when the business rule says so.

---

### 17.6 Data-Type Conversion

```python
# Requires: pip install pandas
import pandas as pd

frame = pd.DataFrame({
    "qty": ["1", "2", "x", None],
    "price": ["9.99", "5", "3.50", "1"],
    "is_active": ["true", "false", "true", None],
    "created": ["2026-10-29", "2026-13-01", "2026-10-30", None],
})
frame["qty"] = pd.to_numeric(frame["qty"], errors="coerce").astype("Int64")   # nullable integer
frame["price"] = frame["price"].astype("float64")
frame["is_active"] = frame["is_active"].map({"true": True, "false": False}).astype("boolean")
frame["created"] = pd.to_datetime(frame["created"], format="%Y-%m-%d", errors="coerce")
print(frame.dtypes.astype(str).to_dict())
print(frame["qty"].tolist(), frame["created"].isna().sum())
print(pd.Series([1, None]).dtype, pd.Series([1, None], dtype="Int64").dtype)
```

**Output:**

```text
{'qty': 'Int64', 'price': 'float64', 'is_active': 'boolean', 'created': 'datetime64[ns]'}
[1, 2, <NA>, <NA>] 2
float64 Int64
```

**Key facts:**
- `errors="coerce"` turns unparseable values into `NaN`/`NaT`. **Count them**; don't hide them.
- A regular `int64` column cannot hold missing values, so pandas silently converts it to `float64` (`[1, None]` → `[1.0, NaN]`). Nullable dtypes (`Int64`, `boolean`, `string`) keep the integer type and use `pd.NA`.
- `astype(str)` converts `NaN` to the string `"nan"`, the pandas version of the `"None"` bug.

---

### 17.7 Duplicates

```python
# Requires: pip install pandas
import pandas as pd

events = pd.DataFrame({
    "order_id": [1, 1, 2, 3, 3],
    "status": ["new", "paid", "new", "new", "new"],
    "updated_at": pd.to_datetime(["2026-10-29 09:00", "2026-10-29 10:00", "2026-10-29 09:30",
                                  "2026-10-29 08:00", "2026-10-29 08:00"]),
})
print(events.duplicated().sum(), events.duplicated(subset=["order_id"]).sum())
print(events[events.duplicated(subset=["order_id"], keep=False)]["order_id"].unique().tolist())

latest = (events.sort_values(["order_id", "updated_at"])
                .drop_duplicates(subset=["order_id"], keep="last"))      # latest version per key
print(latest[["order_id", "status"]].to_dict("records"))
```

**Output:**

```text
1 2
[1, 3]
[{'order_id': 1, 'status': 'paid'}, {'order_id': 2, 'status': 'new'}, {'order_id': 3, 'status': 'new'}]
```

**Important:** `drop_duplicates(keep="last")` keeps the last row **in the current order**. Sort by the version column first, or the result depends on file order.

---

### 17.8 Sorting

```python
# Requires: pip install pandas
import pandas as pd

staff = pd.DataFrame({"dept": ["IT", "HR", "IT", "HR"], "name": ["Bo", "Al", "Cy", "Di"], "salary": [70, 60, 90, None]})
print(staff.sort_values(["dept", "salary"], ascending=[True, False], na_position="last")["name"].tolist())
print(staff.nlargest(2, "salary")["name"].tolist())          # top-N without a full sort
print(staff.sort_index(ascending=False).index.tolist())
```

**Output:**

```text
['Al', 'Di', 'Cy', 'Bo']
['Cy', 'Bo']
[3, 2, 1, 0]
```

---

### 17.9 groupby and Aggregation

**How it works – "split, apply, combine":** split the rows into groups by key, apply an aggregation or transformation to each group, then combine the results.

```python
# Requires: pip install pandas
import pandas as pd

orders = pd.DataFrame({
    "region": ["EU", "US", "EU", "US", "EU"],
    "customer": ["a", "b", "a", "c", "d"],
    "status": ["paid", "paid", "new", "paid", "paid"],
    "amount": [100.0, 50.0, 30.0, 70.0, 20.0],
})

summary = (orders[orders["status"] == "paid"]
           .groupby("region", as_index=False)
           .agg(orders=("amount", "size"), revenue=("amount", "sum"),
                avg_order=("amount", "mean"), customers=("customer", "nunique")))
print(summary.to_dict("records"))

orders["share_of_region"] = orders["amount"] / orders.groupby("region")["amount"].transform("sum")
orders["rank_in_region"] = orders.groupby("region")["amount"].rank(method="dense", ascending=False).astype(int)
print(orders[["region", "amount", "share_of_region", "rank_in_region"]].round(2).to_dict("records")[:2])

big_regions = orders.groupby("region").filter(lambda group: group["amount"].sum() > 140)
print(sorted(big_regions["region"].unique().tolist()))
```

**Output:**

```text
[{'region': 'EU', 'orders': 2, 'revenue': 120.0, 'avg_order': 60.0, 'customers': 2}, {'region': 'US', 'orders': 2, 'revenue': 120.0, 'avg_order': 60.0, 'customers': 2}]
[{'region': 'EU', 'amount': 100.0, 'share_of_region': 0.67, 'rank_in_region': 1}, {'region': 'US', 'amount': 50.0, 'share_of_region': 0.42, 'rank_in_region': 2}]
['EU']
```

| Method | Returns | Use |
|---|---|---|
| `agg` | one row per group | summaries (`GROUP BY`) |
| `transform` | same shape as the input | per-row group metrics (window functions: share of total, group mean) |
| `filter` | a subset of the original rows | keep groups that meet a condition (`HAVING`) |
| `apply` | flexible | last resort: slow, row/group-wise Python |

**Gotchas:** `groupby` drops rows with `NaN` keys by default (`dropna=False` keeps them); `size` counts rows while `count` counts non-null values.

---

### 17.10 merge, join and concat

| Operation | SQL equivalent | Use |
|---|---|---|
| `pd.merge(left, right, on=..., how="inner"/"left"/"right"/"outer"/"cross")` | `JOIN` | combine on key columns |
| `left.join(right, how=...)` | join on the index | index-aligned joins |
| `pd.concat([df1, df2], ignore_index=True)` | `UNION ALL` | stack rows (or `axis=1` for columns) |

```python
# Requires: pip install pandas
import pandas as pd

orders = pd.DataFrame({"order_id": [1, 2, 3], "customer_id": [10, 11, 99], "amount": [50, 20, 5]})
customers = pd.DataFrame({"customer_id": [10, 11, 12], "name": ["Asha", "Ben", "Cy"]})

joined = orders.merge(customers, on="customer_id", how="left", validate="many_to_one", indicator=True)
print(joined[["order_id", "name", "_merge"]].astype(str).to_dict("records"))
print("orphans:", joined.loc[joined["_merge"] == "left_only", "order_id"].tolist())

duplicated_dim = pd.concat([customers, customers.iloc[[0]]], ignore_index=True)
try:
    orders.merge(duplicated_dim, on="customer_id", how="left", validate="many_to_one")
except pd.errors.MergeError as error:
    print("MergeError:", str(error).split(";")[0])

print(pd.concat([orders.iloc[:1], orders.iloc[2:]], ignore_index=True)["order_id"].tolist())
```

**Output:**

```text
[{'order_id': '1', 'name': 'Asha', '_merge': 'both'}, {'order_id': '2', 'name': 'Ben', '_merge': 'both'}, {'order_id': '3', 'name': 'nan', '_merge': 'left_only'}]
orphans: [3]
MergeError: Merge keys are not unique in right dataset
[1, 3]
```

**Why `validate=` matters:** a duplicate key in a dimension table makes a join **silently multiply rows** ("join explosion"), which inflates revenue. `validate="many_to_one"` turns that into an error. `indicator=True` finds orphan records (a referential-integrity check).

---

### 17.11 apply, map and Vectorized Operations

**Rule:** prefer, in order: **vectorised column operations** → built-in `.str` / `.dt` accessors → `map` with a dict → `apply` → `iterrows` (almost never).

```python
# Requires: pip install pandas numpy
import time

import numpy as np
import pandas as pd

frame = pd.DataFrame({"qty": np.arange(200_000) % 7, "price": np.linspace(1, 100, 200_000)})

started = time.perf_counter()
frame["total_apply"] = frame.apply(lambda row: row["qty"] * row["price"], axis=1)    # Python per row
apply_seconds = time.perf_counter() - started

started = time.perf_counter()
frame["total_vector"] = frame["qty"] * frame["price"]                                 # one C-level operation
vector_seconds = time.perf_counter() - started
print(np.allclose(frame["total_apply"], frame["total_vector"]), vector_seconds * 10 < apply_seconds)

frame["size"] = np.where(frame["total_vector"] > 300, "large", "small")              # vectorised if/else
frame["band"] = pd.cut(frame["price"], bins=[0, 25, 75, 100], labels=["low", "mid", "high"])
status_names = {0: "none", 1: "single"}
frame["qty_label"] = frame["qty"].map(status_names).fillna("multi")                  # dict lookup
emails = pd.Series([" A@X.COM ", "b@y.org"])
print(emails.str.strip().str.lower().str.split("@").str[1].tolist())
print(frame[["size", "band", "qty_label"]].iloc[0].tolist())
```

**Output:**

```text
True True
['x.com', 'y.org']
['small', 'low', 'none']
```

---

### 17.12 Pivot and Melt

- **`pivot_table`** turns rows into columns (long → wide), with aggregation; like a spreadsheet pivot.
- **`melt`** turns columns into rows (wide → long), the format most databases and BI tools prefer.

```python
# Requires: pip install pandas
import pandas as pd

sales = pd.DataFrame({
    "month": ["2026-01", "2026-01", "2026-02", "2026-02", "2026-02"],
    "region": ["EU", "US", "EU", "US", "US"],
    "amount": [100, 80, 120, 60, 40],
})
wide = sales.pivot_table(index="month", columns="region", values="amount", aggfunc="sum", fill_value=0)
print(wide)

long = wide.reset_index().melt(id_vars="month", var_name="region", value_name="amount")
print(long.sort_values(["month", "region"]).to_dict("records"))
```

**Output:**

```text
region    EU   US
month            
2026-01  100   80
2026-02  120  100
[{'month': '2026-01', 'region': 'EU', 'amount': 100}, {'month': '2026-01', 'region': 'US', 'amount': 80}, {'month': '2026-02', 'region': 'EU', 'amount': 120}, {'month': '2026-02', 'region': 'US', 'amount': 100}]
```

`pivot` (without `_table`) raises an error on duplicate index/column pairs; `pivot_table` aggregates them.

---

### 17.13 Datetime Processing

```python
# Requires: pip install pandas tzdata
import pandas as pd

events = pd.DataFrame({
    "event_ts": pd.to_datetime(["2026-10-29 23:30:00", "2026-10-30 00:15:00", "2026-10-30 13:00:00"], utc=True),
    "amount": [10, 20, 30],
})
events["local_ts"] = events["event_ts"].dt.tz_convert("America/New_York")
events["local_date"] = events["local_ts"].dt.date
events["hour_utc"] = events["event_ts"].dt.floor("h").dt.hour
print(events["local_date"].astype(str).tolist(), events["hour_utc"].tolist())

daily = events.set_index("event_ts").resample("D")["amount"].sum()          # time-based grouping (UTC days)
print(daily.tolist(), daily.index.strftime("%Y-%m-%d").tolist())

series = pd.Series([1, 2, 3, 4], index=pd.date_range("2026-10-01", periods=4, freq="D"))
print(series.rolling(window=2).mean().tolist())
print(pd.Timestamp("2026-01-31") + pd.DateOffset(months=1))
```

**Output:**

```text
['2026-10-29', '2026-10-29', '2026-10-30'] [23, 0, 13]
[10, 50] ['2026-10-29', '2026-10-30']
[nan, 1.5, 2.5, 3.5]
2026-02-28 00:00:00
```

Note how the 00:15 UTC event belongs to **October 29** in New York. Always decide which time zone defines "a day" for a report.

---

### 17.14 Chunk-Based File Reading

**Definition:** `read_csv(..., chunksize=N)` (or `iterator=True`) returns an iterator of DataFrames with N rows each, so files larger than memory can be processed piece by piece.

```python
# Requires: pip install pandas
import pandas as pd

with open("big_orders.csv", "w", encoding="utf-8") as file:
    file.write("order_id,region,amount\n")
    for order_id in range(1, 100_001):
        file.write(f"{order_id},{['EU', 'US', 'APAC'][order_id % 3]},{order_id % 50}.5\n")

running_totals: dict[str, float] = {}
row_count = 0
for chunk in pd.read_csv("big_orders.csv", chunksize=25_000, usecols=["region", "amount"],
                         dtype={"region": "category", "amount": "float64"}):
    row_count += len(chunk)
    for region, total in chunk.groupby("region", observed=True)["amount"].sum().items():
        running_totals[region] = running_totals.get(region, 0.0) + total
print(row_count, {region: round(total, 1) for region, total in sorted(running_totals.items())})
```

**Output:**

```text
100000 {'APAC': 833316.5, 'EU': 833349.5, 'US': 833334.0}
```

**Rules for chunked processing:** only **combinable** aggregations work directly (sum, count, min, max). For a mean, keep sum and count; for medians or distinct counts you need other techniques. Write each processed chunk out (append to Parquet partitions or a database) instead of collecting chunks in a list.

---

### 17.15 Memory Optimization

| Technique | Effect |
|---|---|
| `usecols=[...]` | don't load unused columns |
| Explicit `dtype=` | avoid 64-bit defaults and object columns |
| Downcast numbers: `pd.to_numeric(s, downcast="integer")` | `int64` → `int8`/`int16`/`int32` |
| `category` for low-cardinality strings | stores integer codes plus one copy of each label |
| `string[pyarrow]` / Arrow-backed dtypes | compact strings |
| Process in chunks; free intermediates (`del df`) | bounded peak memory |
| Parquet with column selection | read less |

```python
# Requires: pip install pandas numpy
import numpy as np
import pandas as pd

rows = 200_000
frame = pd.DataFrame({
    "country": np.random.default_rng(0).choice(["IN", "US", "DE", "FR"], size=rows),
    "quantity": np.random.default_rng(1).integers(0, 100, size=rows),
})
before = frame.memory_usage(deep=True).sum()
frame["country"] = frame["country"].astype("category")
frame["quantity"] = pd.to_numeric(frame["quantity"], downcast="integer")
after = frame.memory_usage(deep=True).sum()
print(frame.dtypes.astype(str).to_dict(), f"reduced by {1 - after / before:.0%}")
```

**Output:**

```text
{'country': 'category', 'quantity': 'int8'} reduced by 97%
```

`memory_usage(deep=True)` measures the real size of object (string) columns. Without `deep=True` they are badly under-counted.

---

### 17.16 Common Performance Problems

| Problem | Fix |
|---|---|
| `iterrows()` / `apply(axis=1)` over millions of rows | vectorise; use `np.where`, `.str`, `.dt`, `merge` |
| Appending to a DataFrame in a loop (`pd.concat` per row) | collect dicts in a list, build one DataFrame at the end |
| Object dtype for numbers or dates | convert once with `to_numeric` / `to_datetime(format=...)` |
| `to_datetime` without `format=` on large columns | pass an explicit `format` |
| Joining on mismatched key dtypes (`int` vs `str`) | align dtypes before `merge` |
| Loading entire files to use 3 columns | `usecols=`, Parquet column pruning |
| `to_sql` row-by-row | `method="multi"`, `chunksize=`, or a native bulk load (`COPY`) |
| Repeated filtering in a loop | `groupby` once |
| Data bigger than RAM | chunks, Polars (lazy), DuckDB, Spark |

---

### 17.17 Pandas versus PySpark

| Aspect | pandas | PySpark |
|---|---|---|
| Execution | single process, in memory, **eager** | distributed across a cluster, **lazy** (actions trigger work) |
| Data size | up to a few GB comfortably (limited by RAM) | GB to PB |
| Start-up / overhead | none | JVM and cluster scheduling: seconds to minutes |
| API | rich, flexible, index-based | SQL-like DataFrame API, no row index |
| Fault tolerance | none (the process dies, the work is lost) | task retries; recomputes from lineage |
| Best for | small/medium data, quick transforms, tests, notebooks | large joins/aggregations, lakehouse pipelines |
| Bridges | `pyspark.pandas` (pandas API on Spark), `toPandas()` (collects to the driver – risky), Arrow-optimised UDFs | |

**Decision guide:** if the data fits comfortably in one machine's memory (with 3–5× headroom) and the job is simple, pandas, Polars or DuckDB is cheaper and faster to develop. If it doesn't fit, or must scale with data growth, or needs distributed joins, use Spark (or warehouse SQL). See the scenario in [21.17](#2117-choosing-python-pandas-or-pyspark).

---

### 17.18 Interview Coding Examples

**1. Top 2 customers by revenue per region (window-style ranking):**

```python
# Requires: pip install pandas
import pandas as pd

orders = pd.DataFrame({
    "region": ["EU", "EU", "EU", "US", "US", "US"],
    "customer": ["a", "b", "c", "d", "e", "d"],
    "amount": [100, 300, 200, 50, 80, 60],
})
revenue = orders.groupby(["region", "customer"], as_index=False)["amount"].sum()
revenue["rank"] = revenue.groupby("region")["amount"].rank(method="first", ascending=False)
top2 = revenue[revenue["rank"] <= 2].sort_values(["region", "rank"])
print(top2[["region", "customer", "amount"]].to_dict("records"))
```

**Output:**

```text
[{'region': 'EU', 'customer': 'b', 'amount': 300}, {'region': 'EU', 'customer': 'c', 'amount': 200}, {'region': 'US', 'customer': 'd', 'amount': 110}, {'region': 'US', 'customer': 'e', 'amount': 80}]
```

**2. Find customers whose order count increased month over month:**

```python
# Requires: pip install pandas
import pandas as pd

orders = pd.DataFrame({
    "customer": ["a", "a", "a", "b", "b", "b"],
    "order_date": pd.to_datetime(["2026-01-05", "2026-02-01", "2026-02-20", "2026-01-10", "2026-01-11", "2026-02-02"]),
})
monthly = (orders.assign(month=orders["order_date"].dt.to_period("M"))
                 .groupby(["customer", "month"]).size().rename("orders").reset_index())
monthly["previous"] = monthly.groupby("customer")["orders"].shift(1)
growing = monthly[monthly["orders"] > monthly["previous"]]["customer"].unique().tolist()
print(monthly.astype(str).values.tolist(), growing)
```

**Output:**

```text
[['a', '2026-01', '1', 'nan'], ['a', '2026-02', '2', '1.0'], ['b', '2026-01', '2', 'nan'], ['b', '2026-02', '1', '2.0']] ['a']
```

**3. Compare two snapshots (inserted, deleted, updated):**

```python
# Requires: pip install pandas
import pandas as pd

old = pd.DataFrame({"id": [1, 2, 3], "status": ["new", "paid", "paid"]})
new = pd.DataFrame({"id": [2, 3, 4], "status": ["paid", "shipped", "new"]})
both = old.merge(new, on="id", how="outer", suffixes=("_old", "_new"), indicator=True)
inserted = both.loc[both["_merge"] == "right_only", "id"].tolist()
deleted = both.loc[both["_merge"] == "left_only", "id"].tolist()
updated = both.loc[(both["_merge"] == "both") & (both["status_old"] != both["status_new"]), "id"].tolist()
print(inserted, deleted, updated)
```

**Output:**

```text
[4] [1] [3]
```

---

### Chapter 17 Review

**Key takeaways**
- Specify dtypes on read (identifiers as strings, categories, dates with formats).
- `loc` = labels (inclusive slices), `iloc` = positions (exclusive slices); assign with a single `.loc`.
- Missing values: detect, decide, document; nullable dtypes avoid int → float conversion.
- `agg` / `transform` / `filter` map to GROUP BY / window functions / HAVING.
- `merge(..., validate=..., indicator=True)` protects against join explosions and finds orphans.
- Vectorise; avoid `iterrows` and row-wise `apply`.
- Chunk big files; measure memory with `deep=True`; move to Polars/DuckDB/Spark when data outgrows RAM.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| `loc` vs `iloc`? | Label-based (inclusive) vs position-based (exclusive). |
| `merge` vs `join` vs `concat`? | Key-based join vs index-based join vs stacking. |
| `apply` vs `map` vs vectorised? | Row/column Python function vs element-wise mapping vs C-level column operation (fastest). |
| Why did my int column become float? | It contains missing values; use `Int64`. |
| How do you process a 20 GB CSV with pandas? | `chunksize`, `usecols`, dtypes, combinable aggregations; or switch tools. |
| `size` vs `count` in groupby? | All rows vs non-null values. |

**Common traps:** `and` instead of `&`; chained assignment; `drop_duplicates` without sorting; `astype(str)` producing `"nan"`; `toPandas()` on huge Spark DataFrames.

**Practice exercise:** Given `orders(order_id, customer_id, order_ts_utc, amount)` and `customers(customer_id, country, tz)`, compute daily revenue per country **in each customer's local time zone**, exclude orders from unknown customers (report how many there were), and return the top 3 days per country.

---

## 18. Testing, Logging and Code Quality

### 18.1 Unit, Integration and End-to-End Testing

| Level | Scope | Speed | Data Engineering example |
|---|---|---|---|
| **Unit** | one function or class, dependencies faked | milliseconds | `normalize_order(row)` returns the right types; `split_valid` rejects bad rows |
| **Integration** | several components with real infrastructure | seconds | a loader writes to a real PostgreSQL container; reading Parquet from local MinIO (S3-compatible) |
| **End-to-end (E2E)** | the whole pipeline from source to target | minutes | run the DAG on a sample dataset in a staging environment, then check the outputs and reconciliation |
| **Data tests** | the data itself, at run time | per run | not-null, unique, accepted values, freshness, row-count checks ([15.9](#159-data-quality-checks)) |

**The test pyramid:** many fast unit tests, fewer integration tests, a handful of E2E tests. Code tests prove the **logic** is right; data tests prove the **inputs** are right. Pipelines need both.

---

### 18.2 pytest Basics

**Definition:** pytest discovers files named `test_*.py` (or `*_test.py`) and functions named `test_*`, and uses plain `assert` with detailed failure messages.

```python
# Requires: pip install pytest      Run with: pytest test_basics.py -q
import pytest


def dedupe_keep_order(items: list) -> list:
    return list(dict.fromkeys(items))


def safe_ratio(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("denominator must not be zero")
    return numerator / denominator


def test_dedupe_preserves_first_occurrence():
    assert dedupe_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_dedupe_empty_input():
    assert dedupe_keep_order([]) == []


def test_ratio_float_comparison():
    assert safe_ratio(1, 3) == pytest.approx(0.3333, rel=1e-3)     # never == on floats


def test_ratio_zero_denominator():
    with pytest.raises(ZeroDivisionError, match="must not be zero"):
        safe_ratio(1, 0)
```

**Useful commands:** `pytest -q` (quiet), `-x` (stop at the first failure), `-k "dedupe and not slow"` (select by name), `-m integration` (select by marker), `--lf` (rerun the last failures), `-vv` (verbose diffs), `--cov` (coverage, with pytest-cov).

---

### 18.3 Fixtures and Parameterized Tests

**Fixtures** provide reusable setup and teardown (temporary folders, DB connections, sample data). They are injected by **argument name**. Code after `yield` runs as teardown. Scope can be `function` (the default), `module` or `session`. Shared fixtures go in `conftest.py`.

**Parametrisation** runs one test function with many input/expected pairs, covering edge cases without duplicated code.

```python
# Requires: pip install pytest      Run with: pytest test_fixtures.py -q
import sqlite3

import pytest


def load_rows(conn: sqlite3.Connection, rows: list[tuple[int, float]]) -> int:
    with conn:
        conn.executemany("INSERT INTO orders (id, amount) VALUES (?, ?)", rows)
    return conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]


def parse_amount(raw: str | None) -> float | None:
    if raw is None or raw.strip() == "":
        return None
    return float(raw.replace(",", ""))


@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, amount REAL)")
    yield conn                    # the test runs here
    conn.close()                  # teardown, even if the test fails


@pytest.fixture
def sample_rows() -> list[tuple[int, float]]:
    return [(1, 10.0), (2, 20.5)]


def test_load_rows_counts(db, sample_rows):
    assert load_rows(db, sample_rows) == 2


def test_duplicate_key_rolls_back(db, sample_rows):
    load_rows(db, sample_rows)
    with pytest.raises(sqlite3.IntegrityError):
        load_rows(db, [(3, 1.0), (1, 99.0)])
    assert db.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 2   # row 3 was rolled back


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("10", 10.0), (" 2.5 ", 2.5), ("1,234.50", 1234.5), ("", None), (None, None), ("0", 0.0)],
    ids=["int", "spaces", "thousands", "empty", "none", "zero"],
)
def test_parse_amount(raw, expected):
    assert parse_amount(raw) == expected


@pytest.mark.parametrize("bad", ["abc", "1.2.3"])
def test_parse_amount_rejects_garbage(bad):
    with pytest.raises(ValueError):
        parse_amount(bad)
```

**Built-in fixtures worth knowing:** `tmp_path` (a unique temporary directory as a `Path`), `monkeypatch` (set environment variables and attributes, restored automatically), `caplog` (capture log records), `capsys` (capture stdout/stderr).

---

### 18.4 Mocking

**Definition:** replacing a real dependency (an HTTP API, S3, a database, the clock, random numbers) with a **test double** that returns controlled results and records how it was used.

| Double | Meaning |
|---|---|
| Stub | returns canned data |
| Mock | also verifies the calls (arguments, counts) |
| Fake | a simplified working implementation (an in-memory repository, SQLite instead of PostgreSQL) |

**Guidelines:**
- Mock at **system boundaries** (network, cloud SDKs, time), not your own internal logic.
- Patch **where the name is looked up** (`mypipeline.extract.requests.get`, not `requests.get`, if `extract.py` imports requests).
- Use `autospec=True` / `create_autospec`, so a mock rejects calls that don't match the real signature.
- Prefer **dependency injection** (pass a client into the function), which often removes the need for patching.

```python
# Requires: pip install pytest      Run with: pytest test_mocking.py -q
from unittest import mock

import pytest


class ApiError(Exception):
    pass


def fetch_all_pages(client, url: str) -> list[dict]:
    """Collect every page from a cursor-paginated API using an injected client."""
    records, cursor = [], None
    while True:
        response = client.get(url, params={"cursor": cursor} if cursor else {})
        if response.status_code != 200:
            raise ApiError(f"status {response.status_code}")
        payload = response.json()
        records.extend(payload["data"])
        cursor = payload.get("next")
        if not cursor:
            return records


def fake_response(status: int, payload: dict | None = None) -> mock.Mock:
    response = mock.Mock(status_code=status)
    response.json.return_value = payload or {}
    return response


def test_fetch_all_pages_follows_cursor():
    client = mock.Mock()
    client.get.side_effect = [
        fake_response(200, {"data": [{"id": 1}], "next": "c2"}),
        fake_response(200, {"data": [{"id": 2}], "next": None}),
    ]
    assert fetch_all_pages(client, "/orders") == [{"id": 1}, {"id": 2}]
    assert client.get.call_args_list == [
        mock.call("/orders", params={}),
        mock.call("/orders", params={"cursor": "c2"}),
    ]


def test_fetch_all_pages_raises_on_error():
    client = mock.Mock()
    client.get.return_value = fake_response(503)
    with pytest.raises(ApiError, match="503"):
        fetch_all_pages(client, "/orders")


def test_environment_and_clock(monkeypatch):
    monkeypatch.setenv("PIPELINE_ENV", "test")                     # restored after the test
    with mock.patch("time.time", return_value=1_800_000_000):
        import os
        import time
        assert os.environ["PIPELINE_ENV"] == "test"
        assert time.time() == 1_800_000_000
```

**Over-mocking warning:** tests that mock everything only prove that the mocks were called. Keep some integration tests against real (containerised) services. Tools such as `testcontainers`, `moto` (AWS) and `responses` / `respx` (HTTP) help.

---

### 18.5 Testing Files, Databases and APIs

```python
# Requires: pip install pytest      Run with: pytest test_io.py -q
import csv
import json
from pathlib import Path

import pytest


def csv_to_jsonl(source: Path, target: Path, rejects: Path) -> dict[str, int]:
    """Convert CSV to JSON Lines; invalid amounts go to a rejects CSV."""
    counts = {"read": 0, "written": 0, "rejected": 0}
    with source.open(newline="", encoding="utf-8") as src, \
         target.open("w", encoding="utf-8") as out, \
         rejects.open("w", newline="", encoding="utf-8") as bad:
        reject_writer = csv.writer(bad)
        reject_writer.writerow(["line", "raw_amount", "reason"])
        for line_number, row in enumerate(csv.DictReader(src), start=2):
            counts["read"] += 1
            try:
                row["amount"] = float(row["amount"])
            except ValueError as error:
                reject_writer.writerow([line_number, row["amount"], str(error)])
                counts["rejected"] += 1
                continue
            out.write(json.dumps(row) + "\n")
            counts["written"] += 1
    return counts


@pytest.fixture
def source_csv(tmp_path: Path) -> Path:
    path = tmp_path / "orders.csv"
    path.write_text("id,amount\n1,10.5\n2,bad\n3,7\n", encoding="utf-8")
    return path


def test_csv_to_jsonl_counts_and_outputs(tmp_path, source_csv):
    target, rejects = tmp_path / "out.jsonl", tmp_path / "rejects.csv"
    counts = csv_to_jsonl(source_csv, target, rejects)

    assert counts == {"read": 3, "written": 2, "rejected": 1}
    assert counts["read"] == counts["written"] + counts["rejected"]           # reconciliation
    written = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
    assert [row["id"] for row in written] == ["1", "3"]
    with rejects.open(newline="", encoding="utf-8") as file:
        reject_rows = list(csv.DictReader(file))
    assert reject_rows[0]["line"] == "3" and reject_rows[0]["raw_amount"] == "bad"


def test_empty_file_produces_empty_outputs(tmp_path):
    source = tmp_path / "empty.csv"
    source.write_text("id,amount\n", encoding="utf-8")
    counts = csv_to_jsonl(source, tmp_path / "o.jsonl", tmp_path / "r.csv")
    assert counts == {"read": 0, "written": 0, "rejected": 0}
```

**Strategies by dependency:**

| Dependency | Unit-test approach | Integration-test approach |
|---|---|---|
| Local files | `tmp_path` with small fixture files | realistic sample files in `tests/data/` |
| SQL database | SQLite in memory, or a fake repository | a real DB in Docker (testcontainers), transactions rolled back after each test |
| HTTP API | inject a client; `mock`, `responses`, `respx` | a sandbox API or contract tests |
| AWS S3 / SQS | `moto` (in-memory AWS) | LocalStack / MinIO or a test account |
| Time / dates | pass `run_date` in; patch the clock | – |

---

### 18.6 Logging Levels

| Level | Value | Use in a pipeline |
|---|---|---|
| `DEBUG` | 10 | detailed diagnostics (SQL text, per-batch details); off in production by default |
| `INFO` | 20 | normal milestones: job started, file processed, rows loaded, job finished |
| `WARNING` | 30 | something unexpected but handled: retries, rejected rows below the threshold, a slow step |
| `ERROR` | 40 | an operation failed: a file could not be loaded, a batch failed |
| `CRITICAL` | 50 | the job or service cannot continue: missing config, the target is unavailable after all retries |

A logger emits records **at or above** its effective level. Handlers can filter further, e.g. send `ERROR+` to an alerting channel.

```python
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.WARNING, format="%(levelname)s:%(name)s:%(message)s")
log = logging.getLogger("levels_demo")
log.debug("hidden")
log.info("hidden too")
log.warning("retrying batch %d (attempt %d/%d)", 7, 2, 5)
log.error("batch %d failed", 7)
log.setLevel(logging.DEBUG)
log.debug("visible after lowering the logger level")
print(logging.getLevelName(30), logging.INFO)
```

**Output:**

```text
WARNING:levels_demo:retrying batch 7 (attempt 2/5)
ERROR:levels_demo:batch 7 failed
DEBUG:levels_demo:visible after lowering the logger level
WARNING 20
```

---

### 18.7 Structured and Contextual Logging

Covered with a full example in [15.21](#1521-structured-logging). Summary:
- Emit **JSON** with consistent field names.
- Attach **context** (run_id, pipeline, run_date, table, batch, file) with `LoggerAdapter`, `extra=`, or `contextvars` for async and threaded code.
- Log **metrics-like facts** (rows, durations, bytes) as fields, not buried in message text, so they can be queried and charted.
- Correlate across systems with a shared run ID or trace ID.

---

### 18.8 Avoiding Sensitive Information in Logs

**Never log:** passwords, tokens, API keys, connection strings with credentials, full payment card numbers, national IDs, or whole raw records containing personal data (PII).

**Techniques:**
- Log **identifiers and counts**, not record contents (`"rejected order_id=123: invalid amount"`).
- **Redaction filters** on handlers ([15.23](#1523-secrets-management-principles)).
- `repr=False` on secret dataclass fields ([16.16](#1616-dataclasses)); custom `__repr__` on connection objects.
- **Mask** values when you must show them (`****1111`).
- Watch exception messages: driver errors may include the failing SQL **with parameter values**.
- Restrict access to logs, and set retention periods that match compliance requirements (GDPR, PCI DSS, HIPAA).

```python
def mask(value: str, visible: int = 4) -> str:
    return "*" * max(len(value) - visible, 0) + value[-visible:]


print(mask("4111111111111111"), mask("abc"))
```

**Output:**

```text
************1111 abc
```

---

### 18.9 PEP 8 and Formatting

**PEP 8** is the Python style guide. Key points: 4-space indentation; `snake_case` functions and variables, `PascalCase` classes, `UPPER_CASE` constants; two blank lines around top-level definitions; imports at the top, grouped as **standard library → third-party → local** (one per line); spaces around operators; lines of about 79–100 characters (the team decides).

**Automate it:** **Black** or **ruff format** (an opinionated formatter), **ruff** (a very fast linter that covers pyflakes, pycodestyle, isort, many bug patterns), and **pre-commit** hooks that run them before each commit. Formatting debates then disappear from code review.

---

### 18.10 Type Hints and Static Analysis

| Tool | Checks |
|---|---|
| **mypy** / **pyright** | type errors: `None` passed where a `str` is required, wrong return types, missing attributes |
| **ruff** / flake8 / pylint | unused imports and variables, undefined names, bare excepts, mutable defaults, complexity |
| **bandit** | security issues: hardcoded passwords, `pickle`/`yaml.load` on untrusted data, `shell=True` |
| **pip-audit** | known vulnerabilities in dependencies |

```python
def batch_total(amounts: list[float]) -> float:
    return sum(amounts)


def describe(user_name: str | None) -> str:
    # mypy would flag `user_name.upper()` here: user_name may be None
    return user_name.upper() if user_name is not None else "UNKNOWN"


print(batch_total([1.5, 2.5]), describe(None))
```

**Output:**

```text
4.0 UNKNOWN
```

Run these tools in **CI** on every pull request, and fail the build on errors.

---

### 18.11 Docstrings

**Definition:** a string literal placed first in a module, class or function, available as `__doc__` and used by `help()`, IDEs and documentation generators. Common styles: Google, NumPy and reStructuredText (Sphinx). Pick one per project.

```python
def load_partition(table: str, run_date: str, *, overwrite: bool = True) -> int:
    """Load one daily partition into the warehouse.

    Args:
        table: Target table name (must be in the allowlist).
        run_date: Logical date in ISO format, e.g. "2026-10-29".
        overwrite: Replace the existing partition instead of appending.

    Returns:
        Number of rows written.

    Raises:
        ValueError: If the table is not allowed or the date is invalid.
    """
    return 0


print(load_partition.__doc__.splitlines()[0])
```

**Output:**

```text
Load one daily partition into the warehouse.
```

**What to document:** *why* (business rules, units, time zones, idempotency, side effects), not *what* the code obviously does.

---

### 18.12 Code Organization

- **Separate concerns:** `extract`, `transform` (pure), `load`, `quality`, `config`, `cli` modules ([10.9](#109-package-structure)).
- **Functional core, imperative shell:** pure transformations in the middle, I/O at the edges ([5.16](#516-pure-functions-and-side-effects)).
- **Dependency injection** for clients, connections and clocks.
- **One entry point** per job (`main(argv) -> int`) that parses arguments, loads config, sets up logging and calls the pipeline.
- **Small functions** with clear names; avoid deep nesting (use early returns and guard clauses).
- **Shared utilities** in a versioned internal package, not copy-pasted ([10.11](#1011-building-a-reusable-data-engineering-utility-package)).
- Keep **orchestration code** (Airflow DAGs) thin. DAG files should import and call your package, not contain business logic.

---

### 18.13 Defensive Programming

**Definition:** writing code that **fails early and clearly** on invalid input or state, instead of producing wrong results silently.

| Technique | Example |
|---|---|
| Validate inputs at boundaries | check config, CLI arguments, file headers and schemas before processing |
| Guard clauses | `if not rows: logger.info("nothing to load"); return 0` |
| Explicit `None` checks | `if value is None` instead of truthiness |
| Assertions for internal invariants (not for input validation) | `assert total >= 0`, but `python -O` removes asserts, so never rely on them for real checks |
| Timeouts on every external call | HTTP, DB, queue waits |
| Bounded resources | `maxsize` on queues, `maxlen` on deques, batch sizes, retry caps |
| Immutable data where possible | frozen dataclasses, tuples |
| Reconcile outputs | row counts and control totals ([15.13](#1513-source-to-target-reconciliation)) |
| Fail loudly | raise specific exceptions; non-zero exit codes; never `except: pass` |

```python
def require_positive_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an int, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"{name} must be > 0, got {value}")
    return value


for candidate in (500, True, -1):
    try:
        print(require_positive_int("batch_size", candidate))
    except (TypeError, ValueError) as error:
        print(type(error).__name__, error)
```

**Output:**

```text
500
TypeError batch_size must be an int, got bool
ValueError batch_size must be > 0, got -1
```

---

### 18.14 Production-Readiness Checklist

**Correctness**
- [ ] Unit tests for transformations, including edge cases (NULLs, empty input, duplicates, time zones)
- [ ] Data-quality checks with blocking and warning severities
- [ ] Source-to-target reconciliation (counts plus control totals)

**Reliability**
- [ ] Idempotent writes; safe to re-run any logical date
- [ ] Checkpoints and watermarks persisted after successful writes
- [ ] Retries with backoff for transient errors only; timeouts on all I/O
- [ ] Atomic outputs (no partial files or tables visible)

**Operability**
- [ ] Structured logs with a run ID; audit record per run
- [ ] Metrics and alerts (failures, duration, volume, freshness); non-zero exit code on failure
- [ ] A runbook: how to re-run, backfill, roll back

**Security**
- [ ] No secrets in code, config, logs or images; least-privilege credentials
- [ ] Parameterised SQL; validated identifiers; safe deserialisation (no untrusted pickle or `yaml.load`)
- [ ] PII handling (masking, retention) reviewed

**Maintainability**
- [ ] Pinned dependencies; reproducible environment (lock file / container image)
- [ ] Formatter, linter and type checker in CI
- [ ] Configuration-driven where it adds value; documented assumptions (time zone, NULL conventions, keys)

---

### Chapter 18 Review

**Key takeaways**
- Test logic with fast unit tests; test integration with real services in containers; test data at run time.
- pytest: plain asserts, fixtures (`tmp_path`, `monkeypatch`), parametrisation, `pytest.raises`, `pytest.approx`.
- Mock at boundaries, patch where names are looked up, prefer dependency injection.
- Use log levels deliberately; log context and counts, never secrets or raw PII.
- Automate style, linting, typing and security checks in CI.
- Be defensive at boundaries; fail loudly.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| Unit vs integration test? | Isolated logic with fakes vs components working with real dependencies. |
| What is a fixture? | Reusable setup/teardown injected into tests by name. |
| How do you test code that calls an API? | Inject the client and mock it; add a contract or sandbox integration test. |
| How do you test time-dependent code? | Pass the date or time in (preferred), or patch the clock. |
| What do you log at INFO vs DEBUG? | Milestones and counts vs detailed diagnostics. |
| Why not rely on `assert` for validation? | Asserts are removed with `python -O`; raise exceptions instead. |

**Common traps:** tests that depend on the current date; shared state between tests; over-mocking; comparing floats with `==`; logging full records with PII.

**Practice exercise:** Write pytest tests for the `apply_cdc` function in [15.5](#155-cdc-fundamentals): insert, update, delete, out-of-order events in one batch, and replaying the same batch twice (idempotency). Use parametrisation for the event sequences.

---

## 19. Design Patterns for Data Engineering

Design patterns are reusable solutions to recurring design problems. In Python, many classic patterns become **simpler** because functions are first-class objects and modules are natural singletons. Use a pattern when it removes real duplication or coupling, not to look sophisticated.

### 19.1 Factory

**Problem:** choose and construct the right implementation (a reader, writer or connector) from **configuration**, without `if/elif` chains scattered through the code.

```python
from typing import Protocol


class Reader(Protocol):
    def read(self, location: str) -> list[dict]: ...


class CsvReader:
    def read(self, location: str) -> list[dict]:
        return [{"source": "csv", "location": location}]


class ParquetReader:
    def read(self, location: str) -> list[dict]:
        return [{"source": "parquet", "location": location}]


class ApiReader:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def read(self, location: str) -> list[dict]:
        return [{"source": "api", "location": f"{self.base_url}/{location}"}]


READER_FACTORIES = {
    "csv": lambda options: CsvReader(),
    "parquet": lambda options: ParquetReader(),
    "api": lambda options: ApiReader(base_url=options["base_url"]),
}


def create_reader(kind: str, **options) -> Reader:
    try:
        return READER_FACTORIES[kind](options)
    except KeyError:
        raise ValueError(f"unknown reader {kind!r}; expected one of {sorted(READER_FACTORIES)}") from None


print(create_reader("parquet").read("s3://lake/orders/"))
print(create_reader("api", base_url="https://api.example.com").read("orders"))
try:
    create_reader("xml")
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
[{'source': 'parquet', 'location': 's3://lake/orders/'}]
[{'source': 'api', 'location': 'https://api.example.com/orders'}]
ValueError: unknown reader 'xml'; expected one of ['api', 'csv', 'parquet']
```

**Useful when:** the implementation is chosen at run time from config, and new types are added often (a registry decorator, [11.7](#117-class-decorators-and-decorator-classes), lets plug-ins register themselves).
**Overengineering when:** there is only one implementation, or the choice never changes.

---

### 19.2 Strategy

**Problem:** the same step needs **interchangeable algorithms**: different load modes (append / overwrite / merge), deduplication rules or masking methods.

In Python, a strategy is often just **a function**.

```python
from typing import Callable

LoadStrategy = Callable[[list[dict], list[dict], str], list[dict]]


def append(target: list[dict], batch: list[dict], key: str) -> list[dict]:
    return target + batch


def overwrite(target: list[dict], batch: list[dict], key: str) -> list[dict]:
    return list(batch)


def merge(target: list[dict], batch: list[dict], key: str) -> list[dict]:
    by_key = {row[key]: row for row in target}
    by_key.update({row[key]: row for row in batch})                 # upsert
    return list(by_key.values())


STRATEGIES: dict[str, LoadStrategy] = {"append": append, "overwrite": overwrite, "merge": merge}

existing = [{"id": 1, "v": "old"}, {"id": 2, "v": "old"}]
incoming = [{"id": 2, "v": "new"}, {"id": 3, "v": "new"}]
for mode in ("append", "overwrite", "merge"):
    result = STRATEGIES[mode](existing, incoming, "id")
    print(mode, [(row["id"], row["v"]) for row in result])
```

**Output:**

```text
append [(1, 'old'), (2, 'old'), (2, 'new'), (3, 'new')]
overwrite [(2, 'new'), (3, 'new')]
merge [(1, 'old'), (2, 'new'), (3, 'new')]
```

**Factory vs Strategy:** a factory **creates** objects; a strategy **is** the swappable behaviour. They are often used together (a factory returns a strategy chosen from config).

---

### 19.3 Singleton and Its Limitations

**Problem:** exactly one shared instance (configuration, a connection pool, a metrics client).

**Pythonic approach:** a **module-level object**. Modules are imported once per process ([10.2](#102-how-import-works)), so a module attribute is already a singleton. `functools.cache` on a factory function gives lazy creation.

```python
from functools import cache


class Settings:
    def __init__(self) -> None:
        print("loading settings once")
        self.batch_size = 500


@cache
def get_settings() -> Settings:          # lazy singleton: created on the first call
    return Settings()


first, second = get_settings(), get_settings()
print(first is second, first.batch_size)
get_settings.cache_clear()               # tests can reset it
```

**Output:**

```text
loading settings once
True 500
```

**Limitations (an interview favourite):**
- **Hidden global state** makes dependencies invisible and tests order-dependent.
- Hard to **substitute in tests** (you need resets or patching).
- **Not shared across processes**: every multiprocessing worker or Spark executor has its own copy.
- Thread-safety of lazy initialisation must be considered.
- Prefer **creating the object once in `main()` and injecting it** (19.7). Keep singletons for truly global, stateless or read-only things (loggers, immutable config).

---

### 19.4 Builder

**Problem:** construct a complex object (a SQL query, a Spark job configuration, an API request) step by step with readable, validated, optional parts.

```python
from dataclasses import dataclass, field


@dataclass
class SelectQuery:
    table: str
    columns: list[str] = field(default_factory=lambda: ["*"])
    filters: list[str] = field(default_factory=list)
    params: list[object] = field(default_factory=list)
    order_by: str | None = None
    limit: int | None = None


class QueryBuilder:
    """Builds parameterised SELECT statements; identifiers must come from an allowlist."""

    ALLOWED_TABLES = {"orders", "customers"}

    def __init__(self, table: str) -> None:
        if table not in self.ALLOWED_TABLES:
            raise ValueError(f"table not allowed: {table}")
        self._query = SelectQuery(table)

    def select(self, *columns: str) -> "QueryBuilder":
        self._query.columns = list(columns)
        return self

    def where(self, condition: str, value: object) -> "QueryBuilder":
        self._query.filters.append(condition)
        self._query.params.append(value)
        return self

    def order(self, column: str) -> "QueryBuilder":
        self._query.order_by = column
        return self

    def take(self, limit: int) -> "QueryBuilder":
        self._query.limit = limit
        return self

    def build(self) -> tuple[str, list[object]]:
        q = self._query
        sql = f"SELECT {', '.join(q.columns)} FROM {q.table}"
        if q.filters:
            sql += " WHERE " + " AND ".join(q.filters)
        if q.order_by:
            sql += f" ORDER BY {q.order_by}"
        if q.limit is not None:
            sql += " LIMIT ?"
            q.params.append(q.limit)
        return sql, q.params


sql, params = (QueryBuilder("orders").select("id", "amount")
               .where("updated_at > ?", "2026-10-29").where("status = ?", "paid")
               .order("updated_at").take(1000).build())
print(sql)
print(params)
```

**Output:**

```text
SELECT id, amount FROM orders WHERE updated_at > ? AND status = ? ORDER BY updated_at LIMIT ?
['2026-10-29', 'paid', 1000]
```

**Useful when:** objects have many optional parts or must be validated as a whole. In Python, **keyword arguments with defaults and dataclasses** often replace builders. Use a builder only when step-by-step construction really improves readability. (Real projects usually use SQLAlchemy Core rather than a hand-written query builder.)

---

### 19.5 Adapter

**Problem:** make an existing class with an incompatible interface (a vendor SDK, a legacy client) fit the interface your pipeline expects.

```python
from typing import Protocol


class RecordSource(Protocol):
    def read_records(self) -> list[dict]: ...


class LegacyCrmClient:                        # third-party code you cannot change
    def fetch(self, page_size: int) -> list[tuple[int, str]]:
        return [(1, "Asha"), (2, "Ben")]


class CrmSourceAdapter:
    """Adapts LegacyCrmClient to the RecordSource interface."""

    def __init__(self, client: LegacyCrmClient, page_size: int = 500) -> None:
        self._client, self._page_size = client, page_size

    def read_records(self) -> list[dict]:
        return [{"customer_id": cid, "name": name} for cid, name in self._client.fetch(self._page_size)]


def ingest(source: RecordSource) -> int:
    return len(source.read_records())


adapter = CrmSourceAdapter(LegacyCrmClient())
print(adapter.read_records(), ingest(adapter))
```

**Output:**

```text
[{'customer_id': 1, 'name': 'Asha'}, {'customer_id': 2, 'name': 'Ben'}] 2
```

**Useful when:** integrating many external systems behind one internal interface (sources, sinks, notifiers). It also isolates vendor changes to one class.

---

### 19.6 Template Method

**Problem:** many jobs share the **same skeleton** (extract → validate → transform → load → audit) but differ in specific steps.

```python
from abc import ABC, abstractmethod


class BatchJob(ABC):
    """Template method: run() fixes the order of steps; subclasses fill in the details."""

    def run(self) -> dict:
        raw = self.extract()
        valid = [row for row in raw if self.is_valid(row)]
        transformed = [self.transform(row) for row in valid]
        written = self.load(transformed)
        return {"job": type(self).__name__, "read": len(raw), "rejected": len(raw) - len(valid), "written": written}

    @abstractmethod
    def extract(self) -> list[dict]: ...

    def is_valid(self, row: dict) -> bool:            # hook with a sensible default
        return True

    def transform(self, row: dict) -> dict:            # hook with a default
        return row

    @abstractmethod
    def load(self, rows: list[dict]) -> int: ...


class OrdersJob(BatchJob):
    def extract(self) -> list[dict]:
        return [{"id": 1, "amount": "5"}, {"id": 2, "amount": ""}, {"id": 3, "amount": "7.5"}]

    def is_valid(self, row: dict) -> bool:
        return row["amount"] != ""

    def transform(self, row: dict) -> dict:
        return {**row, "amount": float(row["amount"])}

    def load(self, rows: list[dict]) -> int:
        return len(rows)


print(OrdersJob().run())
```

**Output:**

```text
{'job': 'OrdersJob', 'read': 3, 'rejected': 1, 'written': 2}
```

**Trade-off:** template methods use inheritance, so the hierarchy can become rigid. The composition-based pipeline in [7.17](#717-data-engineering-oop-design-example) is often more flexible. Use templates for a small, stable skeleton.

---

### 19.7 Dependency Injection

**Problem:** classes that create their own dependencies (`self.db = PostgresClient(...)` inside `__init__`) are hard to test and reconfigure.

**Solution:** pass dependencies **in** (constructor or function arguments). Wire the concrete objects together in one place, the **composition root**, usually `main()`. No framework is needed in Python.

```python
from datetime import date
from typing import Callable, Protocol


class Storage(Protocol):
    def write(self, path: str, rows: list[dict]) -> None: ...


class InMemoryStorage:
    def __init__(self) -> None:
        self.files: dict[str, list[dict]] = {}

    def write(self, path: str, rows: list[dict]) -> None:
        self.files[path] = rows


class DailyExport:
    def __init__(self, storage: Storage, today: Callable[[], date]) -> None:   # injected dependencies
        self.storage, self.today = storage, today

    def run(self, rows: list[dict]) -> str:
        path = f"exports/dt={self.today():%Y-%m-%d}/data.json"
        self.storage.write(path, rows)
        return path


storage = InMemoryStorage()                                   # in production: S3Storage(boto3_client)
job = DailyExport(storage, today=lambda: date(2026, 10, 29))  # in production: date.today
print(job.run([{"id": 1}]), list(storage.files))
```

**Output:**

```text
exports/dt=2026-10-29/data.json ['exports/dt=2026-10-29/data.json']
```

**Benefits:** trivial testing (inject fakes and a fixed clock), environment-specific wiring, and explicit dependencies.

---

### 19.8 Repository Pattern

**Problem:** SQL and storage details leak into business logic, making it hard to test or to switch storage.

**Solution:** a **repository** class exposes domain-level operations (`get_watermark`, `save_batch`, `find_by_id`) and hides how the data is stored.

```python
import sqlite3
from contextlib import closing
from typing import Protocol


class WatermarkRepository(Protocol):
    def get(self, pipeline: str) -> str | None: ...
    def set(self, pipeline: str, value: str) -> None: ...


class SqliteWatermarkRepository:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn
        conn.execute("CREATE TABLE IF NOT EXISTS watermarks (pipeline TEXT PRIMARY KEY, value TEXT NOT NULL)")

    def get(self, pipeline: str) -> str | None:
        row = self.conn.execute("SELECT value FROM watermarks WHERE pipeline = ?", (pipeline,)).fetchone()
        return row[0] if row else None

    def set(self, pipeline: str, value: str) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO watermarks (pipeline, value) VALUES (?, ?) "
                "ON CONFLICT(pipeline) DO UPDATE SET value = excluded.value", (pipeline, value))


class InMemoryWatermarkRepository:                    # a fake for unit tests
    def __init__(self) -> None:
        self.values: dict[str, str] = {}

    def get(self, pipeline: str) -> str | None:
        return self.values.get(pipeline)

    def set(self, pipeline: str, value: str) -> None:
        self.values[pipeline] = value


def advance(repository: WatermarkRepository, pipeline: str, new_value: str) -> str:
    current = repository.get(pipeline)
    if current is not None and new_value < current:
        raise ValueError("watermark cannot move backwards")
    repository.set(pipeline, new_value)
    return new_value


with closing(sqlite3.connect(":memory:")) as conn:
    for repository in (SqliteWatermarkRepository(conn), InMemoryWatermarkRepository()):
        advance(repository, "orders", "2026-10-29T10:00")
        advance(repository, "orders", "2026-10-29T11:00")
        print(type(repository).__name__, repository.get("orders"))
```

**Output:**

```text
SqliteWatermarkRepository 2026-10-29T11:00
InMemoryWatermarkRepository 2026-10-29T11:00
```

---

### 19.9 Pipeline Pattern

**Problem:** compose many small processing steps into a readable, reorderable, testable flow.

**Solution:** each stage is a function `Iterable[record] -> Iterable[record]` (often a generator), and the pipeline chains them. It is lazy, constant-memory and easy to test stage by stage ([6.10](#610-generator-based-data-pipelines)).

```python
from functools import reduce
from typing import Callable, Iterable, Iterator

Stage = Callable[[Iterable[dict]], Iterator[dict]]


def compose(*stages: Stage) -> Stage:
    return lambda records: reduce(lambda stream, stage: stage(stream), stages, records)


def drop_test_accounts(records):
    return (r for r in records if not r["email"].endswith("@test.com"))


def normalize_email(records):
    return ({**r, "email": r["email"].strip().lower()} for r in records)


def add_domain(records):
    return ({**r, "domain": r["email"].split("@")[1]} for r in records)


pipeline = compose(normalize_email, drop_test_accounts, add_domain)
source = [{"id": 1, "email": " Ana@Corp.com "}, {"id": 2, "email": "qa@TEST.com"}, {"id": 3, "email": "bo@shop.io"}]
print(list(pipeline(source)))
```

**Output:**

```text
[{'id': 1, 'email': 'ana@corp.com', 'domain': 'corp.com'}, {'id': 3, 'email': 'bo@shop.io', 'domain': 'shop.io'}]
```

Note that the order of stages matters: `normalize_email` runs first, so the uppercase test address is caught.

---

### 19.10 When Patterns Become Overengineering

| Smell | Simpler alternative |
|---|---|
| An abstract base class with one implementation and no tests needing a fake | a plain class or function |
| A factory for a choice that never changes | direct construction |
| A Strategy *class* hierarchy for stateless behaviour | a dict of functions |
| A Singleton class with `__new__` tricks | a module-level object or `functools.cache` |
| A Builder for an object with three fields | a dataclass with keyword arguments |
| Five layers of indirection for a 200-line script | a few well-named functions |
| A "framework" written before the second use case exists | wait for the duplication, then refactor (the rule of three) |

**Interview framing:** "I introduce a pattern when it solves a concrete problem I have *now*: multiple implementations selected by config, a dependency I need to fake in tests, or a repeated job skeleton. Otherwise I keep the code simple, because simplicity is easier to operate at 3 AM."

---

### Chapter 19 Review

**Key takeaways**
- Factory: build from config. Strategy: swap behaviour (often just functions). Adapter: fit external interfaces.
- Template Method: a shared skeleton with overridable steps. Repository: hide storage. Pipeline: compose stages.
- Dependency injection is the most valuable pattern for testable pipelines.
- Singletons hide state; prefer module objects or injection.
- Patterns should remove complexity, not add it.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How do you implement a singleton in Python? | A module-level instance or `functools.cache` on a factory; discuss the drawbacks. |
| Strategy vs Template Method? | Composition (swap a function or object) vs inheritance (override steps). |
| Why dependency injection? | Testability, explicit dependencies, environment-specific wiring. |
| What does a repository give you? | Business logic independent of storage details; easy fakes. |
| Give a factory example in data engineering. | `create_reader(config["format"])` returning CSV/Parquet/API readers. |

**Common traps:** pattern-first design; singletons holding connections across forked processes; deep template hierarchies.

**Practice exercise:** Design a `Notifier` interface with `SlackNotifier`, `EmailNotifier` and `ConsoleNotifier` implementations, a factory that builds one from config, and a `JobRunner` that receives a notifier by injection and calls it on failure. Write one unit test using a fake notifier.

---

## 20. Interview Coding Problems

Each problem follows the same structure: **problem → sample → expected output → approach → solution → output → optimised or alternative approaches → complexity → edge cases → common mistakes → follow-up questions**. Difficulty labels: **[Easy]**, **[Medium]**, **[Advanced]**.

**How to answer in an interview:** (1) restate the problem and ask about the input size, duplicates, NULLs and ordering; (2) give a brute-force idea and its complexity; (3) improve it (usually with a dict, set, heap or two pointers); (4) code it cleanly; (5) test it with the sample and with edge cases; (6) state time and space complexity.

**Problem index**

| # | Problem | Topic | Level |
|---|---|---|---|
| 1 | [Reverse a string](#problem-1-reverse-a-string-without-reverse-easy) | strings | Easy |
| 2 | [Palindrome check](#problem-2-check-whether-a-string-is-a-palindrome-easy) | strings, two pointers | Easy |
| 3 | [First non-repeating character](#problem-3-find-the-first-non-repeating-character-easy) | strings, Counter | Easy |
| 4 | [Character and word frequencies](#problem-4-count-character-and-word-frequencies-easy) | Counter, regex | Easy |
| 5 | [Group anagrams](#problem-5-group-anagrams-medium) | dict, hashing | Medium |
| 6 | [Remove duplicates, keep order](#problem-6-remove-duplicates-while-preserving-order-easy) | lists, sets | Easy |
| 7 | [Duplicates and frequencies](#problem-7-find-duplicate-elements-and-their-frequencies-easy) | Counter | Easy |
| 8 | [Second-largest value](#problem-8-find-the-second-largest-value-easy) | lists | Easy |
| 9 | [Missing numbers](#problem-9-find-missing-numbers-easy) | lists, sets | Easy |
| 10 | [Flatten a nested list](#problem-10-flatten-a-nested-list-medium) | recursion, generators | Medium |
| 11 | [Two sum](#problem-11-two-sum-easy) | dict | Easy |
| 12 | [Merge overlapping intervals](#problem-12-merge-overlapping-intervals-medium) | sorting | Medium |
| 13 | [Merge dictionaries](#problem-13-merge-dictionaries-easy--medium) | dict, recursion | Easy–Medium |
| 14 | [Invert a dictionary](#problem-14-invert-a-dictionary-with-non-unique-values-easy) | defaultdict | Easy |
| 15 | [Sort dicts by multiple fields](#problem-15-sort-a-list-of-dictionaries-by-multiple-fields-medium) | sorting | Medium |
| 16 | [Top-N by frequency](#problem-16-find-the-top-n-items-by-frequency-medium) | heapq, Counter | Medium |
| 17 | [Binary search](#problem-17-binary-search-and-first-occurrence-easy--medium) | searching | Easy–Medium |
| 18 | [Depth of nested JSON](#problem-18-maximum-depth-of-nested-json-medium) | recursion | Medium |
| 19 | [Task dependency order](#problem-19-order-pipeline-tasks-by-their-dependencies-topological-sort-advanced) | recursion, graphs | Advanced |
| 20 | [Group records by key](#problem-20-group-records-by-a-key-easy) | grouping | Easy |
| 21 | [Aggregate without pandas](#problem-21-aggregate-data-without-pandas-medium) | aggregation, NULLs | Medium |
| 22 | [Hash join](#problem-22-join-two-datasets-hash-join-medium) | joins | Medium |
| 23 | [Latest record per key](#problem-23-deduplicate-cdc-records-keeping-the-latest-per-key-medium) | deduplication, CDC | Medium |
| 24 | [Top-N per group](#problem-24-top-n-records-per-group-medium) | heapq | Medium |
| 25 | [Validate CSV, write rejects](#problem-25-read-a-csv-validate-rows-transform-data-and-write-rejected-records-separately-medium) | ETL, CSV | Medium |
| 26 | [Process a very large file](#problem-26-process-a-very-large-file-without-loading-it-into-memory-medium) | streaming | Medium |
| 27 | [Compare two files](#problem-27-compare-two-files-and-identify-missing-records-medium) | sets, merge | Medium |
| 28 | [CSV rows to nested JSON](#problem-28-transform-flat-csv-rows-into-nested-json-medium) | transformation | Medium |
| 29 | [Flatten nested JSON](#problem-29-flatten-nested-json-medium) | recursion, JSON | Medium |
| 30 | [Log-file analysis](#problem-30-log-file-analysis--errors-per-hour-and-top-error-messages-medium) | regex, Counter | Medium |
| 31 | [Sessionize events](#problem-31-sessionize-user-events-30-minute-inactivity-gap-advanced) | dates | Advanced |
| 32 | [Missing dates in partitions](#problem-32-find-missing-dates-in-daily-partitions-medium) | dates | Medium |
| 33 | [Generator batch reader](#problem-33-build-a-generator-based-batch-reader-medium) | generators | Medium |
| 34 | [Retry with backoff](#problem-34-implement-retry-with-exponential-backoff-medium) | decorators | Medium |
| 35 | [Timing/logging decorator](#problem-35-implement-a-timing-and-logging-decorator-easy) | decorators | Easy |
| 36 | [API pagination](#problem-36-handle-api-pagination-offsetlimit-medium) | APIs | Medium |
| 37 | [Batch database loading](#problem-37-load-database-records-in-configurable-batches-medium) | databases | Medium |
| 38 | [Incremental extraction](#problem-38-implement-an-incremental-extraction-using-a-watermark-advanced) | watermarks | Advanced |
| 39 | [Reconcile counts](#problem-39-reconcile-source-and-target-record-counts-per-partition-medium) | reconciliation | Medium |
| 40 | [Moving average](#problem-40-moving-average-over-a-stream-medium) | deque | Medium |
| 41 | [Missing values](#problem-41-handle-missing-values-in-records-medium) | data quality | Medium |
| 42 | [Duplicates in a huge file](#problem-42-find-duplicate-keys-in-a-file-larger-than-memory-advanced) | memory, partitioning | Advanced |
| 43 | [LRU cache](#problem-43-implement-an-lru-cache-medium) | design | Medium |
| 44 | [TTL cache](#problem-44-implement-a-cache-with-time-to-live-ttl-medium) | design | Medium |
| 45 | [Balanced parentheses](#problem-45-validate-balanced-parentheses-easy) | stack | Easy |
| 46 | [Merge two sorted lists](#problem-46-merge-two-sorted-lists-easy) | two pointers | Easy |
| 47 | [Bubble, merge and quick sort](#problem-47-implement-bubble-sort-merge-sort-and-quick-sort-medium) | sorting algorithms | Medium |
| 48 | [Candy-wrapper puzzle](#problem-48-candy-wrapper-exchange-puzzle-easy) | simulation | Easy |

### 20.1 String Problems

#### Problem 1: Reverse a String Without `reverse()` [Easy]

- **Problem:** Return the characters of a string in reverse order without using `reversed()` or `list.reverse()`.
- **Sample input:** `"pipeline"`
- **Expected output:** `"enilepip"`

**Approach:**
1. Pythonic: slicing with a step of -1 (`text[::-1]`).
2. Manual: walk the indexes from the end to the start, collect the characters in a list, and `join` once at the end.
3. In-place style: convert to a list and swap characters from both ends moving inward (two pointers).

```python
def reverse_slice(text: str) -> str:
    return text[::-1]


def reverse_loop(text: str) -> str:
    characters = []
    for index in range(len(text) - 1, -1, -1):
        characters.append(text[index])
    return "".join(characters)


def reverse_two_pointers(text: str) -> str:
    characters = list(text)
    left, right = 0, len(characters) - 1
    while left < right:
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1
    return "".join(characters)


print(reverse_slice("pipeline"), reverse_loop("pipeline"), reverse_two_pointers("pipeline"), repr(reverse_loop("")))
print(" ".join("data engineering is fun".split()[::-1]))     # follow-up: reverse the word order
```

**Output:**

```text
enilepip enilepip enilepip ''
fun is engineering data
```

**Complexity:** O(n) time and O(n) space for all three (strings are immutable, so a new string is always created).

**Edge cases:** empty string; a single character; Unicode such as emoji with modifiers or combining accents, where reversing code points can break visual characters (grapheme clusters).

**Common mistakes:** `result = char + result` inside a loop (can be O(n²)); off-by-one errors in `range(len(text) - 1, -1, -1)`.

**Follow-up questions:** reverse each word but keep the word order? (`" ".join(word[::-1] for word in text.split())`); reverse in place? (Strings are immutable, so you need a list or `bytearray`.)

---

#### Problem 2: Check Whether a String Is a Palindrome [Easy]

- **Problem:** Return `True` if the string reads the same forwards and backwards, ignoring case and non-alphanumeric characters.
- **Sample input:** `"A man, a plan, a canal: Panama"`, `"race a car"`
- **Expected output:** `True`, `False`

**Approach (O(1) extra space):** two pointers start at both ends. Skip non-alphanumeric characters, compare the lowercase characters, and move inward.

```python
def is_palindrome(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        if not text[left].isalnum():
            left += 1
        elif not text[right].isalnum():
            right -= 1
        elif text[left].lower() != text[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


def is_palindrome_simple(text: str) -> bool:
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


samples = ["A man, a plan, a canal: Panama", "race a car", "", "!!"]
print([is_palindrome(s) for s in samples], [is_palindrome_simple(s) for s in samples])
```

**Output:**

```text
[True, False, True, True] [True, False, True, True]
```

**Complexity:** two pointers: O(n) time, O(1) space. Simple version: O(n) time, O(n) space.

**Edge cases:** an empty string or punctuation only (a palindrome by convention); mixed case; Unicode case folding (`"ß".casefold() == "ss"`, so use `casefold()` for international text).

**Common mistakes:** forgetting to skip punctuation on **both** sides; comparing without normalising case.

**Follow-up questions:** can the string become a palindrome by removing at most one character? (Two pointers; on the first mismatch, test both skip options.) What about the longest palindromic substring? (Expand around each centre: O(n²).)

---

#### Problem 3: Find the First Non-Repeating Character [Easy]

- **Problem:** Return the first character that appears exactly once, or `None`.
- **Sample input:** `"swiss"`, `"aabb"`
- **Expected output:** `"w"`, `None`

**Approach:**
1. Count every character (`Counter`): one pass.
2. Scan the string again in order and return the first character with count 1.

```python
from collections import Counter


def first_non_repeating(text: str) -> str | None:
    counts = Counter(text)
    return next((char for char in text if counts[char] == 1), None)


def first_non_repeating_unique_scan(text: str) -> str | None:
    counts: dict[str, int] = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return next((char for char, count in counts.items() if count == 1), None)   # dicts keep order


print(first_non_repeating("swiss"), first_non_repeating("aabb"), first_non_repeating_unique_scan("swiss"))
```

**Output:**

```text
w None w
```

**Optimised alternative:** the second version scans only the **unique** characters in the second pass (O(k) instead of O(n)), using dict insertion order.

**Complexity:** O(n) time; O(k) space, where k is the number of distinct characters.

**Edge cases:** an empty string; all characters repeating; case sensitivity (`"Aa"`); whitespace counted as a character.

**Common mistakes:** a nested loop calling `text.count(char)` for every character (O(n²)); returning the first character of `set(text)` (sets are unordered).

**Follow-up questions:** for a **stream** of characters, return the first unique character so far after each arrival (keep counts plus a `deque` of candidates, popping from the front while the front's count is > 1).

---

#### Problem 4: Count Character and Word Frequencies [Easy]

- **Problem:** Count word frequencies (case-insensitive, ignoring punctuation) and character frequencies (ignoring spaces); return the top 2 of each.
- **Sample input:** `"The cat and the hat. The END"`, `"hello world"`
- **Expected output:** `[('the', 3), ('cat', 1)]`, `[('l', 3), ('o', 2)]`

**Approach:** normalise (lowercase), tokenise with a regex (`\w+` handles punctuation), count with `Counter`, then call `most_common(k)`.

```python
import re
from collections import Counter


def top_words(text: str, k: int) -> list[tuple[str, int]]:
    return Counter(re.findall(r"\w+", text.lower())).most_common(k)


def top_characters(text: str, k: int) -> list[tuple[str, int]]:
    return Counter(char for char in text if not char.isspace()).most_common(k)


print(top_words("The cat and the hat. The END", 2), top_characters("hello world", 2))
```

**Output:**

```text
[('the', 3), ('cat', 1)] [('l', 3), ('o', 2)]
```

**Complexity:** O(n) to count; `most_common(k)` uses a heap, O(m log k) for m distinct items.

**Edge cases:** an empty text; apostrophes (`"don't"` → `don`, `t` with `\w+`; use `[\w']+` if needed); Unicode words; ties (`most_common` orders ties by first appearance).

**Common mistakes:** `text.split()` keeps punctuation attached (`"hat."`); case not normalised; a manual `if key in d` counter that is longer and slower than `Counter`.

**Follow-up questions:** do the same for a 100 GB file (stream it line by line, [Problem 26](#problem-26-process-a-very-large-file-without-loading-it-into-memory-medium)); deterministic tie-breaking (sort by `(-count, word)`); exclude stop words (a set lookup).

---

#### Problem 5: Group Anagrams [Medium]

- **Problem:** Group words that are anagrams of each other.
- **Sample input:** `["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Expected output:** `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`

**Approach:** anagrams share a **canonical signature**, their sorted letters (`"eat"` → `"aet"`). Use the signature as a dict key and collect the words in lists (`defaultdict(list)`).

```python
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        groups["".join(sorted(word))].append(word)
    return list(groups.values())


def group_anagrams_counting(words: list[str]) -> list[list[str]]:
    """O(n*k) for lowercase a-z: a letter-count tuple is the signature."""
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for word in words:
        counts = [0] * 26
        for char in word:
            counts[ord(char) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words), group_anagrams_counting(words) == group_anagrams(words))
```

**Output:**

```text
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] True
```

**Complexity:** sorting signature: O(n · k log k) time; counting signature: O(n · k); O(n · k) space (n words of length k).

**Edge cases:** empty strings (they group together); case differences (normalise first); non-ASCII input (use `Counter` / sorted signatures, not the 26-slot array).

**Common mistakes:** using a list as a dict key (unhashable); comparing every pair of words (O(n² · k)).

**Follow-up questions:** are two strings anagrams? (`Counter(a) == Counter(b)`); find all anagrams of a pattern inside a text (sliding window with counts).

---

### 20.2 List and Tuple Problems

#### Problem 6: Remove Duplicates While Preserving Order [Easy]

- **Problem:** Remove duplicate values, keeping the **first** occurrence and the original order.
- **Sample input:** `[3, 1, 3, 2, 1]`
- **Expected output:** `[3, 1, 2]`

**Approach:** dicts keep insertion order and keys are unique, so `dict.fromkeys(items)` does it in one step. The explicit version uses a `seen` set. For unhashable records, deduplicate on a hashable **key**.

```python
def dedupe(items: list) -> list:
    return list(dict.fromkeys(items))


def dedupe_explicit(items: list) -> list:
    seen, result = set(), []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def dedupe_records(records: list[dict], key: str) -> list[dict]:
    seen, result = set(), []
    for record in records:
        if record[key] not in seen:
            seen.add(record[key])
            result.append(record)
    return result


print(dedupe([3, 1, 3, 2, 1]), dedupe_explicit(["b", "a", "b"]))
print(dedupe_records([{"id": 1, "v": "first"}, {"id": 1, "v": "second"}, {"id": 2, "v": "x"}], "id"))
```

**Output:**

```text
[3, 1, 2] ['b', 'a']
[{'id': 1, 'v': 'first'}, {'id': 2, 'v': 'x'}]
```

**Complexity:** O(n) time, O(n) space.

**Edge cases:** an empty list; unhashable items (dicts or lists: dedupe by key or by `tuple`/JSON); `1`, `1.0` and `True` are equal and hash the same, so they count as duplicates.

**Common mistakes:** `list(set(items))` loses the order; `if item not in result` on a list is O(n²).

**Follow-up questions:** keep the **last** occurrence instead (`list(dict.fromkeys(reversed(items)))[::-1]`, or overwrite in a dict); deduplicate a stream too large for memory ([Problem 42](#problem-42-find-duplicate-keys-in-a-file-larger-than-memory-advanced)).

---

#### Problem 7: Find Duplicate Elements and Their Frequencies [Easy]

- **Problem:** Return each value that appears more than once, with its count.
- **Sample input:** `["a", "b", "a", "c", "b", "a"]`
- **Expected output:** `{'a': 3, 'b': 2}`

```python
from collections import Counter


def duplicate_counts(items: list) -> dict:
    return {value: count for value, count in Counter(items).items() if count > 1}


print(duplicate_counts(["a", "b", "a", "c", "b", "a"]), duplicate_counts([1, 2, 3]))
```

**Output:**

```text
{'a': 3, 'b': 2} {}
```

**Approach:** count once with `Counter`, then filter counts > 1. The result keeps first-appearance order.

**Complexity:** O(n) time, O(k) space for k distinct values.

**Edge cases:** no duplicates (an empty dict); `None` values (they count like any other value); case-insensitive duplicates (normalise first).

**Common mistakes:** `[x for x in items if items.count(x) > 1]` is O(n²) and repeats values.

**Follow-up questions:** return the line numbers of duplicates (`defaultdict(list)` of positions); duplicates of a composite key (use a tuple key); in SQL, `GROUP BY key HAVING COUNT(*) > 1`.

---

#### Problem 8: Find the Second-Largest Value [Easy]

- **Problem:** Return the second-largest **distinct** value, or `None` if it doesn't exist.
- **Sample input:** `[5, 1, 5, 3]`, `[7, 7]`
- **Expected output:** `3`, `None`

**Approach (single pass):** track `largest` and `second`. A new maximum pushes the old maximum down to `second`. A value strictly between the two becomes the new `second`. Skip values equal to `largest`.

```python
def second_largest(values: list[float]) -> float | None:
    largest = second = None
    for value in values:
        if largest is None or value > largest:
            largest, second = value, largest
        elif value != largest and (second is None or value > second):
            second = value
    return second


def second_largest_simple(values: list[float]) -> float | None:
    distinct = sorted(set(values), reverse=True)
    return distinct[1] if len(distinct) > 1 else None


samples = [[5, 1, 5, 3], [7, 7], [], [-2, -5], [1, 2, 3, 4]]
print([second_largest(s) for s in samples], [second_largest_simple(s) for s in samples])
```

**Output:**

```text
[3, None, None, -5, 3] [3, None, None, -5, 3]
```

**Complexity:** single pass: O(n) time, O(1) space. Simple version: O(n log n) time, O(n) space.

**Edge cases:** empty input; all values equal; negative numbers (don't initialise with `0`); `None` values in the data (filter them first).

**Common mistakes:** `sorted(values)[-2]` returns the duplicate maximum (`5` for `[5, 1, 5, 3]`); initialising with `0`, which breaks for all-negative input.

**Follow-up questions:** the k-th largest (`heapq.nlargest(k, set(values))[-1]`, O(n log k)); the second-highest salary per department (group, then apply the same logic; in SQL, `DENSE_RANK()`).

---

#### Problem 9: Find Missing Numbers [Easy]

- **Problem:** (a) A list contains the numbers 1..n with exactly **one** missing; find it. (b) Find **all** missing numbers in a range.
- **Sample input:** (a) `[1, 2, 4, 5]`; (b) `[1, 2, 4, 6]` for the range 1..6
- **Expected output:** (a) `3`; (b) `[3, 5]`

**Approach:** (a) The sum of 1..n is `n(n+1)/2`; the expected total minus the actual total is the missing number. (b) Set difference between the full range and the values present.

```python
def find_single_missing(values: list[int]) -> int:
    n = len(values) + 1
    return n * (n + 1) // 2 - sum(values)


def find_single_missing_xor(values: list[int]) -> int:
    result = 0
    for number in range(1, len(values) + 2):
        result ^= number
    for value in values:
        result ^= value
    return result


def find_all_missing(values: list[int], start: int, end: int) -> list[int]:
    present = set(values)
    return [number for number in range(start, end + 1) if number not in present]


print(find_single_missing([1, 2, 4, 5]), find_single_missing_xor([1, 2, 4, 5]), find_all_missing([1, 2, 4, 6], 1, 6))
```

**Output:**

```text
3 3 [3, 5]
```

**Complexity:** (a) O(n) time, O(1) space; (b) O(n + range) time, O(n) space.

**Edge cases:** the missing number is the first or the last; unsorted input (both methods work); duplicates (the sum method breaks, so use sets); an empty list for (a) (the answer is 1).

**Common mistakes:** sorting first (unnecessary O(n log n)); assuming the input is sorted.

**Follow-up questions:** missing **dates** in daily partitions ([Problem 32](#problem-32-find-missing-dates-in-daily-partitions-medium)); missing IDs in a sequence of 1 billion values (process in chunks with a bitmap, or `generate_series` + anti-join in SQL).

---

#### Problem 10: Flatten a Nested List [Medium]

- **Problem:** Flatten an arbitrarily nested list into a flat list.
- **Sample input:** `[1, [2, [3, [4]]], 5]`
- **Expected output:** `[1, 2, 3, 4, 5]`

**Approach:** recursively: for each item, if it is a list, recurse into it; otherwise yield it. A **generator** (`yield from`) avoids building intermediate lists. For very deep nesting, use an explicit stack to avoid `RecursionError` ([5.14](#514-recursion)).

```python
from itertools import chain
from typing import Iterator


def flatten(nested: list) -> Iterator:
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def flatten_iterative(nested: list) -> list:
    stack, result = [iter(nested)], []
    while stack:
        for item in stack[-1]:
            if isinstance(item, (list, tuple)):
                stack.append(iter(item))
                break
            result.append(item)
        else:
            stack.pop()
    return result


print(list(flatten([1, [2, [3, [4]]], 5])), flatten_iterative([1, [2, [3, [4]]], 5]))
print(list(chain.from_iterable([[1, 2], [3], []])))          # one level only
```

**Output:**

```text
[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
[1, 2, 3]
```

**Complexity:** O(n) time for n total elements; O(d) stack space for nesting depth d (plus the output).

**Edge cases:** empty sublists; strings (they are iterable, so don't treat them as lists or they explode into characters); very deep nesting.

**Common mistakes:** `sum(nested, [])` (O(n²), and only one level); checking `hasattr(item, "__iter__")`, which also matches strings and dicts.

**Follow-up questions:** flatten nested **JSON** with key paths ([Problem 29](#problem-29-flatten-nested-json-medium)); limit the flattening depth (pass a `depth` parameter).

---

#### Problem 11: Two Sum [Easy]

- **Problem:** Return the indexes of two numbers that add up to `target`.
- **Sample input:** `[2, 7, 11, 15]`, `target = 9`
- **Expected output:** `(0, 1)`

**Approach:** while scanning, ask "have I already seen `target - current`?" Store each value's index in a dict. One pass.

```python
def two_sum(values: list[int], target: int) -> tuple[int, int] | None:
    index_of: dict[int, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in index_of:
            return index_of[complement], index
        index_of[value] = index
    return None


print(two_sum([2, 7, 11, 15], 9), two_sum([3, 3], 6), two_sum([1, 2], 10))
```

**Output:**

```text
(0, 1) (0, 1) None
```

**Complexity:** O(n) time, O(n) space (the brute-force double loop is O(n²)).

**Edge cases:** duplicate values (`[3, 3]`); no solution; negative numbers; using the same element twice (avoided by checking before inserting).

**Common mistakes:** inserting before checking, which pairs an element with itself when `target == 2 * value`.

**Follow-up questions:** all unique pairs (a set of sorted tuples, [4.9](#49-representative-looping-problems)); sorted input (two pointers, O(1) space); three-sum (sort, then two pointers: O(n²)).

---

#### Problem 12: Merge Overlapping Intervals [Medium]

- **Problem:** Merge overlapping or touching intervals (for example maintenance windows or user activity periods).
- **Sample input:** `[[8, 10], [1, 3], [2, 6], [9, 12], [15, 18]]`
- **Expected output:** `[[1, 6], [8, 12], [15, 18]]`

**Approach:** sort by start time. For each interval, if it starts before (or exactly when) the last merged interval ends, extend that interval's end; otherwise start a new merged interval.

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


print(merge_intervals([[8, 10], [1, 3], [2, 6], [9, 12], [15, 18]]), merge_intervals([[1, 2], [2, 3]]), merge_intervals([]))
```

**Output:**

```text
[[1, 6], [8, 12], [15, 18]] [[1, 3]] []
```

**Complexity:** O(n log n) time (the sort), O(n) space for the output.

**Edge cases:** touching intervals (`[1,2]` and `[2,3]`: decide whether they merge, here `<=` merges them); one interval containing another (`[1,10]`, `[2,3]`, hence `max`); unsorted input; an empty list.

**Common mistakes:** forgetting to sort; replacing the end without `max` (that shrinks a containing interval); mutating the caller's input lists.

**Follow-up questions:** the total covered time (sum of the merged lengths); insert a new interval into a sorted list; the maximum number of overlapping intervals at any moment (sweep line over the sorted start and end events).

---

### 20.3 Set and Dictionary Problems

#### Problem 13: Merge Dictionaries [Easy → Medium]

- **Problem:** (a) Merge two dicts where the right side wins; (b) merge counters by **summing** values; (c) **deep-merge** nested configuration dictionaries.
- **Sample input:** `defaults = {"db": {"host": "localhost", "port": 5432}, "retries": 3}`, `overrides = {"db": {"host": "prod-db"}, "retries": 5}`
- **Expected output (deep):** `{'db': {'host': 'prod-db', 'port': 5432}, 'retries': 5}`

**Approach:** (a) `a | b` (3.9+) or `{**a, **b}`. (b) Add values key by key, or use `Counter` addition. (c) Recurse when both values are dicts; otherwise the override wins. Return **new** dicts and never mutate the inputs.

```python
import copy
from collections import Counter


def deep_merge(base: dict, override: dict) -> dict:
    merged = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def sum_merge(first: dict[str, int], second: dict[str, int]) -> dict[str, int]:
    totals = dict(first)
    for key, value in second.items():
        totals[key] = totals.get(key, 0) + value
    return totals


defaults = {"db": {"host": "localhost", "port": 5432}, "retries": 3}
overrides = {"db": {"host": "prod-db"}, "retries": 5}
print(defaults | overrides)                          # shallow: the nested 'port' is lost
print(deep_merge(defaults, overrides))
print(sum_merge({"a": 1, "b": 2}, {"b": 3, "c": 4}), dict(Counter(a=1, b=2) + Counter(b=3, c=4)))
print(defaults["db"])                                # inputs unchanged
```

**Output:**

```text
{'db': {'host': 'prod-db'}, 'retries': 5}
{'db': {'host': 'prod-db', 'port': 5432}, 'retries': 5}
{'a': 1, 'b': 5, 'c': 4} {'a': 1, 'b': 5, 'c': 4}
{'host': 'localhost', 'port': 5432}
```

**Complexity:** shallow: O(n + m); deep: O(total number of nested keys).

**Edge cases:** an override value of `None` (does it mean "unset" or "set to None"? Decide explicitly); lists (replace or concatenate? A policy decision); type conflicts (a dict vs a scalar under the same key).

**Common mistakes:** a shallow merge of nested config (silently losing keys); mutating the defaults that are shared by all jobs; `Counter` addition drops zero and negative results.

**Follow-up questions:** merge N config layers (`functools.reduce(deep_merge, layers)`, or `ChainMap` for flat lookups); report which keys were overridden (useful for config auditing).

---

#### Problem 14: Invert a Dictionary with Non-Unique Values [Easy]

- **Problem:** Swap keys and values; several keys may share a value.
- **Sample input:** `{"a": 1, "b": 2, "c": 1}`
- **Expected output:** `{1: ['a', 'c'], 2: ['b']}`

```python
from collections import defaultdict


def invert(mapping: dict) -> dict:
    inverted: dict = defaultdict(list)
    for key, value in mapping.items():
        inverted[value].append(key)
    return dict(inverted)


print(invert({"a": 1, "b": 2, "c": 1}), {v: k for k, v in {"a": 1, "b": 2}.items()})
```

**Output:**

```text
{1: ['a', 'c'], 2: ['b']} {1: 'a', 2: 'b'}
```

**Approach:** group the keys under each value with `defaultdict(list)`. A plain dict comprehension is only correct if the values are unique; otherwise later keys silently overwrite earlier ones.

**Complexity:** O(n) time and space.

**Edge cases:** unhashable values (lists can't become keys, so convert to tuples); an empty dict.

**Common mistakes:** `{v: k for k, v in d.items()}` with duplicate values (data loss without an error).

**Follow-up questions:** build a reverse lookup from country code to customers for a join; detect values mapped by more than one key (a data-quality check on a mapping table).

---

### 20.4 Sorting and Searching Problems

#### Problem 15: Sort a List of Dictionaries by Multiple Fields [Medium]

- **Problem:** Sort employees by `dept` ascending, then `salary` descending (missing salaries last), then `name` ascending.
- **Sample input:** five employee records (below)
- **Expected output:** `['Ed', 'Al', 'Bo', 'Cy', 'Di']`

**Approach:** use a tuple sort key. Negate numbers for descending order. Put `salary is None` in the key so missing values sort last (`False` < `True`).

```python
from operator import itemgetter

employees = [
    {"name": "Cy", "dept": "IT", "salary": 90},
    {"name": "Al", "dept": "HR", "salary": 60},
    {"name": "Bo", "dept": "IT", "salary": 90},
    {"name": "Di", "dept": "IT", "salary": None},
    {"name": "Ed", "dept": "HR", "salary": 75},
]


def sort_key(employee: dict) -> tuple:
    salary = employee["salary"]
    return (employee["dept"], salary is None, -(salary or 0), employee["name"])


print([e["name"] for e in sorted(employees, key=sort_key)])

# Alternative for keys that cannot be negated (e.g. strings descending): stable multi-pass sort,
# from the LEAST significant key to the most significant one.
by_name = sorted(employees, key=itemgetter("name"))
by_salary = sorted(by_name, key=lambda e: (e["salary"] is None, -(e["salary"] or 0)))
by_dept = sorted(by_salary, key=itemgetter("dept"))
print([e["name"] for e in by_dept])
```

**Output:**

```text
['Ed', 'Al', 'Bo', 'Cy', 'Di']
['Ed', 'Al', 'Bo', 'Cy', 'Di']
```

**Complexity:** O(n log n) time, O(n) space for the new list.

**Edge cases:** `None` values (comparing `None` with `int` raises `TypeError`); mixed-case strings (`str.lower` or `casefold` in the key); ties (they keep their input order, because Timsort is stable).

**Common mistakes:** sorting by the primary key first in a multi-pass sort (reverse the order of passes); `reverse=True` for the whole sort when only one field should be descending.

**Follow-up questions:** sort 50 GB of records (an external merge sort: sort chunks, write sorted runs, merge with `heapq.merge`); the SQL equivalent (`ORDER BY dept, salary DESC NULLS LAST, name`).

---

#### Problem 16: Find the Top-N Items by Frequency [Medium]

- **Problem:** Return the `k` most frequent items, breaking ties alphabetically.
- **Sample input:** `"b a c b a b d c".split()`, `k = 2`
- **Expected output:** `[('b', 3), ('a', 2)]`

**Approach:** count with `Counter`, then select the top k with a heap (`heapq.nsmallest` with the key `(-count, item)` gives highest count first and alphabetical ties). That is O(m log k) instead of sorting all m distinct items.

```python
import heapq
from collections import Counter


def top_k_frequent(items: list[str], k: int) -> list[tuple[str, int]]:
    counts = Counter(items)
    return heapq.nsmallest(k, counts.items(), key=lambda pair: (-pair[1], pair[0]))


words = "b a c b a b d c".split()
print(top_k_frequent(words, 2), Counter(words).most_common(2))
print(heapq.nlargest(3, [5, 1, 9, 7, 3])[-1])             # follow-up: 3rd largest value
```

**Output:**

```text
[('b', 3), ('a', 2)] [('b', 3), ('a', 2)]
5
```

**Complexity:** counting O(n); selection O(m log k); space O(m).

**Edge cases:** `k` larger than the number of distinct items (returns all of them); `k = 0`; ties at the boundary (define the rule explicitly).

**Common mistakes:** sorting the whole counter when k is small; non-deterministic tie handling in reports.

**Follow-up questions:** top-k over a stream that doesn't fit in memory (approximate: Count-Min Sketch + a heap; exact: hash-partition by item, count per partition, merge the per-partition top-k); top-k per group ([Problem 24](#problem-24-top-n-records-per-group-medium)).

---

#### Problem 17: Binary Search (and First Occurrence) [Easy → Medium]

- **Problem:** In a **sorted** list, find the index of the **first** occurrence of the target, or -1.
- **Sample input:** `[1, 3, 3, 3, 5, 8]`, `target = 3`
- **Expected output:** `1`

**Approach:** keep `[low, high]` bounds. When `values[mid] >= target`, the answer is at `mid` or to its left, so move `high`. Otherwise move `low`. Finally check that `values[low] == target`.

```python
from bisect import bisect_left, bisect_right


def first_occurrence(values: list[int], target: int) -> int:
    low, high = 0, len(values)                # search in [low, high)
    while low < high:
        mid = (low + high) // 2
        if values[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low if low < len(values) and values[low] == target else -1


data = [1, 3, 3, 3, 5, 8]
print(first_occurrence(data, 3), first_occurrence(data, 4), first_occurrence([], 1))
print(bisect_left(data, 3), bisect_right(data, 3) - bisect_left(data, 3))   # index and count of 3s
```

**Output:**

```text
1 -1 -1
1 3
```

**Complexity:** O(log n) time, O(1) space.

**Edge cases:** an empty list; the target smaller or larger than all values; all elements equal; unsorted input (binary search gives wrong answers, so it must be sorted).

**Common mistakes:** infinite loops from wrong bound updates (`high = mid - 1` with half-open intervals); returning any match instead of the first.

**Follow-up questions:** find a timestamp in a sorted log file (binary search over byte offsets); find the partition containing a given date; search a rotated sorted array.

---

### 20.5 Recursion Problems

#### Problem 18: Maximum Depth of Nested JSON [Medium]

- **Problem:** Return the nesting depth of a JSON-like structure (scalars have depth 0; each dict or list level adds 1).
- **Sample input:** `{"a": {"b": {"c": 1}}, "d": [1, {"e": 2}]}`
- **Expected output:** `3`

**Approach:** recursion. The depth of a container is 1 + the maximum depth of its children (0 for an empty container's children); the depth of a scalar is 0.

```python
def json_depth(value: object) -> int:
    if isinstance(value, dict):
        return 1 + max((json_depth(child) for child in value.values()), default=0)
    if isinstance(value, list):
        return 1 + max((json_depth(child) for child in value), default=0)
    return 0


def json_depth_iterative(value: object) -> int:
    deepest, stack = 0, [(value, 0)]
    while stack:
        current, depth = stack.pop()
        if isinstance(current, (dict, list)):
            children = current.values() if isinstance(current, dict) else current
            deepest = max(deepest, depth + 1)
            stack.extend((child, depth + 1) for child in children)
    return deepest


document = {"a": {"b": {"c": 1}}, "d": [1, {"e": 2}]}
print(json_depth(document), json_depth_iterative(document), json_depth({}), json_depth(42))
```

**Output:**

```text
3 3 1 0
```

**Complexity:** O(n) time for n total nodes; recursion uses O(depth) stack.

**Edge cases:** empty containers; scalars at the top level; very deep documents (use the iterative version).

**Common mistakes:** `max()` of an empty sequence without `default=` (raises `ValueError`); treating strings as containers.

**Follow-up questions:** why measure depth? (To choose a flattening strategy, or to reject payloads deeper than a safety limit.) List all leaf paths ([Problem 29](#problem-29-flatten-nested-json-medium)).

---

#### Problem 19: Order Pipeline Tasks by Their Dependencies (Topological Sort) [Advanced]

- **Problem:** Given task dependencies, return an execution order in which every task runs after its dependencies. Detect cycles. (This is what orchestrators such as Airflow do with a DAG.)
- **Sample input:** `{"load": ["transform"], "transform": ["extract", "validate"], "validate": ["extract"], "extract": []}`
- **Expected output:** `['extract', 'validate', 'transform', 'load']`

**Approach (DFS):** visit each task. Before adding a task, recursively visit its dependencies. Mark tasks as *visiting* while on the current path; meeting a *visiting* task again means there is a **cycle**.

```python
from graphlib import TopologicalSorter


def topological_order(dependencies: dict[str, list[str]]) -> list[str]:
    order: list[str] = []
    state: dict[str, str] = {}

    def visit(task: str, path: list[str]) -> None:
        if state.get(task) == "done":
            return
        if state.get(task) == "visiting":
            raise ValueError("cycle: " + " -> ".join(path + [task]))
        state[task] = "visiting"
        for dependency in dependencies.get(task, []):
            visit(dependency, path + [task])
        state[task] = "done"
        order.append(task)

    for task in dependencies:
        visit(task, [])
    return order


dag = {"load": ["transform"], "transform": ["extract", "validate"], "validate": ["extract"], "extract": []}
print(topological_order(dag))
print(list(TopologicalSorter(dag).static_order()))          # standard library (3.9+)
try:
    topological_order({"a": ["b"], "b": ["a"]})
except ValueError as error:
    print("ValueError:", error)
```

**Output:**

```text
['extract', 'validate', 'transform', 'load']
['extract', 'validate', 'transform', 'load']
ValueError: cycle: a -> b -> a
```

**Complexity:** O(V + E) time (tasks + dependency edges); O(V) space.

**Edge cases:** a dependency that isn't a key in the dict (treated as having no dependencies); disconnected tasks; self-dependency (`{"a": ["a"]}` is a cycle).

**Common mistakes:** no cycle detection (infinite recursion); recursion depth problems for very long chains (use Kahn's algorithm with in-degree counts and a queue).

**Follow-up questions:** which tasks can run **in parallel**? (Kahn's algorithm level by level; `TopologicalSorter.get_ready()`); re-run only the downstream tasks of a failed task (a reverse-graph traversal).

---

### 20.6 Grouping, Joining and Aggregation Problems

#### Problem 20: Group Records by a Key [Easy]

- **Problem:** Group order IDs by region.
- **Sample input:** `[{"region": "EU", "order_id": 1}, {"region": "US", "order_id": 2}, {"region": "EU", "order_id": 3}, {"region": "APAC", "order_id": 4}]`
- **Expected output:** `{'EU': [1, 3], 'US': [2], 'APAC': [4]}`

**Approach:** `defaultdict(list)` creates the list on first access, so one pass is enough. `itertools.groupby` is an alternative for **pre-sorted** (streaming) input.

```python
from collections import defaultdict
from itertools import groupby
from operator import itemgetter

records = [{"region": "EU", "order_id": 1}, {"region": "US", "order_id": 2},
           {"region": "EU", "order_id": 3}, {"region": "APAC", "order_id": 4}]


def group_by(rows: list[dict], key: str, value: str) -> dict:
    groups: dict = defaultdict(list)
    for row in rows:
        groups[row[key]].append(row[value])
    return dict(groups)


print(group_by(records, "region", "order_id"))
ordered = sorted(records, key=itemgetter("region"))                   # groupby needs sorted input
print([(region, [r["order_id"] for r in rows]) for region, rows in groupby(ordered, key=itemgetter("region"))])
```

**Output:**

```text
{'EU': [1, 3], 'US': [2], 'APAC': [4]}
[('APAC', [4]), ('EU', [1, 3]), ('US', [2])]
```

**Complexity:** dict version O(n) time and O(n) space; the `groupby` version O(n log n) because of the sort, but O(1) extra memory per group when the input is already sorted.

**Edge cases:** a missing key in a record (`row.get(key)` groups it under `None`, or reject the record); keys with different cases or whitespace (normalise them).

**Common mistakes:** `groupby` on unsorted data (fragmented groups); `dict.setdefault(key, [])` inside hot loops is fine, but `defaultdict` is clearer.

**Follow-up questions:** group by a composite key (a tuple `(region, day)`); group 100 GB of data (sort externally or use the database / Spark `groupBy`).

---

#### Problem 21: Aggregate Data Without pandas [Medium]

- **Problem:** Per region, compute the row count, NULL count, sum, min, max and average of `amount` (ignoring NULLs for the statistics).
- **Sample input:** six rows, including one with `amount = None`
- **Expected output:** shown below

**Approach:** keep a running **accumulator** per group (count, sum, min, max), updating it in one pass. Compute the average at the end as `sum / non-null count`. This is exactly what SQL `GROUP BY` does internally (hash aggregation).

```python
def aggregate(rows: list[dict], key: str, value: str) -> dict[str, dict]:
    stats: dict[str, dict] = {}
    for row in rows:
        group = stats.setdefault(row[key], {"rows": 0, "nulls": 0, "sum": 0.0, "min": None, "max": None})
        group["rows"] += 1
        raw = row.get(value)
        if raw is None:
            group["nulls"] += 1
            continue
        amount = float(raw)
        group["sum"] += amount
        group["min"] = amount if group["min"] is None else min(group["min"], amount)
        group["max"] = amount if group["max"] is None else max(group["max"], amount)
    for group in stats.values():
        non_null = group["rows"] - group["nulls"]
        group["avg"] = round(group["sum"] / non_null, 2) if non_null else None
    return stats


rows = [{"region": "EU", "amount": 100}, {"region": "US", "amount": 50}, {"region": "EU", "amount": 30},
        {"region": "US", "amount": 70}, {"region": "EU", "amount": 20}, {"region": "EU", "amount": None}]
for region, summary in aggregate(rows, "region", "amount").items():
    print(region, summary)
```

**Output:**

```text
EU {'rows': 4, 'nulls': 1, 'sum': 150.0, 'min': 20.0, 'max': 100.0, 'avg': 50.0}
US {'rows': 2, 'nulls': 0, 'sum': 120.0, 'min': 50.0, 'max': 70.0, 'avg': 60.0}
```

**Complexity:** O(n) time, O(g) space for g groups. It works on a stream of any size.

**Edge cases:** all values NULL in a group (avg `None`, not a division by zero); string amounts (convert them; invalid ones should be rejected, not crash the job); money (use `Decimal`).

**Common mistakes:** averaging over all rows including NULLs (SQL `AVG` ignores NULLs); storing every value per group just to compute the sum (O(n) memory).

**Follow-up questions:** a **median** or distinct count per group in bounded memory (you need all the values, sorting, or approximations such as t-digest / HyperLogLog); merge partial aggregates from several workers (sum the counts and sums; min of mins; recompute the average from the totals, never average the averages).

---

#### Problem 22: Join Two Datasets (Hash Join) [Medium]

- **Problem:** Join orders to customers on `customer_id`: an inner join and a left join.
- **Sample input:** three orders (one with an unknown customer) and two customers
- **Expected output:** inner `[(1, 'Asha'), (2, 'Ben')]`; left `[(1, 'Asha'), (2, 'Ben'), (3, None)]`

**Approach:** **build** a dict from the **smaller** dataset (the key → rows), then **probe** it for each row of the larger dataset. Store a **list** per key, so one-to-many joins are correct.

```python
from collections import defaultdict


def hash_join(left: list[dict], right: list[dict], key: str, how: str = "inner") -> list[dict]:
    lookup: dict = defaultdict(list)
    for row in right:                                   # build side: the smaller dataset
        lookup[row[key]].append(row)
    joined = []
    for row in left:                                    # probe side
        matches = lookup.get(row[key], [])
        if matches:
            joined.extend({**row, **match} for match in matches)
        elif how == "left":
            joined.append({**row, **{column: None for column in (right[0].keys() if right else []) if column != key}})
    return joined


orders = [{"order_id": 1, "customer_id": 10}, {"order_id": 2, "customer_id": 11}, {"order_id": 3, "customer_id": 99}]
customers = [{"customer_id": 10, "name": "Asha"}, {"customer_id": 11, "name": "Ben"}]
print([(r["order_id"], r["name"]) for r in hash_join(orders, customers, "customer_id")])
print([(r["order_id"], r["name"]) for r in hash_join(orders, customers, "customer_id", how="left")])
```

**Output:**

```text
[(1, 'Asha'), (2, 'Ben')]
[(1, 'Asha'), (2, 'Ben'), (3, None)]
```

**Complexity:** O(n + m) time; O(m) space for the build side (a nested-loop join is O(n × m)).

**Edge cases:** duplicate keys on the build side (row multiplication: validate uniqueness when it should be one-to-one); NULL join keys (in SQL, `NULL` never equals `NULL`, so exclude them); column name collisions (`{**row, **match}` lets the right side overwrite the left; prefix the columns if needed).

**Common mistakes:** a dict of single rows (`{c[key]: c}`) silently drops duplicate customers; building from the larger dataset (memory).

**Follow-up questions:** neither dataset fits in memory (a sort-merge join, or hash-partition both sides by key and join partition by partition, which is what Spark does in a shuffle join); a broadcast join in Spark (ship the small table to every executor).

---

#### Problem 23: Deduplicate CDC Records, Keeping the Latest per Key [Medium]

- **Problem:** Change events may contain several versions of each record. Keep only the newest version per `id`.
- **Sample input:** four events for ids 1 and 2 (one of them older and arriving late)
- **Expected output:** `[(1, 'paid'), (2, 'new')]`

**Approach:** one pass with a dict `id → best record so far`; replace it when the incoming record's `updated_at` (with a sequence number as a **tie-breaker**) is greater.

```python
def latest_per_key(records: list[dict], key: str = "id", version: tuple[str, ...] = ("updated_at", "seq")) -> list[dict]:
    latest: dict = {}
    for record in records:
        current = latest.get(record[key])
        record_version = tuple(record.get(field) or 0 for field in version)
        if current is None or record_version > tuple(current.get(field) or 0 for field in version):
            latest[record[key]] = record
    return list(latest.values())


events = [
    {"id": 1, "status": "new", "updated_at": "2026-10-29T09:00", "seq": 1},
    {"id": 2, "status": "new", "updated_at": "2026-10-29T09:30", "seq": 2},
    {"id": 1, "status": "paid", "updated_at": "2026-10-29T10:00", "seq": 3},
    {"id": 1, "status": "stale", "updated_at": "2026-10-29T08:00", "seq": 4},    # arrives late but is older
]
print([(r["id"], r["status"]) for r in latest_per_key(events)])
```

**Output:**

```text
[(1, 'paid'), (2, 'new')]
```

**Complexity:** O(n) time, O(k) space for k distinct keys.

**Edge cases:** equal timestamps (use the tie-breaker); ISO-8601 strings compare correctly only if they share a format and time zone (otherwise parse them to datetimes); missing timestamps; delete events (see [15.5](#155-cdc-fundamentals)).

**Common mistakes:** "last one wins" in arrival order (late events overwrite newer data); sorting the full dataset when one pass is enough.

**Follow-up questions:** the SQL version (`ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC, seq DESC) = 1`, or `QUALIFY` in Snowflake); the pandas version (`sort_values` + `drop_duplicates(keep="last")`, [17.7](#177-duplicates)).

---

#### Problem 24: Top-N Records per Group [Medium]

- **Problem:** Return the top 2 customers by revenue in each region.
- **Sample input:** `[("EU", "a", 100), ("EU", "b", 300), ("EU", "c", 200), ("US", "d", 50), ("US", "e", 80)]`
- **Expected output:** `{'EU': [('b', 300), ('c', 200)], 'US': [('e', 80), ('d', 50)]}`

**Approach:** keep a **min-heap of size N per group**. Push each record; if the heap grows beyond N, pop the smallest. Memory stays at O(groups × N) regardless of the input size, so it works on streams.

```python
import heapq
from collections import defaultdict


def top_n_per_group(rows: list[tuple[str, str, float]], n: int) -> dict[str, list[tuple[str, float]]]:
    heaps: dict[str, list[tuple[float, str]]] = defaultdict(list)
    for group, item, value in rows:
        heap = heaps[group]
        heapq.heappush(heap, (value, item))
        if len(heap) > n:
            heapq.heappop(heap)                           # drop the smallest
    return {group: [(item, value) for value, item in sorted(heap, reverse=True)] for group, heap in heaps.items()}


sales = [("EU", "a", 100), ("EU", "b", 300), ("EU", "c", 200), ("US", "d", 50), ("US", "e", 80)]
print(top_n_per_group(sales, 2))
```

**Output:**

```text
{'EU': [('b', 300), ('c', 200)], 'US': [('e', 80), ('d', 50)]}
```

**Complexity:** O(n log N) time; O(g × N) space.

**Edge cases:** groups with fewer than N items; ties (decide whether to include all tied rows, like SQL `RANK`, or exactly N, like `ROW_NUMBER`); the same customer appearing several times (aggregate first, then rank).

**Common mistakes:** sorting every group completely; using a max-heap and popping N times (fine for small data, but it keeps everything in memory).

**Follow-up questions:** the SQL version (`ROW_NUMBER() OVER (PARTITION BY region ORDER BY revenue DESC) <= 2`); the pandas version ([17.18](#1718-interview-coding-examples)).

---

### 20.7 File, CSV and JSON Problems

#### Problem 25: Read a CSV, Validate Rows, Transform Data and Write Rejected Records Separately [Medium]

- **Problem:** Read `orders.csv`, validate each row (integer `id`, an email containing `@`, a non-negative numeric `amount`, a valid ISO `order_date`), normalise the email to lowercase, write valid rows to `clean.csv`, and write invalid rows to `rejects.csv` with the line number and reason. Return the counts.
- **Sample input:** five data rows (created in the code)
- **Expected output:** `{'read': 5, 'good': 2, 'rejected': 3}`, plus the reasons below

**Approach:**
1. Stream the input with `csv.DictReader` (constant memory).
2. Validate each row in a separate, pure function that returns either a cleaned row or a reason.
3. Write each row to the right output immediately.
4. Reconcile: `read == good + rejected`.

```python
import csv
from datetime import date
from pathlib import Path

Path("orders.csv").write_text(
    "id,email,amount,order_date\n"
    "1,a@x.com,10.5,2026-10-29\n"
    "2,bad-email,5,2026-10-29\n"
    "3,c@y.com,-1,2026-10-29\n"
    "4,d@z.com,7,2026-02-30\n"
    "5, E@X.COM ,0,2026-10-30\n",
    encoding="utf-8",
)


def clean_row(row: dict[str, str]) -> tuple[dict | None, str | None]:
    """Return (clean_row, None) or (None, reason)."""
    try:
        order_id = int(row["id"])
    except (TypeError, ValueError):
        return None, "invalid id"
    email = (row.get("email") or "").strip().lower()
    if "@" not in email:
        return None, "invalid email"
    try:
        amount = float(row["amount"])
    except (TypeError, ValueError):
        return None, "invalid amount"
    if amount < 0:
        return None, "negative amount"
    try:
        order_date = date.fromisoformat(row["order_date"])
    except (TypeError, ValueError) as error:
        return None, f"invalid date: {error}"
    return {"id": order_id, "email": email, "amount": amount, "order_date": order_date.isoformat()}, None


def process(source: Path, clean_path: Path, rejects_path: Path) -> dict[str, int]:
    counts = {"read": 0, "good": 0, "rejected": 0}
    with source.open(newline="", encoding="utf-8") as src, \
         clean_path.open("w", newline="", encoding="utf-8") as good_file, \
         rejects_path.open("w", newline="", encoding="utf-8") as bad_file:
        reader = csv.DictReader(src)
        good = csv.DictWriter(good_file, fieldnames=["id", "email", "amount", "order_date"], lineterminator="\n")
        bad = csv.DictWriter(bad_file, fieldnames=[*reader.fieldnames, "line", "reason"], lineterminator="\n")
        good.writeheader()
        bad.writeheader()
        for line_number, row in enumerate(reader, start=2):
            counts["read"] += 1
            cleaned, reason = clean_row(row)
            if cleaned is None:
                bad.writerow({**row, "line": line_number, "reason": reason})
                counts["rejected"] += 1
            else:
                good.writerow(cleaned)
                counts["good"] += 1
    assert counts["read"] == counts["good"] + counts["rejected"]
    return counts


print(process(Path("orders.csv"), Path("clean.csv"), Path("rejects.csv")))
with open("rejects.csv", newline="", encoding="utf-8") as file:
    print([(row["line"], row["reason"]) for row in csv.DictReader(file)])
print(Path("clean.csv").read_text(encoding="utf-8").splitlines())
```

**Output:**

```text
{'read': 5, 'good': 2, 'rejected': 3}
[('3', 'invalid email'), ('4', 'negative amount'), ('5', 'invalid date: day is out of range for month')]
['id,email,amount,order_date', '1,a@x.com,10.5,2026-10-29', '5,e@x.com,0.0,2026-10-30']
```

**Complexity:** O(n) time; O(1) memory (streaming).

**Edge cases:** an empty file (header only); a missing header; extra or missing columns (`DictReader` gives `None` for missing fields, which `clean_row` handles); a BOM in the header (`utf-8-sig`); an amount of `0` (valid, so don't use truthiness); a reject rate above the threshold (fail the run, [15.22](#1522-error-handling-and-alerting)).

**Common mistakes:** loading the whole file into a list; `if not amount` rejecting zero; losing the original raw values in the reject file; no line numbers; no reconciliation. (In production, raise an exception rather than relying on `assert`, which `python -O` removes.)

**Follow-up questions:** make it idempotent and atomic (write to temp files, then rename, [9.17](#917-safe-and-atomic-file-writing)); parallelise across many files ([13.14](#1314-parallel-file-and-api-processing-examples)); make the validation rules configuration-driven ([15.19](#1519-configuration-driven-pipeline-design)).

---

#### Problem 26: Process a Very Large File Without Loading It into Memory [Medium]

- **Problem:** Find the 3 most common words in a log file that may be far larger than RAM.
- **Sample input:** four log lines (created in the code)
- **Expected output:** `[('error', 3), ('disk', 3), ('full', 2)]`

**Approach:** iterate over the file object (it streams line by line with buffering), tokenise each line, and update one `Counter`. Memory is O(distinct words), not O(file size).

```python
import re
from collections import Counter
from pathlib import Path

WORD = re.compile(r"[a-z]+")

Path("app.log").write_text("error disk full\nwarning disk slow\nerror network down\nerror disk full\n", encoding="utf-8")


def top_words_in_file(path: Path, k: int) -> list[tuple[str, int]]:
    counts: Counter[str] = Counter()
    with path.open(encoding="utf-8", errors="replace") as file:
        for line in file:                                   # one line in memory at a time
            counts.update(WORD.findall(line.lower()))
    return counts.most_common(k)


print(top_words_in_file(Path("app.log"), 3))
```

**Output:**

```text
[('error', 3), ('disk', 3), ('full', 2)]
```

**Complexity:** O(total characters) time; O(V) memory for V distinct words.

**Edge cases:** a single huge line without newlines (read fixed-size blocks instead and handle words split across block boundaries); undecodable bytes (`errors="replace"`, and count them); compressed input (`gzip.open(path, "rt")`).

**Common mistakes:** `file.read()` or `file.readlines()` (loads everything); `pandas.read_csv` without `chunksize`; collecting all the words into a list before counting.

**Follow-up questions:** too many distinct words for memory (hash-partition the words into N temp files, then count each partition; or an approximate Count-Min Sketch); a multi-core speed-up (split the file by byte ranges aligned to newlines and process them with `ProcessPoolExecutor`, then merge the Counters); several files (`itertools.chain` over generators).

---

#### Problem 27: Compare Two Files and Identify Missing Records [Medium]

- **Problem:** Given a source extract and a target extract (both CSV with an `id` column), list the IDs missing from the target and the unexpected IDs in the target.
- **Sample input:** source IDs 1–6; target IDs 1, 2, 4, 6, 7
- **Expected output:** `missing: [3, 5]`, `unexpected: [7]`

**Approach (fits in memory):** load the **keys only** of the smaller file into a set, stream the other file, and use set differences. **Huge sorted files:** a streaming **merge** compare with two pointers uses O(1) memory.

```python
import csv
from pathlib import Path
from typing import Iterator

Path("source.csv").write_text("id\n" + "".join(f"{n}\n" for n in range(1, 7)), encoding="utf-8")
Path("target.csv").write_text("id\n1\n2\n4\n6\n7\n", encoding="utf-8")


def read_ids(path: Path) -> Iterator[int]:
    with path.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            yield int(row["id"])


def compare_with_set(source: Path, target: Path) -> tuple[list[int], list[int]]:
    target_ids = set(read_ids(target))                     # keys only, from the smaller file
    seen_source: set[int] = set()
    missing = []
    for source_id in read_ids(source):
        seen_source.add(source_id)
        if source_id not in target_ids:
            missing.append(source_id)
    return missing, sorted(target_ids - seen_source)


def compare_sorted_streams(source_ids: Iterator[int], target_ids: Iterator[int]) -> tuple[list[int], list[int]]:
    """Both inputs must be sorted ascending. O(1) extra memory beyond the outputs."""
    missing, unexpected = [], []
    sentinel = object()
    left, right = next(source_ids, sentinel), next(target_ids, sentinel)
    while left is not sentinel or right is not sentinel:
        if right is sentinel or (left is not sentinel and left < right):
            missing.append(left)
            left = next(source_ids, sentinel)
        elif left is sentinel or right < left:
            unexpected.append(right)
            right = next(target_ids, sentinel)
        else:
            left, right = next(source_ids, sentinel), next(target_ids, sentinel)
    return missing, unexpected


print(compare_with_set(Path("source.csv"), Path("target.csv")))
print(compare_sorted_streams(read_ids(Path("source.csv")), read_ids(Path("target.csv"))))
```

**Output:**

```text
([3, 5], [7])
([3, 5], [7])
```

**Complexity:** set version: O(n + m) time, O(m + n) memory for the keys. Merge version: O(n + m) time, O(1) extra memory, but the inputs must be sorted (an external sort costs O(n log n)).

**Edge cases:** duplicate keys in a file (report them separately); keys with different formats (`"007"` vs `7`: normalise them); different encodings or delimiters; an empty file.

**Common mistakes:** comparing whole lines (formatting differences produce false mismatches); a nested loop over both files (O(n × m)); loading full rows when only the keys are needed.

**Follow-up questions:** also detect **changed** rows (compare row hashes per key, [15.13](#1513-source-to-target-reconciliation)); billions of keys (hash-partition both files into N buckets by key, then compare bucket by bucket; or do it in SQL with a `FULL OUTER JOIN ... WHERE a.id IS NULL OR b.id IS NULL`).

---

#### Problem 28: Transform Flat CSV Rows into Nested JSON [Medium]

- **Problem:** Convert order-line rows into one JSON document per order, with a list of items.
- **Sample input:** `order_id,customer,sku,qty` rows: (1, Asha, p1, 2), (1, Asha, p2, 1), (2, Ben, p3, 5)
- **Expected output:** shown below

**Approach:** group the rows by `order_id` in a dict (insertion order preserved); the first row of each order creates the header fields, and every row appends an item. Convert types explicitly.

```python
import csv
import io
import json

CSV_TEXT = "order_id,customer,sku,qty\n1,Asha,p1,2\n1,Asha,p2,1\n2,Ben,p3,5\n"


def rows_to_documents(text_stream) -> list[dict]:
    orders: dict[int, dict] = {}
    for row in csv.DictReader(text_stream):
        order_id = int(row["order_id"])
        document = orders.setdefault(order_id, {"order_id": order_id, "customer": row["customer"], "items": []})
        if document["customer"] != row["customer"]:
            raise ValueError(f"order {order_id} has conflicting customers")
        document["items"].append({"sku": row["sku"], "qty": int(row["qty"])})
    return list(orders.values())


print(json.dumps(rows_to_documents(io.StringIO(CSV_TEXT))))
```

**Output:**

```text
[{"order_id": 1, "customer": "Asha", "items": [{"sku": "p1", "qty": 2}, {"sku": "p2", "qty": 1}]}, {"order_id": 2, "customer": "Ben", "items": [{"sku": "p3", "qty": 5}]}]
```

**Complexity:** O(n) time; O(n) memory, because all orders are held until the end. If the input is **sorted by order_id**, stream it with `itertools.groupby` and write each document as soon as its group ends (O(largest order) memory).

**Edge cases:** inconsistent header fields for the same order (raise or log, as above); an order with no items; type conversion errors.

**Common mistakes:** assuming the rows are grouped together when they aren't; duplicating the header fields into every item.

**Follow-up questions:** write JSON Lines instead of one big array (streamable); the reverse transformation (explode nested items into rows, [Problem 29](#problem-29-flatten-nested-json-medium)); the pandas version (`groupby` + `apply(to_dict)`, or `json_normalize` for the reverse).

---

#### Problem 29: Flatten Nested JSON [Medium]

- **Problem:** Flatten nested dicts **and lists** into one level, joining keys with dots and using list indexes. Keep empty containers as `None`, so their keys are not lost.
- **Sample input:** `{"id": 1, "customer": {"name": "A", "address": {"zip": "10001"}}, "tags": ["x", "y"], "items": [{"sku": "p1", "qty": 2}], "notes": {}}`
- **Expected output:** `{'id': 1, 'customer.name': 'A', 'customer.address.zip': '10001', 'tags.0': 'x', 'tags.1': 'y', 'items.0.sku': 'p1', 'items.0.qty': 2, 'notes': None}`

**Approach:** recursive descent carrying the key path. A dict child extends the path with its key, a list child with its index, and a scalar is stored at the current path.

```python
def flatten_json(value: object, parent_key: str = "", sep: str = ".") -> dict:
    flat: dict = {}
    if isinstance(value, dict):
        if not value and parent_key:
            flat[parent_key] = None
        for key, child in value.items():
            flat.update(flatten_json(child, f"{parent_key}{sep}{key}" if parent_key else str(key), sep))
    elif isinstance(value, list):
        if not value and parent_key:
            flat[parent_key] = None
        for index, child in enumerate(value):
            flat.update(flatten_json(child, f"{parent_key}{sep}{index}" if parent_key else str(index), sep))
    else:
        flat[parent_key] = value
    return flat


def unflatten_json(flat: dict, sep: str = ".") -> dict:
    """Reverse operation for dict-only paths (list indexes stay as string keys)."""
    root: dict = {}
    for path, value in flat.items():
        node = root
        *parents, leaf = path.split(sep)
        for part in parents:
            node = node.setdefault(part, {})
        node[leaf] = value
    return root


document = {"id": 1, "customer": {"name": "A", "address": {"zip": "10001"}},
            "tags": ["x", "y"], "items": [{"sku": "p1", "qty": 2}], "notes": {}}
print(flatten_json(document))
print(unflatten_json({"a.b": 1, "a.c": 2, "d": 3}))
```

**Output:**

```text
{'id': 1, 'customer.name': 'A', 'customer.address.zip': '10001', 'tags.0': 'x', 'tags.1': 'y', 'items.0.sku': 'p1', 'items.0.qty': 2, 'notes': None}
{'a': {'b': 1, 'c': 2}, 'd': 3}
```

**Complexity:** O(n) time over all nodes. Repeated `update` calls copy the dicts, so for very large documents pass one accumulator dict down the recursion instead. Recursion depth = nesting depth.

**Edge cases:** keys that already contain the separator (`"a.b"`, which is ambiguous; choose another separator or escape it); key collisions (`{"a.b": 1, "a": {"b": 2}}`); very deep documents (iterative version); `None` values versus missing keys.

**Common mistakes:** ignoring lists (the original guide's version did); exploding big arrays into thousands of columns (instead, move arrays into a **child table** with a foreign key, or keep them as JSON).

**Follow-up questions:** explode `items` into one row per item with the parent ID (normalisation); the pandas equivalent (`pd.json_normalize(records, record_path="items", meta=["id"])`); schema drift when new nested keys appear.

---

### 20.8 Date and Log Problems

#### Problem 30: Log-File Analysis – Errors per Hour and Top Error Messages [Medium]

- **Problem:** From application logs, count ERROR lines per hour, find the most common error message, and count unparseable lines.
- **Sample input:** six lines (below), including one malformed line
- **Expected output:** `{'2026-10-29 10': 2, '2026-10-29 11': 1}`, `[('db timeout', 2)]`, `1`

**Approach:** compile one regex with named groups; stream the lines; for each match with level ERROR, bucket by the `YYYY-MM-DD HH` prefix; count the messages; count lines that don't match.

```python
import re
from collections import Counter

LOG_LINE = re.compile(r"^(?P<hour>\d{4}-\d{2}-\d{2} \d{2}):\d{2}:\d{2} (?P<level>[A-Z]+) (?P<message>.+)$")

lines = [
    "2026-10-29 10:05:01 ERROR db timeout",
    "2026-10-29 10:15:22 INFO batch loaded",
    "2026-10-29 10:47:09 ERROR db timeout",
    "2026-10-29 11:02:00 ERROR disk full",
    "garbage line",
    "2026-10-29 11:30:00 WARNING slow query",
]


def analyze(log_lines) -> tuple[dict[str, int], list[tuple[str, int]], int]:
    per_hour: Counter[str] = Counter()
    messages: Counter[str] = Counter()
    unparsed = 0
    for line in log_lines:
        match = LOG_LINE.match(line.rstrip("\n"))
        if match is None:
            unparsed += 1
            continue
        if match["level"] == "ERROR":
            per_hour[match["hour"]] += 1
            messages[match["message"]] += 1
    return dict(sorted(per_hour.items())), messages.most_common(1), unparsed


print(*analyze(lines))
```

**Output:**

```text
{'2026-10-29 10': 2, '2026-10-29 11': 1} [('db timeout', 2)] 1
```

**Complexity:** O(n) time; O(hours + distinct messages) space.

**Edge cases:** multi-line stack traces (continuation lines should attach to the previous entry, not count as unparsed); time zones in the log timestamps; hours with zero errors (fill them in for charts by iterating over the hour range); messages containing variable IDs (`"timeout for order 123"`: normalise them with a regex, e.g. replace digits with `<n>`, to group similar errors).

**Common mistakes:** `re.search` without anchors (matching inside messages); compiling the regex inside the loop; `split(" ")` breaking on messages that contain spaces.

**Follow-up questions:** alert when errors in any 5-minute window exceed a threshold (a sliding window with a `deque` of timestamps); process logs from 100 servers (parallel per file, then merge the Counters); the p95 latency per endpoint (collect values per endpoint, or use a streaming quantile sketch).

---

#### Problem 31: Sessionize User Events (30-Minute Inactivity Gap) [Advanced]

- **Problem:** Group each user's events into sessions. A new session starts when the gap since the user's previous event exceeds 30 minutes.
- **Sample input:** u1 at 10:00, 10:10, 11:00, 11:20; u2 at 09:00 (unsorted)
- **Expected output:** `[('u1', 1, '10:00', '10:10', 2), ('u1', 2, '11:00', '11:20', 2), ('u2', 1, '09:00', '09:00', 1)]`

**Approach:** sort by `(user, timestamp)`; walk through the events, keeping the current session per user; start a new session when the user changes or the gap exceeds the limit.

```python
from datetime import datetime, timedelta

events = [("u1", "2026-10-29T10:00"), ("u1", "2026-10-29T10:10"), ("u2", "2026-10-29T09:00"),
          ("u1", "2026-10-29T11:00"), ("u1", "2026-10-29T11:20")]


def sessionize(raw_events: list[tuple[str, str]], gap: timedelta = timedelta(minutes=30)) -> list[tuple]:
    parsed = sorted((user, datetime.fromisoformat(ts)) for user, ts in raw_events)
    sessions: list[list] = []                 # [user, number, start, end, event_count]
    for user, ts in parsed:
        current = sessions[-1] if sessions else None
        if current and current[0] == user and ts - current[3] <= gap:
            current[3] = ts
            current[4] += 1
        else:
            number = current[1] + 1 if current and current[0] == user else 1
            sessions.append([user, number, ts, ts, 1])
    return [(u, n, s.strftime("%H:%M"), e.strftime("%H:%M"), c) for u, n, s, e, c in sessions]


print(sessionize(events))
```

**Output:**

```text
[('u1', 1, '10:00', '10:10', 2), ('u1', 2, '11:00', '11:20', 2), ('u2', 1, '09:00', '09:00', 1)]
```

**Complexity:** O(n log n) time (the sort); O(n) space.

**Edge cases:** exactly a 30-minute gap (decide whether `<=` or `<`); events with identical timestamps; out-of-order and late events in streaming (needs watermarks and allowed lateness); time zones (use UTC).

**Common mistakes:** forgetting to sort; resetting the session number when the user changes incorrectly; comparing timestamp strings in different formats.

**Follow-up questions:** a streaming version per user (state: last event time and session ID per user, with a timeout to close sessions); the SQL version (`LAG(ts) OVER (PARTITION BY user ORDER BY ts)`, flag gaps > 30 minutes, then a running `SUM` of the flags gives the session ID); the average session length per user.

---

#### Problem 32: Find Missing Dates in Daily Partitions [Medium]

- **Problem:** Given the dates of partitions that exist, list the missing dates in a range, also as compact ranges, so you can schedule a backfill.
- **Sample input:** present `2026-10-01, 02, 05, 06, 09`; range `2026-10-01` to `2026-10-10`
- **Expected output:** 5 missing dates and the ranges `[('2026-10-03', '2026-10-04'), ('2026-10-07', '2026-10-08'), ('2026-10-10', '2026-10-10')]`

**Approach:** generate the full date range, subtract the set of present dates, then merge consecutive missing dates into ranges (a missing date that follows the previous missing date by one day extends the current range).

```python
from datetime import date, timedelta


def missing_dates(present: list[str], start: date, end: date) -> list[date]:
    have = {date.fromisoformat(day) for day in present}
    return [start + timedelta(days=n) for n in range((end - start).days + 1) if start + timedelta(days=n) not in have]


def to_ranges(days: list[date]) -> list[tuple[str, str]]:
    ranges: list[list[date]] = []
    for day in days:
        if ranges and day - ranges[-1][1] == timedelta(days=1):
            ranges[-1][1] = day
        else:
            ranges.append([day, day])
    return [(first.isoformat(), last.isoformat()) for first, last in ranges]


present = ["2026-10-01", "2026-10-02", "2026-10-05", "2026-10-06", "2026-10-09"]
gaps = missing_dates(present, date(2026, 10, 1), date(2026, 10, 10))
print(len(gaps), [d.isoformat() for d in gaps])
print(to_ranges(gaps))
```

**Output:**

```text
5 ['2026-10-03', '2026-10-04', '2026-10-07', '2026-10-08', '2026-10-10']
[('2026-10-03', '2026-10-04'), ('2026-10-07', '2026-10-08'), ('2026-10-10', '2026-10-10')]
```

**Complexity:** O(D + P) time for D days in the range and P present partitions; O(P) space.

**Edge cases:** present dates outside the range (ignored); duplicates in the input; business days only (skip weekends with `weekday() < 5`, plus a holiday set); partitions in different formats (`dt=20261001`: parse them consistently).

**Common mistakes:** string comparisons of dates in mixed formats; an off-by-one error that excludes the end date.

**Follow-up questions:** discover the partitions on S3 (list the prefixes with pagination, then parse `dt=` from each key); automatically trigger backfill runs for the ranges (an orchestrator API or CLI); in SQL, `generate_series` + `LEFT JOIN ... WHERE partition IS NULL`.

---

### 20.9 Generator and Decorator Problems

#### Problem 33: Build a Generator-Based Batch Reader [Medium]

- **Problem:** Write a generator that reads a CSV file of any size and yields **parsed** records in batches of `batch_size` (the last batch may be smaller).
- **Sample input:** a CSV with 7 data rows; `batch_size = 3`
- **Expected output:** batch sizes `[3, 3, 1]`; the first batch shown below

**Approach:** open the file inside the generator (so it stays open while the caller iterates); parse the rows lazily with `csv.DictReader`; use `itertools.islice` to cut fixed-size batches; stop when a batch comes back empty.

```python
import csv
from itertools import islice
from pathlib import Path
from typing import Iterator

Path("amounts.csv").write_text("id,amount\n" + "".join(f"{n},{n * 1.5}\n" for n in range(1, 8)), encoding="utf-8")


def read_batches(path: Path, batch_size: int) -> Iterator[list[dict]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    with path.open(newline="", encoding="utf-8") as file:
        parsed = ({"id": int(row["id"]), "amount": float(row["amount"])} for row in csv.DictReader(file))
        while batch := list(islice(parsed, batch_size)):
            yield batch


batches = list(read_batches(Path("amounts.csv"), batch_size=3))
print([len(batch) for batch in batches])
print(batches[0])
```

**Output:**

```text
[3, 3, 1]
[{'id': 1, 'amount': 1.5}, {'id': 2, 'amount': 3.0}, {'id': 3, 'amount': 4.5}]
```

**Complexity:** O(n) time overall; O(batch_size) memory.

**Edge cases:** an empty file (no batches); `batch_size` larger than the file (one batch); an invalid `batch_size` (validated eagerly? Note that this check only runs when iteration **starts**, because generator bodies are lazy; validate in a wrapper function if you need an immediate error); a parse error mid-file (decide: skip and log, or fail).

**Common mistakes:** `readlines()` followed by slicing (loads everything); returning a generator from a normal function that has already closed the file; forgetting the last partial batch.

**Follow-up questions:** add the batch number and a running row count for logging; make batches size-aware (by bytes) for API payload limits; process batches concurrently while preserving order (`ThreadPoolExecutor.map`).

---

#### Problem 34: Implement Retry with Exponential Backoff [Medium]

- **Problem:** Write a `@retry` decorator that retries only specified transient exceptions, with exponentially growing delays, and re-raises after the last attempt. Make it testable without real sleeping.
- **Sample input:** a function that fails twice with `ConnectionError` and then succeeds
- **Expected output:** `ok 3 [0.1, 0.2]`

**Approach:** a decorator factory (three levels: settings → decorator → wrapper). The delay for attempt *n* is `base_delay * 2 ** (n - 1)`. **Inject the sleep function**, so tests can record the delays instead of waiting.

```python
import functools
import time


def retry(*, attempts: int = 3, base_delay: float = 0.1,
          exceptions: tuple[type[BaseException], ...] = (ConnectionError, TimeoutError), sleep=time.sleep):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    sleep(base_delay * 2 ** (attempt - 1))
        return wrapper
    return decorator


delays: list[float] = []
calls = {"count": 0}


@retry(attempts=4, base_delay=0.1, sleep=delays.append)
def flaky_fetch() -> str:
    calls["count"] += 1
    if calls["count"] < 3:
        raise ConnectionError("connection reset")
    return "ok"


print(flaky_fetch(), calls["count"], delays)

delays.clear()


@retry(attempts=2, base_delay=0.5, sleep=delays.append)
def always_times_out() -> None:
    raise TimeoutError("read timeout")


try:
    always_times_out()
except TimeoutError:
    print("gave up after", len(delays) + 1, "attempts; delays:", delays)

delays.clear()


@retry(sleep=delays.append)
def bad_data() -> None:
    raise ValueError("invalid row")


try:
    bad_data()
except ValueError:
    print("ValueError is not retried; delays:", delays)
```

**Output:**

```text
ok 3 [0.1, 0.2]
gave up after 2 attempts; delays: [0.5]
ValueError is not retried; delays: []
```

**Complexity:** O(attempts) calls; the total waiting time grows exponentially (cap it with `max_delay`).

**Edge cases:** `attempts=1` (no retries); generator functions (the decorator retries creating the generator, not consuming it); async functions (need an `async def` wrapper with `await asyncio.sleep`).

**Common mistakes:** catching `Exception` (retrying bugs and bad data); swallowing the final exception; no jitter in distributed systems; retrying non-idempotent writes.

**Follow-up questions:** add jitter (`delay * random.uniform(0.5, 1.0)`) and `max_delay`; honour HTTP `Retry-After`; an overall deadline across attempts; the production-grade version with logging in [11.5](#115-decorators-with-arguments).

---

#### Problem 35: Implement a Timing and Logging Decorator [Easy]

- **Problem:** Write `@timed` that logs how long each call took, logs failures with their duration, re-raises errors and preserves the function's metadata.
- **Sample input:** a fake clock returning 100.0 then 101.25
- **Expected output:** `load_table took 1.25s`

**Approach:** read the clock before and after (in `try/except`), use `functools.wraps`, and inject the clock and the logger for testability.

```python
import functools
import time


def timed(clock=time.perf_counter, log=print):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            started = clock()
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                log(f"{func.__name__} failed after {clock() - started:.2f}s: {error}")
                raise
            log(f"{func.__name__} took {clock() - started:.2f}s")
            return result
        return wrapper
    return decorator


fake_clock_values = iter([100.0, 101.25, 200.0, 200.5])


def fake_clock() -> float:
    return next(fake_clock_values)


@timed(clock=fake_clock)
def load_table(rows: list[int]) -> int:
    """Pretend to load rows."""
    return len(rows)


@timed(clock=fake_clock)
def broken_step() -> None:
    raise RuntimeError("boom")


print(load_table([1, 2, 3]))
try:
    broken_step()
except RuntimeError:
    pass
print(load_table.__name__, load_table.__doc__)
```

**Output:**

```text
load_table took 1.25s
3
broken_step failed after 0.50s: boom
load_table Pretend to load rows.
```

**Complexity:** O(1) overhead per call.

**Edge cases:** the clock choice (`perf_counter` for durations, never `time.time`, which can jump when the system clock changes); nested decorated calls (each one logs its own duration); very fast functions (format with milliseconds).

**Common mistakes:** missing `wraps`; not returning `result`; logging the success message even when the function raised; swallowing exceptions.

**Follow-up questions:** emit metrics (a histogram per function name) instead of logs; add the argument count or a row count; decorate every method of a class (a class decorator that loops over `vars(cls)`).

---

### 20.10 API and Database Problems

#### Problem 36: Handle API Pagination (Offset/Limit) [Medium]

- **Problem:** Fetch all records from an API that returns pages via `offset` and `limit`, stopping correctly and never looping forever.
- **Sample input:** 7 records, `limit = 3`
- **Expected output:** IDs `[1, 2, 3, 4, 5, 6, 7]`, requested offsets `[0, 3, 6]`

**Approach:** request a page, yield its records, and stop when a page is **shorter than the limit** (or empty). Guard with `max_pages`. Deduplicate by ID, because offset paging can return repeats if the data changes during the extraction.

```python
from typing import Callable, Iterator


def fetch_all(get_page: Callable[[int, int], list[dict]], limit: int = 100, max_pages: int = 10_000) -> Iterator[dict]:
    offset, seen_ids = 0, set()
    for _ in range(max_pages):
        page = get_page(offset, limit)
        for record in page:
            if record["id"] not in seen_ids:           # protect against shifted pages
                seen_ids.add(record["id"])
                yield record
        if len(page) < limit:
            return
        offset += limit
    raise RuntimeError(f"exceeded {max_pages} pages")


def make_fake_api(total: int):
    data = [{"id": number} for number in range(1, total + 1)]
    offsets: list[int] = []

    def get_page(offset: int, limit: int) -> list[dict]:
        offsets.append(offset)
        return data[offset:offset + limit]
    return get_page, offsets


get_page, offsets = make_fake_api(7)
print([record["id"] for record in fetch_all(get_page, limit=3)], offsets)
get_page, offsets = make_fake_api(6)                  # exact multiple: one extra (empty) request
print(len(list(fetch_all(get_page, limit=3))), offsets)
```

**Output:**

```text
[1, 2, 3, 4, 5, 6, 7] [0, 3, 6]
6 [0, 3, 6]
```

**Complexity:** O(n) records, O(n / limit) requests; O(n) memory for `seen_ids` (drop it if the API guarantees stable pages).

**Edge cases:** an exact multiple of the limit (one extra empty call); the API capping `limit` below what you asked for (compare with the **requested** limit carefully, or use a `has_more` / `next` field when available); an empty dataset; records inserted or deleted during paging.

**Common mistakes:** `while True` with no guard; stopping on `len(page) == 0` only (an extra call every time); not handling HTTP 429 and 5xx responses ([15.14](#1514-api-pagination)).

**Follow-up questions:** cursor-based pagination (more robust, [15.14](#1514-api-pagination)); incremental API pulls with `updated_since` and a watermark; parallel page fetching when the total count is known (`ThreadPoolExecutor` with a rate limit).

---

#### Problem 37: Load Database Records in Configurable Batches [Medium]

- **Problem:** Insert an iterable of rows into a table in batches of `batch_size`, committing each batch, and return the total rows and number of batches.
- **Sample input:** 10 generated rows, `batch_size = 4`
- **Expected output:** `(10, 3)` and a table count of `10`

**Approach:** chunk the iterable lazily (`islice`), run `executemany` per chunk inside a transaction, and accumulate the counts.

```python
import sqlite3
from contextlib import closing
from itertools import islice
from typing import Iterable, Iterator, Sequence


def chunked(rows: Iterable[Sequence], size: int) -> Iterator[list[Sequence]]:
    iterator = iter(rows)
    while batch := list(islice(iterator, size)):
        yield batch


def load_in_batches(conn: sqlite3.Connection, rows: Iterable[Sequence], batch_size: int = 1000) -> tuple[int, int]:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    total = batches = 0
    for batch in chunked(rows, batch_size):
        with conn:                                              # one transaction per batch
            conn.executemany("INSERT INTO events (id, kind) VALUES (?, ?)", batch)
        total += len(batch)
        batches += 1
    return total, batches


with closing(sqlite3.connect(":memory:")) as conn:
    conn.execute("CREATE TABLE events (id INTEGER PRIMARY KEY, kind TEXT)")
    generated = ((n, "click" if n % 2 else "view") for n in range(1, 11))   # a generator: never fully in memory
    print(load_in_batches(conn, generated, batch_size=4))
    print(conn.execute("SELECT COUNT(*) FROM events").fetchone()[0])
```

**Output:**

```text
(10, 3)
10
```

**Complexity:** O(n) time; O(batch_size) memory; O(n / batch_size) round trips and commits.

**Edge cases:** an empty input (0, 0); a failure in batch k (batches before k are committed, so a re-run must be **idempotent**: upsert, or record the last committed batch); a constraint violation in one row failing the whole batch (retry that batch row by row to isolate the bad rows).

**Common mistakes:** one giant transaction for millions of rows (lock contention, huge rollback); a commit per row (very slow); `fetchall()` on the source side.

**Follow-up questions:** how do you choose the batch size? (Measure; typically 1k–10k; it depends on the row width and the network latency); even faster loading (`COPY` / bulk load from a staged file, [14.7](#147-batch-inserts-and-executemany)); resuming after a crash (a checkpoint of the last loaded key).

---

#### Problem 38: Implement an Incremental Extraction Using a Watermark [Advanced]

- **Problem:** Extract only the rows changed since the last run, using a compound watermark `(updated_at, id)`, and return the new watermark. A second run with no changes must extract nothing.
- **Sample input:** four source rows; previous watermark `("2026-10-29T10:00", 2)`
- **Expected output:** first run IDs `[3, 4]` with watermark `('2026-10-29T11:00', 4)`; second run `[]` with the same watermark

**Approach:**
1. Select rows whose `(updated_at, id)` tuple is **greater** than the watermark. The ID tie-breaker catches rows that share the watermark's timestamp.
2. Order them by `(updated_at, id)`.
3. The new watermark is the last row's `(updated_at, id)`. **Persist it only after the rows are successfully loaded.**

```python
def extract_incremental(source: list[dict], watermark: tuple[str, int]) -> tuple[list[dict], tuple[str, int]]:
    changed = sorted((row for row in source if (row["updated_at"], row["id"]) > watermark),
                     key=lambda row: (row["updated_at"], row["id"]))
    new_watermark = (changed[-1]["updated_at"], changed[-1]["id"]) if changed else watermark
    return changed, new_watermark


source_rows = [
    {"id": 1, "updated_at": "2026-10-29T09:00"},
    {"id": 2, "updated_at": "2026-10-29T10:00"},
    {"id": 3, "updated_at": "2026-10-29T10:00"},     # same timestamp as the watermark, higher id
    {"id": 4, "updated_at": "2026-10-29T11:00"},
]
state = ("2026-10-29T10:00", 2)
rows, state = extract_incremental(source_rows, state)
print([row["id"] for row in rows], state)
rows, state = extract_incremental(source_rows, state)
print([row["id"] for row in rows], state)
```

**Output:**

```text
[3, 4] ('2026-10-29T11:00', 4)
[] ('2026-10-29T11:00', 4)
```

In SQL the same predicate is `WHERE updated_at > :ts OR (updated_at = :ts AND id > :id) ORDER BY updated_at, id`. The production version, with batching, upserts and atomic state, is in [14.12](#1412-production-safe-incremental-extraction).

**Complexity:** O(n log n) here (filtering plus sorting in Python); in a database with an index on `(updated_at, id)` it is O(changes · log n).

**Edge cases:** the first run (an initial watermark such as `("1970-01-01", 0)`, or a configured start date); late-committed rows with an older `updated_at` (a lookback window plus idempotent upserts); deleted rows (invisible to this method, so use CDC or soft deletes); time-zone-inconsistent timestamps; clock skew between servers.

**Common mistakes:** using `>=` on the timestamp alone (re-extracts rows every time) or `>` alone (skips rows that share the timestamp); saving the watermark **before** the load succeeds (data loss on failure); taking the watermark from `now()` instead of from the data.

**Follow-up questions:** how do you backfill one day? (Run with an explicit start and end range, independent of the stored watermark); how do you make the load idempotent? (Upsert by key); how do you handle a source without `updated_at`? (CDC, hash comparison, or a full reload.)

---

#### Problem 39: Reconcile Source and Target Record Counts per Partition [Medium]

- **Problem:** Compare per-day row counts between the source and the target and report mismatching, missing and unexpected partitions.
- **Sample input:** source `{27: 100, 28: 120, 29: 90}`, target `{27: 100, 28: 118, 30: 5}` (October 2026)
- **Expected output:** shown below

**Approach:** take the union of the partition keys; for each one compare `source.get(day, 0)` with `target.get(day, 0)`; report the differences, sorted.

```python
def reconcile_counts(source: dict[str, int], target: dict[str, int]) -> tuple[list[tuple[str, int, int, int]], dict[str, int]]:
    mismatches = []
    for day in sorted(source.keys() | target.keys()):
        source_count, target_count = source.get(day, 0), target.get(day, 0)
        if source_count != target_count:
            mismatches.append((day, source_count, target_count, target_count - source_count))
    partitions = len(source.keys() | target.keys())
    return mismatches, {"partitions": partitions, "matched": partitions - len(mismatches), "mismatched": len(mismatches)}


source_counts = {"2026-10-27": 100, "2026-10-28": 120, "2026-10-29": 90}
target_counts = {"2026-10-27": 100, "2026-10-28": 118, "2026-10-30": 5}
problems, summary = reconcile_counts(source_counts, target_counts)
for problem in problems:
    print(problem)
print(summary)
```

**Output:**

```text
('2026-10-28', 120, 118, -2)
('2026-10-29', 90, 0, -90)
('2026-10-30', 0, 5, 5)
{'partitions': 4, 'matched': 1, 'mismatched': 3}
```

**Complexity:** O(p log p) for p partitions (the sort).

**Edge cases:** rejected rows (compare `source == target + rejected`); expected differences from filters (document them and reconcile against the filtered source count); late-arriving data (the counts may legitimately change for recent days, so re-check them later).

**Common mistakes:** comparing only grand totals (offsetting errors cancel out: one day +5 and another −5); counts without control totals (`SUM(amount)`); comparing at different times while the source is still changing.

**Follow-up questions:** produce the counts efficiently (`SELECT dt, COUNT(*), SUM(amount) FROM ... GROUP BY dt` in each system); automate alerts above a tolerance; find **which** rows differ (key-set diff and row hashes, [15.13](#1513-source-to-target-reconciliation)).

---

### 20.11 Memory, Missing-Value and Complexity Problems

#### Problem 40: Moving Average over a Stream [Medium]

- **Problem:** Yield the average of the last `window` values for each position once the window is full, in O(1) time per element.
- **Sample input:** `[1, 2, 3, 4, 5, 6]`, `window = 3`
- **Expected output:** `[2.0, 3.0, 4.0, 5.0]`

**Approach:** keep a `deque` of the window's values and a running total. Add the new value; when the window overflows, subtract the value that falls out.

```python
from collections import deque
from typing import Iterable, Iterator


def moving_average(values: Iterable[float], window: int) -> Iterator[float]:
    if window <= 0:
        raise ValueError("window must be positive")
    buffer: deque[float] = deque()
    total = 0.0
    for value in values:
        buffer.append(value)
        total += value
        if len(buffer) > window:
            total -= buffer.popleft()
        if len(buffer) == window:
            yield total / window


print(list(moving_average([1, 2, 3, 4, 5, 6], 3)), list(moving_average([1, 2], 3)))
```

**Output:**

```text
[2.0, 3.0, 4.0, 5.0] []
```

**Complexity:** O(n) time overall (O(1) per element); O(window) space.

**Edge cases:** fewer values than the window (nothing yielded, or yield partial averages, as agreed); `None` values (skip or impute them); floating-point drift over very long streams (recompute the total periodically, or use `math.fsum` on the deque).

**Common mistakes:** `sum(values[i-window:i])` for every i (O(n × window)); a list with `pop(0)` (O(window) per step).

**Follow-up questions:** a **time-based** window ("average over the last 5 minutes": pop from the left while the oldest timestamp is out of the window); a moving median (two heaps, or `sortedcontainers`); pandas `rolling(window).mean()`.

---

#### Problem 41: Handle Missing Values in Records [Medium]

- **Problem:** Count missing values per column, then forward-fill missing `temp` readings **per sensor** (using the sensor's previous reading), flagging the imputed values. Leave the value missing when there is no previous reading.
- **Sample input:** five sensor readings, two with `temp = None`
- **Expected output:** missing counts `{'sensor': 0, 'ts': 0, 'temp': 2}` and the filled rows below

**Approach:** count missing values with a dict of counters; for the forward-fill, sort by `(sensor, ts)` and remember the last non-missing value per sensor in a dict. Never invent a value without a rule, and always flag imputed values.

```python
def missing_counts(rows: list[dict], columns: list[str]) -> dict[str, int]:
    return {column: sum(1 for row in rows if row.get(column) in (None, "")) for column in columns}


def forward_fill(rows: list[dict], group: str, order: str, column: str) -> list[dict]:
    last_seen: dict = {}
    filled = []
    for row in sorted(rows, key=lambda r: (r[group], r[order])):
        value = row.get(column)
        imputed = False
        if value is None and row[group] in last_seen:
            value, imputed = last_seen[row[group]], True
        if row.get(column) is not None:
            last_seen[row[group]] = row[column]
        filled.append({**row, column: value, f"{column}_imputed": imputed})
    return filled


readings = [
    {"sensor": "s1", "ts": 1, "temp": 20.0},
    {"sensor": "s1", "ts": 2, "temp": None},
    {"sensor": "s2", "ts": 1, "temp": None},
    {"sensor": "s1", "ts": 3, "temp": 22.0},
    {"sensor": "s2", "ts": 2, "temp": 18.0},
]
print(missing_counts(readings, ["sensor", "ts", "temp"]))
for row in forward_fill(readings, "sensor", "ts", "temp"):
    print(row["sensor"], row["ts"], row["temp"], row["temp_imputed"])
```

**Output:**

```text
{'sensor': 0, 'ts': 0, 'temp': 2}
s1 1 20.0 False
s1 2 20.0 True
s1 3 22.0 False
s2 1 None False
s2 2 18.0 False
```

**Complexity:** O(n log n) because of the sort (O(n) if the input is already ordered); O(groups) extra memory.

**Edge cases:** the first reading of a group is missing (it stays missing); long gaps (limit how far a value may be carried, e.g. at most 3 readings or 1 hour); placeholder tokens (`""`, `"N/A"`: normalise them first, [15.10](#1510-null-and-empty-string-handling)); a legitimate `0` (not missing).

**Common mistakes:** filling across groups (sensor s2 inheriting s1's value); filling before sorting by time; `fillna(0)` / `or 0` style defaults that turn "unknown" into a fake measurement.

**Follow-up questions:** the pandas equivalent (`df.sort_values(["sensor", "ts"]).groupby("sensor")["temp"].ffill()`); when to reject instead of impute (required business fields such as amount or customer ID); report the missing-rate per column as a data-quality metric over time.

---

#### Problem 42: Find Duplicate Keys in a File Larger Than Memory [Advanced]

- **Problem:** Find keys that occur more than once in a file too large to hold all the keys in memory.
- **Sample input:** keys `5 3 9 5 1 2 9 7 2 2 8 4` (one per line)
- **Expected output:** `[('2', 3), ('5', 2), ('9', 2)]`

**Approach – hash partitioning ("divide and conquer"):**
1. Stream the file once and write each key to one of N partition files chosen by a **stable hash** of the key (`zlib.crc32`; the built-in `hash()` of strings changes between runs). All copies of a key land in the **same** partition.
2. Each partition is about 1/N of the data, small enough to count in memory with a `Counter`.
3. Collect the keys with a count > 1 from each partition.

This is the same idea as a MapReduce or Spark **shuffle**.

```python
import tempfile
import zlib
from collections import Counter
from contextlib import ExitStack
from pathlib import Path


def duplicate_keys_external(path: Path, partitions: int = 4) -> list[tuple[str, int]]:
    duplicates: list[tuple[str, int]] = []
    with tempfile.TemporaryDirectory() as work_dir:
        partition_paths = [Path(work_dir, f"part_{n}.txt") for n in range(partitions)]
        with ExitStack() as stack, path.open(encoding="utf-8") as source:
            outputs = [stack.enter_context(p.open("w", encoding="utf-8")) for p in partition_paths]
            for line in source:                                     # pass 1: scatter
                key = line.strip()
                if key:
                    outputs[zlib.crc32(key.encode("utf-8")) % partitions].write(key + "\n")
        for partition_path in partition_paths:                      # pass 2: count each partition
            with partition_path.open(encoding="utf-8") as partition:
                counts = Counter(line.strip() for line in partition)
            duplicates.extend((key, count) for key, count in counts.items() if count > 1)
    return sorted(duplicates)


Path("keys.txt").write_text("\n".join("5 3 9 5 1 2 9 7 2 2 8 4".split()) + "\n", encoding="utf-8")
print(duplicate_keys_external(Path("keys.txt"), partitions=3))
```

**Output:**

```text
[('2', 3), ('5', 2), ('9', 2)]
```

**Complexity:** two passes, O(n) I/O; peak memory about O(distinct keys / N); disk space O(n).

**Edge cases:** skewed keys (one huge partition: increase N or re-partition the big one); blank lines; key normalisation (whitespace, case) before hashing.

**Common mistakes:** `hash()` for partitioning across processes or runs (randomised per process for strings); too few partitions; leaving temp files behind (use `TemporaryDirectory`).

**Follow-up questions:** an alternative (an external sort, then one pass comparing neighbours); probabilistic deduplication (a Bloom filter: no false negatives, a small false-positive rate); the "real-world" answer (load into a database or Spark and `GROUP BY key HAVING COUNT(*) > 1`).

---

**Complexity quick-check (often asked verbally):**

| Snippet | Complexity | Why |
|---|---|---|
| `for x in a: if x in b_list:` | O(n × m) | list membership is linear |
| `b_set = set(b); for x in a: if x in b_set:` | O(n + m) | set membership is O(1) on average |
| `sorted(items)[:k]` vs `heapq.nsmallest(k, items)` | O(n log n) vs O(n log k) | a heap keeps only k items |
| `s = ""; for p in parts: s += p` | up to O(n²) | strings are immutable |
| `lst.pop(0)` in a loop | O(n²) total | shifts every element; use `deque.popleft()` |
| `for i in range(n): for j in range(i, n):` | O(n²) | ≈ n²/2 iterations |
| Binary search | O(log n) | halves the search space each step |
| Recursion `fib(n)` without memoisation | O(2ⁿ) | overlapping subproblems; `lru_cache` makes it O(n) |

---

### 20.12 Design Problems

#### Problem 43: Implement an LRU Cache [Medium]

- **Problem:** Build a cache with a fixed capacity, where `get` and `put` are O(1), that evicts the **least recently used** key when full.
- **Sample input:** capacity 2: `put(a,1)`, `put(b,2)`, `get(a)`, `put(c,3)`, `get(b)`
- **Expected output:** `get(a) → 1`, `get(b) → None` (b was evicted), order `['a', 'c']`

**Approach:** `OrderedDict` keeps the usage order. On `get` or `put`, `move_to_end(key)` marks the key as most recent; when over capacity, `popitem(last=False)` removes the oldest. (Under the hood this is a hash map plus a doubly linked list, which is what you would implement in a language without `OrderedDict`.)

```python
from collections import OrderedDict
from typing import Hashable


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._data: OrderedDict[Hashable, object] = OrderedDict()

    def get(self, key: Hashable, default: object = None) -> object:
        if key not in self._data:
            return default
        self._data.move_to_end(key)                 # mark as most recently used
        return self._data[key]

    def put(self, key: Hashable, value: object) -> None:
        self._data[key] = value
        self._data.move_to_end(key)
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)          # evict the least recently used

    def keys(self) -> list:
        return list(self._data)


cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
first = cache.get("a")
cache.put("c", 3)                                   # evicts "b"
print(first, cache.get("b"), cache.keys())
cache.put("a", 10)                                  # update moves "a" to the most-recent end
print(cache.keys(), cache.get("a"))
```

**Output:**

```text
1 None ['a', 'c']
['c', 'a'] 10
```

**Complexity:** O(1) for `get` and `put`; O(capacity) space.

**Edge cases:** capacity 1; updating an existing key (must not evict anything, and moves it to the most-recent end); a stored value of `None` (use a sentinel default if you need to tell "missing" from "None").

**Common mistakes:** a list for the order (O(n) removals); forgetting to refresh the order on `get`; not thread-safe (add a `threading.Lock` if it is shared between threads).

**Follow-up questions:** use `functools.lru_cache` for pure functions instead; add expiry ([Problem 44](#problem-44-implement-a-cache-with-time-to-live-ttl-medium)); LFU (least *frequently* used) eviction; a distributed cache (Redis, with its own eviction policies).

---

#### Problem 44: Implement a Cache with Time-to-Live (TTL) [Medium]

- **Problem:** Cache values that expire after `ttl` seconds (for example API tokens or reference data), and make it testable without waiting.
- **Sample input:** `set("token", "abc")` at t=0 with a TTL of 10 s; `get` at t=5 and t=10
- **Expected output:** `abc`, then `None`, and the cache is empty afterwards

**Approach:** store `(expires_at, value)`. On `get`, compare against the clock and delete expired entries lazily. **Inject the clock** (default `time.monotonic`, which never jumps backwards) so tests control time.

```python
import time
from typing import Callable, Hashable


class TTLCache:
    def __init__(self, ttl_seconds: float, clock: Callable[[], float] = time.monotonic) -> None:
        self.ttl, self._clock = ttl_seconds, clock
        self._data: dict[Hashable, tuple[float, object]] = {}

    def set(self, key: Hashable, value: object) -> None:
        self._data[key] = (self._clock() + self.ttl, value)

    def get(self, key: Hashable, default: object = None) -> object:
        entry = self._data.get(key)
        if entry is None:
            return default
        expires_at, value = entry
        if self._clock() >= expires_at:
            del self._data[key]                     # lazy expiry
            return default
        return value

    def purge_expired(self) -> int:
        now = self._clock()
        expired = [key for key, (expires_at, _) in self._data.items() if now >= expires_at]
        for key in expired:
            del self._data[key]
        return len(expired)

    def __len__(self) -> int:
        return len(self._data)


fake_now = [0.0]
cache = TTLCache(ttl_seconds=10, clock=lambda: fake_now[0])
cache.set("token", "abc")
fake_now[0] = 5.0
print(cache.get("token"))
fake_now[0] = 10.0
print(cache.get("token"), len(cache))
```

**Output:**

```text
abc
None 0
```

**Complexity:** `get` and `set` O(1); `purge_expired` O(n).

**Edge cases:** an expiry exactly at the boundary (`>=` means expired); keys that are never read again (memory grows unless you purge periodically or cap the size, e.g. combine with LRU); clock changes (use a monotonic clock, not `time.time()`).

**Common mistakes:** `time.time()` (wall-clock jumps break expiry); background threads for expiry when lazy expiry is enough; caching errors or empty responses for the full TTL.

**Follow-up questions:** refresh tokens **before** they expire (refresh at 80% of the TTL); thread safety (a lock around access); share the cache across workers (Redis with `SETEX`).

---

### 20.13 Classic Algorithm Problems

#### Problem 45: Validate Balanced Parentheses [Easy]

- **Problem:** Return `True` if every bracket in the string is closed by the matching bracket in the correct order.
- **Sample input:** `"([]{})"`, `"([)]"`, `"(("`
- **Expected output:** `True`, `False`, `False`

**Approach:** use a **stack**. Push opening brackets; on a closing bracket, the top of the stack must be its matching opener. At the end the stack must be empty.

```python
PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text: str) -> bool:
    stack: list[str] = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in PAIRS:
            if not stack or stack.pop() != PAIRS[char]:
                return False
    return not stack


print([is_balanced(s) for s in ["([]{})", "([)]", "((", "", "f(x[0]) + {y}"]])
```

**Output:**

```text
[True, False, False, True, True]
```

**Complexity:** O(n) time; O(n) space in the worst case (all openers).

**Edge cases:** an empty string (balanced); non-bracket characters (ignored); a closer with an empty stack.

**Common mistakes:** only counting brackets (`"([)]"` has balanced counts but the wrong order); forgetting the final empty-stack check.

**Follow-up questions:** brackets inside quoted strings should be ignored (track a "quoted" state); validate nested JSON or SQL parentheses before parsing; return the position of the first error.

---

#### Problem 46: Merge Two Sorted Lists [Easy]

- **Problem:** Merge two ascending lists into one ascending list in linear time.
- **Sample input:** `[1, 4, 7]`, `[2, 3, 8, 9]`
- **Expected output:** `[1, 2, 3, 4, 7, 8, 9]`

**Approach:** two pointers; repeatedly take the smaller head; then append whatever remains. This is the core step of merge sort and of **external sorting**, where sorted run files are merged.

```python
import heapq


def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    i = j = 0
    merged: list[int] = []
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:            # <= keeps the merge stable
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    return merged + first[i:] + second[j:]


print(merge_sorted([1, 4, 7], [2, 3, 8, 9]), merge_sorted([], [1]))
print(list(heapq.merge([1, 5], [2, 6], [3, 4])))          # k sorted inputs, lazily
```

**Output:**

```text
[1, 2, 3, 4, 7, 8, 9] [1]
[1, 2, 3, 4, 5, 6]
```

**Complexity:** O(n + m) time and space; `heapq.merge` of k streams is O(N log k) time with O(k) memory.

**Edge cases:** empty inputs; duplicates across the lists; inputs that are not actually sorted (the output will be wrong, so validate if unsure).

**Common mistakes:** `sorted(first + second)` (correct but O((n+m) log(n+m))); forgetting the leftovers.

**Follow-up questions:** merge 100 sorted files that don't fit in memory (`heapq.merge` over file iterators); merge with a key function (`heapq.merge(..., key=...)`).

---

#### Problem 47: Implement Bubble Sort, Merge Sort and Quick Sort [Medium]

- **Problem:** Implement three classic sorting algorithms and compare them.
- **Sample input:** `[5, 2, 9, 1, 5, 6]`
- **Expected output:** `[1, 2, 5, 5, 6, 9]` from all three

| Algorithm | Idea | Time (average / worst) | Extra space | Stable |
|---|---|---|---|---|
| Bubble sort | repeatedly swap adjacent out-of-order items; stop early when a pass makes no swaps | O(n²) / O(n²) (best O(n) on sorted input) | O(1) | Yes |
| Merge sort | split in half, sort each half recursively, merge | O(n log n) / O(n log n) | O(n) | Yes |
| Quick sort | partition around a pivot, sort each side | O(n log n) / O(n²) (bad pivots) | O(log n) in place; O(n) for the simple version below | No |
| **Timsort** (`sorted`, `list.sort`) | merge sort + insertion sort, exploits existing runs | O(n log n) / O(n log n), best O(n) | O(n) | Yes |

```python
def bubble_sort(values: list[int]) -> list[int]:
    items = values[:]                                   # don't mutate the caller's list
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for index in range(end):                        # the last items are already in place
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:
            break
    return items


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values[:]
    middle = len(values) // 2
    left, right = merge_sort(values[:middle]), merge_sort(values[middle:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def quick_sort(values: list[int]) -> list[int]:
    """Simple (not in-place) version; the middle-element pivot avoids the worst case on sorted input."""
    if len(values) <= 1:
        return values[:]
    pivot = values[len(values) // 2]
    return (quick_sort([v for v in values if v < pivot])
            + [v for v in values if v == pivot]
            + quick_sort([v for v in values if v > pivot]))


sample = [5, 2, 9, 1, 5, 6]
print(bubble_sort(sample), merge_sort(sample), quick_sort(sample))
print(all(algorithm(sample) == sorted(sample) for algorithm in (bubble_sort, merge_sort, quick_sort)), sample)
```

**Output:**

```text
[1, 2, 5, 5, 6, 9] [1, 2, 5, 5, 6, 9] [1, 2, 5, 5, 6, 9]
True [5, 2, 9, 1, 5, 6]
```

**Edge cases:** empty and single-element lists; all-equal values (the three-way partition in `quick_sort` handles them efficiently); already-sorted input (bubble sort exits after one pass).

**Common mistakes:** quick sort with the first element as the pivot on sorted data (O(n²) and deep recursion); merge sort without `<=` (loses stability); sorting in place by accident when the caller expects a new list.

**Follow-up questions:** *Which would you use in production?* `sorted()` / `list.sort()`. These implementations exist to test fundamentals. *Why does stability matter?* Multi-pass sorts by several keys rely on it ([Problem 15](#problem-15-sort-a-list-of-dictionaries-by-multiple-fields-medium)). *How do you sort data bigger than memory?* An external merge sort: sort chunks, write sorted runs, `heapq.merge` them.

---

#### Problem 48: Candy-Wrapper Exchange Puzzle [Easy]

- **Problem:** Each candy costs 1 unit, and every `k` wrappers can be exchanged for 1 new candy (which also has a wrapper). How many candies can you eat with `amount` money?
- **Sample input:** `amount = 15`, `k = 3`
- **Expected output:** `22` (15 bought, then +5, +1, +1, with 1 wrapper left over)

**Approach (simulation):** start with `amount` candies and `amount` wrappers. While you have at least `k` wrappers: exchange them for `wrappers // k` new candies; the new wrapper count is the leftover (`wrappers % k`) plus the wrappers of the new candies.

```python
def max_candies(amount: int, wrappers_per_candy: int = 3) -> int:
    if wrappers_per_candy < 2:
        raise ValueError("wrappers_per_candy must be at least 2 (otherwise candies are infinite)")
    candies = wrappers = amount
    while wrappers >= wrappers_per_candy:
        new_candies = wrappers // wrappers_per_candy
        candies += new_candies
        wrappers = wrappers % wrappers_per_candy + new_candies
    return candies


def max_candies_formula(amount: int, wrappers_per_candy: int = 3) -> int:
    """Each exchange consumes k wrappers and returns 1, a net cost of k - 1 wrappers."""
    return amount + (amount - 1) // (wrappers_per_candy - 1) if amount > 0 else 0


print(max_candies(15), max_candies(20), max_candies(0), [max_candies_formula(n) for n in (15, 20, 0)])
```

**Output:**

```text
22 29 0 [22, 29, 0]
```

**Complexity:** simulation O(log amount) iterations (the wrapper count shrinks geometrically); formula O(1).

**Edge cases:** `amount = 0`; `k = 1` (infinite, so reject it); very large amounts (Python integers don't overflow).

**Common mistakes:** forgetting that the new candies produce wrappers too; dropping the leftover wrappers each round.

**Follow-up questions:** what if you can "borrow" a candy and return a wrapper later? (Then the answer becomes `amount * k // (k - 1)`.) Interviewers use this puzzle to check that you can model state changes in a loop cleanly.

---

### Chapter 20 Review

**Key takeaways**
- Most problems become O(n) with the right structure: a **dict** (lookups, grouping, joins, latest-per-key), a **set** (membership, diffs), a **Counter** (frequencies), a **heap** (top-N), a **deque** (windows).
- Stream inputs and keep only the state you need; partition to disk when even the state is too large.
- State the edge cases out loud: empty input, NULLs vs zero, duplicates, ties, time zones, unsorted input.
- Make production-style helpers testable: inject the clock, the sleep function and the clients.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How do you approach an unfamiliar problem? | Clarify → brute force → optimise with the right data structure → code → test → complexity. |
| When do you sort first? | When order makes the logic simpler (intervals, sessions, groupby, merge compare): O(n log n). |
| How do you handle huge inputs? | Streaming, chunking, hash partitioning, external sort, or push the work to a database / Spark. |
| How do you make the output deterministic? | Define the tie-breaking rules and sort the final results. |

**Common traps:** `list(set(x))` losing order; `sorted(x)[-2]` with duplicates; `groupby` without sorting; `>=` vs `>` on watermarks; truthiness rejecting `0`; mutating the input arguments.

**Practice exercise:** Re-solve Problems 6, 16, 22, 25, 29 and 38 from memory in under 15 minutes each, then write two extra edge-case tests for each one.

---

## 21. Scenario-Based Interview Questions

Scenario questions test **judgement**: can you design something that works at 3 AM with bad data and flaky networks? A strong answer structure: **clarify** (volume, latency, SLAs, sources, failure tolerance) → **approach** → **why** → **failure modes** → **operations** (monitoring, re-runs, cost).

### 21.1 Processing a File Larger Than Available Memory

**Problem:** A 60 GB CSV must be aggregated on a worker with 8 GB of RAM.

**Recommended approach:**
1. **Stream** it: iterate over the file object or `csv.reader`, or use `pandas.read_csv(chunksize=...)` with `usecols` and explicit `dtype`s.
2. Keep only **combinable aggregates** in memory (counts, sums, min/max per key), or write intermediate results out per chunk.
3. If the per-key state itself is too big, **hash-partition** to disk first ([Problem 42](#problem-42-find-duplicate-keys-in-a-file-larger-than-memory-advanced)).
4. Parallelise **by file or byte range** with processes if you are CPU-bound.
5. If this is recurring and growing, convert it to **Parquet** and use DuckDB, Polars (lazy/streaming) or Spark.

**Why it works:** memory becomes O(chunk + aggregate state) instead of O(file size).

```text
totals = {}
for chunk in read_csv(path, chunksize=200_000, usecols=["region", "amount"], dtype={...}):
    for region, subtotal in chunk.groupby("region")["amount"].sum().items():
        totals[region] = totals.get(region, 0) + subtotal
write(totals)
```

**Failure cases:** a non-combinable metric (median, distinct count) needs sorting, partitioning or approximation; one malformed line in the middle (handle it per row, [21.2](#212-handling-malformed-rows)); a gzip file (not splittable, so only sequential reading).

**Production considerations:** checkpoint progress (byte offset or chunk number) for restartability; log progress every N rows; measure the peak RSS.

**Follow-up questions:** *How do you compute a median?* An external sort or partition, or an approximate quantile sketch. *How do you speed it up?* Columnar formats, parallel processes, pushing the work into a query engine.

---

### 21.2 Handling Malformed Rows

**Problem:** Some rows have extra delimiters, bad encodings, invalid dates or missing required fields.

**Recommended approach:**
- Parse with a **real parser** (the `csv` module), never `split(",")`.
- Validate each row (schema, types, rules) in a **pure function** that returns `(clean_row, None)` or `(None, reason)` ([Problem 25](#problem-25-read-a-csv-validate-rows-transform-data-and-write-rejected-records-separately-medium)).
- Route bad rows to a **quarantine / dead-letter** location with the raw content, line number, reason and run ID.
- **Fail the run** if the reject ratio exceeds a threshold (e.g. 1%), because a high reject rate means the upstream format changed.
- Reconcile: `read = loaded + rejected`.

**Why it works:** good data keeps flowing, bad data is never silently lost, and systemic problems still stop the pipeline.

**Failure cases:** a header change shifts every column (validate the header first and fail fast); an encoding problem in the whole file (fail rather than reject 100% of the rows); a quarantine area that nobody reviews (alert and own it).

**Production considerations:** a reprocessing path (fix the rows → re-ingest them from quarantine idempotently); PII in the quarantine (same access controls as the main data); metrics for the reject counts per reason.

**Follow-up questions:** *Who fixes rejected rows?* Define the ownership with the source team (a data contract). *How do you replay them?* A re-ingest job reading the quarantine with the same validation.

---

### 21.3 Handling Duplicate Records

**Problem:** The same records arrive several times: re-sent files, at-least-once message delivery, retries, overlapping extraction windows.

**Recommended approach:**
- Identify the **business key** (or a natural key plus a version).
- Deduplicate **within a batch** (keep the latest per key by `updated_at` and a sequence number, [Problem 23](#problem-23-deduplicate-cdc-records-keeping-the-latest-per-key-medium)).
- Deduplicate **across batches** by writing with **upsert / MERGE** on the key, or delete+insert per partition.
- Detect **duplicate files** with checksums in a manifest ([15.15](#1515-file-ingestion-pipelines)).
- For exact duplicates without a key, use a **row hash** ([15.7](#157-deduplication)).

**Why it works:** idempotent writes make duplicates harmless no matter how they arrive.

**Failure cases:** no reliable key (agree on a key or hash with the business); "duplicates" that are legitimate repeated events (two identical purchases a second apart: do they need an event ID?); out-of-order versions (compare versions, not arrival order).

**Production considerations:** track the duplicate rate as a metric; enforce uniqueness in the target where the platform supports it; document the "keep first or keep latest" rule.

**Follow-up questions:** *SQL for deduplication?* `ROW_NUMBER() OVER (PARTITION BY key ORDER BY updated_at DESC) = 1`. *How do you dedupe a 1-TB table?* In the warehouse or Spark, partitioned by key.

---

### 21.4 Recovering from Partial Pipeline Failures

**Problem:** A job processing 30 partitions fails on partition 17. Some outputs are written, others are not.

**Recommended approach:**
- Make the **unit of work** small and independent (a partition, file or batch).
- Write each unit **atomically** (temp + rename, a transaction, a staging table + swap).
- Record a **checkpoint per unit after success** ([15.24](#1524-restartability-and-recovery)).
- On re-run, **skip completed units** and redo the failed ones. Each unit is idempotent, so redoing it is safe.
- Publish downstream only when **all** units succeed (a `_SUCCESS` marker, or a final "publish" task).

```text
for partition in partitions:
    if checkpoint.is_done(partition): continue
    write_to_staging(partition)                 # atomic per partition
    swap_into_target(partition)                 # overwrite = idempotent
    checkpoint.mark_done(partition)
publish_success_marker()
```

**Why it works:** failures are contained, and a re-run converges to the correct state without duplicates.

**Failure cases:** a checkpoint written before the data (data loss); non-atomic writes leaving half a partition; downstream consumers reading before the publish step.

**Production considerations:** orchestrator retries per task (Airflow task-level retries); alerting with the failing partition ID; a runbook for manual re-runs.

**Follow-up questions:** *What if the failure corrupted the target?* Restore from table time travel or snapshots, or rebuild the partition from the raw layer (the reason to keep raw data).

---

### 21.5 Designing an Idempotent Pipeline

**Problem:** "Design a daily pipeline that can be re-run any number of times for any date without duplicating data."

**Recommended approach:**
1. Parameterise everything by the **logical run date** (never `today()` inside the logic).
2. Use **deterministic outputs**: `.../dt=2026-10-29/` and fixed file names per partition.
3. **Overwrite partitions** (delete+insert in one transaction, `INSERT OVERWRITE`, or a dynamic partition overwrite) or **MERGE** by key.
4. Deduplicate inputs; track processed files by checksum.
5. Make side effects idempotent too: notifications with idempotency keys, API writes with request IDs.

```python
# A pure, date-parameterised path builder: the same input always gives the same output location
from datetime import date


def output_path(table: str, run_date: date) -> str:
    return f"s3://lake/curated/{table}/dt={run_date:%Y-%m-%d}/part-0000.parquet"


print(output_path("orders", date(2026, 10, 29)))
```

**Output:**

```text
s3://lake/curated/orders/dt=2026-10-29/part-0000.parquet
```

**Why it works:** the final state depends only on the input data and the run date, not on how many times or when the job ran.

**Failure cases:** appending to a table without keys; random file names (UUIDs) causing duplicates on re-runs; time-based logic that changes with the actual run time.

**Production considerations:** backfill tooling (`for day in date_range(...)`); concurrency control (two runs for the same date must not overlap: orchestrator `max_active_runs` or a lock).

**Follow-up questions:** *Exactly-once?* At-least-once processing + idempotent sinks = exactly-once results.

---

### 21.6 Reading Millions of Database Rows

**Problem:** Extract 50 million rows from PostgreSQL to Parquet without exhausting memory or overloading the database.

**Recommended approach:**
- Use a **server-side cursor** (`fetchmany` with named cursors) or **keyset pagination** (`WHERE id > :last ORDER BY id LIMIT :n`). Never `fetchall()`.
- Select **only the needed columns**; push filters into SQL.
- Write output **in batches** (e.g. one Parquet row group or file per N rows).
- Read from a **replica**, off-peak, with a `statement_timeout`.
- Parallelise by **key ranges** (several workers, each taking `id BETWEEN a AND b`), within the DB's connection limits.
- For very large or recurring extracts, prefer **database-native exports** (`COPY ... TO`, Snowflake `COPY INTO @stage`) or CDC.

**Why it works:** memory is bounded by the batch size; keyset pagination uses the index and stays fast at depth.

**Failure cases:** `OFFSET` pagination getting slower and inconsistent; a long-running transaction blocking vacuum or holding snapshots; a connection drop mid-extract (resume from the last key).

**Production considerations:** a checkpoint of the last extracted key; reconciling the source `COUNT(*)` with the rows written; monitoring the DB load; tagging the session (`application_name`).

**Follow-up questions:** *How do you handle rows changing during a long extract?* Use a consistent snapshot (`REPEATABLE READ`), or extract by watermark plus reconciliation.

---

### 21.7 Handling API Pagination and Rate Limits

**Problem:** Ingest 2 million records from a REST API that returns 500 records per page and allows 10 requests per second.

**Recommended approach:**
- Prefer **cursor** pagination; implement the loop with guards (max pages, repeated-cursor detection, [15.14](#1514-api-pagination)).
- Rate-limit with a **token bucket** ([15.18](#1518-rate-limiting)), slightly below the quota.
- On HTTP **429/503**, back off with jitter and honour `Retry-After`.
- Use **incremental** pulls (`updated_since=watermark`) instead of full pulls.
- Write each page (or group of pages) **incrementally** to storage, and checkpoint the cursor and watermark.
- Parallelise only across **independent partitions** (date ranges, accounts), and share the global rate limit.

**Why it works:** you stay within the quota, recover from throttling, and can resume after a crash.

**Failure cases:** expiring cursors (restart from the watermark); data changing during offset paging (duplicates or skips; deduplicate by ID); a quota shared with other consumers.

**Production considerations:** metrics for requests, 429s and latency; a timeout on every request; secrets from a vault; a contract with the API owner about limits.

**Follow-up questions:** *2M records at 500/page and 10 req/s: how long does it take?* 4,000 pages / 10 per second ≈ 400 seconds minimum, plus latency and backoff.

---

### 21.8 Retrying Transient Errors Without Duplicating Records

**Problem:** A batch write to the warehouse times out. Did it commit or not? Retrying might insert the rows twice.

**Recommended approach:**
- Make the write **idempotent**: `MERGE`/upsert on the business key, or delete+insert of the batch's partition in one transaction.
- Use a **batch ID / idempotency key**: record `batch_id` in a load-log table in the **same transaction** as the data; before retrying, check whether that `batch_id` is already committed.
- Retry only **transient** errors, with backoff ([8.8](#88-retry-handling)).

```python
import sqlite3
from contextlib import closing


def load_batch_once(conn: sqlite3.Connection, batch_id: str, rows: list[tuple[int, float]]) -> str:
    with conn:                                                   # data + load log commit together
        if conn.execute("SELECT 1 FROM load_log WHERE batch_id = ?", (batch_id,)).fetchone():
            return "skipped (already loaded)"
        conn.executemany("INSERT INTO sales (order_id, amount) VALUES (?, ?)", rows)
        conn.execute("INSERT INTO load_log (batch_id, row_count) VALUES (?, ?)", (batch_id, len(rows)))
    return "loaded"


with closing(sqlite3.connect(":memory:")) as conn:
    conn.executescript("CREATE TABLE sales (order_id INTEGER, amount REAL);"
                       "CREATE TABLE load_log (batch_id TEXT PRIMARY KEY, row_count INTEGER);")
    rows = [(1, 10.0), (2, 20.0)]
    print(load_batch_once(conn, "orders-2026-10-29-b0001", rows))
    print(load_batch_once(conn, "orders-2026-10-29-b0001", rows))     # the retry after an "unknown" outcome
    print(conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0])
```

**Output:**

```text
loaded
skipped (already loaded)
2
```

**Why it works:** the batch ID and the data commit atomically, so "did it commit?" has a definitive answer.

**Failure cases:** the batch ID is not deterministic (it must be derived from the input, e.g. `source_file + batch_number`, not a fresh UUID per attempt); the load log is in a different system from the data (not atomic, so you need upsert semantics instead).

**Production considerations:** keep the load-log table forever (it is also an audit trail); for warehouses without multi-statement transactions, use `MERGE` with the batch ID column.

**Follow-up questions:** *What about Kafka consumers?* Commit offsets **after** idempotent writes; or use transactional producers/consumers for exactly-once semantics within Kafka.

---

### 21.9 Tracking Watermarks

**Problem:** Design watermark tracking for 200 incremental tables.

**Recommended approach:**
- Store watermarks in a durable **state table**: `(pipeline, table, watermark_value, watermark_id, updated_at, run_id)`.
- Use a **compound** watermark `(updated_at, id)` to handle ties ([Problem 38](#problem-38-implement-an-incremental-extraction-using-a-watermark-advanced)).
- Advance it **only after** a successful load (atomically with the data when they are in the same database).
- Take the new watermark from the **data** (the max extracted value), not from the clock.
- Add a **lookback window** for late-committed rows; rely on upserts to absorb the overlap.
- Support **manual overrides** for backfills (start/end parameters that bypass the stored state).

**Why it works:** the state is explicit, durable and auditable; re-runs resume correctly.

**Failure cases:** clock skew and time zones (store UTC); a source that updates rows without bumping `updated_at`; deletes (not captured).

**Production considerations:** a dashboard of watermark lag per table (freshness SLAs); alerts when a watermark stops moving; access control on the state table.

**Follow-up questions:** *Watermarks in streaming?* There, "watermark" means event-time progress used to close windows. Same name, different concept: explain both.

---

### 21.10 Handling Schema Changes

**Problem:** A source adds, removes, renames or retypes columns without notice.

**Recommended approach:**
- **Validate the schema** at ingestion against an expected schema ([15.8](#158-schema-validation)).
- Use a **policy per change type**:
  - new nullable column → allow it (land it in raw; add it to curated after review, or evolve automatically);
  - removed or renamed required column → **fail fast**;
  - type widening (`int` → `bigint`) → allow; narrowing or incompatible change → fail.
- Land raw data in **schema-flexible** formats (JSON / raw tables) so nothing is lost while you adapt.
- Use formats and table layers that support **schema evolution** (Parquet with merge-schema, Delta/Iceberg, Avro with a schema registry).
- Agree on **data contracts** with the producers (versioned schemas, deprecation periods).

**Why it works:** expected evolution flows through; breaking changes are caught before they corrupt downstream tables.

**Failure cases:** positional CSV parsing (a new column shifts every value, so parse by header name); `SELECT *` in transforms propagating unexpected columns.

**Production considerations:** schema-drift alerts with a diff; versioned schema files in Git; a quarantine for files with unknown schemas.

**Follow-up questions:** *How do you backfill a new column for history?* Re-process the raw data for the affected partitions (another reason to keep raw).

---

### 21.11 Maintaining Audit Counts

**Problem:** The business asks you to prove that every record from the source reached the warehouse.

**Recommended approach:**
- Write an **audit record per run and per stage**: rows read, rejected, written; control totals (sum of amounts); watermark before and after; status; timings ([15.11](#1511-audit-logging)).
- Reconcile automatically: `read = written + rejected`, plus `source_count = target_count` per partition ([Problem 39](#problem-39-reconcile-source-and-target-record-counts-per-partition-medium)).
- Compute the source and target counts **in their own systems** (SQL aggregates), compare, and alert on differences.

**Why it works:** losses or duplicates appear as count mismatches immediately, with the run ID pointing to the cause.

**Failure cases:** counts taken at different times (the source keeps changing, so count within the same extraction window); filters that legitimately drop rows (record them as a separate "filtered" count).

**Production considerations:** keep the audit tables long-term; build dashboards and SLAs on them; include the file names and checksums for traceability.

**Follow-up questions:** *Counts match but the values are wrong?* Add control totals and row hashes.

---

### 21.12 Handling NULL versus Empty Strings

**Problem:** Source CSVs use `""`, `"NULL"`, `"N/A"` and `\N` inconsistently; some downstream reports treat empty strings as values.

**Recommended approach:**
- Agree on a **NULL convention per source** in configuration (a list of NULL tokens) and normalise at ingestion ([15.10](#1510-null-and-empty-string-handling)).
- Decide per column whether `""` is meaningful (e.g. an intentionally blank middle name) or missing.
- Trim whitespace before checking; keep `0` and `False` as values.
- When **writing** CSV, use an explicit NULL marker that the target loader understands (`NULL_IF` / `NULL AS '\N'` options in `COPY` commands).
- Use nullable dtypes in pandas (`string`, `Int64`), and `IS NULL` / `COALESCE` / `NULLIF` in SQL.

**Why it works:** one consistent meaning of "missing" across the pipeline; counts and joins behave predictably.

**Failure cases:** `str(None)` → `"None"`; `astype(str)` → `"nan"`; Oracle treating `''` as NULL; `NOT IN` with NULLs returning no rows.

**Production considerations:** NULL-rate metrics per column; tests for each token; documenting the convention in the data catalogue.

**Follow-up questions:** *Why does `COUNT(col)` differ from `COUNT(*)`?* `COUNT(col)` skips NULLs.

---

### 21.13 Avoiding the Small-File Problem

**Problem:** A streaming or hourly job writes thousands of tiny (KB-sized) Parquet files; queries and listings have become slow and expensive.

**Why it's a problem:** every file costs metadata operations, open/close overhead, task scheduling and per-request cloud charges. Engines like Spark, Athena and Trino are much more efficient with fewer, larger files (often 128 MB–1 GB).

**Recommended approach:**
- **Batch writes**: buffer records and write larger files less often; set the target file size or row-group size.
- **Repartition / coalesce** by the partition column before writing (Spark `repartition("dt")`).
- **Avoid over-partitioning** (e.g. by `dt` instead of `dt/hour/customer_id`); partitions should usually contain hundreds of MB.
- Run periodic **compaction**: rewrite a partition's small files into a few large ones (Delta `OPTIMIZE`, Iceberg `rewrite_data_files`, or a custom job), atomically.

```text
compact(partition):
    files = list_files(partition)
    if count(files) > threshold and avg_size(files) < 64 MB:
        data = read_all(files)
        write(data, staging_path, target_file_size=512 MB)
        atomically_swap(partition, staging_path)      # table formats do this transactionally
```

**Failure cases:** compaction racing with writers (use table formats with transactions, or compact only closed partitions); compaction changing the data (verify the counts before swapping).

**Production considerations:** monitor the file count and average size per partition; schedule compaction off-peak.

**Follow-up questions:** *How do you choose partition columns?* Columns used in filters, with moderate cardinality, giving partitions of reasonable size.

---

### 21.14 Designing Configuration-Driven Pipelines

**Problem:** You must onboard 50 similar feeds (CSV or JSON files → staging → curated tables) without writing 50 scripts.

**Recommended approach:**
- One **generic, tested engine** (extract → validate → transform → load) and one **config file per feed**: source location and format, schema, keys, load mode, transforms, quality checks, schedule ([15.19](#1519-configuration-driven-pipeline-design)).
- Validate **all configs at start-up** (dataclasses or pydantic), and in CI.
- Use a **registry of named transforms**; complex custom logic goes into code, referenced by name.
- Keep **environment differences** (paths, connections) out of feed configs: environment variables or per-environment overlays ([15.20](#1520-environment-based-configuration)).

**Why it works:** onboarding becomes a reviewed config change; the engine's tests cover every feed.

**Failure cases:** config growing into a programming language (conditions, loops in YAML); untested combinations of options; secrets in config files.

**Production considerations:** version configs in Git; generate orchestration DAGs from configs; a dry-run / validation command.

**Follow-up questions:** *How do you test it?* Unit-test the engine with sample configs; a CI job that validates every config and runs a smoke test on sample data.

---

### 21.15 Protecting Credentials

**Problem:** Pipelines need database passwords, API tokens and cloud access.

**Recommended approach ([15.23](#1523-secrets-management-principles)):**
- **No secrets in code, Git, config files, images or notebooks.** Scan repositories (pre-commit secret scanners).
- Prefer **identity-based auth**: IAM roles for compute, workload identity, key-pair/OAuth for warehouses.
- Store the rest in a **secrets manager**; fetch at run time or inject as environment variables; **rotate** them regularly.
- **Least privilege**, with separate credentials per pipeline and environment.
- **Redact** logs and exceptions; exclude secrets from `repr` and error messages.

**Why it works:** a leaked repository or log doesn't leak access; compromised credentials have a limited blast radius and lifetime.

**Failure cases:** secrets printed in debug logs or stack traces (connection strings); long-lived keys shared between teams; `.env` files committed by accident.

**Production considerations:** audit secret access; automatic rotation; break-glass procedures.

**Follow-up questions:** *A secret was committed to Git: what do you do?* Rotate it **immediately** (assume it is compromised), then remove it from the history and add scanning.

---

### 21.16 Improving Slow Python Transformation Code

**Problem:** A transformation over 5 million records takes 2 hours.

**Recommended approach:**
1. **Measure first:** `cProfile` / `py-spy` / timing per stage. Find the real bottleneck; don't guess.
2. Fix **algorithmic** problems: list membership inside loops → sets/dicts; nested-loop joins → hash joins; repeated work → caching.
3. Push work to **vectorised or native engines**: pandas/NumPy operations, Polars, DuckDB, or SQL in the warehouse.
4. **Reduce I/O**: read only the needed columns (Parquet), batch DB calls, stream instead of `read()`.
5. **Parallelise** only after that: processes for CPU, threads or async for I/O.
6. Avoid per-row overhead: logging every row, regex compilation in loops, string concatenation in loops.

```python
import time

valid_codes = [f"C{n:05d}" for n in range(5_000)]
records = [f"C{n:05d}" for n in range(0, 10_000, 2)]

started = time.perf_counter()
slow = [code for code in records if code in valid_codes]           # O(n*m): list membership
slow_seconds = time.perf_counter() - started

valid_set = set(valid_codes)
started = time.perf_counter()
fast = [code for code in records if code in valid_set]             # O(n): set membership
fast_seconds = time.perf_counter() - started
print(slow == fast, len(fast), fast_seconds * 20 < slow_seconds)
```

**Output:**

```text
True 2500 True
```

**Why it works:** most slow Python data code is slow because of complexity or per-row interpretation overhead, not because of Python startup or the GIL.

**Failure cases:** parallelising an O(n²) algorithm (it is still O(n²)); vectorising with `apply` (still a Python loop); premature micro-optimisation of a step that takes 1% of the time.

**Production considerations:** keep a performance regression test or benchmark on representative data; track the job duration over time.

**Follow-up questions:** *How do you profile?* `python -m cProfile -s cumtime job.py`, or `py-spy top --pid ...` for running processes; `tracemalloc` for memory.

---

### 21.17 Choosing Python, pandas or PySpark

**Problem:** "Which tool would you use for this workload, and why?"

| Workload | Good choice | Reason |
|---|---|---|
| API ingestion, file moves, orchestration glue, small transforms | **plain Python** | no heavy dependencies; streaming with generators; easy to test |
| Up to a few GB, single machine, rich transforms, quick delivery | **pandas** (or **Polars**) | vectorised, expressive; Polars is multi-core and lazy |
| SQL-style analytics on local or S3 Parquet files, medium to large | **DuckDB** | fast columnar SQL engine, no cluster needed |
| Tens of GB to TB+, large joins and aggregations, data growth expected | **PySpark** (or warehouse SQL) | distributed, fault-tolerant, scales horizontally |
| Data already in Snowflake / BigQuery / Redshift | **SQL in the warehouse (ELT, dbt)** | moves compute to the data; no extraction cost |
| Low-latency streams | Kafka consumers / Flink / Spark Structured Streaming | event-at-a-time or micro-batch processing |

**Decision factors to state explicitly:**
1. **Data size now and in 1–2 years** versus the memory of one machine (pandas needs ~3–10× the data size in RAM).
2. **Latency and SLA** (Spark's start-up overhead matters for small, frequent jobs).
3. **Where the data lives** (avoid moving data out of the warehouse just to transform it).
4. **Team skills and platform** (an existing Databricks or EMR cluster versus none).
5. **Cost** (a cluster for a 200 MB file is wasteful; a single huge VM for 5 TB is fragile).

**Example answer:** "For a 500 MB daily CSV with simple cleaning, I'd use pandas or Polars in a container, reading with explicit dtypes and writing Parquet. If it grew to 200 GB with joins against other large tables, I'd move it to Spark or to SQL in the warehouse, keeping the same validation rules in a shared library."

**Failure cases:** `toPandas()` / `collect()` on big Spark DataFrames (driver out-of-memory); pandas jobs that work in dev on samples and fail in prod on full data; Spark for tiny data (slow and expensive).

**Follow-up questions:** *What does Spark do that pandas can't?* Distributed execution, lazy optimisation (the Catalyst optimiser), fault tolerance through lineage, and processing beyond one machine's memory.

---

### Chapter 21 Review

**Key takeaways**
- Bound memory (streaming, chunking, partitioning) and push compute to the right engine.
- Make every write idempotent and every unit of work atomic; checkpoint after success.
- Quarantine bad data and fail above thresholds; reconcile and audit every run.
- Paginate safely, rate-limit, retry transient errors only, with idempotency keys.
- Treat schema, NULL conventions and credentials as explicit, reviewed contracts.
- Measure before optimising; fix complexity before parallelising.

**Frequently asked questions**

| Question | Short answer |
|---|---|
| How do you make a pipeline restartable? | Small idempotent units + durable checkpoints after success. |
| How do you prevent duplicates on retry? | Upserts/MERGE, partition overwrite, deterministic batch IDs recorded atomically. |
| How do you handle late data? | A lookback window plus idempotent upserts; reprocess the affected partitions. |
| How big should files be? | Usually 128 MB–1 GB for analytics engines; avoid many tiny files. |
| pandas or Spark? | It depends on data size versus memory, latency, location and cost. |

**Common traps:** checkpointing before writing; random output names; offset pagination on changing data; counts without control totals; secrets in logs.

**Practice exercise:** Write a one-page design for "ingest hourly JSON event files from S3 into a warehouse table, with deduplication, late data up to 48 hours, schema drift alerts and full auditability." Include the components, state stores, failure handling and monitoring.

---

## 22. Rapid Revision Material

### 22.1 Python Interview Cheat Sheet

```text
NAMES & OBJECTS   Variables are names bound to objects; assignment never copies.
                  == compares values, `is` compares identity (use only for None).
MUTABILITY        Mutable: list, dict, set, bytearray. Immutable: int, float, str, tuple, frozenset, bytes.
                  Hashable = immutable all the way down -> can be a dict key / set member.
ARGUMENTS         Pass-by-object-reference: mutation visible to the caller, rebinding is not.
                  Defaults are evaluated ONCE: never use a mutable default (use None).
TRUTHINESS        Falsy: None, False, 0, 0.0, "", [], {}, set(), range(0). Check data with `is None`.
COPIES            copy.copy = shallow (shares nested objects); copy.deepcopy = full copy.
STRINGS           Immutable; build with "".join(parts); always pass encoding="utf-8".
COMPREHENSIONS    [f(x) for x in xs if cond]   |   [a if c else b for x in xs]   |   (lazy generator)
GENERATORS        yield = pause + resume; lazy; single pass; constant memory for streams.
DECORATORS        @d == f = d(f); use functools.wraps; with arguments -> factory -> decorator -> wrapper.
CONTEXT MANAGERS  with = guaranteed cleanup (__enter__/__exit__ or @contextmanager + try/finally).
EXCEPTIONS        Catch specific; raise ... from err; log once; never bare except / except: pass.
OOP               @classmethod alt constructors; @staticmethod helpers; super() follows the MRO;
                  composition > inheritance; define __hash__ with __eq__; dataclasses for records.
CONCURRENCY       GIL: threads/asyncio for I/O, processes for CPU; always call future.result().
FILES             with open(..., encoding=, newline="" for csv); stream lines; atomic write = temp + os.replace.
DATABASES         Parameterised SQL only; commit/rollback; executemany/COPY; fetchmany/server cursors.
DATA ENGINEERING  Idempotent writes, watermarks (updated_at, id), checkpoints after success,
                  quarantine + thresholds, reconcile counts AND totals, audit every run.
DATES             Aware UTC internally; zoneinfo for local logic; pass the logical run date in.
MONEY             decimal.Decimal("19.99") or integer cents; quantize with a named rounding mode.
```

---

### 22.2 Data Structure Comparison Summary

| Structure | Ordered | Mutable | Duplicates | Lookup | Best for |
|---|---|---|---|---|---|
| `list` | Yes | Yes | Yes | O(n) search, O(1) index | ordered batches, results |
| `tuple` | Yes | No | Yes | O(n) search, O(1) index | fixed records, composite keys |
| `set` | No | Yes | No | **O(1)** | membership, dedupe, diffs |
| `frozenset` | No | No | No | O(1) | hashable sets (as keys) |
| `dict` | Yes (insertion) | Yes | Keys unique | **O(1)** by key | records, lookups, grouping, joins |
| `collections.deque` | Yes | Yes | Yes | O(1) at the ends | queues, sliding windows |
| `collections.Counter` | Yes | Yes | Keys unique | O(1) | frequencies, top-N |
| `collections.defaultdict` | Yes | Yes | Keys unique | O(1) | grouping without key checks |
| `heapq` (on a list) | Heap order | Yes | Yes | O(1) min, O(log n) push/pop | top-N, priority queues |
| `namedtuple` / `NamedTuple` | Yes | No | Yes | by field name | lightweight immutable rows |
| `dataclass` | – | Configurable | – | by attribute | typed records, configs |
| generator | Sequential | – | – | single pass | streaming large data |

---

### 22.3 Complexity Summary

| Operation | Average time |
|---|---|
| `list[i]`, `list.append`, `list.pop()` | O(1) (append amortised) |
| `list.insert(0, x)`, `list.pop(0)`, `x in list`, `list.remove(x)` | O(n) |
| `list.sort()` / `sorted()` (Timsort, stable) | O(n log n) |
| `dict[k]`, `dict[k] = v`, `k in dict`, `del dict[k]` | O(1) |
| `set.add`, `x in set`, `set.remove` | O(1) |
| `s \| t` / `s & t` / `s - t` | O(len(s) + len(t)) / O(min(len(s), len(t))) / O(len(s)) |
| `deque.append/appendleft/pop/popleft` | O(1) |
| `heapq.heappush/heappop` | O(log n) |
| `heapq.nlargest(k, xs)` | O(n log k) |
| `bisect.bisect_left` on a sorted list | O(log n) |
| `"".join(parts)` | O(total length) |
| `str + str` in a loop | up to O(n²) total |
| Hash join of n and m rows | O(n + m) |
| Nested-loop join | O(n × m) |

**Space:** list/dict/set O(n); generators O(1) state; a recursion depth of d uses O(d) stack frames (default limit ~1000).

---

### 22.4 Common Built-in Functions Summary

| Function | Purpose | Example |
|---|---|---|
| `len(x)` | size | `len(rows)` |
| `range(start, stop, step)` | lazy integer sequence | `range(0, 10, 2)` |
| `enumerate(it, start=0)` | index + item | `for line_no, line in enumerate(f, 1)` |
| `zip(*its, strict=False)` | parallel iteration | `dict(zip(header, row))` |
| `map(f, it)` / `filter(f, it)` | lazy transform / select | `filter(None, values)` |
| `sorted(it, key=, reverse=)` | new sorted list | `sorted(rows, key=itemgetter("ts"))` |
| `reversed(seq)` | reverse iterator | `reversed(items)` |
| `min/max(it, key=, default=)` | extremes | `max(rows, key=len, default=None)` |
| `sum(it, start=0)` | total | `sum(r["amount"] for r in rows)` |
| `any(it)` / `all(it)` | short-circuit tests | `all(v is not None for v in row.values())` |
| `iter(x)` / `next(it, default)` | the iterator protocol | `next(reader, None)` |
| `isinstance(x, types)` | type check (with subclasses) | `isinstance(v, (int, float))` |
| `type(x)`, `id(x)`, `hash(x)` | exact class, identity, hash | |
| `getattr/setattr/hasattr` | dynamic attributes | `getattr(module, name)` |
| `round(x, n)` | round half to even | `round(2.5) == 2` |
| `divmod(a, b)`, `abs`, `pow(a, b, mod)` | arithmetic | `divmod(125, 60)` |
| `int/float/str/bool/list/dict/set/tuple` | conversion | `int("42")` |
| `repr(x)` / `str(x)` / `format(x, spec)` | text representations | `format(0.25, ".1%")` |
| `open(path, mode, encoding=, newline=)` | file I/O | |
| `print(*args, sep=, end=, file=)` | output | `print(msg, file=sys.stderr)` |
| `vars(obj)`, `dir(obj)`, `callable(obj)` | introspection | |
| `ord(c)` / `chr(n)` | code point ↔ character | `ord("é") == 233` |

---

### 22.5 Common Exception Types

| Exception | Typical cause | Data Engineering example |
|---|---|---|
| `ValueError` | right type, wrong value | `int("abc")`, `date.fromisoformat("2026-02-30")` |
| `TypeError` | wrong type / wrong call | `"5" + 5`, a missing argument, `None` comparison in a sort |
| `KeyError` | missing dict key | `row["amount"]` when the column is absent |
| `IndexError` | sequence index out of range | `row[5]` on a short CSV row |
| `AttributeError` | missing attribute | calling `.strip()` on `None` |
| `NameError` / `UnboundLocalError` | undefined or not-yet-assigned name | a typo; assigning a global without `global` |
| `ZeroDivisionError` | division by zero | the average of an empty group |
| `FileNotFoundError` / `PermissionError` / `IsADirectoryError` | file system | a missing input; no access |
| `FileExistsError` | `"x"` mode or `mkdir` without `exist_ok` | protecting outputs |
| `UnicodeDecodeError` | wrong encoding | a cp1252 file read as UTF-8 |
| `json.JSONDecodeError` (a `ValueError`) | invalid JSON | a truncated API response |
| `csv.Error` | malformed CSV | an unterminated quote, a field larger than the limit |
| `ConnectionError` / `TimeoutError` (`OSError`) | network | API or DB connectivity (retry these) |
| `StopIteration` | iterator exhausted | `next(it)` without a default |
| `RecursionError` | too-deep recursion | deeply nested JSON |
| `MemoryError` | out of memory | `read()` on a huge file |
| `ImportError` / `ModuleNotFoundError` | missing package, shadowing, circular import | an environment problem |
| `NotImplementedError` | an abstract method not implemented | base-class hooks |
| `AssertionError` | a failed `assert` | tests (not input validation) |
| `KeyboardInterrupt` / `SystemExit` | Ctrl+C / `sys.exit()` | must not be swallowed |
| `ExceptionGroup` (3.11+) | several concurrent failures | `asyncio.TaskGroup` |
| `sqlite3.IntegrityError` / driver `IntegrityError` | constraint violation | a duplicate primary key |
| `sqlite3.OperationalError` / driver `OperationalError` | DB operational problem | locked database, connection lost, deadlock |

---

### 22.6 Important Library Summary

| Library | One-line purpose | Key APIs |
|---|---|---|
| `os` | environment and OS interaction | `environ`, `getenv`, `walk`, `replace`, `makedirs` |
| `sys` | interpreter interaction | `argv`, `exit`, `path`, `stdout`, `version_info` |
| `argparse` | command-line arguments | `ArgumentParser`, `add_argument`, `parse_args` |
| `pathlib` | object-oriented paths | `Path`, `/`, `glob`, `rglob`, `read_text`, `stat` |
| `shutil` | high-level file operations | `copy2`, `move`, `rmtree`, `make_archive`, `disk_usage` |
| `glob` | wildcard file matching | `glob`, `iglob`, `recursive=True` |
| `tempfile` | safe temporary files and folders | `TemporaryDirectory`, `NamedTemporaryFile`, `mkstemp` |
| `re` | regular expressions | `compile`, `fullmatch`, `search`, `findall`, `sub`, named groups |
| `json` | JSON | `loads`, `dumps(default=)`, `load`, `dump`, JSON Lines |
| `csv` | delimited files | `reader`, `DictReader`, `writer`, `DictWriter`, `Sniffer` |
| `gzip` / `bz2` / `zipfile` | compression | `gzip.open("rt")`, `ZipFile.open` |
| `datetime` | dates and times | `datetime.now(timezone.utc)`, `strptime`, `fromisoformat`, `timedelta` |
| `zoneinfo` | IANA time zones | `ZoneInfo("America/New_York")` (+ `tzdata` on Windows) |
| `calendar` | calendar helpers | `monthrange` |
| `decimal` | exact decimal arithmetic | `Decimal("1.10")`, `quantize`, `ROUND_HALF_UP` |
| `hashlib` / `hmac` | hashes and signatures | `sha256`, `md5`, `hmac.new`, `compare_digest` |
| `secrets` | cryptographically secure tokens | `token_urlsafe` |
| `logging` | logging | `getLogger(__name__)`, `dictConfig`, `LoggerAdapter`, `exception` |
| `collections` | specialised containers | `Counter`, `defaultdict`, `deque`, `namedtuple`, `OrderedDict`, `ChainMap` |
| `itertools` | iterator tools | `islice`, `chain`, `groupby`, `accumulate`, `pairwise`, `batched` |
| `functools` | function tools | `lru_cache`, `cache`, `partial`, `reduce`, `wraps`, `singledispatch` |
| `operator` | function versions of operators | `itemgetter`, `attrgetter`, `methodcaller` |
| `typing` | type hints | `Protocol`, `TypedDict`, `Literal`, `Callable`, `Iterator`, `TypeVar` |
| `dataclasses` | record classes | `dataclass`, `field`, `asdict`, `replace` |
| `concurrent.futures` | pools | `ThreadPoolExecutor`, `ProcessPoolExecutor`, `as_completed` |
| `asyncio` | async I/O | `run`, `gather`, `TaskGroup`, `Semaphore`, `timeout` |
| `sqlite3` | embedded SQL database (DB-API) | `connect`, `execute`, `executemany`, transactions |
| `unittest` / `unittest.mock` | tests and mocks | `TestCase`, `Mock`, `patch`, `side_effect` |
| `requests` (3rd party) | HTTP client | `Session`, `get(timeout=)`, `raise_for_status`, `iter_content` |
| `pandas` (3rd party) | DataFrames | `read_csv`, `merge`, `groupby`, `to_parquet` |
| `numpy` (3rd party) | arrays | vectorisation, `where`, broadcasting |
| `pytest` (3rd party) | testing | fixtures, `parametrize`, `raises`, `tmp_path`, `monkeypatch` |
| `pyarrow` (3rd party) | Arrow / Parquet | `parquet.read_table`, `ParquetFile.iter_batches` |

---

### 22.7 Top Python Data Engineer Interview Questions

**Core Python**
1. **List vs tuple?** A list is mutable; a tuple is immutable and hashable (if its items are), so it can be a dict key.
2. **`==` vs `is`?** Value equality vs object identity; use `is` only for `None`.
3. **What is the mutable default argument problem?** Defaults are evaluated once at definition, so a `[]` default is shared across calls; use `None`.
4. **Shallow vs deep copy?** A shallow copy shares nested objects; `deepcopy` copies recursively.
5. **How are arguments passed?** By object reference: mutations are visible, rebinding is not.
6. **What is the GIL?** A CPython lock that lets one thread execute bytecode at a time; it is released during I/O.
7. **Iterator vs generator?** A generator is a convenient iterator created with `yield`; both are lazy and single-pass.
8. **What does a decorator do?** It wraps a function to add behaviour; `@d` means `f = d(f)`.
9. **What is a context manager?** An object with `__enter__`/`__exit__` that guarantees setup and cleanup in a `with` block.
10. **`@staticmethod` vs `@classmethod`?** No implicit argument vs receives `cls` (alternative constructors, subclass-aware).
11. **`__str__` vs `__repr__`?** User-friendly vs unambiguous developer representation.
12. **What is MRO?** The C3-linearised order in which classes are searched for attributes; `super()` follows it.
13. **Why define `__hash__` with `__eq__`?** Equal objects must have equal hashes; defining `__eq__` alone makes instances unhashable.
14. **What is a closure?** An inner function that remembers variables from its enclosing scope.
15. **Explain LEGB.** Local → Enclosing → Global → Built-in name lookup.
16. **EAFP vs LBYL?** Try and handle the failure vs check first; EAFP is idiomatic and avoids races.
17. **What is `if __name__ == "__main__":` for?** Run code only when executed as a script (also required for multiprocessing on spawn platforms).
18. **How does Python manage memory?** Reference counting + a cyclic garbage collector + the pymalloc allocator.

**Data processing**
19. **How do you process a file larger than memory?** Stream or chunk it; keep combinable aggregates; partition to disk; or use DuckDB/Spark.
20. **How do you remove duplicates while keeping order?** `list(dict.fromkeys(items))`, or a seen-set loop.
21. **How do you find the top-N frequent items?** `Counter.most_common(n)` or `heapq.nlargest`.
22. **How do you join two datasets in plain Python?** A hash join: build a dict from the smaller dataset and probe it with the larger.
23. **How do you flatten nested JSON?** Recursive traversal that builds dotted key paths (handle lists, collisions, depth).
24. **Why `newline=""` for the csv module?** The csv module handles line endings itself; translation breaks quoted newlines.
25. **How do you handle NULL vs empty strings?** An agreed list of NULL tokens per source, normalised at ingestion; `is None` checks.
26. **Why not `float` for money?** Binary floating point can't represent most decimal fractions exactly; use `Decimal` or integer cents.
27. **Naive vs aware datetime?** Without vs with time zone; store aware UTC and pass the logical run date in.
28. **pandas: `loc` vs `iloc`?** Labels (inclusive slices) vs positions (exclusive slices).
29. **Why avoid `iterrows`?** It runs Python per row; vectorised operations run in C and are much faster.
30. **When would you choose Spark over pandas?** When the data exceeds one machine's memory, needs distributed joins, or must scale with growth.

**Pipelines and production**
31. **What is idempotency and how do you achieve it?** Same result for repeated runs: deterministic paths, partition overwrite, MERGE/upsert, batch IDs.
32. **Full vs incremental load?** Reload everything vs only the changes (watermarks/CDC); incremental needs a plan for deletes and late data.
33. **How do you track a watermark safely?** Compound `(updated_at, id)`, taken from the data, persisted after a successful load, with a lookback window.
34. **What is CDC?** Change Data Capture: a stream of inserts, updates and deletes, applied in order per key and idempotently.
35. **How do you retry safely?** Transient errors only, exponential backoff + jitter, capped attempts, idempotent operations.
36. **How do you handle API pagination and rate limits?** Cursor loops with guards, a token bucket, backoff on 429 honouring `Retry-After`, checkpoints.
37. **How do you prevent SQL injection?** Parameterised queries; allowlisted identifiers; least privilege.
38. **How do you read millions of rows from a database?** Server-side cursors / `fetchmany` / keyset pagination; write in batches.
39. **How do you validate data quality?** Schema checks + rule checks (not-null, unique, ranges, referential, freshness, volume) with severities.
40. **How do you prove nothing was lost?** Audit records and reconciliation of counts, control totals and keys between source and target.
41. **How do you manage secrets?** A secrets manager or IAM roles, never in code or logs, with rotation and least privilege.
42. **How do you test ETL code?** Pure transforms with unit tests (pytest, parametrised edge cases), integration tests with real services, data tests at run time.
43. **Threads, processes or asyncio for 5,000 API calls?** asyncio (or a thread pool) with a concurrency limit and a rate limit; processes are for CPU work.
44. **What is the small-file problem?** Too many tiny files hurt metadata and scan performance; batch writes and compact them.
45. **How do you handle schema drift?** Validate against an expected schema; allow additive changes, fail on breaking ones; use data contracts.

---

### 22.8 Last-Minute Revision Checklist

- [ ] I can explain mutable vs immutable, hashability, `is` vs `==`, and shallow vs deep copy with examples.
- [ ] I know the mutable-default pitfall, late-binding closures and `UnboundLocalError`.
- [ ] I can write list/dict/set comprehensions and generator expressions, and know when not to.
- [ ] I can write a generator pipeline with batching (`islice`), and explain laziness and single-pass behaviour.
- [ ] I can write a decorator with arguments (retry) using `functools.wraps`.
- [ ] I can write a context manager with a class and with `@contextmanager`.
- [ ] I can explain the GIL and choose threads vs processes vs asyncio.
- [ ] I know the complexities of list/dict/set operations and can replace O(n²) code with dict/set lookups.
- [ ] I can solve: dedupe preserving order, top-N frequency, two-sum, merge intervals, group by, hash join, flatten JSON, latest-per-key, moving average, LRU cache.
- [ ] I can read and write CSV/JSON/JSON Lines correctly (encoding, `newline=""`, NULL handling) and write files atomically.
- [ ] I can write parameterised SQL, manage transactions, batch inserts and stream large results.
- [ ] I can design an incremental, idempotent, restartable pipeline with watermarks, checkpoints, audit and reconciliation.
- [ ] I can handle dates in UTC and local time zones, and do month arithmetic correctly.
- [ ] I can test with pytest fixtures, parametrisation and mocks.
- [ ] I can discuss pandas vs PySpark trade-offs and pandas performance and memory techniques.

---

### 22.9 Production-Readiness Checklist (Short Form)

The detailed version is in [18.14](#1814-production-readiness-checklist).

1. **Correct** – tests, data-quality checks, reconciliation.
2. **Idempotent** – safe re-runs and backfills; deterministic outputs.
3. **Restartable** – small units, checkpoints after success, atomic writes.
4. **Resilient** – timeouts, bounded retries with backoff, failure thresholds.
5. **Observable** – structured logs with a run ID, audit tables, metrics, actionable alerts, non-zero exit codes.
6. **Secure** – no secrets in code or logs, least privilege, parameterised SQL, safe deserialisation.
7. **Efficient** – streaming/chunking, the right engine, sensible file sizes, measured performance.
8. **Maintainable** – pinned dependencies, linting/typing/formatting in CI, config-driven where useful, documented assumptions.

---

### 22.10 Practice Assignments

Work through these in order. Each one combines several chapters. Suggested acceptance criteria are given so you can check your own solution.

**Assignment 1 – String and collection warm-up (Chapters 2–4)**
Write `profile_column(values)` that returns the count, null count (None or blank), distinct count, the top 3 values with counts, and the min/max length of the non-null values.
*Check:* `profile_column(["a", "", None, "bb", "a"])` → count 5, nulls 2, distinct 2, top `[('a', 2), ('bb', 1)]`, min length 1, max length 2.

**Assignment 2 – Generator pipeline (Chapter 6)**
Stream a large JSON Lines file, skip malformed lines (count them), keep events of type `"purchase"`, and yield batches of 500 parsed events.
*Check:* memory stays flat for a 1 GB file; `malformed + purchases + others == total lines`.

**Assignment 3 – Decorators and context managers (Chapter 11)**
Implement `@retry` (transient exceptions only, exponential backoff, injectable sleep) and `audit_run(run_id)` (a context manager that records start, end, status and error).
*Check:* a function failing twice then succeeding records two sleeps; an exception inside `audit_run` is recorded **and** re-raised.

**Assignment 4 – File ingestion (Chapters 9, 15)**
Build an ingestion job for a landing folder: checksum-based duplicate detection, header validation, row validation with a rejects file, a 2% reject threshold, an atomic output write, an archive/quarantine move and an audit JSON per file.
*Check:* re-running the job changes nothing; a file with a bad header goes to quarantine; the audit counts reconcile.

**Assignment 5 – Incremental database extraction (Chapter 14)**
Using SQLite, implement batched incremental extraction from `source_orders` to `target_orders` with a compound watermark, upserts and an `etl_audit` table. Simulate a crash after the second batch.
*Check:* after a restart, the target equals the source exactly; the watermark never moves backwards; no duplicates.

**Assignment 6 – Concurrency (Chapter 13)**
Download (simulate with `sleep`) 200 "files" using a thread pool with at most 10 workers and a 20-requests-per-second token bucket; parse each one in a process pool; collect failures without stopping the others.
*Check:* the total time is close to the rate-limit bound; failures are listed with their keys; the exit code is non-zero if any failed.

**Assignment 7 – pandas transformation (Chapter 17)**
From `orders` and `customers` DataFrames, compute daily revenue per country in each customer's local time zone, flag orphan orders, and output the top 3 days per country as Parquet.
*Check:* `merge(validate="many_to_one")` passes; orphans are counted; the output dtypes are explicit.

**Assignment 8 – Testing (Chapter 18)**
Write pytest tests for Assignments 3–5: fixtures for temporary folders and an in-memory DB, parametrised edge cases (NULLs, zero, duplicates, time-zone boundaries) and mocks for the clock and the network.
*Check:* the tests run in under 5 seconds with no network access.

**Assignment 9 – System design (Chapters 15, 19, 21)**
Write a one-page design for a config-driven framework that onboards a new CSV feed by adding a YAML file: components, interfaces (Source, Sink, Validator), state stores (watermarks, manifests, audit), failure handling, monitoring and how you would test it.
*Check:* every scenario in Chapter 21 is addressed by some part of the design.

---

**You have reached the end of the handbook.** Revisit the Chapter Review sections regularly, re-solve the Chapter 20 problems from memory, and practise explaining the Chapter 21 scenarios out loud. Interviewers value clear reasoning about trade-offs as much as correct code.
