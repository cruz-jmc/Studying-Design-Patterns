# Importa o Creator abstrato.
from exportador_de_acervo import ExportadorDeAcervo

# Importa o ConcreteProduct que será criado.
from arquivo_fits import ArquivoFITS


# Cria um exportador especializado em FITS.
class ExportadorFITS(ExportadorDeAcervo):

    # Sobrescreve o Factory Method.
    def criar_arquivo(self, destino: str):

        # Cria e retorna o produto concreto ArquivoFITS.
        return ArquivoFITS(destino)