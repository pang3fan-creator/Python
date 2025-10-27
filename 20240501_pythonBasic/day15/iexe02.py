# class PrdIterator:
#     def __init__(self, data):
#         self.__data = data
#         self.__index = 0
#
#     def next_1(self):
#         if self.__index < len(self.__data):
#             item = self.__data[self.__index]
#             self.__index += 1
#             return item
#         else:
#             raise StopIteration()


class PrdController:
    def __init__(self):
        self.commodity = []

    def add_commodity(self, *stu):
        for item in stu:
            self.commodity.append(item)

    # def __iter__(self):
    #     return PrdIterator(self.commodity)


ctrl_1 = PrdController()
ctrl_1.add_commodity("屠龙刀", "倚天剑", "金箍棒", "口罩", "酒精")
for item in ctrl_1.commodity:
    print(item)



iterator = ctrl_1.__iter__()
while True:
    try:
        item = iterator.next_1()
        print(item)  #
    except StopIteration:
        break
