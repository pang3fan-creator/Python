class MyRange:
    def __init__(self, end):
        self.end = end
        self.index = 0
        self.yield_1 = []

    def find_odd(self):
        start = 0
        while start < self.end:
            yield start
            start += 1

    def __iter__(self):
        return self.find_odd()

    # def __next__(self):
    #     if self.index < len(self.yield_1):
    #         result = self.yield_1[self.index]
    #         self.index += 1
    #         return result
    #     else:
    #         raise StopIteration


for item in MyRange(10):
    print(item)
