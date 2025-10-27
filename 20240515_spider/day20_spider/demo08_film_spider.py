"""
    demo08_film_spider.py
    豆瓣电影动态加载全站数据抓取
"""
import json
import time
import random
import requests
from lxml import etree
from ua_pool import ua_list


class FilmSpider:
    def __init__(self):
        pass

    def get_headers(self):
        """功能函数1:生成headers"""
        return {"User-Agent": random.choice(ua_list)}

    def get_html(self, url):
        """功能函数2:获取响应内容-字符串"""
        return requests.get(url=url, headers=self.get_headers()).text

    def get_total_count(self, type_value):
        """
        功能函数3：获取电影总数
        """
        total_url = f"https://movie.douban.com/j/chart/top_list_count?type={type_value}&interval_id=100%3A90&action="
        # total_html: '{"total":944, ...}'
        total_html = self.get_html(url=total_url)
        total_html = json.loads(total_html)
        total_count = total_html.get("total")

        return total_count

    def get_type_dict(self):
        """
        功能函数:获取所有类别及对应type值的大字典
        """
        index_url = "https://movie.douban.com/chart"
        index_html = self.get_html(url=index_url)
        # 解析提取数据
        eobj = etree.HTML(index_html)
        # ['/typerank?type_name=剧情&type=11&interval_id=100:90&action=', '', ...]
        href_list = eobj.xpath('//div[@class="types"]/span/a/@href')
        type_dict = {}
        for href in href_list:
            key = href.split('?')[1].split('&')[0].split('=')[1]
            type_value = href.split('?')[1].split('&')[1].split('=')[1]
            type_dict[key] = type_value

        return type_dict

    def parse_html(self, html):
        """解析提取数据"""
        # html:字符串 "[{},{},{},{},...]"
        # JSON格式的字符串 ------> Python对象[列表、字典]
        # for循环遍历,依次提取每个电影数据
        html = json.loads(html)
        for dic in html:
            item = {}
            item["rank"] = dic.get("rank")
            item["title"] = dic.get("title")
            item["score"] = dic.get("score")
            print(item)

    def crawl(self):
        # {"剧情":"11","喜剧":"24","爱情":"13", ...}
        type_dict = self.get_type_dict()
        # 剧情|喜剧|爱情|黑色电影|...
        menu = "|".join(list(type_dict.keys()))
        print(menu)
        choice = input("请输入类别:")
        type_value = type_dict[choice]

        # 1.获取该类别下的电影总数
        total_count = self.get_total_count(type_value)
        # 2.计算页数
        total_page = total_count//20 if total_count%20==0 else total_count//20 + 1

        for page in range(1, total_page + 1):
            start = (page - 1) * 20
            page_url = f"https://movie.douban.com/j/chart/top_list?type={type_value}&interval_id=100%3A90&action=&start={start}&limit=20"
            page_html = self.get_html(url=page_url)
            self.parse_html(page_html)
            # 控制爬取频率
            time.sleep(random.randint(2, 5))


if __name__ == '__main__':
    spider = FilmSpider()
    spider.crawl()















