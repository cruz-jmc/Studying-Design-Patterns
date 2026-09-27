# Importa a classe Circulo.
# Ela será um dos ConcretePrototypes utilizados pelo cliente.
from circulo import Circulo


# Importa a classe Retangulo.
# Ela será outro ConcretePrototype utilizado pelo cliente.
from retangulo import Retangulo


# Define a função principal da aplicação.
def main():

    # Cria o círculo original.
    # Esse objeto poderá funcionar como um protótipo.
    circulo_original = Circulo(
        x=10,
        y=20,
        cor="vermelho",
        raio=50
    )

    # Cria o retângulo original.
    # Ele também poderá funcionar como um protótipo.
    retangulo_original = Retangulo(
        x=30,
        y=40,
        cor="azul",
        largura=100,
        altura=50
    )

    # Mostra uma separação visual no terminal.
    print("=== CÍRCULO ORIGINAL ===")

    # Exibe os dados do círculo original.
    circulo_original.mostrar()

    # Solicita ao próprio objeto que faça uma cópia de si mesmo.
    circulo_copia = circulo_original.clone()

    # Mostra uma separação visual.
    print("\n=== CÍRCULO COPIADO ===")

    # Exibe os dados da cópia.
    circulo_copia.mostrar()

    # Altera a cor apenas da cópia.
    circulo_copia.cor = "verde"

    # Mostra uma separação visual.
    print("\n=== APÓS ALTERAR A CÓPIA ===")

    # Exibe o objeto original.
    print("\nCírculo original:")

    # Mostra novamente o estado do original.
    circulo_original.mostrar()

    # Exibe a cópia.
    print("\nCírculo copiado:")

    # Mostra o estado da cópia depois da alteração.
    circulo_copia.mostrar()

    # Mostra uma mensagem explicativa.
    print("\nAs duas referências apontam para o mesmo objeto?")

    # Verifica se original e cópia são exatamente o mesmo objeto na memória.
    # O resultado esperado é False.
    print(circulo_original is circulo_copia)

    # Mostra uma separação visual para o exemplo do retângulo.
    print("\n=== RETÂNGULO ORIGINAL ===")

    # Mostra os dados do retângulo original.
    retangulo_original.mostrar()

    # Solicita ao próprio retângulo que crie uma cópia.
    retangulo_copia = retangulo_original.clone()

    # Mostra uma separação visual.
    print("\n=== RETÂNGULO COPIADO ===")

    # Mostra os dados da cópia.
    retangulo_copia.mostrar()

    # Cria uma lista contendo diferentes tipos de formas.
    formas = [
        circulo_original,
        retangulo_original
    ]

    # Cria uma nova lista contendo uma cópia de cada forma.
    # Observe que não precisamos verificar se é Círculo ou Retângulo.
    copias = [forma.clone() for forma in formas]

    # Mostra uma separação visual.
    print("\n=== CLONANDO VÁRIAS FORMAS ===")

    # Percorre todas as cópias criadas.
    for copia in copias:

        # Mostra os dados da cópia.
        copia.mostrar()

        # Imprime uma linha vazia para separar as formas.
        print()


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":

    # Chama a função principal.
    main()