"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_response_content.py
"""
import requests

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 正常的URL地址   200
response = requests.get(
  "http://mirrors.sohu.com/",
  proxies = proxies,
)
response.encoding='utf8'
# text : 响应体消息
# print(response.text)

# 直接获取消息体中字节串bytest内容
print(response.content)

# 对字节串进行解码
print(response.content.decode('utf8'))