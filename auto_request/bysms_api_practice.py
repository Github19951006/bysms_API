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

# 登录
# 通过session对象 发起请求
response = session.post('http://127.0.0.1/api/mgr/signin',
                        data=payload,
                        proxies = proxies
                        )
responseData(response)

# URL参数
urlpara = {
	'action' : 'list_customer',
	'pagesize' : '4',
	'pagenum' : '1',
	'keywords' : ''
}

# 列出所有客户
response = session.get('http://127.0.0.1/api/mgr/customers',
                        params = urlpara,
                        proxies = proxies
                        )
responseData(response)

payload = {
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}

# 添加一个客户
response = session.post('http://127.0.0.1/api/mgr/customers',
                        json = payload,
                        proxies = proxies
                        )
responseData(response)