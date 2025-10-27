import copy


def main():
    A, B = map(int, input().split(' '))
    list_A = list(map(int, input().split(' ')))
    list_B = list(map(int, input().split(' ')))
    avg_A_B = (sum(list_A) + sum(list_B)) / 2
    for i, j in enumerate(list_A):
        temp_A = copy.copy(list_A)
        temp_A.pop(i)
        for v in list_B:
            if sum(temp_A) + v == avg_A_B: return j, v


while True:
    try:
        res = main()
        print(f"{res[0]} {res[1]}")
    except:
        break
