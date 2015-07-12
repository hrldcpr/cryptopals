
import base64
import math

from Crypto.Cipher import AES

import utilities

from set1.challenge7 import encrypt_ecb
from set1.challenge8 import repeats
from .challenge11 import guess_mode, random_bytes


def pad16(text):
    # we can't use PKCS#7 padding as in Challenge 9,
    # because then shifting changes the padding values
    return text.ljust(16 * math.ceil(len(text) / 16), b'\x00')

SUFFIX = base64.b64decode('''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK''')
KEY = random_bytes(16)
def oracle(text):
    return encrypt_ecb(pad16(text + SUFFIX), KEY)

def guess_block_size(oracle=oracle):
    for n in range(2, 40):
        if repeats(oracle(b'x' * n * 3), n):
            return n

def find_suffix(n):
    suffix = b''
    for i in range(len(oracle(b''))):
        j = n * (i // n) # beginning of current chunk
        padding = b'x' * (n - 1 - (i % n))
        target = oracle(padding)
        for b in range(256):
            encrypted = oracle(padding + suffix + bytes([b]))
            if encrypted[j:j+n] == target[j:j+n]:
                suffix += bytes([b])
                break
        else: raise Exception("couldn't find byte after {}".format(suffix))
    return suffix


@utilities.main
def main():
    guess_mode(lambda text: (oracle(text), AES.MODE_ECB))

    n = guess_block_size()
    assert n == 16

    encrypted = oracle(random_bytes(n) * 2)
    assert encrypted[:n] == encrypted[n:2*n] # ECB

    suffix = find_suffix(n)
    assert suffix == pad16(SUFFIX)
    print(suffix)
