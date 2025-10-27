"""
    demo04_xpath
"""
import requests
from lxml import etree

# 1.请求
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(url="https://movie.douban.com/top250",
                    headers=headers).text

# 2.解析
eobj = etree.HTML(html)
# 知识点1：只要调用了xpath，结果一定是列表;
# 知识点2：xpath表达式末尾如果没有添加 /text() 方法，得到的是节点对象;

# 2.1 提取25个电影名称
title_list = eobj.xpath('//ol[@class="grid_view"]/li//a/span[1]/text()')
print(title_list)
# 2.2 提取25个电影评分
score_list = eobj.xpath('//ol[@class="grid_view"]/li//span[@class="rating_num"]/text()')
print(score_list)


"""
    title_list: ["肖申克的救赎","霸王别姬","大话西游之月光宝盒"]
    score_list: ["9.7","9.6","9.5"]
"""









