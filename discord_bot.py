# -*- coding: utf-8 -*-
'''
discord 操作 main 関数
'''
import os
import discord
from discord.ext import commands

import controller
import command_receiver
import trn_api

# コマンドのプレフィックス
bot = commands.Bot(command_prefix='!')

# コントローラ初期化
db = controller.Controller()

@bot.event
async def on_ready():
    print('ログインしました')

# 以下コマンド
@bot.command()
async def test(ctx, arg):
    await ctx.channel.send(arg)

@bot.command()
async def rp(ctx):
    rp_dict_list = db.get_recent_5(user_name='m1zThePredator')
    ans = ''''''
    for d in rp_dict_list:
        ans += str(d['rp']) + '   ' + str(d['registerd_at']) + '\n'
    await ctx.channel.send(ans[:-2])

@bot.command()
async def ls(ctx):
    ans = ''''''
    friends = ['m1zThePredator', 'megushinnn']
    for user_name in friends:
        use_api = trn_api.UseApi(user_name=user_name)
        category = ['name', 'rank', 'point']
        info = [user_name, use_api.get_rank(), use_api.get_rp()]
        for (c, i) in zip(category, info):
            ans += c + ': ' + str(i) + '\n'
        ans += '\n'
    await ctx.channel.send(ans[:-2])

bot.run(os.environ['DISCORD_TOKEN'])