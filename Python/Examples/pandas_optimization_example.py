"""
Pandas Optimization Examples
Demonstrates optimized vs unoptimized approaches for common data operations.
"""

import pandas as pd
import numpy as np
import time


def benchmark(func):
    """Decorator to benchmark function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.4f}s")
        return result
    return wrapper


# Example 1: Vectorized operations vs apply()
@benchmark
def slow_apply():
    """BAD: Using apply with lambda (slow)"""
    df = pd.DataFrame({'amount': np.random.randn(100000)})
    df['doubled'] = df['amount'].apply(lambda x: x * 2)
    return df


@benchmark
def fast_vectorized():
    """GOOD: Vectorized operation (100x faster)"""
    df = pd.DataFrame({'amount': np.random.randn(100000)})
    df['doubled'] = df['amount'] * 2
    return df


# Example 2: Optimizing data types
@benchmark
def default_types():
    """BAD: Default types use more memory"""
    df = pd.DataFrame({
        'user_id': range(1000000),  # int64
        'category': ['A', 'B', 'C'] * 333334,  # object
        'amount': np.random.randn(1000000)  # float64
    })
    memory_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"  Memory: {memory_mb:.2f} MB")
    return df


@benchmark
def optimized_types():
    """GOOD: Optimized types (50% less memory)"""
    df = pd.DataFrame({
        'user_id': pd.array(range(1000000), dtype='int32'),
        'category': pd.Categorical(['A', 'B', 'C'] * 333334),
        'amount': pd.array(np.random.randn(1000000), dtype='float32')
    })
    memory_mb = df.memory_usage(deep=True).sum() / 1024**2
    print(f"  Memory: {memory_mb:.2f} MB")
    return df


# Example 3: Efficient filtering
@benchmark
def slow_filtering():
    """BAD: Multiple passes through data"""
    df = pd.DataFrame({
        'amount': np.random.randn(1000000),
        'category': np.random.choice(['A', 'B', 'C'], 1000000)
    })
    
    # Multiple filters
    df_a = df[df['category'] == 'A']
    df_high = df_a[df_a['amount'] > 0]
    return df_high


@benchmark
def fast_filtering():
    """GOOD: Combined filter (single pass)"""
    df = pd.DataFrame({
        'amount': np.random.randn(1000000),
        'category': np.random.choice(['A', 'B', 'C'], 1000000)
    })
    
    # Combined filter
    df_result = df[(df['category'] == 'A') & (df['amount'] > 0)]
    return df_result


# Example 4: Efficient groupby
@benchmark
def slow_groupby():
    """BAD: Multiple groupby operations"""
    df = pd.DataFrame({
        'user_id': np.random.randint(0, 10000, 1000000),
        'amount': np.random.randn(1000000)
    })
    
    totals = df.groupby('user_id')['amount'].sum()
    counts = df.groupby('user_id').size()
    averages = df.groupby('user_id')['amount'].mean()
    return totals, counts, averages


@benchmark
def fast_groupby():
    """GOOD: Single groupby with agg"""
    df = pd.DataFrame({
        'user_id': np.random.randint(0, 10000, 1000000),
        'amount': np.random.randn(1000000)
    })
    
    stats = df.groupby('user_id')['amount'].agg(['sum', 'count', 'mean'])
    return stats


# Example 5: String operations
@benchmark
def slow_string_ops():
    """BAD: Inefficient string concatenation"""
    df = pd.DataFrame({
        'first_name': ['John'] * 100000,
        'last_name': ['Doe'] * 100000
    })
    
    result = []
    for idx, row in df.iterrows():  # Very slow!
        result.append(row['first_name'] + ' ' + row['last_name'])
    
    df['full_name'] = result
    return df


@benchmark
def fast_string_ops():
    """GOOD: Vectorized string operations"""
    df = pd.DataFrame({
        'first_name': ['John'] * 100000,
        'last_name': ['Doe'] * 100000
    })
    
    df['full_name'] = df['first_name'] + ' ' + df['last_name']
    return df


# Example 6: Reading large files
def slow_file_read():
    """BAD: Load entire file into memory"""
    # This would fail for files > available RAM
    # df = pd.read_csv('huge_file.csv')
    pass


def fast_file_read():
    """GOOD: Process in chunks"""
    chunk_size = 100000
    
    for chunk in pd.read_csv('data.csv', chunksize=chunk_size):
        # Process each chunk
        chunk_clean = chunk.dropna()
        # ... process and write to output
        pass


def main():
    """Run all benchmarks"""
    print("=" * 60)
    print("PANDAS OPTIMIZATION BENCHMARKS")
    print("=" * 60)
    
    print("\n1. Vectorized vs Apply:")
    slow_apply()
    fast_vectorized()
    
    print("\n2. Data Type Optimization:")
    default_types()
    optimized_types()
    
    print("\n3. Filtering Efficiency:")
    slow_filtering()
    fast_filtering()
    
    print("\n4. GroupBy Optimization:")
    slow_groupby()
    fast_groupby()
    
    print("\n5. String Operations:")
    slow_string_ops()
    fast_string_ops()
    
    print("\n" + "=" * 60)
    print("Key Takeaways:")
    print("- Use vectorized operations instead of apply()")
    print("- Optimize data types to reduce memory usage")
    print("- Combine filters for single-pass processing")
    print("- Use agg() for multiple aggregations")
    print("- Never use iterrows() in production!")
    print("=" * 60)


if __name__ == "__main__":
    main()
