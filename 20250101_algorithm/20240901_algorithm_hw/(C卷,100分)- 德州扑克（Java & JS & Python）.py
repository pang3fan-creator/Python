def judge_cards(num):
    if num == "J":
        return 11
    elif num == "Q":
        return 12
    elif num == "K":
        return 13
    elif num == "A":
        return 14
    else:
        return int(num)


def countNums(list_c, first_c, second_c):
    count = {}
    for num in list_c: count[num] = count.get(num, 0) + 1
    count_v = sorted(count.values(), reverse=True)
    return count_v[0] == first_c and count_v[1] == second_c


def case1(list_c):
    return countNums(list_c, 4, 1)


def case2(list_c):
    return countNums(list_c, 3, 2)


def case3(list_c):
    return countNums(list_c, 3, 1)


def case4(list_c):
    return countNums(list_c, 2, 2)


def case5(list_c):
    return countNums(list_c, 2, 1)


def is_shunzi(list_c):
    for i in range(1, len(list_c), 1):
        if list_c[i] - list_c[i - 1] != 1: return False
    return True


def is_tonghua(list_suit):
    return len(set(list_suit)) == 1


if __name__ == '__main__':
    while True:
        try:
            list_cards = [input().strip().split(' ') for _ in range(5)]
            list_c = sorted(map(lambda x: judge_cards(x[0]), list_cards))
            list_suit = list(map(lambda x: x[1], list_cards))
            if case1(list_c):
                print(2)
            elif case2(list_c):
                print(3)
            elif case3(list_c):
                print(6)
            elif case4(list_c):
                print(7)
            elif case5(list_c):
                print(8)
            elif is_shunzi(list_c) and is_tonghua(list_suit):
                print(1)
            elif is_shunzi(list_c):
                print(5)
            elif is_tonghua(list_suit):
                print(4)
            else:
                print(0)
        except:
            break
