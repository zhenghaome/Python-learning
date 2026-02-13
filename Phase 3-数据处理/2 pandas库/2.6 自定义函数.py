"""
apply()：对 DataFrame 的‌行或列‌应用自定义函数，实现数据的批量转换、计算或处理
它本质上是用指定的函数遍历到每一行（axis=1）或每一列（axis=0）上，并返回处理后的结果
注意：apply() 操作的是 Series，不是单个元素也不是 DataFrame
"""
import pandas as pd
import numpy as np

# 语法：df.apply(func, axis=0, raw=False, result_type=None, args=0)
# func: 要应用的函数，可以是内置函数（如 np.sum）、lambda 表达式或自定义函数
# raw: 如果设置为 True，函数接收的是 NumPy 数组而非 Series，可提升性能（适用于纯数值计算）

data = np.arange(10).reshape((2,5))
df = pd.DataFrame(data, index = ['a', 'b'], columns = [1, 2, 3, 4, 5])

# 内置函数
print(df.apply(np.mean, axis = 1))   # 打印每行的平均值

# 自定义函数（分解版）
def add_column(row):
    return row[1] + row[2]   # 列索引是int，不是字符串，注意不能写row['1']
df[6] = df.apply(add_column, axis = 1)   # 加一列，这一列的值是第一列和第二列相加
print(df)

# 自定义函数（合并版）
count = df.apply(lambda row: row.max() - row.min(), axis = 1)   #计算每一行最大值与最小值之差
print(count)