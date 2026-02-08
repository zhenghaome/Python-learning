import pandas as pd

# duplicated() 检查重复，如果对应的数据是重复的，会返回 True
data = {'name': ['小张', '小王', '小王', '小李'],
        'age': [18, 20, 20, 23]}
df = pd.DataFrame(data, index = [1,2,3,4])
print(df.duplicated())

# 删除重复：drop_duplicates()
df.drop_duplicates(inplace = True)
print(df)