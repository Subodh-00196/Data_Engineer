## 1. Core Concepts Interviewers Probe

| Concept | Key point |
|---|---|
| Mutable vs immutable | Mutable: `list`, `dict`, `set`. Immutable: `int`, `float`, `str`, `tuple`, `frozenset`. Only hashable (immutable) objects can be dict keys / set members. |
| `is` vs `==` | `==` compares values; `is` compares identity (same object). Use `is` only for `None`. |
| Pass-by-object-reference | Functions receive a reference. Mutating a list inside a function changes the caller's list; reassigning the name does not. |
| Shallow vs deep copy | `copy.copy(x)` / `x[:]` copies the outer container only; `copy.deepcopy(x)` copies nested objects too. |
| Truthiness | `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None` are falsy. |
| GIL | CPython runs one thread of Python bytecode at a time → threads help **I/O-bound** work (API calls, S3); use **multiprocessing** for CPU-bound work. |
| Memory | Generators and iterators process data lazily → constant memory for large files. |

```python
import copy
a = [[1, 2], [3]]
b = copy.copy(a);  b[0].append(9)   # a is changed too → [[1, 2, 9], [3]]
c = copy.deepcopy(a); c[0].append(7) # a unchanged
```

**Mutable default argument pitfall (very common):**
```python
def add(item, bucket=[]):      # BAD – same list reused across calls
    bucket.append(item); return bucket

def add(item, bucket=None):    # GOOD
    bucket = [] if bucket is None else bucket
    bucket.append(item); return bucket
```

---

## 2. Built-in Collections

### Complexity cheat sheet
| Operation | list | dict / set |
|---|---|---|
| Index / lookup by key | O(1) | O(1) average |
| `x in` | O(n) | O(1) average |
| Append / add | O(1) amortized | O(1) average |
| Insert/delete at front | O(n) | – |
| Sort | O(n log n) (Timsort, stable) | – |

Use a **set/dict for membership checks**, not a list.

### List
```python
nums = [3, 1, 4, 1, 5]
nums.append(9); nums.extend([2, 6]); nums.insert(0, 0)
nums.remove(1)        # removes first 1
last = nums.pop()     # removes last; pop(0) is O(n) → use deque
nums.sort()           # in place, returns None
ordered = sorted(nums, reverse=True)   # new list
first3, last3 = nums[:3], nums[-3:]
```

### Dict
```python
d = {'a': 1, 'b': 2}
d.get('z', 0)                    # default instead of KeyError
d.setdefault('c', []).append(5)  # create if missing
merged = d | {'b': 20}           # 3.9+, right side wins
for k, v in d.items(): ...
by_value = dict(sorted(d.items(), key=lambda kv: kv[1], reverse=True))
```
Dicts keep insertion order (guaranteed since 3.7).

### Set and tuple
```python
s1, s2 = {1, 2, 3}, {3, 4}
s1 | s2, s1 & s2, s1 - s2, s1 ^ s2     # union, intersection, difference, symmetric diff

point = (10, 20)                        # immutable, hashable → usable as dict key
x, y = point                            # unpacking
first, *rest = [1, 2, 3, 4]             # first=1, rest=[2, 3, 4]
```

### `collections` module
```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

Counter("mississippi").most_common(2)      # [('i', 4), ('s', 4)]

groups = defaultdict(list)                 # no KeyError on first access
for dept, name in [('IT', 'A'), ('HR', 'B'), ('IT', 'C')]:
    groups[dept].append(name)              # {'IT': ['A', 'C'], 'HR': ['B']}

q = deque(maxlen=3)                        # O(1) append/pop at both ends
q.extend([1, 2, 3, 4])                     # deque([2, 3, 4]) – keeps last 3

Row = namedtuple('Row', 'id name')
r = Row(1, 'Alice'); r.name                # readable, immutable record

od = OrderedDict(a=1, b=2); od.move_to_end('a')   # move_to_end/popitem(last=False) → LRU cache (section 16)
```

`heapq` – top-N without sorting everything:
```python
import heapq
heapq.nlargest(3, [5, 1, 9, 7, 3])                 # [9, 7, 5]
heapq.nsmallest(2, rows, key=lambda r: r['ts'])   # works with key
```

