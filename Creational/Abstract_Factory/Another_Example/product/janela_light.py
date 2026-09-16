# Importa a classe abstrata Janela.
from .janela import Janela


# Mesma coisa aqui so que para o tema "claro".
class JanelaLight(Janela):

    def exibir(self):
        print("Exibindo janela no tema Light.")