from django.shortcuts import render, HttpResponse, redirect
from alipay import AliPay, DCAliPay, ISVAliPay
from alipay.utils import AliPayConfig
import time
# 导入自带的路由守卫
from django.contrib.auth.decorators import login_required

# Create your views here.

def goodlist(request):
    return render(request, 'goodlist.html')

# 给支付添加路由守卫
@login_required()
def alipay(request, id):
    # 支付宝网页下载的证书不能直接被使用，需要加上头尾
    # 你可以在此处找到例子： tests/certs/ali/ali_private_key.pem
    # 找到cert下的两个对应文件
    app_private_key_string = open("cert/app_private_key.pem").read()
    alipay_public_key_string = open("cert/ali_public_key.pem").read()
    # 创建实例，里面大部分内容还是在沙箱环境中进行查找
    alipay = AliPay(
        # 换成自己沙箱环境中国的APPID
        appid="9021000129608132",
        # 现在测试get请求还用不到
        app_notify_url=None,  # 默认回调 url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        # 现在都是RSA2，所以要修改为RSA2，不修改会报错
        # sign_type="RSA",  # RSA 或者 RSA2
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认 False
        verbose=False,  # 输出调试数据
        config=AliPayConfig(timeout=15)  # 可选，请求超时时间
    )

    # 如果你是 Python3 的用户，使用默认的字符串即可
    subject = f"测试订单:{id}"

    # 电脑网站支付，需要跳转到：https://openapi.alipay.com/gateway.do? + order_string
    # 提供这个地址其实是上线之后的地址，修改为沙箱环境中的支付宝网关地址：https://openapi-sandbox.dl.alipaydev.com/gateway.do
    # 后面也一样，所以我们的拼接地址应该是https://openapi-sandbox.dl.alipaydev.com/gateway.do? + order_string
    # order_string返回的就是一个网址
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单
        # 订单号，使用time模块进行测试设置
        out_trade_no=f"{id}:{int(time.time())}",
        total_amount=0.01,
        subject=subject,
        # 支付的结果
        return_url="http://127.0.0.1:8000/pay/alipayback/",
        notify_url="https://example.com/notify"  # 可选，不填则使用默认 notify url
    )

    # 使用重定向
    return redirect(f"https://openapi-sandbox.dl.alipaydev.com/gateway.do?{order_string}")


def alipayback(request):
    # for django users return url是同步的get请求
    data = request.GET.dict()


    signature = data.pop("sign")
    app_private_key_string = open("cert/app_private_key.pem").read()
    alipay_public_key_string = open("cert/ali_public_key.pem").read()
    alipay = AliPay(
        # 换成自己沙箱环境中国的APPID
        appid="9021000129608132",
        # 现在测试get请求还用不到
        app_notify_url=None,  # 默认回调 url
        app_private_key_string=app_private_key_string,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=alipay_public_key_string,
        # 现在都是RSA2，所以要修改为RSA2，不修改会报错
        # sign_type="RSA",  # RSA 或者 RSA2
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认 False
        verbose=False,  # 输出调试数据
        config=AliPayConfig(timeout=15)  # 可选，请求超时时间
    )

    # verification
    # 又用到了alipay，从alipay函数中复制过来或包装成函数或类
    success = alipay.verify(data, signature)
    # if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
    #     print("trade succeed")
    print(success, data)
    if success:
        s = data['out_trade_no']
        good = s[:s.index(':')]
        # 购买成功后用户money增加
        request.user.money += int(good)
        request.user.save()
    # 重定向个人中心
    return redirect("/user/center/")

