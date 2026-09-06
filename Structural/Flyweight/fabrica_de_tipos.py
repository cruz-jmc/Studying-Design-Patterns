# Importa a classe TipoEstrela do arquivo tipo_estrela.py.
# Essa classe será utilizada para criar os Flyweights.
from tipo_estrela import TipoEstrela


# Declara a classe responsável por criar e reutilizar os Flyweights.
class FabricaDeTipos:

    # Cria um dicionário que funcionará como cache dos Flyweights.
    # A chave será uma string, como "G" ou "K".
    # O valor será o objeto TipoEstrela correspondente.
    _cache: dict[str, TipoEstrela] = {}

    # Define um catálogo com as cores RGB de cada tipo espectral.
    # Essas informações pertencem ao estado intrínseco.
    _CATALOGO = {

        # Define a cor RGB para estrelas do tipo O.
        "O": (155, 176, 255),

        # Define a cor RGB para estrelas do tipo B.
        "B": (170, 191, 255),

        # Define a cor RGB para estrelas do tipo A.
        "A": (202, 215, 255),

        # Define a cor RGB para estrelas do tipo F.
        "F": (248, 247, 255),

        # Define a cor RGB para estrelas do tipo G.
        "G": (255, 244, 234),

        # Define a cor RGB para estrelas do tipo K.
        "K": (255, 210, 161),

        # Define a cor RGB para estrelas do tipo M.
        "M": (255, 204, 111),
    }

    # @classmethod faz com que o método pertença à classe,
    # e não a uma instância específica da classe.
    @classmethod
    def obter(cls, tipo: str) -> TipoEstrela:

        # Verifica se o tipo solicitado ainda não existe no cache.
        if tipo not in cls._cache:

            # Cria um novo Flyweight e armazena-o no cache.
            cls._cache[tipo] = TipoEstrela(

                # Define o tipo espectral do Flyweight.
                tipo_espectral=tipo,

                # Obtém a cor correspondente ao tipo no catálogo.
                cor_rgb=cls._CATALOGO[tipo],

                # Cria uma representação simplificada da textura.
                # Aqui estamos simulando 12.288 bytes de dados.
                textura=b"\x00" * 12_288,

                # Cria uma representação simplificada da curva.
                # Aqui estamos simulando 8.192 bytes de dados.
                curva=b"\x00" * 8_192
            )

        # Retorna o Flyweight que está no cache.
        # Se ele acabou de ser criado, retorna o novo objeto.
        # Se já existia, retorna exatamente o mesmo objeto.
        return cls._cache[tipo]

    # Define um método para informar quantos Flyweights foram criados.
    @classmethod
    def total_criados(cls) -> int:

        # Retorna a quantidade de elementos existentes no cache.
        return len(cls._cache)