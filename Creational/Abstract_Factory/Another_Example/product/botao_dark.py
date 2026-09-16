# Importa a classe abstrata Botao.
from .botao import Botao


# Cria a classe BotaoDark. Ela herda de Botao e, portanto, precisa implementar desenhar().
# Uma implementação concreta do botao para o tema "escuro".
class BotaoDark(Botao):

    def desenhar(self):
        print("Desenhando botão no tema Dark.")