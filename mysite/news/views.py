from django.shortcuts import render,get_object_or_404
from .models import Category, News
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print("以下是new index")
    print("sessionid", request.COOKIES.get("sessionid"))
    print("qiku", request.COOKIES.get("qiku"))
    cs = Category.objects.all()
    return render(request, "index.html", {"cs": cs})


@login_required
def detail(request, id):
    n = get_object_or_404(News, id=id)
    return render(request, "detail.html", {"n": n})




