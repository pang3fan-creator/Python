if __name__ == '__main__':
    # 输入获取
    s, i = input().split()


    # 算法入口
    def getResult():
        sArr = list(s)
        sArr.sort()

        tar = sArr[int(i) - 1]
        return s.find(tar)


    # 算法调用
    print(getResult())
