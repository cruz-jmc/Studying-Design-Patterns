from imagem_alta_resolucao import ImagemAltaResolucao
from marca_dagua import MarcaDagua
from compressao import Compressao
from contraste import Contraste
from log import Log


# Exibe um título para organizar a saída do programa.
print("\n=== IMAGEM ORIGINAL ===\n")


# Cria a imagem concreta com largura de 1920 pixels e altura de 1080 pixels.
imagem_original = ImagemAltaResolucao(1920, 1080)


# Exibe a imagem sem nenhum Decorator.
imagem_original.exibir()


# Exibe uma separação visual no terminal.
print("\n=== IMAGEM COM MARCA D'ÁGUA ===\n")


# Cria uma nova composição envolvendo a imagem com MarcaDagua.
imagem_com_marca_dagua = MarcaDagua(imagem_original)


# Exibe a imagem decorada.
imagem_com_marca_dagua.exibir()


# Exibe uma separação visual no terminal.
print("\n=== IMAGEM COM COMPRESSÃO E CONTRASTE ===\n")


# Primeiro envolve a imagem com Compressao.
imagem_com_tratamentos = Compressao(imagem_original)


# Depois envolve o resultado anterior com Contraste.
imagem_com_tratamentos = Contraste(imagem_com_tratamentos)


# Exibe a composição final.
imagem_com_tratamentos.exibir()


# Exibe uma separação visual no terminal.
print("\n=== IMAGEM COM TODOS OS TRATAMENTOS ===\n")


# Cria uma nova imagem real para demonstrar uma composição completa.
imagem_completa = ImagemAltaResolucao(3840, 2160)


# Adiciona uma marca d'água à imagem.
imagem_completa = MarcaDagua(imagem_completa)


# Adiciona compressão sobre o objeto já decorado.
imagem_completa = Compressao(imagem_completa)


# Adiciona ajuste de contraste sobre a composição anterior.
imagem_completa = Contraste(imagem_completa)


# Adiciona o Decorator de log como camada mais externa.
imagem_completa = Log(imagem_completa)


# Executa toda a cadeia de Decorators.
imagem_completa.exibir()


# Exibe uma separação visual no terminal.
print("\n=== DIMENSÕES DA IMAGEM ===\n")


# Obtém as dimensões através da composição completa de Decorators.
largura, altura = imagem_completa.dimensoes()


# Exibe as dimensões obtidas.
print(f"Dimensões finais: {largura}x{altura}")