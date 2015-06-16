
import base64

import utilities

from set1.challenge5 import xor
from set1.challenge6 import chunked
from set1.challenge7 import decrypt_ecb, encrypt_ecb


def encrypt_cbc(text, key, iv):
    encrypted = []
    for chunk in chunked(text, 16):
        chunk = bytes(chunk)
        iv = encrypt_ecb(xor(iv, chunk), key)
        encrypted.append(iv)
    return b''.join(encrypted)


def decrypt_cbc(encrypted, key, iv):
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

    y = decrypt_cbc(x, key, iv)

    assert encrypt_cbc(y, key, iv) == x
    print(y)
