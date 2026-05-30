# ###  GitHub 用户信息查询器

# import GitHub_api as api

# import history

# import info
     


# def main():
#     res = api.get_user_info()
#     if res is not None:
#         data, name = res
#         info.print_info(data, name)
#         file = history.History(history.DEFAULT_HISTORY_FILE)
#         file.save_history(data,name)
        

# while True:        

#     print('1.查询用户\n'
#           '2.查看历史记录\n'
#           '3.退出')

#     choose = input('请选择:')


#     if choose == '1':

#         main()

#     elif choose == '2':
#         file = history.History(history.DEFAULT_HISTORY_FILE)
#         try:  
#             times = len(file.records)
#             print('最近一次查询记录:')
#             print(f"用户名:{file.records[-1]['用户名']},关注者:{file.records[-1]['关注者']},查询时间:{file.records[-1]['查询时间']}")
#             print('***历史查询记录***')
#             for record in file.records:
#                 print(f"用户名:{record['用户名']},关注者:{record['关注者']},查询时间:{record['查询时间']}")
#             print(f"总查询次数:{times}")

#         except IndexError :
#                 print('暂无历史记录')    

#     elif choose =='3':
#         break
        
#     else:
#         print('请输入功能序号')



import requests
import config

def create_repo():
    
    token = config.load_config()
    response = requests.post(url='https://api.github.com/user/repos',headers={"Authorization":f'Bearer {token}'},json={'name':'测试仓库'})
    print(response)
create_repo()    