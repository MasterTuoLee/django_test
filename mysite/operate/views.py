from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from news.models import News
from .models import Collect, Comment



# Create your views here.

def collect(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            nid = request.POST.get("nid")
            news = get_object_or_404(News, id=nid)
            collect = Collect.objects.filter(news=news, user=request.user).first()
            if collect:
                collect.delete()
                return JsonResponse({
                    "code": 0,
                    "msg": "取消收藏成功",
                    "state": 0
                })
            else:
                Collect.objects.create(user=request.user, news=news)
                return JsonResponse({
                    "code": 0,
                    "msg": "收藏成功",
                    "state": 1
                })


        else:
            return JsonResponse({
                "code": -1,
                "msg": "用户尚未登录"
            })






    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })


def comment(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            nid = request.POST.get("nid")
            news = get_object_or_404(News, id=nid)
            content = request.POST.get("content")
            c = Comment.objects.create(user=request.user, news=news, content=content)
            return JsonResponse({
                "code": 0,
                "msg": "评论成功",
                "data": {
                    "id": c.id,
                    "time": c.time.strftime("%Y年%m月%d日 %H:%M"),
                    "head": request.user.head.url,
                    "username": request.user.username
                }
            })


        else:
            return JsonResponse({
                "code": -1,
                "msg": "用户尚未登录"
            })
    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })
