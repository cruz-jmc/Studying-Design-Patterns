# Importa o decorator dataclass, que reduz a quantidade de código necessário para criar classes de dados.
from dataclasses import dataclass, field


# Declara que RelatorioPDF será uma dataclass.
@dataclass
class RelatorioPDF:

    # Cria uma lista de páginas que armazenará o conteúdo do relatório.
    # O default_factory garante que cada RelatorioPDF tenha sua própria lista.
    paginas: list[str] = field(default_factory=list)
    # define um atributo chamado paginas que aceita uma lista de strings (list[str])
    # Em vez de passar uma lista pronta como valor padrão,
    # você passa uma função construtora (neste caso, a própria função embutida list)

    # Declara o método responsável por transformar o relatório em texto.
    def renderizar(self) -> str:

        # Percorre todas as páginas armazenadas no relatório.
        # enumerate() fornece tanto o índice quanto o conteúdo de cada página.
        # i + 1 transforma o índice iniciado em 0 em uma numeração iniciada em 1.
        # O resultado de cada iteração possui o número da página e seu conteúdo.
        return "\n".join(
            f"--- pág {i + 1} ---\n{pagina}"
            for i, pagina in enumerate(self.paginas)
        )