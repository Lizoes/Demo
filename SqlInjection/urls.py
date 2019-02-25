from django.urls import path
from SqlInjection import views

urlpatterns = [

    path(r'login/',views.login),
    path(r'post/',views.post),
]