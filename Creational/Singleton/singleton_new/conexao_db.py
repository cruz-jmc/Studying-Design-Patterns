class ConexaoDB:

    # Guarda a única instância criada pela classe.
    _instancia = None

    # O método __new__ é responsável por criar uma nova instância.
    def __new__(cls, *args, **kwargs):

        # Verifica se ainda não existe uma instância da classe.
        if cls._instancia is None:

            # Cria a instância normalmente através do __new__ da superclasse.
            cls._instancia = super().__new__(cls)

        # Retorna a única instância existente.
        return cls._instancia

    # O método __init__ inicializa a instância.
    def __init__(self, dsn="postgres://acervo"):

        # Verifica se a instância já possui o atributo _socket.
        if hasattr(self, "_socket"):

            # Se o atributo já existe, significa que a instância
            # já foi inicializada anteriormente.
            return

        # Exibe uma mensagem simulando a abertura da conexão.
        print(f"[REDE] abrindo conexão com {dsn}...")

        # Simula a criação de um socket para a conexão.
        self._socket = f"socket-{id(self)}"

    # Define o método responsável por executar uma consulta.
    def consultar(self, sql: str):

        # Retorna uma representação da consulta utilizando o socket.
        return f"[{self._socket}] {sql}"