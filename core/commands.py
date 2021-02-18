import logging
import discord
from discord.ext import commands, tasks
from ark.settings import __version__, DRAGON_IMG
from core.api_requests import (get_capsules, get_capsule, get_company, get_histories,
                               get_history, get_missions, get_mission, get_rockets, get_rocket)


client = commands.Bot(command_prefix='x:')
log = logging.getLogger(__name__)


@client.event
async def on_ready():
    log.info('In orbit!')


@client.command(aliases=['v'])
async def version(ctx):
    return await ctx.send(__version__)


@client.command()
async def capsules(ctx):
    """
    Lists SpaceX capsules.
    """
    data = get_capsules()
    if not data.get('data'):
        return ctx.send('Oops, something wrong happened...')

    capsules = data['data'].get('capsules', [])
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    for capsule in capsules:
        landings = capsule.get('landings')
        reuse = capsule.get('reuse_count')
        status = capsule.get('status')
        capsule_type = capsule.get('type')

        body = f'Landings: {landings} | Reuse count: {reuse} | ' \
               f'Status: {status} | Type: {capsule_type}'
        embed.add_field(
            name=f'ID: {capsule.get("id")}',
            value=body,
            inline=True
        )

    return await ctx.send(':rocket: Showing capsules info!', embed=embed)


@client.command()
async def capsule(ctx, id=None):
    """
    Get data from a specific capsule by ID.
    usage example:
        x:capsule C101
    """
    if not id:
        return await ctx.send('Must specify a capsule ID!')

    data = get_capsule(id)
    if not data.get('data'):
        return await ctx.send('Oops, something wrong happened...')

    capsule = data['data'].get('capsule', {})
    embed = discord.Embed(color=0x1E1E1E, type='rich')
    embed.set_thumbnail(url=DRAGON_IMG)

    # get variable names from API response
    landings = capsule.get('landings')
    original_launch = capsule.get('original_launch')
    reuse_count = capsule.get('reuse_count')
    status = capsule.get('status')
    capsule_type = capsule.get('type')

    embed.add_field(name=':airplane_arriving: Landings', value=landings, inline=True)
    embed.add_field(name=':airplane_departure: Original Launch', value=original_launch, inline=True)
    embed.add_field(name=':recycle: Reuse count', value=reuse_count, inline=True)
    embed.add_field(name=':exclamation: Status', value=status, inline=True)
    embed.add_field(name=':mag: Type', value=capsule_type, inline=True)

    # missions data
    missions = capsule.get('missions', [])
    if missions:
        missions_info = ''
        for mission in missions:
            missions_info += f'Name: {mission.get("name")} Flight: {mission.get("flight")}\n'
        embed.add_field(
            name=':tickets: Missions :tickets:',
            value=missions_info,
            inline=False
        )

    # dragon data
    dragon = capsule.get('dragon')
    if dragon:
        active = dragon.get('active')
        crew_capacity = dragon.get('crew_capacity')
        description = dragon.get('description')
        dry_mass_kg = dragon.get('dry_mass_kg')
        first_flight = dragon.get('first_flight')
        name = dragon.get('name')
        orbit_duration_yr = dragon.get('orbit_duration_yr')
        sidewall_angle_deg = dragon.get('sidewall_angle_deg')

        # diameter
        diameter_feet = dragon['diameter'].get('feet')
        diameter_meter = dragon['diameter'].get('meters')

        # heat shield
        heat_shield_dev_partner = dragon['heat_shield'].get('dev_partner')
        heat_shield_material = dragon['heat_shield'].get('material')
        heat_shield_size_meters = dragon['heat_shield'].get('size_meters')
        heat_shield_temp_degrees = dragon['heat_shield'].get('temp_degrees')

        heat_shield = f'Partner: {heat_shield_dev_partner} | Material: {heat_shield_material} | ' \
                      f'Size: {heat_shield_size_meters}mt - {heat_shield_temp_degrees}dg'

        # thrusters
        thrusters = dragon.get('thrusters', [])
        if thrusters:
            thrusters_info = ''
        for thruster in thrusters:
            amount = thruster.get('amount')
            fuel_1 = thruster.get('fuel_1')
            fuel_2 = thruster.get('fuel_2')
            pods = thruster.get('pods')
            thruster_type = thruster.get('type')

            thrusters_info += f'Amount: {amount} | Fuels: {fuel_1} - {fuel_2} | ' \
                              f'Pods: {pods} | type: {thruster_type}\n'

        embed.add_field(
            name=':boom: Thrusters :boom:',
            value=thrusters_info,
            inline=False
        )
        embed.add_field(name='Thruster name', value=name, inline=True)
        embed.add_field(name='Active', value=active, inline=True)
        embed.add_field(name='Crew Capacity', value=crew_capacity, inline=True)
        embed.add_field(name='Dry mass Kg', value=dry_mass_kg, inline=True)
        embed.add_field(name='First flight', value=first_flight, inline=True)
        embed.add_field(name='Orbit duration years', value=orbit_duration_yr, inline=True)
        embed.add_field(name='Sidewall angle', value=sidewall_angle_deg, inline=True)
        embed.add_field(name='Diameter', value=f'{diameter_feet}ft | {diameter_meter}mt', inline=True)
        embed.add_field(name='Heat Shield', value=heat_shield, inline=True)

        embed.add_field(name='Description', value=description, inline=False)

    return await ctx.send(':rocket: Showing capsule info!', embed=embed)


