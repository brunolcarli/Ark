import logging
import sys
from ark.settings import Config, __version__
from core.commands import client
from core.keep_alive import keep_alive

logging.basicConfig(level='INFO')
log = logging.getLogger()


if __name__ == '__main__':
    log.info(
        r'''
       ^
      / \
     /___\
    |=   =|
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
   /|##!##|\
  / |##!##| \
 /  |##!##|  \
|  / ^ | ^ \  |
| /  ( | )  \ |
|/   ( | )   \|
    ((   ))
   ((  :  ))
   ((  :  ))
    ((   ))
     (( ))
      ( )
       .
       .
       .
     _    ____  _  __
    / \  |  _ \| |/ /
   / _ \ | |_) | ' / 
  / ___ \|  _ <| . \ 
 /_/   \_\_| \_\_|\_\                          
        '''
    )
    log.info('Running ARK version: %s\n', __version__)

    if Config.ENV_REF == 'replit':
        keep_alive()

    client.run(Config.TOKEN)
