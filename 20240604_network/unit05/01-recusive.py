'''
递归函数(recursive),函数直接或间接调用自身

什么时候使用递归函数?

一个问题的解决方案可以拆分为若干个子问题，而子问题的解决方案与原来的方案相同

'''


def a(n):
    if n == 0:
        return 0
    else:

        return n + a(n - 1)


print(a(100))
