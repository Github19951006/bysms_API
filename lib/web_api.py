"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :web_api.py
"""
from lib.printResponse import *
from cfg import cfg
class APIMgr:
	
	# 登录
	def mgr_login(self,uername = 'byhy',
	              password = '88888888',
	              uerProxies = False):
		
		payload = {
			'username': uername,
			'password': password
		}
		# 创建session 对象
		self.session = requests.Session()
		# 设置代理环境
		if uerProxies:
			self.session.proxies.update({f'http: http://{cfg.target_host}:8888'})
			
		# 通过session对象 发起请求
		response = self.session.post(f'http://{cfg.target_host}/api/mgr/signin',
		                        data=payload
		                        )
		responseData(response)
		return response
	
	# 列出所有客户
	def customer_list(self, pagesize = 10,
	                  pagenumber = 1,
	                  keywords = ''):
		# URL参数
		payload = {
			'action': 'list_customer',
			'pagesize': pagesize,
			'pagenum': pagenumber,
			'keywords': keywords
		}
		response = self.session.get(f'http://{cfg.target_host}/api/mgr/customers',
		                 params = payload
		                 )
		responseData(response)
		return response
	
	
	# 添加客户
	def customers_add(self,c_data):
		
		payload = {
			"action": "add_customer",
			"data": c_data
		}
			
		response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers',
		                        json=payload
		                        )
		responseData(response)
		return response
	
	# 修改客户信息
	def customers_modify(self,cid,name,phonenumber,address):
		
		payload = {
			"action": "modify_customer",
			"id": cid,
			"newdata": {
				"name": name,
				"phonenumber": phonenumber,
				"address": address
			}
		}
		response = self.session.put(f'http://{cfg.target_host}/api/mgr/customers',
		                       json=payload
		                       )
		responseData(response)
		return response
	
	
	def customers_del(self,cid):
		# 删除客户信息
		payload = {
			"action": "del_customer",
			"id": cid
		}
		
		response = self.session.delete(f'http://{cfg.target_host}/api/mgr/customers',
		                          json=payload
		                          )
		responseData(response)
		return response
	
	# 删除所有药品
	def medicines_del_all(self):
		response = self.medicines_list()
		total_number = response.json()['total']
		if total_number == 0:
			return None
		else:
			response = self.medicines_list(pagesize= total_number)
			retList = response.json()['retlist']
			for medicine_mid in retList:
				self.medicines_del(medicine_mid['id'])
		
	# 删除所有客户
	def customers_del_all(self):
		response = self.customer_list()
		total_number = response.json()['total']
		if total_number == 0:
			return None
		else:
			response = self.customer_list(pagesize=total_number)
			retList = response.json()['retlist']
			for customer_cid in retList:
				self.customers_del(customer_cid['id'])
		
	# 删除所有订单
	def orders_del_all(self):
		response = self.orders_list()
		total_number = response.json()['total']
		if total_number == 0:
			return None
		else:
			response = self.orders_list(pagesize=total_number)
			retList = response.json()['retlist']
			for orders_oid in retList:
				self.orders_del(orders_oid['id'])
	
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
		response = self.session.get(f'http://{cfg.target_host}/api/mgr/medicines',
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
		response = self.session.post(f'http://{cfg.target_host}/api/mgr/medicines',
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
		response = self.session.put(f'http://{cfg.target_host}/api/mgr/medicines',
		                       json=payload
		                       )
		responseData(response)
		return response
	
	
	def medicines_del(self,mid):
		# 删除药品信息
		payload = {
			"action": "del_medicine",
			"id": mid
		}
		
		response = self.session.delete(f'http://{cfg.target_host}/api/mgr/medicines',
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
		response = self.session.get(f'http://{cfg.target_host}/api/mgr/orders',
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
		response = self.session.post(f'http://{cfg.target_host}/api/mgr/orders',
		                        json=payload
		                        )
		responseData(response)
		return response
	
	
	def orders_del(self,oid):
		# 删除订单信息
		payload = {
			"action": "delete_order",
			"id": oid
		}
		
		response = self.session.delete(f'http://{cfg.target_host}/api/mgr/orders',
		                          json=payload
		                          )
		responseData(response)
		return response

# 	实例化对象
api = APIMgr()
