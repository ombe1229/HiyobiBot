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
    embed.add_field(name=';정보 N', value='망가 정보를 불러옵니다.', inline=False)
    embed.add_field(name=';최신', value='최신 망가 10개를 불러옵니다.', inline=False)
    embed.add_field(name=';페이지 N', value='최신 망가 리스트 중 N번째 페이지를 불러옵니다.', inline=False)
    embed.add_field(name=';초대', value='HiyobiBot 초대 링크를 불러옵니다.', inline=False)
    embed.add_field(name=':warning: 경고', value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.\n주의하세요.', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=';정보 N', value='망가 정보를 불러옵니다.', inline=False)
    embed.add_field(name=';최신', value='최신 망가 10개를 불러옵니다.', inline=False)
    embed.add_field(name=';페이지 N', value='최신 망가 리스트 중 N번째 페이지를 불러옵니다.', inline=False)
    embed.add_field(name=';초대', value='HiyobiBot 초대 링크를 불러옵니다.', inline=False)
    embed.add_field(name=':warning: 경고', value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.\n주의하세요.', inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 정보(ctx, arg):
    '''
        if page == None:
            embed = discord.Embed(title=':bulb: 정보 명령어 사용 방법',description=';정보 N\n해당 망가의 정보를 불러옵니다.\nex) ;정보 1629336', color=0xff0000)
            embed.set_thumbnail(url=thumbnail)

            await ctx.send(embed=embed)
            return None
        '''

    if not arg.isdigit():
        await ctx.send('숫자를 입력해주세요.')
        return None

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
    embed.set_thumbnail(url=f'http://cdn.hiyobi.me/tn/{arg}.jpg')
    embed.add_field(name='제목', value=f'{title}', inline=False)
    embed.add_field(name='작가', value=f'{artists}', inline=True)
    embed.add_field(name='원작', value=f'{parodys}', inline=True)
    embed.add_field(name='원작', value='없음', inline=True)
    embed.add_field(name='캐릭터', value=f'{character_list}', inline=False)
    embed.add_field(name='태그', value=f'{tag_list}', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def 최신(ctx):
    await ctx.send('정보를 불러오는 중입니다...')

    data = requests.get(f'https://api.hiyobi.me/list')
    resp = data.json()

    embed = discord.Embed(title=f':scroll: 최신 망가 리스트', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        title = resp['list'][i]['title']
        id = resp['list'][i]['id']
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists}\n번호 : {id}', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def 페이지(ctx, page):
    '''
    if page == None:
        embed = discord.Embed(title=':bulb: 페이지 명령어 사용 방법',description=';페이지 N\n최신 망가 리스트 중 N번째 페이지를 불러옵니다.\nex) ;페이지 2', color=0xff0000)
        embed.set_thumbnail(url=thumbnail)

        await ctx.send(embed=embed)
        return None
    '''

    if not page.isdigit():
        await ctx.send('숫자를 입력해주세요.')
        return None

    await ctx.send('정보를 불러오는 중입니다...')

    data = requests.get(f'https://api.hiyobi.me/list/{page}')
    resp = data.json()

    embed = discord.Embed(title=f':scroll: 최신 망가 리스트 - {page}페이지', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        title = resp['list'][i]['title']
        id = resp['list'][i]['id']
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists}\n번호 : {id}', inline=False)

    await ctx.send(embed=embed)




bot.run(os.environ['token'])
