# Importa o Creator abstrato.
from exportador_de_acervo import ExportadorDeAcervo

# Importa o ConcreteProduct ArquivoPNG.
from arquivo_png import ArquivoPNG


# Cria um exportador especializado em PNG.
class ExportadorPNG(ExportadorDeAcervo):

    # Sobrescreve o Factory Method.
    def criar_arquivo(self, destino: str):

        # Cria e retorna o produto concreto ArquivoPNG.
        return ArquivoPNG(destino)