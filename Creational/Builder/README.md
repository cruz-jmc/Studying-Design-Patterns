# 🧱 Builder — Reference: [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/builder)

## 📌 Objetivo

O **Builder** é um Design Pattern **criacional** utilizado para separar a **construção de um objeto complexo** da sua **representação final**.

A ideia principal é permitir que um objeto seja construído **passo a passo**, através de etapas bem definidas, evitando construtores enormes, difíceis de ler e fáceis de utilizar incorretamente.

A definição clássica apresentada pelo **GoF —** ***Design Patterns: Elements of Reusable Object-Oriented Software*** é:

> **"Separe a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações."**

Em termos mais simples:

```text
Objeto complexo
      │
      │ possui muitas configurações
      ▼
Construção passo a passo
      │
      ├── adicionar etapa
      ├── adicionar outra etapa
      ├── adicionar configuração
      └── finalizar
             │
             ▼
       Objeto construído
```

O Builder é especialmente útil quando um objeto possui:

- muitos atributos;
- muitos atributos opcionais;
- diferentes combinações possíveis;
- uma ordem de construção que pode variar;
- regras de validação durante a construção;
- diferentes representações finais.

---

# 🏗️ O Problema

Imagine que estamos desenvolvendo um sistema para um **observatório astronômico**.

O acervo cresceu e agora precisamos gerar diferentes tipos de **relatórios de observação**.

Um relatório pode conter diversas informações:

```text
Relatório
│
├── Título
├── Autor
├── Cabeçalho
├── Logo do observatório
├── Sumário
├── Imagens
├── Miniaturas
├── Metadados
├── Gráficos
├── Rodapé
├── Assinatura
├── Marca d'água
└── Índice
```

O problema é que:

> **Nem todo relatório precisa possuir todas essas características.**

Um relatório simples poderia possuir apenas:

```text
Título
Autor
Conteúdo
```

Enquanto um relatório completo poderia possuir:

```text
Título
Autor
Cabeçalho
Logo
Sumário
Imagens
Miniaturas
Metadados
Gráficos
Rodapé
Assinatura
Marca d'água
Índice
```

Portanto, temos um objeto com muitas possibilidades de configuração.

---

# 🔢 O problema dos muitos parâmetros

Uma primeira tentativa poderia ser criar uma classe `Relatorio` com um construtor que recebe todos os atributos:

```python
class Relatorio:

    def __init__(
        self,
        titulo,
        autor,
        cabecalho,
        logo,
        sumario,
        imagens,
        miniaturas,
        metadados,
        graficos,
        rodape,
        assinatura,
        marca_dagua,
        indice
    ):
        ...
```

O problema aparece rapidamente.

Temos **treze parâmetros**.

Ao criar o objeto, precisamos lembrar:

```text
1  → título
2  → autor
3  → cabeçalho
4  → logo
5  → sumário
6  → imagens
7  → miniaturas
8  → metadados
9  → gráficos
10 → rodapé
11 → assinatura
12 → marca d'água
13 → índice
```

Isso torna o código difícil de ler.

---

# 💥 O problema da ordem dos parâmetros

Imagine uma chamada como:

```python
relatorio = Relatorio(
    "Observação NGC 4654",
    "Dra. Silva",
    True,
    "upe.png",
    True,
    imagens,
    False,
    True,
    None,
    True,
    None,
    True,
    False
)
```

Agora tente responder:

```text
O que significa o False na sétima posição?
```

E:

```text
O que significa o True na décima segunda posição?
```

É necessário conhecer exatamente a ordem dos parâmetros para entender a chamada.

Pior ainda:

```python
Relatorio(
    "Observação NGC 4654",
    "Dra. Silva",
    True,
    "upe.png",
    True,
    imagens,
    True,     # deveria ser False?
    True,
    None,
    True,
    None,
    True,
    False
)
```

A aplicação pode continuar funcionando normalmente.

Porém, o relatório pode estar sendo construído com uma configuração diferente daquela pretendida.

Isso é especialmente perigoso porque:

> **Trocar dois argumentos de posição pode não produzir um erro de implementação.**

O programa pode simplesmente produzir um objeto incorreto.

---

# 🐍 E os argumentos nomeados do Python?

Python possui uma funcionalidade bastante útil:

```text
argumentos nomeados
```

Isso melhora bastante a legibilidade:

```python
Relatorio(
    titulo="Observação NGC 4654",
    autor="Dra. Silva",
    cabecalho=True,
    logo="upe.png",
    sumario=True,
    imagens=imagens,
    miniaturas=False,
    metadados=True,
    graficos=None,
    rodape=True,
    assinatura=None,
    marca_dagua=True,
    indice=False
)
```

Entretanto, quando o objeto é realmente complexo, ainda podemos ter problemas.

A chamada continua enorme.

Além disso, a classe `Relatorio` ainda precisa conhecer toda a lógica de construção e configuração do objeto.

---

# 🚨 O problema do construtor telescópico

Outra solução tradicional é criar parâmetros opcionais com valores padrão:

```python
class Relatorio:

    def __init__(
        self,
        titulo,
        autor,
        cabecalho=True,
        logo=None,
        sumario=False,
        imagens=None,
        miniaturas=False,
        metadados=False,
        graficos=None,
        rodape=True,
        assinatura=None,
        marca_dagua=False,
        indice=False
    ):
        ...
```

Agora podemos criar:

```python
Relatorio(
    "Observação NGC 4654",
    "Dra. Silva"
)
```

ou:

```python
Relatorio(
    "Observação NGC 4654",
    "Dra. Silva",
    cabecalho=True,
    logo="upe.png",
    sumario=True,
    imagens=imagens,
    miniaturas=True,
    metadados=True,
    graficos=graficos,
    rodape=True,
    assinatura="Dra. Silva",
    marca_dagua=True,
    indice=True
)
```

Isso resolve parte do problema.

