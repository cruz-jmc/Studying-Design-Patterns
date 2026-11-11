# Importa o decorator dataclass, utilizado para simplificar a criação da classe.
from dataclasses import dataclass, field


# Declara que RelatorioHTML será uma dataclass.
@dataclass
class RelatorioHTML:

    # Cria uma lista que armazenará as tags HTML do relatório.
    # O default_factory cria uma nova lista para cada objeto.
    tags: list[str] = field(default_factory=list)

    # Declara o método responsável por renderizar o relatório como HTML.
    def renderizar(self) -> str:

        # Abre a estrutura HTML.
        # Depois adiciona todas as tags armazenadas.
        # Por fim, fecha a estrutura HTML.
        return "<html>\n" + "\n".join(self.tags) + "\n</html>"