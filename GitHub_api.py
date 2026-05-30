import asyncio

import requests

import config

import time

STATUS_MESSAGES = {
    404: '用户不存在',
    403: '请求过于频繁',
    401: '认证失败',
    500: 'GitHub服务异常',
    429: '请求过多，请稍后再试',
}

async def get_user_info(name):
    token = config.load_config()
    url = f"https://api.github.com/users/{name}"
    headers = {"Authorization": f'Bearer {token}'}
    try:
        t0 = time.time()
        print(f"开始查询 {name}")
        response = await asyncio.to_thread(requests.get, url, headers=headers)
        print(f"{name} 单次耗时: {time.time() - t0:.2f} 秒")
        code = response.status_code
        if code == 200:
            data = response.json()
            return data, name
        if code not in STATUS_MESSAGES:
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

async def main():
    args = input('输入你要查询用户名(不同用户名用逗号隔开):')
    args = args.strip().split(",")
    coros = [get_user_info(name) for name in args]
    start = time.time()
    results = await asyncio.gather(*coros)
    print(f"总耗时: {time.time() - start:.2f} 秒")
    return results
