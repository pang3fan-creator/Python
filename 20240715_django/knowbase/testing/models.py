from django.db import models

# Create your models here.
#定义数据表的结构
class Ab(models.Model):
    username = models.CharField(max_length=30,unique=True) # username VARCHAR(30) UNIQUE KEY
    password = models.CharField(max_length=32) # password VARCHAR(32)
    age = models.PositiveSmallIntegerField(default=18) # age SMALLINT UNSIGNED DEFAULT 18
    sex = models.BooleanField(default=True) # sex TINYINT(1) DEFAULT 1
    salary = models.DecimalField(max_digits=8,decimal_places=2,default=0.00) # salary DECIMAL(8,2)
    mobile = models.CharField(max_length=11,null=True) # mobile VARCHAR(11) NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at DATETIME
    updated_at = models.DateTimeField(auto_now=True) # updated_at DATETIME
    class Meta:
        db_table = 'testing_members'

class Book(models.Model):
    bookname = models.CharField(max_length=250)
    imageurl = models.CharField(max_length=80)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    publishing = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'testing_book'
