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
# print(title_list)
# 2.2 提取25个电影评分
score_list = eobj.xpath('//ol[@class="grid_view"]/li//span[@class="rating_num"]/text()')
# print(score_list)

"""
    1.首先获取每个电影信息的li节点对象的列表;
    2.然后for循环遍历,依次提取每个电影的信息
"""
eobj1 = etree.HTML(html)
# li_list: [<element li at xxx>, <element li at xxx>, ...]
li_list = eobj1.xpath('//ol[@class="grid_view"]/li')
# li: <element li at xxx>
for li in li_list:
    item = {}
    # 电影名称
    item["title"] = li.xpath('.//a/span[1]/text()')[0]
    item["actor"] = li.xpath('.//div[@class="bd"]/p[1]/text()')[0].strip().replace("\xa0", " ")
    item["score"] = float(li.xpath('.//span[@class="rating_num"]/text()')[0])
    item["number"] = int(li.xpath('.//div[@class="star"]/span[4]/text()')[0].strip()[:-3])
    item["comment"] = li.xpath('.//span[@class="inq"]/text()')[0].strip()

    print(item)








