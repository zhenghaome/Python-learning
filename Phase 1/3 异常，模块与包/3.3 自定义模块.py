import my_module1
my_module1.test1(1, 2)

# 导入不同模块的同名函数，会被后一个覆盖
from my_module1 import test1
from my_module2 import test1
test1(2, 3)

# __main__变量
# python程序中内置一个变量__name__，运行这个程序时，这个变量会被标记为__main__，使得程序被运行
# 如果没有这句if，在调用这个模块时，仅仅一句import就会让程序运行，丧失传数据的权力
# 但是my_module1里的test的本意其实是调试这个模块
from my_module1 import test1
test1(1, 2)

# __all__变量
# 原本*可以导入整个模块，有了__all__之后只能导入all指定的test2
# 但是all只对*起作用，手动导入test1是可以的
from my_module1 import *
test2(1, 2)