import logging
from os import listdir
from pretty_help import PrettyHelp
from discord.ext import commands
from ark.settings import __version__, DRAGON_IMG

loaded_cogs = 0
client = commands.Bot(command_prefix='x:',help_command=PrettyHelp(),description="SpaceX information gatherer bot. Shows information collected from SpaceX company, missions, rockets and more.")
log = logging.getLogger(__name__)



# Scan for files in ./core/cogs
for file in listdir("./core/cogs/"):
	if not file.endswith(".py"):
				continue
	f = file.replace(".py", "")
	try:
            #load cog
            client.load_extension(f"core.cogs.{f}")
          
            log.info(f"Loaded cog: ${f.title()}!")
           
            loaded_cogs += 1
	except Exception as error:
            # if error has ocurred loading a cog.
		    log.error(f"Has ocurred a error loading cog: {f.title()}! Error: {error}")

@client.event
async def on_ready():
    log.info(f"🚀 -> Loaded {loaded_cogs} Cogs!")
    log.info('In orbit!')