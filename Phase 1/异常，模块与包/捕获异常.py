"""
为什么要捕获异常（bug）？
提前假设某处会出现异常，提前做准备，当异常出现时，有相应手段
"""

# 捕获基本异常-语法：
# try:
#     可能出现错误的代码
# except:
#     如果出现异常执行的代码

# 捕获指定异常-语法：
# try:
#     可能出现错误的代码
# except 错误类型 as e:
#     print("balabala")
try:
    print(abc)
except NameError as e:
    print("出现变量未定义异常")

# 捕获多个异常
try:
    1 / 0
    print(variable)
except (NameError, ZeroDivisionError) as e:
    print("出现变量未定义 或者 除以0的异常")

# 捕获全部异常
try:
    1 / 0
    f = open("file.txt", "r", encoding="utf-8")
except Exception as e:
    print("出现异常")
# else表明没有异常时要执行的代码
else:
    print("没有异常")
# finally表明无论是否有异常都要执行的代码
finally:
    print("无论是否有异常都要执行")
    f.close()
# else和finally不是必须写
# 根据函数之间的层级关系，异常是会传递的
# 捕获异常时不需要深入到真正出现异常的那一句代码，在最顶级的一层依然可以进行try捕获






