# -*- coding: utf-8 -*-
import requests
import json
import os

# base_url = 'https://public-api.tracker.gg/v2/apex/standard/'

# params = {"TRN-Api-Key": os.environ['TRN_API_KEY']}

# user_name = 'm1zThePredator'

# endpoint = "profile/origin/" + user_name

# session = requests.Session()
# req = session.get(url=base_url+endpoint, params=params)

# print(req.text)

# print("ステータスコード: " + str(req.status_code))
# req.close()
# res = json.loads(req.text)

# rank_value = res["data"]["segments"][0]["stats"]["rankScore"]["value"]
# rank_name = res["data"]["segments"][0]["stats"]["rankScore"]["metadata"]["rankName"]
# print("ユーザ名: ", user_name)
# print("ランク: " + rank_name + " (", rank_value,  ")")    

TRN_API_KEY = 'eba7ee87-3e0c-42fb-b80d-06113f6f89bf'

def get_rp(user_name):
    base_url = 'https://public-api.tracker.gg/v2/apex/standard/'
    # params = {"TRN-Api-Key": os.environ['TRN_API_KEY']}
    params = {"TRN-Api-Key": TRN_API_KEY}
    endpoint = "profile/origin/" + user_name

    session = requests.Session()
    req = session.get(url=base_url+endpoint, params=params)

    req.close()
    res = json.loads(req.text)

    rank_value = res["data"]["segments"][0]["stats"]["rankScore"]["value"]

    return rank_value