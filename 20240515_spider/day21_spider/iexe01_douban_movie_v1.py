#   静态页面：https://movie.douban.com/chart
#   动态页面，用于提取电影数量：https://movie.douban.com/j/chart/top_list_count?type=24&interval_id=100%3A90&action=
#   动态页面，用于抓取电影列表：https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20
import csv
import json
import time
import random
import requests
from lxml import etree
from useragent_list import ua_list

# 第一步：汇总所有需要的地址
file_str = '../day21/douban/{}.csv'
web_type = 'https://movie.douban.com/chart'
web_num = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90&action='
web_movie = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'

# 第二步，解析第一个地址，获取电影类型
html_type = requests.get(web_type, headers={'User-Agent': random.choice(ua_list)}).text
etree_type = etree.HTML(html_type)
list_type = etree_type.xpath('//div[@class="types"]//a')
dict_type = {}
for item in list_type:
    type_str = item.xpath('./@href')[0]
    type_name = type_str.split('=')[1].split('&')[0]
    type_id = type_str.split('=')[2].split('&')[0]
    dict_type[type_name] = type_id
print(dict_type)

# 第三步，获取电影数量
info_name = input('请输入电影类型：')
info_num = dict_type.get(info_name)
html_num = requests.get(web_num.format(info_num), headers={'User-Agent': random.choice(ua_list)}).text
dict_num = json.loads(html_num)
str_num = dict_num.get('total')

# 第四步，获取电影列表
file_name = open(file_str.format(info_name), 'w', encoding='utf-8', newline='')
file_writer = csv.writer(file_name)
file_writer.writerow(['排名', '电影名称', '评分', '评分人数', '上映时间'])
num_movie = int(str_num) // 20 if int(str_num) % 20 == 0 else int(str_num) // 20 + 1
for i in range(0, num_movie, 1):
    start = i * 20
    html_movie = requests.get(web_movie.format(info_num, i), headers={'User-Agent': random.choice(ua_list)}).text
    list_temp_movie = json.loads(html_movie)
    for item in list_temp_movie:
        file_writer.writerow([item.get('rank'), item.get('title'),
                              float(item.get('score')), item.get('vote_count'), item.get('release_date')])
        print(item.get('title'))
    time.sleep(random.randint(1, 3))
file_name.close()
