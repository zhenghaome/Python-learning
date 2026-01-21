# 自定义包
# 导入自定义包，from方式也是可以的
import my_package.pk_module1
import my_package.pk_module2

my_package.pk_module1.test1()
my_package.pk_module2.test2()

# 通过__all__变量控制import*
# __all__写在_init.py_里
from my_package import *
pk_module1.test1()

"""
安装第三方包
cmd里输入pip install 包的名称（或python -m pip install 包的名称）
如果网速太慢可以连一个清华的网站
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包的名称
"""
