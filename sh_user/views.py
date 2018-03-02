from django.shortcuts import render,redirect
from hashlib import sha1  #加密模块
from sh_user.models import User,Address
from django.http import HttpResponseRedirect,JsonResponse
from sh_goods.models import GoodInfo
from sh_user import user_decorator
# Create your views here.
# 实现自动添值
def login(request):
    uname=request.COOKIES.get('uname','') #存过用户名显示用户名 没有用户名 显示空字符串
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,'pwd':pwd,'error':0}
    try:
        url=request.META['HTTP_REFERER']
        if '/user/register'in url:raise Exception()
    except:url='/'
    response=render(request,'sh_user/login.html',context)
    response.set_cookie('url',url)
    return response

def register(request):
    return render(request,'sh_user/register.html')
@user_decorator.login    #装饰器 验证权限的目的
def shdz(request):
    adds=Address.objects.filter(uid=request.session.get('uid',''),scbz=0)
    return render(request,'sh_user/shdz.html',locals())



def login_handle(request):
    post=request.POST #接收表单请求
    uname=post.get('username')
    pwd=post.get('pwd')
    remeber=post.get('remember','0')
    print(uname)
    s=sha1()
    s.update(pwd.encode('utf8'))  #先编码
    upwd=s.hexdigest() #十六进制加密
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()
    if user:
        url=request.COOKIES.get('url','/')
        red=HttpResponseRedirect(url)
        if remeber=='1':
            red.set_cookie('uname',uname.encode('utf-8'))
            red.set_cookie('upwd',pwd)
        else:
            red.set_cookie('uname','',max_age=-1)  #cookie存在浏览器
            red.set_cookie('upwd','',max_age=-1)  #保存时间 -1 就是瞬间消失
        request.session['username']=uname
        request.session['uid']=user.id  #session存在应用里 有效时间一般半个小时 可以改期限
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request,'sh_user/login.html',context)

def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get('username','')
    pwd=post.get('pwd','')
    cpwd=post.get('cpwd','')
    uemail=post.get('email','')
    #判断密码是否相等
    if pwd!=cpwd:
        return redirect('/user/register')
    #密码加密
    #使用sha1加密
    s1=sha1()
    #sha1加密前，要先编码为比特
    s1.update(pwd.encode('utf8'))
    pwd=s1.hexdigest()
    #存入数据库
    user=User()
    user.uname=uname
    user.upwd=pwd
    user.uemail=uemail
    user.save()
    print(user.uname)
    return redirect('/user/login')

def logout(request):
    request.session.flush()  #清空所有session
    return redirect('/')

def register_exist(request):
    uname=request.GET.get('un')
    count=User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
@user_decorator.login
def user__center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list=[]
    if goodids!='':
        goodidl=goodids.split(',')
        for i in goodidl:
            goods_list.append(GoodInfo.objects.filter(pk=i).first())
            pass
    return render(request,'sh_user/个人资料.html',locals())

def userupdate(request):
    post = request.POST
    uid = request.session.get('uid', '')
    user = User.objects.filter(id=uid).first()
    user.uname=post.get('un', '')
    user.uphone = post.get('uphone','')
    user.upwd = post.get('upwd', '')
    user.uemil = post.get('uemil', '')
    user.usex=post.get('usex','')
    user.save()
    request.session['username']=user.uname
    return redirect('/')

@user_decorator.login
def add_save(request):
    post = request.POST
    aid=post.get('aid')
    print(post.get('sheng'))
    if aid:
        Address.objects.filter(id=aid).update(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
                                                  qu=post.get('qu'),detialaddr=post.get('detialaddr'),
                                                  rphone=post.get('rphone'),yzbm=post.get('yzbm'))
    else:Address.objects.create(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
                                                  qu=post.get('qu'),uid=request.session.get('uid'),detialaddr=post.get('detialaddr'),
                                                  rphone=post.get('rphone'),yzbm=post.get('yzbm'))
    return redirect('/')

@user_decorator.login
def mrdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(mrdz=1).update(mrdz=0)
    Address.objects.filter(id=dzid).update(mrdz=1)
    return redirect('/user/shdz')


@user_decorator.login
def scdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(id=dzid).update(scbz=1)
    return redirect('/user/shdz')

@user_decorator.login
def xgdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid)
    adds = Address.objects.filter(uid=request.session.get('uid', ''), scbz=0)
    return render(request, 'sh_user/shdz.html', locals())




