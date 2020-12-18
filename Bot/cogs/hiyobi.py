from .etc.embeds import Embeds
import discord
from discord.ext import commands
import requests
from .etc.functions import CreateEmbed

CreateEmbed = CreateEmbed()

thumbnail = 'https://i.imgur.com/GKPAp4q.png'


class Hiyobi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        async def 정보(ctx, num):

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

            embed = discord.Embed(
                title=f'{title}', url=f'https://hiyobi.me/info/{num}', color=0xff0000)
            embed.set_thumbnail(url=f'http://cdn.hiyobi.me/tn/{num}.jpg')
            embed.add_field(name='작가', value=", ".join(artists), inline=False)
            embed.add_field(name='그룹', value=", ".join(groups), inline=False)
            embed.add_field(name='원작', value=", ".join(parody), inline=False)
            embed.add_field(name='캐릭터', value=", ".join(
                characters), inline=False)
            embed.add_field(name='태그', value=", ".join(tags), inline=False)

            await waitMessage.edit(embed=embed)

        @bot.command()
        async def 최신(ctx):
            waitMessage = await ctx.send(embed=Embeds.Wait)

            data = requests.get('https://api.hiyobi.me/list')
            resp = data.json()

            embed = discord.Embed(
                title=':scroll: 히요비 최신 리스트', url='https://hiyobi.me/', color=0xff0000)
            embed.set_thumbnail(url=thumbnail)

            for i in range(14):
                iid = resp['list'][i]['id']
                title = resp['list'][i]['title']
                if title == '':
                    title = '없음'
                try:
                    artists = resp['list'][i]['artists'][0]['display']
                except:
                    artists = '없음'

                tags = [t['display'] for t in resp['list'][i]['tags']]
                if not tags:
                    tags.append('없음')
                tag = ', '.join(tags)

                embed.add_field(
                    name=f'{title}', value=f'작가 : {artists} | 번호 : {iid} \n 태그 : {tag}', inline=False)

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

            embed = discord.Embed(title=f':scroll: 히요비 최신 리스트 - {page}페이지', url=f'https://hiyobi.me/list/{page}',
                                  color=0xff0000)
            embed.set_thumbnail(url=thumbnail)

            for i in range(14):
                iid = resp['list'][i]['id']
                title = resp['list'][i]['title']
                if title == '':
                    title = '없음'
                try:
                    artists = resp['list'][i]['artists'][0]['display']
                except:
                    artists = '없음'

                tags = [t['display'] for t in resp['list'][i]['tags']]
                if not tags:
                    tags.append('없음')
                tag = ', '.join(tags)

                embed.add_field(
                    name=f'{title}', value=f'작가 : {artists} | 번호 : {iid} \n 태그 : {tag}', inline=False)

            try:
                await waitMessage.edit(embed=embed)
            except Exception as e:
                await waitMessage.edit(embed=CreateEmbed.Error(e))

        @bot.command()
        async def 검색(ctx, search):
            waitMessage = await ctx.send(embed=Embeds.Wait)

            data = {"search": search, "paging": 1}
            url = 'https://api.hiyobi.me/search'
            resp = requests.post(url=url, json=data).json()

            if resp["count"] != 0:
                embed = discord.Embed(
                    title=':mag: 검색 결과', url=f'https://hiyobi.me/search/{search}', color=0xff0000)
                embed.set_thumbnail(url=thumbnail)

                for i in range(14):
                    iid = resp['list'][i]['id']
                    title = resp['list'][i]['title']
                    if title == '':
                        title = '없음'
                    try:
                        artists = resp['list'][i]['artists'][0]['display']
                    except:
                        artists = '없음'
                    tags = [t['display'] for t in resp['list'][i]['tags']]
                    if not tags:
                        tags.append('없음')
                    tag = ', '.join(tags)

                    embed.add_field(
                        name=f'{title}', value=f'작가 : {artists} | 번호 : {iid} \n 태그 : {tag}', inline=False)
                try:
                    await waitMessage.edit(embed=embed)
                except Exception as e:
                    await waitMessage.edit(embed=CreateEmbed.Error(e))

        @bot.command()
        async def 표지(ctx, num):

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
            if not page.isdigit():
                await ctx.send(embed=Embeds.PlzInputNum)
                return None

            waitMessage = await ctx.send(embed=Embeds.Wait)

            data = requests.get(f'https://cdn.hiyobi.me/json/{num}_list.json')
            resp = data.json()
            page = int(page)
            name = resp[page-1]["name"]

            try:
                img = f'https://cdn.hiyobi.me/data/{num}/{name}'
            except:
                await waitMessage.edit(embed=Embeds.WrongNum)
                return None

            embed = discord.Embed()
            embed.set_image(url=img)

            await waitMessage.edit(embed=embed)


def setup(bot):
    bot.add_cog(Hiyobi(bot))
