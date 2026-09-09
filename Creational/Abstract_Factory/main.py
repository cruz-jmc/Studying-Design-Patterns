# Importa a fábrica concreta da família Material.
from fabrica_material import FabricaMaterial

# Importa a fábrica concreta da família Cupertino.
from fabrica_cupertino import FabricaCupertino

# Importa a abstração da fábrica.
from fabrica_widgets import FabricaWidgets


# Define uma função responsável por montar uma tela.
# A função recebe uma fábrica, mas não depende de uma fábrica concreta.
def montar_tela(fabrica: FabricaWidgets) -> None:

    # Solicita à fábrica um botão.
    # O cliente não sabe qual botão concreto será criado.
    botao = fabrica.criar_botao("confirmar")

    # Solicita à fábrica um checkbox.
    # Novamente, o cliente não sabe qual implementação será utilizada.
    checkbox = fabrica.criar_checkbox("Lembrar de mim")

    # Renderiza o botão criado pela fábrica.
    print(botao.renderizar())

    # Renderiza o checkbox criado pela fábrica.
    print(checkbox.renderizar())


# Cria um dicionário contendo as fábricas disponíveis.
# A chave identifica a plataforma.
# O valor é a fábrica responsável por aquela família de produtos.
FABRICAS = {

    # Associa "android" à fábrica Material.
    "android": FabricaMaterial(),

    # Associa "ios" à fábrica Cupertino.
    "ios": FabricaCupertino()
}


# Solicita a fábrica Material ao dicionário.
# Depois passa essa fábrica para montar_tela().
montar_tela(FABRICAS["android"])


# Imprime uma linha separadora para facilitar a visualização da saída.
print("---")


# Solicita a fábrica Cupertino ao dicionário.
# A mesma função montar_tela() é utilizada novamente.
montar_tela(FABRICAS["ios"])