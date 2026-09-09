# Importa a classe Arquivo, que representa o Product.
from arquivo import Arquivo


# Cria o produto concreto responsável por arquivos FITS.
class ArquivoFITS(Arquivo):

    # Implementa o método abstrato escrever_cabecalho().
    def escrever_cabecalho(self) -> None:

        # Simula a escrita do cabeçalho específico do formato FITS.
        print("  ├─ [FITS] SIMPLE=T BITPIX=-32 NAXIS=2")

    # Implementa o método abstrato adicionar().
    def adicionar(self, imagem: str) -> None:

        # Incrementa a quantidade de imagens armazenadas.
        self._itens += 1

        # Simula a adição da imagem ao arquivo FITS.
        print(
            f"  ├─ [FITS] HDU {self._itens}: {imagem}"
        )