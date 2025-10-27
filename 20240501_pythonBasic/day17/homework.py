import time


def calculate_time(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        result_time = (end - start) * 10e3
        print(f"{func.__name__}函数运行时间：{result_time:.2f}ms")
        print(f'函数运行了{result}次')

    return wrapper


@calculate_time
def display(list_numbers: list):
    count = 0
    for i in list_numbers:
        print(i)
        count += 1
    return count


list_1 = [i for i in range(100)]
display(list_1)
