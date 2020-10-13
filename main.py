import discord
from discord.ext import commands, tasks
import requests
import os


bot = commands.Bot(command_prefix=';')
thumbnail = 'https://i.imgur.com/GKPAp4q.png'


@bot.event
async def on_ready():
    print('히요비봇 온라인')
    game = discord.Game(';help')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 도움말', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=' - ' + prefix + '정보 [N]', value='망가 정보를 불러옵니다.', inline=True)

    await ctx.send(embed)

bot.run(os.environ['token'])