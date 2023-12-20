from django.urls import path, include
from .views import *
app_name = "demo1"
urlpatterns = [
    # 普通式分页
    path('demo1/', demo1),
    # 异步刷新分页
    path('demo2/', demo2),
    path('loaddata/', loaddata),
]
