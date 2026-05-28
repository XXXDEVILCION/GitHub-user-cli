import os

import json

CONFIG = os.path.join(os.path.dirname(__file__), 'config.json')

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