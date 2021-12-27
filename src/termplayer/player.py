import vlc, pafy
import time
import threading

class Player:
  def __init__(self):
    self.instance = vlc.Instance()
    self.instance.log_unset()
    self.player = self.instance.media_player_new()
    # self.mediaResource = pafy.new(url.strip())
    # self.player = vlc.MediaPlayer(self.mediaResource.getbestaudio().url)
    # self.eventManager = self.player.event_manager()
    # self.audioFinished = threading.Condition()
    # self.finished = False

    # self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, self.finish)
    # self.eventManager.event_attach(vlc.EventType.MediaPlayerEncounteredError, self.finish)
  
  def setAudio(self, url: str, onFinish):
    # if self.player is not None:
    #   self.player.stop()
    #   del self.player
    self.player.set_mrl(url)

    # self.player = vlc.MediaPlayer(url)
    self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, onFinish)
    self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEncounteredError, onFinish)

  def play(self):
    if self.player != None:
      self.player.play()
  
  def pause(self):
    if self.player != None:
      self.player.pause()
  
  def stop(self):
    if self.player != None:
      self.player.stop()
