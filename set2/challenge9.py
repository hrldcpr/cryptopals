
import utilities


def pad(text, n):
    m = n - len(text)
    return text + bytes([m] * m)


@utilities.main(__name__)
def main():
    x = b'YELLOW SUBMARINE'

    y = pad(x, 20)

    assert y == b'YELLOW SUBMARINE\x04\x04\x04\x04'
    print(y)
