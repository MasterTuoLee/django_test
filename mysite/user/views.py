from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import CustomUser, TelephoneCode
from django.contrib.auth import login as lgi, logout as lgo
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from django.conf import settings
import time
from .sendmsg import generate_code, send
from client.CaptchaDemo import check_token

@login_required
def center(request):
    return render(request, "center.html")


def modify_telephone(request):
    if request.method == "POST":
        code = request.POST.get("code")
        telephone = request.POST.get("telephone")
        print(f"手机号{telephone} 验证码{code}")
        tc = TelephoneCode.objects.filter(telephone=telephone, code=code).first()

        if tc:
            tc.delete()
            request.user.telephone =telephone
            request.user.save()
            return JsonResponse({
                "code": 0,
                "msg": "绑定成功"
            })
        else:
            return JsonResponse({
                "code": -2,
                "msg": "验证码错误"
            })
    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })


def change_telephone(request):
    if request.method == "POST":
        token = request.POST.get("token")
        if check_token(token):
            telephone = request.POST.get("telephone")
            code_type = request.POST.get("code_type", "change_telephone_code")

            code_str = generate_code()
            TelephoneCode.objects.create(telephone=telephone, code=code_str, code_type=code_type)
            print(f"向手机号{telephone} 发送验证码{code_str}")
            data = send(code_str, telephone)

            return JsonResponse({
                "code": 0,
                "msg": "发送成功",
                "data": data
            })
        else:
            return JsonResponse({
                "code": -1,
                "msg": "未知错误"
            })
    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })


def change_username(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if username == request.user.username:
            return JsonResponse({
                "code": -1,
                "msg": "用户名和原来一样"
            })
        else:
            first = CustomUser.objects.filter(username=username).first()
            if first:
                return JsonResponse({
                    "code": -3,
                    "msg": "用户名已存在"
                })
            else:
                request.user.username = username
                request.user.save()
                return JsonResponse({
                    "code": 0,
                    "msg": "修改成功"
                })
    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })


def active(request, id):
    serializer2 = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
    try:
        obj = serializer2.loads(id)
        user = get_object_or_404(CustomUser, id=obj["id"])
        user.is_active = True
        user.save()
        return redirect(reverse("user:login"))
    except SignatureExpired as e:
        return HttpResponse("请在5分钟内激活")
    except BadSignature as e:
        return HttpResponse("指纹不匹配")
    except Exception as e:
        return HttpResponse("未知错误")


def change_head(request):
    if request.method == "POST":
        user = request.user
        user.head = request.FILES.get("file")
        user.save()
        return JsonResponse({
            "code": 0,
            "msg": "更换头像成功",
            "data": {
                "head": user.head.url
            }
        })
    else:
        return JsonResponse({
            "code": -1,
            "msg": "只允许post请求"
        })


def login(request):
    next = request.GET.get("next")
    if request.method == "GET":
        if next:
            return render(request, "login.html", {"next": next})
        return render(request, "login.html")
    elif request.method == "POST":
        login_type = request.POST.get("login_type", "email_login")
        if login_type == "email_login":
            email = request.POST.get("email")
            user = CustomUser.objects.filter(email=email).first()
            if user:
                password = request.POST.get("password")
                if user.check_password(password):
                    if user.is_active:
                        lgi(request, user)
                        if next:
                            return redirect(next)
                        return redirect(reverse("news:index"))
                    else:
                        error = "用户尚未激活"
                else:
                    error = "密码错误"
            else:
                error = "邮箱不存在"
            return render(request, "login.html", {"error": error})
        elif login_type == "telephone_login":
            telephone = request.POST.get("telephone")
            user = CustomUser.objects.filter(telephone=telephone).first()
            if user:
                login_code = request.POST.get("login_code")

                tc = TelephoneCode.objects.filter(telephone=telephone, code=login_code,
                                                  code_type="login_code").first()
                print(tc, telephone, login_code, )
                if tc:
                    lgi(request, user)
                    # tc.delete()
                    return JsonResponse({
                        "code": 0,
                        "msg": "登录成功"
                    })
                else:
                    return JsonResponse({
                        "code": -2,
                        "msg": "验证码错误"
                    })
            else:
                return JsonResponse({
                    "code": -1,
                    "msg": "手机号不存在"
                })


def regist(request):
    if request.method == "GET":
        return render(request, "regist.html")
    elif request.method == "POST":
        email = request.POST.get("email")
        user = CustomUser.objects.filter(email=email).first()
        if not user:
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            if password2 != password:
                error = "密码不一致"
            else:
                # 用户名默认和邮箱保持一致  默认没有激活
                user = CustomUser.objects.create_user(email=email, username=email, password=password, is_active=False)
                serializer = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY, expires_in=60 * 5)
                s0 = serializer.dumps({"id": user.id})
                s0 = s0.decode()
                # 向email 发送邮件让用户激活
                mail = EmailMultiAlternatives("新闻网-激活邮件", "点击激活", from_email="15138001200@163.com",
                                              to=["496575233@qq.com"])
                mail.attach_alternative(f"<a href='http://127.0.0.1:8000/user/active/{s0}'>点击激活新闻网账户</a>",
                                        "text/html")
                mail.send()

            return redirect(reverse("user:login"))

        else:
            error = "邮箱已经存在"
        return render(request, "regist.html", {"error": error})


def logout(request):
    lgo(request)
    return redirect(reverse("user:login"))
