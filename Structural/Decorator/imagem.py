# Importa ABC, que permite criar classes abstratas.
# Importa abstractmethod, que permite declarar métodos obrigatórios.
from abc import ABC, abstractmethod


# Declara a classe abstrata Imagem.
# ABC significa Abstract Base Class.
class Imagem(ABC):

    # Declara que toda classe que implementar Imagem
    # deverá possuir um método chamado exibir().
    @abstractmethod
    def exibir(self) -> None:
        # pass indica que esta classe não possui uma implementação concreta.
        # A responsabilidade de implementar este método será das subclasses.
        pass


    # Declara que toda classe que implementar Imagem
    # também deverá informar suas dimensões.
    @abstractmethod
    def dimensoes(self) -> tuple[int, int]:
        # Assim como no método exibir(), a implementação
        # será responsabilidade das subclasses.
        pass