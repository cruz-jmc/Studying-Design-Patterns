# Importa a classe abstrata Botao.
from botao import Botao


# Declara o botão concreto da família Material.
# Ele herda de Botao e, portanto, precisa implementar renderizar().
class BotaoMaterial(Botao):

    # Construtor da classe.
    # Recebe o texto que será exibido no botão.
    def __init__(self, rotulo: str):

        # Armazena o rótulo recebido dentro do objeto.
        self.rotulo = rotulo

    # Implementa o método abstrato definido em Botao.
    def renderizar(self) -> str:

        # Retorna uma representação textual de um botão Material.
        # upper() transforma o texto em letras maiúsculas.
        return f"[ {self.rotulo.upper()} ]"