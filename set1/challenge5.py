
import itertools

import utilities

from .challenge2 import encode_hex


def encrypt(bs, key):
    return bytes(b ^ k for b, k in zip(bs, itertools.cycle(key)))


@utilities.main(__name__)
def main():
    x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

    print(encode_hex(encrypt(x, b'ICE')))
