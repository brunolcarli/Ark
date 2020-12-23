import logging
import sys
from ark.settings import TOKEN, __version__
from core.commands import client

logging.basicConfig(level='INFO')
log = logging.getLogger()

if __name__ == '__main__':
    log.info(
        r'''
     _    ____  _  __
    / \  |  _ \| |/ /
   / _ \ | |_) | ' / 
  / ___ \|  _ <| . \ 
 /_/   \_\_| \_\_|\_\      
                    
        '''
    )
    log.info('Running ARK version: %s\n', __version__)

    client.run(TOKEN)
