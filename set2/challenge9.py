
import utilities


def pad(text, n):
    m = n - len(text)
    return text + bytes([m] * m)

def unpad(text, n):
    if text:
        m = text[-1]
        if m < n and text.endswith(bytes([m] * m)):
            return text[:-m]
    return text


@utilities.main
def main():
    x = b'YELLOW SUBMARINE'

    y = pad(x, 20)

    assert y == b'YELLOW SUBMARINE\x04\x04\x04\x04'
    assert unpad(y, 20) == x
    print(y)
