from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def order_list(request, order_num, city_code):
    print(order_num, city_code)
    return render(request,
                  'list_order.html',
                  locals())


def cancel_order(request, order_num):
    # order_num订单编号是UUID类型
    print(order_num)
    return render(request,
                  'list_order.html',
                  locals())


def search(request, phone):
    return HttpResponse('hi, phone: %s' % phone)


def query(request: HttpRequest):
    # 查询参数中code
    # （1：按城市city和订单号num来查询，
    # 2：按手机号phone来查询）
    # url = reverse('order:search', args=('15100000000',))
    # return HttpResponse('hi, Query %s' % url)
    # url = reverse('order:list', args=('CSC', 1001))
    print(type(request.GET), request.GET)

    url = reverse('order:list', kwargs=dict(city_code='csc', order_num=1001))

    return HttpResponseRedirect(url)
