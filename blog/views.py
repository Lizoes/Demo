from django.shortcuts import render
from blog import models

# Create your views here.

def article(request,*args,**kwargs):
    condition={}
    for k,v in kwargs.items():
        if v=="0":
            pass
        else:
            condition[k]=v
    article_type_list=models.ArticleType.objects.all()
    category_list=models.Category.objects.all()
    result = models.Article.objects.filter(**condition)

    content={"article_type_list":article_type_list,
             "category_list":category_list,
             "result":result,
             "arg_dict":kwargs}

    return render(request,"article.html",content)