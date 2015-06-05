
import base64

import utilities

from .challenge1 import decode_hex


def encode_hex(bs):
    return base64.b16encode(bs).lower()


@utilities.main(__name__)
def main():
    a = '1c0111001f010100061a024b53535009181c'
    b = '686974207468652062756c6c277320657965'

    a = decode_hex(a)
    b = decode_hex(b)
    c = bytes(x ^ y for x, y in zip(a, b))

    print(encode_hex(c) == b'746865206b696420646f6e277420706c6179')
