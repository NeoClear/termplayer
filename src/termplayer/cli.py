import random
import click
import os
from logger import log
from play_list import PlayList
from repl import repl

import pafy

@click.command()
@click.option('--playlist', default='~/.trm', help='Playlist location')
def cli(playlist):
  try:
    with open(os.path.expanduser(playlist), 'r') as playListFile:
      urls = list(map(lambda s: s.strip(), playListFile.readlines()))
      log('Playlist loaded')

      playList = PlayList(urls)
      playList.playNext()
      repl(playList)
      
  except IOError as e:
    print(f'Unable to open playlist file \'{playlist}\'')
