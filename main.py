import discord
from discord.ext import commands, tasks
import requests
import os


bot = commands.Bot(command_prefix=';')
thumbnail = 'https://i.imgur.com/GKPAp4q.png'


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';help'))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=' - ;정보 [N]', value='망가 정보를 불러옵니다.', inline=True)

    await ctx.send(embed=embed)

bot.run(os.environ['token'])