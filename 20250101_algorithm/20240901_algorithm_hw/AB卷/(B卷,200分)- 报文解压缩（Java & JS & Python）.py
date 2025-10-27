# 算法入口
def getResult(s):
    stack = []

    # idxs记录要被重复的子串的起始位置
    idxs = []
    # nums记录要被重复的子串的重复次数，和idxs对应
    nums = []

    # tmpRepeatCount记录重复次数的的字符组成
    tmpRepeatCount = []

    # 遍历输入的字符串，c是当前正在遍历的字符
    for c in s:
        if c == '[':
            # 此时tmpRepeatCount已记录完当前重复子串对应的重复次数的所有字符
            repeatCount = int("".join(tmpRepeatCount))
            nums.append(repeatCount)
            tmpRepeatCount = []

            # 记录要被重复的子串的起始位置
            idxs.append(len(stack))
        elif c == ']':
            # 需要被重复的子串在栈中的起始位置
            start = idxs.pop()
            # 需要被重复的次数
            repeatCount = nums.pop()
            # 需要被重复的子串
            repeatStr = "".join(stack[start:])

            # 先删除要被替换的子串，然后加入新串（即重复对应次数的子串）
            stack = stack[:start]
            stack.append("".join([repeatStr] * repeatCount))
        elif '0' <= c <= '9':
            tmpRepeatCount.append(c)
        else:
            stack.append(c)

    return "".join(stack)


if __name__ == '__main__':
    # 输入获取
    s = input()
    # 算法调用
    print(getResult(s))
