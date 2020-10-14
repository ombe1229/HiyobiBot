import discord
from discord.ext import commands, tasks
import json
from urllib.request import urlopen
import os


bot = commands.Bot(command_prefix=';')
thumbnail = 'https://i.imgur.com/GKPAp4q.png'


@bot.event
async def on_ready():
    print('봇 온라인.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';명령어'))

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=' - ;정보 [N]', value='망가 정보를 불러옵니다.', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=' - ;정보 [N]', value='망가 정보를 불러옵니다.', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def 정보(ctx, arg):
    await ctx.send('정보를 검색하는 중입니다...')

    response = urlopen(f'https://api.hiyobi.me/gallery/{arg}').read()
    responseJson = json.loads(response)

    title = responseJson.get('title')
    artist = responseJson.get('artists.value')

    embed = discord.Embed(title=f':closed_book: {arg} 검색 결과', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=':desktop: 제목', value=f'{title}', inline=True)
    embed.add_field(name=':pencil2: 작가', value=f'{artist}', inline=False)

    await ctx.send(embed=embed)



bot.run(os.environ['token'])