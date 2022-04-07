"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :dataEnvir_modify_customer_API.py
"""
from lib.web_api import api
from hytest import *

# 标签
force_tags = ['有一个客户的数据环境','dataEnvironment_oneCustomer_API测试']

class API_0252:
	'''
	删除存在的客户
	'''
	name = '删除客户 - API_0252'
	
	# 初始化方法
	def setup(self):
		r = api.customers_add({
				"name": "University of Technology",
				"phonenumber": "898989888",
				"address": "松山湖大学路1号"
			})
		
		self.cid = r.json()['id']
	
	# 测试入口
	def teststeps(self):
		
		STEP(1, '删除存在的客户ID号')
		r_del = api.customers_del(self.cid)
		ret = r_del.json()['ret']
		INFO(ret)
		CHECK_POINT('检查返回的ret的值', ret == 0)
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量', response_list.json()['total'] == 1)