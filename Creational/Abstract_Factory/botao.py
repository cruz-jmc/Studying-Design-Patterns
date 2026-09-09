# Importa ABC e abstractmethod do módulo abc.
# ABC permite criar uma classe abstrata.
# abstractmethod permite declarar métodos abstratos.
from abc import ABC, abstractmethod


# Declara a classe abstrata Botao.
# ABC indica que essa classe participa da estrutura de abstração.
class Botao(ABC):

    # Declara o método abstrato renderizar.
    # Toda classe concreta que herdar de Botao deverá implementá-lo.
    @abstractmethod
    def renderizar(self) -> str:

        # O método não possui implementação concreta.
        # A implementação será responsabilidade das subclasses.
        pass