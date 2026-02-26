import torch
import numpy as np

# 张量 -> numpy
def func01():
    t1 = torch.tensor([1,2,3,4,5])
    n1 = t1.numpy()   # 这样只是浅拷贝，修改 n1 会同步改变t1
    n1_1 = t1.numpy().copy()   # 这样才是深拷贝
    print(f'n1_1：{n1_1}，类型是：{type(n1_1)}')
    print('---------------------------------------------------')

# numpy -> 张量
def func02():
    n2 = np.array([11,22,33,44])
    t2 = torch.from_numpy(n2)   # 浅拷贝
    print(f't2：{t2}，类型是：{type(t2)}')
    t2_1 = torch.tensor(n2)   # 深拷贝
    print(f't2_1：{t2_1}，类型是：{type(t2_1)}')
    print('---------------------------------------------------')

# 从标量张量提取出这个数
def func03():
    t3 = torch.tensor(100)
    value = t3.item()   # item 只能提取标量张量
    print(f'value：{value}，类型是：{type(value)}')


if __name__ == '__main__':
    func01()
    func02()
    func03()