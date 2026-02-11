"""
pandas的排序帮助我们按特定标准对数据进行排列，而聚合则让我们对数据进行汇总，计算出各种统计量

排序是指将数据按某个列的值进行升序或降序排列
   sort_values()：根据列的值进行排序
   sort_index()：根据行或列的索引进行排序
聚合是将数据按某些规则进行汇总，通常是对某些列的数据进行求和、求平均数、求最大值、求最小值等操作
   groupby()：按某些列分组
   聚合函数：如 sum(), mean(), count(), min(), max(), std()
"""

import pandas as pd

df = pd.read_csv('nba.csv')[:10]

## 排序
# 语法：sort_values(by = ' ', ascending = )
# by表示按照哪一列排序，ascending控制升序或降序
df_sorted = df.sort_values(by = 'Age', ascending = False)   # 按照年龄降序排列
print(df_sorted.to_string())

# sort_index
df_sorted_by_index = df.sort_index(axis = 0)   # 按照行索引的升序排列
print(df_sorted_by_index.to_string())


## 聚合
# groupby()
# 语法：df.groupby(by).agg()，按指定列（by）进行分组，agg() 可以传入不同的聚合函数，进行多种操作
grouped = df.groupby(by = 'Position').agg({'Salary': 'sum'})   # 按照Position分组，并计算工资总和
print(grouped.to_string())

# 多重聚合函数
mul_grouped = df.groupby(by = 'Position').agg({'Salary': ['sum', 'mean']})  # 按照Position分组，并计算工资总和和平均数
print(mul_grouped.astype(str))   # 直接打印会显示科学计数法，转成字符串格式就可以输出

# 聚合后排序
grouped_data = df.groupby(by = 'Position')
sorted_data = grouped_data.apply(lambda x: x.sort_values(by = 'Number'))
print(sorted_data.to_string())


## 透视表
# df.pivot_table(values, index, columns, aggfunc)
# 用指定的列进行行、列分类汇总，values 是需要聚合的值，aggfunc 是聚合函数
data = df.pivot_table(values = 'Salary', index = 'Age', aggfunc = 'mean')
print(data.to_string())
