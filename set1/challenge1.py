
import base64

import utilities


def decode_hex(nibbles):
    return base64.b16decode(nibbles, True)


@utilities.main
def main():
    x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    y = decode_hex(x)

    assert base64.b64encode(y) == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print(y.decode())
