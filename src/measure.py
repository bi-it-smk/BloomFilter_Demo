from bloom_filter import BloomFilter
from benchmark import benchmark_set, benchmark_bloom, measure_set_memory, measure_bloom_memory

NUM_USERS = 100000

users = {
    f"user{i}"
    for i in range(NUM_USERS)
}

bloom = BloomFilter(
    size=1000000,
    num_hashes=7
)
bloomSize = bloom.size
bloomHash = bloom.num_hashes

for user in users:
    bloom.add(user)

lookup_values = [
    f"user{i}"
    for i in range(NUM_USERS)
]

set_time = benchmark_set(users, lookup_values)
bloom_time = benchmark_bloom(bloom, lookup_values)

print(f"Users: {len(users):,}")

print(f"Set lookup time: {set_time:.6f} seconds") #faster --> set uses C
print(f"Bloom lookup time: {bloom_time:.6f} seconds") #slower --> value -> 7 hashes

current, peak = measure_set_memory(NUM_USERS)
print(f"Set current memory: {current / 1024 / 1024:.2f} MB")
print(f"Set peak memory: {peak / 1024 / 1024:.2f} MB")

current, peak = measure_bloom_memory(NUM_USERS,bloomSize,bloomHash)
print(f"Bloom current memory: {current / 1024 / 1024:.2f} MB")
print(f"Bloom peak memory: {peak / 1024 / 1024:.2f} MB")