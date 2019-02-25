from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render , redirect
import os

USER_LIST=[
    {"username":"lizo","email":"1@163.com","gender":"boy"}
]

USER_DICT={
    "1":{"name":"lizo","age":16},
    "2":{"name":"Rizo","age":13},
    "3":{"name":"Kizo","age":14},
    "4":{"name":"Jizo","age":17}
}

def home(request):
    if request.method=="POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        data={"username":name , "email":email , "gender":gender}
        USER_LIST.append(data)
    return render(request,"show_msg.html",{"user_list":USER_LIST})

def login(request):
    # f=open("templates/login.html",'r',encoding="utf-8")
    # data=f.read()
    # return HttpResponse(data)
    return render(request,"login.html")

def login2(request):
    msg=""
    if request.method=="POST":
        user=request.POST.get("user",None)
        psd=request.POST.get("psd",None)
        if user=="lizo" and psd=="123":
            return redirect("http://www.baidu.com")
        else:
            msg="账号或者密码错误"

    return render(request,"login.html",{"error_msg":msg})

def check(request):
    if request.method=="POST":
        u = request.POST.get("user",None)
        p = request.POST.get("psd",None)
        g = request.POST.get("gender",None)
        choice = request.POST.getlist("char")
        city=request.POST.get("city",None)

        obj=request.FILES.get("file")
        print(obj,obj.name)

        # 获取project下的upload目录，然后把问价名加到后面，组合成新的路径
        path=os.path.join("upload",obj.name)
        f=open(path,mode="wb")
        for item in obj.chunks():
            f.write(item)
        f.close()

        print("name=%s , password=%s , gender=%s"%(u,p,g))
        print("choice=",choice)
        print("city=", city)

    return render(request,"upload_img.html")


from django.views import View

class TC(View):
    def dispatch(self, request, *args, **kwargs):
        print("before")
        result=super(TC, self).dispatch(request, *args, **kwargs)
        print("after")
        return result

    def get(self,request):
        print(request.method)
        return render(request,"tc.html")
    def post(self,request):
        print(request.method)
        return render(request, "tc.html")

# def index(request,nid):
#     nid=request.method.GET.get("nid")
#     return render(request,"zhengze.html",{"nid":nid})

from django.urls import reverse
def index(request,nid,uid):
    url=reverse("myindex",kwargs={"nid":66,"uid":99})
    print(url)
    info=request.path_info
    return render(request,"index.html",{"url_info":info,"dic":USER_DICT})

# def detail(request):
#     nid=request.GET.get("nid")
#     info=USER_DICT[nid]
#     return render(request, "detail.html", {"info": info})

def detail(request,nid):
    info=USER_DICT[nid]
    return render(request, "detail.html", {"info": info})

def detail2(request,nid,uid):
    print("nid=",nid,"uid=",uid)
    info=USER_DICT[nid]
    return render(request, "detail.html", {"info": info})

from cmdb import models as mo
def orm(request):
    # 增
    '''
    mo.User.objects.create(name="Lizo",age=18)
    mo.User.objects.create(name="Rizo", age=27)
    mo.User.objects.create(name="Kizo", age=29)
    mo.User.objects.create(name="Hizo", age=18)
    mo.User.objects.create(name="ooo", age=30)
    '''
    # 查
    '''
    result=mo.User.objects.filter(age=18)
    print("result=",result,"\n","类型:",type(result))
    for line in result:
        print("name:",line.name,"age:",line.age)
    '''
    # 删
    '''
    result_delet=mo.User.objects.filter(name="ooo")
    result_delet.delete()
    '''
    # 改
    result_update=mo.User.objects.filter(name="Hizo")
    result_update.update(age=28)

    return HttpResponse("o文明k")