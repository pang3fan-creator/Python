class BookModel:
    """
    Book Model
    """

    def __init__(self, title, author, isbn, borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = borrowed

    def borrow(self):
        # 将图书状态设置为已经借出
        self.borrowed = True
        print(f"{self.title}已借出")

    def return_book(self):
        # 将图书状态设置为未借出
        self.borrowed = False
        print(f"{self.title}已归还")

    def is_borrowed(self):
        # 检查图书是否借出，并返回对应的布尔值
        if self.borrowed:
            print(f"{self.title}已被借出")
        else:
            print(f"{self.title}未被借出")
        return self.borrowed


book1 = BookModel("活着", "夜瑾", "123456")
book1.borrow()
book1.return_book()
book1.is_borrowed()
