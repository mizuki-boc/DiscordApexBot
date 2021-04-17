import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Controller:
    def __init__(self):
        '''
        firestore接続
        '''
        cred = credentials.Certificate("discordapexinfobot-firebase-adminsdk-w4ryu-f123a1595c.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def select_db_from_firestore(self):
        '''
        json取り出し（テスト）
        '''
        docs = self.db.collection('m1zThePredator').stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
            # print(doc.to_dict()['rp'])
        return f'{doc.id} => {doc.to_dict()}'
        
    def set_rp(self, user_name, rp):
        '''
        rp, timestamp の保存
        '''
        doc_ref = self.db.collection(user_name).document()
        doc_ref.set({
            'rp': rp,
            'registerd_at': firestore.SERVER_TIMESTAMP,
        })

    def get_recent_5(self, user_name):
        '''
        最新のデータ (list) を返す
        '''
        ans = []
        docs = self.db.collection(user_name)\
                   .order_by('registerd_at', direction=firestore.Query.DESCENDING)\
                   .limit(5).stream()
        for doc in docs:
            # print(doc.to_dict())
            ans.append(doc.to_dict())
        return ans

    def check_existance(self):
        '''
        入力されたユーザが存在するか確認する
        '''
        is_exist = true
        return is_exist
    

if __name__ == '__main__':
    db = Controller()
    db.get_recent_5('m1zThePredator')