### dataclasses (clean record classes)
```python
from dataclasses import dataclass, field

@dataclass(frozen=True)          # frozen → immutable & hashable
class Order:
    order_id: int
    amount: float
    tags: list = field(default_factory=list)   # never use a mutable literal default
```

---

## 3. Strings

```python
s = "  Hello, World  "
s.strip().lower().replace(',', '')
"a,b,,c".split(',')            # ['a', 'b', '', 'c']
'-'.join(['2026', '10', '29']) # build strings with join, not += in a loop (O(n²))
f"{3.14159:.2f} | {42:05d} | {'x':>5}"   # '3.14 | 00042 |     x'
s[::-1]                        # reverse
"abc".startswith('a'), "42".isdigit(), "ab1".isalnum()
```

Common problems:
```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def are_anagrams(a, b):
    return Counter(a.lower()) == Counter(b.lower())      # O(n) vs sorted O(n log n)

def first_non_repeating(s):
    counts = Counter(s)
    return next((c for c in s if counts[c] == 1), None)

def compress(s):                                          # "aabcccccaaa" → "a2b1c5a3"
    from itertools import groupby
    out = ''.join(f"{ch}{len(list(g))}" for ch, g in groupby(s))
    return out if len(out) < len(s) else s

def longest_unique_substring(s):                          # sliding window, O(n)
    last, left, best = {}, 0, 0
    for right, ch in enumerate(s):
        if last.get(ch, -1) >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

### Regular expressions
```python
import re
text = "Call 123-456-7890 or 987-654-3210"
re.findall(r'\d{3}-\d{3}-\d{4}', text)                 # all phone numbers
re.sub(r'\d(?=\d{4})', '*', "4111111111111111")        # mask all but last 4 digits
m = re.search(r'(\d{3})-(\d{3})-(\d{4})', text); m.group(1) if m else None
re.split(r'[,\s]+', "apple, banana  orange")           # ['apple', 'banana', 'orange']
LOG = re.compile(r'(?P<ts>\S+) (?P<level>INFO|ERROR) (?P<msg>.*)')   # compile once, reuse
```
`re.match` checks only the start of the string; `re.search` scans anywhere; `re.fullmatch` requires the whole string.

---

## 4. Comprehensions and Functional Tools

```python
squares   = [x * x for x in range(10)]
evens     = [x for x in range(20) if x % 2 == 0]
labels    = ['even' if x % 2 == 0 else 'odd' for x in range(5)]   # if/else goes before for
flat      = [x for row in [[1, 2], [3, 4]] for x in row]           # [1, 2, 3, 4]
inv       = {v: k for k, v in {'a': 1, 'b': 2}.items()}            # dict comprehension
uniq_len  = {len(w) for w in ['a', 'bb', 'cc']}                    # set comprehension
total     = sum(x * x for x in range(10**6))                       # generator: no big list
```
Prefer comprehensions over `map`/`filter` + `lambda` for readability; keep them to one level of nesting.

```python
from functools import reduce
list(map(str.upper, ['a', 'b']))               # ['A', 'B']
list(filter(None, [0, 1, '', 'x']))            # [1, 'x'] – removes falsy
reduce(lambda acc, x: acc * x, [1, 2, 3, 4])   # 24
list(zip(['a', 'b'], [1, 2]))                  # [('a', 1), ('b', 2)] – stops at shortest
names, scores = zip(*[('a', 1), ('b', 2)])     # unzip
all(x > 0 for x in [1, 2]), any(x < 0 for x in [1, -2])
for i, v in enumerate(['x', 'y'], start=1): ...
sorted(rows, key=lambda r: (r['dept'], -r['salary']))   # multi-key sort
```

`itertools` highlights:
```python
from itertools import chain, islice, groupby, product, combinations, accumulate
list(chain([1, 2], [3]))                 # [1, 2, 3]
list(islice(huge_generator(), 5))        # first 5 items lazily
list(accumulate([1, 2, 3]))              # running total [1, 3, 6]
list(combinations('abc', 2))             # [('a','b'), ('a','c'), ('b','c')]
# groupby only groups CONSECUTIVE equal keys → sort by the key first
for k, grp in groupby(sorted(data, key=lambda r: r['k']), key=lambda r: r['k']): ...
```

---

## 5. Functions

```python
def load(path, *args, sep=',', **kwargs):   # positional, *args tuple, keyword-only sep, **kwargs dict
    ...
