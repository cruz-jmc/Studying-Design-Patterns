# Importa a abstração Arquivo.
from arquivo import Arquivo


# Cria o produto concreto responsável por arquivos PNG.
class ArquivoPNG(Arquivo):

    # Implementa o método abstrato escrever_cabecalho().
    def escrever_cabecalho(self) -> None:

        # Simula a escrita do cabeçalho específico de um PNG.
        print("  ├─ [PNG] \x89PNG IHDR sRGB")

    # Implementa o método abstrato adicionar().
    def adicionar(self, imagem: str) -> None:

        # Incrementa a quantidade de imagens adicionadas.
        self._itens += 1

        # Simula a conversão da imagem para PNG.
        print(
            f"  ├─ [PNG] convertendo {imagem} para 8-bit"
        )