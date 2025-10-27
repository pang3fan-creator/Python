import csv
import json
import random
import time

import requests
from lxml import etree

from ua_pool import ua_list


class FilmSpider:
    def __init__(self):
        self.file_name = open('dongtai.csv', 'w', encoding='utf-8')
        self.writer = csv.writer(self.file_name)

    def get_headers(self):
        """随机获取一个User-Agent"""
        return {'User-Agent': random.choice(ua_list)}

    def get_html(self, url):
        """获取网页内容"""
        return requests.get(url, headers=self.get_headers()).text

    def parse_html(self, html):
        """解析网页内容"""
        list_html = json.loads(html)
        list = []
        for dic in list_html:
            item = {"排名": dic.get('rank'),
                    '名字': dic.get('title'),
                    '评分': dic.get('score')}
            list.append([dic.get('rank'),
                         dic.get('title'),
                         dic.get('score')])
        return list

    def get_type_dict(self):
        """获取大字典"""
        self.file_name.write('排名,名字,评分\n')
        index_url = "https://movie.douban.com/chart"
        index_htl = self.get_html(index_url)
        eobj = etree.HTML(index_htl)
        href_list = eobj.xpath('//div[@class="types"]/span/a/@href')
        type_dict = {}
        for href in href_list:
            key = href.split('?')[1].split('&')[0].split('=')[1]
            type_value = href.split('?')[1].split('&')[1].split('=')[1]
            type_dict[key] = type_value
        return type_dict

    def crawl(self):
        """爬取数据"""
        dict_type = self.get_type_dict()
        nemu = '|'.join(list(dict_type.keys()))
        info = input('请输入要爬取的类型(%s):' % nemu)
        if info in dict_type.keys():
            type_id = dict_type.get(info)
        else:
            print('输入有误')
            return
        total_page = self.get_total_count(type_id)
        for page in range(1, total_page):
            start = (page - 1) * 20
            page_url = f'https://movie.douban.com/j/chart/top_list?type={type_id}&interval_id=100%3A90&action=&start={start}&limit=20'
            page_html = self.get_html(page_url)
            page_values = self.parse_html(page_html)
            time.sleep(random.randint(1, 3))
            self.save_data(page_values)
            self.file_name.close()
            return

    def get_total_count(self, type_id):
        """获取总页数"""
        url = f'https://movie.douban.com/j/chart/top_list_count?type={type_id}&interval_id=100%3A90&action='
        html = self.get_html(url)
        total_count = int(json.loads(html).get('total'))
        total_page = total_count // 20 if total_count % 20 == 0 else total_count // 20 + 1
        return total_page

    def save_data(self, page_values):
        self.writer.writerows(page_values)


if __name__ == '__main__':
    spider = FilmSpider()
    spider.crawl()
