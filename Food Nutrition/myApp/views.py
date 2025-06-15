from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from myApp.models import User
from .utils.error import *
from .utils import  getHomeData
from .utils.getPublicData import getAppleData


# Create your views here.

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user=User.objects.get(name=uname,password=pwd)
            request.session['name']=user.name
            return  redirect('/myApp/index')
        except:
            messages.error(request, '用户名或密码出错！')
            return redirect('/myApp/login')

def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html')
    else:
        uname = request.POST.get('signup-name')
        pwd = request.POST.get('signup-password')
        checkPwd = request.POST.get('signup-checkpassword')
        print(f"接收到的用户名：{uname}")
        # 检查两次密码是否一致
        if pwd != checkPwd:
            messages.error(request, '两次输入的密码不一致，请重新输入！')
            return redirect('/myApp/signup')

        try:
            # 创建用户
            User.objects.create(name=uname, password=pwd)
            messages.success(request, '注册成功！请登录。')
            return redirect('/myApp/login?success=1')
        except Exception as e:
         messages.error(request, f'注册失败：{str(e)}')
         return redirect('/myApp/signup')

def logout(request):
    request.session.clear()
    return  redirect('login')

def index(request):
    uname=request.session.get('name')
    print(uname)
    userinfo=User.objects.get(name=uname)
    return render(request,'index.html',{
        'userinfo':userinfo
    })

def account(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'account.html', {
        'userinfo': userinfo
    })

def changePassword(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'resetPassword.html', {
        'userinfo': userinfo
    })

def foodCategory(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'foodCategory.html', {
        'userinfo': userinfo
    })

def foodData(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'foodData.html', {
        'userinfo': userinfo
    })

def charts(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'charts.html', {
        'userinfo': userinfo
    })

def recommend(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'recommend.html', {
        'userinfo': userinfo
    })

def help(request):
    uname = request.session.get('name')
    print(uname)
    userinfo = User.objects.get(name=uname)
    return render(request, 'help.html', {
        'userinfo': userinfo
    })

def apple_data_view(request):
    apple_data = getAppleData()
    return render(request, 'index.html', {'apple_data': apple_data})












