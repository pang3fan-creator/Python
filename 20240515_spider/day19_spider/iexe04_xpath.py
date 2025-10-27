import requests
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 "}
html = requests.get(url='https://movie.douban.com/top250', headers=headers)

e_obj = etree.HTML(html.text)
list_names = e_obj.xpath('//ol[@class="grid_view"]//a/span[1]/text()')
# print(list_names)
list_scores = e_obj.xpath('//ol[@class="grid_view"]/li//span[@class="rating_num"]/text()')
# print(list_scores)
list_nunbers = e_obj.xpath('//ol[@class="grid_view"]/li//div[@class="star"]/span[4]/text()')
# print(list_nunbers)
list_comments = e_obj.xpath('//ol[@class="grid_view"]/li//p/span[@class="inq"]/text()')
# print(list_comments)
list_orders = e_obj.xpath('//ol[@class="grid_view"]/li//em/text()')
# print(list_orders)


list_all = []
for i in zip(list_orders, list_names, list_scores, list_nunbers, list_comments):
    list_all.append({"序号": i[0], "名字": i[1],
                     "评分": i[2], "评价人数": i[3], "介绍": i[4]})
for i in list_all:
    print(i)
