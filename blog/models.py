from django.db import models

# Create your models here.
from django.db import models

#文章种类
class Category(models.Model):
    caption=models.CharField(max_length=16)

#文章类型
class ArticleType(models.Model):
    caption=models.CharField(max_length=16)

#文章
class Article(models.Model):
    title=models.CharField(max_length=32)
    content=models.CharField(max_length=255)
    category=models.ForeignKey(to="Category",to_field="id",on_delete=models.CASCADE)
    articleType=models.ForeignKey(to="ArticleType",to_field="id",on_delete=models.CASCADE)