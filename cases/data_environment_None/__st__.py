"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/04
@File   :__st__.py
"""
from lib.web_api import api

# 初始化
def suite_setup():
	# 开代理
	# api.mgr_login(uerProxies=True)
	api.mgr_login()
	api.orders_del_all()
	api.customers_del_all()
	api.medicines_del_all()