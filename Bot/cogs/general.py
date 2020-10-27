from .etc.embeds import Embeds
from discord.ext import commands


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        bot.remove_command('help')

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
        async def 초대(ctx):
            await ctx.send(embed=Embeds.Invite)

        @bot.command()
        async def 지원(ctx):
            await ctx.send(embed=Embeds.Support)


def setup(bot):
    bot.add_cog(General(bot))