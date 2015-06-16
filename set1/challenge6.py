
import base64
import itertools
import statistics

import utilities

from .challenge3 import best_key, distribution, english
from .challenge5 import xor


BITS = tuple(1 << i for i in range(8))
def ones(byte):
    return sum(1 for bit in BITS if byte & bit)  # "someone for…"

def hamming_distance(x, y):
    assert len(x) == len(y)
    return sum(ones(a ^ b) for a, b in zip(x, y))  # "someone's a b"

def distance(x, y):
    return hamming_distance(x, y) / len(x)

def chunked(data, n, trailing=False):
    f = itertools.zip_longest if trailing else zip
    return f(*itertools.repeat(iter(data), n))

def transpose(rows):
    return zip(*rows)

def score(data, n):
    """average distance between successive pairs of blocks"""
    return statistics.mean(distance(a, b) for a, b in
                           chunked(chunked(data, n), 2))


@utilities.main(__name__)
def main():
    assert hamming_distance(b'this is a test', b'wokka wokka!!!') == 37

    with open('set1/challenge6.txt') as f:
        x = base64.b64decode(f.read())

    n = min(range(2, 40), key=lambda n: score(x, n))
    print(n, 'byte key')

    columns = transpose(chunked(x, n, trailing=True))
    english_distribution = distribution(english())
    key = bytes(best_key(list(filter(None, column)), english_distribution)
                for column in columns)

    print(key)
    print(xor(x, key).decode())


# why should we expect smallest hamming distance from block to block?
# aligned: (x ^ a) ^ (y ^ a) = x ^ y ^ (a ^ a) = x ^ y
# misaligned: (x ^ a) ^ (y ^ b) = x ^ y ^ a ^ b
# for random x, y there should be no difference
# but if x and y are probably similar then x ^ y will probably have fewer 1s than x ^ y ^ a ^ b
# test by (repeatedly) encoding random bytes versus random letters:
def test(n=18, samples=100):
    with open('set1/challenge6.txt') as f:
        size = len(base64.b64decode(f.read()))
    print(size, 'byte texts')
    print(n, 'byte keys')

    import collections
    tests = collections.defaultdict(list)
    for _ in range(samples):
        utilities.flushprint('.')
        for name, scores in random_test(size, n).items():
            tests[name].append(scores)
    print()
    tests = {name: {n: statistics.mean(scores[n] for scores in results)
                    for n in range(2, 40)}
             for name, results in tests.items()}
    for name, scores in tests.items():
        print(name, ' '.join('{}={:.2f}'.format(n, score) for score, n in
                             sorted((score, n) for n, score in scores.items())))

def random_test(size, n):
    import random, string
    byte_key = bytes(random.randrange(256) for _ in range(n))
    ascii_key = ''.join(random.choice(string.printable) for _ in range(n)).encode('ascii')
    random_bytes = bytes(random.randrange(256) for _ in range(size))
    random_ascii = ''.join(random.choice(string.printable) for _ in range(size)).encode('ascii')

    tests = {
        'bytes with byte key': xor(random_bytes, byte_key),
        'bytes with ascii key': xor(random_bytes, ascii_key),
        'ascii with byte key': xor(random_ascii, byte_key),
        'ascii with ascii key': xor(random_ascii, ascii_key)
    }
    return {name: {n: score(encrypted, n) for n in range(2, 40)}
            for name, encrypted in tests.items()}
