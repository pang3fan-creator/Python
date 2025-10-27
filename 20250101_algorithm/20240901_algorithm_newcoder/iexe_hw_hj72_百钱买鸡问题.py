"""
元五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
现要求你打印出所有花一百元买一百只鸡的方式。
"""
while True:
    try:
        n = int(input())

        cock_price = 5
        hen_price = 3
        chick_price = 1 / 3

        for cock in range(100 // cock_price):
            for hen in range(100 // hen_price):
                for chick in range(100):
                    if 5 * cock + 3 * hen + chick / 3 == 100 and cock + hen + chick == 100:
                        print(f'{cock} {hen} {chick}')
    except:
        break
