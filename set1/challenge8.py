import utilities

from .challenge1 import decode_hex
from .challenge6 import chunked


def repeats(encrypted):
    chunks = list(chunked(encrypted, 16))
    return len(set(chunks)) < len(chunks)


@utilities.main(__name__)
def main():
    with open('set1/challenge8.txt') as f:
        likely_ecbs = [x for x in f if repeats(decode_hex(x.strip()))]

    assert len(likely_ecbs) == 1
    print(likely_ecbs[0])
