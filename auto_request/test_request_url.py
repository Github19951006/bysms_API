"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_request_url.py
"""
import requests

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# URL参数
urlpara = {
  'wd' : 'iphone',
  'rsv_spt' : '1'
}

response = requests.get(
  'http://www.baidu.com/s',
  params = urlpara,proxies = proxies
)

print(response.text)