"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_response_headers.py
"""
import requests,json

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 正常的URL地址   200
response = requests.post(
  "http://httpbin.org/post",
  data={1:1,2:2},
  proxies = proxies
)

# obj = json.loads(response.content.decode('utf8'))

# 优化   获取响应消息体消息
obj = response.json()
print(obj)