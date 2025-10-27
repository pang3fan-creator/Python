def find_odd(end):
    start = 0
    while start < end:
        yield start
        start += 1


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return find_odd(self.end)


for item in MyRange(10):
    print(item)
