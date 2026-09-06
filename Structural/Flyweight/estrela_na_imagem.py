# Importa a classe TipoEstrela.
# Precisamos dela para informar que o atributo _tipo armazenará
# uma referência para um objeto TipoEstrela.
from tipo_estrela import TipoEstrela


# Define a classe que representa uma estrela individual na imagem.
class EstrelaNaImagem:

    # Define os atributos permitidos diretamente no objeto.
    # Isso evita a criação de um __dict__ para cada instância.
    # Como podemos possuir milhões de estrelas, isso pode reduzir
    # a sobrecarga de memória de cada objeto.
    __slots__ = ("_x", "_y", "_tipo")

    # Define o construtor da classe.
    # Ele será executado sempre que criarmos uma EstrelaNaImagem.
    def __init__(
        self,
        x: float,
        y: float,
        tipo: TipoEstrela
    ):

        # Armazena a posição horizontal da estrela.
        # Esse valor é específico daquela estrela.
        self._x = x

        # Armazena a posição vertical da estrela.
        # Esse valor também é específico daquela estrela.
        self._y = y

        # Armazena uma referência para o Flyweight.
        # Várias estrelas podem apontar para o mesmo TipoEstrela.
        self._tipo = tipo

    # Define o método responsável por desenhar a estrela.
    def desenhar(self, tela: str) -> None:

        # Delegamos o desenho para o Flyweight.
        # Passamos a tela e o estado extrínseco x/y.
        # O Flyweight fornece os dados intrínsecos, como tipo e cor.
        self._tipo.desenhar(
            tela,
            self._x,
            self._y
        )