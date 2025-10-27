import numpy as np
import cv2


def list_reshape(list_pic, N, M):
    list_pic_new = []
    for i in range(N):
        list_pic_new.append([])
        for j in range(M): list_pic_new[i].append(list_pic[i * M + j])
    return list_pic_new


if __name__ == '__main__':
    list_gray = list(map(int, input().split(' ')))
    x, y = map(int, input().split(' '))
    list_gray = list(zip(list_gray[0::2], list_gray[1::2]))
    N, M = list_gray.pop(0)
    list_pic = [i[0] for i in list_gray for __ in range(i[1])]
    list_pic = list_reshape(list_pic, N, M)
    print(list_pic[x][y])

    np_pic = np.array(list_pic).reshape(N, M).astype(np.uint8)
    cv2.imshow('pic', np_pic)
    cv2.waitKey(0)
