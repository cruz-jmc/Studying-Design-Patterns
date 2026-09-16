# Importa a classe abstrata Botao.
from .botao import Botao


class BotaoLight(Botao):

    def desenhar(self):
        print("Desenhando botão no tema Light.")