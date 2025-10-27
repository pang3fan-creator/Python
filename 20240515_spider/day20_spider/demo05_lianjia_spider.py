"""
    demo05_lianjia_spider.py
"""
import csv
import time
import random
import requests
from lxml import etree
from ua_pool import ua_list


class LianJiaSpider:
    def __init__(self):
        self.f = open("lianjia.csv", "w", encoding="utf-8", newline="")
        self.writer = csv.writer(self.f)

    def get_html(self, url):
        # http://httpbin.org/get
        return requests.get(url=url, headers={"User-Agent": random.choice(ua_list)}).text

    def parse_html(self, html):
        eobj = etree.HTML(html)
        li_list = eobj.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            item = {}
            # 1.小区名称
            title_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item["title"] = title_list[0].strip() if title_list else None

            # 2.小区区域
            location_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item["location"] = location_list[0].strip() if location_list else None

            # 3.房源信息
            info_list = li.xpath('.//div[@class="houseInfo"]/text()')
            item["info"] = info_list[0].strip() if info_list else None

            # 4.总价
            total_list = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
            item["total"] = float(total_list[0].strip())*10000 if total_list else None

            # 5.单价
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item["unit"] = float(unit_list[0].strip()[:-3].replace(",", "")) if unit_list else None
            print(item)
            # 存入csv文件
            self.writer.writerow(list(item.values()))

    def crawl(self):
        for page in range(1, 101):
            page_url = f"https://bj.lianjia.com/ershoufang/pg{page}/"
            page_html = self.get_html(url=page_url)
            self.parse_html(html=page_html)
            time.sleep(random.randint(1, 4))

        # 关闭文件
        self.f.close()


if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.crawl()




















