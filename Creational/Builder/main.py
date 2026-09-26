# Importa o Builder responsável por construir relatórios PDF.
from Builders.construtor_pdf import ConstrutorPDF

# Importa o Builder responsável por construir relatórios HTML.
from Builders.construtor_html import ConstrutorHTML

# Importa o Director responsável pelas receitas de construção.
from Director.diretor_de_relatorio import DiretorDeRelatorio


# Define a função principal da aplicação.
def main():

    # Cria a lista de imagens que será utilizada nos relatórios.
    imagens = ["hubble_001", "andromeda"]

    # ============================================================
    # BUILDER SEM DIRECTOR
    # ============================================================

    # Cria um Builder concreto para PDF.
    pdf = ConstrutorPDF()

    # Utiliza o Builder diretamente, definindo manualmente cada etapa.
    relatorio_pdf = (
        pdf
        .com_cabecalho("Observação NGC 4654")
        .com_imagens(imagens)
        .com_rodape("UPE Garanhuns")
        .construir()
    )

    # Exibe o relatório PDF no terminal.
    print(relatorio_pdf.renderizar())

    # Cria um Builder concreto para HTML.
    html = ConstrutorHTML()

    # Utiliza o Builder HTML diretamente.
    relatorio_html = (
        html
        .com_cabecalho("Observação NGC 4654")
        .com_imagens(imagens)
        .com_rodape("UPE Garanhuns")
        .construir()
    )

    # Exibe o relatório HTML no terminal.
    print(relatorio_html.renderizar())

    # ============================================================
    # BUILDER COM DIRECTOR
    # ============================================================

    # Cria uma instância do Director.
    diretor = DiretorDeRelatorio()

    # Cria um novo Builder PDF.
    pdf = ConstrutorPDF()

    # Solicita ao Director que execute a receita de relatório completo.
    diretor.relatorio_completo(
        pdf,
        "NGC 4654",
        imagens
    )

    # Finaliza a construção do relatório PDF.
    arquivo_pdf = pdf.construir()

    # Exibe o relatório PDF construído pelo Director.
    print(arquivo_pdf.renderizar())

    # Cria um novo Builder HTML.
    html = ConstrutorHTML()

    # Solicita ao Director que execute a mesma receita no Builder HTML.
    diretor.relatorio_completo(
        html,
        "NGC 4654",
        imagens
    )

    # Finaliza a construção do relatório HTML.
    arquivo_html = html.construir()

    # Exibe o relatório HTML construído pelo Director.
    print(arquivo_html.renderizar())


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":

    # Executa a função principal da aplicação.
    main()