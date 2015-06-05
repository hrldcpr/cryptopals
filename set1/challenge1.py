
import base64

import utilities


def decode_hex(s):
    return base64.b16decode(s, True)


@utilities.main(__name__)
def main():
    x = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    y = base64.b64encode(decode_hex(x))

    print(y == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
