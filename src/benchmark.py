import time
import tracemalloc
from bloom_filter import BloomFilter

def benchmark_set(users, values):
    start = time.perf_counter()
    for value in values:
        value in users
    return time.perf_counter() - start

def benchmark_bloom(bloom, values):
    start = time.perf_counter()
    for value in values:
        bloom.might_contain(value)
    return time.perf_counter() - start

def measure_set_memory(num_users):
    tracemalloc.start()
    users = {
        f"user{i}"
        for i in range(num_users)
    }
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

def measure_bloom_memory(num_users, bloomSize, bloomHash):
    tracemalloc.start()
    bloom = BloomFilter(
        size=bloomSize,
        num_hashes=bloomHash
    )
    for i in range(num_users):
        bloom.add(f"user{i}")
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak