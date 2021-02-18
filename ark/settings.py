from decouple import config


__version__ = '0.1.0'

TOKEN = config('TOKEN', 'bot_token')

DRAGON_IMG = 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/COTS2Dragon.6.jpg/800px-COTS2Dragon.6.jpg'
ENV_REF = config('ENV_REF', 'development')
