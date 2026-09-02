# Flyweight - Reference: <https://refactoring.guru/pt-br/design-patterns/flyweight>

## 📌 Objetivo

O **Flyweight** é um Design Pattern **estrutural** utilizado para **reduzir o consumo de memória quando uma aplicação precisa trabalhar com uma grande quantidade de objetos semelhantes**.

A ideia central do padrão é:

> **Em vez de armazenar repetidamente os mesmos dados em milhares ou milhões de objetos, compartilhamos esses dados entre os objetos que possuem informações em comum.**

Em outras palavras:

```text
Muitos objetos
      |
      v
Possuem dados repetidos
      |
      v
Separar o que muda
do que não muda
      |
      v
Compartilhar os dados
imutáveis e repetidos
```

O Flyweight é especialmente útil quando temos situações como:

- milhões de objetos;
- objetos muito semelhantes;
- grande quantidade de dados repetidos;
- consumo excessivo de memória;
- informações que podem ser compartilhadas com segurança.

---

# ❗ Problema

Imagine que estamos desenvolvendo um sistema para visualizar e analisar um grande catálogo de estrelas obtido por um telescópio espacial, como o Hubble.

O catálogo possui:

```text
Milhões de estrelas
```

Cada estrela precisa possuir informações como:

```text
Posição X

Posição Y

Tipo espectral

Cor RGB

Textura

Curva de luminosidade

Referência para o catálogo
```

Uma primeira implementação poderia criar uma classe como:

```python
class Estrela:

    def __init__(
        self,
        x,
        y,
        tipo_espectral,
        cor_rgb,
        textura,
        curva_luminosidade,
        catalogo_ref
    ):
        self.x = x
        self.y = y
        self.tipo_espectral = tipo_espectral
        self.cor_rgb = cor_rgb
        self.textura = textura
        self.curva_luminosidade = curva_luminosidade
        self.catalogo_ref = catalogo_ref
```

Depois, para criar milhões de estrelas:

```python
estrelas = [
    Estrela(
        x,
        y,
        "G",
        (255, 244, 234),
        textura_g,
        curva_g,
        "MK"
    )
    for x, y in posicoes
]
```

Inicialmente, isso parece perfeitamente razoável.

Porém, existe um problema importante.

---

# 💥 Onde está o desperdício?

Nem todas as informações de uma estrela realmente precisam ser armazenadas individualmente.

Observe os campos:

| Campo                | Tamanho aproximado | Varia para cada estrela?        |
| -------------------- | ------------------ | ------------------------------- |
| `x, y`               | 56 B               | Sim                             |
| `tipo_espectral`     | ~50 B              | Apenas alguns valores possíveis |
| `cor_rgb`            | ~72 B              | Derivado do tipo                |
| `textura`            | 12 KB              | Não                             |
| `curva_luminosidade` | 8 KB               | Não                             |
| `catalogo_ref`       | ~60 B              | Pode ser compartilhado          |

Agora imagine:

```text
2.000.000 de estrelas
```

Suponha que todas as estrelas do mesmo tipo espectral utilizem:

```text
A mesma textura

A mesma curva de luminosidade

A mesma configuração de cor
```

Uma implementação ingênua poderia armazenar essas informações repetidamente:

```text
Estrela 1
├── x
├── y
├── tipo G
├── textura G
├── curva G
└── catálogo MK


Estrela 2
├── x
├── y
├── tipo G
├── textura G
├── curva G
└── catálogo MK


Estrela 3
├── x
├── y
├── tipo G
├── textura G
├── curva G
└── catálogo MK
```

E assim por diante:

```text
2.000.000 vezes
```

Mas surge uma pergunta importante:

> Por que armazenar milhões de cópias da mesma textura se elas possuem exatamente o mesmo conteúdo?

Ou:

> Por que cada estrela precisa possuir sua própria cópia da curva de luminosidade se milhares de estrelas podem utilizar a mesma curva?

É exatamente esse tipo de problema que o **Flyweight** busca resolver.

---

# 🔴 O problema conceitual

O problema não é necessariamente possuir muitos objetos.

Ter muitos objetos não é, por si só, um problema.

O problema acontece quando temos:

```text
Muitos objetos
+
Grande quantidade de dados repetidos
=
Desperdício de memória
```

Podemos representar assim:

