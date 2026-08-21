from abc import ABC, abstractmethod
# import a native Python Library to create abstract classes and abstract methods.


class Target(ABC): # Interface between user and the program.
    @abstractmethod
    def play(self):
        pass


class AudioPlayer(Target): # Concret Target implementation 
    def play(self):
        print("Reproduzindo áudio")


class MediaPlayer:
    def __init__(self, player: Target): # Builder
        self.player = player

    def execute(self): # Execute any type of object whereas it has the "play()" method.
        self.player.play()