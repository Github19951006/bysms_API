"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :web_api.py
"""
from lib.printResponse import *
class APIMgr:
	
	# 登录
	def mgr_login(self,uername = 'byhy',password = '88888888'):
		
		payload = {
			'username': uername,
			'password': password
		}
		# 创建session 对象
		self.session = requests.Session()

		# 通过session对象 发起请求
		response = self.session.post('http://127.0.0.1/api/mgr/signin',
		                        data=payload
		                        )
		responseData(response)
		return response
	
	# 列出所有客户
	def customer_list(self,pagesize = 10,pagenumber = 1,keywords = ''):
		# URL参数
		urlpara = {
			'action': 'list_customer',
			'pagesize': pagesize,
			'pagenum': pagenumber,
			'keywords': keywords
		}
		response = self.session.get("http://127.0.0.1/api/mgr/customers",
		                 params = urlpara
		                 )
		responseData(response)
		return response
	
	# 添加一个客户
	def customers_add(self,name,phonenumber,address):
		payload = {
			"action": "add_customer",
			"data": {
				"name": name,
				"phonenumber": phonenumber,
				"address": address
			}
		}
		response = self.session.post('http://127.0.0.1/api/mgr/customers',
		                        json=payload
		                        )
		responseData(response)
		return response
	
	# 修改客户信息
	def customers_modify(self,id,name,phonenumber,address):
		
		payload = {
			"action": "modify_customer",
			"id": id,
			"newdata": {
				"name": name,
				"phonenumber": phonenumber,
				"address": address
			}
		}
		response = self.session.put('http://127.0.0.1/api/mgr/customers',
		                       json=payload
		                       )
		responseData(response)
		return response
	
	
	def customers_del(self,id):
		# 删除客户信息
		payload = {
			"action": "del_customer",
			"id": id
		}
		
		response = self.session.delete('http://127.0.0.1/api/mgr/customers',
		                          json=payload
		                          )
		responseData(response)
		return response
	
	'''--------------------------------药品---------------------------'''
	
	def medicines_list(self,pagesize = 10,pagenum = 1,keywords = ''):
		# 列出所有客户
		# URL参数
		urlpara = {
			'action': 'list_medicine',
			'pagesize': pagesize,
			'pagenum' : pagenum,
			'keywords': keywords
		}
		response = self.session.get('http://127.0.0.1/api/mgr/medicines',
		                       params=urlpara
		                       )
		responseData(response)
		return response
	
	# 添加一个药品
	def medicines_add(self,name,descm,sn):
		
		payload = {
			"action": "add_medicine",
			"data": {
				"name" : name,
				"desc" : descm,
				"sn"   : sn
			}
		}
		response = self.session.post('http://127.0.0.1/api/mgr/medicines',
		                        json=payload
		                        )
		responseData(response)
		return response
	
	
	def medicines_modify(self,id,name,desc,sn):
		# 修改药品信息
		payload = {
			"action": "modify_medicine",
			"id": id,
			"newdata": {
				"name" : name,
				"desc" : descm,
				"sn"   : sn
			}
		}
		response = self.session.put('http://127.0.0.1/api/mgr/medicines',
		                       json=payload
		                       )
		responseData(response)
		return response
	
	
	def medicines_del(self,id):
		# 删除药品信息
		payload = {
			"action": "del_medicine",
			"id": id
		}
		
		response = self.session.delete('http://127.0.0.1/api/mgr/medicines',
		                          json=payload
		                          )
		responseData(response)
		return response
	
	
	'''--------------------------------订单---------------------------'''
	
	def orders_list(self,pagesize = 10,pagenum = 1,keywords = ''):
		# 列出所有客户
		# URL参数
		urlpara = {
			'action'   : 'list_order',
			'pagesize' : pagesize,
			'pagenum'  : pagenum,
			'keywords' : keywords
		}
		response = self.session.get('http://127.0.0.1/api/mgr/orders',
		                       params=urlpara
		                       )
		responseData(response)
		return response
	
	
	def orders_add(self,name,customerid,medicinelist):
		# 添加一个订单
		payload = {
			"action": "add_order",
			"data": {
				"name": "东莞理工学院3",
				"customerid": 691,
				"medicinelist": [
					{"id": medicinelist[0], "amount": medicinelist[1], "name": medicinelist[2]},
				]
			}
		}
		response = self.session.post('http://127.0.0.1/api/mgr/orders',
		                        json=payload
		                        )
		responseData(response)
		return response
	
	
	def orders_del(self,id):
		# 删除订单信息
		payload = {
			"action": "delete_order",
			"id": id
		}
		
		response = self.session.delete('http://127.0.0.1/api/mgr/orders',
		                          json=payload
		                          )
		responseData(response)
		return response

# 	实例化对象
api = APIMgr()
