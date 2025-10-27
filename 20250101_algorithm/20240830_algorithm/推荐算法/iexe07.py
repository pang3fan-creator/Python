import numpy as np

x = np.array([[3.8, 4.5]])
w1 = np.random.normal(2, 1, (2, 3))
b1 = np.array([1, 1, 1])
y1 = np.dot(x, w1) + b1
print(y1)

w2 = np.mat(np.random.normal(0, 1, (3, 2)))
b2 = np.array([1, 1])
y2 = y1 * w2 + b2
print(y2)
