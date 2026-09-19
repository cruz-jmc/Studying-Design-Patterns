import conexao # Importa o módulo conexao.
import exportador # Importa o módulo exportador.
import processador # Importa o módulo processador.


# Define algumas imagens fictícias para o exemplo.
imagens = ["hubble_001.fits", "andromeda.tiff"]


# Utiliza a função exportar.
exportador.exportar(imagens)

# Utiliza a função processar.
processador.processar(imagens)


# Importa o módulo sys para acessar os módulos carregados.
import sys


# Verifica se a referência armazenada em sys.modules["conexao"] é exatamente o mesmo objeto que a variável conexao.
print(sys.modules["conexao"] is conexao)