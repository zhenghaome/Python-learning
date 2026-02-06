import numpy as np
# 一维
a = np.arange(2,8)
print(a[2])   # 下标从0开始
print("----------------------------------------")

# 二维
b = np.arange(3,19).reshape((4,4))
print(b)
print(b[2])   # 第3行
print(b[2][1])   # 第3行第2列
print(b[:, 1])   # 第2列全部，冒号表示这一行/列的全部
print(b[1, 1:3])   # 第2行的第2到4个值（不包括第4个）
print("----------------------------------------")

# for循环
# for循环默认迭代行
for row in b:
    print(row)
# 转置一下就可以迭代列
for column in b.T:
    print(column)
# 迭代每一项要先把矩阵变成只有一行
# flatten和flat区别在于：前者返回修改后的矩阵，后者只是一个迭代器
print(b.flatten())
for item in b.flat:
    print(item)