"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path, include

from django.conf.urls.static import static


# 声明views的处理函数
# view处理函数必须要求声明一个request参数，表示客户端的请求对象
# 请求对象中包含哪些信息:
#       - 请求头 headers( method, content_type, path, path_info, get_full_path(), COOKIES )
#       - 字典结构的请求信息
#           - request.COOKIES
#           - request.GET
#           - request.POST
#  请求体: body(字节类型)
def index(request: HttpRequest):
    # 加载数据模型
    users = [
        {'id': 1, 'name': 'crayon'},
        {'id': 2, 'name': 'ironman'},
        {'id': 3, 'name': 'stark'}
    ]
    # 将数据渲染搭配模板中，并将渲染之后的html响应给客户端
    return render(request, 'index.html', {'users': users,
                                          'msg': '所有用户'})
    # return HttpResponse('<h1>hi, Django</h1>'.encode('utf-8'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index),
    # 配置子路由, include()导入app模块下urls.py中声明的所有子路由
    path('user/', include('mainapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
