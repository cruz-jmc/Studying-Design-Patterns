from .ui_factory import UIFactory # Importa a interface UIFactory.
from product.botao_light import BotaoLight # Importa o botão concreto do tema Light.
from product.janela_light import JanelaLight # Importa a janela concreta do tema Light.


# Cria a fábrica responsável pelo conjunto de componentes Light.
class LightThemeFactory(UIFactory):

    # Implementa o método criar_botao() definido pela UIFactory.
    def criar_botao(self):

        # Cria uma instância do botão Light.
        botao = BotaoLight()

        return botao

    # Implementa o método criar_janela() definido pela UIFactory.
    def criar_janela(self):

        # Cria uma instância da janela Light.
        janela = JanelaLight()

        return janela