@client.command()
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


@client.command()
async def histories(ctx):
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



@client.command()
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
@client.command()
async def rockets(ctx):
    """
    Show Rockets and their id
    """

    data = get_rockets()
    embed = discord.Embed(type='rich')

    rockets = data['data'].get('rockets', {})
    for i in rockets:
        embed.add_field(name=f'ID: {i.get("id")} ', value=f'**Name: {str(i.get("id"))}**', inline=True)

    await ctx.send("Rocket ids",embed=embed)
@client.command()
async def rocket(ctx, id=None):
    """
    Show detailed information about a single rocket based on it ID
    """
    if not id:
        await ctx.send('must specify an id')
    data = get_rocket(id)
    rocket = data["data"].get('rocket', {})
    embed = discord.Embed(type="rich")
    if not rocket:
       await ctx.send('Ops... Something wrong happened')

    embed.add_field(name='Active', value=rocket.get('active'), inline=True)
    embed.add_field(name='company', value=rocket.get('company'), inline=True)
    embed.add_field(name='Country', value=rocket.get('country'), inline=True)
    embed.add_field(name='Description', value=rocket.get('description'), inline=True)
    embed.add_field(name="Cost Per launch", value=rocket.get('cost_per_launch'), inline=True)
    embed.add_field(name='Sucess Rate', value=rocket.get('success_rate_pct'), inline=True)
    embed.add_field(name='height in Meters', value=rocket['height'].get('meters'), inline=True)
    embed.add_field(name='Height in feet', value=rocket['height'].get('feet'), inline=True)

    await ctx.send(embed=embed)

@client.command()
async def missions(ctx):
    """
    Lists all missions.
    """
    data = get_missions()

    if not data.get('data'):
        return ctx.send('Oops, something wrong happened...')

    missions = data['data'].get('missions', [])
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    for mission in missions:
        name = mission.get('name')

        body = f'Name: {name}'
        embed.add_field(
            name=f'ID: {mission.get("id")}',
            value=body,
            inline=True
        )

    return await ctx.send(':rocket: Showing missions!', embed=embed)

@client.command()
async def mission(ctx, id=None):
    """
    Get data from a specific Mission by ID.
    usage example:
        x:mission 9D1B7E0
    """
    data = get_mission(id)

    if not id:
        return await ctx.send('Must specify a mission ID!')

    if not data.get('data'):
        return await ctx.send('Oops, something wrong happened...')

    mission = data['data'].get('mission', {})
    embed = discord.Embed(color=0x1E1E1E, type='rich')

    name = mission.get('name')
    id = mission.get('id')
    website = f'[Go to the website]({mission.get("website")})'
    manufacturers = mission.get('manufacturers')
    description = mission.get('description')

    embed.add_field(name=':satellite_orbital: Name', value=name, inline=True)
    embed.add_field(name=':id: Id', value=id, inline=True)
    embed.add_field(name=':exclamation: Manufacturer', value=manufacturers[len(manufacturers)-1],
                    inline=True)
    embed.add_field(name=':link: Website', value=website, inline=True)
    embed.add_field(name='Description', value=description, inline=False)

    return await ctx.send(':rocket: Showing mission info!', embed=embed)
