from django.contrib import admin
from .models import *
# Register your models here.
admin.AdminSite.site_title = '电商管理系统'
admin.AdminSite.site_header = '电商管理系统 @weiranr'


@admin.register(MallUser)
class MallUserAdmin(admin.ModelAdmin):
    # list_display这个属性即使用于定义人员列表页显示哪些字段，列表页中的值，必须和model类中声明的字段保持一致。
    list_display = ['user_id', 'login_name', 'user_pwd', 'nick_name', 'locked', 'is_delete', 'create_time']
    # fields属性和fieldsets属性不能同时使用。因为都作用于添加页面。
    fieldsets = [
        ('用户名', {'fields': ['login_name']}),
        ('密码', {'fields': ['user_pwd']}),
        ('昵称', {'fields': ['nick_name']}),
        ('是否锁定', {'fields': ['locked']}),
        ('是否删除', {'fields': ['is_delete']}),
    ]
    search_fields = ['login_name', 'nick_name']
    # list_per_page = 20
    ordering = ('user_id',)


admin.site.register(UserAddress)
admin.site.register(UserToken)


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'goods_name', 'goods_intro', 'goods_cover_img', 'goods_carousel',
                    'goods_detail_content', 'original_price', 'selling_price', 'stock_num', 'tag', 'goods_sell_status']
    fieldsets = [
        ('商品名', {'fields': ['goods_name']}),
        ('简介', {'fields': ['goods_intro']}),
        ('图片地址', {'fields': ['goods_cover_img']}),
        ('商品地址', {'fields': ['goods_carousel']}),
        ('详细内容', {'fields': ['goods_detail_content']}),
        ('原价', {'fields': ['original_price']}),
        ('销售价', {'fields': ['selling_price']}),
        ('存库数量', {'fields': ['stock_num']}),
        ('标签', {'fields': ['tag']}),
        ('销售状态', {'fields': ['goods_sell_status']}),
    ]
    search_fields = ['goods_name', 'goods_intro']
    # list_per_page = 20
    ordering = ('goods_id',)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

admin.site.register(GoodsCategory)
admin.site.register(ShoppingCart)
admin.site.register(MallOrder)
admin.site.register(OrderItem)
admin.site.register(OrderAddress)
admin.site.register(MallCarousel)

class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['goods_id', 'config_name', ]
admin.site.register(IndexConfig)
admin.site.register(MallComment)
