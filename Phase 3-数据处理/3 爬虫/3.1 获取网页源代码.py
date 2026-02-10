"""
一、定义
http（超文本传输协议）：是客户端和服务器请求和响应协议（浏览器就可以是一个客户端）

二、分类：
1. get方法：获得数据（例如浏览网页）
2. post请求：创建数据（例如登录输入密码）

三、完整的http请求的构成
1. 请求行
   · 方法（Method）：表示你想对资源做什么。最常见的有：
     · GET：请求获取数据（例如，加载网页）。
     · POST：提交数据（例如，提交登录表单）。
     · PUT / DELETE：更新或删除数据（常用于API）。
   · URL路径：你想访问的资源位置（例如，/index.html 或 /api/users）。
   · HTTP版本：使用的协议版本（例如，HTTP/1.1）。
2. 请求头
   · 一系列“键值对”，向服务器传递附加信息。例如：
     · User-Agent：告诉服务器你用的浏览器和操作系统类型。
     · Accept：告诉服务器你希望接收什么类型的数据（如HTML、图片、JSON）。
     · Authorization：携带身份验证信息（如令牌）。
     · Content-Type：（在POST/PUT请求中）告诉服务器你发送过去的数据是什么格式（如JSON）。
3. 请求体
   · 可选部分。主要在 POST、PUT 等方法中使用，用于承载要发送给服务器的数据。例如，你填写的用户名、密码、发布的文章内容等就放在这里。

四、用requests库发送请求（例如response接收请求）
response.text：获得网页的html源码
response.ok：能知道请求是否成功，成功显示 True

   https://books.toscrape.com/ 可以专门练习爬虫
"""

import requests

response = requests.get('https://movie.douban.com/top250')   # 直接打印出来http状态码是418，是请求失败

# 用一个请求头把程序伪装成浏览器
# 随便打开一个网页-右键-检查-Network-刷新网页-随便点进一个http请求-Request Headers-复制它的User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
response1 = requests.get('https://movie.douban.com/top250', headers = headers)
print(response1)   # 能得到请求状态
print(response1.text)   # 能得到html源码


