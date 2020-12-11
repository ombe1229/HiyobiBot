from discord.ext import commands
from .etc.embeds import Embeds


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        async def 청소(ctx, *num):
            await ctx.send(embed=Embeds.NotReady)


def setup(bot):
    bot.add_cog(Util(bot))
