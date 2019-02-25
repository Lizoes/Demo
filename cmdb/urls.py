"""
注意：
1.path()处理字符串路由
re_path()处理正则表达式路由
2.URL字符串不以“/”开头，但要以“/”结尾
"""
from django.urls import path, re_path
from django.contrib import admin
from cmdb import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/',views.home),
    path('login/',views.login2),
    path('check/',views.check),
    path('orm/',views.orm),
    path('tc/',views.TC.as_view()),
    re_path(r'index/(?P<nid>\d+)-(?P<uid>\d)/',views.index,name="myindex"),
    re_path(r'detail-(\d+).html/',views.detail),
    re_path(r'detail-(?P<nid>\d+)-(?P<uid>\d).html/',views.detail2)
]