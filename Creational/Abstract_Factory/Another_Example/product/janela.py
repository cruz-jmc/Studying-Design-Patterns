# Importa ABC e abstractmethod para criar uma classe abstrata.
from abc import ABC, abstractmethod


# Declara a interface Janela.
class Janela(ABC):

    # Aqui funciona de forma parecida com a interface botao.
    @abstractmethod
    def exibir(self):
        pass