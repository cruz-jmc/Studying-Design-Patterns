from player import Target
from video_player import VideoPlayer
# importing the main class(player.py) and the class we want adapt(video_player).


class VideoAdapter(Target):
    def __init__(self, adaptee: VideoPlayer): # the adaptee looks like the Target from player.
        self.adaptee = adaptee # doing this, the class "media_player" from player will accept video.

    def play(self):
        self.adaptee.play_mp4() # do the same but now in mp4, the "translation".