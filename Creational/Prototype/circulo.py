# Importa a classe Forma. Circulo será uma especialização de Forma.
from forma import Forma


# Importa count para gerar identificadores sequenciais.
# Isso será utilizado apenas para demonstrar um estado interno do objeto.
from itertools import count


# Cria um contador que começa no número 1. Cada novo círculo receberá um identificador diferente.
_proximo_id = count(1)


# Declara a classe Circulo. Ela herda de Forma.
class Circulo(Forma):

    # Define o construtor do círculo.
    # Além de x, y e cor, o círculo possui um raio.
    def __init__(self, x, y, cor, raio):

        # Chama o construtor da classe Forma.
        # Dessa maneira, x, y e cor são inicializados pela classe pai.
        super().__init__(x, y, cor)

        # Guarda o raio específico do círculo.
        self.raio = raio

        # Cria um atributo privado contendo a área calculada. Esse é um exemplo de informação interna do objeto.
        self.__cache_area = 3.14159 * raio ** 2

        """
        Ele transforma __cache_area dentro da classe RelatorioPDF em:

        _RelatorioPDF__cache_area
        Isso significa que, se você tentar acessar o atributo pelo nome original do lado de fora da classe,
        o Python dirá que ele não existe
        ou seja, o __ antes do atributo serve para o Python entendê-lo como um atributo privado
        """

        # Cria um identificador interno para a instância. Esse atributo também representa um detalhe interno do objeto.
        self.__id_render = next(_proximo_id)

    # Implementa o método clone(). Agora temos a implementação concreta do Prototype.
    def clone(self):

        # Cria uma nova instância de Circulo. Utilizamos os mesmos valores do objeto original.
        copia = Circulo(
            self.x,
            self.y,
            self.cor,
            self.raio
        )

        # Copia também o valor armazenado no cache da área. O próprio Circulo conhece esse atributo privado.
        copia.__cache_area = self.__cache_area

        return copia

    # Cria um método auxiliar para visualizar o estado do objeto, só um monte de print.
    def mostrar(self):

        # Mostra o tipo da forma.
        print("Tipo: Círculo")

        # Mostra a posição.
        print(f"Posição: ({self.x}, {self.y})")

        # Mostra a cor.
        print(f"Cor: {self.cor}")

        # Mostra o raio.
        print(f"Raio: {self.raio}")

        # Mostra o cache interno da área.
        print(f"Cache da área: {self.__cache_area}")

        # Mostra o identificador interno.
        print(f"ID de renderização: {self.__id_render}")