load('a.csv', 1, 2, sep='|', encoding='utf-8')

def f(a, b, /, c, *, d): ...   # a, b positional-only; d keyword-only
```

- **First-class functions:** can be passed, returned, stored in dicts.
- **Closures:** an inner function remembers variables of the enclosing scope.
- **Scope (LEGB):** Local → Enclosing → Global → Built-in. Use `nonlocal` / `global` to rebind.
- **Type hints** document intent; not enforced at runtime.

```python
def make_multiplier(n):
    def multiply(x):
        return x * n          # n captured by the closure
    return multiply
double = make_multiplier(2); double(5)   # 10

def counter():
    count = 0
    def inc():
        nonlocal count; count += 1; return count
    return inc
```

Memoization – use the standard library, not a mutable default dict:
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```
Recursion: Python's default limit is ~1000 frames and there is no tail-call optimization – prefer iteration for deep inputs.

---

## 6. Iterators and Generators

- **Iterable:** has `__iter__` (list, dict, file, generator).
- **Iterator:** has `__next__`; raises `StopIteration` when done; can be consumed **only once**.
- **Generator:** a function with `yield` – an easy way to build an iterator. Values are produced lazily, so memory stays constant.

```python
class CountUp:                         # custom iterator
    def __init__(self, start, end):
        self.cur, self.end = start, end
    def __iter__(self):
        return self
    def __next__(self):
        if self.cur >= self.end:
            raise StopIteration
        self.cur += 1
        return self.cur - 1

def read_lines(path):                  # generator: file of any size
    with open(path, encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\n')

def chunked(iterable, size):           # batch records for bulk inserts / API calls
    it = iter(iterable)
    while batch := list(islice(it, size)):
        yield batch

# Generator pipeline: each stage processes one record at a time
lines   = read_lines('events.log')
errors  = (l for l in lines if 'ERROR' in l)
parsed  = (l.split('|') for l in errors)
for batch in chunked(parsed, 1000):
    ...   # write batch
```
Gotcha: a generator is exhausted after one pass – `list(gen)` twice returns `[]` the second time.
`yield from sub_gen()` delegates to another generator.

---

## 7. Decorators

A decorator takes a function and returns a new function that adds behaviour (logging, timing, retries, auth). Always use `functools.wraps` to keep the original name/docstring.

```python
import functools, time, logging

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            logging.info("%s took %.2fs", func.__name__, time.perf_counter() - start)
    return wrapper

def retry(times=3, delay=1, exceptions=(Exception,)):   # decorator with arguments → 3 levels
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == times:
                        raise
                    time.sleep(delay * 2 ** (attempt - 1))   # exponential backoff
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
@timer
def fetch_page(url): ...
```
Stacked decorators apply bottom-up: `fetch_page = retry(...)(timer(fetch_page))`.

---

## 8. Context Managers

`with` guarantees cleanup (close files, release connections, commit/rollback) even when an exception occurs.

```python
class DBTransaction:
    def __init__(self, conn):
        self.conn = conn
    def __enter__(self):
        return self.conn.cursor()
    def __exit__(self, exc_type, exc, tb):
        if exc_type: self.conn.rollback()
        else:        self.conn.commit()
        return False            # False → re-raise the exception; True would swallow it

from contextlib import contextmanager

@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.2f}s")

with open('in.csv') as src, open('out.csv', 'w') as dst, timed('copy'):
    dst.write(src.read())
```

---

## 9. Exception Handling

```python
try:
    value = int(raw)
except (ValueError, TypeError) as e:     # catch specific exceptions
    log.warning("bad value %r: %s", raw, e)
    value = None
else:
    pass                                 # runs only if no exception
finally:
    pass                                 # always runs (cleanup)
```

