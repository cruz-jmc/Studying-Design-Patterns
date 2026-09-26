# Importa a classe abstrata que define o contrato dos Builders.
from Builders.construtor_de_relatorio import ConstrutorDeRelatorio

# Importa o produto PDF que será construído por este Builder.
from Products.relatorio_pdf import RelatorioPDF


# Declara o Builder concreto responsável pela construção de relatórios PDF.
class ConstrutorPDF(ConstrutorDeRelatorio):

    # Define o construtor da classe.
    def __init__(self):

        # Inicializa o Builder criando um produto vazio.
        self.reiniciar()

    # Reinicia o estado interno do Builder.
    def reiniciar(self) -> None:

        # Cria um novo relatório PDF vazio.
        # O atributo _r representa o produto que está sendo construído.
        self._r = RelatorioPDF()

    # Adiciona um cabeçalho ao relatório que está sendo construído.
    def com_cabecalho(self, titulo: str) -> "ConstrutorPDF":

        # Adiciona uma nova página contendo o logotipo e o título.
        # upper() transforma o título em letras maiúsculas.
        self._r.paginas.append(
            f"[LOGO UPE]\n{titulo.upper()}"
        )

        # Retorna a própria instância do Builder.
        # Isso permite realizar chamadas encadeadas.
        return self

    # Adiciona imagens ao relatório.
    def com_imagens(self, imagens: list[str]) -> "ConstrutorPDF":

        # Percorre cada imagem recebida.
        for imagem in imagens:

            # Adiciona uma página representando a figura.
            self._r.paginas.append(
                f"[figura: {imagem}.fits]"
            )

        # Retorna a própria instância para permitir encadeamento.
        return self

    # Adiciona um rodapé ao relatório.
    def com_rodape(self, texto: str) -> "ConstrutorPDF":

        # Cria uma linha separadora e adiciona o texto do rodapé.
        self._r.paginas.append(
            f"{'_' * 30}\n{texto}"
        )

        # Retorna a própria instância do Builder.
        return self

    # Finaliza a construção e devolve o produto pronto.
    def construir(self) -> RelatorioPDF:

        # Guarda temporariamente o produto que acabou de ser construído.
        resultado = self._r

        # Cria um novo produto vazio para que o Builder possa ser reutilizado.
        self._r = RelatorioPDF()

        # Retorna o produto que foi construído.
        return resultado