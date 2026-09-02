# Importa a classe ABC, utilizada para criar classes abstratas,
# e o decorator abstractmethod, utilizado para declarar métodos abstratos.
from abc import ABC, abstractmethod


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
        ...


    # Indica que todas as classes concretas devem implementar
    # uma operação para contar arquivos.
    @abstractmethod
    def contar_arquivos(self) -> int:
        ...


    # Indica que todas as classes concretas devem implementar
    # uma operação para listar sua estrutura.
    # O parâmetro nivel representa a profundidade atual na árvore.
    @abstractmethod
    def listar(self, nivel: int = 0) -> None:
        ...