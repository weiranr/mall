from django.contrib import admin
from django.urls import path, include
from mall import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'malluser', views.MallUserViewSet)
router.register(r'goodsinfo', views.GoodsInfoViewSet)
router.register(r'goodscategory', views.GoodsCategoryViewSet)
router.register(r'mallcarousel', views.MallCarouselViewSet)
router.register(r'indexconfig', views.IndexConfigViewSet)

urlpatterns = [
    path('search/', views.GoodsInfoViewSet.as_view({'get': 'findSearch'})),
    path('findgoods/', views.GoodsInfoViewSet.as_view({'get': 'findGoodsById'}))
]

urlpatterns += router.urls
