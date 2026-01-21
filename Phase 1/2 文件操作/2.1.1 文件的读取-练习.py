f = open("/Phase 1/2 文件操作/word.txt", "r", encoding ="utf-8")

# 方法一
content = f.read()
count = content.count("itheima")
print(count)

# 方法二
count = 0
for line in f:
    line = line.strip()       # 去除空格和\n
    words = line.split(" ")   # 按照空格分割字符串
    for word in words:
        if word == "itheima":
            count += 1
print(count)

f.close()