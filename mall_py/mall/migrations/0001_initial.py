# Generated by Django 4.0.2 on 2022-02-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_level', models.CharField(max_length=32)),
                ('parent_id', models.CharField(max_length=32)),
                ('category_rank', models.IntegerField()),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'mall_goods_category',
            },
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=100)),
                ('goods_intro', models.CharField(max_length=100)),
                ('goods_cover_img', models.CharField(max_length=100)),
                ('goods_carousel', models.CharField(max_length=100)),
                ('goods_detail_content', models.CharField(max_length=100)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=64)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=64)),
                ('stock_num', models.IntegerField(default=0)),
                ('tag', models.CharField(max_length=100)),
                ('goods_sell_status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'mall_goods_info',
            },
        ),
        migrations.CreateModel(
            name='IndexConfig',
            fields=[
                ('config_id', models.AutoField(primary_key=True, serialize=False)),
                ('config_name', models.CharField(max_length=100)),
                ('config_type', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(max_length=100)),
                ('config_rank', models.IntegerField()),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MallCarousel',
            fields=[
                ('carousel_id', models.AutoField(primary_key=True, serialize=False)),
                ('carousel_url', models.CharField(max_length=100)),
                ('redirect_url', models.CharField(max_length=100)),
                ('carousel_rank', models.IntegerField()),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MallComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MallOrder',
            fields=[
                ('order_code', models.IntegerField(auto_created=True)),
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=64)),
                ('pay_status', models.IntegerField(default=0)),
                ('pay_type', models.CharField(max_length=100)),
                ('pay_time', models.DateTimeField()),
                ('order_status', models.IntegerField(default=0)),
                ('extra_info', models.CharField(max_length=100)),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mall_mall_order',
            },
        ),
        migrations.CreateModel(
            name='MallUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_name', models.CharField(max_length=32)),
                ('user_pwd', models.CharField(max_length=32)),
                ('nick_name', models.CharField(max_length=32)),
                ('locked', models.IntegerField(default=0)),
                ('introduce', models.CharField(max_length=100)),
                ('is_delete', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_user',
            },
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_phone', models.CharField(max_length=32)),
                ('province_name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
                ('region_name', models.CharField(max_length=100)),
                ('detail_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=100)),
                ('goods_cover_img', models.CharField(max_length=100)),
                ('goods_count', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mall_order_item',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('cart_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_count', models.IntegerField()),
                ('is_deleted', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mall_shopping_cart',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
                ('user_phone', models.CharField(max_length=32)),
                ('default_flag', models.IntegerField(default=0)),
                ('province_name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
                ('region_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('token', models.AutoField(primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('expire_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'user_token',
            },
        ),
    ]
