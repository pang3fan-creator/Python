from pathlib import Path

a = __file__
b = Path(a)

if __name__ == '__main__':
    print(a)
    print(type(a))

    print(b)
    print(type(b))
    print(b.parent.parent)
