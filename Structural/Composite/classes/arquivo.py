# Importa a abstração comum utilizada por todos
# os elementos do acervo.
from classes.item_do_acervo import ItemDoAcervo


# Define a classe Arquivo.
# Arquivo herda de ItemDoAcervo.
class Arquivo(ItemDoAcervo):

    # Define o construtor da classe Arquivo.
    # Recebe o nome e o tamanho do arquivo em MB.
    def __init__(self, nome: str, tamanho_mb: float):

        # Chama o construtor da classe pai.
        # Isso inicializa o atributo nome.
        super().__init__(nome)

        # Armazena o tamanho próprio do arquivo.
        self._tamanho = tamanho_mb


    # Implementa a operação tamanho definida
    # na classe abstrata ItemDoAcervo.
    def tamanho(self) -> float:

        # Um arquivo possui tamanho próprio.
        # Portanto, simplesmente retorna seu tamanho.
        return self._tamanho


    # Implementa a operação de contar arquivos.
    def contar_arquivos(self) -> int:

        # Como este objeto é um arquivo,
        # ele conta como exatamente um arquivo.
        return 1


    # Implementa a operação de listar.
    def listar(self, nivel: int = 0) -> None:

        # Imprime espaços de acordo com o nível atual da árvore,
        # seguidos pelo nome e pelo tamanho do arquivo.
        print(f"{'  ' * nivel}{self.nome} ({self._tamanho:.2f} MB)")