Best practices:
- Catch **specific** exceptions; never use a bare `except:` (it also catches `KeyboardInterrupt`/`SystemExit`).
- Re-raise with context: `raise PipelineError("load failed") from e`.
- Use `logging` (with `logger.exception(...)` inside `except` to include the traceback), not `print`.
- **EAFP** (try first, handle failure) is idiomatic Python: `try: d[k] except KeyError:` vs checking first.

```python
class DataValidationError(Exception):
    """Raised when a record fails validation."""
    def __init__(self, record_id, reason):
        super().__init__(f"record {record_id}: {reason}")
        self.record_id, self.reason = record_id, reason

def validate(rec):
    if rec.get('amount') is None or rec['amount'] < 0:
        raise DataValidationError(rec.get('id'), 'invalid amount')
```

---

## 10. OOP

```python
from abc import ABC, abstractmethod

class Source(ABC):                              # abstract base class = interface
    def __init__(self, name):
        self.name = name                        # instance attribute
    @abstractmethod
    def read(self): ...
    def __repr__(self):
        return f"{type(self).__name__}({self.name!r})"

class S3Source(Source):                         # inheritance
    region = 'us-east-1'                        # class attribute (shared)
    def __init__(self, name, bucket):
        super().__init__(name)
        self.bucket = bucket
    def read(self):                             # polymorphism: same method, different behaviour
        return f"reading s3://{self.bucket}"

    @classmethod
    def from_uri(cls, uri):                     # alternative constructor
        return cls('s3', uri.removeprefix('s3://').split('/')[0])

    @staticmethod
    def is_valid_key(key):                      # utility, no self/cls
        return not key.endswith('/')

    @property
    def uri(self):                              # computed attribute with getter
        return f"s3://{self.bucket}"
```

| Concept | Meaning |
|---|---|
| Encapsulation | Bundle data + methods; `_name` = internal by convention, `__name` = name-mangled |
| Inheritance | Reuse a parent class; `super()` calls the parent; MRO decides lookup order with multiple inheritance |
| Polymorphism | Different classes, same interface (`read()`); also duck typing |
| Abstraction | `ABC` + `@abstractmethod` forces subclasses to implement methods |
| Composition | "has-a" (pipeline has a source and a sink) – often preferred over deep inheritance |

Useful dunder methods: `__init__`, `__repr__`/`__str__`, `__eq__`/`__hash__`, `__len__`, `__iter__`, `__enter__`/`__exit__`, `__call__`.

---

## 11. Files, CSV, JSON

```python
import csv, json, gzip
from pathlib import Path

# Text files – always pass encoding; iterate instead of read() for big files
with open('input.txt', encoding='utf-8') as f:
    for line in f: ...

# CSV
with open('in.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):               # each row is a dict keyed by header
        ...
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['id', 'name'])
    w.writeheader(); w.writerows([{'id': 1, 'name': 'Alice'}])

# JSON
data = json.loads('{"a": 1}');  text = json.dumps(data, indent=2, default=str)  # default=str handles dates/Decimals
with open('data.json', encoding='utf-8') as f: obj = json.load(f)

# JSON Lines (one JSON object per line) – streamable, common for logs/events
with gzip.open('events.jsonl.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        event = json.loads(line)

# pathlib
for p in Path('landing').glob('**/*.csv'):
    print(p.name, p.stem, p.suffix, p.stat().st_size)
```

Flatten nested JSON (very common):
```python
def flatten(obj, parent='', sep='.'):
    items = {}
    for k, v in obj.items():
        key = f"{parent}{sep}{k}" if parent else k
        if isinstance(v, dict):
            items.update(flatten(v, key, sep))
        else:
            items[key] = v
    return items

flatten({'id': 1, 'cust': {'name': 'A', 'addr': {'zip': '10001'}}})
# {'id': 1, 'cust.name': 'A', 'cust.addr.zip': '10001'}
```

---

## 12. Dates and Times

