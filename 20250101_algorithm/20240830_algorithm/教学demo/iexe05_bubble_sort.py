import random
import time


# 冒泡
def bubble_sort(list):
    for i in range(0, len(list) - 1, 1):
        for j in range(i + 1, len(list), 1):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


if __name__ == '__main__':
    random.seed(5)
    list = [i for i in range(1000)]
    random.shuffle(list)
    a = time.time()
    print(bubble_sort(list))
    b = time.time()
    print(b - a)
