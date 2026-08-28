# Importa a abstração Imagem.
# ImagemAltaResolucao precisará seguir o contrato definido por Imagem.
from imagem import Imagem


# Declara a classe concreta que representa uma imagem real.
# Ela herda da classe abstrata Imagem.
class ImagemAltaResolucao(Imagem):

    # O construtor recebe a largura e a altura da imagem.
    def __init__(self, largura: int, altura: int) -> None:

        # Armazena a largura da imagem no próprio objeto.
        self.largura = largura

        # Armazena a altura da imagem no próprio objeto.
        self.altura = altura


    # Implementa o método obrigatório definido pela interface Imagem.
    def exibir(self) -> None:

        # Exibe uma mensagem representando a exibição da imagem real.
        print(
            f"Exibindo imagem em alta resolução "
            f"({self.largura}x{self.altura})."
        )


    # Implementa o método obrigatório responsável por retornar as dimensões.
    def dimensoes(self) -> tuple[int, int]:

        # Retorna uma tupla contendo largura e altura.
        return self.largura, self.altura