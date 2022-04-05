"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :dataEnvir_modify_customer_API.py
"""
from lib.web_api import api
from hytest import *

class API_0202:
	'''
	修改已经存在一个客户的环境
	'''
	name = '修改客户 - API_0202'
	
	# 初始化清除
	def teardown(self):
		# 调用全局共享 数据
		cid = GSTORE['cid']
		api.customers_del(cid)
		
	# 测试入口
	def teststeps(self):
		# 调用全局共享 数据
		cid = GSTORE['cid']
		
		STEP(1, '修改存在的客户ID')
		response_modify = api.customers_modify(f'{cid}',
		                                       '东莞大学',
		                                       '13553896530',
		                                       '广东省-东莞市-松山湖大学路1号')
		
		STEP(2, '检查返回的ret结果')
		ret = response_modify.json()["ret"]
		INFO(ret)
		CHECK_POINT('检查ret返回的结果', ret == 0)