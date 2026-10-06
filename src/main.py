from bloom_filter import BloomFilter

bloom = BloomFilter(size=20, num_hashes=3)

#add users
users = {"alice", "bob", "ben"}

for user in users:
    bloom.add(user)

#check if users exist
print("alice", bloom.might_contain("alice"))
print("bob", bloom.might_contain("bob"))
print("ben", bloom.might_contain("ben"))
print("sam", bloom.might_contain("sam"))

#demonstrate false positives
for i in range(10000):
    username = f"user{i}"
    if bloom.might_contain(username):
        print("False positive:", username)
        print("Bloom Filter:", bloom.might_contain(username))
        print("Python set:", username in users)
        break