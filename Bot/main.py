import discord
from discord.ext import commands
import requests
from Bot.etc import Embeds
from Bot.etc import CreateEmbed
import json
import os


bot = commands.Bot(command_prefix=';')
thumbnail = 'https://i.imgur.com/GKPAp4q.png'
bot.remove_command('help')

BASEURL = "https://api.koreanbots.dev"
token = os.environ['dbltoken']
serverCount = 21


@bot.event
async def on_ready():
    response = requests.post(f'{BASEURL}/bots/servers', headers={"token":token, "Content-Type": "application/json"}, json={"servers": serverCount})
    print('봇 온라인.')
    print(response.json())
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';명령어 | ombe#7777'))


@bot.command()
async def help(ctx):
    await ctx.send(embed=Embeds.Help)


@bot.command()
async def 도움말(ctx):
    await ctx.send(embed=Embeds.Help)


@bot.command()
async def 명령어(ctx):
    await ctx.send(embed=Embeds.Help)


@bot.command()
async def 정보(ctx, num):
    if not num.isdigit():
        await ctx.send(embed=Embeds.PlzInputNum)
        return None

    waitMessage = await ctx.send(embed=Embeds.Wait)

    url = f'https://api.hiyobi.me/gallery/{num}'
    response = requests.get(url).json()

    if response['title'] == '정보없음':
        await waitMessage.edit(embed=Embeds.NoResult)
        return None

    title = response['title']
    artists = [a['display'] for a in response['artists']]
    groups = [g['display'] for g in response['groups']]
    parody = [p['display'] for p in response['parodys']]
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

    embed = discord.Embed(title=f'{title}', url=f'https://hiyobi.me/info/{num}', color=0xff0000)
    embed.set_thumbnail(url=f'http://cdn.hiyobi.me/tn/{num}.jpg')
    embed.add_field(name='작가', value=", ".join(artists), inline=False)
    embed.add_field(name='그룹', value=", ".join(groups), inline=False)
    embed.add_field(name='원작', value=", ".join(parody), inline=False)
    embed.add_field(name='캐릭터', value=", ".join(characters), inline=False)
    embed.add_field(name='태그', value=", ".join(tags), inline=False)

    await waitMessage.edit(embed=embed)


@bot.command()
async def 최신(ctx):
    waitMessage = await ctx.send(embed=Embeds.Wait)

    data = requests.get('https://api.hiyobi.me/list')
    resp = data.json()

    embed = discord.Embed(title=':scroll: 히요비 최신 리스트', url='https://hiyobi.me/', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        id = resp['list'][i]['id']
        title = resp['list'][i]['title']
        if title == '':
            title = '없음'
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists} | 번호 : {id}', inline=False)

    try:
        await waitMessage.edit(embed=embed)
    except Exception as e:
        await waitMessage.edit(embed=CreateEmbed.Error(e))


@bot.command()
async def 페이지(ctx, page):
    if not page.isdigit():
        await ctx.send(embed=Embeds.PlzInputNum)
        return None

    waitMessage = await ctx.send(embed=Embeds.Wait)

    data = requests.get(f'https://api.hiyobi.me/list/{page}')
    resp = data.json()

    embed = discord.Embed(title=f':scroll: 히요비 최신 리스트 - {page}페이지', url=f'https://hiyobi.me/list/{page}', color=0xff0000)
    embed.set_thumbnail(url=thumbnail)

    for i in range(9):
        id = resp['list'][i]['id']
        title = resp['list'][i]['title']
        if title == '':
            title = '없음'
        try:
            artists = resp['list'][i]['artists'][0]['display']
        except:
            artists = '없음'

        embed.add_field(name=f'{title}', value=f'작가 : {artists} | 번호 : {id}', inline=False)

    try:
        await waitMessage.edit(embed=embed)
    except Exception as e:
        await waitMessage.edit(embed=CreateEmbed.Error(e))


@bot.command()
async def 검색(ctx, *tag):
    waitMessage = await ctx.send(embed=Embeds.NotReady)


@bot.command()
async def 표지(ctx, num):
    if not num.isdigit():
        await ctx.send(embed=Embeds.PlzInputNum)
        return None

    waitMessage = await ctx.send(embed=Embeds.Wait)

    url = f'https://api.hiyobi.me/gallery/{num}'
    response = requests.get(url).json()

    if response['title'] == '정보없음':
        await waitMessage.edit(embed=Embeds.NoResult)
        return None

    embed = discord.Embed()
    embed.set_image(url=f'http://cdn.hiyobi.me/tn/{num}.jpg')

    try:
        await waitMessage.edit(embed=embed)
    except Exception as e:
        await waitMessage.edit(embed=CreateEmbed.Error(e))


@bot.command()
async def 보기(ctx, num, page):
    if not num.isdigit() or not page.isdigit():
        await ctx.send(embed=Embeds.PlzInputNum)
        return None

    waitMessage = await ctx.send(embed=Embeds.Wait)

    data = requests.get(f'https://cdn.hiyobi.me/data/json/{str(num)}_list.json')
    resp = data.json()

    try:
        img = f'https://cdn.hiyobi.me/data/{num}/{resp[int(page)]["name"]}'
    except:
        await waitMessage.edit(embed=Embeds.WrongNum)
        return None

    embed = discord.Embed()
    embed.set_image(url=img)

    await waitMessage.edit(embed=embed)



@bot.command()
async def 초대(ctx):
    await ctx.send(embed=Embeds.Invite)


@bot.command()
async def 지원(ctx):
    await ctx.send(embed=Embeds.Support)


bot.run(os.environ['token'])