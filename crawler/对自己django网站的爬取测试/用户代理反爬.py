import random

import requests
from pyquery import PyQuery

url = "http://127.0.0.1:8000/user/login/"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
]
headers = {
    "User-Agent":random.choices(user_agents)[0]
}
requests = requests.get(url=url, headers=headers)
print(requests.text)
