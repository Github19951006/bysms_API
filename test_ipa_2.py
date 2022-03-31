"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_ipa_2.py
"""
import requests

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

urlpara = {
  'wd' : 'iphone',
  'rsv_spt' : '1'
}

response = requests.get('https://www.baidu.com/s',params= urlpara,proxies = proxies)
print(response.text)