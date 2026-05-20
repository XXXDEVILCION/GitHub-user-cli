###  GitHub 用户信息查询器

import requests


def get_user_info():
    name = input("请输入要查询的用户名:")
    url = f"https://api.github.com/users/{name}"
    response = requests.get(url)
    data = response.json()
    return data, name


def print_info(data, name):
    print(f"{name}的GitHub信息:")
    print(f"用户名:{data['login']}")
    print(f"关注者:{data['followers']}")
    print(f"仓库:{data['public_repos']}")
    print(f"简介:{data.get('bio') or '暂无简介'}")


def main():
    data, name = get_user_info()
    print_info(data, name)


main()