from django.shortcuts import render,redirect
from webUI import models
from django.shortcuts import HttpResponse
# Create your views here.


def business1(request):

    v1=models.Business.objects.all()
    # QuerySet,[obj.obj,....]
    print(v1)
    print("all():",type(v1))

    v2=models.Business.objects.all().values('id','caption')
    # QuerySet,[{'id':1}.{'caption':'xx'},,....]
    print(v2)
    print("all().values():", type(v2))

    v3=models.Business.objects.all().values_list('id','caption')
    # QuerySet,[('id',1),('caption',xx),....]
    print(v3)
    print("all().values_list():", type(v3))

    return HttpResponse("jjjjj")
    # return render(request,'b usiness1.html',{'v1':v1,'v2':v2,'v3':v3})


def business2(request):


    v4=models.Host.objects.filter(nid__gt=0)
    v5=models.Host.objects.filter(nid__gt=0).values('nid','hostname','port','ip','bus__caption')
    v6=models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','ip','port','bus__caption')

    print(v4)
    print(v5)
    print(v6)
    return render(request, 'webUI/business2.html', {'v4': v4,'v5':v5,'v6':v6})
    #return HttpResponse("总站索嗨")


def business3(request):
    v = models.Business.objects.filter(id__gt=0)

    for i in v:
        if i.code=="aaa":
            print(i)
            print("tyope",type(i))
            i.delete()



    # render(request, 'webUI/business2.html', {'v4': v4,'v5':v5,'v6':v6})
    return HttpResponse("aaa")


def cookie(request):
    if request.method=="GET":
        return render(request,"cookie_login.html")
    elif request.method=="POST":
        name=request.POST.get("username",None)
        password=request.POST.get("psd",None)
        result=my_authenticate(name,password)
        if result:
            return HttpResponse("欢迎，"+name)
        else:
            return render(request, "cookie_login.html")


def cookie2(request):
    if request.method=="GET":
        return render(request,"cookie_login.html")
    elif request.method=="POST":
        name=request.POST.get("username",None)
        password=request.POST.get("psd",None)
        result=my_authenticate(name,password)
        if result:
            res=redirect("/webUI/index/")
            res.set_cookie("username00",name)
            return res
        else:
            return render(request, "cookie_login.html")

def cookie_index(request):
    u=request.COOKIES.get("username00")
    if not u:
        return redirect("cookie_login.thml")
    return render(request,"index.html",{"current_user":u})

def my_authenticate(name,password):
    user=models.Host.objects.filter(hostname=name,port=password)
    if user:
        return True
    else:
        return False

def session1_login(request):
    if request.method=="GET":
        print("in the login_get")
        return render(request,"session1_login.html")
    elif request.method=="POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        print("user=",user,"password=",password)
        print("in the login_post_before")
        if user=="Lizo" and password=="111":
            request.session["username"]=user
            request.session["password"]=password
            return redirect("/webUI/session1_index")
        else:
            #return redirect("/webUI/session1_login/")
            return render(request, "session1_login.html")

def session1_index(request):
    user=request.session["username"]
    password=request.session["password"]
    return HttpResponse("hello "+user)

def test_middle_ware(request):
    return HttpResponse("Hello，Lizo ！")



from django.forms import Form,widgets,fields
class MyForm(Form):
    #字段名需要和html中的一致，否则不能拿到
    name = fields.CharField(max_length=10,
                             min_length=3,
                             error_messages={'required': u'xx不能为空',
                                             'max_length': u'xx最多为20个字符',
                                             'min_length': u'xx最少为3个字符',
                                             'invalid': u'格式不正确',
                                             },)

    password = fields.CharField(max_length=10,
                                min_length=3,
                                error_messages={'required': u'xx不能为空',
                                                'max_length': u'xx最多为20个字符',
                                                'min_length': u'xx最少为3个字符',
                                                'invalid': u'格式不正确',
                                                },
                                 widget  = widgets.PasswordInput,
                                 #widget2 = widgets.PasswordInput(attrs={"class":"cl"}),
                                 )

    gender = fields.ChoiceField(choices=((1,"boy"),(2,"girl")),
                                initial=1,                  #默认选中1.boy
                                widget=widgets.RadioSelect,  #单选
                                error_messages = {'required': u'xx不能为空',
                                                  'max_length': u'xx最多为20个字符',
                                                  'min_length': u'xx最少为3个字符',
                                                  'invalid': u'格式不正确',
                                                  },
                                )

    email = fields.EmailField( )

def form(request):
    if request.method == "GET":
        obj=MyForm()
        return render(request,"form.html",{"obj":obj})
    elif request.method=="POST":
        obj=MyForm(request.POST)  #创建Form对象
        result=obj.is_valid()     #进行验证，返回验证的结果，True或者False
    if result:
        # modles.XX.objects.create(**obj.cleaned_data) #**是转成字典，保存到数据库
        print(obj.cleaned_data)
    else:
        print(obj.errors)
        print("---"+obj.errors['name'][0])
        return render(request,"form.html",{"obj":obj})
    return render(request,"form.html",{"obj":obj})


from django import forms
class HostModelForm(forms.ModelForm):
    class Meta:
        model=models.Host
        fields='__all__'


def modelform(request):
    if request.method=="GET":
        obj=HostModelForm()
    elif request.method=="POST":
        obj=HostModelForm(request.POST)
        obj.is_valid()
        print(obj.cleaned_data)
    return render(request, "modelform.html", {"obj": obj})

def lookmodelform(request):
    obj=models.Host.objects.all()
    return render(request, "lookmodelform.html", {"obj": obj})


def host_edit(request,id):
    host=models.Host.objects.filter(nid=id).first()
    if request.method=="GET":
        mf=HostModelForm(instance=host)
        return render(request, "host_edit.html", {"mf": mf,"id":id})
    elif request.method=="POST":
        mf=HostModelForm(request.POST,instance=host)
        if mf.is_valid():
            mf.save()
            print("host has been saved.")
        else:
            print(mf.errors)
        return render(request,"host_edit.html",{"mf":mf})

def add(request):
    dic={"choices":"M","bus_id":2,"hostname":"Lizo444","port":"8568","ip":"1.1.4.1"}
    models.Host.objects.create(**dic)
    print("asdfasdfs")
    return HttpResponse("HHHHHH")

def show(request):
    result=models.Host.objects.all().values("hostname","ip","port")
    print(type(result))
    print(result)
    return HttpResponse("HHHHHH")