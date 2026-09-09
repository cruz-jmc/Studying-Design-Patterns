# Importa a abstração Botao.
from botao import Botao


# Declara o botão concreto da família Cupertino.
class BotaoCupertino(Botao):

    # Construtor da classe.
    def __init__(self, rotulo: str):

        # Armazena o rótulo recebido.
        self.rotulo = rotulo

    # Implementa o método renderizar() exigido por Botao.
    def renderizar(self) -> str:

        # Retorna uma representação textual de um botão Cupertino.
        return f"( {self.rotulo} )"