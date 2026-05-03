# Python for Data Engineers - Part 6: Real Interview Scenarios

## Real Interview Scenarios

### Scenario 1: Memory Error in Production ETL

**Problem:** ETL pipeline fails with `MemoryError` after months of successful runs.

**Solution:**
```python
# Process in chunks instead of loading entire file
import pandas as pd

def process_large_file_chunked(filepath, chunk_size=100000):
    """Memory-efficient processing"""
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        # Transform chunk
        chunk_clean = chunk.dropna()
        chunk_transformed = chunk_clean[chunk_clean['amount'] > 0]
        
        # Load chunk to database
        chunk_transformed.to_sql('output', engine, if_exists='append', index=False)
        
    print("Processing complete")
```

### Scenario 2: Handling Duplicates from Multiple Sources

**Problem:** Multiple data sources creating duplicate records.

**Solution:**
```python
def handle_duplicates_with_priority(df):
    """Keep record from highest priority source"""
    source_priority = {'api': 1, 'database': 2, 'file': 3}
    
    df['priority'] = df['source'].map(source_priority)
    df_sorted = df.sort_values(['id', 'priority'])
    df_dedup = df_sorted.drop_duplicates(subset=['id'], keep='first')
    
    return df_dedup.drop(columns=['priority'])
```

### Scenario 3: Slow Query Performance

**Problem:** Daily batch job takes 6 hours, needs to run in 1 hour.

**Optimization Steps:**
1. Profile to find bottlenecks
2. Batch database queries (fix N+1 problem)
3. Use multiprocessing for CPU work
4. Optimize data types in Pandas
5. Switch to PySpark if needed

```python
from multiprocessing import Pool, cpu_count

def optimized_processing(records):
    """Parallel processing for speedup"""
    chunk_size = len(records) // cpu_count()
    chunks = [records[i:i+chunk_size] for i in range(0, len(records), chunk_size)]
    
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(process_chunk, chunks)
    
    return [item for chunk in results for item in chunk]
```

### Scenario 4: Data Quality Issues

**Problem:** 20% of production records have invalid data.

**Solution Framework:**
```python
class DataQualityChecker:
    """Validate and clean data"""
    
    def validate_record(self, record):
        """Validate single record"""
        issues = []
        
        # Check required fields
        if not record.get('user_id'):
            issues.append('Missing user_id')
        
        # Check data types
        if not isinstance(record.get('amount'), (int, float)):
            issues.append('Invalid amount type')
        
        # Check business rules
        if record.get('amount', 0) < 0:
            issues.append('Negative amount')
        
        return len(issues) == 0, issues
```

### Scenario 5: API Rate Limiting

**Problem:** External API has rate limits causing pipeline failures.

**Solution:**
```python
import time
from functools import wraps

def rate_limited(max_per_second):
    """Decorator to enforce rate limiting"""
    min_interval = 1.0 / max_per_second
    
    def decorator(func):
        last_called = [0.0]
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            left_to_wait = min_interval - elapsed
            
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        
        return wrapper
    return decorator

@rate_limited(max_per_second=10)
def api_call(endpoint):
    """API call with rate limiting"""
    import requests
    return requests.get(endpoint).json()
```

---

## Quick Reference: Python for Data Engineers

### Must-Know Concepts
1. **Data Structures:** dict > set > list for lookups
2. **Generators:** Memory-efficient for large data
3. **Pandas:** Vectorized operations, avoid iterrows()
4. **PySpark:** For data > 5GB, lazy evaluation
5. **Concurrency:** Threading for I/O, multiprocessing for CPU
6. **Error Handling:** Try-except-finally, custom exceptions
7. **Optimization:** Profile first, optimize bottlenecks

### Common Pitfalls
- Mutable default arguments
- N+1 database queries
- Loading entire file into memory
- Using apply() when vectorized operation exists
- Not handling schema evolution
- Ignoring data quality checks

### Best Practices
- Use type hints for clarity
- Write docstrings for functions
- Log extensively in production
- Handle errors gracefully
- Test with production-like data volumes
- Monitor data quality and pipeline health

---

**Final Interview Tips:**
1. Always ask clarifying questions
2. Discuss trade-offs (time vs space, simplicity vs performance)
3. Think about edge cases
4. Consider scalability
5. Mention production concerns (monitoring, logging, alerting)
6. Explain your thought process clearly