```text
Estrela 1 ─── possui ───> Textura G
Estrela 2 ─── possui ───> Textura G
Estrela 3 ─── possui ───> Textura G
Estrela 4 ─── possui ───> Textura G
Estrela 5 ─── possui ───> Textura G
```

Em uma implementação tradicional, poderíamos acabar criando:

```text
Textura G #1

Textura G #2

Textura G #3

Textura G #4

Textura G #5
```

Mesmo que todas sejam iguais.

Isso significa:

```text
Mesma informação
+
Muitas cópias
+
Milhões de objetos
=
Grande desperdício de memória
```

---

# 💡 A ideia do Flyweight

A solução é separar os dados de um objeto em duas categorias:

```text
Estado intrínseco
```

e:

```text
Estado extrínseco
```

Essa separação é a ideia mais importante para compreender o Flyweight.

---

# 🧠 Estado Intrínseco

O **estado intrínseco** representa os dados que podem ser:

- compartilhados;
- reutilizados;
- armazenados fora dos objetos individuais;
- normalmente imutáveis.

No nosso exemplo, podemos considerar:

```text
Tipo espectral

Cor RGB

Textura

Curva de luminosidade
```

Por exemplo:

```text
Tipo: G

Cor: (255, 244, 234)

Textura: textura_g

Curva: curva_g
```

Essas informações podem ser compartilhadas por diversas estrelas.

Portanto:

```text
Estrela A ──┐
            │
Estrela B ──┼──> TipoEstrela G
            │
Estrela C ──┘
```

Em vez de:

```text
Estrela A -> cópia de TipoEstrela G

Estrela B -> cópia de TipoEstrela G

Estrela C -> cópia de TipoEstrela G
```

utilizamos:

```text
               +----------------+
               | TipoEstrela G  |
               +----------------+
                      ^
                      |
          +-----------+-----------+
          |           |           |
          |           |           |
       Estrela A   Estrela B   Estrela C
```

Um único objeto pode representar os dados compartilhados.

---

# 📍 Estado Extrínseco

O **estado extrínseco** representa os dados que variam entre os objetos.

No exemplo das estrelas:

```text
Posição X

Posição Y

Tamanho
```

Cada estrela pode estar localizada em uma posição diferente.

Por exemplo:

```text
Estrela A

x = 10
y = 20
```

```text
Estrela B

x = 300
y = 450
```

```text
Estrela C

x = 900
y = 100
```

Essas informações não podem ser compartilhadas.

Portanto:

```text
Estado extrínseco
=
dados específicos de cada objeto
```

---

# 🔄 Separando os estados

Antes do Flyweight, uma estrela poderia possuir tudo:

```text
Estrela

├── x
├── y
├── tipo espectral
├── cor
├── textura
├── curva de luminosidade
└── catálogo
```

Com Flyweight, separamos:

```text
Estado específico
```

de:

```text
Estado compartilhável
```

A estrutura passa a ser:

```text
EstrelaNaImagem

├── x
├── y
├── tamanho
└── referência para TipoEstrela
```

E:

```text
TipoEstrela

├── tipo espectral
├── cor RGB
├── textura
└── curva de luminosidade
```

Visualmente:

```text
EstrelaNaImagem
      |
      | referência
      v
+----------------------+
|     TipoEstrela      |
+----------------------+
| tipo_espectral       |
| cor_rgb              |
| textura              |
| curva_luminosidade   |
+----------------------+
```

Agora várias estrelas podem compartilhar o mesmo objeto.

---

# 🌟 Aplicando ao exemplo

Suponha que existam apenas:

```text
7 tipos espectrais
```

Por exemplo:

```text
O

B

A

F

G

K

M
```

Mas o catálogo possui:

```text
2.000.000 de estrelas
```

Sem Flyweight:

```text
2.000.000 objetos

cada um contendo:

textura

curva

cor

tipo
```

Com Flyweight:

```text
2.000.000 objetos leves
```

contendo apenas:

```text
posição

tamanho

referência para um Flyweight
```

Enquanto os dados compartilhados podem existir apenas:

```text
7 vezes
```

Uma para cada tipo.

---

# 💡 Solução com Flyweight

Podemos criar uma classe para representar os dados compartilháveis.

Por exemplo:

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TipoEstrela:

    tipo_espectral: str
    cor_rgb: tuple[int, int, int]
    textura: bytes
    curva: bytes

    def desenhar(self, tela: str, x: float, y: float) -> None:
        print(
            f"[{tela}] "
            f"{self.tipo_espectral} "
            f"rgb={self.cor_rgb} "
            f"em ({x:.1f}, {y:.1f})"
        )
