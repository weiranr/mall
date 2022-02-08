from django.db import models

# Create your models here.


# 用户表 User
class MallUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    login_name = models.CharField(max_length=32)
    user_pwd = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=32)
    locked = models.IntegerField(default=0)
    introduce = models.CharField(max_length=100)
    is_delete = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mall_user'


# 用户地址表 User_address
class UserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    default_flag = models.IntegerField(default=0)
    province_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'user_address'


# 用户token User_token
class UserToken(models.Model):
    # user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    token = models.AutoField(primary_key=True)
    update_time = models.DateTimeField(auto_now=True)
    expire_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'user_token'


# 商品信息表 Goods_info
class GoodsInfo(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=100)
    goods_intro = models.CharField(max_length=100)
    goods_category_id = models.IntegerField(default=0)
    goods_cover_img = models.CharField(max_length=100)
    goods_carousel = models.CharField(max_length=100)
    goods_detail_content = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=64, decimal_places=2)
    selling_price = models.DecimalField(max_digits=64, decimal_places=2)
    stock_num = models.IntegerField(default=0)
    tag = models.CharField(max_length=100)
    goods_sell_status = models.IntegerField(default=0)
    # create_user = models.IntegerField(default=0)
    # create_time = models.DateTimeField(auto_now_add=True)
    # update_user = models.IntegerField(default=0)
    # update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mall_goods_info'


# 商品分类表 Goods_category
class GoodsCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_level = models.CharField(max_length=32)
    parent_id = models.CharField(max_length=32)
    category_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'mall_goods_category'


# 购物车表 Shopping_Cart
class ShoppingCart(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    # goods_id = models.ForeignKey("GoodsInfo", on_delete=models.SET_NULL, null=True)
    goods_count = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mall_shopping_cart'


# 订单表 Mall_order
class MallOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_code = models.IntegerField(auto_created=True)
    # user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=64, decimal_places=2)
    pay_status = models.IntegerField(default=0)
    pay_type = models.CharField(max_length=100)
    pay_time = models.DateTimeField()
    order_status = models.IntegerField(default=0)
    extra_info = models.CharField(max_length=100)
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'mall_mall_order'


# 订单项表 Order_item
class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    # order_id = models.ForeignKey("MallOrder", on_delete=models.SET_NULL, null=True)
    # goods_id = models.ForeignKey("GoodsInfo", on_delete=models.SET_NULL, null=True)
    goods_name = models.CharField(max_length=100)
    goods_cover_img = models.CharField(max_length=100)
    goods_count = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mall_order_item'


# 订单地址表 Order_address
class OrderAddress(models.Model):
    # order_id = models.ForeignKey("MallOrder", on_delete=models.SET_NULL, null=True)
    user_name = models.CharField(max_length=32)
    user_phone = models.CharField(max_length=32)
    province_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    detail_address = models.CharField(max_length=100)

    class Mata:
        db_table = 'mall_order_address'


# 首页广告表 Mall_carousel
class MallCarousel(models.Model):
    carousel_id = models.AutoField(primary_key=True)
    carousel_url = models.CharField(max_length=100)
    redirect_url = models.CharField(max_length=100)
    carousel_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'mall_mall_carousel'


# 首页设置表 Index_config
class IndexConfig(models.Model):
    config_id = models.AutoField(primary_key=True)
    config_name = models.CharField(max_length=100)
    config_type = models.CharField(max_length=100)
    goods_id = models.IntegerField(default=0)
    redirect_url = models.CharField(max_length=100)
    config_rank = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'mall_index_config'


# 评论表 Mall_comment
class MallComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    # goods_id = models.ForeignKey("GoodsInfo", on_delete=models.SET_NULL, null=True
    # user_id = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    comment_text = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Mata:
        db_table = 'mall_mall_comment'

