from abc import ABC, abstractmethod # Importa ABC para criar uma classe abstrata.
from product.botao import Botao # Importa a abstração Botao.
from product.janela import Janela # Importa a abstração Janela.


# Cria a interface UIFactory (nossa fábrica).
class UIFactory(ABC):

    # Define o método responsável pela criação de botões.
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    # Define o método responsável pela criação de janelas.
    @abstractmethod
    def criar_janela(self) -> Janela:
        pass