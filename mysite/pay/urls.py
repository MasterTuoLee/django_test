from django.urls import path
from .views import *
app_name = "pay"
urlpatterns = [
    # 商品列表
    path('goodlist/', goodlist, name="goodlist"),
    path('alipay/<int:id>', alipay, name="alipay"),
    path('alipayback/', alipayback, name="alipayback"),

]
