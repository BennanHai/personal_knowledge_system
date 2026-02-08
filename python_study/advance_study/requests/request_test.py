# @Author: Benanahai
# @Time  : 2024/11/17 20:24

import requests

requests.get("http://httpbin.org/get") #GET请求
requests.post("http://httpbin.org/post") #POST请求
requests.put("http://httpbin.org/put") #PUT请求
requests.delete("http://httpbin.org/delete") #DELETE请求
requests.head("http://httpbin.org/get") #HEAD请求
requests.options("http://httpbin.org/get") #OPTIONS请求


# 1. 发送Get请求
url = "https://www.baidu.com"
response = requests.get(url)
# 查看响应状态码
print(response.status_code)
# 响应内容
print(response.text)
# 响应头
print(f"响应头 ：{response.headers}")
# 响应体
print(f"响应体： {response.content}")


# 2. 发送post请求
print("* -- *" * 33)
url = "http://httpbin.org/post"
data = {"name": "test", "age": 18}
response = requests.post(url, data=data)
print(response.text)


# 3. 设置请求头
# 可以通过将请求头信息封装为字典，并传递给headers参数来实现。
print("* -- *" * 33)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
response = requests.post(url, headers=headers)
print(response.text)


# 4. 对于get请求， 可以通过params参数传递请求参数
print("* -- *" * 33)
params = {'name': 'test', 'age': 34, 'sex': 'man'}
response = requests.get("http://httpbin.org/get", params=params)
print(response.text)


# 5. 高级用法
# 5.1 设置超时时间
response = requests.get("http://httpbin.org/get", timeout=5)
# print(response)

# 5.2 异常处理
from requests import Timeout, HTTPError
try:
    response = requests.get("http://httpbin.org/get", timeout=0.01)
except Timeout:
    print("请求超时")
except HTTPError as e:
    print(f"HTTPError: {e}")
