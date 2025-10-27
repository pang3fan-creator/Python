"""
    demo02_tieba_spider.py
    1.请求获取响应;
    2.解析提取数据;
    3.数据处理;
"""
import time
import random
import requests


class TieBaSpider:
    def __init__(self):
        # http://httpbin.org/get
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    def get_html(self, url):
        """功能函数:获取响应内容"""
        return requests.get(url=url, headers=self.headers).text

    def parse_html(self):
        """功能函数:解析提取数据"""
        pass

    def save_html(self, filename, html):
        """功能函数:数据处理:encoding: gb18030  utf-8"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

    def crawl(self):
        """程序入口函数"""
        name = input("请输入贴吧名:")
        start_page = int(input("请输入起始页:"))
        end_page = int(input("请输入终止页:"))
        for page in range(start_page, end_page + 1):
            pn = (page - 1) * 50
            page_url = f"https://tieba.baidu.com/f?kw={name}&pn={pn}"
            page_html = self.get_html(url=page_url)
            # 赵丽颖第1页.html 赵丽颖第2页.html
            filename = f"{name}第{page}页.html"
            self.save_html(filename, page_html)
            print(f"第{page}页抓取成功")
            # 每爬取1个页面,随机休眠1-3秒钟
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = TieBaSpider()
    spider.crawl()















