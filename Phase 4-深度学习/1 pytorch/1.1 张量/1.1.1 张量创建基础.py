"""
张量是一个元素为同一种类型的多维数组，可以是标量、向量、矩阵或更高维度的数据结构。
在 PyTorch 中，张量（ Tensor）是数据的核心表示形式，类似于 NumPy 的多维数组，但具有更强大的功能，例如支持 GPU 加速和自动梯度计算。
张量支持多种数据类型（整型、浮点型、布尔型等），但是必须是数值。
张量可以存储在 CPU 或 GPU 中，GPU 张量可显著加速计算。
"""

# 导包
import torch
import numpy as np

# 1. torch.tensor：根据指定数据创建张量
def func01():
    # 标量张量（一维）
    t1 = torch.tensor(10)
    print(f"t1的值为：{t1}，类型为：{type(t1)}")
    print('-----------------------------------------------------------')

    # 二位数组转张量
    data = [[1,2,3], [4,5,6]]
    t2 = torch.tensor(data)
    print(f"t2的值为：{t2}，类型为：{type(t2)}")
    print('-----------------------------------------------------------')

    # numpy 数组转张量
    arr = np.random.randint(10, size = (2, 5))
    t3 = torch.tensor(arr)
    print(f"t3的值为：{t3}，类型为：{type(t3)}")
    print('-----------------------------------------------------------')

# 2. torch.Tensor：在 tensor 基础上，还能根据形状创建张量
def func02():
    t4 = torch.Tensor(2, 3)   # 创建2行3列张量
    print(f"t4的值为：{t4}，类型为：{type(t4)}")
    print('-----------------------------------------------------------')

#  3. IntTensor，FloatTensor，DoubleTensor：在 tensor 基础上，能强制转换数据类型（张量中默认 float32）
def func03():
    t5 = torch.FloatTensor([1,2,3])
    print(f"t5的值为：{t5}，类型为：{type(t5)}")   # int 转成 float


if __name__ == "__main__":
    func01()
    func02()
    func03()