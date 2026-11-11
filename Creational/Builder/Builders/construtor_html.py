# Importa a interface abstrata dos Builders.
from Builders.construtor_de_relatorio import ConstrutorDeRelatorio

# Importa o produto HTML que será construído.
from Products.relatorio_html import RelatorioHTML


# Declara o Builder concreto responsável por construir relatórios HTML.
class ConstrutorHTML(ConstrutorDeRelatorio):

    # Define o construtor da classe.
    def __init__(self):

        # Inicializa o produto interno.
        self.reiniciar()

    # Cria um novo relatório HTML vazio.
    def reiniciar(self) -> None:

        # Cria uma nova instância de RelatorioHTML.
        self._r = RelatorioHTML()

    # Adiciona o cabeçalho ao relatório HTML.
    def com_cabecalho(self, titulo: str) -> "ConstrutorHTML":

        # Adiciona uma tag h1 contendo o título do relatório.
        self._r.tags.append(
            f'<h1 class="titulo">{titulo}</h1>'
        )

        # Retorna a própria instância para permitir chamadas encadeadas.
        return self

    # Adiciona imagens ao relatório HTML.
    def com_imagens(self, imagens: list[str]) -> "ConstrutorHTML":

        # Percorre todas as imagens recebidas.
        for imagem in imagens:

            # Cria uma tag img para cada imagem.
            self._r.tags.append(
                f'<img src="{imagem}.png" loading="lazy">'
            )

        # Retorna a própria instância do Builder.
        return self

    # Adiciona um rodapé ao relatório HTML.
    def com_rodape(self, texto: str) -> "ConstrutorHTML":

        # Cria uma tag footer contendo o texto recebido.
        self._r.tags.append(
            f"<footer>{texto}</footer>"
        )

        # Retorna a própria instância para permitir encadeamento.
        return self

    # Finaliza a construção do relatório.
    def construir(self) -> RelatorioHTML:

        # Guarda o produto atual antes de reiniciar o Builder.
        resultado = self._r

        # Cria um novo produto vazio para permitir reutilização do Builder.
        self._r = RelatorioHTML()

        # Retorna o produto finalizado.
        return resultado