# Exibe uma mensagem quando o módulo é carregado.
print("[REDE] abrindo conexão com postgres://acervo...")

# Simula a abertura de um socket.
_socket = "socket-conexao"


# Define uma função para executar consultas.
def consultar(sql: str):

    # Retorna a consulta utilizando o socket criado pelo módulo.
    return f"[{_socket}] {sql}"