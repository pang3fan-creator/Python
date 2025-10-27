# 输入获取
nums = list(map(int, input().split()))


def push(num, stack):
    total = num

    for i in range(len(stack) - 1, -1, -1):
        total -= stack[i]

        if total == 0:
            del stack[i:]
            push(num * 2, stack)
            return
        elif total < 0:
            break

    stack.append(num)


# 算法入口
def getResult():
    stack = [nums[0]]

    for i in range(1, len(nums)):
        push(nums[i], stack)

    stack.reverse()

    return " ".join(map(str, stack))


# 算法调用
print(getResult())
