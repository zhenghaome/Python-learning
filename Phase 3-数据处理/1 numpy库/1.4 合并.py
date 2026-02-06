import numpy as np

# 合并多个矩阵
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a, b))   # vertical stack 垂直合并
d = np.hstack((a, b))   # horizontal stack 水平合并
print(c, d)
print(c.shape, d.shape)
print("----------------------------------------")

# 不能直接通过转置来改变一维的矩阵，因为一维矩阵在python里不是矩阵，是数组
print(np.transpose(a))   # 不行
a_1 = a.reshape((a.size,1))   #reshape可以
print(a_1)