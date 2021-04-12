# -*- coding: utf-8 -*-
import requests
import json
import os

class UseApi:
    '''
    TRNのApexApiを叩くクラス。
    ユーザーネームを一つ引数にとり、各情報を取得する。
    '''
    def __init__(self, user_name):
        self.user_name = user_name
        # ここでApiたたく
        base_url = 'https://public-api.tracker.gg/v2/apex/standard/'
        params = {"TRN-Api-Key": os.environ['TRN_API_KEY']}
        endpoint = "profile/origin/" + self.user_name

        session = requests.Session()
        req = session.get(url=base_url+endpoint, params=params)

        req.close()
        self.res = json.loads(req.text)
    
    def get_rp(self):
        self.rp = self.res["data"]["segments"][0]["stats"]["rankScore"]["value"]
        return self.rp

    def get_rank(self):
        self.rank = self.res["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["rankName"]
        return self.rank

def get_result(command, user_name):
    '''
    UseApi クラスをインスタンス化し、コマンドを受け取り、結果文字列を返す関数
    '''
    if command == '/ls':
        # friendsc の結果を返す、get_result の user_name は使用しない
        ans = ''
        friends = ['m1zThePredator', 'megushinnn']
        for u_name in friends:
            ans += get_result(command='/stats', user_name=u_name) + '\n'
        return ans
    if command == '/rp':
        use_api = UseApi(user_name=user_name)
        return use_api.get_rp()
    if command == '/rank':
        use_api = UseApi(user_name=user_name)
        return use_api.get_rank()
    if command == '/stats':
        import controller
        use_api = UseApi(user_name=user_name)
        controller.set_rp(user_name=user_name, rp=use_api.get_rp())
        return '''\
name: {user_name}
rank: {rank}
point: {rp}
        '''.format(user_name=user_name,
                    rank=use_api.get_rank(),
                    rp=use_api.get_rp())
    if  command == '/test':
        # ここでdbさわってみる
        use_api = UseApi(user_name=user_name)
        import controller
        return controller.set_rp(user_name=user_name, rp=use_api.get_rp())


