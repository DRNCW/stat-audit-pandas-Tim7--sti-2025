import hashlib
import numpy as np


def monte_carlo_simulation(data, n_samples=10000, threshold=30):
    
    clean_data = data.dropna().values

    samples = np.random.choice(clean_data, size=n_samples, replace=True)
    probability = np.mean(samples > threshold)

    return samples, probability


class BloomFilter:

    def __init__(self, size=10000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        positions = []

        for i in range(self.hash_count):
            text = str(i) + str(item)
            hash_value = int(hashlib.md5(text.encode()).hexdigest(), 16)
            positions.append(hash_value % self.size)

        return positions

    def add(self, item):
        for position in self._hashes(item):
            self.bit_array[position] = 1

    def check(self, item):
        for position in self._hashes(item):
            if self.bit_array[position] == 0:
                return False
        return True

    def fill_rate(self):
        return sum(self.bit_array) / self.size


def build_bloom_filter(titles, size=10000, hash_count=3):
    
    bloom_filter = BloomFilter(size=size, hash_count=hash_count)

    clean_titles = titles.dropna().astype(str)

    for title in clean_titles:
        bloom_filter.add(title)

    return bloom_filter


def run_mcmc(data, n_iter=10000):
    
    clean_data = data.dropna().values
    clean_data = clean_data[clean_data > 0]

    current = np.random.choice(clean_data)
    chain = []

    for _ in range(n_iter):
        proposal = np.random.choice(clean_data)

        accept_prob = min(1, proposal / current)

        if np.random.rand() < accept_prob:
            current = proposal

        chain.append(current)

    return np.array(chain)