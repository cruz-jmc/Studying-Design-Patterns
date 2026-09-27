# abstractmethod permite declarar métodos que as subclasses deverão implementar.
from abc import ABC, abstractmethod


# Declara a classe Prototype,ela herda de ABC porque será uma classe abstrata(interface).
class Prototype(ABC):

    # Declara o método clone como abstrato. Isso significa que as classes concretas deverão implementar esse método.
    @abstractmethod
    def clone(self):
        pass