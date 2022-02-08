from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MallUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MallUser
        fields = '__all__'


class GoodsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsInfo
        fields = '__all__'


class GoodsCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GoodsCategory
        # fields = '__all__'
        fields = ['url', 'category_id', 'category_name', 'category_level', 'parent_id', 'category_rank', 'is_deleted']


class MallCarouselSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MallCarousel
        fields = '__all__'


class IndexConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndexConfig
        fields = ['goods_id', 'config_name', ]