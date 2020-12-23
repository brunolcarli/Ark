import logging
import discord
from discord.ext import commands, tasks
from ark.settings import __version__

client = commands.Bot(command_prefix='x:')


@client.event
async def on_ready():
    log.info('In orbit!')


@client.command(aliases=['v'])
async def version(ctx):
    return await ctx.send(__version__)