import discord
from discord.ext import commands, tasks
import json
import requests
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

    if responseJson.get('title') == '정보없음':
        embed = discord.Embed(title=f':warning: 오류', color=0xff0000)
        embed.set_thumbnail(url=thumbnail)
        embed.add_field(name='검색 결과가 없습니다.', value='번호가 정확한지 다시 한번 확인해주세요.', inline=False)

        await ctx.send(embed=embed)
        return None

    data = requests.get(f'https://api.hiyobi.me/gallery/{arg}')
    resp = data.json()

    title = responseJson.get('title')

    artists = resp['artists'][0]['display']
    parodys = resp['parodys'][0]['display']

    characters = resp['characters']
    character_list = ''
    for i in range(len(characters)):
        if i != 0:
            character_list += ', '
        character_list += resp['characters'][i]['display']

    tags = resp['tags']
    tag_list = ''
    for i in range(len(tags)):
        if i != 0:
            tag_list += ', '
        tag_list += resp['tags'][i]['display']

    embed = discord.Embed(title=f':closed_book: {arg} 검색 결과', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name='제목', value=f'{title}', inline=False)
    embed.add_field(name='작가', value=f'{artists}', inline=True)
    embed.add_field(name='원작', value=f'{parodys}', inline=True)
    embed.add_field(name='캐릭터', value=f'{character_list}', inline=False)
    embed.add_field(name='태그', value=f'{tag_list}', inline=False)

    await ctx.send(embed=embed)


bot.run(os.environ['token'])