Porém, ainda temos uma classe cujo construtor precisa conhecer uma grande quantidade de opções.

Esse tipo de solução é frequentemente associado ao chamado:

> **Construtor telescópico.**

Em linguagens como Java ou C#, isso pode aparecer através de vários construtores sobrecarregados.

Conceitualmente:

```text
Relatorio(...)
Relatorio(..., cabecalho)
Relatorio(..., cabecalho, logo)
Relatorio(..., cabecalho, logo, sumario)
Relatorio(..., cabecalho, logo, sumario, imagens)
...
```

À medida que as possibilidades aumentam, a quantidade de combinações pode crescer rapidamente.

---

# 🧮 O problema das combinações

Imagine que cada uma das seguintes características seja opcional:

```text
Cabeçalho
Logo
Sumário
Imagens
Miniaturas
Metadados
Gráficos
Rodapé
Marca d'água
Índice
```

Se tivermos várias opções independentes, o número de combinações possíveis cresce rapidamente.

Por exemplo, com apenas 8 opções booleanas:

```text
2⁸ = 256 combinações
```

Com mais opções, o número cresce ainda mais.

Isso não significa necessariamente que devemos criar uma classe ou construtor para cada combinação.

Na verdade:

> **Essa explosão combinatória é justamente um sinal de que precisamos separar a construção da representação.**

---

# 🚨 Uma solução aparentemente "esperta"

Poderíamos tentar criar subclasses diferentes.

Por exemplo:

```text
Relatorio
│
├── RelatorioInterno
├── RelatorioPublicado
├── RelatorioParceiro
├── RelatorioParceiroSemGraficos
├── RelatorioInternoComIndice
└── ...
```

Inicialmente parece uma solução simples.

Mas imagine que cada característica possa variar independentemente.

Teríamos combinações como:

```text
Com cabeçalho
Sem cabeçalho

Com logo
Sem logo

Com imagens
Sem imagens

Com gráficos
Sem gráficos

Com índice
Sem índice
```

A quantidade de subclasses poderia crescer de forma descontrolada.

---

# 🧬 Herança não deve ser usada para variar configuração

Esse é um ponto importante.

Herança é adequada quando existe uma relação conceitual do tipo:

```text
É um
```

Por exemplo:

```text
Cachorro
    é um
Animal
```

Mas no nosso problema:

```text
Relatório com logo
Relatório sem logo
Relatório com gráficos
Relatório sem gráficos
```

Essas não são necessariamente categorias diferentes de objetos.

São:

> **Configurações diferentes do mesmo tipo de objeto.**

Portanto, criar uma subclasse para cada combinação não é uma boa solução.

O problema não é comportamento diferente.

O problema é:

> **configuração diferente.**

---

# 💡 A ideia do Builder

O Builder propõe separar:

```text
CONSTRUÇÃO
```

de:

```text
REPRESENTAÇÃO
```

Em vez de fazer:

```python
Relatorio(
    titulo,
    autor,
    cabecalho,
    logo,
    sumario,
    imagens,
    miniaturas,
    metadados,
    graficos,
    rodape,
    assinatura,
    marca_dagua,
    indice
)
```

podemos pensar em:

```text
Construtor de Relatório

      │
      ├── definir cabeçalho
      ├── adicionar logo
      ├── adicionar sumário
      ├── adicionar imagens
      ├── adicionar metadados
      ├── adicionar marca d'água
      │
      ▼
   construir()
      │
      ▼
   Relatório
```

Cada etapa possui um nome.

---

# 🧱 Construção passo a passo

A ideia central pode ser representada assim:

```text
Relatório
    │
    ▼
começar construção
    │
    ▼
definir título
    │
    ▼
definir autor
    │
    ▼
adicionar logo
    │
    ▼
adicionar imagens
    │
    ▼
adicionar metadados
    │
    ▼
adicionar marca d'água
    │
    ▼
construir()
    │
    ▼
Relatório pronto
```

Cada etapa representa uma decisão de construção.

Isso torna a utilização muito mais expressiva.

---

# 🧠 A ideia principal

Em vez de perguntar:

```text
Qual é o significado do argumento
na posição 8?
```

podemos escrever algo conceitualmente semelhante a:

```text
com_metadados()
```

Em vez de:

```text
O que significa True?
```

temos:

```text
com_marca_dagua()
```

Em vez de:

```text
O que significa None?
```

podemos simplesmente não executar aquela etapa.

Portanto:

> **As opções deixam de ser valores posicionais e passam a ser etapas nomeadas da construção.**

---

# 🔗 A construção encadeada

Uma das formas mais conhecidas de utilizar Builder é através de chamadas encadeadas.

Conceitualmente:

```python
relatorio = (
    ConstrutorRelatorio("Observação NGC 4654", "Dra. Silva")
        .com_logo("upe.png")
        .com_sumario()
        .com_imagens(imagens, miniaturas=True)
        .com_metadados()
        .com_marca_dagua("RASCUNHO")
        .construir()
)
```

Observe a diferença.

No construtor tradicional:

```python
Relatorio(
    valor,
    valor,
    True,
    valor,
    False,
    valor,
    ...
)
```

No Builder:

```text
com_logo()
com_sumario()
com_imagens()
com_metadados()
com_marca_dagua()
construir()
```

A intenção do código fica muito mais explícita.

---

# 🏗️ Separando as responsabilidades

O Builder separa duas responsabilidades principais.

## Construção

O Builder é responsável por:

```text
Como cada etapa é executada?
```

Por exemplo:

```text
Como adicionar imagens?

Como adicionar metadados?

Como configurar o rodapé?

Como configurar a marca d'água?
```

## Direção da construção

O **Director**, quando utilizado, é responsável por:

```text
Quais etapas devem ser executadas?

Em qual ordem?
```

Essa distinção é importante.

Podemos pensar:

```text
                 Diretor
                    │
                    │ define a sequência
                    ▼
                 Builder
                    │
                    │ executa as etapas
                    ▼
                 Produto
```

