# Importamos ABC e abstractmethod do módulo abc.
# ABC significa Abstract Base Class e permite criar classes abstratas.
from abc import ABC, abstractmethod


# Criamos uma classe abstrata chamada Imagem.
# Ela representa a interface que qualquer tipo de imagem deve seguir.
class Imagem(ABC):

    # O decorator abstractmethod indica que toda classe filha
    # deve obrigatoriamente implementar este método.
    @abstractmethod
    def exibir(self) -> None:

        # O método não possui implementação aqui.
        # Ele apenas define que qualquer Imagem deve ser capaz de exibir().
        pass


    # Novamente utilizamos abstractmethod para definir
    # que qualquer imagem deve possuir o método dimensoes().
    @abstractmethod
    def dimensoes(self) -> tuple[int, int]:

        # A implementação concreta será responsabilidade
        # das classes que herdarem de Imagem.
        pass