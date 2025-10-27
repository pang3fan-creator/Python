def fun():
    a = 10
    print(f"hello{a}")

    def fun_1():
        print(f"hello{a}")

    return fun_1


res = fun()
res()
