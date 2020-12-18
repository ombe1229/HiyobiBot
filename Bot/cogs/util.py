from discord.ext import commands
from .etc.embeds import Embeds
from .etc.functions import CreateEmbed

CreateEmbed = CreateEmbed()


class Util(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        @bot.command()
        @commands.has_permissions(manage_messages=True)
        async def 청소(ctx, num):
            if int(num) < 1 or not num.isdigit():
                await ctx.send(embed=Embeds.HowtoClear)
                return
            num = int(num)+1
            await ctx.channel.purge(limit=num)
            await ctx.send(embed=CreateEmbed.Cleared(num-1))


def setup(bot):
    bot.add_cog(Util(bot))
