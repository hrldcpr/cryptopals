
import base64

import utilities


def decode_hex(s):
    return base64.b16decode(s, True)


@utilities.main(__name__)
def main():
    S = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    print(base64.b64encode(decode_hex(S)))
