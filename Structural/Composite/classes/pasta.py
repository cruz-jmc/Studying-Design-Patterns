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


    # Lista a estrutura da pasta.
    def listar(self, nivel: int = 0) -> None:

        # Cria a indentação de acordo com o nível da árvore.
        indentacao = "    " * nivel

        # Exibe o nome da pasta.
        # Também mostra seu tamanho total.
        print(
            f"{indentacao}{self.nome}/ "
            f"({self.tamanho():.2f} MB)"
        )

        # Percorre todos os filhos.
        for filho in self._filhos:

            # Chama listar() para cada filho.
            #
            # O nível aumenta em 1.
            #
            # Isso cria a estrutura visual em árvore.
            filho.listar(nivel + 1)


    # Busca um arquivo ou pasta pelo nome.
    def buscar(self, nome: str) -> ItemDoAcervo | None:

        # Primeiro verifica se a própria pasta possui o nome procurado.
        if self.nome == nome:

            # Retorna a própria pasta.
            return self


        # Percorre todos os filhos da pasta.
        for filho in self._filhos:

            # Pede para o filho procurar o item.
            encontrado = filho.buscar(nome)


            # Verifica se o filho encontrou algo.
            if encontrado is not None:

                # Retorna imediatamente o item encontrado.
                return encontrado


        # Caso nenhum filho encontre o item,
        # retorna None.
        return None


    # Busca o caminho completo de um arquivo ou pasta.
    def caminho(self, nome: str) -> str | None:

        # Primeiro verifica se estamos procurando a própria pasta.
        if self.nome == nome:

            # Retorna o nome da própria pasta.
            return self.nome


        # Percorre todos os filhos.
        for filho in self._filhos:

            # Pede para o filho procurar o caminho.
            caminho_encontrado = filho.caminho(nome)


            # Verifica se o filho encontrou o item.
            if caminho_encontrado is not None:

                # Adiciona o nome da pasta atual
                # antes do caminho retornado pelo filho.
                return f"{self.nome}/{caminho_encontrado}"


        # Caso nenhum filho encontre o item,
        # retorna None.
        return None