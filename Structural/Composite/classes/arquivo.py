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


    # Implementa a listagem do arquivo.
    def listar(self, nivel: int = 0) -> None:

        # Cria a indentação de acordo com o nível da árvore.
        indentacao = "    " * nivel

        # Exibe o nome e o tamanho do arquivo.
        print(f"{indentacao}{self.nome} ({self._tamanho:.2f} MB)")


    # Implementa a busca pelo nome.
    def buscar(self, nome: str) -> ItemDoAcervo | None:

        # Verifica se o nome procurado é o nome deste arquivo.
        if self.nome == nome:

            # Retorna o próprio arquivo.
            return self

        # Caso contrário, o arquivo não foi encontrado.
        return None


    # Implementa a busca pelo caminho.
    def caminho(self, nome: str) -> str | None:

        # Verifica se o nome procurado é o nome deste arquivo.
        if self.nome == nome:

            # Como o arquivo não possui filhos,
            # seu caminho relativo é apenas seu próprio nome.
            return self.nome

        # Caso o nome seja diferente,
        # o arquivo não foi encontrado.
        return None