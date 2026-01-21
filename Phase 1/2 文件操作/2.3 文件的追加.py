# 如果文件不存在，追加功能会创建一个文件
# 如果文件本身存在，追加会在原文件后继续写入
f = open("/Phase 1/2 文件操作/测试.txt", "a", encoding ="utf-8")
f.write("\n追加一句话")
f.close()