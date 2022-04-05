"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :del_customer_API.py
"""
from lib.web_api import api
from hytest import *

# 标签
force_tags = ['删除客户']


class API_0251:
	name = '删除客户 - API_0251'
	
	# 测试入口
	def teststeps(self):
		STEP(1, '删除不存在的客户ID号')
		r_del = api.customers_del(56)
		msg = r_del.json()['msg']
		INFO(msg)
		CHECK_POINT('检查返回的msg信息', msg == 'id 为`56`的客户不存在')
		
		STEP(2, '检查系统数据')
		response_list = api.customer_list()
		CHECK_POINT('检查客户的数量', response_list.json()['total'] == 0)