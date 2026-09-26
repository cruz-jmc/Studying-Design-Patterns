# Importa ABC, que permite criar uma classe abstrata.
from abc import ABC, abstractmethod


# Declara a interface abstrata utilizada pelos construtores de relatório.
class ConstrutorDeRelatorio(ABC):

    # Indica que este método precisa obrigatoriamente ser implementado pelas subclasses.
    @abstractmethod
    def reiniciar(self) -> None:

        # Não existe implementação concreta aqui.
        # Cada Builder concreto decidirá como reiniciar seu produto.
        pass

    # Indica que este método precisa ser implementado pelos Builders concretos.
    @abstractmethod
    def com_cabecalho(self, titulo: str) -> "ConstrutorDeRelatorio":

        # A implementação concreta ficará nos Builders específicos.
        pass

    # Indica que este método precisa ser implementado pelos Builders concretos.
    @abstractmethod
    def com_imagens(self, imagens: list[str]) -> "ConstrutorDeRelatorio":

        # A implementação concreta ficará nos Builders específicos.
        pass

    # Indica que este método precisa ser implementado pelos Builders concretos.
    @abstractmethod
    def com_rodape(self, texto: str) -> "ConstrutorDeRelatorio":

        # A implementação concreta ficará nos Builders específicos.
        pass

    # Declara o método responsável por finalizar a construção do produto.
    # O método não precisa estar na interface abstrata, mas colocá-lo aqui deixa o contrato explícito.
    @abstractmethod
    def construir(self):

        # Cada Builder concreto retornará seu próprio tipo de produto.
        pass