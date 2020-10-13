import discord
import requests
import os

client = discord.Client()
prefix = ';'
thumbnail = 'https://i.imgur.com/GKPAp4q.png'

class HiyobiBot(discord.Client):
    async def on_ready(self):
        print('히요비봇 온라인.')
        game = discord.Game(';help')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        channel = message.channel

        if message.author.bot:
            return None

        if message.content == prefix+'help':
            embed = discord.Embed(title=':ticket: HiyobiBot 도움말', color=0xababab)
            embed.set_thumbnail(url=thumbnail)
            embed.add_field(name=' - ' + prefix + '정보 [N]', value='망가 정보를 불러옵니다.', inline=True)

            await channel.send(embed=embed)
            return None
        elif message.content.startswith(prefix):
            await channel.send('이해할 수 없는 명령어입니다.')
            return None

if __name__ == '__main__':
    client = HiyobiBot()
    client.run(os.environ['token'])