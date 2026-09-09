# Importa ABC e abstractmethod para criar uma abstração.
from abc import ABC, abstractmethod


# Declara a classe abstrata Checkbox.
class Checkbox(ABC):

    # Declara a operação que todo checkbox concreto deverá implementar.
    @abstractmethod
    def renderizar(self) -> str:

        # Não existe uma implementação específica aqui.
        # Cada família de produtos definirá sua própria implementação.
        pass