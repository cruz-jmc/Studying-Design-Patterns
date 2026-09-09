# Importa a abstração Checkbox.
from checkbox import Checkbox


# Declara o checkbox concreto da família Cupertino.
class CheckboxCupertino(Checkbox):

    # Construtor da classe.
    def __init__(self, rotulo: str):

        # Armazena o texto associado ao checkbox.
        self.rotulo = rotulo

    # Implementa o método renderizar() definido em Checkbox.
    def renderizar(self) -> str:

        # Retorna uma representação textual de um checkbox Cupertino.
        return f"(●—) {self.rotulo}"