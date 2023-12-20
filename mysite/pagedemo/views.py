from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, Page
from django.http import JsonResponse


# Create your views here.
# venv/django/core/paginator:
# Paginator分页器
# object_list：：需要分页的列表，per_page:每页有多少个
# 函数:validate_number：校验页码是否合法；get_page:获取某一页；count:需要分页的列表中元素的个数；num_pages:返回总的页码；page_range:返回页码列表；
# get_elided_page_range:带有省略号的页码列表

# Page分页
# object_list：当前页的数据列表；number:当前页页码；paginator：当前页所属分页分页器
# has_next:是否有下一页；has_previous:是否有上一页；has_other_pages:有没有其他页码；next_page_number:下一页页码；previous_page_number：上一页页码
# start_index:当前页元素索引开始；end_index:当前页元素结束索引

def demo1(request):
    # datas = NewsItem.objects.all()
    # 按viewcount排序后再逆序
    datas = NewsItem.objects.order_by("viewcount").reverse()
    # 构造分页器
    paginator = Paginator(datas, 10)
    # 提取页码信息，第二个参数默认就是第一页
    page_num = request.GET.get("page_num", 1)
    # print("page_num", page_num)
    # 获取当前分页信息
    page = paginator.get_page(page_num)
    # print(paginator.page_range)
    # 高级写法，返回生成器，在模板中设计分页可以省略
    # print(paginator.get_elided_page_range())
    # 只需要传入page，datas都不用传入
    # 返回所有的页码也传入模板
    elided_page_nums = paginator.get_elided_page_range(page_num, on_ends=2, on_each_side=2)
    return render(request, "demo1.html", locals())


def demo2(request):
    return render(request, 'demo2.html', locals())


def loaddata(request):
    page_num = request.GET.get("page_num", 1)
    datas = NewsItem.objects.all()
    # 构造分页器
    paginator = Paginator(datas, 10)
    # 获取当前前分页
    page = paginator.get_page(page_num)
    result = {
        "code": 0,
        "msg": "success",
        "data": {
            "has_next": page.has_next(),
            "datas": [{"id": data.id, "title": data.title, "time": data.time.strftime("%Y年%m月%d日 %H:%M"), "viewcount": data.viewcount} for data in
                      page.object_list],
        }
    }
    return JsonResponse(result)



