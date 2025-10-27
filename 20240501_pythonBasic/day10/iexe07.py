class Movie:
    def __init__(self, name, index=0):
        self.name = name
        self.index = index

    def display(self):
        print(f"电影{self.name},热度是{self.index}")


m1 = Movie("封神", 60)
m2 = m1
m2.name = "阿凡达"

print(m2.display())
print(m1.display())
