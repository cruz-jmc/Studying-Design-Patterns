# Implementação Ingenua — Sistema de Interface com Temas

# Este exemplo representa uma implementação mais ingênua do problema,
# utilizando vários if/else para decidir qual componente deve ser criado.

# A intenção é comparar esta abordagem com a implementação organizada
# em fábricas que será apresentada no exemplo principal.


# Define uma classe para representar a aplicação.
class Aplicacao:

    # O construtor recebe o tema que será utilizado pela aplicação.
    def __init__(self, tema):

        # Armazena o tema recebido.
        self.tema = tema

        # Inicialmente, o botão ainda não foi criado.
        self.botao = None

        # Inicialmente, a janela ainda não foi criada.
        self.janela = None

        # Verifica qual tema foi escolhido
        if self.tema == "dark":

            # Cria diretamente o botão do tema Dark.
            self.botao = "BotaoDark"

            # Cria diretamente a janela do tema Dark.
            self.janela = "JanelaDark"

        # Verifica se o tema escolhido é Light.
        elif self.tema == "light":

            # Cria diretamente o botão do tema Light.
            self.botao = "BotaoLight"

            # Cria diretamente a janela do tema Light.
            self.janela = "JanelaLight"

        else:

            raise ValueError("Tema inválido.")

    # Define o método responsável por renderizar a aplicação.
    def renderizar(self):

        # Verifica novamente qual tema está sendo utilizado.
        if self.tema == "dark":

            print("Desenhando botão no tema Dark.")

            print("Exibindo janela no tema Dark.")

        # Verifica se o tema utilizado é Light.
        elif self.tema == "light":

            print("Desenhando botão no tema Light.")

            print("Exibindo janela no tema Light.")


if __name__ == "__main__":

    # Define que a primeira aplicação utilizará o tema Dark.
    tema_dark = "dark"

    aplicacao_dark = Aplicacao(tema_dark)

    print("=== TEMA DARK ===")

    aplicacao_dark.renderizar()

    print()

    tema_light = "light"

    aplicacao_light = Aplicacao(tema_light)

    print("=== TEMA LIGHT ===")

    aplicacao_light.renderizar()
