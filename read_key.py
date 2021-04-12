import os

try:
    import key
    print('ローカル環境からfirestoreに接続')
except:
    print('herokuからfirestoreに接続')

dic = {
    "type": os.environ['FB_TYPE'],
    "project_id": os.environ['FB_PROJECT_ID'],
    "private_key_id": os.environ['FB_PRIVATE_KEY_ID'],
    "private_key": os.environ['FB_PRIVATE_KEY'].replace('\\n', '\n'),
    "client_email": os.environ['FB_CLIENT_EMAIL'],
    "client_id": os.environ['FB_CLIENT_ID'],
    "auth_uri": os.environ['FB_AUTH_URL'],
    "token_uri": os.environ['FB_TOKEN_URI'],
    "auth_provider_x509_cert_url": os.environ['FB_AUTH_CERT_URL'],
    "client_x509_cert_url": os.environ['FB_CLIENT_CERT_URL']
  }

import json

with open('discordapexinfobot-firebase-adminsdk-w4ryu-f123a1595c.json', mode='wt', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)

print('read_key.py 実行完了')