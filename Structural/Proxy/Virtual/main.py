# Importamos o Proxy.
# O cliente trabalhará inicialmente apenas com o Proxy.
from proxy_imagem import ProxyImagem


# Criamos uma função para representar
# a abertura de uma galeria de imagens.
def abrir_galeria(imagens: list[ProxyImagem]) -> None:


    # Percorremos todas as imagens da galeria.
    for imagem in imagens:


        # Exibimos apenas uma miniatura conceitual.
        #
        # Para isso precisamos apenas das dimensões.
        # Não precisamos carregar o arquivo pesado.
        print(
            f"miniatura: "
            f"{imagem.caminho} "
            f"{imagem.dimensoes()}"
        )


# Criamos uma lista contendo várias imagens.
#
# Observe que estamos criando Proxies,
# e não ImagemAltaResolucao diretamente.
galeria = [

    # Criamos o Proxy da primeira imagem.
    ProxyImagem(
        "hubble_001.fits",
        8192,
        8192
    ),


    # Criamos o Proxy da segunda imagem.
    ProxyImagem(
        "hubble_002.fits",
        8192,
        8192
    ),


    # Criamos o Proxy da terceira imagem.
    ProxyImagem(
        "hubble_003.fits",
        8192,
        8192
    )
]


# Abrimos a galeria.
#
# Nesse momento apenas mostramos informações
# sobre as imagens.
abrir_galeria(galeria)


# Informamos que o usuário deseja abrir
# a segunda imagem.
print("\nUsuário selecionou a segunda imagem.\n")


# Pedimos para exibir a segunda imagem.
#
# Nesse momento o Proxy percebe que
# a imagem real ainda não existe.
#
# Então ele cria ImagemAltaResolucao,
# carrega o arquivo e exibe a imagem.
galeria[1].exibir()


# Informamos que o usuário deseja abrir
# novamente a mesma imagem.
print("\nUsuário abriu novamente a segunda imagem.\n")


# Chamamos novamente o método exibir().
galeria[1].exibir()