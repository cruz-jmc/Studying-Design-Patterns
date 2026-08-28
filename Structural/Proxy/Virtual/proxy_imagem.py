# Importamos a interface Imagem.
# O Proxy precisa seguir o mesmo contrato
# utilizado pela imagem real.
from imagem import Imagem


# Importamos o objeto real.
# O Proxy irá criar esse objeto somente quando necessário.
from imagem_alta_resolucao import ImagemAltaResolucao


# Criamos a classe ProxyImagem.
# Ela implementa a mesma interface Imagem.
class ProxyImagem(Imagem):


    # O construtor recebe as informações necessárias
    # para representar uma imagem.
    def __init__(
        self,
        caminho: str,
        largura: int,
        altura: int
    ):

        # Guardamos o caminho da imagem.
        self.caminho = caminho

        # Guardamos as dimensões conhecidas da imagem.
        self._dimensoes = (largura, altura)

        # Criamos uma referência para o objeto real.
        # Inicialmente ela possui o valor None porque
        # a imagem real ainda não foi carregada.
        self._real: ImagemAltaResolucao | None = None


    # Implementamos o método dimensoes().
    def dimensoes(self) -> tuple[int, int]:

        # Retornamos as dimensões que já conhecemos.
        #
        # Perceba que não precisamos criar
        # ImagemAltaResolucao para isso.
        #
        # Portanto, conseguimos obter as dimensões
        # sem carregar os 450 MB da imagem.
        return self._dimensoes


    # Implementamos o método exibir().
    def exibir(self) -> None:

        # Verificamos se o objeto real ainda não existe.
        if self._real is None:

            # Informamos que a imagem será carregada
            # pela primeira vez.
            print(
                f"[PROXY] 1ª exibição de "
                f"{self.caminho} → instanciando o objeto real"
            )

            # Criamos o objeto real somente agora.
            #
            # É neste momento que ocorrerá o carregamento
            # pesado da imagem.
            self._real = ImagemAltaResolucao(
                self.caminho
            )


        # Depois de garantir que o objeto real existe,
        # delegamos a operação para ele.
        self._real.exibir()