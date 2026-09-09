# Importa Callable do módulo typing.
from typing import Callable

# Importa o Product.
from arquivo import Arquivo

# Importa os três ConcreteProducts.
from arquivo_fits import ArquivoFITS
from arquivo_png import ArquivoPNG
from arquivo_tiff import ArquivoTIFF

# Lista contendo os nomes das imagens que serão exportadas.
imagens = [
    "hubble_001",
    "hubble_002",
    "andromeda"
]


# Cria um apelido de tipo para representar uma função
# que recebe uma string e retorna um Arquivo.
FabricaDeArquivo = Callable[[str], Arquivo]


# Cria um exportador que recebe a fábrica pelo construtor.
class ExportadorDeAcervo:

    # Define o construtor da classe.
    def __init__(
        self,
        criar_arquivo: FabricaDeArquivo
    ) -> None:

        # Guarda a função responsável por criar o arquivo.
        self._criar_arquivo = criar_arquivo

    # Define o fluxo de exportação.
    def exportar(
        self,
        imagens: list[str],
        destino: str
    ) -> None:

        # Exibe uma mensagem informando a quantidade de imagens.
        print(
            f"Exportando {len(imagens)} imagens →"
        )

        # Usa a função recebida no construtor
        # para criar o arquivo.
        arquivo = self._criar_arquivo(destino)

        # Solicita que o arquivo escreva seu cabeçalho.
        arquivo.escrever_cabecalho()

        # Percorre todas as imagens.
        for img in imagens:

            # Adiciona a imagem ao arquivo.
            arquivo.adicionar(img)

        # Fecha o arquivo.
        arquivo.fechar()


# Cria o exportador passando ArquivoFITS como fábrica.
ExportadorDeAcervo(ArquivoFITS).exportar(
    imagens,
    "acervo.fits"
)


# Cria o exportador passando ArquivoPNG como fábrica.
ExportadorDeAcervo(ArquivoPNG).exportar(
    imagens,
    "galeria.png"
)


# Cria o exportador passando ArquivoTIFF como fábrica.
ExportadorDeAcervo(ArquivoTIFF).exportar(
    imagens,
    "impressao.tiff"
)