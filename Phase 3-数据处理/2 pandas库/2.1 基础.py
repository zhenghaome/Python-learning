"""
pandas 是一个开源的数据分析和数据处理库，特别适用于处理结构化数据
主要引入了两种数据结构：Series 和 DataFrame
"""

import pandas as pd
import numpy as np

# Series：类似于一个一维的数组，可以存储任何数据类型，并通过标签（索引）来访问元素
# 语法：pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

ser = pd.Series([3,2,1])   # 如果不提供索引，默认从0，1，2开始
print(ser)

a = ['小明', '小红', '小王']   # 自定义索引
height = pd.Series([170,180,183], index = a, name = 'height')
print(height)
print(height['小王'])   # 根据索引找数据

# 也可以用key/value方法创建Series
stu_num = pd.Series({3:'小王', 4:'小郑', 5:'小邹'}, name = 'student number')
print(stu_num)
print("----------------------------------------")


# DataFrame：表格型的数据结构，每列可以是不同的值类型
# 创建DataFrame可以从字典、列表的列表、numpy数组和Series创建
# 语法：pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
data = np.array([[1,2,3],
                 [4,5,9],
                 [6,7,13]])
df = pd.DataFrame(data, index = [1,2,3], columns = ['num1', 'num2', 'sum'])
df['sum'] = df['sum'].astype('float')   # 设置某一行/列的数据类型
print(df)

# key/value方法
val = [{'0201':'晴', '0202':'雨', '0203':'阴'}, {'0201':'开心'}]   # key自动成为columns
df2 = pd.DataFrame(val, index = ['天气', '心情'])   # 必须要传index
print(df2)   # 没有的值会变为NaN
print(df2.loc['天气'])   # 用loc是标签索引，返回指定行的数据，如果没有行索引，默认0，1，2开始
                        # iloc是位置索引
