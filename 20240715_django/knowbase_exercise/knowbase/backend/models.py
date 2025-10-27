# Create your models here.
from django.db import models

# 文章分类
class Category(models.Model):
    # 分类名称
    catename = models.CharField(max_length=100)
    # 显示顺序
    sort_order = models.PositiveSmallIntegerField(default=1)
    # 文章数量
    article_number = models.PositiveIntegerField(default=0)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 数据表名称
        db_table = 'knowbase_category'
        # 默认排序字段,以sort_order和article_number降序排列
        ordering = ['-sort_order', '-article_number']


# 作者等级
class AuthorLevel(models.Model):
    # 等级名称
    level_name = models.CharField(max_length=30)
    # 积分
    integral = models.PositiveSmallIntegerField(default=0)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 数据表名称
        db_table = 'knowbase_author_level'


# 作者基本信息
class AuthorBasicInfo(models.Model):
    # 用户名
    username = models.CharField(max_length=30, unique=True)
    # 密码
    password = models.CharField(max_length=32)
    # 用户昵称
    nickname = models.CharField(max_length=30)
    # 用户头像
    face = models.CharField(max_length=50,default='4e701907jw1e8qgp5bmzyj2050050aa8.jpg')
    # 文章数量
    article_number = models.PositiveIntegerField(default=0)
    # 用户等级(外键,一对多)，字段名称最终为 level_id
    level = models.ForeignKey(AuthorLevel, on_delete=models.CASCADE)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 数据表名称
        db_table = 'knowbase_author_basic_info'
        ordering = ['-article_number', '-created_at']


# 作者详细信息
class AuthorDetailInfo(models.Model):
    # 真实姓名
    realname = models.CharField(max_length=50)
    # 性别:False表示男,True表示女
    gender = models.BooleanField(default=False)
    # 出生日期
    birthday = models.DateField(null=True)
    # 通讯地址
    address = models.CharField(max_length=100)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)
    # 用户ID，(外键,一对一)，字段名称最终为 user_id
    author = models.OneToOneField(AuthorBasicInfo, on_delete=models.CASCADE)

    class Meta:
        # 数据表名称
        db_table = 'knowbase_author_detail_info'


# 文章信息
class Article(models.Model):
    # 文章标题
    subject = models.CharField(max_length=100)
    # 文章正文
    content = models.TextField()
    # 作者ID，(外键,一对多)，字段名称最终为 author_id
    author = models.ForeignKey(AuthorBasicInfo, on_delete=models.CASCADE)
    # 分类ID，(外键,一对多)，字段名称最终为 category_id
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 是否放入回收站:False表示未放入回收站,True表示放入回收站
    is_deleted = models.BooleanField(default=False)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 数据表名称
        db_table = 'knowbase_article'
        # 排序字段
        ordering = ['-created_at', '-is_deleted']
