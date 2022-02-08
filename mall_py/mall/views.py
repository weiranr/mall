from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action


class MallUserViewSet(viewsets.ModelViewSet):
    queryset = MallUser.objects.all()
    serializer_class = MallUserSerializer


class GoodsInfoViewSet(viewsets.ModelViewSet):
    queryset = GoodsInfo.objects.all()
    serializer_class = GoodsInfoSerializer

    # detail=False包含id是True， 不包含id是False
    @action(methods=['GET'], detail=False, url_path="search")
    def findSearch(self, request):
        name = request.GET['name']
        queryset = GoodsInfo.objects.values().filter(goods_name__contains=name)
        # print(JsonResponse(list(queryset), safe=False))
        if (queryset != ''):
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发送错误'})

    # detail=False包含id是True， 不包含id是False
    @action(methods=['GET'], detail=False, url_path="findgoods")
    def findGoodsById(self, request):
        id = request.GET['id']
        queryset = GoodsInfo.objects.values().filter(goods_id=id)
        # print(JsonResponse(list(queryset), safe=False))
        if (queryset != ''):
            return JsonResponse({'status': 200, 'data': list(queryset)}, safe=False)
        else:
            return JsonResponse({'status': 500, 'message': '服务器发送错误'})


class GoodsCategoryViewSet(viewsets.ModelViewSet):
    queryset = GoodsCategory.objects.all().filter(is_deleted=0)
    serializer_class = GoodsCategorySerializer


class MallCarouselViewSet(viewsets.ModelViewSet):
    queryset = MallCarousel.objects.all()
    serializer_class = MallCarouselSerializer


class IndexConfigViewSet(viewsets.ModelViewSet):
    queryset = IndexConfig.objects.all().filter(is_deleted=0)
    serializer_class = IndexConfigSerializer

