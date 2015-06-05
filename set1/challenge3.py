
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

def english():
    with open('/Users/harold/Documents/lit/erature/murakami.txt') as f:
        for line in f:
            for c in line:
                    yield c

def best_key(encrypted, target_distribution):
    best = float('inf'), None

    for key in range(256):
        text = decrypt(encrypted, key).decode('ascii', errors='ignore')
        d = difference(distribution(text), target_distribution), key
        if d < best: best = d

    return best

@utilities.main(__name__)
def main():
    X = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    x = decode_hex(X)
    _, key = best_key(x, distribution(english()))
    print(key)
    print(decrypt(x, key))
