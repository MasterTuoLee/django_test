import os
import requests
from pyquery import PyQuery

# 爬取网址为：http://www.cssmoban.com/ppt

# 根网址
base_url = "http://www.cssmoban.com/ppt/"

# 设置异常捕获
try:
    for index in range(1, 10):
        response = requests.get(url=f"{base_url}{index}.html")
        if response.status_code == 200:
            doc_response = PyQuery(response.text)

            # 使用属性选择器先选择到info-list属性
            img_lists = doc_response(".info-list")

            # 创建文件夹，指定下载路径
            save_folder = f'ppt/ppt_{index}'
            os.makedirs(save_folder, exist_ok=True)

            # 遍历获取每一个图像地址
            for e in img_lists:
                # 获取图像下载地址，获取img属性
                img_url = PyQuery(e)("img").attr("src")
                # 指定下载名
                img_name = img_url.split('/')[-1]
                # 拼接下载路径
                img_path = os.path.join(save_folder, img_name)

                # 开始请求下载
                ppt_response = requests.get(url=img_url)
                # 查看状态码
                if ppt_response.status_code == 200:
                    # 以二进制形式写入文件
                    with open(img_path, 'wb') as img_file:
                        img_file.write(ppt_response.content)
                        print(f"下载ppt{index}中的{img_name}完成")
                else:
                    print("下载失败")
            print(f"下载ppt{index}完成")
        else:
            print("请求失败")
except Exception as e:
    print("出异常了！！！异常类型为：e")
