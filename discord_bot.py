# -*- coding: utf-8 -*-
'''
discord 操作 main 関数
'''
import os
import discord

import controller
import command_receiver
import trn_api

# 接続に必要なオブジェクトを生成
client = discord.Client()

# コントローラ初期化
db = controller.Controller()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    await message.channel.send(command_receiver.get_result(command=message.content,\
                                                           user_name='m1zThePredator',\
                                                           db=db))

# Botの起動とDiscordサーバーへの接続
client.run(os.environ['DISCORD_TOKEN'])