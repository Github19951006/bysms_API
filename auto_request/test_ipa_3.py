"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_ipa_3.py
"""
import requests

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 请求的消息头
headers = {
  'user-agent' : 'my-app/0.0.1',
  'auth-type' : 'jwt-token'
}


response = requests.post(
  "http://httpbin.org/post",
  proxies = proxies,
  headers = headers
)

print(response.text)