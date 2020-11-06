import discord
from discord.ext import commands


class Owner(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        @commands.is_owner()
        async def ck(ctx):
            await ctx.send('ㅇㅇ')


def setup(bot):
    bot.add_cog(Owner(bot))