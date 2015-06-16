import utilities

from .challenge1 import decode_hex
from .challenge6 import chunked


def score(encrypted):
    chunks = list(chunked(encrypted, 16))
    return len(set(chunks)) / len(chunks)


@utilities.main(__name__)
def main():
    with open('set1/challenge8.txt') as f:
        print(min(f, key=lambda x: score(decode_hex(x.strip()))))
