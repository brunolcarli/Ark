from decouple import config

__version__ = '0.2.1'


class Config:
    ENV_REF = config('ENV_REF', 'development')

    TOKEN = config('TOKEN', 'bot_token')
    BOT_PREFIX = config('BOT_PREFIX', 'x:')
    DRAGON_IMG = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/COTS2Dragon.6.jpg/800px-COTS2Dragon.6.jpg'
    DESCRIPTION= '''
    SpaceX information gatherer bot.
    Shows information collected from SpaceX company, missions, rockets and more.
    '''
