
import itertools

import utilities

from .challenge2 import encode_hex


def xor(bites, key):
    return bytes(b ^ k for b, k in zip(bites, itertools.cycle(key)))


@utilities.main(__name__)
def main():
    x = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
    k = b'ICE'

    y = xor(x, k)

    assert encode_hex(y) == b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
