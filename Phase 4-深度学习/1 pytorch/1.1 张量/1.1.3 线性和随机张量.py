import torch

# 创建线性张量
def func01():
    # torch.arange：指定范围
    t1 = torch.arange(0, 10, 2)
    print(t1)

    # torch.linspace：指定范围且等差数列
    t2 = torch.linspace(1, 10, 5)   # 闭区间，且“5”的意思是要在区间内要5个数
    print(t2)
    print('-----------------------------------------------------')

# 创建随机张量
def func02():
    # 设置随机种子（只要随机种子固定，无论在何时何地运行程序，生成的随机数序列都是完全相同的）
    #torch.initial_seed()   # 默认用当前系统的时间戳设置种子（一般不用这个）
    torch.manual_seed(3)   # 种子一旦设置，以下的张量都要按照种子创建，所以一般写在导包后面

    # torch.rand：很随机的随机张量
    t3 = torch.rand(size = (2, 3))
    print(t3)

    # torch.randn：符合正态分布的随机张量、
    t4 = torch.randn(2, 3)
    print(t4)

    # 创建随机整数张量
    t5 = torch.randint(0, 20, size = (2, 5))
    print(t5)


if __name__ == '__main__':
    func01()
    func02()