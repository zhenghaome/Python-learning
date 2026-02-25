import torch

# 1.直接创建指定类型的张量
t1 = torch.tensor([1,2,3,4], dtype = torch.float)   # float 默认 float32
print(f't1是：{t1}，元素类型是：{t1.dtype}')

# 2.创建好张量后，类型转换
# type()
t2 = t1.type(torch.int16)
print(f't2是：{t2}')

# half()/float()/double()/short()/int()/long()
# 对应 float16/32/64 和 int16/32/64
t3 = t1.double()
print(f't3是：{t3}')