from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from user.models import Student

# Create your views here.
#原生上传文件方式
def index_view(request):
    if request.method == 'GET':
       return render(request, 'index2.html')
    elif request.method == 'POST':
        #获取请求参数
        uname = request.POST.get('uname','')
        photo = request.FILES.get('photo','')
        print(photo.name)
        import os
        print(os.getcwd())
        if not os.path.exists('media'):
             os.mkdir('media')
        #拼接路径
        with open(os.path.join(os.getcwd(),'media',photo.name),'wb') as fw:
            # photo.read() #一次性读取文件到内存
            # fw.write(photo.read())

            #分块读取，性能高
            for ck in photo.chunks():
                fw.write(ck)

        return HttpResponse('It is post request,上传成功')

    else:
        return HttpResponse('It is not post and get request!')

def upload_view(request):
    uname = request.POST.get('uname','')
    photo = request.FILES.get('photo','')
    #入库操作
    Student.objects.create(sname=uname,photo=photo)
    return HttpResponse('上传成功!')

#显示图片
def showall_view(request):
    stus = Student.objects.all()
    print(stus)
    return render(request,'show.html',{'stus':stus})