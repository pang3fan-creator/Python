from django.db import models

# Create your models here.
class MemberModel(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=32)
    sex = models.BooleanField(default=0)
    age = models.PositiveSmallIntegerField(default=22)
    class Meta:
        db_table = 'testing_member'
