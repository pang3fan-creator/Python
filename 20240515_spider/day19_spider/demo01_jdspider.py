"""
    向京东官网发请求,获取到响应内容
"""
import requests


# 1.向京东官网发请求,得到响应对象
response = requests.get(url="http://httpbin.org/get",
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"})
# 2.text: 获取响应内容[字符串]:提取文本数据
html = response.text
# 3.content:获取响应内容[字节串]:抓取图片、文件、音频、视频之类的数据
# html = response.content
print(html)











