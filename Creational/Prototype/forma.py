# Importa a classe Prototype. Forma será uma implementação da interface definida pelo Prototype.
from prototype import Prototype


# Ela herda de Prototype e, portanto, precisa respeitar o contrato de clone().
class Forma(Prototype):

    # Define o construtor da classe Forma.
    def __init__(self, x, y, cor):

        # Guarda a coordenada horizontal dentro do objeto.
        self.x = x

        # Guarda a coordenada vertical dentro do objeto.
        self.y = y

        # Guarda a cor dentro do objeto.
        self.cor = cor

    # Declara a operação de clonagem. Neste ponto ainda não sabemos como uma forma concreta será clonada.
    def clone(self):

        # Levanta uma exceção caso alguém tente clonar diretamente uma Forma.
        raise NotImplementedError(
            "As subclasses devem implementar clone()."
        )