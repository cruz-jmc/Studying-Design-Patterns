# Importa ABC para permitir que ExportadorDeAcervo
# seja uma classe abstrata.
from abc import ABC, abstractmethod

# Importa a classe Arquivo porque o Factory Method
# retornará um objeto desse tipo.
from arquivo import Arquivo


# Cria o Creator abstrato do nosso padrão.
class ExportadorDeAcervo(ABC):

    # Define o método responsável pela exportação.
    def exportar(
        self,
        imagens: list[str],
        destino: str
    ) -> None:

        # Chama o Factory Method.
        # A classe NÃO sabe qual arquivo concreto será criado.
        arquivo = self.criar_arquivo(destino)

        # Solicita ao arquivo que escreva seu cabeçalho.
        arquivo.escrever_cabecalho()

        # Percorre todas as imagens recebidas.
        for img in imagens:

            # Adiciona a imagem ao arquivo criado.
            arquivo.adicionar(img)

        # Fecha o arquivo depois que todas as imagens foram adicionadas.
        arquivo.fechar()

    # Declara o Factory Method.
    @abstractmethod
    def criar_arquivo(
        self,
        destino: str
    ) -> Arquivo:

        # A classe filha será responsável por decidir
        # qual tipo concreto de Arquivo será criado.
        pass