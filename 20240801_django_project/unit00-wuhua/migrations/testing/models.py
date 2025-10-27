from django.db import models


class Category(models.Model):
    catename = models.CharField(max_length=30)


class Article(models.Model):
    subject = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
