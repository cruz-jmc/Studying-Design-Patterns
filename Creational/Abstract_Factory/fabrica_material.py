# Importa a fábrica abstrata.
from fabrica_widgets import FabricaWidgets

# Importa o produto concreto BotaoMaterial.
from botao_material import BotaoMaterial

# Importa o produto concreto CheckboxMaterial.
from checkbox_material import CheckboxMaterial


# Declara a fábrica concreta responsável pela família Material.
class FabricaMaterial(FabricaWidgets):

    # Implementa o método criar_botao() definido pela fábrica abstrata.
    def criar_botao(self, rotulo: str) -> BotaoMaterial:

        # Cria e retorna um botão da família Material.
        return BotaoMaterial(rotulo)

    # Implementa o método criar_checkbox() definido pela fábrica abstrata.
    def criar_checkbox(self, rotulo: str) -> CheckboxMaterial:

        # Cria e retorna um checkbox da família Material.
        return CheckboxMaterial(rotulo)