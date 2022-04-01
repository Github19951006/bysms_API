"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_response_headers.py
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

# headers : 响应头消息
print(response.headers)

# 继承自 Dict 字典 类型的一个 类。
print(type(response.headers))
# 强制转成 dict类型
print(type(dict(response.headers)))

# 类似字典一样的键值对 获取信息
# 通过键  -- 获取value值
print(response.headers['Server'])