
import collections
import statistics

import utilities

from .challenge1 import decode_hex


def normalize(counts):
    total = sum(counts.values())
    return {k: count / total
            for k, count in counts.items()}

def distribution(text):
    return normalize(collections.Counter(text))

def difference(a, b):
    keys = a.keys() | b.keys()
    return statistics.mean((a.get(k, 0) - b.get(k, 0)) ** 2
                           for k in keys)

def decrypt(encrypted, key):
    return bytes(x ^ key for x in encrypted)

def as_ascii(bs):
    return bs.decode('ascii', errors='ignore')

def english():
    with open('set1/english.txt') as f:
        for line in f:
            for c in line:
                yield c

def score(encrypted, target_distribution, key):
    return difference(distribution(as_ascii(decrypt(encrypted, key))),
                      target_distribution)

def best_key(encrypted, target_distribution):
    return min(range(256), key=lambda key: score(encrypted, target_distribution, key))


@utilities.main(__name__)
def main():
    x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    x = decode_hex(x)
    key = best_key(x, distribution(english()))
    print(key)
    print(decrypt(x, key))
