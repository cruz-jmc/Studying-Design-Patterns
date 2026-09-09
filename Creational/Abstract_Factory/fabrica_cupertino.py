# Importa a fábrica abstrata.
from fabrica_widgets import FabricaWidgets

# Importa o produto concreto BotaoCupertino.
from botao_cupertino import BotaoCupertino

# Importa o produto concreto CheckboxCupertino.
from checkbox_cupertino import CheckboxCupertino


# Declara a fábrica concreta responsável pela família Cupertino.
class FabricaCupertino(FabricaWidgets):

    # Implementa o método criar_botao() definido pela fábrica abstrata.
    def criar_botao(self, rotulo: str) -> BotaoCupertino:

        # Cria e retorna um botão da família Cupertino.
        return BotaoCupertino(rotulo)

    # Implementa o método criar_checkbox() definido pela fábrica abstrata.
    def criar_checkbox(self, rotulo: str) -> CheckboxCupertino:

        # Cria e retorna um checkbox da família Cupertino.
        return CheckboxCupertino(rotulo)