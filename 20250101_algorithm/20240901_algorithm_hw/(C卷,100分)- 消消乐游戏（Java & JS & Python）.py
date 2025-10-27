def main():
    stack = []
    for item in str_input:
        if not ('A' <= item <= 'Z' or 'a' <= item <= 'z'): return 0
        if len(stack) > 0 and stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    return len(stack)


if __name__ == '__main__':
    str_input = input().strip()
    print(main())
