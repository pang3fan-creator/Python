import random
import time

import requests


class TieBaSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    def get_html(self, url):
        return requests.get(url, headers=self.headers).text

    def parse_html(self):
        pass

    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def crawl(self):
        name = input("请输入贴吧名：")
        start_page = int(input("请输入起始页码："))
        end_page = int(input("请输入结束页码："))
        for page in range(start_page, end_page + 1, 1):
            pn = (page - 1) * 50
            page_url = f'https://tieba.baidu.com/f?kw={name}&pn={pn}'

            page_html = self.get_html(page_url)
            file_name = f'./douban/{name}_{page}.html'
            self.save_html(file_name, page_html)

            print(f'第{page}页爬取成功')
            time.sleep(random.uniform(2, 4))


if __name__ == '__main__':
    tieba = TieBaSpider()
    tieba.crawl()
