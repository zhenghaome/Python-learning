"""
CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号）
其文件以纯文本形式存储表格数据（数字和文本）
"""

import pandas as pd

## 读取文件（任何读取的语法都是pd.read_xxx）
# 语法：df = pd.read_csv('data.csv', sep=';', header=0, names=['A', 'B', 'C'], dtype={'A': int, 'B': float})
    # sep：定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）
    # usecols：要读取的列名
df = pd.read_csv('nba.csv', usecols = ['Name', 'Team', 'Number'])
print(df.to_string())   # to_string()用于返回 DataFrame 类型的数据
                        # 如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替


## 写入文件（任何写入的语法都是df.to_xxx）
# 语法：df.to_csv('output.csv', index=True, header=True, columns=['A', 'B'])
    # index：是否写入行索引，默认 True 表示写入索引
    # columns：指定写入的列，可以是列的名称列表
    # mode：写入文件的模式，默认是 w（写模式），可以设置为 a（追加模式）
    # encoding：文件的编码格式，如 utf-8，latin1 等
df[:10].to_csv('data.csv', index = False)
print('成功')


## 数据处理
# head(n) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行
print(df.head(10))

# tail(n) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN
print(df.tail(10))

# info() 方法返回表格的一些基本信息
print(df.info())
