"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/04/03
@File   :bysms_api_practice.py
"""
import requests, json
from lib.printResponse import *

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 创建一下session 对象
session = requests.Session()

'''--------------------------------客户---------------------------'''
def signin():
    # 请求消息体
    # 参数以 格式 x-www-form-urlencoded 存储
    payload = {
        'username': 'byhy',
        'password': '88888888'
    }
    
    # 登录
    # 通过session对象 发起请求
    response = session.post('http://127.0.0.1/api/mgr/signin',
                            data=payload,
                            proxies = proxies
                            )
    return responseData(response)
signin()

def customers_list():
    '''--------------------------------客户---------------------------'''
    # 列出所有客户
    # URL参数
    urlpara = {
        'action' : 'list_customer',
        'pagesize' : '30',
        'pagenum' : '1',
        'keywords' : ''
    }
    response = session.get('http://127.0.0.1/api/mgr/customers',
                            params = urlpara,
                            proxies = proxies
                            )
    return responseData(response)

customers_list()

def customers_add():
    # 添加一个客户
    payload = {
        "action":"add_customer",
        "data":{
            "name":"武汉市桥西医院",
            "phonenumber":"13345679934",
            "address":"武汉市桥西医院北路"
        }
    }
    response = session.post('http://127.0.0.1/api/mgr/customers',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
customers_add()

def customers_modify():
    # 修改客户信息
    payload = {
        "action":"modify_customer",
        "id": 695,
        "newdata":{
            "name":"武汉市桥北医院",
            "phonenumber":"13345678888",
            "address":"武汉市桥北医院北路"
        }
    }
    response = session.put('http://127.0.0.1/api/mgr/customers',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
customers_modify()

def customers_del():
    # 删除客户信息
    payload = {
        "action":"del_customer",
        "id": 696
    }
    
    response = session.delete('http://127.0.0.1/api/mgr/customers',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
customers_del()


'''--------------------------------药品---------------------------'''
def medicines_list():
    # 列出所有客户
    # URL参数
    urlpara = {
    	'action' : 'list_medicine',
    	'pagesize' : '4',
    	'pagenum' : '1',
    	'keywords' : ''
    }
    response = session.get('http://127.0.0.1/api/mgr/medicines',
                            params = urlpara,
                            proxies = proxies
                            )
    return responseData(response)
medicines_list()


def medicines_add():
    # 添加一个药品
    payload = {
        "action":"add_medicine",
        "data":{
            "name": "青霉素",
            "desc": "青霉素 国字号",
            "sn": "099877883837"
        }
    }
    response = session.post('http://127.0.0.1/api/mgr/medicines',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
medicines_list()


def medicines_modify():
    # 修改药品信息
    payload = {
        "action":"modify_medicine",
        "id": 279,
        "newdata":{
            "name": "修青霉素",
            "desc": "修青霉素 国字号",
            "sn": "0889898989898"
        }
    }
    response = session.put('http://127.0.0.1/api/mgr/medicines',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
medicines_modify()

def medicines_del():
    # 删除药品信息
    payload = {
        "action":"del_medicine",
        "id": 279
    }
    
    response = session.delete('http://127.0.0.1/api/mgr/medicines',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
medicines_del()

'''--------------------------------订单---------------------------'''
def orders_list():
    # 列出所有客户
    # URL参数
    urlpara = {
        'action' : 'list_order',
        'pagesize' : '4',
        'pagenum' : '1',
        'keywords' : ''
    }
    response = session.get('http://127.0.0.1/api/mgr/orders',
                            params = urlpara,
                            proxies = proxies
                            )
    return responseData(response)
orders_list()

def orders_add():
    # 添加一个订单
    payload = {
        "action":"add_order",
        "data":{
            "name":"东莞理工学院3",
            "customerid":691,
            "medicinelist":[
                {"id":290,"amount":5,"name":"青霉素"},
                {"id":289,"amount":5,"name":"青霉素"}
            ]
        }
    }
    response = session.post('http://127.0.0.1/api/mgr/orders',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
orders_add()

def orders_del():
    # 删除订单信息
    payload = {
        "action":"delete_order",
        "id": 291
    }
    
    response = session.delete('http://127.0.0.1/api/mgr/orders',
                            json = payload,
                            proxies = proxies
                            )
    return responseData(response)
orders_del()