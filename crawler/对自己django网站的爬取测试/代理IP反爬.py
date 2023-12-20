import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# 在使用IP检测被风控IP后，可以使用代理IP进行访问,用于测试的代理IP，质量不是太好，但是多次测试也成功过，每个IP代理网站都大同小异
# 网站获取api接口：http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=125022&vkey=EB27682B2E5FDC0C374CA46BDFAA9FEC&num=1&time=30&plat=0&re=0&type=1&so=1&ow=1&spl=1&addr=&db=1
# 解析
ip_response = requests.get(
    url="http://api.xiequ.cn/VAD/GetIp.aspx?act=get&uid=125022&vkey=EB27682B2E5FDC0C374CA46BDFAA9FEC&num=1&time=30&plat=0&re=0&type=1&so=1&ow=1&spl=1&addr=&db=1")
print(ip_response.json())
# print(ip_response.json()["data"][0]["IP"],ip_response.json()["data"][0]["Port"])

# 代理服务器
# 使用socks5模式请打开注释
# proxyType = "socks5"
proxyType = "http"

# 用户名密码验
proxyU = "qiku123"
proxyP = "dsb666..."

# 携趣代理IP地址和端口
proxyHost = ip_response.json()["data"][0]["IP"]
proxyPort = ip_response.json()["data"][0]["Port"]

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyU,
    "pass": proxyP,
}
myproxies = {
    "http": proxyMeta,
    "https": proxyMeta
}
print(myproxies)
response = requests.get(url="http://192.168.185.157:6789/user/login/", headers=headers, proxies=myproxies)
print(response.text)
