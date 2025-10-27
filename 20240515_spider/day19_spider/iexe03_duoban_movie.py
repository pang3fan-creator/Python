import random
import time

import requests

user_agent_pool = [
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
    'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1']


class DouBanSpider:
    def __init__(self):
        pass

    def get_pool(self):
        return random.choice(user_agent_pool)

    def get_html(self, url):
        return requests.get(url, headers={"User-Agent":self.get_pool()}).text

    def parse_html(self):
        pass

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def crawl(self):
        for i in range(1, 100, ):
            start = (i - 1) * 25
            page_url = f'https://movie.douban.com/top250?start={start}'
            page_html = self.get_html(page_url)
            file_name = f'./douban/{i}.html'
            self.save_html(file_name, page_html)
            print(f'{i}页爬取完成')
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    douban_spider = DouBanSpider()
    douban_spider.crawl()
