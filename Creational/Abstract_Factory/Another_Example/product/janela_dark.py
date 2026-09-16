# Importa a classe abstrata Janela.
from .janela import Janela


# Também funciona igual ao botao_dark e botao_light. Mas respeitando a interface "Janela" definida anteriormente.
class JanelaDark(Janela):

    def exibir(self):        
        print("Exibindo janela no tema Dark.")