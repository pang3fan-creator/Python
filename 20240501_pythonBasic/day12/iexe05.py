class Father:
    def __init__(self, fname, age):
        self.name = fname
        self.age = age


class Son(Father):
    def __init__(self, fname, age):
        super(Son, self).__init__()


son = Son("zhangsan", 20)
print(son.name)
