from django.urls import path, re_path,include
from blog import views

urlpatterns=[
    re_path("article-(?P<articleType_id>\d+)-(?P<category_id>\d+)",views.article)
]