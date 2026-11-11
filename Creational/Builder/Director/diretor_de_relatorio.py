# Importa o Builder abstrato utilizado pelo Director.
from Builders.construtor_de_relatorio import ConstrutorDeRelatorio


# Declara o Director responsável por definir sequências pré-moldadas de construção.
class DiretorDeRelatorio:

    # Define uma receita para construir um relatório mínimo.
    def relatorio_minimo(
        self,
        construtor: ConstrutorDeRelatorio,
        titulo: str
    ) -> None:

        # Reinicia o Builder para garantir que a construção comece limpa.
        construtor.reiniciar()

        # Adiciona o cabeçalho e o rodapé seguindo uma sequência predefinida.
        (
            construtor
            .com_cabecalho(titulo)
            .com_rodape("UPE Garanhuns")
        )

    # Define uma receita para construir um relatório completo.
    def relatorio_completo(
        self,
        construtor: ConstrutorDeRelatorio,
        titulo: str,
        imagens: list[str]
    ) -> None:

        # Reinicia o Builder antes de iniciar uma nova construção.
        construtor.reiniciar()

        # Executa todas as etapas necessárias para produzir um relatório completo.
        (
            construtor
            .com_cabecalho(titulo)
            .com_imagens(imagens)
            .com_rodape("UPE Garanhuns")
        )