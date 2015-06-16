
import math
import random

from Crypto.Cipher import AES

import utilities

from set1.challenge7 import encrypt_ecb
from set1.challenge8 import score
from .challenge9 import pad
from .challenge10 import encrypt_cbc


def random_bytes(n):
    return bytes(random.randrange(256) for _ in range(n))

def pad16(text):
    return pad(text, 16 * math.ceil(len(text) / 16))

def encryption_oracle(text):
    text = pad16(random_bytes(random.randint(5, 10))
                 + text
                 + random_bytes(random.randint(5, 10)))
    key = random_bytes(16)
    if random.randrange(2):
        return encrypt_ecb(text, key), AES.MODE_ECB
    else:
        return encrypt_cbc(text, key, random_bytes(16)), AES.MODE_CBC

def guess_mode():
    text = []
    for offset in range(16):
        text.append(pad(b'YELLOW SUBMARINE' * 2, 32 + offset))
    encrypted, mode = encryption_oracle(b''.join(text))
    if score(encrypted) < 1: # repeated chunks
        assert mode == AES.MODE_ECB
    else:
        assert mode == AES.MODE_CBC
    return mode


@utilities.main(__name__)
def main():
    for _ in range(100):
        print('ECB' if guess_mode() == AES.MODE_ECB else 'CBC')
