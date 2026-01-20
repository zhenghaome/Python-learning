"""
需求：
读取bill.txt文件
将文件写出到bill.txt.bak文件进行备份
同时将标记为测试的数据进行丢弃
"""

f1 = open("D:/Trivial Things/Python-learning/Phase 1/文件操作/bill.txt", "r", encoding = "utf-8")
f2 = open("D:/Trivial Things/Python-learning/Phase 1/文件操作/bill.txt.bak", "w", encoding = "utf-8")

for line in f1:
    line = line.strip()
    words = line.split("，")
    if words[4] == "测试":
        continue
    else:
        f2.write(line)
        f2.write("\n")

f1.close()
f2.close()