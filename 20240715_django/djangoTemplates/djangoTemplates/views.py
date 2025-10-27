import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def comment(request):
    return HttpResponse('OK')


#########################################

class SimpleClass:
    def __init__(self, username, age):
        self._username = username
        self._age = age
        self.flag = True

    def get_username(self):
        return self._username

    def get_age(self):
        return self._age

    def set_username(self, username):
        self._username = username

    def set_age(self, age):
        self._age = age


#########################################

def variable(request):
    sc = SimpleClass(username='Frank', age=24)
    sc.set_age(26)
    # 想像成从数据库中获取到的动态数据
    username = 'Tom'
    age = 23
    salary = 88996.25
    context = {
        'username': username,
        'age': age,
        'salary': salary,
        'friends': ['Tom', 'John', 'Rose'],
        'scores': {
            'math': 149,
            'chinese': 138,
            'english': 150
        },
        'object': sc
    }
    return render(request, 'basic/variable.html', context)


def loop(request):
    user_objects = []
    fourclassics = ['西游记', '红楼梦', '水浒传', '三国演义']
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
    context = {
        'fourclassics': fourclassics,
        'book_objects': book_objects,
        'user_objects': user_objects
    }
    return render(request, 'basic/loop.html', context)


def case(request):
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
    context = {
        'student_objects': student_objects
    }
    return render(request, 'basic/case.html', context)


def register(request):
    return render(request, 'basic/register.html')


def staticfiles(request):
    username = 'Rose'
    context = {
        'username': username
    }
    return render(request, 'basic/staticfiles.html', context)


def mediafiles(request):
    return HttpResponse('OK')


def filter(request):
    return HttpResponse('OK')
