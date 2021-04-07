# -*- coding: utf-8 -*-
import requests
import json
import os

# def get_rp(user_name):
#     base_url = 'https://public-api.tracker.gg/v2/apex/standard/'
#     params = {"TRN-Api-Key": os.environ['TRN_API_KEY']}
#     endpoint = "profile/origin/" + user_name

#     session = requests.Session()
#     req = session.get(url=base_url+endpoint, params=params)

#     req.close()
#     res = json.loads(req.text)

#     rank_value = res["data"]["segments"][0]["stats"]["rankScore"]["value"]
#     rank_name = res["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["rankName"]
#     print("ユーザ名: ", user_name)
#     print("ランク: " + rank_name + " (", rank_value,  ")")

#     ans = "ランク: " + rank_name + " (", rank_value,  ")"

#     return rank_name

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

if __name__ == '__main__':
    a = UseApi(user_name='m1zThePredator')