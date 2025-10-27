import sys

inl = [i for i in sys.stdin]
for i in range(len(inl) // 3):
    a = int(inl[i * 3])
    b = list(inl[i * 3 + 1].split())
    c = int(inl[i * 3 + 2])
    print(b[-1 * c])
