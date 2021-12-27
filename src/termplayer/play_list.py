from cache import Cache
import pafy
from typing import List
from random import randrange
from player import Player

class PlayList:
  def __init__(self, urls: List[str]):
    self.cache = Cache(pafy.new)
    self.urls = urls
    assert len(urls) > 0
    self.idx = 0

    # Default next function to loop
    self.next = self.loop

    self.modeMapping = {
      'repeat': self.repeat,
      'loop': self.loop,
      'random': self.random
    }

    self.player = Player()

  def repeat(self):
    return self.idx
  
  def loop(self):
    idx = self.idx
    self.idx += 1
    print(self.idx)
    if self.idx >= len(self.urls):
      self.idx = 0
    return idx

  def random(self):
    idx = self.idx
    self.idx = randrange(0, len(urls))
    return idx

  def setMode(self, mode: str):
    if mode in self.modeMapping:
      self.next = self.modeMapping[mode]

  def playNext(self):
    self.player.setAudio(self.cache.get(self.urls[self.next()]).getbestaudio().url, lambda e: self.playNext())
    self.player.play()
  
  def pause(self):
    self.player.pause()

  def play(self):
    self.player.play()
