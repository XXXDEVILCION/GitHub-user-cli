###  GitHub 用户信息查询器

import os

import json

import requests

from datetime import datetime

HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'history.json')
CONFIG = os.path.join(os.path.dirname(__file__), 'config.json')

STATUS_MESSAGES = {
    404: '用户不存在',
    403: '请求过于频繁',
    401: '认证失败',
    500: 'GitHub服务异常',
    429: '请求过多，请稍后再试',
                              }

def get_user_info():
    token = load_config()
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

def print_info(data, name):
    print(f"{name}的GitHub信息:")
    print(f"用户名:{data['login']}")
    print(f"关注者:{data['followers']}")    
    print(f"仓库:{data['public_repos']}")
    print(f"简介:{data.get('bio') or '暂无简介'}")

def save_history(data,name):
    if os.path.exists(HISTORY_FILE):
        try:
            with open (HISTORY_FILE,'r') as f:
                RECORD = json.loads(f.read())
        except json.JSONDecodeError:
            RECORD = []        
            
    else:
        RECORD = []
    followers= data['followers']
    record = {'用户名':name,'关注者':followers,'查询时间':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    RECORD.append(record)
    with open (HISTORY_FILE,'w') as f:
        f.write(json.dumps(RECORD))     

def load_config():
    try:
        with open(CONFIG,'r') as f:
            config = json.load(f)
            token = config.get('github_token')
            if not token :
                print('缺少Token,请先添加')
                token = input('将你的Token粘贴在此处:')    
                with open(CONFIG,'w') as f:
                    f.write(json.dumps({"github_token":token}))
                    return token
            else:    
                return token
    except json.JSONDecodeError:
        print('缺少Token,请先创建config.json')
        token = input('将你的Token粘贴在此处:')    
        with open(CONFIG,'w') as f:
            f.write(json.dumps({"github_token":token}))
            return token
                



def main():
    res = get_user_info()
    if res is not None:
        data, name = res
        print_info(data, name)
        save_history(data,name)
        
        

while True:        

    print('1.查询用户\n'
          '2.查看历史记录\n'
          '3.退出')

    choose = input('请选择:')


    if choose == '1':

        main()

    elif choose == '2':
        if os.path.exists(HISTORY_FILE):
            try:
                with open (HISTORY_FILE,'r') as f:
                    RECORD = json.loads(f.read())
                    lens = len(RECORD)
                    print('最近一次查询记录:')
                    print(f"用户名:{RECORD[-1]['用户名']},关注者:{RECORD[-1]['关注者']},查询时间:{RECORD[-1]['查询时间']}")
                    print('***历史查询记录***')
                    for record in RECORD:
                        print(f"用户名:{record['用户名']},关注者:{record['关注者']},查询时间:{record['查询时间']}")
                    print(f"总查询次数:{lens}")

            except json.JSONDecodeError:
                print('暂无历史记录或文件已经损坏')
                            
        else:
            print("暂无历史记录")

    elif choose =='3':
        break
        
    else:
        print('请输入功能序号')

