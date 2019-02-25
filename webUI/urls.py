from django.urls import path, re_path,include
from django.contrib import admin
from webUI import views

urlpatterns=[
    # path("cmdb/",include("cmdb.urls")),
    # path("webUI/",include("webUI.urls"))
    #path('', views.cookie),
    #path(r'admin/', admin.site.urls),
    path(r'',views.business2),
    path(r'business1/',views.business1),
    path(r'business2/',views.business2),
    path(r'business3/', views.business3),
    path(r'cookie2/',views.cookie),
    path(r'cookie_index/',views.cookie_index),
    path(r'session1_login/',views.session1_login),
    path(r'session1_index/',views.session1_index),
    path(r'test_middle_ware/',views.test_middle_ware),
    path(r'form/',views.form),
    path(r'modelform/',views.modelform),
    path(r'lookmodelform/', views.lookmodelform),
    re_path(r'host_edit-(\d+)/',views.host_edit),
    path(r'add/',views.add),
    path(r'show/', views.show)
]