"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/04
@File   :add_customer_API.py
"""
from lib.web_api import api
from hytest import *
class API_0151:
	name = '添加客户 - API_0151'
	
	def setup(self):
		api.mgr_login()
		api.orders_del_all()
		api.customers_del_all()
		api.medicines_del_all()
	
	def teardown(self):
		api.customers_del(cid = self.add_customerID)
		
	def teststeps(self):
		STEP(1,'添加客户信息')
		response_add = api.customers_add(name = '东莞理工学院',
		                  phonenumber = '13553896530',
		                  address= '广东省-东莞市-松山湖大学路壹号'
		                  )
		
		ret_add_customer_json = response_add.json()
		CHECK_POINT('检查返回的ret结果',
		            ret_add_customer_json['ret'] == 0
		            )
		self.add_customerID = ret_add_customer_json['id']
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量',response_list.json()['total'] == 1)
		