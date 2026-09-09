# Importa ABC e abstractmethod para criar uma fábrica abstrata.
from abc import ABC, abstractmethod

# Importa a abstração Botao.
from botao import Botao

# Importa a abstração Checkbox.
from checkbox import Checkbox


# Declara a fábrica abstrata de widgets.
class FabricaWidgets(ABC):

    # Declara o método responsável por criar um botão.
    @abstractmethod
    def criar_botao(self, rotulo: str) -> Botao:

        # A fábrica abstrata apenas define o contrato.
        # Ela não sabe qual botão concreto será criado.
        pass

    # Declara o método responsável por criar um checkbox.
    @abstractmethod
    def criar_checkbox(self, rotulo: str) -> Checkbox:

        # Novamente, apenas definimos o contrato.
        # A implementação será feita pelas fábricas concretas.
        pass