"""
    demo03_doubanbook_spider.py

create database if not exists doubandb charset=utf8;
use doubandb;
create table douban_book(
    id int primary key auto_increment,
    title varchar(100),
    info varchar(500),
    score decimal(5,2),
    number int,
    comment varchar(500)
);
"""
import csv
import time
import pymysql
import random
import requests
from lxml import etree
from ua_pool import ua_list


class DouBanBookSpider:
    def __init__(self):
        # 打开文件,创建csv文件写入对象
        # gb18030
        self.f = open("doubanbook.csv", "w", encoding="utf-8", newline="")
        self.writer = csv.writer(self.f)

        # 创建数据库连接对象和游标对象
        self.conn = pymysql.connect(host="localhost", user="root", password="123456", port=3306, database="doubandb", charset="utf8")
        self.cur = self.conn.cursor()
        self.ins = "insert into douban_book(title,info,score,number,comment) values(%s,%s,%s,%s,%s)"

    def get_html(self, url):
        """请求功能函数"""
        return requests.get(url=url, headers={"User-Agent": random.choice(ua_list)}).text

    def parse_html(self, html):
        """解析功能函数"""
        eobj = etree.HTML(html)
        # 1.基准xpath:匹配25个书籍的节点对象的列表
        table_list = eobj.xpath('//table')
        # 2.依次遍历提取每本书籍的数据
        for table in table_list:
            # 字典,存储提取的每本书籍的数据
            item = {}
            # 书籍名称
            title_list = table.xpath('.//div[@class="pl2"]/a/text()')
            item["title"] = title_list[0].strip() if title_list else None

            # 书籍信息
            info_list = table.xpath('.//p[@class="pl"]/text()')
            item["info"] = info_list[0].strip() if info_list else None

            # 书籍评分
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item["score"] = float(score_list[0].strip()) if score_list else None

            # 评价人数:s = '(\n        109197人评价\n           )'
            number_list = table.xpath('.//span[@class="pl"]/text()')
            item["number"] = int(number_list[0].strip()[1:-1].strip()[:-3]) if number_list else None

            # 书籍描述
            comment_list = table.xpath('.//span[@class="inq"]/text()')
            item["comment"] = comment_list[0].strip() if comment_list else None

            print(item)
            # 将此条数据存入csv文件
            self.writer.writerow(list(item.values()))

            # 存入数据库
            self.cur.execute(self.ins, list(item.values()))
            self.conn.commit()

    def crawl(self):
        """程序入口函数"""
        for page in range(1, 11):
            start = (page - 1) * 25
            page_url = f"https://book.douban.com/top250?start={start}"
            page_html = self.get_html(url=page_url)
            self.parse_html(page_html)
            # 控制频率
            time.sleep(random.uniform(1, 3))

        # 所有页的所有数据抓取完成后关闭文件
        self.f.close()

        # 所有页的所有数据抓取完成后断开数据库连接
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    spider = DouBanBookSpider()
    spider.crawl()