---

# 👷 Director

O **Director** é um participante opcional do padrão.

Sua responsabilidade é definir uma sequência de construção.

Por exemplo:

```text
Relatório completo

1. título
2. autor
3. cabeçalho
4. logo
5. sumário
6. imagens
7. metadados
8. gráficos
9. rodapé
10. assinatura
11. índice
```

Outro tipo de relatório poderia utilizar:

```text
Relatório simples

1. título
2. autor
3. imagens
4. rodapé
```

O Director pode encapsular essas receitas.

---

# 👤 Builder sem Director

O Builder **não exige** a existência de um Director.

Esse é um ponto importante.

Podemos ter:

```text
Cliente
   │
   │ executa as etapas
   ▼
Builder
   │
   ▼
Produto
```

Nesse modelo, o próprio cliente decide:

```text
Qual etapa executar?

Qual etapa não executar?

Qual será a ordem?
```

Esse é um uso bastante comum.

---

# 👨‍💼 Builder com Director

Também podemos utilizar:

```text
Cliente
   │
   ▼
Director
   │
   │ define sequência
   ▼
Builder
   │
   │ constrói
   ▼
Produto
```

Nesse caso, o cliente pode dizer:

```text
"Quero um relatório completo."
```

E o Director sabe quais etapas devem ser executadas para construir esse tipo de relatório.

---

# 🔄 A ordem das etapas

Uma característica interessante do Builder é que as etapas podem ser organizadas de maneira explícita.

Por exemplo:

```text
Builder
   │
   ├── título
   ├── autor
   ├── logo
   ├── imagens
   ├── metadados
   └── construir
```

Outro processo poderia utilizar:

```text
Builder
   │
   ├── título
   ├── autor
   ├── metadados
   ├── imagens
   ├── gráficos
   ├── assinatura
   └── construir
```

Dependendo do domínio, determinadas etapas podem ser opcionais ou possuir regras de precedência.

---

# 🧩 Produto

O **Product** é o objeto que queremos construir.

No nosso exemplo:

```text
Produto
   │
   ▼
Relatório
```

Ele representa o relatório final.

Por exemplo:

```text
Relatório
│
├── Título
├── Autor
├── Logo
├── Sumário
├── Imagens
├── Metadados
└── Marca d'água
```

O Product não precisa necessariamente conhecer todos os detalhes de como foi construído.

Essa responsabilidade fica principalmente no Builder.

---

# 🔨 Builder

O **Builder** define as etapas de construção.

No nosso domínio, podemos imaginar operações como:

```text
reiniciar()

com_cabecalho()

com_logo()

com_sumario()

com_imagens()

com_metadados()

com_graficos()

com_rodape()

com_assinatura()

com_marca_dagua()

com_indice()

construir()
```

A ideia não é necessariamente que todos esses métodos existam exatamente dessa forma.

O importante é entender que:

> **Cada método representa uma etapa da construção.**

---

# 🧱 Concrete Builder

O **Concrete Builder** implementa as etapas definidas pelo Builder.

Por exemplo:

```text
Builder
    │
    ├── definir título
    ├── adicionar imagens
    ├── adicionar metadados
    └── construir
```

Um Concrete Builder poderia produzir:

```text
RelatorioPDF
```

Outro poderia produzir:

```text
RelatorioHTML
```

Assim:

```text
                 Builder
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   ConcreteBuilder       ConcreteBuilder
       PDF                    HTML
          │                   │
          ▼                   ▼
    RelatorioPDF        RelatorioHTML
```

Essa possibilidade está diretamente relacionada à intenção do GoF:

> **O mesmo processo de construção pode produzir diferentes representações.**

---

# 📝 O nosso domínio: relatórios de observação

Neste estudo, o objeto complexo será um:

```text
Relatório de observação astronômica
```

Ele poderá possuir diferentes elementos.

Por exemplo:

```text
Relatório
│
├── Título
├── Autor
├── Cabeçalho
├── Logo
├── Sumário
├── Imagens
├── Miniaturas
├── Metadados
├── Gráficos
├── Rodapé
├── Assinatura
├── Marca d'água
└── Índice
```

Nem todos os relatórios precisarão dessas características.

---

# 🔭 Exemplo de relatório simples

Um relatório simples poderia possuir:

```text
Relatório
│
├── Título
├── Autor
└── Imagens
```

Não precisamos necessariamente adicionar:

```text
Logo
Sumário
Gráficos
Marca d'água
Índice
```

---

# 📊 Exemplo de relatório completo

Um relatório mais completo poderia possuir:

```text
Relatório
│
├── Título
├── Autor
├── Cabeçalho
├── Logo
├── Sumário
├── Imagens
├── Miniaturas
├── Metadados
├── Gráficos
├── Rodapé
├── Assinatura
├── Marca d'água
└── Índice
```

A diferença entre os dois relatórios não precisa resultar em duas subclasses.

São apenas:

> **duas configurações diferentes do mesmo produto.**

---

# 🧠 Builder e separação de responsabilidades

Sem Builder:

```text
                 Relatorio
                     │
        ┌────────────┴────────────┐
        │                         │
        │ construção              │ representação
        │                         │
        └────────────┬────────────┘
                     │
                     ▼
              Classe complexa
```

A classe precisa conhecer muitas coisas.

Com Builder:

```text
       Cliente
          │
          ▼
       Builder
          │
          │ constrói
          ▼
       Relatório
          │
          │ representa
          ▼
       Produto
```

A construção fica separada da representação.

---

# 🧠 Builder e o princípio da responsabilidade única

O Builder pode ajudar a aplicar o princípio:

> **Single Responsibility Principle — SRP**

Uma classe de relatório deve representar o relatório.

O Builder pode ficar responsável pela construção desse relatório.

Podemos pensar:

```text
Relatório
    │
    └── Responsabilidade:
        representar o relatório


Builder
    │
    └── Responsabilidade:
        construir o relatório
```

