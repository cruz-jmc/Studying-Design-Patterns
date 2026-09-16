# Importa o ABC, que permite criar uma classe abstrata.
from abc import ABC, abstractmethod


# Declara a interface Botao.
class Botao(ABC):

    @abstractmethod
    def desenhar(self):
        pass