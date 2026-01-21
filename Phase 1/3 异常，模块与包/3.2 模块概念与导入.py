"""
模块是python内置的一个.py文件，可以帮助我们快速使用一些功能
语法：from 模块名 import 模块/类/变量/函数/* as 别名
"""

# import基础用法
import time         # 按住ctrl点击time，可以看到time模块的源代码
print("开始")
time.sleep(5)
print("结束")
time.sleep(1)

# from用法
from time import sleep
print("第二个开始")
sleep(5)
print("第二个结束")
sleep(1)

# 通过*导入模块的全部功能
from time import *
print("第三个开始")
sleep(5)
print("第三个结束")
sleep(1)

# as加别名
import time as t
print("第四个开始")
t.sleep(5)
print("第四个结束")

