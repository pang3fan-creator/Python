def fibonacci(length):
    if length == 1: return 1
    if length == 2: return 1
    return fibonacci(length - 1) + fibonacci(length - 2)


if __name__ == '__main__':
    res = fibonacci(int(input('请输入斐波那契数列长度:')))
    print(res)
