import pandas as pd
import numpy as np

df = pd.read_excel('student info.xlsx')

## 访问元素
# 访问列-通过列名访问
print(df['年龄'])

# 通过 .loc[] 访问（标签索引）
print(df.loc[:, '身高'])   # loc是行索引

# 通过 .iloc[] 访问（位置索引）
print(df.iloc[:, 0])

# 访问单个元素
print(df['体重'][1])   # 列名 + 行索引
print(df.iloc[1,4])   # 行 + 列

# 访问行-通过loc[]
print(df.loc[0])


## 修改DataFrame
# 修改列数据：直接修改
df['身高'] = [151,161,171]

# 添加新列：直接赋值


## 删除元素
# 删除行
new_df = df.drop(1)

# 删除列
new_df2 = df.drop('身高', axis = 1)   # 列标签 + axis = 1


## 统计分析
# 描述性统计：使用 .describe() 查看数值列的统计摘要
print(df.describe())

# 计算统计数据：使用聚合函数如 .sum()、.mean()、.max() 等


## 索引操作
# 重置索引
print(df.reset_index())

# 设置索引
print(df.set_index('年龄'))   # 把年龄设置为行索引


## 数据类型
# 查看数据类型
print(df.dtypes)

# 转换数据类型
df['年龄'] = df['年龄'].astype('float64')