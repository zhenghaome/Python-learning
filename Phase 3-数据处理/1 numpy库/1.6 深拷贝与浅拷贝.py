import numpy as np

# 简单赋值操作只是浅拷贝，a变了，b、c都跟着变
a = np.array([1,2,3])
b = a
c = a
a[0] = 11
print(b)
print(c)

# .copy是深拷贝，二者不会关联
A = np.array([4,5,6])
B = A.copy()
A[0] = 44
print(B)