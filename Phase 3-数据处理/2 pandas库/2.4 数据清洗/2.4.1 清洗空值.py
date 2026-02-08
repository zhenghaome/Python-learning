# 数据清洗是对一些没有用的数据进行处理的过程

import pandas as pd

# 识别空值
missing_values = ['na', 'NA', 'n/a']   # 读取csv文件，指定空数据类型（也可以不指定）
df = pd.read_csv('../property-data.csv', na_values ='missing_values')
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())   # 用isnull()判断是否是空值

# 删除包含空字段的行：dropna()
# 语法：DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
df = pd.read_csv('../property-data.csv')
new_df = df.dropna(axis = 1)   # pandas里0行1列
print(new_df.to_string())
# to_string()用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替
# 默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据
# 如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数

# 移除指定列有空值的行
df = pd.read_csv('../property-data.csv')
df.dropna(subset = 'SQ_FT', inplace = True)
print(df.to_string())

# fillna()替换一些空字段
df = pd.read_csv('../property-data.csv')
df.fillna(54321, inplace = True)
print(df.to_string())
# 替换空单元格的常用方法是计算列的均值mean()、中位数median()或众数mode()
x = df['ST_NUM'].mean()
new = df['ST_NUM'].fillna(x)
print(new.to_string())