```

Essa classe representa o:

```text
Flyweight
```

Ela armazena os dados que podem ser compartilhados.

---

# 🧊 Por que o Flyweight deve ser imutável?

Imagine que temos:

```text
1 objeto TipoEstrela
```

sendo compartilhado por:

```text
100.000 estrelas
```

Se alguém fizer:

```text
Alterar textura
```

todas as estrelas que compartilham esse objeto seriam afetadas.

Por isso, normalmente queremos que o Flyweight seja:

```text
Imutável
```

No Python, podemos representar isso com:

```python
@dataclass(frozen=True)
```

A palavra:

```text
frozen=True
```

indica que, depois de criado, o objeto não deve ser modificado.

A ideia é:

```text
Criar Flyweight
       |
       v
Compartilhar
       |
       v
Nunca alterar
```

Isso evita problemas como:

```text
Objeto compartilhado alterado
          |
          v
Todos os objetos afetados
```

---

# 🏭 O papel da Flyweight Factory

Agora surge uma nova pergunta:

> Como garantir que não criaremos vários Flyweights iguais?

Imagine que o sistema faça:

```python
TipoEstrela("G", ...)
```

diversas vezes.

Poderíamos acabar criando:

```text
TipoEstrela G #1

TipoEstrela G #2

TipoEstrela G #3
```

Isso destruiria parte do benefício do padrão.

Por isso, normalmente utilizamos uma:

```text
Flyweight Factory
```

A Factory é responsável por:

- criar Flyweights;
- armazená-los;
- reutilizá-los;
- garantir que objetos equivalentes sejam compartilhados.

---

# 🏭 FabricaDeTipos

Podemos criar uma fábrica como:

```python
class FabricaDeTipos:

    _cache: dict[str, TipoEstrela] = {}
```

Esse atributo representa um:

```text
cache
```

Mas é importante entender que, nesse contexto, ele possui uma função específica.

A fábrica mantém os Flyweights criados:

```text
Cache

"G" -> TipoEstrela G

"K" -> TipoEstrela K

"M" -> TipoEstrela M
```

Quando alguém solicita:

```text
Tipo G
```

a fábrica verifica:

```text
O Flyweight já existe?
```

Se existir:

```text
Retornar o existente
```

Caso contrário:

```text
Criar
+
Armazenar
+
Retornar
```

---

# 🔄 Funcionamento da Factory

O fluxo pode ser representado assim:

```text
Cliente solicita TipoEstrela("G")
                |
                v
        FabricaDeTipos
                |
                v
        "G" está no cache?
             /        \
           Não         Sim
            |           |
            v           v
          Criar       Reutilizar
            |           |
            +-----+-----+
                  |
                  v
          Retornar Flyweight
```

Uma implementação poderia ser:

```python
class FabricaDeTipos:

    _cache: dict[str, TipoEstrela] = {}

    _CATALOGO = {
        "O": (15, 176, 255),
        "B": (170, 191, 255),
        "A": (202, 215, 255),
        "F": (248, 247, 255),
        "G": (255, 244, 234),
        "K": (255, 210, 161),
        "M": (255, 204, 111)
    }

    @classmethod
    def obter(cls, tipo: str) -> TipoEstrela:

        if tipo not in cls._cache:

            cls._cache[tipo] = TipoEstrela(
                tipo_espectral=tipo,
                cor_rgb=cls._CATALOGO[tipo],
                textura=b"\x00" * 128,
                curva=b"\x00" * 8192
            )

        return cls._cache[tipo]

    @classmethod
    def total_criados(cls) -> int:

        return len(cls._cache)
```

---

# 🧠 O que acontece nessa Factory?

Quando fazemos:

```python
tipo_g = FabricaDeTipos.obter("G")
```

a fábrica verifica:

```text
"G" já existe?
```

Se não existir:

```text
Criar TipoEstrela G
```

Depois:

```text
Armazenar no cache
```

Assim:

```text
_cache

"G" -> TipoEstrela G
```

Se depois fizermos novamente:

```python
outro_tipo_g = FabricaDeTipos.obter("G")
```

não é necessário criar outro objeto.

A Factory simplesmente retorna:

```text
O mesmo TipoEstrela G
```

Portanto:

```text
tipo_g
   |
   v

