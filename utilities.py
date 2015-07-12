
import sys


def main(f):
    if f.__module__ == '__main__':
        f()
    return f

def flushprint(text):
    sys.stdout.write(text)
    sys.stdout.flush()
