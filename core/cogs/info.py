from discord.ext import commands
from discord.ext.commands.context import Context
from ark.settings import __version__


class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "BotInfo Commands"

    @commands.command(aliases=['v'],pass_context=True)
    async def version(self,ctx:Context):
        return await ctx.send(__version__)


def setup(bot):
    bot.add_cog(Botinfo(bot))