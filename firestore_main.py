'''
コレクションにユーザ名、ドキュメントにrpを追加していく？
フィールドは、rp, timestamp のみかな。検討
'''

import read_key

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("discordapexinfobot-firebase-adminsdk-w4ryu-f123a1595c.json")
firebase_admin.initialize_app(cred)

def select_db_from_firestore():
    db = firestore.client()
    docs = db.collection('m1zThePredator').stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        # print(doc.to_dict()['rp'])
    return f'{doc.id} => {doc.to_dict()}'

if __name__ == '__main__':
    select_db_from_firestore()