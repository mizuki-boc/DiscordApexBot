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

    def get_result(self, command):
        if command == '/test':
            return 'test_message'
        if command == '/rp':
            return self.get_rp()
        if command == '/rank':
            return get_rank()
        if command == '/stats':
            return '''\
name: {user_name}
rank: {rank}
point: {rp}
            '''.format(user_name=self.user_name,
                        rank=self.get_rank(),
                        rp=self.get_rp())

if __name__ == '__main__':
    a = UseApi(user_name='m1zThePredator')