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

class API_0202:
	'''
	修改客户name
	'''
	name = '修改客户 - API_0202'
		
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
		
		STEP(3, '列出客户信息')
		r = api.customer_list()
		retlist = r.json()['retlist']
		for ret in retlist:
			INFO(ret['name'])
			CHECK_POINT('检查响应信息体retlist列表', ret['name'] == '东莞大学')


class API_0203:
	'''
	修改客户的地址
	'''
	name = '修改客户 - API_0203'
	
	# 测试入口
	def teststeps(self):
		# 调用全局共享 数据
		cid = GSTORE['cid']
		
		STEP(1, '修改存在的客户ID')
		response_modify = api.customers_modify(f'{cid}',
		                                       '东莞大学',
		                                       '88888888',
		                                       '广东省-东莞市-松山湖大学路1号')
		
		STEP(2, '检查返回的ret结果')
		ret = response_modify.json()["ret"]
		INFO(ret)
		CHECK_POINT('检查ret返回的结果', ret == 0)
		
		STEP(3, '列出客户信息')
		r = api.customer_list()
		retlist = r.json()['retlist']
		for ret in retlist:
			INFO(ret['name'])
			CHECK_POINT('检查响应信息体retlist列表', ret['phonenumber'] == '88888888')


class API_0252:
	'''
	删除存在的客户
	'''
	name = '删除客户 - API_0251'
	
	# 测试入口
	def teststeps(self):
		# 调用全局共享 数据
		cid = GSTORE['cid']
		STEP(1, '删除存在的客户ID号')
		r_del = api.customers_del(cid)
		ret = r_del.json()['ret']
		INFO(ret)
		CHECK_POINT('检查返回的ret的值', ret == 0)
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量', response_list.json()['total'] == 0)