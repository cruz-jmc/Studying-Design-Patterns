# Importa a classe ABC, que permite criar uma classe abstrata.
from abc import ABC, abstractmethod


# Declara a classe Arquivo como uma classe abstrata.
class Arquivo(ABC):

    # Define o construtor da classe Arquivo.
    def __init__(self, destino: str):

        # Guarda o caminho/nome do arquivo que será criado.
        self.destino = destino

        # Guarda a quantidade de imagens adicionadas ao arquivo.
        self._itens = 0

    # Marca escrever_cabecalho() como um método abstrato.
    # As subclasses serão obrigadas a implementar esse método.
    @abstractmethod
    def escrever_cabecalho(self) -> None:

        # O "pass" indica que a implementação será feita pelas subclasses.
        pass

    # Marca adicionar() como um método abstrato.
    @abstractmethod
    def adicionar(self, imagem: str) -> None:

        # Cada tipo concreto de arquivo deverá decidir
        # como uma imagem será adicionada.
        pass

    # Define um método concreto.
    # Ele NÃO precisa ser implementado pelas subclasses.
    def fechar(self) -> None:

        # Exibe uma mensagem informando que o arquivo foi fechado.
        print(
            f"  └─ [{self.destino}] fechado "
            f"({self._itens} imagens)"
        )