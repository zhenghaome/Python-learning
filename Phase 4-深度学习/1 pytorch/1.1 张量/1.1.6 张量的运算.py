import torch

# 1. 基本运算
def basic_calculation():
    # 加法
    t1 = torch.tensor([1,2,3])
    t2 = torch.tensor([4,5,6])
    t3 = t1 + 10   # 等价于 t1.add(10)，在t1基础上每个数都加10，且不会修改源数据
    t2 += 20   # 等价于 t2.add_(10)，会修改源数据
    print(f't1:{t1}\nt2:{t2}\nt3:{t3}')
    print('---------------------------------------------------')

    # 减:sub()，乘:mul()，除（默认小数形式）:div()，取负号:neg()，用法同上


# 2. 点乘：要求两个张量维度一致，对应元素直接乘
def hadamard():
    t1 = torch.tensor([1,2,3])
    t2 = torch.tensor([4,5,6])
    print(t1 * t2)   # t1.mul(t2)也可以
    print('---------------------------------------------------')


# 3. 矩阵乘法：要求左边的行等于右边的列
def squ_mul():
    t1 = torch.tensor([[1,2,3],
                       [4,5,6]])   # 2行3列
    t2 = torch.tensor([[1,2],
                       [3,4],
                       [5,6]])   # 3行2列
    print(t1 @ t2)   # t1.matmul(t2)也可以

    # dot()：只对一维张量有效
    t3 = torch.tensor([10,11,12])
    t4 = torch.tensor([13,14,15])
    print(t3.dot(t4))   # 对应元素乘完在加起来


if __name__ == '__main__':
    basic_calculation()
    hadamard()
    squ_mul()