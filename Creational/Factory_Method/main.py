# Importa o Creator concreto responsável por FITS.
from exportador_fits import ExportadorFITS

# Importa o Creator concreto responsável por PNG.
from exportador_png import ExportadorPNG

# Importa o Creator concreto responsável por TIFF.
from exportador_tiff import ExportadorTIFF


# Cria uma lista simulando imagens astronômicas.
imagens = [
    "hubble_001",
    "hubble_002",
    "andromeda"
]


# Cria um dicionário que relaciona o nome do formato
# à classe de exportador correspondente.
EXPORTADORES = {
    "fits": ExportadorFITS,
    "png": ExportadorPNG,
    "tiff": ExportadorTIFF,
}


# Define uma função responsável por exportar o acervo.
def exportar_acervo(
    imagens: list[str],
    destino: str,
    formato: str
) -> None:

    # Obtém a classe do exportador correspondente ao formato.
    classe_exportador = EXPORTADORES[formato]

    # Cria uma instância do ConcreteCreator.
    exportador = classe_exportador()

    # Executa o fluxo de exportação definido pelo Creator.
    exportador.exportar(imagens, destino)


# Exporta as imagens no formato FITS.
exportar_acervo(
    imagens,
    "acervo.fits",
    "fits"
)


# Exporta as imagens no formato PNG.
exportar_acervo(
    imagens,
    "site/galeria.png",
    "png"
)


# Exporta as imagens no formato TIFF.
exportar_acervo(
    imagens,
    "impressao.tiff",
    "tiff"
)