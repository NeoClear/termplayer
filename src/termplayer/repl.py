from play_list import PlayList

def repl(pl: PlayList):
  while True:
    line = input('termplayer> ')
    if line == 'pause':
      pl.pause()
    elif line == 'play':
      pl.play()
    elif line == 'next':
      pl.playNext()
