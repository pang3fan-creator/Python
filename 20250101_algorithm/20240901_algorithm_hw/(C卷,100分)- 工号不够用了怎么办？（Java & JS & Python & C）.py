import math

if __name__ == '__main__':
    while True:
        try:
            num_id, num_letter = map(int, input().strip().split(' '))
            x = math.log10(num_id / (26 ** num_letter))
            print(max(1, math.ceil(x)))
        except:
            break
# # 输入获取
#
#
# x, y = map(int, input().split())
#
#
# # 算法入口
# def getResult(x, y):
#     print(max(1, math.ceil(math.log10(x / math.pow(26, y)))))
#
#
# # 算法调用
# getResult(x, y)
