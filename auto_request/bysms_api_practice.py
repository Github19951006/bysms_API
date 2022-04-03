"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :bysms_api_practice.py
"""
import requests, json
from lib.printResponse import *

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

payload = {
	'username': 'byhy',
	'password': '88888888'
}
# 创建一下session 对象
session = requests.Session()

# 通过session对象 发起请求
response = session.post('http://127.0.0.1/api/mgr/signin',
                        data=payload,
                        proxies = proxies
                        )
responseData(response)
