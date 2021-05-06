import discord
from discord.ext import commands
import os
from pathlib import Path


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)
thumbnail = 'https://i.imgur.com/GKPAp4q.png'
token = os.environ['token']

cwd = Path(__file__).parents[0]
cwd = str(cwd)
bot.cwd = cwd


@bot.event
async def on_ready():
    print('봇 온라인.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('ㅂ'))


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    await bot.process_commands(message)


if __name__ == '__main__':
    for file in os.listdir(os.path.join(cwd, 'cogs')):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(token)
