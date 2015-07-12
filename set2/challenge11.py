
import math
import random

from Crypto.Cipher import AES

import utilities

from set1.challenge7 import encrypt_ecb
from set1.challenge8 import repeats
from .challenge9 import pad, unpad
from .challenge10 import encrypt_cbc


def random_bytes(n):
    return bytes(random.randrange(256) for _ in range(n))

def pad16(text):
    return pad(text, 16 * math.ceil(len(text) / 16))

def unpad16(text):
    return unpad(text, 16)

def oracle(text):
    text = pad16(random_bytes(random.randint(5, 10))
                 + text
                 + random_bytes(random.randint(5, 10)))
    key = random_bytes(16)
    if random.randrange(2):
        return encrypt_ecb(text, key), AES.MODE_ECB
    else:
        return encrypt_cbc(text, key, random_bytes(16)), AES.MODE_CBC

def guess_mode(oracle=oracle):
    text = b'x' * 100
    encrypted, mode = oracle(text)
    if repeats(encrypted):
        assert mode == AES.MODE_ECB
    else:
        assert mode == AES.MODE_CBC
    return mode


@utilities.main(__name__)
def main():
    for _ in range(1000):
        utilities.flushprint('o' if guess_mode() == AES.MODE_ECB else 'O')
