# Importa o Decorator base.
from imagem_decorator import ImagemDecorator


# Declara um Decorator responsável pelo ajuste de contraste.
class Contraste(ImagemDecorator):

    # Sobrescreve o método exibir().
    def exibir(self) -> None:

        # Informa que o contraste está sendo ajustado.
        print("Ajustando o contraste da imagem.")

        # Delega a execução para o objeto envolvido.
        super().exibir()