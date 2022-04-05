"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/05
@File   :__st__.py
"""
from lib.web_api import api
from hytest import *

# 初始化方法
def suite_setup():
	INFO('添加一个客户信息')
	response_add = api.customers_add('东莞理工学院',
	                                 '13553896530',
	                                 '广东省-东莞市-松山湖大学路壹号')
	# 将添加客户后返回的id保存
	cid = response_add.json()['id']
	
	# 存储 全局共享 数据
	GSTORE['cid'] = cid
	
# 清除
def suite_teardown():
	INFO('删除初始添加的客户信息')
	# 调用全局共享 数据
	cid = GSTORE['cid']
	api.customers_del(cid)