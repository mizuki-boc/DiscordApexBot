import os

try:
    import key
    print('ローカル環境からfirestoreに接続')
except:
    print('herokuからfirestoreに接続')

dic = {
    "type": os.environ['fb_type'],
    "project_id": os.environ['fb_project_id'],
    "private_key_id": os.environ['fb_private_key_id'],
    "private_key": os.environ['fb_private_key'],
    "client_email": os.environ['fb_client_email'],
    "client_id": os.environ['fb_client_id'],
    "auth_uri": os.environ['fb_auth_uri'],
    "token_uri": os.environ['fb_token_uri'],
    "auth_provider_x509_cert_url": os.environ['fb_auth_provider_x509_cert_url'],
    "client_x509_cert_url": os.environ['fb_client_x509_cert_url']
  }

import json

with open('discordapexinfobot-firebase-adminsdk-w4ryu-f123a1595c.json', mode='wt', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)

print('read_key.py 実行完了')