# -*- coding: utf-8 -*-
import os

import discord

import bot_command
# import trn_api

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    use_api = trn_api.UseApi(user_name='megushinnn')
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
#     if message.content == '/hello':
#         await message.channel.send('こんにちは！')
#     if message.content == '/rp':
#         await message.channel.send(use_api.get_rp())
#     if message.content == '/rank':
#         await message.channel.send(use_api.get_rank())
#     if message.content == '/stats':
#         ans = '''\
# name: {user_name}
# rank: {rank}
# point: {rp}
#         '''.format(user_name=use_api.user_name,
#                     rank=use_api.get_rank(),
#                     rp=use_api.get_rp())
#         await message.channel.send(ans)
    await message.channel.send(trn_api.get_result(message.content))

# Botの起動とDiscordサーバーへの接続
client.run(os.environ['DISCORD_TOKEN'])