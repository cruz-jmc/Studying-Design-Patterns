from .ui_factory import UIFactory # Importa a interface UIFactory.
from product.botao_dark import BotaoDark # Importa o botão concreto do tema Dark.
from product.janela_dark import JanelaDark # Importa a janela concreta do tema Dark.


# Cria a fábrica responsável pelo conjunto de componentes Dark.
class DarkThemeFactory(UIFactory):

    # Implementa o método criar_botao() definido pela UIFactory.
    def criar_botao(self):

        # Cria uma instância do botão Dark.
        botao = BotaoDark()

        return botao

    # Implementa o método criar_janela() definido pela UIFactory.
    def criar_janela(self):

        # Cria uma instância da janela Dark.
        janela = JanelaDark()

        return janela