+---------------+
| TipoEstrela G |
+---------------+
   ^
   |
outro_tipo_g
```

Os dois podem apontar para o mesmo objeto.

---

# ⭐ Representando cada estrela

Agora podemos criar uma classe mais leve.

Por exemplo:

```python
class EstrelaNaImagem:

    __slots__ = ("_x", "_y", "_tipo")

    def __init__(
        self,
        x: float,
        y: float,
        tipo: TipoEstrela
    ):
        self._x = x
        self._y = y
        self._tipo = tipo

    def desenhar(self, tela: str) -> None:
        self._tipo.desenhar(
            tela,
            self._x,
            self._y
        )
```

Essa classe não precisa possuir:

```text
Textura

Curva

Cor

Tipo espectral
```

diretamente.

Ela possui:

```text
x

y

referência para TipoEstrela
```

Portanto:

```text
EstrelaNaImagem

+-------------------+
| x                 |
| y                 |
| tipo ----------+  |
+-------------------+
                 |
                 v
        +------------------+
        | TipoEstrela      |
        +------------------+
        | tipo espectral   |
        | cor              |
        | textura          |
        | curva            |
        +------------------+
```

---

# 🔗 Compartilhando o Flyweight

Agora imagine:

```python
tipo_g = FabricaDeTipos.obter("G")
```

Depois:

```python
estrela_1 = EstrelaNaImagem(10, 20, tipo_g)

estrela_2 = EstrelaNaImagem(100, 250, tipo_g)

estrela_3 = EstrelaNaImagem(900, 450, tipo_g)
```

A estrutura será:

```text
Estrela 1
    |
    v

    Tipo G <----------- Estrela 2
    ^                       |
    |                       v
    +------------------- Estrela 3
```

Ou visualmente:

```text
+-------------+
| Estrela #1  |
| x = 10      |
| y = 20      |
+------+------+
       |
       |
       v

       +--------------------+
       |   TipoEstrela G    |
       +--------------------+
       | tipo = G           |
       | cor                |
       | textura            |
       | curva              |
       +--------------------+
              ^
              |
       +------+------+
       |             |
+------+------+ +----+------+
| Estrela #2 | | Estrela #3 |
| x = 100    | | x = 900    |
| y = 250    | | y = 450    |
+------------+ +-----------+
```

Os dados pesados são compartilhados.

---

# 🧩 Estrutura conceitual do Flyweight

Podemos representar o padrão assim:

```text
                 Client
                    |
                    v
            FlyweightFactory
                    |
          +---------+---------+
          |                   |
          v                   v
     Flyweight A         Flyweight B
          ^                   ^
          |                   |
     +----+----+         +----+----+
     |         |         |         |
     v         v         v         v

 Context    Context   Context   Context
```

No nosso exemplo:

```text
Cliente
   |
   v

FabricaDeTipos
   |
   +----------------------+
   |                      |
   v                      v

TipoEstrela G       TipoEstrela K
   ^                      ^
   |                      |
   |                      |

Estrela A         Estrela C
Estrela B         Estrela D
```

---

# 🧱 Participantes do Flyweight

O padrão geralmente possui alguns participantes importantes.

---

## 🟢 Flyweight

O Flyweight representa o objeto que contém o estado compartilhável.

No nosso exemplo:

```text
TipoEstrela
```

Ele armazena:

```text
tipo_espectral

cor_rgb

textura

curva
```

A principal característica é:

> O Flyweight deve poder ser compartilhado por diversos objetos.

---

## 🟡 FlyweightFactory

A Factory controla a criação dos Flyweights.

No nosso exemplo:

```text
FabricaDeTipos
```

Sua responsabilidade é:

```text
Solicitação
     |
     v

Flyweight existe?

     |
 +---+---+
 |       |
Não     Sim
 |       |
 v       v

Criar  Reutilizar
 |       |
 +---+---+
     |
     v

Retornar
```

---

## 🔵 Context

O Context representa o objeto que possui o estado específico.

No nosso exemplo:

```text
EstrelaNaImagem
```

Cada estrela possui:

```text
posição

tamanho

referência para o Flyweight
```

Portanto:

```text
Context
=
dados individuais
+
referência para dados compartilhados
```

---

## 👤 Client

O Client é o código responsável por utilizar o sistema.

Por exemplo:

```python
tipo = FabricaDeTipos.obter("G")

