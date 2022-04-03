"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :printResponse.py
"""
import requests,json
import pprint

def responseData(response):
	print('------------响应状态码---------------')
	print(response.status_code)
	
	print('------------响应消息头---------------')
	for k, v in response.headers.items():
		print(f'{k}: {v}')
	
	print('------------响应消息体---------------')
	obj = json.loads(response.content.decode('utf8'))
	pprint.pprint(obj)