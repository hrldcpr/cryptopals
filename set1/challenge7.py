
import base64

from Crypto.Cipher import AES

import utilities


def decrypt(x, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(x)

@utilities.main(__name__)
def main():
    key = b'YELLOW SUBMARINE'
    with open('set1/challenge7.txt') as f:
        x = base64.b64decode(f.read())
    print(decrypt(x, key).decode())