estrela = EstrelaNaImagem(
    100,
    200,
    tipo
)
```

O cliente solicita um Flyweight para a Factory e utiliza esse objeto ao criar os Contexts.

---

# 🔄 Fluxo completo

O funcionamento pode ser representado assim:

```text
Cliente
   |
   | solicitar tipo "G"
   v

FabricaDeTipos
   |
   v

"G" existe?
   |
+--+--+
|     |
Não   Sim
|     |
v     v

Criar  Retornar existente
|
v

Armazenar
|
v

Retornar TipoEstrela
|
v

Criar EstrelaNaImagem
```

Depois:

```text
EstrelaNaImagem
       |
       | desenhar()
       v

TipoEstrela
       |
       v

Utilizar estado compartilhado
+
Receber posição específica
```

---

# 🎨 Estado intrínseco e extrínseco no exemplo

Podemos resumir o nosso problema assim:

| Informação            | Tipo de estado |
| --------------------- | -------------- |
| Tipo espectral        | Intrínseco     |
| Cor RGB               | Intrínseco     |
| Textura               | Intrínseco     |
| Curva de luminosidade | Intrínseco     |
| Posição X             | Extrínseco     |
| Posição Y             | Extrínseco     |
| Tamanho               | Extrínseco     |

A separação fica:

```text
Estado Intrínseco

Compartilhado
+
Imutável
+
Flyweight
```

e:

```text
Estado Extrínseco

Individual
+
Variável
+
Context
```

---

# 🧠 Uma forma simples de memorizar

Imagine que temos:

```text
1.000.000 de estrelas
```

Cada estrela possui uma posição diferente:

```text
Estrela 1 -> (10, 20)

Estrela 2 -> (40, 90)

Estrela 3 -> (500, 120)
```

Mas várias possuem o mesmo tipo:

```text
G
```

Portanto:

```text
Posição

Não pode ser compartilhada
```

Mas:

```text
Tipo G

Pode ser compartilhado
```

A lógica é:

```text
O que muda?

Fica no Context.
```

```text
O que se repete?

Pode virar Flyweight.
```

---

# 📦 Exemplo de organização do projeto

Para implementar este exemplo em Python, uma possível estrutura seria:

```text
Flyweight/
│
├── main.py
│
├── tipo_estrela.py
│
├── fabrica_de_tipos.py
│
└── estrela_na_imagem.py
```

Responsabilidades:

### `main.py`

```text
Cliente responsável por criar
e utilizar as estrelas.
```

### `tipo_estrela.py`

```text
Contém o Flyweight.

Armazena o estado intrínseco.
```

### `fabrica_de_tipos.py`

```text
Contém a Flyweight Factory.

Cria e reutiliza os Flyweights.
```

### `estrela_na_imagem.py`

```text
Contém o Context.

Armazena o estado extrínseco
e uma referência para o Flyweight.
```

---

# 🧪 Exemplo de utilização

O `main.py` poderia possuir algo semelhante a:

```python
from fabrica_de_tipos import FabricaDeTipos
from estrela_na_imagem import EstrelaNaImagem


tipo_g = FabricaDeTipos.obter("G")

estrela_1 = EstrelaNaImagem(
    10,
    20,
    tipo_g
)

estrela_2 = EstrelaNaImagem(
    50,
    80,
    tipo_g
)

estrela_3 = EstrelaNaImagem(
    300,
    400,
    tipo_g
)


estrela_1.desenhar("Hubble")
estrela_2.desenhar("Hubble")
estrela_3.desenhar("Hubble")
```

Apesar de existirem três objetos:

```text
EstrelaNaImagem
```

podemos possuir apenas um:

```text
TipoEstrela G
```

Compartilhado.

---

# 🔍 Verificando o compartilhamento

Podemos testar conceitualmente:

```python
tipo_1 = FabricaDeTipos.obter("G")

tipo_2 = FabricaDeTipos.obter("G")
```

Agora:

```python
tipo_1 is tipo_2
```

deve resultar em:

```text
True
```

Isso significa:

```text
tipo_1
```

e:

```text
tipo_2
```

não são apenas objetos com o mesmo conteúdo.

Eles representam:

```text
A mesma instância em memória
```

Visualmente:

```text
tipo_1 ─────┐
            v
       +----------+
       | Tipo G   |
       +----------+
            ^
            |
