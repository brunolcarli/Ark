import discord
from discord.ext.commands.core import command
from core.api_requests import get_company, get_histories, get_history
from discord.ext import commands
from discord.ext.commands.context import Context
from ark.settings import __version__, DRAGON_IMG
class Misc(commands.Cog): 
 def __init__(self, bot):
        self.bot = bot
        self.description = "Miscellaneous commands."
  
 @commands.command()
 async def histories(self,ctx):
    """
    List SpaceX launch histories.
    """
    
    data = get_histories()
    if not data.get('data'):
        return await ctx.send('Oops, something wrong happened...')

    histories = data['data'].get('histories', {})
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    for history in histories:
        event_date_utc = history.get('event_date_utc')
        embed.add_field(
            name=f'ID: {history.get("id")} - {history.get("title")}',
            value=f'Event date (UTC): {event_date_utc}',
            inline=True
        )

    return await ctx.send(':rocket: Showing SpaceX launch histories!', embed=embed)

 @commands.command()
 async def history(ctx, id=None):
    """
    Shows a event history based on its ID.
    Usage example:
        x:history 3
    """
    if not id:
        return await ctx.send('Must specify a history ID!')

    data = get_history(id)
    if not data.get('data'):
        return await ctx.send('Oops, something wrong happened...')

    history = data['data'].get('history', {})
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    details = history.get('details')
    event_date = history.get('event_date_utc')
    title = history.get('title')

    embed.add_field(name='Event date (UTC)', value=event_date, inline=True)

    # links
    links = history.get('links')
    if links:
        article = links.get('article')
        embed.add_field(name='Article', value=article, inline=False)

    # flight
    flight = history.get('flight')
    if flight:
        flight_details = flight.get('details')
        is_tentative = flight.get('is_tentative')
        launch_success = flight.get('launch_success')
        launch_year = flight.get('launch_year')
        mission_name = flight.get('mission_name')

        embed.add_field(name='Mission name', value=mission_name, inline=True)
        embed.add_field(name='Tentative launch', value='Yes' if is_tentative else 'No', inline=True)
        embed.add_field(name='Launch success', value='Yes' if launch_success else 'No', inline=True)
        embed.add_field(name='Launch year', value=launch_year, inline=True)
        embed.add_field(name='Flight details', value=flight_details, inline=True)

        # site
        site = flight.get('launch_site')
        if site:
            site_name_long = site.get('site_name_long')
            embed.add_field(name='Launch site', value=site_name_long, inline=False)

        # video
        if flight.get('links'):
            video = flight['links'].get('video_link')
            embed.add_field(name='Video', value=video, inline=False)

        # rocket
        rocket = flight.get('rocket')
        if rocket:
            rocket_name = rocket.get('rocket_name')
            rocket_type = rocket.get('rocket_type')
            embed.add_field(
                name='Rocket',
                value=f'Name: {rocket_name} - Type: {rocket_type}',
                inline=False
            )

    embed.add_field(name='Details', value=details, inline=False)

    return await ctx.send(title, embed=embed)


 @commands.command()
 async def company(ctx):
    """
    Get SpaceX company information.
    """
    data = get_company()
    if not data.get('data'):
        return await ctx.send('Oops, something wrong happened...')
    
    company = data['data'].get('company', {})
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    embed.add_field(name='CEO', value=company.get('ceo'), inline=True)
    embed.add_field(name='COO', value=company.get('coo'), inline=True)
    embed.add_field(name='CTO propulsion', value=company.get('cto_propulsion'), inline=True)
    embed.add_field(name='CTO', value=company.get('cto'), inline=True)
    embed.add_field(name='Employees count', value=company.get('employees'), inline=True)
    embed.add_field(name='Foundig year', value=company.get('founded'), inline=True)
    embed.add_field(name='Founder', value=company.get('founder'), inline=True)
    embed.add_field(name='Launch sites', value=company.get('launch_sites'), inline=True)
    embed.add_field(name='Summary', value=company.get('summary'), inline=False)

    return await ctx.send(f':rocket: {company.get("name")}!', embed=embed)


def setup(bot):
    bot.add_cog(Misc(bot))