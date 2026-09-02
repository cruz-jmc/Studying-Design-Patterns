# Importa a abstração comum utilizada
# pelos elementos do acervo.
from classes.item_do_acervo import ItemDoAcervo


# Define a classe Pasta.
# Pasta também é um ItemDoAcervo.
class Pasta(ItemDoAcervo):

    # Define o construtor da classe Pasta.
    def __init__(self, nome: str):

        # Chama o construtor da classe pai
        # para inicializar o nome da pasta.
        super().__init__(nome)

        # Cria uma lista vazia.
        # Essa lista armazenará os filhos da pasta.
        self._filhos: list[ItemDoAcervo] = []


    # Adiciona um novo item dentro da pasta.
    def adicionar(self, item: ItemDoAcervo) -> "Pasta":

        # Adiciona o item recebido à lista de filhos.
        self._filhos.append(item)

        # Retorna a própria pasta.
        # Isso permite encadear chamadas de adicionar().
        return self


    # Remove um item da lista de filhos.
    def remover(self, item: ItemDoAcervo) -> None:

        # Remove o item recebido da lista de filhos.
        self._filhos.remove(item)


    # Calcula o tamanho total da pasta.
    def tamanho(self) -> float:

        # Percorre todos os filhos da pasta,
        # chama tamanho() em cada um
        # e soma todos os resultados.
        return sum(filho.tamanho() for filho in self._filhos)


    # Conta todos os arquivos existentes
    # dentro da pasta.
    def contar_arquivos(self) -> int:

        # Percorre todos os filhos,
        # chama contar_arquivos() em cada um
        # e soma os resultados.
        return sum(filho.contar_arquivos() for filho in self._filhos)


    # Lista a pasta e todos os seus descendentes.
    def listar(self, nivel: int = 0) -> None:

        # Imprime o nome da pasta.
        # A indentação depende do nível atual na árvore.
        print(f"{'  ' * nivel}{self.nome}/ ({self.tamanho():.2f} MB)")

        # Percorre todos os filhos da pasta.
        for filho in self._filhos:

            # Chama listar() para cada filho.
            # O nível aumenta em 1.
            # Isso cria a indentação e a recursão.
            filho.listar(nivel + 1)

    def buscar # -> falta denifir o buscar

    def caminho(self, nome: Str) -> str | None: # -> falta definir o caminho
        if self.nome == nome:
