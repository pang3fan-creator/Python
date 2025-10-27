from django.db import models

# Create your models here.
from django.db import models

from backend.models import Article

# Create your models here.
class User(models.Model):
    # 用户名
    username = models.CharField(max_length=30,unique=True)
    # 密码
    password = models.CharField(max_length=32)
    # 用户昵称
    nickname = models.CharField(max_length=30)
    # 用户头像
    face = models.CharField(max_length=50,default='6cedc12fly8ffgpgw3rwjj20yi0y1dhc.jpg')
    # 邮箱
    email = models.CharField(max_length=100,null=True)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        # 数据表名称
        db_table = 'knowbase_user'

class Comment(models.Model):
    # 评论内容
    content = models.CharField(max_length=200)
    # 作者ID，(外键,一对多)，字段名称最终为 author_id
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # 文章ID，(外键,一对多)，字段名称最终为 article_id
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 修改时间
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        # 数据表名称
        db_table = 'knowbase_comment'
        # 排序字段
        ordering = ['-created_at']