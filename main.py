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
    embed.add_field(name=';정보 [N]', value='망가 정보를 불러옵니다.', inline=True)
    embed.add_field(name=';보기 [N] [N]', value='망가의 해당 페이지를 확인합니다.', inline=False)
    embed.add_field(name=':warning: 경고', value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.\n주의하세요.', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=';정보 [N]', value='망가 정보를 불러옵니다.', inline=False)
    embed.add_field(name=';보기 [N] [N]', value='망가의 해당 페이지를 확인합니다.', inline=False)
    embed.add_field(name=':warning: 경고', value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.\n주의하세요.', inline=False)
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

    try:
        artists = resp['artists'][0]['display']
    except:
        artists = '없음'

    try:
        parodys = resp['parodys'][0]['display']
    except:
        parodys = '없음'

    try:
        characters = resp['characters']
        character_list = ''
        for i in range(len(characters)):
            if i != 0:
                character_list += ', '
            character_list += resp['characters'][i]['display']
    except:
        character_list = '없음'

    try:
        tags = resp['tags']
        tag_list = ''
        for i in range(len(tags)):
            if i != 0:
                tag_list += ', '
            tag_list += resp['tags'][i]['display']
    except:
        tag_list = '없음'

    embed = discord.Embed(title=f':closed_book: {arg} 검색 결과', color=0xff0000)
    embed.set_thumbnail(url=f'http://cdn.hiyobi.me/tn/{arg}.jpg')
    embed.add_field(name='제목', value=f'{title}', inline=False)
    embed.add_field(name='작가', value=f'{artists}', inline=True)
    embed.add_field(name='원작', value=f'{parodys}', inline=True)
    embed.add_field(name='캐릭터', value=f'{character_list}', inline=False)
    embed.add_field(name='태그', value=f'{tag_list}', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def 보기(ctx, arg1, arg2):
    await ctx.send('페이지를 불러오는 중입니다...\n검색 결과가 없으면 사진이 뜨지 않습니다.')
    if len(arg2) == 1:
        arg2 = '0'+str(arg2)
    url = f'https://cdn.hiyobi.me/data/{arg1}/{arg2}.png'

    await ctx.send(url)


bot.run(os.environ['token'])
