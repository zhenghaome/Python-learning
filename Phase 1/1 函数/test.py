def func(a, b):
    return a + b

if __name__ == '__main__':   # 只有在作为独立脚本运行时才会执行 if 的代码
    print('该代码正在直接运行')
else:
    print('该代码正在作为模块导入')