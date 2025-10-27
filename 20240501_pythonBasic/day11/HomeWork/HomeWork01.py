class Movie:
    def __init__(self, name, index=0):
        self.name = name
        self.index = index


def fun1(p1, p2):
    p1 = Movie("八角笼中", 123)
    p2.num = 456


m1 = Movie("八角笼中")
m2 = Movie("封神")
fun1(m1, m2)
print(m1.index)  # ?
print(m2.index)  # ?
