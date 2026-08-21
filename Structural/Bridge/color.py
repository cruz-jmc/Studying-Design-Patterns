from abc import ABC, abstractmethod

# one of "Father-classes"
class Color(ABC): # Interface color determinate that all color need to implement fill()

    @abstractmethod
    def fill(self) -> str:
        raise NotImplementedError