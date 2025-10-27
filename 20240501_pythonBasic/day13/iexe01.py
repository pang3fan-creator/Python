class Vehicle:
    def run(self):
        pass


class Car(Vehicle):
    def run(self):
        print("开车去东北")


class Airplane(Vehicle):
    def run(self):
        print("开飞机去东北")


class Person:
    def __init__(self, name, vehicle: Vehicle):
        self.name = name
        self.vehicle = vehicle

    def p_drive(self):
        self.vehicle.run()

    def __eq__(self, other):
        pass
person_laoli = Person("老李", Car())
person_laoli_1 = Person("老李", Airplane())
print(person_laoli == "老李")
