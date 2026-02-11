import requests
from bs4 import BeautifulSoup

# 爬取腾讯视频前50综艺榜并保存在文档里

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
response = requests.get('https://v.qq.com/biu/ranks/?t=hotsearch&channel=10', headers = headers)
response.encoding = 'utf-8'   # 解决中文乱码问题
content = response.text

soup = BeautifulSoup(content, 'lxml')   # lxml 比 html.parser 快

all_names = soup.findAll('a', attrs = {'class' : 'name'})
all_ranks = soup.find_all('span', attrs = {'class' : 'num'})

f = open('tx name.txt', 'w', encoding = 'utf-8')

rank = 1
for name in all_names:
    f.write(f"第{rank}名：{name.string}")
    f.write('\n')
    rank += 1




