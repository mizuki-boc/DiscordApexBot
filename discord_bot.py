# -*- coding: utf-8 -*-
import discord
import os

import trn_api

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
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/rp':
        await message.channel.send(trn_api.get_rp(user_name='m1zThePredator'))

# Botの起動とDiscordサーバーへの接続
client.run(os.environ['DISCORD_TOKEN'])
# client.run(DISCORD_TOKEN)