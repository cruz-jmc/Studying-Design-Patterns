from abc import ABC, abstractmethod
from color import Color


class Shape(ABC): # Another Father-class, but this is a abstraction

    def __init__(self, color: Color): # gives a color to some shape (the "Bridge" joke, it's literally a Bridge between 2 main classes)
        self.color = color # -> this is a builder

    @abstractmethod
    def draw(self):
        raise NotImplementedError