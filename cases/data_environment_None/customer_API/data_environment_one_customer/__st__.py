"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :__st__.py
"""
from lib.web_api import api
from hytest import *
def suite_setup():
	
	response_add = api.customers_add('东莞理工学院',
	                                 '13553896530',
	                                 '广东省-东莞市-松山湖大学路壹号')
	# 将添加客户后返回的id保存
	cid = response_add.json()['id']
	
	# 存储 全局共享 数据
	GSTORE['cid'] = cid