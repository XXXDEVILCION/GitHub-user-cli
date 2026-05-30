import os

import json

from datetime import datetime


DEFAULT_HISTORY_FILE = os.path.join(os.path.dirname(__file__), 'history.json')


class History:
    def __init__(self,file_path):
        self.file_path = file_path
        if os.path.exists(file_path):
            try:
                with open (file_path,'r') as f:
                    self.records = json.load(f)
            except json.JSONDecodeError:
                self.records= [] 
        else:
           self.records = []                

    def save_history(self,data,name):
        followers= data['followers']
        record = {'用户名':name,'关注者':followers,'查询时间':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.records.append(record)
        with open (self.file_path,'w') as f:
            f.write(json.dumps(self.records))       
        