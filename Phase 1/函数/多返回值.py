def test():
    return 1, "hello", True
# 用逗号隔开返回值，就可以实现多返回值

x, y, z = test()
print(x)
print(y)
print(z)
# 变量接收时，是一一对应的
