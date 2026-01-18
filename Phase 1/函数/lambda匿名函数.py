def test(compute):
    result = compute(1,2)
    print(result)
# 传入lambda匿名函数作为参数
# 语法：lambda 传入参数: 函数体（一行代码）
test(lambda x, y: x + y)