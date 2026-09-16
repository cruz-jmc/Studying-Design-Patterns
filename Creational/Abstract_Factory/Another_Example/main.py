from factory.ui_factory import UIFactory # Importa a interface UIFactory.
from factory.dark_theme_factory import DarkThemeFactory # Importa a fábrica responsável pelo tema Dark.
from factory.light_theme_factory import LightThemeFactory # Importa a fábrica responsável pelo tema Light.


# Cria a classe que representa a aplicação.
class Aplicacao:

    # O construtor recebe uma fábrica de interface.
    def __init__(self, factory: UIFactory):

        # Armazena a fábrica recebida e utiliza ela para criar o botão e a janela.
        self.factory = factory
        self.botao = self.factory.criar_botao()
        self.janela = self.factory.criar_janela()

    # Define o método responsável por renderizar a aplicação.
    def renderizar(self):

        # Chama os métodos desenhar() e exibir() de botao e janela que foram criados.
        self.botao.desenhar()
        self.janela.exibir()


if __name__ == "__main__":

    # Cria uma fábrica para o tema Dark.
    dark_factory = DarkThemeFactory()

    # Cria uma aplicação utilizando a fábrica Dark.
    aplicacao_dark = Aplicacao(dark_factory)

    print("=== TEMA DARK ===")

    # Renderiza os componentes da aplicação Dark.
    aplicacao_dark.renderizar()

    print()

    # Faz o mesmo, mas agora utilizando o tema Light.
    light_factory = LightThemeFactory()

    aplicacao_light = Aplicacao(light_factory)

    print("=== TEMA LIGHT ===")

    aplicacao_light.renderizar()