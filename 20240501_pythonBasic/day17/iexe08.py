def new_func(func):
    print(f"new_func{func}")

    def inner_func(*args):
        result = func(*args)
        print(f"inner_func")
        return result

    return inner_func


@new_func
def old_func(n, m):
    print(f"old_func {n}{m}")
    return n + m


print(old_func(666, 777))
