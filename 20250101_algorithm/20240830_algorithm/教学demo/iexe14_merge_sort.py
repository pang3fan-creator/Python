import random

if __name__ == "__main__":
    count = 0
    N = int(input("请输入数组长度："))
    arr = list(set(random.randint(1, 501) for i in range(N)))
    random.shuffle(arr)
    print(arr)
    list_n = []
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            list_n.append([arr[i], arr[i + 1]])
            count += 1

    print(list_n)
    print(count)