Isso evita concentrar todas as decisões de construção dentro do próprio produto.

---

# 🧠 Builder e validação

Outro benefício possível é centralizar regras de validação durante a construção.

Imagine que um relatório não possa ser construído sem:

```text
Título
```

e:

```text
Autor
```

O processo poderia verificar essas condições antes de produzir o objeto final.

Conceitualmente:

```text
construir()
    │
    ├── título existe?
    │      │
    │      └── não → erro
    │
    ├── autor existe?
    │      │
    │      └── não → erro
    │
    └── tudo válido
           │
           ▼
       Relatório
```

Assim:

> **O produto pode ser entregue ao cliente somente depois que as regras necessárias para sua construção forem satisfeitas.**

Isso não é uma obrigação do Builder, mas é uma aplicação bastante útil do padrão.

---

# 🛡️ Produto válido

Um dos objetivos que podemos buscar no nosso exemplo é:

```text
Builder
   │
   │ configura
   ▼
Validação
   │
   ├── inválido → erro
   │
   └── válido
         │
         ▼
     construir()
         │
         ▼
      Relatório
```

Dessa forma, o objeto final pode ser construído somente quando suas condições necessárias forem atendidas.

---

# 🔁 Builder e diferentes representações

A intenção original do padrão também envolve a possibilidade de produzir diferentes representações.

No nosso domínio, poderíamos imaginar:

```text
                 Builder
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
    Builder PDF          Builder HTML
          │                   │
          ▼                   ▼
    RelatorioPDF        RelatorioHTML
```

O processo conceitual pode ser semelhante:

```text
Título
   ↓
Autor
   ↓
Imagens
   ↓
Metadados
   ↓
Rodapé
   ↓
Construir
```

Mas o resultado final pode possuir representações diferentes.

Por exemplo:

```text
RelatorioPDF
```

ou:

```text
RelatorioHTML
```

---

# 🏗️ Estrutura clássica do Builder

A estrutura clássica pode ser representada assim:

```text
                         Client
                            │
                            │ utiliza
                            ▼
                         Builder
                            ▲
                            │
              ┌─────────────┴─────────────┐
              │                           │
              │ implementa                │
              │                           │
              ▼                           ▼
      ConcreteBuilder 1          ConcreteBuilder 2
              │                           │
              ▼                           ▼
          Product 1                   Product 2


                    Director
                       │
                       │ define
                       ▼
                 sequência de
                  construção
                       │
                       ▼
                    Builder
```

Nem todos os participantes precisam obrigatoriamente existir em toda implementação.

Especialmente:

```text
Director
```

é opcional.

---

# 🧩 Participantes do Builder

## 🔷 Builder

Define as etapas comuns da construção.

Pode declarar operações como:

```text
construir título
adicionar imagens
adicionar metadados
adicionar rodapé
obter resultado
```

---

## 🔨 Concrete Builder

Implementa as etapas do Builder.

É responsável por efetivamente montar o produto.

Pode produzir uma representação específica.

---

## 📦 Product

É o objeto final.

No nosso exemplo:

```text
Relatório
```

Pode representar:

```text
RelatorioPDF
```

ou:

```text
RelatorioHTML
```

ou outra representação.

---

## 👨‍💼 Director

Define uma sequência de construção.

Por exemplo:

```text
Construir relatório completo
```

pode significar:

```text
1. título
2. autor
3. cabeçalho
4. logo
5. sumário
6. imagens
7. metadados
8. gráficos
9. rodapé
10. assinatura
11. índice
```

O Director não precisa conhecer os detalhes internos de cada etapa.

Ele apenas define:

> **Quais etapas devem ser executadas e em qual ordem.**

---

## 👤 Client

É o código que utiliza o Builder.

Pode:

```text
criar um Builder
```

e então:

```text
executar as etapas
```

ou:

```text
pedir ao Director uma determinada receita de construção
```

No nosso estudo, vamos observar principalmente o primeiro caso.

---

# 📊 Participantes no nosso exemplo

| Participante | Exemplo no domínio | Responsabilidade |
|---|---|---|
| **Builder** | `ConstrutorRelatorio` | Define as etapas de construção |
| **Concrete Builder** | `ConstrutorRelatorioPDF` / `ConstrutorRelatorioHTML` | Implementa a construção |
| **Product** | `RelatorioPDF` / `RelatorioHTML` | Representa o resultado final |
| **Director** | `DiretorRelatorio` | Define receitas de construção |
| **Client** | Aplicação | Utiliza o Builder |

Dependendo da implementação escolhida, algumas dessas classes podem não existir.

---

# 🔗 O encadeamento de métodos

Uma característica muito comum nas implementações de Builder é o chamado **fluent interface**.

A ideia é permitir:

```text
builder
   .etapa()
   .outra_etapa()
   .mais_uma_etapa()
   .construir()
```

Visualmente:

```text
Builder
   │
   ▼
etapa 1
   │
   ▼
etapa 2
   │
   ▼
etapa 3
   │
   ▼
construir()
   │
   ▼
Produto
```

Isso torna o código próximo de uma descrição das etapas.

---

# 🧠 Por que o encadeamento funciona?

Para permitir algo como:

```text
builder
    .com_logo()
    .com_sumario()
    .com_imagens()
    .construir()
```

cada etapa precisa devolver o próprio Builder ou outro objeto apropriado para continuar a cadeia.

Conceitualmente:

```text
com_logo()
    ↓
Builder

com_sumario()
    ↓
Builder

com_imagens()
    ↓
Builder

construir()
    ↓
Produto
```

O objetivo é facilitar a leitura da sequência de construção.

---

# 🆚 Construtor tradicional × Builder

## Construtor tradicional

```text
Relatorio(
    titulo,
    autor,
    cabecalho,
    logo,
    sumario,
    imagens,
    miniaturas,
    metadados,
    graficos,
    rodape,
    assinatura,
    marca_dagua,
    indice
)
```

