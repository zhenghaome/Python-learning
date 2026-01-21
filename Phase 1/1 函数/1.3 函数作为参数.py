# 函数作为参数传入
def compute(x, y):
    return x + y
# 传入的是一种逻辑
def test(a):
    result = compute(2, 3)
    print(f'compute数据类型是{type(compute)}')
    print(f'计算结果是{result}')

test(compute)