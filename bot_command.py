def bot_command(command):
    '''
    コマンドを入力すると、結果の文字列を返す関数
    '''
    use_api = trn_api.UseApi(user_name='megushinnn')
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('こんにちは！')
    if message.content == '/rp':
        await message.channel.send(use_api.get_rp())
    if message.content == '/rank':
        await message.channel.send(use_api.get_rank())
    if message.content == '/stats':
        ans = '''\
name: {user_name}
rank: {rank}
point: {rp}
        '''.format(user_name=use_api.user_name,
                    rank=use_api.get_rank(),
                    rp=use_api.get_rp())
    if command == '/test':
        return 'testmessage'
    if command == '/rp':
        
