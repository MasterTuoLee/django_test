import requests
from pyquery import PyQuery

url_login = "http://127.0.0.1:8000/user/login/"

response_login_get = requests.get(url=url_login)
# print(response_login_get)
doc_response_login_get = PyQuery(response_login_get.text)
# print(doc_response_login_get)
print(response_login_get.cookies)

cookies = {
    "csrftoken": response_login_get.cookies.get("csrftoken")
}

data = {
    'email': 'admin@qq.com',
    'pwd': '123456',
    'csrfmiddlewaretoken':doc_response_login_get("[name='csrfmiddlewaretoken']").val()
}


# 设置allow_redirects为False，不允许重定向，不然无法获取新的登录过的cookies
response_login_post = requests.post(url=url_login,data=data, cookies=cookies,allow_redirects=False)

# print(response_login_post.cookies)

cookies_logined = {
    "csrftoken": response_login_post.cookies.get("csrftoken"),
    "sessionid":response_login_post.cookies.get("sessionid")
}

# # 在网站手动登录，每次重置cookie都需要重新登陆获取sessionid
# cookies_logined = {
#     "csrftoken": response_login_post.cookies.get("csrftoken"),
#     "sessionid":.......
# }

response_home = requests.get(url="http://127.0.0.1:8000/", cookies=cookies_logined)
# print(response_home.text)
doc_home = PyQuery(response_home.text)
# print(doc_home)
news_list = doc_home(".list-group-item a").items()
for news in news_list:
    print(news.text().strip(),f"http://127.0.0.1:8000{news.attr('href')}")