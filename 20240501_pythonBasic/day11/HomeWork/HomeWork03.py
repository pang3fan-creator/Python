"""
3. 完成以下练习
   创建一个图书类 有4个属性
   title 书名 author 作者 isbn
   书号 borrowed 是否被借出 默认false

   3个函数方法：
   borrow(self)  将图书状态设置为已经借出
   return_book(self)  将图书状态设置为未借出
   is_borrowed(self)  检查图书是否借出，并返回对应的布尔值

   调用实例：
   book1 = Book("活着","夜瑾","123456")
   book1.borrow()
   book1.return_book()
   book1.is_borrowed()
"""


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    # 将图书状态设置为已经借出
    def borrow(self):
        self.borrowed = True

    # 将图书状态设置为未借出
    def return_book(self):
        self.borrowed = False

    # 检查图书是否借出，并返回对应的布尔值
    def is_borrowed(self):
        return self.borrowed


book1 = Book("活着", "夜瑾", "123456")
book1.borrow()
print(book1.is_borrowed())
book1.return_book()
print(book1.is_borrowed())

