import urllib.parse
import urllib.request
import random


def generate_code():
    code = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 6)
    code_str = ""
    for v in code:
        code_str += str(v)
    return code_str


def send(code_str, telephone):
    # 接口地址
    url = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
    # 定义请求的数据
    values = {
        'account': 'C17376176',
        'password': 'ee7a7824e96d06bb60907146578dedbc',
        'mobile': telephone,
        'content': f'您的验证码是：{code_str}。请不要把验证码泄露给其他人。',
        'format': 'json',
    }

    # 将数据进行编码
    data = urllib.parse.urlencode(values).encode(encoding='UTF8')

    # 发起请求
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    res = response.read()

    # 打印结果
    return res.decode("utf8")
