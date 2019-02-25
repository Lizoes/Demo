from django.db import models

# Create your models here.


class Student(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=16)
    sid = models.IntegerField()
    phone = models.CharField(max_length=11)

