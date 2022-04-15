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

class API_0154:
	name = '添加客户（客户名字段重复2次） - API_0154'
	
	# 清除方法
	# def teardown(self):
	# 	api.customers_del(cid = self.add_customerID)
	#
	# 测试入口
	def teststeps(self):
		STEP(1,'添加客户信息')
		response_add = api.customers_add({
				"name": "东莞理工学院",
				"name": "东莞理工学院",
				"phonenumber": "13553896530",
				"address": "广东省-东莞市-松山湖大学路壹号"
			})
		
		ret_add_customer_json = response_add.json()
		INFO(ret_add_customer_json)
		CHECK_POINT('检查返回的ret结果',
		            ret_add_customer_json['ret'] == 0
		            )
		
		# # 保存添加客户的ID
		# self.add_customerID = ret_add_customer_json['id']
		#
		# STEP(2, '检查系统数据')
		# response_list = api.customer_list()
		# CHECK_POINT('检查客户的数量',response_list.json()['total'] == 1)

