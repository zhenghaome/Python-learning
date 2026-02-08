import pandas as pd

# 第三个日期格式错误
data = {'date': ['2026/02/01', '2026/02/02', '20260203'],
        'duration': [30,40,50]}
df = pd.DataFrame(data, index = ['day1', 'day2', 'day3'])

df['date'] = pd.to_datetime(df['date'], format = 'mixed')
print(df)
# 还有其它格式清洗......