# Importa o decorator dataclass, que simplifica a criação de classes de dados.
from dataclasses import dataclass, field


# Define uma dataclass e exige que seus argumentos sejam nomeados.
@dataclass(kw_only=True)
class Relatorio:

    # Define o título obrigatório do relatório.
    titulo: str

    # Define o autor obrigatório do relatório.
    autor: str

    # Define o logo como opcional.
    # O valor padrão None significa que nenhum logo foi informado.
    logo: str | None = None

    # Define se o relatório terá sumário.
    # Por padrão, o sumário não será criado.
    sumario: bool = False

    # Cria uma lista de imagens.
    # default_factory evita compartilhar a mesma lista entre objetos.
    imagens: list[str] = field(default_factory=list)

    # Define se o relatório terá miniaturas.
    # Por padrão, as miniaturas ficam desativadas.
    miniaturas: bool = False

    # Define uma marca d'água opcional.
    # None significa que nenhuma marca d'água foi informada.
    marca_dagua: str | None = None

    # Método executado automaticamente depois da criação do objeto.
    def __post_init__(self):

        # Verifica se miniaturas foram solicitadas sem que existam imagens.
        if self.miniaturas and not self.imagens:

            # Impede a criação de um objeto inválido.
            raise ValueError(
                "miniaturas exigem imagens"
            )


# Cria um relatório utilizando argumentos nomeados.
relatorio = Relatorio(
    titulo="NGC 4654",
    autor="Dra. Silva",
    sumario=True,
    imagens=["hubble_001"],
    miniaturas=True
)


# Esta chamada produziria TypeError porque os argumentos precisam ser nomeados.
# Relatorio("NGC 4654", "Dra. Silva")