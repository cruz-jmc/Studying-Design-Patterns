# Importa a função consultar diretamente do módulo conexao.
from conexao import consultar


# Define a função responsável por exportar imagens.
def exportar(imagens):

    # Consulta os dados necessários para realizar a exportação.
    dados = consultar("SELECT * FROM acervo")

    # Exibe os dados obtidos.
    print(dados)

    # Exibe as imagens que seriam exportadas.
    print(f"Exportando: {imagens}")