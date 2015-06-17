
import collections
import statistics

import utilities

from .challenge1 import decode_hex


def normalize(counts):
    total = sum(counts.values())
    return {k: count / total for k, count in counts.items()}

def distribution(text):
    return normalize(collections.Counter(text))

def difference(x, y):
    keys = x.keys() | y.keys()
    return statistics.mean((x.get(k, 0) - y.get(k, 0)) ** 2 for k in keys)

def xor(bites, key):
    return bytes(b ^ key for b in bites)

def as_ascii(bites):
    return bites.decode('ascii', errors='ignore')

def english():
    with open('set1/english.txt') as f:
        for line in f:
            for c in line:
                yield c

def score(encrypted, target_distribution, key):
    return difference(distribution(as_ascii(xor(encrypted, key))),
                      target_distribution)

def best_score_key(encrypted, target_distribution):
    return min((score(encrypted, target_distribution, k), k)
               for k in range(256))

def best_key(encrypted, target_distribution):
    _, key = best_score_key(encrypted, target_distribution)
    return key


@utilities.main(__name__)
def main():
    x = decode_hex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

    key = best_key(x, distribution(english()))

    print(bytes([key]))
    print(xor(x, key).decode())