```python
from datetime import datetime, date, timedelta, timezone
from zoneinfo import ZoneInfo                       # 3.9+

now_utc = datetime.now(timezone.utc)                # prefer timezone-aware datetimes
ny      = now_utc.astimezone(ZoneInfo('America/New_York'))
parsed  = datetime.strptime('2026-10-29 14:05', '%Y-%m-%d %H:%M')   # str → datetime
text    = parsed.strftime('%Y%m%d')                                   # datetime → str
iso     = datetime.fromisoformat('2026-10-29T14:05:00+00:00')
delta   = date(2026, 12, 31) - date(2026, 1, 1); delta.days         # 364
yesterday = date.today() - timedelta(days=1)

def month_bounds(d):                                # first and last day of a month
    first = d.replace(day=1)
    nxt = (first + timedelta(days=32)).replace(day=1)
    return first, nxt - timedelta(days=1)

def date_range(start, end):                         # inclusive daily range (backfills)
    for n in range((end - start).days + 1):
        yield start + timedelta(days=n)
```
`timedelta(days=30)` is not "one month" – use `dateutil.relativedelta(months=1)` or the helper above.

---

## 13. Concurrency (when it matters)

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

# I/O-bound (S3 downloads, API calls) → threads
with ThreadPoolExecutor(max_workers=8) as pool:
    futures = {pool.submit(download, key): key for key in keys}
    for fut in as_completed(futures):
        try:
            fut.result()
        except Exception as e:
            log.error("failed %s: %s", futures[fut], e)

# CPU-bound (parsing, hashing, compression) → processes (bypasses the GIL)
with ProcessPoolExecutor() as pool:
    results = list(pool.map(parse_file, files))
```
`asyncio` is another option for very high numbers of concurrent I/O calls (e.g. `aiohttp`).

---

## 14. pandas Essentials (often asked alongside Python)

```python
import pandas as pd

df = pd.read_csv('orders.csv', parse_dates=['order_ts'], dtype={'zip': 'string'})
df = df.drop_duplicates(subset=['order_id'], keep='last')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)
summary = (df[df['status'] == 'COMPLETE']
           .groupby('region', as_index=False)
           .agg(orders=('order_id', 'count'), revenue=('amount', 'sum')))
merged = df.merge(customers, on='customer_id', how='left', validate='many_to_one')
latest = df.sort_values('updated_at').groupby('order_id').tail(1)     # latest row per key
df['rank'] = df.groupby('region')['amount'].rank(method='dense', ascending=False)

for chunk in pd.read_csv('huge.csv', chunksize=100_000):              # large files
    process(chunk)
```
Avoid row-by-row `iterrows()`; use vectorized column operations. For data larger than memory use chunks, Polars, DuckDB or Spark.

---

## 15. AWS boto3 Basics

```python
import boto3, json

s3 = boto3.client('s3')

# list_objects_v2 returns at most 1,000 keys per call → always paginate
paginator = s3.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket='my-bucket', Prefix='landing/2026/'):
    for obj in page.get('Contents', []):
        print(obj['Key'], obj['Size'])

s3.upload_file('local.csv', 'my-bucket', 'landing/local.csv')    # multipart for large files
s3.download_file('my-bucket', 'landing/local.csv', '/tmp/local.csv')

body = s3.get_object(Bucket='my-bucket', Key='data/events.jsonl')['Body']
for line in body.iter_lines():                                     # stream, don't read() huge files
    event = json.loads(line)

s3.put_object(Bucket='my-bucket', Key='out/result.json', Body=json.dumps({'ok': True}))

secret = json.loads(
    boto3.client('secretsmanager').get_secret_value(SecretId='prod/db')['SecretString'])
```
Credentials come from IAM roles / environment – never hardcode keys. Handle `botocore.exceptions.ClientError` and check `e.response['Error']['Code']`.

Secure tokens: use the `secrets` module (`secrets.token_urlsafe(16)`), **not** `random`, which is predictable.

---

## 16. Data Engineer Coding Problems

### Arrays and hashing
```python
def two_sum(nums, target):                        # O(n)
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []

def find_missing(nums):                           # numbers 1..n with one missing
    n = len(nums) + 1
    return n * (n + 1) // 2 - sum(nums)

