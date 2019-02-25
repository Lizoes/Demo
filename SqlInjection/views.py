from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

import pymysql
from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def post(request):
    username = request.POST.get("username", "")
    password = request.POST.get("psd", "")

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='pydb',charset='utf8' )
    cursor = conn.cursor()
    sql_select = " select * from sqlinjection_Student where username='{}' and password='{}' ".format(username, password)
    cursor.execute(sql_select)
    result = cursor.fetchall()
    return render(request,"sqlinjection.html", {"result": result})


def post2(request):
    username = request.POST.get("username", "")
    password = request.POST.get("psd", "")
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='pydb',charset='utf8' )
    cursor = conn.cursor()
    sql_select = " select * from sqlinjection_Student where username='{}' and password='{}' ".format(username, password)
    cursor.execute(sql_select)
    result = cursor.fetchall()
    return render(request,"sqlinjection.html", {"result": result})
