import requests
from pyquery import PyQuery
# 循环插入数据
for i in range(2, 10):
    # 先获取网址url路由
    url = "http://127.0.0.1:8000/user/regist/"

    response = requests.get(url)
    # print(response.text)

    doc = PyQuery(response.text)

    hidden_element = doc("[name='csrfmiddlewaretoken']")

    # print(response.cookies.get("csrftoken"))

    cookies = {
        "csrftoken": response.cookies.get("csrftoken"),
    }

    date = {
        "un": f"admin{i}",
        "pwd": "123456",
        "pwd1": "123456",
        "csrfmiddlewaretoken": hidden_element.attr("value"),
    }

    print(requests.post(url, cookies=cookies, data=date))