Problemas:

```text
❌ Muitos parâmetros
❌ Ordem importante
❌ Difícil leitura
❌ Muitas opções
❌ Fácil configuração incorreta
```

---

## Builder

```text
ConstrutorRelatorio
    │
    ├── título
    ├── autor
    ├── logo
    ├── sumário
    ├── imagens
    ├── metadados
    ├── marca d'água
    └── construir
```

Vantagens:

```text
✓ Construção passo a passo
✓ Etapas nomeadas
✓ Opções opcionais
✓ Código mais expressivo
✓ Possibilidade de validação
```

---

# 🆚 Builder × herança

Sem Builder:

```text
Relatorio
   │
   ├── RelatorioComLogo
   ├── RelatorioSemLogo
   ├── RelatorioComImagens
   ├── RelatorioComLogoEImagens
   ├── RelatorioComLogoSemImagens
   └── ...
```

Com Builder:

```text
Relatorio
   ▲
   │
Builder
   │
   ├── com_logo()
   ├── com_imagens()
   ├── com_metadados()
   └── construir()
```

A configuração passa a ser feita durante a construção, em vez de ser representada através de subclasses.

---

# 🧠 Builder não é simplesmente "um construtor diferente"

É importante não reduzir o Builder à ideia de:

> "Uma classe que chama o construtor por partes."

O principal objetivo é separar responsabilidades.

Temos:

```text
Como construir?
```

e:

```text
O que está sendo construído?
```

Essas responsabilidades são separadas.

Portanto:

```text
Construção
    ≠
Representação
```

Essa separação é o coração do padrão.

---

# 🔄 O fluxo do Builder

Podemos resumir o funcionamento:

```text
                    CLIENTE
                       │
                       ▼
                    BUILDER
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Etapa 1      Etapa 2      Etapa 3
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                   construir()
                       │
                       ▼
                    PRODUTO
```

Com Director:

```text
                    CLIENTE
                       │
                       ▼
                   DIRECTOR
                       │
              define a sequência
                       │
                       ▼
                    BUILDER
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Etapa 1      Etapa 2      Etapa 3
                       │
                       ▼
                   PRODUTO
```

---

# 🔭 Exemplo-problema deste projeto

Neste projeto de estudo, o Builder será aplicado à construção de **relatórios de observação astronômica**.

O problema inicial é um relatório com muitas características possíveis:

```text
Relatório
│
├── Título
├── Autor
├── Cabeçalho
├── Logo do observatório
├── Sumário
├── Imagens
├── Miniaturas
├── Metadados
├── Gráficos de curva de luz
├── Rodapé
├── Assinatura
├── Marca d'água
└── Índice
```

Nem todo relatório utilizará todas essas opções.

Podemos ter:

```text
Relatório simples
```

com:

```text
Título
Autor
Imagens
```

ou:

```text
Relatório científico completo
```

com:

```text
Título
Autor
Cabeçalho
Logo
Sumário
Imagens
Miniaturas
Metadados
Gráficos
Rodapé
Assinatura
Índice
```

O objetivo do estudo será representar essa construção sem depender de um construtor gigantesco.

---

# 🎯 Objetivos da implementação

Na implementação posterior deste estudo, o Builder deverá permitir que o relatório seja construído de maneira progressiva.

Conceitualmente:

```text
Criar construtor

      ↓

Definir título

      ↓

Definir autor

      ↓

Adicionar logo

      ↓

Adicionar sumário

      ↓

Adicionar imagens

      ↓

Adicionar metadados

      ↓

Adicionar marca d'água

      ↓

Construir relatório

      ↓

Relatório pronto
```

A ideia é que características não utilizadas simplesmente não façam parte daquela construção.

---

# 🧱 Possíveis representações

O exemplo também permite compreender a ideia de diferentes representações.

Podemos imaginar:

```text
                    Builder
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
    Builder PDF                Builder HTML
          │                         │
          ▼                         ▼
    Relatório PDF              Relatório HTML
```

Assim, as mesmas etapas conceituais podem produzir produtos diferentes.

Por exemplo:

```text
Título
Autor
Imagens
Metadados
Rodapé
```

poderiam ser representados em:

```text
PDF
```

ou:

```text
HTML
```

---

# 🧠 Builder e Python

O Builder é um padrão muito conhecido em linguagens orientadas a objetos, mas sua necessidade varia de acordo com a linguagem.

Python possui recursos que tornam alguns problemas de construção mais simples.

Por exemplo:

```python
@dataclass(kw_only=True)
```

pode ser suficiente em muitos casos para representar objetos com muitos atributos opcionais.

Além disso, Python permite:

```text
argumentos nomeados
```

e:

```text
valores padrão
```

que reduzem bastante os problemas encontrados em linguagens com construtores mais rígidos.

Portanto:

> **Nem todo objeto com muitos atributos precisa de Builder em Python.**

O padrão passa a ser mais interessante quando existe uma **construção realmente complexa**, com etapas, validações, diferentes representações ou diferentes receitas de construção.

---

# 🐍 Builder versus `dataclass`

Imagine um objeto simples:

```text
Relatório
├── título
├── autor
├── logo
├── sumário
└── rodapé
```

Se esses atributos forem apenas dados, uma estrutura simples pode ser suficiente.

Por exemplo, conceitualmente:

```python
@dataclass
class Relatorio:
    ...
```

poderia resolver o problema sem criar diversas classes adicionais.

Por outro lado, se a criação envolver:

```text
Validações
+
Etapas
+
Dependências entre etapas
+
Diferentes representações
+
Receitas de construção
+
Regras de negócio
```

o Builder pode passar a fazer sentido.

Portanto:

> **O Builder não deve ser utilizado apenas porque uma classe possui muitos atributos.**

O que importa é a **complexidade da construção**.

---

# 🧠 Builder não significa necessariamente "muitas classes"

