"""
@Project ：Auto_bysms_API 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/30
@File   :test_request_date_json.py
"""
import requests,json

# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# json 请求的消息体
payload = {
    "Overall":"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        },
    ]
}

# 可以使用json库的dumps方法，如下
# response = requests.post(
#   "http://httpbin.org/post",
#   proxies = proxies,
#   data = json.dumps(payload)
# )

# 数据对象 直接 传递给post方法的 json参数，如下
response = requests.post(
  "http://httpbin.org/post",
  proxies = proxies,
  json = payload
)

print(response.text)