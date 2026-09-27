# Importa a classe Forma.
# Retangulo será uma especialização de Forma.
from forma import Forma


# Importa count para gerar identificadores sequenciais.
from itertools import count


# Cria um contador para os identificadores internos dos retângulos.
_proximo_id = count(1)


# Declara a classe Retangulo.
# Ela herda de Forma.
class Retangulo(Forma):

    # Define o construtor do retângulo.
    def __init__(self, x, y, cor, largura, altura):

        # Chama o construtor da classe Forma.
        # x, y e cor serão inicializados pela classe pai.
        super().__init__(x, y, cor)

        # Guarda a largura do retângulo.
        self.largura = largura

        # Guarda a altura do retângulo.
        self.altura = altura

        # Calcula a área e guarda o resultado em um atributo privado.
        self.__cache_area = largura * altura

        # Gera um identificador interno para esta instância.
        self.__id_render = next(_proximo_id)

    # Implementa o método clone(). Esta é a implementação concreta da clonagem do Retangulo.
    def clone(self):

        # Cria uma nova instância de Retangulo. Utilizamos os mesmos valores do objeto original.
        copia = Retangulo(
            self.x,
            self.y,
            self.cor,
            self.largura,
            self.altura
        )

        # Copia também o cache interno da área. O próprio Retangulo consegue acessar esse atributo.
        copia.__cache_area = self.__cache_area

        return copia

    # Cria um método auxiliar para mostrar o estado do retângulo.
    def mostrar(self):

        # Mostra o tipo da forma.
        print("Tipo: Retângulo")

        # Mostra a posição.
        print(f"Posição: ({self.x}, {self.y})")

        # Mostra a cor.
        print(f"Cor: {self.cor}")

        # Mostra a largura.
        print(f"Largura: {self.largura}")

        # Mostra a altura.
        print(f"Altura: {self.altura}")

        # Mostra o cache interno da área.
        print(f"Cache da área: {self.__cache_area}")

        # Mostra o identificador interno.
        print(f"ID de renderização: {self.__id_render}")