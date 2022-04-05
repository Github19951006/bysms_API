"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/04
@File   :add_customer_API.py
"""
from lib.web_api import api
from hytest import *

# 标签
force_tags = ['添加客户']

class API_0151:
	name = '添加客户 - API_0151'
	
	# 清除方法
	def teardown(self):
		api.customers_del(cid = self.add_customerID)
	
	# 测试入口
	def teststeps(self):
		STEP(1,'添加客户信息')
		response_add = api.customers_add('东莞理工学院',
		                                '13553896530',
		                                '广东省-东莞市-松山湖大学路壹号'
		                                 )
		
		ret_add_customer_json = response_add.json()
		CHECK_POINT('检查返回的ret结果',
		            ret_add_customer_json['ret'] == 0
		            )
		# 保存添加客户的ID
		self.add_customerID = ret_add_customer_json['id']
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量',response_list.json()['total'] == 1)


class API_0152:
	name = '添加客户 - API_0152'
	
	# 初始化方法
	def setup(self):
		
		INFO('添加10个客户')
		for i in range(10):
			api.customers_add(f'东莞理工学院{i+1}',
			                  f'0755-819583{i+2}',
			                  f'东莞市松山湖大学路{i+1}'
			                  )
	# 清除方法
	def teardown(self):
		
		add_customer_list = [] # 存储添加客户的id
		# 列出所有客户，返回response
		response_customer_list = api.customer_list(pagesize=11)
		# 获取添加的客户ID,存到add_customer_list列表
		retList = response_customer_list.json()["retlist"]
		for customer in retList:
			add_customer_list.append(customer['id'])
		for cid in add_customer_list:
			api.customers_del(cid=cid)
		INFO(add_customer_list)
	
	# 测试入口
	def teststeps(self):
		
		STEP(1, '添加客户信息')
		response_add = api.customers_add('东莞职业技术学院',
		                                 '88886666',
		                                 '广东省-东莞市-松山湖大学路壹号'
		                                 )
		
		ret_add_customer_json = response_add.json()
		CHECK_POINT('检查返回的ret结果',
		            ret_add_customer_json['ret'] == 0
		            )
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list(pagesize=11)
		INFO(response_list.json())
		CHECK_POINT('检查客户的数量', response_list.json()['total'] == 11)


class API_0153:
	name = '添加客户 - API_0153'
	
	# 测试入口
	def teststeps(self):
		STEP(1, '添加客户信息')
		response_add = api.customers_add(None,
		                                 '13553896530',
		                                 '广东省-东莞市-松山湖大学路壹号'
		                                 )
		
		ret_add_customer_json = response_add.json()
		INFO(ret_add_customer_json)
		CHECK_POINT('检查返回的ret结果',
		            ret_add_customer_json['ret'] == 1
		            )
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量', response_list.json()['total'] == 0)
		
