"""cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from cloud.settings import DEBUG, MEDIA_ROOT
import pymysql

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def test(request):
    return render(request, 'index.html')


def save(request):
    has_register = 0
    a = request.GET
    print(a)
    userName = a.get('username')
    passWord = a.get('password')
    print(userName)
    print(passWord)

    db = pymysql.connect('127.0.0.1', 'root1', 'root', 'db2')
    cursor = db.cursor()
    sql1 = 'select * from user1'
    cursor.execute(sql1)

    all_users = cursor.fetchall()
    i = 0
    while i < len(all_users):
        if userName in all_users[i]:
            has_register = 1
        i += 1
    if has_register == 0:
        sql2 = 'insert into user1(username, password) values(%s,%s)'
        cursor.execute(sql2, (userName, passWord))
        db.commit()
        cursor.close()
        db.close()
        return HttpResponse('注册成功')
    else:
        cursor.close()
        db.close()
        return HttpResponse('该账号已存在')

def query(request):
    a = request.GET
    userName = a.get('username')
    passWord = a.get('password')
    user_tup = (userName, passWord)
    db = pymysql.connect('127.0.0.1', 'root1', 'root', 'db2')
    cursor = db.cursor()
    sql = 'select * from user1'
    cursor.execute(sql)
    all_users = cursor.fetchall()
    cursor.close()
    db.close()
    has_user = 0
    i = 0
    while i < len(all_users):
        if user_tup == all_users[i]:
            has_user = 1
            break
        i += 1
    if has_user == 1:
        return HttpResponse('登录成功')
    else:
        return HttpResponse('用户名或密码错误')

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    #path('login/', login),
    path('login.html', login),
    path('index/', index),
    path('test/', test),
    #path('register/', register),
    path('register.html', register),
    path('register.html/save', save),
    path('login.html/query', query),
    url(r'user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

from django.views.static import serve
if DEBUG:
    urlpatterns+=url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),
