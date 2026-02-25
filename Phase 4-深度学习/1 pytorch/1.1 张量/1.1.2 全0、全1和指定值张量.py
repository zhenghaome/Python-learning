import torch

# 创建全1张量：ones & ones_like
t1 = torch.ones(2, 3)   # 2行3列全1张量
print(t1)

t2 = torch.tensor([[1,2], [3,4], [5,6]])   # 3行2列张量
t3 = torch.ones_like(t2)   # 模仿t2的形状，创建全1张量
print(t3)

# 创建全0张量：zeros & zeros_like（和上面一样）

# 创建指定值张量
t4 = torch.full(fill_value = 10, size = (3, 4))
print(t4)
# fill_like 同理