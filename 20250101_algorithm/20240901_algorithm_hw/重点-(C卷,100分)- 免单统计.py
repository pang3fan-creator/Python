if __name__ == '__main__':
    N = int(input())
    list_time = sorted([input() for i in range(N)])
    stack = [list_time.pop(0)]
    for item in list_time:
        if item == stack[-1]:
            stack.append(item)
        if item[0:-4:] != stack[-1][0:-4:]:
            stack.append(item)
    print(len(stack))
