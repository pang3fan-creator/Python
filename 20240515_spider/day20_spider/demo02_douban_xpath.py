"""
    demo02_douban_xpath.py
    xpath爬取豆瓣电影top250的信息
"""
import time
import random
import requests
from lxml import etree
from ua_pool import ua_list


class DouBanSpider:
    def __init__(self):
        pass

    def get_html(self, url):
        return requests.get(url=url, headers={"User-Agent": random.choice(ua_list)}).text

    def parse_html(self, html):
        eobj = etree.HTML(html)
        li_list = eobj.xpath('//ol[@class="grid_view"]/li')
        for li in li_list:
            item = {}
            # 电影名称
            title_list = li.xpath('.//a/span[1]/text()')
            item["title"] = title_list[0] if title_list else None

            # 主演
            actor_list = li.xpath('.//div[@class="bd"]/p[1]/text()')
            item["actor"] = actor_list[0].strip().replace("\xa0", " ") if actor_list else None

            # 评论
            score_list = li.xpath('.//span[@class="rating_num"]/text()')
            item["score"] = float(score_list[0].strip()) if score_list else None

            # 评价人数
            number_list = li.xpath('.//div[@class="star"]/span[4]/text()')
            item["number"] = number_list[0].strip()[:-3] if number_list else None

            # 描述
            comment_list = li.xpath('.//span[@class="inq"]/text()')
            item["comment"] = comment_list[0].strip() if comment_list else None

            print(item)

    def save_html(self, filename, html):
        pass

    def crawl(self):
        for page in range(1, 11):
            # 拼接1页地址
            start = (page - 1) * 25
            page_url = f"https://movie.douban.com/top250?start={start}"
            # 爬取1页数据
            page_html = self.get_html(url=page_url)
            # 解析1页数据
            self.parse_html(page_html)
            print(page)
            # 控制爬取频率
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()


























