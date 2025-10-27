class Movie:
    def __init__(self, name, index=0):
        self.name = name
        self.index = index


m1 = Movie("八角笼中", 123)
list_movie = [
    m1,
    Movie("封神", 456)
]
sum = 0
for item in list_movie:
    sum += item.index
print(sum)  # ?
