
import utilities


def pad(x, n):
    m = n - len(x)
    return x + bytes([m] * m)


@utilities.main(__name__)
def main():
    x = b'YELLOW SUBMARINE'
    assert pad(x, 20) == b'YELLOW SUBMARINE\x04\x04\x04\x04'
