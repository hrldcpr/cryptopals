
import base64

import utilities

from .challenge1 import decode_hex


def encode_hex(bs):
    return base64.b16encode(bs).lower()


@utilities.main(__name__)
def main():
    A = '1c0111001f010100061a024b53535009181c'
    B = '686974207468652062756c6c277320657965'

    a = decode_hex(A)
    b = decode_hex(B)
    c = bytes(x ^ y for x, y in zip(a, b))

    print(encode_hex(c))
