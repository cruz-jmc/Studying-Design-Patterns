# Importa a função consultar do mesmo módulo conexao.
from conexao import consultar


# Define a função responsável por processar imagens.
def processar(imagens):

    # Executa uma consulta utilizando a conexão do módulo.
    dados = consultar("SELECT * FROM acervo")

    # Exibe os dados obtidos.
    print(dados)

    # Exibe as imagens que seriam processadas.
    print(f"Processando: {imagens}")