# -*- coding: utf-8 -*-
import requests
import json
import os

import controller

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
    UseApi クラスのインスタンス化（なるべくここだけで。）
    コマンドを受け取り、結果文字列を返す関数
    '''
    commands = ['/ls', '/rp', '/rank', '/stats', '/test']
    # DB 初期化の位置をどうするのか
    db = controller.DB()
    if command == '/ls':
        # friendsc の結果を返す、get_result の user_name は使用しない
        ans = ''
        friends = ['m1zThePredator', 'megushinnn']
        for user_name in friends:
            ans += get_result(command='/stats', user_name=user_name) + '\n'
        return ans
    if command == '/rp':
        # ５データ取得
        rp_list = db.get_recent_5(user_name=user_name)
        ans = ''''''
        for i in rp_list:
            ans += str(i['rp']) + '   ' + str(i['registerd_at']) + '\n'
        return ans[:-2]
    if command == '/rp_old':
        # 現在の rp のみを取得
        use_api = UseApi(user_name=user_name)
        return use_api.get_rp()
    if command == '/rank':
        use_api = UseApi(user_name=user_name)
        return use_api.get_rank()
    if command == '/stats':
        use_api = UseApi(user_name=user_name)
        # firestore に保存
        db.set_rp(user_name=user_name, rp=use_api.get_rp())
        return '''\
name: {user_name}
rank: {rank}
point: {rp}
        '''.format(user_name=user_name,
                    rank=use_api.get_rank(),
                    rp=use_api.get_rp())
    if  command == '/test':
        recent_5_data = db.get_recent_5()
        print(recent_5_data[0]['rp'])
        # return db.set_rp(user_name=user_name, rp=use_api.get_rp())


