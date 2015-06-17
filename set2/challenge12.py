
import base64

import utilities

from set1.challenge7 import encrypt_ecb
from set1.challenge8 import repeats
from .challenge11 import pad16, random_bytes


SUFFIX = base64.b64decode('''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK''')
KEY = random_bytes(16)
def encryption_oracle(text):
    return encrypt_ecb(pad16(text + SUFFIX), KEY)

def guess_block_size():
    zero = encryption_oracle(b'')
    for n in range(1, 40):
        if encryption_oracle(b'x' * n)[n:2*n] == zero[:n]:
            return n # 0th block has become 1st block

def find_suffix(n):
    suffix = b''
    for i in range(len(encryption_oracle(b''))):
        j = n * (i // n) # beginning of current chunk
        padding = b'x' * (n - 1 - (i % n))
        target = encryption_oracle(padding)
        for b in range(256):
            encrypted = encryption_oracle(padding + suffix + bytes([b]))
            if encrypted[j:j+n] == target[j:j+n]:
                suffix += bytes([b])
                break
        else: raise Exception("couldn't find byte after {}".format(suffix))
    return suffix

@utilities.main(__name__)
def main():
    n = guess_block_size()
    assert n == 16

    encrypted = encryption_oracle(random_bytes(n) * 2)
    assert encrypted[:n] == encrypted[n:2*n] # ECB

    suffix = find_suffix(n)
    assert suffix == pad16(SUFFIX)
    print(suffix)
