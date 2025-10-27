# demo02_Stack.py
""" 栈:
1) 访问规则受限的线性表：只能在队尾(栈顶)添加、删除
2) 元素先进后出，后进先出
"""


class Stack:
    def __init__(self):
        self.elems = []  # 存储数据元素

    def is_empty(self):
        return len(self.elems) <= 0

    def push(self, item):  # 入栈(尾部添加元素)
        self.elems.append(item)

    def destack(self):  # 出栈(尾部删除元素)
        if self.is_empty():
            print("空栈")
            return None

        return self.elems.pop()


if __name__ == "__main__":
    s = Stack()  # 创建栈对象
    s.push(100)  # 元素压栈
    s.push(200)
    s.push(300)
    s.push(400)
    print(s.elems)  # 打印数据

    print(s.destack())  # 出栈
    print(s.destack())
    print(s.destack())
    print(s.destack())