A estrutura clássica do GoF apresenta:

```text
Builder
ConcreteBuilder
Product
Director
Client
```

Porém, uma implementação real pode simplificar essa estrutura.

Por exemplo:

```text
Client
   │
   ▼
Builder
   │
   ▼
Product
```

O Director pode ser completamente desnecessário.

Da mesma forma, dependendo da linguagem e do domínio, não é obrigatório criar uma hierarquia enorme de builders.

O padrão deve ser adaptado ao problema.

---

# 🎯 Quando utilizar Builder?

O Builder é especialmente interessante quando:

- o objeto possui muitos parâmetros;
- existem muitos parâmetros opcionais;
- a construção ocorre em várias etapas;
- a ordem de determinadas etapas é relevante;
- existem regras de validação durante a construção;
- existem diferentes representações do mesmo produto;
- existem diferentes receitas para construir o mesmo tipo de objeto;
- queremos evitar construtores telescópicos;
- queremos tornar a criação do objeto mais legível;
- a lógica de construção está ficando complexa demais dentro do produto.

---

# 🚫 Quando não utilizar Builder?

O Builder pode ser desnecessário quando:

- o objeto possui poucos atributos;
- a construção é simples;
- não existem etapas relevantes;
- não existem muitas opções;
- não existem regras complexas de construção;
- uma `dataclass` ou construtor simples já resolve o problema;
- adicionar Builder apenas aumentaria a quantidade de classes sem trazer benefício real.

Em especial:

> **Não use Builder simplesmente porque o padrão existe.**

Se o objeto é simples, um construtor simples provavelmente é mais adequado.

---

# 🟢 Prós e Contras do Builder

## 🟢 Prós

### Construção passo a passo

O Builder permite construir objetos gradualmente.

Isso é útil quando os dados chegam aos poucos ou quando a criação envolve várias etapas.

```text
Etapa 1
   ↓
Etapa 2
   ↓
Etapa 3
   ↓
Etapa 4
   ↓
Produto
```

---

### Melhor legibilidade

Em vez de:

```text
True
False
None
True
None
False
```

podemos ter operações semanticamente explícitas:

```text
com_logo()
com_sumario()
com_imagens()
com_metadados()
```

A intenção do código fica mais fácil de compreender.

---

### Diferentes representações

O mesmo processo de construção pode produzir diferentes representações.

Por exemplo:

```text
Builder
   │
   ├── PDF
   │
   └── HTML
```

---

### Separação de responsabilidades

A lógica de construção pode ser retirada da classe do produto.

Podemos separar:

```text
Produto
    │
    └── representa o objeto

Builder
    │
    └── constrói o objeto
```

Isso pode contribuir para uma melhor separação de responsabilidades e para o princípio **S** do **SOLID — Single Responsibility Principle**.

---

### Possibilidade de validação

A construção pode verificar regras antes de entregar o objeto final.

```text
Builder
   │
   ▼
Validação
   │
   ├── inválido → erro
   │
   └── válido
         │
         ▼
      Produto
```

Isso ajuda a evitar que o produto seja entregue em uma configuração inválida quando o domínio exige determinadas condições.

---

### Reutilização de receitas

Com um Director, ou com métodos específicos de construção, podemos reutilizar determinadas sequências.

Por exemplo:

```text
Relatório completo
```

pode sempre seguir:

```text
Título
↓
Autor
↓
Logo
↓
Sumário
↓
Imagens
↓
Metadados
↓
Gráficos
↓
Rodapé
```

Enquanto:

```text
Relatório resumido
```

pode seguir:

```text
Título
↓
Autor
↓
Imagens
↓
Rodapé
```

---

# 🔴 Contras

## Mais classes e abstrações

Uma implementação clássica pode aumentar a quantidade de elementos:

```text
Builder
ConcreteBuilder
Product
Director
```

Isso aumenta a quantidade de código.

---

## Maior complexidade inicial

Para alguém que nunca utilizou o padrão, pode ser mais difícil entender:

```text
Quem constrói?

Quem define a ordem?

Quem representa o produto?

Quem executa cada etapa?
```

Existe uma camada adicional de abstração.

---

## Pode ser exagero

Se temos:

```text
Classe simples
```

com:

```text
3 atributos
```

criar:

```text
Builder
Director
ConcreteBuilder
```

provavelmente adicionaria complexidade sem necessidade.

---

## Pode não ser necessário em Python

Python possui recursos como:

```text
argumentos nomeados
```

```text
valores padrão
```

e:

```text
dataclasses
```

que podem resolver muitos casos simples.

Por isso:

> **Em Python, o Builder deve ser utilizado quando a complexidade da construção justificar sua existência.**

---

## Aumenta o código de manutenção

Mais classes significam mais código para:

```text
ler
testar
documentar
alterar
manter
```

O benefício precisa justificar esse custo.

---

# ⚖️ O ponto de equilíbrio

A pergunta não deve ser:

```text
"Tenho muitos atributos?"
```

Mas sim:

```text
"A construção desse objeto é complexa?"
```

Essas duas coisas não são necessariamente iguais.

Podemos ter:

```text
20 atributos
```

mas uma construção simples.

Nesse caso, talvez Builder não seja necessário.

Por outro lado, podemos ter:

```text
8 atributos
```

e uma construção que envolve:

```text
dependências
+
validações
+
etapas
+
diferentes representações
```

Nesse caso, Builder pode ser interessante.

---

# 📌 Regra prática

Podemos pensar:

```text
Objeto simples
      │
      ▼
Construtor / dataclass
```

Enquanto:

```text
Objeto complexo
      │
      ├── muitas opções
      ├── etapas
      ├── validações
      ├── diferentes representações
      └── diferentes receitas
              │
              ▼
           Builder
```

Não é uma regra absoluta.

É apenas uma orientação para evitar aplicar o padrão sem necessidade.

---

# 🆚 Builder × Factory Method

