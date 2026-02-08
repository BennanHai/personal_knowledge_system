# @Author: Benanahai
# @Time  : 2025/2/15 11:26 
# @Desc  :


"""
OpenAI API 调用示例
"""
# from openai import OpenAI
#
# client = OpenAI(api_key="Bearer sk-84a17e4826a1487392e115ab525c71d0", base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )
#
# print(response.choices[0].message.content)


# import requests
#
# # 填写 API Key
# API_KEY = "sk-84a17e4826a1487392e115ab525c71d0"
#
# url = "https://api.deepseek.com/chat/completions"
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {API_KEY}"
# }
#
# data = {
#     # 指定使用 R1 模型（deepseek-reasoner）或者 V3 模型（deepseek-chat）
#     "model": "deepseek-reasoner",
#     # "model": "deepseek-chat",
#     "messages": [
#         {"role": "system", "content": "你是一个专业的助手"},
#         # 提示词
#         # {"role": "user", "content": "python连接MongoDB的代码"}
#         {"role": "user", "content": {YOUR_QUESTion}}
#     ],
#     "stream": False  # 关闭流式传输
# }
#
# response = requests.post(url, headers=headers, json=data)
#
# if response.status_code == 200:
#     result = response.json()
#     print(result['choices'][0]['message']['content'])
# else:
#     print("请求失败，错误码：", response.status_code)
#
#

"""
原生requests库调用示例
"""
import requests

def call_deepseek_api(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-84a17e4826a1487392e115ab525c71d0",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100  # 限制生成长度以降低成本
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # 主动抛出 HTTP 错误
        return response.json()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 402:
            print("ERROR: 账户余额不足，请登录平台充值！")
        else:
            print(f"ERROR: API 调用失败 - {err}")
    except Exception as e:
        print(f"ERROR: {e}")

# 示例调用
result = call_deepseek_api("python连接MongoDB的代码")
if result:
    # print(result)
    print(result["choices"])