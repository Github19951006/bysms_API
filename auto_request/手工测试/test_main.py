"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :test_main.py
"""
from lib.web_api import *
def main():
	# 用例 API-0151
	# 1登录
	api.mgr_login()
	# 2添加客户信息
	api.customers_add('东莞大学','13345679934','广东省-东莞市-松山湖大学路1号')

	
	
	# 用例 API-0152
	# 2添加客户信息
	api.customers_add('东莞理工学院', '1334456433', '广东省-松山湖大学路1号')
	# 3列出客户信息
	api.customer_list(pagesize=11)
	
	# 用例 API-0153
	# 2添加客户信息,客户名字段缺失
	api.customers_add(phonenumber='1334567994',address='松山湖大学路1号')

	
	# API-0201
	# ID 为一个不存在的客户ID号
	api.customers_modify(56,'东莞理工学院', '1334456433', '广东省-松山湖大学路1号')
	
	
	# API-0202
	# 修改信息中只修改客户名称
	api.customers_modify(763, '东莞理工学院34', '1334456433', '广东省-松山湖大学路1号')
	
	
	# API-0203
	# 修改信息中只修改客户名称
	api.customers_modify(763, '东莞理工学院34', '8888888888888', '广东省-松山湖大学路1号')
	
	
	
	# API - 0251
	api.customers_del(76)
	
 	# API - 0252
	api.customers_del(763)

if __name__ == '__main__':
    main()