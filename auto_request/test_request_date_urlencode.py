"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_request_date_urlencode.py
"""
import requests

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# xml格式的消息体
payload = {
  'key1': 'value1',
  'key2': 'value2'
}


response = requests.post(
  "http://httpbin.org/post",
  proxies = proxies,
  data= payload
)

print(response.text)