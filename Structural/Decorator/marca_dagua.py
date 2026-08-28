# Importa o Decorator base.
from imagem_decorator import ImagemDecorator


# Declara um Decorator responsável por adicionar uma marca d'água.
class MarcaDagua(ImagemDecorator):

    # Sobrescreve o método exibir().
    def exibir(self) -> None:

        # Exibe uma mensagem representando a aplicação da marca d'água.
        print("Aplicando marca d'água na imagem.")

        # Chama o método exibir() do objeto que está sendo decorado.
        super().exibir()