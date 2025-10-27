class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


class ElectricCar(Car):
    def __init__(self, brand, color, battery, power):
        super().__init__(brand, color)
        self.battery = battery
        self.power = power

    def __str__(self):
        return '品牌:%s, 颜色:%s, 电池容量:%s, 充电功率:%s' % (
            self.brand, self.color, self.battery, self.power)


electric_car = ElectricCar('理想', 'white', 100, 50)
print(electric_car)
