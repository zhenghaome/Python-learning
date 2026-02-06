import numpy as np
# 一维
a = np.array([10,20,30,40])
b = np.arange(4)
print(a+b)   #加法
print(b**2)   #乘方
print(10 * np.sin(a))   # 三角函数是numpy中的函数
print(b<3)   #看小于3的数

# 多维
c = np.array([[10,20],
              [30,40]])
d = np.arange(2,6).reshape((2,2))
print(c*d)   # 直接一一对应乘
count = np.dot(c,d)   # 矩阵的点乘
count2 = c.dot(d)   # 跟上面意思一样，只是写法不同
print(count)
print(np.sum(c))   # 所有元素总和
print(np.min(c, axis = 0))   # axis表示维，0表示每一列，1表示每一行


e = np.random.random((2,2))   # 随机生成一个0和1之间的2x2矩阵
print(e)

# 一些统计操作
A = np.arange(1,13).reshape((3,4))
print(A)
print(np.mean(A))   # 平均数
print(np.median(A))   # 中位数
print(np.std(A))   # 标准差
print(np.cumsum(A))   # 累加


B = np.arange(14,2,-1).reshape((3,4))
print(B)
print(np.sort(B))   # 逐行按照从小到大排序
print(np.transpose(B))   # 逆矩阵
print(np.clip(B,5,9))   # 分割操作，让所有小于5的都等于5，所有大于9的都等于9
print(np.mean(B, axis = 1))


