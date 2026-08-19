from player import MediaPlayer
from player import AudioPlayer
from video_adapter import VideoAdapter
from video_player import VideoPlayer


MediaPlayer(AudioPlayer()).execute()

MediaPlayer(VideoAdapter(VideoPlayer())).execute()


-------------------------

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def play(self):
        raise NotImplementedError


class AudioPlayer(Target):
    def play(self):
        print("Reproduzindo áudio")


class MediaPlayer:
    def __init__(self, player: Target):
        self.player = player

    def execute(self):
        self.player.play()

# MediaPlayer(AudioPlayer()).execute()


-----------------------------

from player import Target


class VideoAdapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def play(self):
        self.adaptee.play_mp4()

-----------------------------------

class VideoPlayer:
    def play_mp4(self):
        print("Reproduzindo vídeo MP4")

# VideoPlayer().play_mp4()