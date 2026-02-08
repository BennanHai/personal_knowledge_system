# @Author: Benanahai
# @Time  : 2025/3/1 16:51 
# @Desc  :

import requests

class DeepSeekAPI:

    def call_deepseek_api(question):
        """
        调用 DeepSeek API 获取答案
        :param question: 问题
        :return: 答案
        """
        # 填写 API Key
        api_key = "sk-84a17e4826a1487392e115ab525c71d0"

        try:

            url = "https://api.deepseek.com/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
            data = {
                # 指定使用 R1 模型（deepseek-reasoner）或者 V3 模型（deepseek-chat）
                "model": "deepseek-reasoner",
                # "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "你是一个专业的助手"},
                    # 提示词
                    # {"role": "user", "content": "python连接MongoDB的代码"}
                    {"role": "user", "content": question}
                ],
                "stream": False  # False: 关闭流式传输
            }
            print('正在查询答案...')
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 402:
                print("ERROR: 账户余额不足，请登录平台充值！")
            else:
                print(f"ERROR: API 调用失败 - {err}")
        except Exception as e:
            print(f"ERROR: {e}")


def main(question):
        """
        调用 DeepSeek API 获取答案
        :param question: 问题
        :return: 答案
        """
        return DeepSeekAPI.call_deepseek_api(question)


if __name__ == '__main__':
    question = "你是谁"
    print(main(question))
