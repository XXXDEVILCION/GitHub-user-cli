import os

import yaml

CONFIG = os.path.join(os.path.dirname(__file__), 'config.yaml')

def load_config():
    try:
        with open(CONFIG,'r') as f:
            config = yaml.safe_load(f)
            token = config.get('github_token')
            if not token :
                print('缺少Token,请先添加')
                token = input('将你的Token粘贴在此处:')    
                with open(CONFIG,'w') as f:
                    f.write(yaml.dump({"github_token":token}))
                    return token
            else:    
                return token
    except yaml.YAMLError:
        print('缺少Token,请先创建config.yaml')
        token = input('将你的Token粘贴在此处:')    
        with open(CONFIG,'w') as f:
            f.write(yaml.dump({"github_token":token}))
            return token
        