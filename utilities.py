
def main(name):
    def decorator(f):
        if name == '__main__':
            f()
        return f
    return decorator