def second_largest(nums):
    uniq = sorted(set(nums), reverse=True)
    return uniq[1] if len(uniq) > 1 else None

def find_duplicates(items):
    return [k for k, c in Counter(items).items() if c > 1]

def dedupe_keep_order(items):
    return list(dict.fromkeys(items))             # preserves first occurrence

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w))].append(w)
    return list(groups.values())

def top_k_frequent(items, k):
    return [x for x, _ in Counter(items).most_common(k)]

def merge_intervals(intervals):                   # [[1,3],[2,6],[8,10]] → [[1,6],[8,10]]
    out = []
    for start, end in sorted(intervals):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out

def is_valid_parentheses(s):
    pairs, stack = {')': '(', ']': '[', '}': '{'}, []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        elif ch in '([{':
            stack.append(ch)
    return not stack

def binary_search(arr, target):                   # arr must be sorted; or use bisect
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        if arr[mid] < target:  lo = mid + 1
        else:                  hi = mid - 1
    return -1

def merge_sorted(a, b):                           # core of merge sort; or heapq.merge
    i = j = 0; out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else:            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
```
In real code use `sorted()` (Timsort, O(n log n), stable); the algorithms below are asked to test fundamentals.

### Sorting algorithms
| Algorithm | Time (avg / worst) | Extra space | Stable |
|---|---|---|---|
| Bubble sort | O(n²) / O(n²) | O(1) | Yes |
| Merge sort | O(n log n) / O(n log n) | O(n) | Yes |
| Quick sort | O(n log n) / O(n²) | O(log n) in-place; O(n) for the version below | No |

```python
def bubble_sort(arr):                             # swap adjacent items; stop early if no swaps
    arr = arr[:]
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):         # last i items are already in place
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):                              # divide, sort halves, merge
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge_sorted(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def quick_sort(arr):                              # partition around a pivot (simple, not in-place)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    return (quick_sort([x for x in arr if x < pivot])
            + [x for x in arr if x == pivot]
            + quick_sort([x for x in arr if x > pivot]))
```

### Recursion
Every recursive function needs a **base case** and must move toward it. Python's default recursion limit is ~1000 and there is no tail-call optimization.
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def sum_of_digits(n):
    return 0 if n == 0 else n % 10 + sum_of_digits(n // 10)

def reverse_list(lst):                            # O(n²) because of slicing – iterative lst[::-1] is O(n)
    return lst if len(lst) <= 1 else reverse_list(lst[1:]) + [lst[0]]

def tower_of_hanoi(n, source='A', target='C', spare='B'):
    """Move n disks from source to target; 2**n - 1 moves."""
    if n == 0:
        return
    tower_of_hanoi(n - 1, source, spare, target)  # move n-1 disks out of the way
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, spare, target, source)  # move them on top of disk n

tower_of_hanoi(3)   # 7 moves
```

### Candy-wrapper exchange puzzle
"Each candy costs 1; every 3 wrappers can be exchanged for 1 candy. How many candies can you eat with `amount` money?"
```python
def max_candies(amount, wrappers_per_candy=3):
    candies = wrappers = amount
    while wrappers >= wrappers_per_candy:
        new = wrappers // wrappers_per_candy
        candies += new
        wrappers = wrappers % wrappers_per_candy + new   # leftover + wrappers of new candies
    return candies

max_candies(15)   # 22  (15 + 5 + 1 + 1, with 1 wrapper left)
```

### Data-processing scenarios

**1. Word count on a large file (streaming)**
```python
def word_count(path):
    counts = Counter()
    with open(path, encoding='utf-8') as f:
        for line in f:
            counts.update(re.findall(r'\w+', line.lower()))
    return counts.most_common(10)
```

**2. Latest record per key (dedupe CDC records)**
```python
def latest_per_key(records, key='id', ts='updated_at'):
    latest = {}
    for r in records:
        k = r[key]
        if k not in latest or r[ts] > latest[k][ts]:
            latest[k] = r
    return list(latest.values())
```

**3. Group by and aggregate without pandas**
```python
def revenue_by_region(rows):
    totals = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
    for r in rows:
        t = totals[r['region']]
        t['orders'] += 1
        t['revenue'] += float(r['amount'])
    return dict(totals)
```

