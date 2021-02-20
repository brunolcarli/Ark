from discord.ext import commands
import discord
from discord.ext.commands.context import Context
from core.api_requests import APIRequest
from ark.settings import __version__, Config


class InfoOfCapsules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Information of capsule(s) commands."


    @commands.command(pass_context=True) 
    async def capsule(self,ctx:Context, id=None):
        """
        Get data from a specific capsule by ID.
        usage example:
            x:capsule C101
        """
        if not id:
            return await ctx.send('Must specify a capsule ID!')
        
        data = APIRequest.get_capsule(id)
        if not data.get('data'):
            return await ctx.send('Oops, something wrong happened...')

        capsule = data['data'].get('capsule', {})
        embed = discord.Embed(color=0x1E1E1E, type='rich')
        embed.set_thumbnail(url=config.DRAGON_IMG)

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


    @commands.command(pass_context=True)
    async def capsules(self,ctx):
        """
        Lists SpaceX capsules.
        """
        data = APIRequest.get_capsules()
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


def setup(bot):
    bot.add_cog(InfoOfCapsules(bot))
