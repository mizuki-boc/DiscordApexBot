def get_result(command, user_name, db):
    '''
    INPUT
        str command: 操作コマンド
        str user_name: ユーザネーム
        instance db: データベースコントローラのインスタンス
    OUTPUT
        str: bot が送信する文字列
    '''
    commands = ['/ls', '/rp', '/rank', '/stats', '/test']
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
