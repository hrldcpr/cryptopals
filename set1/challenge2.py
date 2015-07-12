
import base64

import utilities

from .challenge1 import decode_hex


def encode_hex(bites):
    return base64.b16encode(bites).lower()


@utilities.main
def main():
    x = decode_hex('1c0111001f010100061a024b53535009181c')
    y = decode_hex('686974207468652062756c6c277320657965')

    z = bytes(a ^ b for a, b in zip(x, y))

    assert encode_hex(z) == b'746865206b696420646f6e277420706c6179'
    print(z.decode())
