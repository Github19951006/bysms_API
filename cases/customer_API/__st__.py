"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/15
@File   :__st__.py
"""
from hytest import *
from lib.web_api import api


# 初始化
def suite_setup():
	# 开代理
	# api.mgr_login(uerProxies=True)
	INFO('删除客户、药品、订单')
	api.mgr_login()