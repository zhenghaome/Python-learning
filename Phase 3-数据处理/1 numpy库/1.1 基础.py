"""
numpy是python科学计算的基础库，基于矩阵（多维数组）计算
"""
# 基本属性
import numpy as np
arr = np.array([[1,2,3],             # 把数组转换为numpy能读懂的格式
                [4,5,6],             # 矩阵格式为：[[   ]]
                [7,8,9]])
print(arr)
print("number of dim:", arr.ndim)    # 数组的维数
print("shape:", arr.shape)           # 几行几列
print("size:", arr.size)             # 元素个数


# 生成array
a = np.array([1,2,3], dtype = np.float32)  # dtype用于确定数据类型
print(a.dtype)

# 只有0和1可以这样
b = np.zeros((2,3))
print(b)

c = np.ones((3,4))
print(c)

d = np.empty((1,2))   # empty也要定义行和列
print(d)

# 给一个范围自动生成数组
e = np.arange(10)   # arange和python的range写法一样
e1 = np.arange(10).reshape((2,5))
print(e)

# 生成线段
f = np.linspace(1, 10, 5)   # 步长为5但是分割成4段，每一段长2.25
print(f)
