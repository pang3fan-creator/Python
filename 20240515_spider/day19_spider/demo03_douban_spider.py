import time
import random
import requests
from ua_pool import ua_list


class DouBanSpider:
    def __init__(self):
        pass

    def get_html(self, url):
        return requests.get(url=url, headers={"User-Agent": random.choice(ua_list)}).text

    def parse_html(self):
        pass

    def save_html(self, filename, html):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    def crawl(self):
        for page in range(1, 11):
            # 拼接1页地址
            start = (page - 1) * 25
            page_url = f"https://movie.douban.com/top250?start={start}"
            # 爬取1页数据
            page_html = self.get_html(url=page_url)
            # 保存1页数据
            filename = f"./douban/第{page}页.html"
            self.save_html(filename, page_html)
            print(f"{filename}爬取成功")
            # 控制爬取频率:uniform(1,3)生成指定范围区间的浮点数
            time.sleep(random.uniform(1, 3))


if __name__ == '__main__':
    spider = DouBanSpider()
    spider.crawl()


























