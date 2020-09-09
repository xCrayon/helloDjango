from django.urls import path
from mainapp.views import user_list, user_list2, user_list3, add_user, \
    update_user, delete_user, find_fruit, find_store, all_store, count_fruit

urlpatterns = [
    path('list', user_list3),
    path('add', add_user),
    path('update', update_user),
    path('delete', delete_user),
    path('find', find_fruit),
    path('all', all_store),
    path('count', count_fruit),
]
