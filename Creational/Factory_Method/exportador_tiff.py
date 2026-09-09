# Importa o Creator abstrato.
from exportador_de_acervo import ExportadorDeAcervo

# Importa o ConcreteProduct ArquivoTIFF.
from arquivo_tiff import ArquivoTIFF


# Cria um exportador especializado em TIFF.
class ExportadorTIFF(ExportadorDeAcervo):

    # Sobrescreve o Factory Method.
    def criar_arquivo(self, destino: str):

        # Cria e retorna o produto concreto ArquivoTIFF.
        return ArquivoTIFF(destino)