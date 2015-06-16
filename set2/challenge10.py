
import base64

import utilities

from set1.challenge5 import xor
from set1.challenge6 import chunked
from set1.challenge7 import decrypt as decrypt_ecb


def decrypt(encrypted, key, iv):
    text = []
    for chunk in chunked(encrypted, 16):
        chunk = bytes(chunk)
        text.append(xor(iv, decrypt_ecb(chunk, key)))
        iv = chunk
    return b''.join(text)


@utilities.main(__name__)
def main():
    key = b'YELLOW SUBMARINE'
    iv = bytes(0 for _ in key)
    with open('set2/challenge10.txt', 'rb') as f:
        x = base64.b64decode(f.read())

    print(decrypt(x, key, iv))