Builder e Factory Method são padrões criacionais, mas resolvem problemas diferentes.

## Factory Method

O foco principal é:

```text
Qual objeto criar?
```

Por exemplo:

```text
Factory
   │
   ├── Produto A
   └── Produto B
```

---

## Builder

O foco principal é:

```text
Como construir um objeto complexo?
```

Por exemplo:

```text
Builder
   │
   ├── etapa 1
   ├── etapa 2
   ├── etapa 3
   └── etapa 4
```

Podemos resumir:

```text
Factory Method
    ↓
Escolha do produto

Builder
    ↓
Processo de construção do produto
```

---

# 🆚 Builder × Abstract Factory

O **Abstract Factory** é utilizado para criar **famílias de objetos relacionados**.

Por exemplo:

```text
Fábrica Dark
├── Botão Dark
└── Janela Dark
```

Enquanto o Builder se preocupa com a construção passo a passo de um produto complexo:

```text
Builder
├── etapa 1
├── etapa 2
├── etapa 3
└── Produto
```

Podemos resumir:

```text
Abstract Factory
    ↓
Família de objetos relacionados

Builder
    ↓
Construção de um objeto complexo
```

---

# 🆚 Builder × Prototype

O **Prototype** utiliza um objeto existente como modelo para criar novos objetos.

```text
Objeto existente
       │
       ▼
     clone()
       │
       ▼
Novo objeto
```

O Builder trabalha de maneira diferente:

```text
Etapas
  │
  ▼
Construção
  │
  ▼
Novo produto
```

---

# 🧠 Builder e o GoF

O Builder pertence ao grupo dos:

> **Padrões Criacionais**

do livro:

> **Design Patterns: Elements of Reusable Object-Oriented Software**

conhecido como:

> **GoF — Gang of Four**

Os padrões criacionais lidam principalmente com mecanismos de criação de objetos.

O Builder se diferencia por não focar apenas em:

```text
qual objeto criar
```

mas também em:

```text
como construir um objeto complexo
```

---

# 📚 Referência conceitual do GoF

A ideia central apresentada pelo GoF pode ser resumida como:

```text
Separar:

Construção
    ↓
da

Representação
```

Isso permite que:

```text
mesmo processo de construção
```

possa produzir:

```text
diferentes representações
```

No nosso domínio:

```text
Processo de construção
        │
        ├───────────────┐
        │               │
        ▼               ▼
   Relatório PDF   Relatório HTML
```

---

# 🌐 Builder segundo o Refactoring Guru

