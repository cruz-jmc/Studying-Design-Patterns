# Importa a metaclasse SingletonMeta.
from singleton_meta import SingletonMeta


# Define a classe de conexão com o banco de dados. A classe utiliza SingletonMeta como sua metaclasse.
class ConexaoDB(metaclass=SingletonMeta):

    # Inicializa a conexão.
    def __init__(self, dsn="postgres://acervo"):

        # Exibe uma mensagem indicando a abertura da conexão.
        print(f"[REDE] abrindo conexão com {dsn}...")

        # Simula a criação de um socket.
        self._socket = f"socket-{id(self)}"

    # Define o método responsável por executar consultas.
    def consultar(self, sql: str):

        # Retorna a consulta utilizando o socket da conexão.
        return f"[{self._socket}] {sql}"