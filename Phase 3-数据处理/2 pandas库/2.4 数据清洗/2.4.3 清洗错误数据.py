import pandas as pd

# 第三个年龄错误
data = {'name': ['小张', '小王', '小李'],
        'age': [18, 20, 12345]}
df = pd.DataFrame(data, index = [1,2,3])

# 直接替换错误数据
df.loc[3, 'age'] = 30

# 设置条件语句：e.g.将年龄大于100的都设为100
for i in df.index:
    if df.loc[i, 'age'] > 100:
        df.loc[i, 'age'] = 100

# 删除有错误数据的行
for i in df.index:
    if df.loc[i, 'age'] > 100:
        df.drop(i, inplace = True)   # drop返回新的dataframe，不会修改源数据