**4. Validate records and quarantine bad ones**
```python
def split_valid(rows, required=('id', 'amount')):
    good, bad = [], []
    for r in rows:
        missing = [c for c in required if not r.get(c)]
        try:
            if missing:
                raise ValueError(f"missing {missing}")
            r['amount'] = float(r['amount'])
            good.append(r)
        except ValueError as e:
            bad.append({**r, '_error': str(e)})
    return good, bad
```

**5. Join two datasets (hash join)**
```python
def left_join(orders, customers, key='customer_id'):
    lookup = {c[key]: c for c in customers}                 # build side: smaller dataset
    return [{**o, **lookup.get(o[key], {})} for o in orders]
```

**6. Compare two files / find changed records**
```python
def diff(old_rows, new_rows, key='id'):
    old = {r[key]: r for r in old_rows}
    new = {r[key]: r for r in new_rows}
    inserted = [new[k] for k in new.keys() - old.keys()]
    deleted  = [old[k] for k in old.keys() - new.keys()]
    updated  = [new[k] for k in new.keys() & old.keys() if new[k] != old[k]]
    return inserted, updated, deleted
```

**7. Parse log lines and count errors per hour**
```python
LOG = re.compile(r'^(?P<ts>\d{4}-\d{2}-\d{2} \d{2}):\d{2}:\d{2} (?P<level>\w+) ')
def errors_per_hour(path):
    counts = Counter()
    for line in read_lines(path):
        m = LOG.match(line)
        if m and m['level'] == 'ERROR':
            counts[m['ts']] += 1
    return dict(sorted(counts.items()))
```

**8. Split a large CSV into files of N rows**
```python
def split_csv(path, rows_per_file=100_000):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, batch in enumerate(chunked(reader, rows_per_file), start=1):
            with open(f"part_{i:04d}.csv", 'w', newline='', encoding='utf-8') as out:
                w = csv.writer(out); w.writerow(header); w.writerows(batch)
```

**9. Moving average / sliding window over a stream**
```python
def moving_average(values, window=3):
    q, total = deque(), 0
    for v in values:
        q.append(v); total += v
        if len(q) > window:
            total -= q.popleft()
        if len(q) == window:
            yield total / window
```

**10. LRU cache (design question)**
```python
class LRUCache:
    def __init__(self, capacity):
        self.cap, self.data = capacity, OrderedDict()
    def get(self, key):
        if key not in self.data:
            return None
        self.data.move_to_end(key)
        return self.data[key]
    def put(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.cap:
            self.data.popitem(last=False)          # evict least recently used
```

---

## 17. Quick Q&A

- **List vs tuple?** List is mutable; tuple is immutable, hashable (if its items are), slightly faster and smaller.
- **List vs generator?** A list holds all items in memory; a generator yields one at a time (lazy, single pass).
- **`append` vs `extend`?** `append` adds one element (even a list); `extend` adds each item of an iterable.
- **`sort()` vs `sorted()`?** `sort()` is in place on lists and returns `None`; `sorted()` returns a new list from any iterable.
- **`@staticmethod` vs `@classmethod`?** Static gets no implicit argument; class method gets `cls` (used for alternative constructors).
- **`__str__` vs `__repr__`?** `__str__` is user-friendly; `__repr__` is unambiguous for developers (used in logs/debugging).
- **What is `if __name__ == '__main__':`?** Runs code only when the file is executed directly, not when imported.
- **How do you process a 50 GB file?** Stream it line by line or in chunks (generators, `chunksize`), never `read()` it all; parallelize by file/partition; use Spark/DuckDB if it outgrows one machine.
- **How do you make a pipeline step idempotent?** Deterministic output paths, overwrite instead of append, dedupe by key, track processed files/watermarks.
- **Threads vs processes?** Threads for I/O-bound work (GIL is released while waiting); processes for CPU-bound work.
- **How do you manage dependencies?** Virtual environments (`venv`), pinned versions in `requirements.txt`/`pyproject.toml`; unit tests with `pytest`; formatting/linting with `black`/`ruff`.
