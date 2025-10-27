import json
import random
import time

import pymysql
import requests
from lxml import etree

from useragent_list import ua_list


class DouBanSpider(object):
    """第一步：确定数据来源，分析url变化的规律，导入需要用到的模块"""

    def __init__(self):
        self.__file_name = '../day21/douban/{}类型.csv'
        self.__url_type = 'https://movie.douban.com/chart'
        self.__url_total = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90&action='
        self.__web_info = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.__conn = pymysql.connect(host='localhost',
                                      port=3306,
                                      user='root',
                                      password='123456',
                                      database='douban',
                                      charset='utf8')
        self.__cur = self.__conn.cursor()

    """第二步：爬取数据，解析数据"""

    @staticmethod
    def __get_html(url_movie):
        """通用爬取"""
        html_text = requests.get(url_movie, headers={'User-Agent': random.choice(ua_list)}).text
        return html_text

    @staticmethod
    def __get_etree(html):
        """通用解析"""
        html_etree = etree.HTML(html)
        return html_etree

    def __get_type(self):
        """爬取解析电影类型"""
        list_type = self.__get_etree(self.__get_html(self.__url_type)).xpath('//div[@class="types"]//a')
        dict_type = {}
        for item in list_type:
            str_type = item.xpath('./@href')[0]
            dict_type[str_type.split('=')[1].split('&')[0]] = str_type.split('=')[2].split('&')[0]
        return dict_type

    def __get_total(self, num_type):
        """爬取电影总数"""
        html_total = self.__get_html(self.__url_total.format(num_type))
        dict_total = json.loads(html_total)
        num_total = int(dict_total.get('total'))
        return num_total // 20 if num_total % 20 == 0 else num_total // 20 + 1

    @staticmethod
    def __get_info(list_temp_movie):
        """爬取电影信息"""
        list_movie = [[item.get('rank'), item.get('title'), float(item.get('score')),
                       item.get('vote_count'), item.get('release_date')] for item in list_temp_movie]
        for item in list_movie:
            print(item)
        return list_movie

    """第三步：写入数据，设置爬取间隔"""

    def __save_file(self):
        def write_file(list_info):
            info = "insert into douban_movie(rank,name,score,people,time_1) values(%s,%s,%s,%s,%s)"
            self.__cur.executemany(info, list_info)
            time.sleep(random.randint(1, 3))

        return write_file

    """主入口，调用方法"""

    def main(self):
        id_type = self.__display(self.__get_type())
        num_total = self.__get_total(id_type)
        file_save = self.__save_file()
        for i in range(0, num_total, 1):
            html_info = self.__get_html(self.__web_info.format(id_type, i * 20))
            list_movie = self.__get_info(json.loads(html_info))
            file_save(list_movie)
        self.__cur.close()
        self.__conn.close()

    def __display(self, dict_type):
        """展示电影类型，并让用户选择"""
        for i, item in enumerate(list(dict_type)):
            if (i + 1) % 7 == 0:
                print(item)
            else:
                print(item, end=' ')
        while True:
            info_name = input('\n请输入电影类型：')
            if info_name in dict_type.keys():
                self.__file_name = self.__file_name.format(info_name)
                return dict_type.get(info_name)
            if input('是否继续？Y/N').upper() != 'Y':
                exit('退出程序')


if __name__ == '__main__':
    douban_spider = DouBanSpider()
    douban_spider.main()
