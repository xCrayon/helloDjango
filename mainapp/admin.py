from django.contrib import admin
from mainapp.models import UserEntity, CateTypeEntity, FruitEntity, StoreEntity
from mainapp.models import RealProfile, CartEntity, FruitCartEntity, TagEntity

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    # 列表中显示的字段
    list_display = ('id', 'name', 'phone')
    list_per_page = 2  # 每一个显示记录数
    list_filter = ('id', 'phone')  # 过滤器（一般配置分类）
    search_fields = ('id', 'name')


class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')


class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'price', 'category')


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'city', 'address', 'store_type', 'logo')
    fields = ('name', 'city', 'address', 'store_type', 'logo', 'summary')


class RealProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'real_name', 'number', 'real_type')


class CartEntityAdmin(admin.ModelAdmin):
    list_display = ('user', 'no')


class FruitCartEntityAdmin(admin.ModelAdmin):
    # 显示字段可以引用关联实体对象的属性
    list_display = ('cart', 'fruit', 'fruit_price_title', 'cnt', 'price_title')

    def fruit_price_title(self, obj):
        return obj.fruit_price

    def price_title(self, obj):
        return obj.price

    fruit_price_title.short_description = '单价'
    price_title.short_description = '小计'


class TagEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_num')
    fields = ('name', 'order_num')


# 将模型增加到站点中
admin.site.register(UserEntity, UserAdmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FruitEntity, FruitAdmin)
admin.site.register(StoreEntity, StoreAdmin)
admin.site.register(RealProfile, RealProfileAdmin)
admin.site.register(CartEntity, CartEntityAdmin)
admin.site.register(FruitCartEntity, FruitCartEntityAdmin)
admin.site.register(TagEntity, TagEntityAdmin)