tipo_2 ─────┘
```

Esse compartilhamento é uma das principais características do Flyweight.

---

# ⚡ Flyweight não é simplesmente Cache

É comum confundir Flyweight com Cache.

Embora uma Factory possa utilizar uma estrutura parecida com um cache:

```python
_cache = {}
```

os conceitos não são exatamente iguais.

---

## 🗃️ Cache

Um Cache normalmente armazena:

```text
Resultados de operações
```

Por exemplo:

```text
Consulta ao banco

Resultado
```

Depois:

```text
Próxima consulta
       |
       v

Resultado já existe?
       |
       v

Retornar resultado armazenado
```

O objetivo principal é:

```text
Evitar trabalho repetido
```

---

## 🪶 Flyweight

O Flyweight possui como objetivo principal:

```text
Compartilhar objetos
```

Para reduzir:

```text
Consumo de memória
```

O foco é:

```text
Evitar múltiplas cópias
dos mesmos dados.
```

Portanto:

```text
Cache

Evita repetir operações.
```

Enquanto:

```text
Flyweight

Evita repetir objetos e dados.
```

Uma Factory de Flyweight pode utilizar uma estrutura de cache para localizar objetos existentes, mas isso não significa que todo cache seja uma implementação do padrão Flyweight.

---

# ⚠️ Por que não simplesmente colocar tudo em uma classe global?

Uma possível pergunta seria:

> Se os dados são compartilhados, por que não simplesmente criar variáveis globais?

Por exemplo:

```python
TEXTURA_G = ...

CURVA_G = ...
```

Isso poderia funcionar em casos muito simples.

Porém, o Flyweight oferece uma estrutura mais organizada.

Podemos representar uma combinação completa de dados como:

```text
TipoEstrela G

├── cor
├── textura
└── curva
```

A Factory também pode garantir:

```text
Solicitou G?
```

Então:

```text
Retornar o Flyweight correspondente.
```

Isso permite encapsular os dados relacionados.

---

# 📊 Comparando antes e depois

## ❌ Sem Flyweight

```text
2.000.000 estrelas
```

Cada uma possui:

```text
posição

+

tipo

+

cor

+

textura

+

curva
```

Resultado:

```text
Milhões de cópias
de dados semelhantes.
```

---

## ✅ Com Flyweight

```text
2.000.000 estrelas
```

Cada uma possui apenas:

```text
posição

+

referência para o tipo
```

Enquanto:

```text
TipoEstrela G

TipoEstrela K

TipoEstrela M

...
```

são compartilhados.

Resultado:

```text
Menos memória
```

e:

```text
Menos duplicação
```

---

# 🎯 Quando utilizar Flyweight?

O Flyweight é especialmente útil quando:

- a aplicação precisa criar uma quantidade muito grande de objetos;
- muitos objetos possuem informações idênticas;
- existe um estado que pode ser compartilhado;
- o consumo de memória está se tornando um problema;
- o estado compartilhado pode ser separado do estado individual;
- os objetos compartilhados podem permanecer imutáveis.

Exemplos comuns incluem:

```text
Editores de texto

Caracteres em documentos

Jogos

Árvores em mapas

Partículas

Sprites

Ícones

Objetos gráficos

Sistemas geográficos

Catálogos astronômicos

Objetos de interfaces gráficas
```

---

# 🌳 Exemplo: árvores em um jogo

Imagine um mapa com:

```text
1.000.000 de árvores
```

Cada árvore possui:

```text
posição X

posição Y
```

Mas muitas árvores possuem o mesmo:

```text
modelo 3D

textura

animação
```

Sem Flyweight:

```text
Árvore 1 -> modelo completo

Árvore 2 -> modelo completo

Árvore 3 -> modelo completo

Árvore 4 -> modelo completo
```

Com Flyweight:

```text
Árvore 1 ──┐
Árvore 2 ──┼──> Modelo de Carvalho
Árvore 3 ──┤
Árvore 4 ──┘
```

Cada árvore possui sua própria posição.

Mas o modelo pode ser compartilhado.

---

# 📝 Flyweight e imutabilidade

Uma regra extremamente importante é:

> **Se um objeto será compartilhado por vários Contexts, alterações nesse objeto podem afetar todos eles.**

Imagine:

```text
Estrela A
    |
    v

Tipo G <----- Estrela B
```

Agora alguém altera:

```text
Tipo G -> cor vermelha
```

Automaticamente:

```text
Estrela A

e

