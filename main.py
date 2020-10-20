import discord
from discord.ext import commands, tasks
import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os


bot = commands.Bot(command_prefix=';')
thumbnail = 'https://i.imgur.com/GKPAp4q.png'
bot.remove_command('help')


@bot.event
async def on_ready():
    print('봇 온라인.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';명령어 | ombe#7777'))


@bot.command()
async def help(ctx):
    embed = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name=';정보 N', value='망가 정보를 불러옵니다.', inline=False)
    embed.add_field(name=';최신', value='최신 망가 10개를 불러옵니다.', inline=False)
    embed.add_field(name=';페이지 N', value='최신 망가 리스트 중 N번째 페이지를 불러옵니다.', inline=False)
    embed.add_field(name=';초대', value='HiyobiBot 초대 링크를 불러옵니다.', inline=False)
    embed.add_field(name=':warning: 경고', value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.\n주의하세요.', inline=False)
    await ctx.send(embed=embed)


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
    if not arg.isdigit():
        await ctx.send('숫자를 입력해주세요.')
        return None

    waitMessage = await ctx.send('정보를 검색하는 중입니다...')

    url = f'https://api.hiyobi.me/gallery/{arg}'
    response = requests.get(url).json()

    if response['title'] == '정보없음':
        embed = discord.Embed(title=':warning: 오류', color=0xff0000)
        embed.set_thumbnail(url=thumbnail)
        embed.add_field(name='검색 결과가 없습니다.', value='번호가 정확한지 다시 한번 확인해주세요.', inline=False)

        await ctx.send(embed=embed)
        return None

    title = response['title']
    artists = [a['display'] for a in response['artists']]
    groups = [g['display'] for g in response['groups']]
    parody = [p['display'] for p in response['parody']]
    characters = [c['display'] for c in response['characters']]
    tags = [t['display'] for t in response['tags']]

    if not artists:
        artists.append('없음')
    if not groups:
        groups.append('없음')
    if not parody:
        parody.append('없음')
    if not characters:
        characters.append('없음')
    if not tags:
        tags.append('없음')

    embed = discord.Embed(title=f'{title}', url=f'https://hiyobi.me/info/{arg}', color=0xff0000)
    embed.set_thumbnail(url=f'http://cdn.hiyobi.me/tn/{arg}.jpg')
    embed.add_field(name='작가', value=", ".join(artists), inline=False)
    embed.add_field(name='그룹', value=", ".join(groups), inline=False)
    embed.add_field(name='원작', value=", ".join(parody), inline=False)
    embed.add_field(name='캐릭터', value=", ".join(characters), inline=False)
    embed.add_field(name='태그', value=", ".join(tags), inline=False)

    await waitMessage.delete()
    await ctx.send(embed=embed)

@bot.command()
async def 최신(ctx):
    waitMessage = await ctx.send('정보를 불러오는 중입니다...')

    data = requests.get(f'https://api.hiyobi.me/list')
    resp = data.json()

    embed = discord.Embed(title=f':scroll: 최신 망가 리스트', url='https://hiyobi.me/', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        title = resp['list'][i]['title']
        id = resp['list'][i]['id']
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists}\n번호 : {id}', inline=False)

    await waitMessage.delete()
    await ctx.send(embed=embed)

@bot.command()
async def 페이지(ctx, page):
    if not page.isdigit():
        await ctx.send('숫자를 입력해주세요.')
        return None

    waitMessage = await ctx.send('정보를 불러오는 중입니다...')

    data = requests.get(f'https://api.hiyobi.me/list/{page}')
    resp = data.json()

    embed = discord.Embed(title=f':scroll: 최신 망가 리스트 - {page}페이지',url=f'https://hiyobi.me/list/{page}', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        title = resp['list'][i]['title']
        id = resp['list'][i]['id']
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists}\n번호 : {id}', inline=False)

    await waitMessage.delete()
    await ctx.send(embed=embed)

'''
@bot.command()
async def 검색(ctx, arg1):
    
    await ctx.send('리스트를 검색하는 중입니다...')
    
    req = requests.get(f'https://hiyobi.me/search/백합')
    con = req.content
    html = BeautifulSoup(con, "html.parser")

    container = html.find("div", {"class":"container"})

    result_list = container.find_all("div", {"class":"sc-jSFkmK jGLdVH row"})

    for i in result_list:
        title_table = i.find("div", {"class":"col-sm-12 col-md-9 p-1 pl-md-4"})
        title = title_table.find("a", {"class":"sc-gKAblj boPkKw"}).text
        print(title)
'''


@bot.command()
async def 초대(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=765557137832542208&scope=bot&permissions=2146954615')
    embed = discord.Embed(title=':inbox_tray: HiyobiBot 초대 링크',url='https://discord.com/oauth2/authorize?client_id=765557137832542208&scope=bot&permissions=2146954615',description='위 링크를 눌러 HiyobiBot을 다른 서버에 초대할 수 있습니다.', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed)


bot.run(os.environ['token'])