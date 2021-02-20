from core.api_requests import get_rockets,get_rocket
from discord.ext import commands
from discord.ext.commands.context import Context
import discord
class InfoOfRockets(commands.Cog):
   def __init__(self, bot):
        self.bot = bot
        self.description = "Information of Rocket(s) Commands"
   @commands.command()
   async def rocket(self,ctx, id=None):
    """
    Show detailed information about a single rocket based on it ID
    """
    if not id:
        await ctx.send('must specify an id')
        return
    data = get_rocket(id)
    rocket = data["data"].get('rocket', {})
    embed = discord.Embed(type="rich")
    if not rocket:
       await ctx.send('Ops... Something wrong happened')
       return
    embed.add_field(name='Active', value=rocket.get('active'), inline=True)
    embed.add_field(name='company', value=rocket.get('company'), inline=True)
    embed.add_field(name='Country', value=rocket.get('country'), inline=True)
    embed.add_field(name='Description', value=rocket.get('description'), inline=True)
    embed.add_field(name="Cost Per launch", value=rocket.get('cost_per_launch'), inline=True)
    embed.add_field(name='Sucess Rate', value=rocket.get('success_rate_pct'), inline=True)
    embed.add_field(name='height in Meters', value=rocket['height'].get('meters'), inline=True)
    embed.add_field(name='Height in feet', value=rocket['height'].get('feet'), inline=True)

    await ctx.send(embed=embed)

   @commands.command()
   async def rockets(self,ctx):
    """
    Show Rockets and their id
    """

    data = get_rockets()
    embed = discord.Embed(type='rich')

    rockets = data['data'].get('rockets', {})
    for i in rockets:
        embed.add_field(name=f'ID: {i.get("id")} ', value=f'**Name: {str(i.get("id"))}**', inline=True)

    await ctx.send("Rocket ids",embed=embed)
def setup(bot):
    bot.add_cog(InfoOfRockets(bot))