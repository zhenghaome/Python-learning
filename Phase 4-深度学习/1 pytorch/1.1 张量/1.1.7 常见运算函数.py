import torch

data = torch.randint(10, size = (2, 3), dtype = torch.float32)
print(data)
print('------------------------------------------')

# 计算均值：必须是 float 或 double 类型
print(data.mean())
print(data.mean(dim = 0))   # 按列计算
print(data.mean(dim = 1))   # 按行计算

# 求最值
print(data.max())   # 同样可以按行按列

# 计算总和
print(data.sum())   # 同样可以按行按列

# 计算次方
print(data.pow(3))   # 输入3就是三次方

# 计算平方根
print(data.sqrt())

# 指数计算，e^n 次方
print(data.exp())

# 对数计算
print(data.log())   # 以e为底
print(data.log2())