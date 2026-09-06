# Importa a Factory responsável por criar e reutilizar Flyweights.
from fabrica_de_tipos import FabricaDeTipos

# Importa a classe que representa uma estrela individual.
from estrela_na_imagem import EstrelaNaImagem


# Solicita à Factory o Flyweight correspondente ao tipo G.
# Se ele já existir, a Factory reutilizará o objeto existente.
# Se não existir, a Factory criará o objeto.
tipo_g = FabricaDeTipos.obter("G")


# Cria a primeira estrela.
# A posição (10, 20) pertence exclusivamente a esta estrela.
# O tipo_g é compartilhado e representa seu estado intrínseco.
estrela_1 = EstrelaNaImagem(
    10,
    20,
    tipo_g
)


# Cria a segunda estrela.
# Ela possui uma posição diferente.
# Porém, utiliza exatamente o mesmo Flyweight tipo_g.
estrela_2 = EstrelaNaImagem(
    50,
    80,
    tipo_g
)


# Cria a terceira estrela.
# Novamente temos uma posição diferente.
# Entretanto, ela também reutiliza o mesmo TipoEstrela G.
estrela_3 = EstrelaNaImagem(
    300,
    400,
    tipo_g
)


# Solicita que a primeira estrela seja desenhada na tela Hubble.
estrela_1.desenhar("Hubble")


# Solicita que a segunda estrela seja desenhada na tela Hubble.
estrela_2.desenhar("Hubble")


# Solicita que a terceira estrela seja desenhada na tela Hubble.
estrela_3.desenhar("Hubble")


# Solicita novamente o Flyweight G à Factory.
# Como o objeto já existe no cache, nenhum novo TipoEstrela será criado.
outro_tipo_g = FabricaDeTipos.obter("G")


# Verifica se tipo_g e outro_tipo_g são exatamente a mesma instância.
# O resultado esperado é True.
print(tipo_g is outro_tipo_g)


# Exibe quantos Flyweights foram criados pela Factory.
# Como só solicitamos o tipo G, o resultado esperado é 1.
print(FabricaDeTipos.total_criados())