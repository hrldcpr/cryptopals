
import sys


def main(name):
    def decorator(f):
        if name == '__main__':
            f()
        return f
    return decorator

def flushprint(text):
    sys.stdout.write(text)
    sys.stdout.flush()
