
import utilities

from .challenge3 import best_score_key, decode_hex, distribution, english, xor


@utilities.main
def main():
    english_distribution = distribution(english())

    with open('set1/challenge4.txt') as f:
        best = (float('inf'), None), None
        for line in f:
            utilities.flushprint('.')
            line = line.strip()
            d = best_score_key(decode_hex(line), english_distribution), line
            if d < best:
                best = d
                print(best)
        print()

    (_, key), line = best
    print(line)
    print(bytes([key]))
    print(xor(decode_hex(line), key).decode())
