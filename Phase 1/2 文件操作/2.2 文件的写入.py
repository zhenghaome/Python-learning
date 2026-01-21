# 如果文件不存在，write功能会创建一个文件
# 如果文件本身存在，write功能会清空原文件重新写入
f = open("D:/test.txt", "w", encoding = "utf-8")

# write写入
f.write("hello world")
# flush刷新
# write只是把文字写入了python程序的内存，实际上没存进硬盘里
# 这样的好处是避免频繁使用write会频繁调用硬盘，降低程序的效率
f.flush()

f.close()           # close自带flush功能，不写flush也可以