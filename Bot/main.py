import discord
from discord.ext import commands
import requests
import os
from pathlib import Path
import sqlite3


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)
thumbnail = 'https://i.imgur.com/GKPAp4q.png'
token = os.environ['token']

BASEURL = "https://api.koreanbots.dev"
dblToken = os.environ['dbltoken']
serverCount = 62

cwd = Path(__file__).parents[0]
cwd = str(cwd)
bot.cwd = cwd


conn = sqlite3.connect("")


@bot.event
async def on_ready():
    requests.post(f'{BASEURL}/bots/servers', headers={"token": dblToken,
                                                      "Content-Type": "application/json"}, json={"servers": serverCount})
    print('봇 온라인.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';명령어 | ombe#7777'))


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    await bot.process_commands(message)


if __name__ == '__main__':
    for file in os.listdir(cwd+'/cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(token)
