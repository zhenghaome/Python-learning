from bs4 import BeautifulSoup
import requests

# 获取豆瓣电影 TOP250 的电影名

# 发送请求获取豆瓣网页源代码
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
for num in range(0, 250, 25):
    content = requests.get(f'https://movie.douban.com/top250?start={num}', headers = headers)   # start那里不要打空格
    html = content.text   # 把读取到的信息用变量html保存

    # 解析html
    soup = BeautifulSoup(html, "html.parser")   # 传入bs的构造函数，html.parser是告诉解析器在解析html内容

    # 获取信息
    # findAll 功能可以根据信息特点找到信息
    # 根据分析，所有的电影标题都在span标签的class属性里，class的值是title
    # 第一个参数表示需要的信息在什么标签里(span)，attrs需要传入字典，表示在什么属性(class)，需要什么值(title)
    movie_title = soup.findAll('span', attrs = {'class': 'title'})
    # findAll会返回一个可迭代对象，需要用for循环迭代出来
    for title in movie_title:
        #print(title.string)   # 直接打印会出来很多不需要的html标签，用.string会去掉这些东西
        # 但是现在把原版标题也打印出来了，根据分析，原版标题都带“/”，只要用if判断即可
        if "/" not in title.string:
            print(title.string)
    # 这样只能爬到top250里第一页的电影，根据观察，每一页不同点在于链接上多了一个“start = 索引”，所以只需要用for循环修改链接


