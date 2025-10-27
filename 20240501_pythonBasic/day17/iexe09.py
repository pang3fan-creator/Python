class MyRange:
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            ret = self.start
            self.start += 1
            return ret
        else:
            raise StopIteration


my_range = MyRange(50)
for i in my_range:
    print(i)
iterator = iter(my_range)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

