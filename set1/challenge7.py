
import base64

from Crypto.Cipher import AES

import utilities


def encrypt_ecb(text, key):
    return AES.new(key, AES.MODE_ECB).encrypt(text)

def decrypt_ecb(encrypted, key):
    return AES.new(key, AES.MODE_ECB).decrypt(encrypted)


@utilities.main(__name__)
def main():
    key = b'YELLOW SUBMARINE'
    with open('set1/challenge7.txt') as f:
        x = base64.b64decode(f.read())

    y = decrypt_ecb(x, key)

    print(y.decode())
