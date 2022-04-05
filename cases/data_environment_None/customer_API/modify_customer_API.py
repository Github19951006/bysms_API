"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :modify_customer_API.py
"""
from lib.web_api import api
from hytest import *

class API_0201:
	'''
	修改不存在的客户ID号
	'''
	name = '修改客户 - API_0201'
	
	# 测试入口
	def teststeps(self):
		STEP(1,'修改不存在的客户ID')
		response_modify = api.customers_modify('78',
		                                       '东莞理工学院',
		                                       '13553896530',
		                                       '广东省-东莞市-松山湖大学路壹号')
		
		STEP(2,'检查返回的msg信息体')
		msg = response_modify.json()["msg"]
		INFO(msg)
		CHECK_POINT('检查msg信息',msg == 'id 为`78`的客户不存在' )
		
		STEP(3, '列出客户信息')
		r = api.customer_list()
		CHECK_POINT('检查响应信息体retlist列表',r.json()['retlist'] == [])
		
		
		
	
