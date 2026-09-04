# Importa a classe ABC, utilizada para criar classes abstratas,
# e o decorator abstractmethod, utilizado para declarar métodos abstratos.
from abc import ABC, abstractmethod

# Importa annotations do futuro.
# Isso permite utilizar referências de tipos que ainda estão sendo definidos.
from __future__ import annotations # -> isso é para o método "buscar", veja lá embaixo.


# Define a classe abstrata ItemDoAcervo.
# ABC significa Abstract Base Class.
# Esta classe representa qualquer item existente no acervo.
class ItemDoAcervo(ABC):

    # Define o construtor da classe.
    # Todo item do acervo deve possuir um nome.
    def __init__(self, nome: str):

        # Armazena o nome recebido no atributo nome do objeto.
        self.nome = nome


    # Indica que todas as classes concretas devem implementar
    # uma operação para calcular ou retornar seu tamanho.
    @abstractmethod
    def tamanho(self) -> float:
        pass


    # Indica que todas as classes concretas devem implementar
    # uma operação para contar arquivos.
    @abstractmethod
    def contar_arquivos(self) -> int:
        pass


    # Indica que todas as classes concretas devem implementar
    # uma operação para listar sua estrutura.
    # O parâmetro nivel representa a profundidade atual na árvore.
    @abstractmethod
    def listar(self, nivel: int = 0) -> None:
        pass

    @abstractmethod
    def caminho(self, nome: str) -> str | None:
        pass

    @abstractmethod
    def buscar(self, nome: str) -> ItemDoAcervo | None:
        pass