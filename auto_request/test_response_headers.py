"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_response_status_code.py
"""
import requests,json

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 正常的URL地址   200
# response = requests.get(
#   "http://httpbin.org/post",
#   proxies = proxies,
# )

# 不存在的URL地址  返回的结果是：404
response = requests.get(
  "http://httpbin.org/aaaaaaa",
  proxies = proxies,
)

# status_code : 响应状态码
print(response.status_code)