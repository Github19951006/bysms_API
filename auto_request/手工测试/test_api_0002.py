"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :test_api_0002.py
"""
import requests
from lib.printResponse import *
payload = {
	'username': 'byhy',
	'password': '8888888'
}
# 创建一个session对象
session = requests.Session()
# 发起请求
response = session.post('http://127.0.0.1/api/mgr/signin',
             data=payload,
             )

responseData(response)