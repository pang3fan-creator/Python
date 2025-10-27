import random

fun_1 = lambda x, y: x > y
fun_2 = lambda x, y: print(x, y)
fun_3 = lambda: random.randint(1, 5)
print(fun_1(1, 2))
print(fun_2(1, 2))
print(fun_3())
