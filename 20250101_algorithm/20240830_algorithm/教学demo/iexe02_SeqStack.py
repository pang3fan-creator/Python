class SeqStack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    s = SeqStack()
    print(s.is_empty())
