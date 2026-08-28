# Importa o Decorator base.
from imagem_decorator import ImagemDecorator


# Declara um Decorator responsável pelo registro de logs.
class Log(ImagemDecorator):

    # Sobrescreve o método exibir().
    def exibir(self) -> None:

        # Obtém as dimensões da imagem que está sendo decorada.
        largura, altura = self.dimensoes()

        # Registra no log que a imagem será exibida.
        print(
            f"[LOG] Iniciando exibição da imagem "
            f"com dimensões {largura}x{altura}."
        )

        # Delega a execução para o objeto envolvido.
        super().exibir()

        # Registra que a operação foi concluída.
        print("[LOG] Exibição da imagem finalizada.")