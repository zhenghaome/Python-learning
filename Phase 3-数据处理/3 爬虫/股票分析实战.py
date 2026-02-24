import requests
import pandas as pd
import time


# 创建会话对象来维持cookie
session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://xueqiu.com/hq',
    'X-Requested-With': 'XMLHttpRequest'
}

# 先访问雪球网首页，获取服务器设置的cookies，然后等待1秒避免请求过快被封
session.get('https://xueqiu.com/', headers = headers)
time.sleep(1)

# 尝试直接获取JSON数据
api_url = 'https://xueqiu.com/service/v5/stock/screener/quote/list'

params = {
    'page': 1,               # 第1页数据
    'size': 90,              # 每页90条
    'order': 'desc',         # 降序排列
    'orderby': 'percent',    # 按涨幅排序
    'order_by': 'percent',   # 另一个排序参数
    'market': 'CN',          # 中国市场
    'type': 'sha',           # 沪A股票
    'first_name': '0',       # 一级分类
    'second_name': '3'       # 二级分类
    }

response = session.get(api_url, headers = headers, params = params)
response.encoding = 'utf-8'

# 检查响应状态
if response.status_code == 200:
    all_data = response.json()
    print(all_data)

df = pd.DataFrame(all_data['data']['list'])
df.to_csv('stock.csv', index = False)




