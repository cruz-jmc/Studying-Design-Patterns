# Importa a função dataclass do módulo dataclasses.
# Ela permite criar classes destinadas principalmente a armazenar dados
# sem precisarmos escrever manualmente vários métodos, como __init__().
from dataclasses import dataclass


# @dataclass transforma a classe TipoEstrela em uma dataclass.
# frozen=True impede alterações nos atributos depois que o objeto é criado.
# slots=True reduz a sobrecarga de memória de cada instância.
# Isso é interessante no contexto do Flyweight porque estamos preocupados
# justamente com o uso de memória.
@dataclass(frozen=True, slots=True)
class TipoEstrela:

    # Armazena o tipo espectral da estrela.
    # Exemplos: "O", "B", "A", "F", "G", "K" ou "M".
    tipo_espectral: str

    # Armazena a cor RGB associada ao tipo da estrela.
    # O tuple possui três inteiros: vermelho, verde e azul.
    cor_rgb: tuple[int, int, int]

    # Armazena a textura utilizada pelas estrelas daquele tipo.
    # bytes é utilizado aqui apenas para representar dados binários.
    textura: bytes

    # Armazena a curva de luminosidade daquele tipo de estrela.
    # Novamente utilizamos bytes apenas como representação simplificada.
    curva: bytes

    # Define o comportamento responsável por desenhar a estrela.
    # x e y serão recebidos do Context porque são estado extrínseco.
    def desenhar(self, tela: str, x: float, y: float) -> None:

        # Exibe no terminal informações sobre o desenho.
        # self.tipo_espectral e self.cor_rgb vêm do Flyweight.
        # x e y vêm do objeto EstrelaNaImagem.
        print(
            # Monta uma mensagem indicando a tela, o tipo, a cor
            # e a posição em que a estrela será desenhada.
            f"[{tela}] "
            f"{self.tipo_espectral} "
            f"rgb={self.cor_rgb} "
            f"em ({x:.1f}, {y:.1f})"
        )