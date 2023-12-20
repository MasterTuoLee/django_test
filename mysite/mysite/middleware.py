import random
import time
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime, timedelta

# # 原理
# now = datetime.now()
# time.sleep(5)
# # datetime.now()-now得到一个timedelta对象有seconds(多少秒)属性
# print((datetime.now()-now).seconds)


# class TestMiddleWare(MiddlewareMixin):
#     def __init__(self, get_response):
#         super().__init__(get_response)
#         # print("TestMiddleWare 初始化")
#
#     def process_request(self, request):
#         """
#         加工请求
#         :param request:
#         :return:
#         """
#         # print("TestMiddleWare 2222")
#         # print("path", request.path)
#         # print("sessionid", request.COOKIES.get("sessionid"))
#         # if not request.COOKIES.get("qiku"):
#         #     return HttpResponseRedirect("http://www.baidu.com")
#         pass
#
#     def process_response(self, request, response):
#         """
#         加工响应
#         :param request:
#         :param response:
#         :return:
#         """
#         # print("TestMiddleWare 3333")
#         # print("csrftoken", response.cookies.get("csrftoken"))
#         # response.cookies["abc"] = "88888"
#         # return HttpResponse("恭喜你被拉黑了")
#         return response
#
#
# class UserAgentMiddleWare(MiddlewareMixin):
#     def process_request(self, request):
#         if request.headers['User-Agent'] not in [
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#             "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36"
#         ]:
#             return HttpResponse("拒绝访问")
#
#


# #  模拟IP黑名单 最好放入数据库中
# forbidden_ip_list = [
#     '192.168.18.33',
#     '192.168.18.34',
#     # '192.168.185.157'
#
#     # '192.168.18.35',
#     # ...
# ]
# # 模拟时间（存放访问时间） 最好放入数据库中
# request_records = {
# }
#
#
# class UserIpForbidden(MiddlewareMixin):
#     def process_request(self, request):
#         # print(dir(request))
#         # print(request.META)
#         ip = request.META["REMOTE_ADDR"]
#         print(f"REMOTE_ADDR:{ip}")
#         now = datetime.now()
#
#         # 两次访问间隔不能超过十秒，否则就被拉黑
#         # if ip not in request_records:
#         #     request_records[ip] = [now]
#         # else:
#         #     if (now - request_records[ip][0]).seconds > 10:
#         #         request_records[ip].pop(0)
#         #         request_records[ip].append(now)
#         #     else:
#         #         forbidden_ip_list.append(ip)
#         #         request_records.pop(ip)
#         #     # request_records[ip].append(now)
#         # print("访问记录", request_records)
#         #
#         # if ip in forbidden_ip_list:
#         #     return HttpResponse("IP检测执行,IP已被拒绝访问")
#
#         # 十秒内连续访问五次就会被封
#         if ip not in request_records:
#             # 如果没有访问记录，直接添加
#             request_records[ip] = [now]
#         else:
#             # # 一般来说一分钟60次
#             # if len(request_records[ip]) < 60:
#             # 访问记录不够五次，直接添加
#             if len(request_records[ip]) < 5:
#                 request_records[ip].append(now)
#             else:
#                 # # 一般来说一分钟60次
#                 # if (now - request_records[ip][0]).minute > 10:
#                 if (now - request_records[ip][0]).seconds > 10:
#                     request_records[ip].pop(0)
#                     request_records[ip].append(now)
#                 else:
#                     forbidden_ip_list.append(ip)
#                     request_records.pop(ip)
#                 # request_records[ip].append(now)
#         print("访问记录", request_records)
#
#         if ip in forbidden_ip_list:
#             return HttpResponse("IP检测执行,IP已被拒绝访问")
