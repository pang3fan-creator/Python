"""
矩阵旋转
"""
import numpy as np

form = int(input("请输入要生成的数组的形状："))
arr = np.arange(0, form * form, 1).reshape(form, form)
print(arr)
index = arr.shape[0] - 1
row_y = index // 2
for i in range(row_y):
    for j in range(i, index - i):
        temp = arr[i][j]
        arr[i][j] = arr[index - j][i]
        arr[index - j][i] = arr[index - i][index - j]
        arr[index - i][index - j] = arr[j][index - i]
        arr[j][index - i] = temp
print(arr)
