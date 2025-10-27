import datetime

##################### 变量 #####################
username = 'Rose'
age = 23
salary = 7986.35
score = {
    'chinese': 125,
    'english': 140,
    'math': 150
}
friends = ['Tom', 'Frank', 'David']

##################### 列表 #####################
fourclassics = ['西游记', '红楼梦', '水浒传', '三国演义']
user_objects = []
##################### 列表 #####################
book_objects = [
    {
        'id': 1,
        'bookname': '孙子兵法大全集（超值金版）',
        'price': 18.4,
        'publishing': '新世界出版社',
        'category': '历史',
        'issuingdate': datetime.datetime.strptime('12/20/2021', '%m/%d/%Y')
    },
    {
        'id': 3,
        'bookname': '甲骨文丛书·拿破仑大帝(全2册) ',
        'price': 119.5,
        'publishing': '中信出版集团',
        'category': '传记',
        'issuingdate': datetime.datetime.strptime('12/28/2021', '%m/%d/%Y')
    },
    {
        'id': 5,
        'bookname': 'JavaScript DOM编程艺术（第2版）',
        'price': 42.7,
        'publishing': '人民邮电出版社',
        'category': '计算机',
        'issuingdate': datetime.datetime.strptime('1/15/2022', '%m/%d/%Y')
    },
    {
        'id': 7,
        'bookname': '精通iOS开发 第8版',
        'price': 102.2,
        'publishing': '人民邮电出版社',
        'category': '计算机',
        'issuingdate': datetime.datetime.strptime('5/27/2022', '%m/%d/%Y')
    },
    {
        'id': 9,
        'bookname': 'UNIX网络编程 卷1 套接字联网API（第3版）',
        'price': 102.9,
        'publishing': '人民邮电出版社',
        'category': '计算机',
        'issuingdate': datetime.datetime.strptime('7/6/2022', '%m/%d/%Y')
    },
    {
        'id': 10,
        'bookname': '曾国藩的正面与侧面：1+2（套装共两册）',
        'price': 59.3,
        'publishing': '岳麓书社',
        'category': '传记',
        'issuingdate': datetime.datetime.strptime('11/9/2022', '%m/%d/%Y')
    },
    {
        'id': 11,
        'bookname': '普京传：不可替代的俄罗斯硬汉 [Mr.Putin: Operative In The Kremlin]  ',
        'price': 39,
        'publishing': '红旗出版社',
        'category': '传记',
        'issuingdate': datetime.datetime.strptime('3/5/2023', '%m/%d/%Y')
    },
]
'''
性别：True为男,False为女
学历：1为中学，2为高中，3为专科，4为本科，5为硕士
'''
student_objects = [
    {
        'name': '王伟',
        'age': 21,
        'sex': True,
        'education': 3
    },
    {
        'name': '张敏',
        'age': 19,
        'sex': False,
        'education': 4
    },
    {
        'name': '李静',
        'age': 22,
        'sex': False,
        'education': 3
    },
    {
        'name': '李强',
        'age': 22,
        'sex': True,
        'education': 1
    },
    {
        'name': '王磊',
        'age': 25,
        'sex': True,
        'education': 5
    },
    {
        'name': '李娟',
        'age': 23,
        'sex': False,
        'education': 2
    },
]
#####################友情链接#####################
friendlinks = '''
<li><a href="http://www.sina.com.cn" target="_blank">新浪</a></li>
<li><a href="http://www.163.com" target="_blank">网易</a></li>
'''
#####################文章简介#####################
description = '''
<p cms-style="font-L">据新华社北京12月27日电 美国国务院日前发布美国延伸大陆架界限地理坐标，单方面宣布在北冰洋等区域延伸大陆架的主张。俄罗斯方面对此表达强烈不满。</p>
<p cms-style="font-L">分析人士指出，美国此举目的是在周边更大范围的海域开采矿物、油气等资源。美国宣称此举依据《联合国海洋法公约》（简称《公约》），但美国并非《公约》缔约国，其主张难以被相关国家接受，将进一步激化与俄罗斯在北极地区的地缘博弈。</p>
<p cms-style="font-L"><font cms-style="font-L strong-Bold">美国主张难获认可</font></p>
'''
#####################明星作者#####################
famousauthors = [
    {
        'id': 5,
        'nickname': '如初不遇不曾识',
        'number': 1478,
        'avatar': 'avatar/0062BPdSjw8er31lceeesg302s02sglj.gif',
        'last_post': datetime.datetime.strptime('12:23:45 5/27/2023', '%H:%M:%S %m/%d/%Y')
    },
    {
        'id': 5,
        'nickname': '土星荒漠',
        'number': 1258,
        'avatar': 'avatar/6a5bdd8fjw8fcox4f4nn3j20sg0lcqbg.jpg',
        'last_post': datetime.datetime.strptime('22:5:9 6/1/2023', '%H:%M:%S %m/%d/%Y')
    },
    {
        'id': 5,
        'nickname': '真实面具',
        'number': 960,
        'avatar': 'avatar/04xbbig8rulseuvzbwlt4h3830.png',
        'last_post': datetime.datetime.strptime('2:45:33 6/2/2023', '%H:%M:%S %m/%d/%Y')
    },
    {
        'id': 5,
        'nickname': '喜吃蜂蜜',
        'number': 912,
        'avatar': 'avatar/4e701907jw1e8qgp5bmzyj2050050aa8.jpg',
        'last_post': datetime.datetime.strptime('19:33:16 6/15/2023', '%H:%M:%S %m/%d/%Y')
    },
    {
        'id': 5,
        'nickname': '一见而散',
        'number': 895,
        'avatar': 'avatar/6cedc12fly8ffgpgw3rwjj20yi0y1dhc.jpg',
        'last_post': datetime.datetime.strptime('23:56:6 7/9/2023', '%H:%M:%S %m/%d/%Y')
    }
]
