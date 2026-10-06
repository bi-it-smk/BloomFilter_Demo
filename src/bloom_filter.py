import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        if size <= 0:
            raise ValueError("size must be greater than 0")
        if num_hashes <= 0:
            raise ValueError("num_hashes must be greater than 0")
        self.size = size
        self.num_hashes = num_hashes

        # bytes needed to store "size" bits
        num_bytes = (size + 7) // 8
        self.bits = bytearray(num_bytes)

    def _hashes(self, value):
        for i in range(self.num_hashes):
            digest = hashlib.sha256(
                f"{i}:{value}".encode()
            ).digest()

            number = int.from_bytes(digest, "big")
            yield number % self.size

    def add(self, value):
        for position in self._hashes(value):
            byte_index = position // 8
            bit_index = position % 8
            self.bits[byte_index] |= (1 << bit_index)

    def might_contain(self, value):
        for position in self._hashes(value):
            byte_index = position // 8
            bit_index = position % 8
            if not (self.bits[byte_index] & (1 << bit_index)):
                return False
        return True

