class Animal:
    # def __init__(self):
    #     self.name = '动物'

    def eat(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__()
        self.name = name

    def eat(self):
        print(self.name + '吃骨头')

    def run(self):
        print(self.name + '跑的快')


class Bird(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def eat(self):
        print(self.name + '吃虫子')

    def fly(self):
        print(self.name + '飞得飞快')


dog_qq = Dog('钱钱')
dog_qq.eat()
dog_qq.run()
print(isinstance(dog_qq, Animal))
print(issubclass(Dog, Animal))
bird_mm = Bird('萌萌')
bird_mm.eat()
bird_mm.fly()
