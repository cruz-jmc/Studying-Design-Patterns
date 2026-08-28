# Importa a abstração Imagem.
from imagem import Imagem


# Declara o Decorator base.
# Ele também herda de Imagem para possuir a mesma interface.
class ImagemDecorator(Imagem):

    # O construtor recebe qualquer objeto que seja uma Imagem.
    def __init__(self, imagem: Imagem) -> None:

        # Armazena a imagem que será envolvida pelo Decorator.
        self.imagem = imagem


    # Implementa o método exibir().
    def exibir(self) -> None:

        # Delega a chamada para o objeto que está sendo envolvido.
        self.imagem.exibir()


    # Implementa o método dimensoes().
    def dimensoes(self) -> tuple[int, int]:

        # Delega a solicitação das dimensões para o objeto envolvido.
        return self.imagem.dimensoes()