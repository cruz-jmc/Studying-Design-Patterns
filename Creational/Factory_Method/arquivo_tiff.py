# Importa a abstração Arquivo.
from arquivo import Arquivo


# Cria o produto concreto responsável por arquivos TIFF.
class ArquivoTIFF(Arquivo):

    # Implementa o método abstrato escrever_cabecalho().
    def escrever_cabecalho(self) -> None:

        # Simula a escrita do cabeçalho específico de um TIFF.
        print("  ├─ [TIFF] II*\x00 LZW CMYK")

    # Implementa o método abstrato adicionar().
    def adicionar(self, imagem: str) -> None:

        # Incrementa a quantidade de imagens adicionadas.
        self._itens += 1

        # Simula a adição da imagem ao arquivo TIFF.
        print(
            f"  ├─ [TIFF] IFD {self._itens}: "
            f"{imagem} @300dpi"
        )