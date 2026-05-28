def print_info(data, name):
    print(f"{name}的GitHub信息:")
    print(f"用户名:{data['login']}")
    print(f"关注者:{data['followers']}")    
    print(f"仓库:{data['public_repos']}")
    print(f"简介:{data.get('bio') or '暂无简介'}")