Estrela B
```

seriam afetadas.

Por isso:

```text
Flyweight
```

deve, sempre que possível, ser:

```text
Imutável
```

No nosso exemplo:

```python
@dataclass(frozen=True)
```

é uma forma de representar essa intenção.

---

# 🧠 `__slots__` no Context

No exemplo, podemos utilizar:

```python
__slots__ = ("_x", "_y", "_tipo")
```

Isso também é interessante porque estamos trabalhando com:

```text
Milhões de objetos
```

Em Python, objetos normalmente possuem estruturas internas que permitem armazenar atributos dinamicamente.

Quando sabemos antecipadamente quais atributos uma classe possuirá, `__slots__` pode ajudar a reduzir a sobrecarga de memória por instância.

No nosso caso:

```text
EstrelaNaImagem
```

sempre possui:

```text
_x

_y

_tipo
```

Portanto:

```python
__slots__ = ("_x", "_y", "_tipo")
```

reforça a ideia de que estamos tentando criar objetos individuais mais leves.

---

# 🧱 Estrutura geral do padrão

Podemos representar a estrutura clássica assim:

```text
                    Client
                       |
                       v
               FlyweightFactory
                       |
                       |
             +---------+---------+
             |                   |
             v                   v

        Flyweight A         Flyweight B
             ^                   ^
             |                   |
             |                   |

         Context A           Context C
         Context B           Context D
```

No nosso exemplo:

```text
                   Cliente
                      |
                      v

               FabricaDeTipos
                      |
           +----------+----------+
           |                     |
           v                     v

      TipoEstrela G         TipoEstrela K
           ^                     ^
           |                     |
           |                     |

     Estrela 1              Estrela 3
     Estrela 2              Estrela 4
```

---

# 🧠 Participantes do Flyweight

| Participante         | Exemplo           | Responsabilidade                    |
| -------------------- | ----------------- | ----------------------------------- |
| **Flyweight**        | `TipoEstrela`     | Armazena o estado compartilhado     |
| **FlyweightFactory** | `FabricaDeTipos`  | Cria e reutiliza Flyweights         |
| **Context**          | `EstrelaNaImagem` | Armazena o estado individual        |
| **Client**           | `main.py`         | Solicita Flyweights e cria Contexts |

---

# 🆚 Flyweight × Objetos tradicionais

## Sem Flyweight

```text
Objeto 1

[ Dados únicos ]
[ Dados repetidos ]
[ Dados repetidos ]
[ Dados repetidos ]


Objeto 2

[ Dados únicos ]
[ Dados repetidos ]
[ Dados repetidos ]
[ Dados repetidos ]


Objeto 3

[ Dados únicos ]
[ Dados repetidos ]
[ Dados repetidos ]
[ Dados repetidos ]
```

---

## Com Flyweight

```text
Objeto 1 ──┐
Objeto 2 ──┼──> [ Dados compartilhados ]
Objeto 3 ──┘
```

Cada objeto mantém apenas:

```text
Seus próprios dados
```

E referencia:

```text
Os dados compartilhados
```

---

# ⚖️ Prós e Contras

## 🟢 Prós

- reduz significativamente o consumo de memória;
- evita duplicação de dados;
- permite compartilhar objetos entre diversas instâncias;
- pode melhorar a eficiência de aplicações com muitos objetos;
- organiza claramente dados compartilhados e dados individuais;
- reduz a quantidade de objetos pesados;
- pode funcionar muito bem em sistemas gráficos e jogos.

---

## 🔴 Contras

- aumenta a complexidade do projeto;
- exige identificar corretamente o estado intrínseco e extrínseco;
- Flyweights compartilhados devem ser tratados cuidadosamente;
- objetos compartilhados mutáveis podem causar efeitos inesperados;
- pode não trazer benefícios quando existem poucos objetos;
- pode adicionar indireção ao acessar dados;
- nem todo dado repetido deve automaticamente virar um Flyweight.

---

# 🚫 Quando não utilizar Flyweight?

O Flyweight pode ser desnecessário quando:

- a aplicação possui poucos objetos;
- os objetos são pequenos;
- os dados não são repetidos;
- o consumo de memória não representa um problema;
- separar estado intrínseco e extrínseco torna o código excessivamente complexo.

Por exemplo:

```text
500 objetos pequenos
```

provavelmente não justificam uma arquitetura adicional apenas para utilizar Flyweight.

O padrão normalmente começa a fazer sentido quando temos:

```text
Dezenas de milhares

