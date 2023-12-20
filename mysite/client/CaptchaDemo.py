# coding=utf-8
 # 构造入参为appId和appSecret
 # appId和前端验证码的appId保持一致，appId可公开
 # appSecret为秘钥，请勿公开
 # token在前端完成验证后可以获取到，随业务请求发送到后台，token有效期为两分钟
from .CaptchaClient import CaptchaClient

def check_token(token):
    appId = "ffdafefea55e62c87267794a266c2d24"
    appSecret = "31610208a346cf04fbe6eaa929876f10"

    captchaClient = CaptchaClient(appId, appSecret)
    captchaClient.setTimeOut(2)
    # 设置超时时间，默认2秒
    # captchaClient.setCaptchaUrl("http://cap.dingxiang-inc.com/api/tokenVerify")
    # 特殊情况可以额外指定服务器，默认情况下不需要设置
    response = captchaClient.checkToken(token)

    return response['result']