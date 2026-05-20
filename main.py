###  GitHub 用户信息查询器

import requests

STATUS_MESSAGES ={  404:'用户不存在'
                ,403:'请求过于频繁'
                ,401:'认证失败'
                ,500:'Gith、Hub服务异常'
                ,429:'请求过多，请稍后再试'}
def get_user_info():
    name = input("请输入要查询的用户名:")
    url = f"https://api.github.com/users/{name}"
    try:
        response = requests.get(url)
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


def main():
    res = get_user_info()
    if res is not None:
        data, name = res
        print_info(data, name)

main()