Centenas de milhares

Milhões de objetos
```

e existe uma quantidade significativa de dados repetidos.

---

# ⚠️ Flyweight não é uma otimização obrigatória

É importante não utilizar Flyweight simplesmente porque:

```text
"O padrão existe"
```

O padrão resolve um problema específico:

```text
Grande quantidade de objetos

+

Grande quantidade de estado compartilhável

+

Pressão de memória
```

Se esse problema não existir:

```text
Flyweight

=

Complexidade desnecessária
```

---

# 📌 Exemplo-problema deste projeto

Neste projeto será implementado um sistema simplificado de visualização de um catálogo astronômico.

O sistema deverá representar:

```text
Milhões de estrelas
```

Cada estrela possuirá informações individuais, como:

```text
Posição X

Posição Y

Tamanho
```

Além disso, cada estrela estará associada a um tipo espectral:

```text
O

B

A

F

G

K

M
```

Cada tipo espectral possuirá informações compartilhadas:

```text
Cor RGB

Textura

Curva de luminosidade
```

A estrutura desejada será:

```text
                    Cliente
                       |
                       v

                FabricaDeTipos
                       |
                       v

                 TipoEstrela
                /      |      \
               /       |       \
              v        v        v

          Estrela    Estrela   Estrela
             |          |         |
             v          v         v

          posição    posição   posição
```

---

# 🎯 Objetivo da implementação

A implementação deverá demonstrar que:

```text
Milhões de estrelas
```

podem compartilhar:

```text
Poucos objetos TipoEstrela
```

Por exemplo:

```text
2.000.000 estrelas
```

mas apenas:

```text
7 Flyweights
```

representando os tipos espectrais.

A ideia é transformar conceitualmente:

```text
2.000.000 objetos pesados
```

em:

```text
2.000.000 Contexts leves

+

7 Flyweights compartilhados
```

---

# 🧠 Ideia principal para memorizar

A ideia central do Flyweight pode ser resumida assim:

```text
Muitos objetos semelhantes
          |
          v
Existe informação repetida?
          |
       +--+--+
       |     |
      Não   Sim
       |     |
       v     v

Manter   Separar dados
normal   compartilháveis
              |
              v

          Flyweight
              |
              v

      Compartilhar entre
        vários objetos
```

Portanto:

> **Flyweight = compartilhar o estado comum entre muitos objetos para reduzir o consumo de memória.**

No exemplo das estrelas:

```text
Cada estrela possui:

Posição própria
```

mas pode compartilhar:

```text
Tipo

Cor

Textura

Curva
```

Visualmente:

```text
Estrela A ──┐
Estrela B ──┤
Estrela C ──┼──> TipoEstrela G
Estrela D ──┤
Estrela E ──┘
```

Em vez de:

```text
Estrela A -> Tipo G próprio

Estrela B -> Tipo G próprio

Estrela C -> Tipo G próprio

Estrela D -> Tipo G próprio

Estrela E -> Tipo G próprio
```

utilizamos:

```text
Um objeto compartilhado
```

para representar o estado comum.

---

# 🧠 Resumo final

O **Flyweight** é um padrão estrutural utilizado principalmente para reduzir o consumo de memória em aplicações que trabalham com uma grande quantidade de objetos semelhantes.

Sua principal estratégia é separar os dados em:

```text
Estado Intrínseco
```

que é:

```text
Compartilhável
+
Normalmente imutável
+
Armazenado no Flyweight
```

e:

```text
Estado Extrínseco
```

que é:

```text
Específico
+
Individual
+
Armazenado no Context
```

Uma Factory é normalmente utilizada para:

```text
Criar Flyweights
+
Armazená-los
+
Reutilizá-los
```

No exemplo deste projeto:

```text
EstrelaNaImagem
```

representará o objeto individual e armazenará informações como:

```text
posição

tamanho
```

Enquanto:

```text
TipoEstrela
```

representará o Flyweight e armazenará:

```text
tipo espectral

cor

textura

curva de luminosidade
```

A Factory:

```text
FabricaDeTipos
```

garantirá que várias estrelas possam compartilhar o mesmo Flyweight.

A ideia mais importante para memorizar é:

> **O Flyweight evita criar várias cópias dos mesmos dados, permitindo que muitos objetos compartilhem um único estado comum e imutável.**
