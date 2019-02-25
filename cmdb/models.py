from django.db import models

# Create your models here.

class User(models.Model):
    #创建表结构，默认增加id列，并且是自增的，是主键
    name=models.CharField(max_length=32)
    age=models.IntegerField()
