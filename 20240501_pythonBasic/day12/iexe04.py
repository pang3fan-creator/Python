class MyClass:
    def __init__(self, name):
        self.name = name
        self.age = 20

    def display(self):
        print(self.name)


my = MyClass('kim')
print(my.__dict__)
my.__dict__ = {'name': 'lee', 'age': 30}
print(my.__dict__)

