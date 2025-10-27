'''
通过python代码实现全连接
'''
import numpy as np

# 第一层

x = np.mat([[3.8, 4.5]])  # (1,2)

print(type(x))
w1 = np.mat(np.random.normal(0, 1, (2, 3)))  # 权重初始值一般为随机数，但不能为0
print(w1.shape)
b1 = np.array([1, 1, 1])  # 偏置的初始值一般是0 or 1
y1 = x * w1 + b1  # (1,3)

# 第二层
w2 = np.mat(np.random.normal(0, 1, (3, 2)))  # (3,2)
b2 = np.array([1, 1])
y2 = y1 * w2 + b2  # (1,2)

# 第三层(输出层)
w3 = np.mat(np.random.normal(0, 1, (2, 2)))  # (2,2)
b3 = np.array([1, 1])
pred_y = y2 * w3 + b3  # (1,2)

print(pred_y)
