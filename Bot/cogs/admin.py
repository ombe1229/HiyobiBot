from discord.ext import commands


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


''' @bot.command()
    @commands.is_owner()
    def printJson(ctx, url):
        await ctx.send(requests.get(url).json())'''


def setup(bot):
    bot.add_cog(Admin(bot))
