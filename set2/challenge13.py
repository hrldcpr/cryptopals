
import urllib.parse

from Crypto.Cipher import AES

import utilities

from set1.challenge7 import decrypt_ecb, encrypt_ecb
from set2.challenge11 import guess_mode, pad16, random_bytes, unpad16
from set2.challenge12 import guess_block_size


KEY = random_bytes(16)
USER_ROLE = b'user'
PREFIX = b'email='

def encrypt(text):
    return encrypt_ecb(pad16(text), KEY)

def decrypt(encrypted):
    return unpad16(decrypt_ecb(encrypted, KEY))

def parse_query(text):
    return urllib.parse.parse_qs(text)

def profile_for(email):
    if '&' in email or '=' in email: raise ValueError()
    return urllib.parse.urlencode(( # order matters
        ('email', email),
        ('uid', 10),
        ('role', USER_ROLE)
    ), safe='@').encode()

def encrypted_profile_for(email):
    return encrypt(profile_for(email.decode()))

BASE_EMAIL = 'x{}@x.st'
MIN_EMAIL_LENGTH = len(BASE_EMAIL.format(''))
def fake_email(n):
    assert n >= MIN_EMAIL_LENGTH
    return BASE_EMAIL.format('x' * (n - MIN_EMAIL_LENGTH)).encode()

def find_alignment(oracle=encrypted_profile_for):
    # find an email length that aligns profile to end of a block
    k = len(oracle(fake_email(MIN_EMAIL_LENGTH)))
    for n in range(MIN_EMAIL_LENGTH + 1, 40):
        if len(oracle(fake_email(n))) > k:
            # got to next block, so previous length was aligned
            return n - 1

def make_admin_role(n, oracle=encrypted_profile_for):
    k = find_alignment()
    assert (len(profile_for('')) + k) % n == 0
    # push 'user' role into the final block, and then throw that out:
    encrypted = oracle(fake_email(k + len(USER_ROLE)))
    assert decrypt(encrypted[-n:]) == USER_ROLE
    encrypted_role = encrypted[:-n]

    assert len(PREFIX) < n
    encrypted_admin = oracle(fake_email(n - len(PREFIX)) + b'admin')[n:n*2]

    return encrypted_role + encrypted_admin


@utilities.main(__name__)
def main():
    try: profile_for('foo@bar.com&role=admin')
    except ValueError: pass
    else: assert False

    guess_mode(lambda text: (encrypted_profile_for(text), AES.MODE_ECB))

    n = guess_block_size(encrypted_profile_for)
    assert n == 16

    encrypted = make_admin_role(n)

    profile = decrypt(encrypted)
    assert parse_query(profile)[b'role'] == [b'admin']
    print(profile)
