from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mainapp.models import UserEntity, FruitEntity, StoreEntity
from django.db.models import Count, Max, Min, Sum, Avg, F, Q


# Create your views here.

# 客户的用户表
def user_list(request):
    datas = [
        {'id': 1, 'name': 'crayon'},
        {'id': 2, 'name': 'ironman'},
        {'id': 3, 'name': 'stark'}
    ]
    return render(request,
                  'user/list.html',
                  {
                      'users': datas,
                      'msg': '最优秀的学员'
                  })


def user_list2(request):
    users = [
        {'id': 1, 'name': 'crayon'},
        {'id': 2, 'name': 'ironman'},
        {'id': 3, 'name': 'stark'}
    ]
    msg = '最优秀的学员'
    return render(request,
                  'user/list.html',
                  locals())


def user_list3(request):
    users = UserEntity.objects.all()
    msg = '最优秀的学员'
    return render(request,
                  'user/list.html',
                  locals())


def add_user(request):
    # 从GET请求中读取数据
    # request.GET.get('name')

    name = request.GET.get('name', None)
    age = request.GET.get('age', 0)
    phone = request.GET.get('phone', None)

    # 验证数据是否完整
    if not all((name, age, phone)):
        return HttpResponse('<h3 style="color:red">请求参数不完整</h3>', status=400)

    u1 = UserEntity()
    u1.name = name
    u1.age = age
    u1.phone = phone
    u1.save()
    return redirect('/user/list')


def update_user(request):
    # 查询参数有id, name ,phone
    id = request.GET.get('id', None)
    if not id:
        return HttpResponse('必须提供id参数', status=400)
    # 通过模型查询id的用户是否存在(表中的数据(记录)是否存在)
    try:
        # Model类.object.get() 可能会报异常 -- 尝试捕获
        user = UserEntity.objects.get(pk=int(id))
        name = request.GET.get('name', None)
        phone = request.GET.get('phone', None)
        if any((name, phone)):
            if name:
                user.name = name
            if phone:
                user.phone = phone

            user.save()
            return redirect('/user/list')

    except:
        return HttpResponse('%s 用户不存在' % id, status=404)


def delete_user(request):
    # 查询参数有id
    id = request.GET.get('id', None)
    # 验证id是否存在
    if id:
        try:
            user = UserEntity.objects.get(pk=int(id))
            user.delete()
            return redirect('/user/list')

        except:
            return HttpResponse('%s 用户不存在' % id)
    else:
        return HttpResponse('必须提供id参数', status=400)


def find_fruit(request):
    # 从查询参数中获取价格区间[price1, price2]
    price1 = request.GET.get('price1', 0)
    price2 = request.GET.get('price2', 1000)

    # 根据价格区间查询满足条件的所有水果信息
    fruits = FruitEntity.objects.filter(price__gte=price1,
                                        price__lte=price2) \
        .exclude(price=250) \
        .filter(name__contains='果') \
        .all()
    # 将查询的数据渲染到html中
    return render(request, 'fruit/list.html', locals())


def find_store(request):
    # 查询2020年开业的水果店
    # 查询参数：year
    queryset = StoreEntity.objects.filter(create_time__month__gte=8,
                                          create_time__year__lte=2020)

    first_store = queryset.first()
    stores = queryset.all().filter(city='郴州')
    return render(request, 'store/list.html', locals())


def all_store(request):
    # 返回所有水果店的json数据
    result = {}
    if StoreEntity.objects.exists():
        datas = StoreEntity.objects.values()

        store_list = []
        for store in datas:
            store_list.append(store)
        result['data'] = store_list
        result['total'] = StoreEntity.objects.count()
    else:
        result['msg'] = '数据是空的'

    return JsonResponse(result)


def count_fruit(request):
    # 返回json数据: 统计每种分类的水果数量、最高价格、最低价格
    result = FruitEntity.objects.aggregate(Count('name'),
                                           Min('price'),
                                           Max('price'),
                                           Avg('price'),
                                           Sum('price'))  # 可以 x = y 的形式

    # 中秋节：全场水果打8.8折
    # FruitEntity.objects.update(price=F('price')*0.88)
    fruits = FruitEntity.objects.values()

    # 查询价格低于1的，或高于200的水果
    fruits2 = FruitEntity.objects.filter(Q(price__lte=1) |
                                         Q(price__gte=200) |
                                         Q(Q(source='新加坡') & Q(name__contains="莲"))).values()

    return JsonResponse({
        'count': result,
        'fruits': [fruit for fruit in fruits],
        'multi_query': [fruit for fruit in fruits2]
    })
