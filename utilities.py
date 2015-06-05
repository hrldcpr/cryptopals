
import sys


def main(name):
    def decorator(f):
        if name == '__main__':
            f()
        return f
    return decorator

def flushprint(s):
    sys.stdout.write(s)
    sys.stdout.flush()
