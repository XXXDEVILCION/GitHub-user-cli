

import requests

import config

STATUS_MESSAGES = {
    404: '用户不存在',
    403: '请求过于频繁',
    401: '认证失败',
    500: 'GitHub服务异常',
    429: '请求过多，请稍后再试',
                              }

def get_user_info():
    token = config.load_config()
    name = input("请输入要查询的用户名:")
    url = f"https://api.github.com/users/{name}"
    headers = {"Authorization":f'Bearer {token}'} 
    try:
        response = requests.get(url,headers = headers)
        code = response.status_code
        if code == 200:
            data = response.json()
            return data, name
        if code not in  STATUS_MESSAGES :
            print(f'发生未知错误，状态码为{code}')
            return None  
        else:
            print("请求失败")
            print(f'状态码为{code}')
            print(STATUS_MESSAGES[code])
            return None
    except Exception as e:
        print('错误信息如下')
        print(type(e))
        print(e)
        return None              