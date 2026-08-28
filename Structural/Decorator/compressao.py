# Importa o Decorator base.
from imagem_decorator import ImagemDecorator


# Declara um Decorator responsável por comprimir a imagem.
class Compressao(ImagemDecorator):

    # Sobrescreve o método exibir().
    def exibir(self) -> None:

        # Informa que a imagem está sendo comprimida.
        print("Comprimindo a imagem antes da exibição.")

        # Delega a execução para o próximo objeto da cadeia.
        super().exibir()