O [Refactoring Guru — Builder](https://refactoring.guru/pt-br/design-patterns/builder) apresenta o Builder como um padrão criacional que permite construir objetos complexos passo a passo.

A estrutura também destaca a separação entre:

```text
código cliente
```

```text
diretor
```

```text
builder
```

e:

```text
produto
```

Um ponto importante é que o **Director é opcional**.

O cliente pode controlar diretamente as etapas quando isso fizer mais sentido.

---

# 🧩 Builder em uma visão geral

Podemos representar o padrão da seguinte maneira:

```text
                         CLIENTE
                            │
                            │
                            ▼
                        DIRECTOR
                            │
                            │ define ordem
                            ▼
                         BUILDER
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
           etapa 1       etapa 2       etapa 3
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ▼
                        construir()
                            │
                            ▼
                         PRODUTO
```

Sem Director:

```text
                         CLIENTE
                            │
                            ▼
                         BUILDER
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
           etapa 1       etapa 2       etapa 3
                            │
                            ▼
                        construir()
                            │
                            ▼
                         PRODUTO
```

---

# 🧠 A principal diferença em relação ao problema original

Antes:

```text
Relatorio(
    titulo,
    autor,
    cabecalho,
    logo,
    sumario,
    imagens,
    miniaturas,
    metadados,
    graficos,
    rodape,
    assinatura,
    marca_dagua,
    indice
)
```

Precisamos lembrar:

```text
posição
+
tipo
+
significado
```

Depois:

```text
ConstrutorRelatorio
    │
    ├── título
    ├── autor
    ├── cabeçalho
    ├── logo
    ├── sumário
    ├── imagens
    ├── metadados
    ├── gráficos
    ├── rodapé
    ├── assinatura
    ├── marca d'água
    ├── índice
    │
    ▼
construir()
```

Cada decisão passa a ser explícita.

---

# 🔎 O que o Builder realmente resolve?

É importante entender exatamente qual problema estamos tentando resolver.

O Builder não existe simplesmente para:

```text
diminuir quantidade de parâmetros
```

Ele existe principalmente para:

```text
organizar a construção de objetos complexos
```

O problema pode envolver:

```text
Muitos parâmetros
```

mas também:

```text
Etapas
```

```text
Validações
```

```text
Dependências
```

```text
Diferentes representações
```

```text
Diferentes receitas de construção
```

Portanto:

> **O verdadeiro problema é a complexidade do processo de construção.**

---

# 🎯 O Builder no nosso exemplo

Nosso problema pode ser resumido assim:

```text
Relatório possui muitas características
                    │
                    ▼
          Construtor muito grande
                    │
                    ▼
         Muitos parâmetros opcionais
                    │
                    ▼
        Código difícil de compreender
                    │
                    ▼
              Builder
                    │
                    ▼
        Construção passo a passo
```

A transformação é:

```text
ANTES

Cliente
   │
   ▼
Construtor gigante
   │
   ▼
Relatório
```

para:

```text
DEPOIS

Cliente
   │
   ▼
Builder
   │
   ├── etapa
   ├── etapa
   ├── etapa
   ├── etapa
   │
   ▼
construir()
   │
   ▼
Relatório
```

---

# 📌 Uma analogia

Podemos comparar o Builder à construção de uma casa.

Sem uma separação clara:

```text
Casa(
    terreno,
    fundacao,
    paredes,
    portas,
    janelas,
    telhado,
    pintura,
    eletrica,
    hidraulica,
    ...
)
```

É difícil visualizar o processo.

Com Builder:

```text
ConstrutorCasa
    │
    ├── preparar_fundacao()
    ├── construir_paredes()
    ├── instalar_portas()
    ├── instalar_janelas()
    ├── construir_telhado()
    ├── instalar_eletrica()
    ├── instalar_hidraulica()
    └── construir()
```

O código passa a representar o processo de construção.

No nosso exemplo:

```text
ConstrutorRelatorio
    │
    ├── com_cabecalho()
    ├── com_logo()
    ├── com_sumario()
    ├── com_imagens()
    ├── com_metadados()
    ├── com_graficos()
    └── construir()
```

---

# 🧠 Builder e legibilidade

Uma das principais vantagens do Builder é tornar a intenção do código mais evidente.

Compare:

```text
Relatorio(
    "Observação NGC 4654",
    "Dra. Silva",
    True,
    "upe.png",
    True,
    imagens,
    False,
    True,
    graficos,
    True,
    None,
    True,
    False
)
```

com:

```text
ConstrutorRelatorio(
    "Observação NGC 4654",
    "Dra. Silva"
)
    .com_logo("upe.png")
    .com_sumario()
    .com_imagens(imagens)
    .com_metadados()
    .com_graficos(graficos)
    .com_marca_dagua("RASCUNHO")
    .construir()
```

No segundo caso, podemos praticamente ler o código como uma descrição do relatório.

---

# 🧪 O que será estudado na implementação

Na implementação deste repositório, o objetivo será observar principalmente:

```text
1. O problema do construtor com muitos parâmetros

2. A separação entre produto e construção

3. A criação do Builder

4. A construção passo a passo

5. O encadeamento das etapas

6. O método construir()

7. A possibilidade de validação

8. O papel opcional do Director

9. A possibilidade de diferentes representações

10. As vantagens e limitações do padrão em Python
```

---

# 🧠 Ideia principal para memorizar

O Builder pode ser resumido como:

```text
Objeto complexo
      │
      ▼
Construção passo a passo
      │
      ▼
Produto final
```

Ou:

```text
COMO construir?
       │
       ▼
    Builder
       │
       ▼
   construir()
       │
       ▼
O QUE foi construído?
       │
       ▼
    Produto
```

A ideia mais importante é:

> **Builder = separar a construção de um objeto complexo da sua representação.**

---

# 📝 Resumo Final

O **Builder** é um Design Pattern **criacional** utilizado quando a construção de um objeto é suficientemente complexa para justificar sua separação em etapas.

No problema deste estudo, temos um:

```text
Relatório de observação astronômica
```

com várias características possíveis:

```text
Cabeçalho
Logo
Sumário
Imagens
Miniaturas
Metadados
Gráficos
Rodapé
Assinatura
Marca d'água
Índice
```

Construir esse objeto diretamente através de um construtor com muitos parâmetros pode resultar em:

```text
❌ código difícil de ler
❌ parâmetros difíceis de lembrar
❌ possibilidade de erros de posição
❌ muitos valores opcionais
❌ construtores telescópicos
❌ dificuldade para representar diferentes configurações
```

O Builder propõe:

```text
Cliente
   │
   ▼
Builder
   │
   ├── etapa 1
   ├── etapa 2
   ├── etapa 3
   ├── etapa 4
   └── ...
          │
          ▼
      construir()
          │
          ▼
       Produto
```

O **Director**, quando utilizado, fica responsável por definir:

```text
Quais etapas executar?
```

e:

```text
Em qual ordem?
```

Enquanto o **Builder** fica responsável por:

```text
Como cada etapa é executada?
```

E o **Product** representa:

```text
O objeto final.
```

No nosso exemplo:

```text
                 Relatório
                     ▲
                     │
                 construir()
                     │
                  Builder
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
     Logo         Imagens      Metadados
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
                 Relatório
```

A ideia central pode ser resumida em uma frase:

> **O Builder separa a construção de um objeto complexo da sua representação, permitindo que o objeto seja construído passo a passo e, quando necessário, que o mesmo processo produza diferentes representações.**

No exemplo do observatório:

```text
Construtor de Relatório
        │
        ├── título
        ├── autor
        ├── logo
        ├── imagens
        ├── metadados
        ├── gráficos
        ├── marca d'água
        │
        ▼
    construir()
        │
        ▼
     Relatório
```

Assim, em vez de tentar lembrar:

```text
Qual era o significado do
True na décima segunda posição?
```

passamos a expressar diretamente a intenção:

```text
com_marca_dagua()
```

Essa é uma das principais ideias que devemos observar ao implementar o padrão.

---

# 📚 Referências

- **GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John.** *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.
- **Refactoring Guru.** *Builder — Padrão de projeto*. Disponível em: [https://refactoring.guru/pt-br/design-patterns/builder](https://refactoring.guru/pt-br/design-patterns/builder). Acesso em: 25 set. 2026.
- **Refactoring Guru.** *Design Patterns*. Disponível em: [https://refactoring.guru/pt-br/design-patterns](https://refactoring.guru/pt-br/design-patterns). Acesso em: 25 set. 2026.

---

# 📌 Para lembrar

```text
┌──────────────────────────────────────┐
│              BUILDER                 │
├──────────────────────────────────────┤
│                                      │
│  Problema:                           │
│  objeto complexo                     │
│  +                                   │
│  muitos parâmetros/opções            │
│  +                                   │
│  construção complexa                 │
│                                      │
│              ↓                       │
│                                      │
│  Solução:                            │
│  construção passo a passo            │
│                                      │
│              ↓                       │
│                                      │
│  Builder                             │
│              ↓                       │
│  Etapas de construção                │
│              ↓                       │
│  construir()                         │
│              ↓                       │
│  Produto                             │
│                                      │
└──────────────────────────────────────┘
```

> **Builder = construir objetos complexos passo a passo, separando o processo de construção da representação final.**
