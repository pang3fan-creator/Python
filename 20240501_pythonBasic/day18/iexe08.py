from pathlib import Path


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # def __str__(self):
    #     return f"{self.name} {self.age} {self.sex}"

    def __repr__(self):
        return f"Student('{self.name}', {self.age}, '{self.sex}')"


s1 = Student("张三", 18, "男")
print(s1)
file_1 = Path("../student.txt")
with open(file_1, "w", encoding="utf-8") as f:
    f.write(s1.__repr__())
with open(file_1, "r", encoding="utf-8") as f:
    s2 = eval(f.read())
    print(s2.name)
    print(s2)
