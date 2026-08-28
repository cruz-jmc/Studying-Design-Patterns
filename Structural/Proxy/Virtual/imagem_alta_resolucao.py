# Importamos o módulo time.
# Ele será utilizado apenas para simular o tempo de carregamento
# de uma imagem muito grande.
import time


# Importamos a interface Imagem.
# A classe ImagemAltaResolucao deverá seguir esse "contrato".
from imagem import Imagem


# Criamos a classe ImagemAltaResolucao.
# Ela herda da interface Imagem.
class ImagemAltaResolucao(Imagem):


    # O construtor é executado quando criamos um objeto
    # da classe ImagemAltaResolucao.
    def __init__(self, caminho: str):

        # Guardamos o caminho do arquivo da imagem.
        # Exemplo: "hubble_001.fits".
        self.caminho = caminho

        # Simulamos os dados pesados da imagem.
        # A variável pixels representa os dados carregados
        # para a memória.
        self.pixels = self._carregar_do_disco()


    # Criamos um método privado.
    # O underline no início indica que esse método é interno
    # à própria classe.
    def _carregar_do_disco(self) -> bytes:

        # Informamos que o sistema está carregando a imagem.
        print(f"[DISCO] Lendo {self.caminho} (450 MB)...")

        # Simulamos uma operação demorada.
        # Em um sistema real, aqui poderia acontecer
        # a leitura de um arquivo grande do disco.
        time.sleep(1)

        # Retornamos uma quantidade de bytes fictícia.
        # Isso representa os dados da imagem carregados.
        return b"\x89PNG" * 100


    # Implementamos o método exibir definido
    # pela interface Imagem.
    def exibir(self) -> None:

        # Simulamos a exibição da imagem na tela.
        print(f"[TELA] Exibindo {self.caminho}")


    # Implementamos o método dimensoes definido
    # pela interface Imagem.
    def dimensoes(self) -> tuple[int, int]:

        # Retornamos as dimensões da imagem.
        # Nesse exemplo, utilizamos valores conhecidos
        # sem precisar carregar novamente o arquivo.
        return (8192, 8192)