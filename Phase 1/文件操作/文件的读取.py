# 打开文件
# 语法：open(文件路径，mode，encoding)
# 一般使用f接收open函数
# encoding一定要用关键字传参是因为utf-8不是第三个参数，不使用关键字传参就不会传给encoding
f = open("D:/Trivial Things/Python-learning/Phase 1/文件操作/测试.txt", "r", encoding = "utf-8")


# 读取文件
# read(num)方式：可以指定读几个字节或者读全部
print(f.read(5))
# 读文件会默认接着继续读
print(f.read())

# readlines()方式：读取文件的全部行，存到列表中
lines = f.readlines()
print(f'lines的数据类型是{type(lines)}')
print(lines)

# readline()方法：一次读取一行
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)

# for循环方式
for line in f:
    print(line)


# 关闭文件
# 如果不关闭，文件就会一直被python程序占用
f.close()
# with open()方法：会自动关闭文件
# 语法：with open(文件路径，mode，encoding) as f:
with open("D:/Trivial Things/Python-learning/Phase 1/文件操作/测试.txt", "r", encoding = "utf-8") as f:
    print(f.read()) # 会自动关闭