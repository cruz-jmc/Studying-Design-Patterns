# Factory Method - Reference: <https://refactoring.guru/pt-br/design-patterns/factory-method>

## 📌 Objetivo

O **Factory Method** é um Design Pattern **criacional** utilizado para **delegar a responsabilidade de criar objetos para um método especializado**, evitando que uma classe precise conhecer diretamente todos os tipos concretos que podem ser instanciados.

A ideia principal é:

> **Definir um método para criação de objetos, mas permitir que subclasses decidam qual objeto concreto deve ser criado.**

Em vez de espalhar pelo sistema vários comandos como:

```text
ObjetoA()
ObjetoB()
ObjetoC()
```

podemos concentrar a decisão de criação em um método:

```python
criar_produto()
```

A classe principal sabe:

```text
"Preciso de um Produto"
```

mas não precisa necessariamente saber:

```text
"Qual classe concreta deve ser instanciada?"
```

Essa decisão pode ficar para subclasses.

---

# 🏭 O que é uma Factory?

Antes de entender o **Factory Method**, é importante entender a ideia de uma **Factory**.

Uma _factory_ é simplesmente uma estrutura responsável por:

> **Criar objetos.**

Por exemplo, imagine um sistema que precisa trabalhar com diferentes formas de pagamento:

```text
Pix
Cartão
Boleto
```

Uma implementação simples poderia fazer:

```python
if tipo == "pix":
    pagamento = Pix()

elif tipo == "cartao":
    pagamento = Cartao()

elif tipo == "boleto":
    pagamento = Boleto()
```

Funciona.

Mas existe um problema.

A classe que possui esse `if` precisa conhecer:

```text
Pix
Cartao
Boleto
```

e também precisa conhecer:

```text
Como cada objeto é criado.
```

Isso gera acoplamento entre quem utiliza o pagamento e as classes concretas.

---

# 💳 Primeiro exemplo: formas de pagamento

Imagine um sistema de pedidos.

O cliente escolhe uma forma de pagamento:

```text
Pix
```

ou:

```text
Cartão
```

Podemos ter algo conceitualmente parecido com:

```python
class Pedido:

    def __init__(self, pagamento: Pagamento):
        self.pagamento = pagamento
```

Depois:

```python
Pedido(Pix()).finalizar(100)
Pedido(Cartao()).finalizar(100)
```

Essa solução já é melhor do que colocar toda a lógica dentro de `Pedido`.

A classe `Pedido` apenas recebe algo que representa um:

```text
Pagamento
```

Portanto, ela não precisa decidir diretamente como o pagamento será criado.

Esse tipo de solução reduz o acoplamento.

---

# 🔄 O problema volta para o cliente

Porém, imagine que exista uma função responsável por interpretar o tipo escolhido pelo usuário:

```python
def processar(tipo: str, valor: float):

    if tipo == "pix":
        pagamento = Pix()

    elif tipo == "cartao":
        pagamento = Cartao()

    # ...

    Pedido(pagamento).finalizar(valor)
```

Agora a situação muda.

O problema da criação apenas foi deslocado para outro lugar.

Ainda existe:

```text
if
elif
elif
elif
```

e essa lógica ainda precisa conhecer:

```text
Pix
Cartao
Boleto
...
```

Se surgirem novas formas de pagamento, esse código terá que ser alterado.

Por exemplo:

```text
Novo pagamento

↓

Adicionar outro if

↓

Adicionar outra instanciação
```

Isso faz com que a lógica de criação fique centralizada em um lugar que talvez não deveria conhecer todos os produtos concretos.

---

# 🧠 A ideia do Factory Method

O **Factory Method** surge justamente para resolver esse tipo de problema.

A ideia é:

> **Delegar a responsabilidade de decidir qual objeto criar para um método.**

Em vez de escrever diretamente:

```python
Pix()
```

ou:

```python
Cartao()
```

podemos ter:

```python
criar_pagamento()
```

A classe principal sabe que existe um método responsável por criar um produto.

Mas quem decide o produto concreto pode ser uma subclasse.

Visualmente:

```text
Creator
   |
   └── criar_produto()
           |
           └── retorna Product
```

Depois:

```text
ConcreteCreatorA
        |
        └── cria ConcreteProductA
```

e:

```text
ConcreteCreatorB
        |
        └── cria ConcreteProductB
```

A criação deixa de ficar diretamente acoplada ao código principal.

---

# 🎯 Intenção do Factory Method

A intenção clássica do padrão pode ser resumida como:

> **Definir uma interface para criar um objeto, mas deixar as subclasses decidirem qual classe instanciar.**

Isso significa que:

```text
Creator
```

define:

```text
"Existe um método responsável por criar o produto."
```

Mas:

```text
ConcreteCreator
```

decide:

```text
"Qual produto concreto será criado?"
```

Portanto:

```text
Classe base
   |
   | conhece
   v
Product
```

enquanto:

```text
Subclasse
   |
   | decide
   v
ConcreteProduct
```

---

# 🧩 Por que isso é chamado de Factory Method?

O nome vem justamente da ideia de utilizar um:

```text
Method
```

como uma:

```text
Factory
```

Ou seja:

```text
Método

↓

Responsável por criar

↓

Objeto
```

Em vez de a classe principal executar diretamente:

```python
ProdutoConcreto()
```

ela chama:

```python
self.criar_produto()
```

Esse método funciona como um ponto de criação.

---

# 🚨 O problema principal

Para entender realmente o Factory Method, precisamos observar o problema que ele tenta resolver.

Imagine que estamos desenvolvendo um sistema responsável por exportar imagens produzidas por telescópios.

Essas imagens são armazenadas originalmente em:

```text
FITS
```

O sistema possui uma classe:

```text
ExportadorDeAcervo
```

Seu trabalho é exportar várias imagens.

Podemos imaginar uma implementação inicial:

```python
class ExportadorDeAcervo:

    def exportar(
        self,
        imagens: list[Imagem],
        destino: str
    ) -> None:

        arquivo = ArquivoFITS(destino)

        arquivo.escrever_cabecalho()

        for img in imagens:
            arquivo.adicionar(img)

        arquivo.fechar()

        print(f"Exportado para {destino}")
```

A implementação parece simples.

O problema aparece quando novos requisitos surgem.

---

# 🔭 O exemplo-problema

Nosso sistema trabalha originalmente com imagens astronômicas em formato:

```text
FITS
```

Esse é o formato utilizado para armazenar os dados produzidos pelos telescópios.

Porém, novos requisitos foram definidos.

O sistema agora precisa exportar imagens em diferentes formatos.

Por exemplo:

```text
PNG
TIFF
FITS
```

Além disso:

```text
FITS
```

precisa possuir uma forma específica de armazenamento.

Podemos representar os requisitos assim:

```text
Sistema de exportação

        |
        ├── PNG
        |
        ├── TIFF
        |
        └── FITS
```

O problema é que o código original conhece diretamente:

```text
ArquivoFITS
```

---

# 📋 Novos requisitos

Imagine que as seguintes demandas chegaram:

## 🌐 Site público

O site público precisa receber as imagens em:

```text
.png
```

Portanto:

```text
Imagem

↓

PNG
```

---

## 🔬 Laboratório

O laboratório exige:

```text
TIFF
```

Portanto:

```text
Imagem

↓

TIFF
```

---

## 🛰️ Armazenamento científico

O sistema científico continua exigindo:

```text
FITS
```

e o arquivo:

```text
FITS
```

precisa ser comprimido antes do armazenamento.

Portanto:

```text
Imagem

↓

FITS

↓

Compressão

↓

Armazenamento
```

---

# 💥 Uma solução ingênua

A primeira solução poderia ser simplesmente adicionar um parâmetro:

```python
def exportar(
    self,
    imagens,
    destino,
    formato
):
```

E então:

```python
if formato == "fits":

    arquivo = ArquivoFITS(destino)

elif formato == "png":

    arquivo = ArquivoPNG(destino)

elif formato == "tiff":

    arquivo = ArquivoTIFF(destino)
```

Visualmente:

```text
exportar()

   |
   v

formato?

   |
   ├── FITS → ArquivoFITS
   |
   ├── PNG  → ArquivoPNG
   |
   └── TIFF → ArquivoTIFF
```

No início isso parece razoável.

Mas existe um problema importante.

---

# 🔴 O problema dos `if` e `elif`

A classe:

```text
ExportadorDeAcervo
```

passou a conhecer diretamente:

```text
ArquivoFITS
ArquivoPNG
ArquivoTIFF
```

Portanto, existe um forte acoplamento.

Visualmente:

```text
ExportadorDeAcervo
        |
        ├── ArquivoFITS
        |
        ├── ArquivoPNG
        |
        └── ArquivoTIFF
```

A classe não depende mais apenas de uma abstração.

Ela depende de vários tipos concretos.

---

# ➕ E se surgir outro formato?

Imagine que amanhã seja necessário adicionar:

```text
JPEG
```

O código precisará ser alterado.

Teríamos:

```python
if formato == "fits":

    arquivo = ArquivoFITS(destino)

elif formato == "png":

    arquivo = ArquivoPNG(destino)

elif formato == "tiff":

    arquivo = ArquivoTIFF(destino)

elif formato == "jpeg":

    arquivo = ArquivoJPEG(destino)
```

E futuramente:

```text
WEBP
SVG
RAW
AVIF
...
```

O método continuaria crescendo.

Teríamos algo como:

```text
if
elif
elif
elif
elif
elif
...
```

Isso é um sinal de que a responsabilidade de criação pode estar no lugar errado.

---

# 🔁 O problema apenas foi deslocado

Uma alternativa seria criar um exportador diferente para cada tipo:

```text
ExportadorFITS
ExportadorPNG
ExportadorTIFF
```

A ideia poderia parecer boa.

Por exemplo:

```python
class ExportadorFITS:

    def exportar(...):

        arquivo = ArquivoFITS(destino)

        ...
```

Depois:

```python
class ExportadorPNG:

    def exportar(...):

        arquivo = ArquivoPNG(destino)

        ...
```

Porém, surge outro problema.

Grande parte da lógica provavelmente seria repetida.

Por exemplo:

```python
arquivo.escrever_cabecalho()

for img in imagens:
    arquivo.adicionar(img)

arquivo.fechar()

print(...)
```

seria praticamente igual em vários lugares.

Portanto:

```text
Código duplicado

↓

Difícil manutenção
```

E acabamos apenas empurrando a complexidade para outras classes.

---

# 💡 O que realmente queremos?

Queremos separar duas coisas:

```text
O que fazer com o arquivo
```

de:

```text
Qual objeto concreto deve ser criado
```

A ideia é que a classe principal saiba realizar a operação:

```text
exportar
```

mas não precise decidir diretamente:

```text
ArquivoFITS
ArquivoPNG
ArquivoTIFF
```

Ela deve poder trabalhar com uma abstração.

Por exemplo:

```text
Arquivo
```

E a criação pode ser delegada para um método:

```text
criar_arquivo()
```

---

# 🏭 A solução com Factory Method

Podemos criar uma estrutura semelhante a:

```text
Creator
```

que possui:

```text
factory_method()
```

Esse método será responsável por criar um:

```text
Product
```

Visualmente:

```text
Creator

    |
    └── factory_method()

                |
                v

             Product
```

Depois criamos subclasses.

Por exemplo:

```text
ExportadorFITS
ExportadorPNG
ExportadorTIFF
```

Cada uma sobrescreve:

```text
factory_method()
```

e retorna seu produto correspondente.

---

# 🏗️ Estrutura geral

A estrutura conceitual fica:

```text
                    Creator
                       |
                       |
              factory_method()
                       |
                       v
                    Product
                  /         \
                 /           \
                v             v
        ConcreteProductA  ConcreteProductB
```

E do outro lado:

```text
                Creator
                /      \
               /        \
              v          v
     ConcreteCreatorA  ConcreteCreatorB
              |          |
              v          v
      ConcreteProductA ConcreteProductB
```

A relação principal é:

```text
ConcreteCreatorA
        |
        └── cria
              |
              v
      ConcreteProductA
```

e:

```text
ConcreteCreatorB
        |
        └── cria
              |
              v
      ConcreteProductB
```

---

# 📦 O Product

O **Product** representa a interface ou abstração comum dos objetos que podem ser criados.

No nosso exemplo:

```text
Arquivo
```

pode ser o Product.

Todos os formatos de arquivo precisam possuir comportamentos que o exportador entende.

Por exemplo:

```text
escrever_cabecalho()
adicionar()
fechar()
```

Então podemos imaginar:

```text
Arquivo
   |
   ├── ArquivoFITS
   |
   ├── ArquivoPNG
   |
   └── ArquivoTIFF
```

A classe principal não precisa necessariamente conhecer todos os detalhes internos dessas implementações.

---

# 🧱 ConcreteProduct

Os **ConcreteProducts** são as implementações concretas do Product.

No nosso exemplo:

```text
ArquivoFITS
ArquivoPNG
ArquivoTIFF
```

Cada classe sabe como trabalhar especificamente com seu formato.

Por exemplo:

```text
ArquivoFITS
    ↓
Trabalha com FITS
```

```text
ArquivoPNG
    ↓
Trabalha com PNG
```

```text
ArquivoTIFF
    ↓
Trabalha com TIFF
```

O comportamento concreto fica nessas classes.

---

# 🏭 O Creator

O **Creator** é a classe que define o Factory Method.

Ele pode conhecer o Product:

```text
Arquivo
```

mas não necessariamente precisa conhecer todos os:

```text
Arquivos concretos
```

Ele pode definir algo conceitualmente como:

```python
def criar_arquivo(self) -> Arquivo:
    ...
```

Esse método representa o ponto de criação.

---

# 🏗️ O ConcreteCreator

Os **ConcreteCreators** são subclasses do Creator.

Eles sobrescrevem o Factory Method.

Por exemplo:

```text
ExportadorFITS
        |
        └── criar_arquivo()
                |
                v
           ArquivoFITS
```

Enquanto:

```text
ExportadorPNG
        |
        └── criar_arquivo()
                |
                v
            ArquivoPNG
```

E:

```text
ExportadorTIFF
        |
        └── criar_arquivo()
                |
                v
            ArquivoTIFF
```

A decisão sobre o tipo concreto fica nas subclasses.

---

# 🧠 O ponto mais importante

O conceito mais importante para entender é:

> **A classe base não precisa saber qual produto concreto será criado.**

Ela sabe apenas:

```text
"Preciso criar um Product."
```

A subclasse decide:

```text
"Vou criar ConcreteProductA."
```

ou:

```text
"Vou criar ConcreteProductB."
```

Visualmente:

```text
Creator

   |
   | conhece
   v

Product
```

Enquanto:

```text
ConcreteCreator

   |
   | decide
   v

ConcreteProduct
```

---

# 🔄 O fluxo de execução

Imagine:

```text
ExportadorPNG
```

e:

```text
ArquivoPNG
```

O cliente pede:

```text
exportar()
```

O fluxo conceitual pode ser:

```text
Cliente

   |
   v

ExportadorPNG

   |
   v

criar_arquivo()

   |
   v

ArquivoPNG

   |
   v

escrever_cabecalho()

   |
   v

adicionar(imagem)

   |
   v

fechar()
```

O cliente não precisa executar:

```python
ArquivoPNG(...)
```

diretamente.

A criação aconteceu através do Factory Method.

---

# 🧩 Estrutura do exemplo-problema

Podemos adaptar o exemplo da exportação de imagens da seguinte maneira:

```text
                    Exportador
                        |
                        |
                 criar_arquivo()
                        |
                        v
                     Arquivo
                   /    |    \
                  /     |     \
                 v      v      v
              FITS     PNG    TIFF
```

Do lado dos criadores:

```text
                  Exportador
                  /         \
                 /           \
                v             v
      ExportadorFITS      ExportadorPNG
              |                 |
              v                 v
         ArquivoFITS       ArquivoPNG
```

E posteriormente:

```text
ExportadorTIFF
      |
      v
ArquivoTIFF
```

---

# 📝 O problema do telescópio

Neste projeto, o sistema receberá uma lista de imagens:

```text
Imagem 1
Imagem 2
Imagem 3
...
```

e precisará exportá-las.

A classe inicialmente conhece apenas:

```text
ArquivoFITS
```

mas novos formatos passam a ser necessários.

Por exemplo:

```text
PNG
TIFF
FITS
```

O objetivo do estudo será reorganizar o código para que a criação dos arquivos seja delegada para um:

```text
Factory Method
```

em vez de colocar várias decisões de criação dentro de um grande:

```text
if / elif / else
```

---

# 🛠️ O que pretendemos evitar

Queremos evitar algo como:

```python
def exportar(self, imagens, destino, formato):

    if formato == "fits":
        arquivo = ArquivoFITS(destino)

    elif formato == "png":
        arquivo = ArquivoPNG(destino)

    elif formato == "tiff":
        arquivo = ArquivoTIFF(destino)

    ...

    arquivo.escrever_cabecalho()

    for imagem in imagens:
        arquivo.adicionar(imagem)

    arquivo.fechar()
```

O problema está principalmente em:

```python
if formato == ...
```

porque o `exportar()` está acumulando duas responsabilidades:

```text
1. Exportar as imagens

2. Decidir qual objeto criar
```

Queremos separar essas responsabilidades.

---

# ✅ O que queremos alcançar

A classe principal deve se preocupar com:

```text
Como realizar a exportação
```

e uma subclasse deve decidir:

```text
Qual arquivo concreto utilizar
```

Dessa forma:

```text
Creator

↓

define o fluxo da operação

↓

possui Factory Method
```

e:

```text
ConcreteCreator

↓

define qual Product criar
```

---

# 🔍 Factory Method não é simplesmente uma classe Factory

Essa é uma distinção importante.

Muitas vezes, quando alguém ouve:

```text
Factory Method
```

imagina:

```python
class Factory:

    def criar(tipo):
        if tipo == "...":
            ...
```

Isso pode ser uma implementação de uma **Simple Factory**, mas não representa necessariamente o padrão **Factory Method** clássico.

No Factory Method, a característica principal é:

```text
Método de criação

↓

pode ser sobrescrito

↓

por subclasses
```

Ou seja:

```text
Classe base
        |
        └── factory_method()

Subclasse A
        |
        └── sobrescreve factory_method()

Subclasse B
        |
        └── sobrescreve factory_method()
```

A diferença é importante.

---

# 🆚 Simple Factory x Factory Method

Podemos comparar conceitualmente.

## Simple Factory

Uma única fábrica decide o tipo:

```text
Factory
   |
   ├── if tipo A → Produto A
   ├── if tipo B → Produto B
   └── if tipo C → Produto C
```

A criação continua centralizada em condições.

---

## Factory Method

A decisão é distribuída pelas subclasses:

```text
Creator
   |
   ├── CreatorA → ProductA
   |
   ├── CreatorB → ProductB
   |
   └── CreatorC → ProductC
```

A escolha acontece por polimorfismo e sobrescrita de método.

---

# 🧠 Factory Method e Polimorfismo

O Factory Method utiliza fortemente:

> **Polimorfismo**

A classe cliente trabalha com:

```text
Creator
```

e o objeto concreto pode ser:

```text
CreatorA
CreatorB
CreatorC
```

Todos possuem:

```text
factory_method()
```

mas cada um cria um produto diferente.

Portanto:

```text
mesma operação

↓

comportamentos diferentes
```

---

# 🔁 A importância da sobrescrita

Imagine que a classe base tenha:

```python
def criar_arquivo(self):
    ...
```

Uma subclasse pode sobrescrever:

```python
class ExportadorPNG(Exportador):

    def criar_arquivo(self):
        return ArquivoPNG(...)
```

Enquanto outra pode fazer:

```python
class ExportadorTIFF(Exportador):

    def criar_arquivo(self):
        return ArquivoTIFF(...)
```

Portanto:

```text
criar_arquivo()
```

possui a mesma assinatura.

Mas o resultado concreto depende da subclasse.

Isso é polimorfismo.

---

# 🧱 Estrutura clássica do Factory Method

A estrutura pode ser entendida desta forma:

```text
┌───────────────────────────┐
│          Product          │
├───────────────────────────┤
│ + operacao()              │
└───────────────────────────┘
             ▲
             │
      ┌──────┴──────┐
      │             │
      │             │
┌──────────────┐ ┌──────────────┐
│ ProductA     │ │ ProductB     │
└──────────────┘ └──────────────┘


┌───────────────────────────┐
│         Creator           │
├───────────────────────────┤
│ + factory_method()        │
│ + operacao()              │
└───────────────────────────┘
             ▲
             │
      ┌──────┴──────┐
      │             │
┌──────────────┐ ┌──────────────┐
│ CreatorA     │ │ CreatorB     │
├──────────────┤ ├──────────────┤
│ factory()    │ │ factory()    │
└──────────────┘ └──────────────┘
```

---

# 🔗 Relação entre Creator e Product

Uma característica importante é:

```text
Creator

↓

usa Product
```

O Creator pode possuir uma operação de negócio que utiliza o produto criado.

Por exemplo:

```text
exportar()
```

pode utilizar:

```text
criar_arquivo()
```

que retorna:

```text
Arquivo
```

Então temos:

```text
exportar()

      |
      v

criar_arquivo()

      |
      v

Arquivo
```

O método de negócio não precisa necessariamente saber qual implementação concreta foi criada.

---

# 📦 O Factory Method como "Virtual Constructor"

O Factory Method também é conhecido como:

> **Virtual Constructor**

A ideia é que o código possa solicitar a criação de um objeto através de um método sem precisar escrever diretamente o construtor da classe concreta.

Em vez de:

```python
ArquivoPNG(...)
```

temos:

```python
self.criar_arquivo()
```

E a implementação concreta decide:

```text
qual construtor chamar.
```

---

# 🔐 Desacoplamento

Um dos principais benefícios do padrão é reduzir o acoplamento.

Sem Factory Method:

```text
Exportador
   |
   ├── ArquivoFITS
   ├── ArquivoPNG
   └── ArquivoTIFF
```

Com Factory Method:

```text
Exportador
   |
   v
Arquivo
```

e:

```text
ExportadorFITS
      |
      v
ArquivoFITS
```

```text
ExportadorPNG
      |
      v
ArquivoPNG
```

```text
ExportadorTIFF
      |
      v
ArquivoTIFF
```

A abstração cria uma separação mais clara.

---

# 🧠 O código de negócio permanece estável

Imagine que a classe base faça:

```text
exportar()

↓

criar arquivo

↓

escrever cabeçalho

↓

adicionar imagens

↓

fechar arquivo
```

Essa sequência pode permanecer igual.

O que muda é:

```text
Qual arquivo foi criado.
```

Portanto:

```text
Fluxo da operação

↓

continua na classe base
```

enquanto:

```text
Decisão de criação

↓

fica nas subclasses
```

Essa separação é uma das ideias centrais do padrão.

---

# 🛰️ Aplicando ao projeto de imagens astronômicas

No projeto que será implementado neste repositório, podemos imaginar a seguinte estrutura:

```text
Imagem
   |
   v
Arquivo
   |
   ├── ArquivoFITS
   ├── ArquivoPNG
   └── ArquivoTIFF
```

e:

```text
Exportador
   |
   ├── ExportadorFITS
   ├── ExportadorPNG
   └── ExportadorTIFF
```

A relação seria:

```text
ExportadorFITS
       |
       └── cria → ArquivoFITS
```

```text
ExportadorPNG
       |
       └── cria → ArquivoPNG
```

```text
ExportadorTIFF
       |
       └── cria → ArquivoTIFF
```

---

# 📋 Participantes do Factory Method

O padrão possui alguns papéis importantes.

---

## 🔷 Product

Define a interface comum dos objetos que podem ser criados.

No nosso exemplo:

```text
Arquivo
```

Pode definir operações como:

```text
escrever_cabecalho()
adicionar()
fechar()
```

---

## 🟩 ConcreteProduct

Representa uma implementação concreta do Product.

No nosso exemplo:

```text
ArquivoFITS
ArquivoPNG
ArquivoTIFF
```

Cada classe possui os detalhes específicos do seu formato.

---

## 🏭 Creator

É a classe que declara o Factory Method.

No nosso exemplo:

```text
Exportador
```

Ela define:

```text
criar_arquivo()
```

Além disso, pode possuir operações de negócio como:

```text
exportar()
```

---

## 🏗️ ConcreteCreator

São as subclasses responsáveis por decidir qual produto concreto deve ser criado.

No nosso exemplo:

```text
ExportadorFITS
ExportadorPNG
ExportadorTIFF
```

Cada uma sobrescreve:

```text
criar_arquivo()
```

e retorna o produto correspondente.

---

## 👤 Client

É o código que utiliza os Creators e Products.

A ideia é que o Client trabalhe principalmente com as abstrações:

```text
Creator
```

e:

```text
Product
```

sem depender desnecessariamente das implementações concretas.

---

# 📊 Participantes no nosso exemplo

| Participante        | Exemplo                                             | Responsabilidade                                |
| ------------------- | --------------------------------------------------- | ----------------------------------------------- |
| **Product**         | `Arquivo`                                           | Define a abstração comum dos arquivos           |
| **ConcreteProduct** | `ArquivoFITS`, `ArquivoPNG`, `ArquivoTIFF`          | Implementam formatos específicos                |
| **Creator**         | `Exportador`                                        | Define o Factory Method e o fluxo da exportação |
| **ConcreteCreator** | `ExportadorFITS`, `ExportadorPNG`, `ExportadorTIFF` | Decidem qual arquivo concreto será criado       |
| **Client**          | Aplicação principal                                 | Utiliza os exportadores                         |

---

# 🔄 Fluxo do nosso exemplo

Podemos imaginar uma chamada:

```text
Cliente
   |
   v
ExportadorPNG
   |
   v
exportar()
   |
   v
criar_arquivo()
   |
   v
ArquivoPNG
   |
   v
escrever_cabecalho()
   |
   v
adicionar(imagem)
   |
   v
fechar()
```

Observe algo importante.

O método:

```text
exportar()
```

pode ser reutilizado.

A diferença está apenas em:

```text
criar_arquivo()
```

---

# 🧪 Exemplo conceitual

A classe base poderia representar:

```python
class Exportador:

    def criar_arquivo(self, destino):
        raise NotImplementedError

    def exportar(self, imagens, destino):

        arquivo = self.criar_arquivo(destino)

        arquivo.escrever_cabecalho()

        for imagem in imagens:
            arquivo.adicionar(imagem)

        arquivo.fechar()
```

Aqui existe uma separação importante.

A classe sabe:

```text
como exportar
```

mas não necessariamente:

```text
qual arquivo concreto criar
```

---

# 🟦 Exportador de FITS

Uma subclasse poderia implementar:

```python
class ExportadorFITS(Exportador):

    def criar_arquivo(self, destino):

        return ArquivoFITS(destino)
```

Agora temos:

```text
ExportadorFITS

        |
        v

criar_arquivo()

        |
        v

ArquivoFITS
```

---

# 🟩 Exportador de PNG

Outra subclasse:

```python
class ExportadorPNG(Exportador):

    def criar_arquivo(self, destino):

        return ArquivoPNG(destino)
```

Agora:

```text
ExportadorPNG

        |
        v

criar_arquivo()

        |
        v

ArquivoPNG
```

---

# 🟨 Exportador de TIFF

E:

```python
class ExportadorTIFF(Exportador):

    def criar_arquivo(self, destino):

        return ArquivoTIFF(destino)
```

Agora:

```text
ExportadorTIFF

        |
        v

criar_arquivo()

        |
        v

ArquivoTIFF
```

---

# 🧠 Observe onde foi parar o `if`

Na abordagem ingênua:

```text
if formato == "fits":
    ...

elif formato == "png":
    ...

elif formato == "tiff":
    ...
```

Na abordagem com Factory Method:

```text
Subclasse

↓

sobrescreve o método

↓

retorna produto adequado
```

A decisão deixa de depender de uma grande cadeia de condicionais.

---

# 🔄 Antes e depois

## ❌ Sem Factory Method

```text
Exportador

   |
   v

verifica formato

   |
   ├── FITS
   |
   ├── PNG
   |
   └── TIFF
```

A classe conhece vários tipos concretos.

---

## ✅ Com Factory Method

```text
Exportador
   |
   v
factory_method()
   |
   v
Product
```

A implementação concreta é definida por subclasses.

---

# 🧠 Factory Method e princípio SRP

O Factory Method pode ajudar na aplicação do:

> **Single Responsibility Principle**

Uma classe não precisa concentrar:

```text
Fluxo da operação
```

e:

```text
Toda a decisão de criação de objetos
```

Podemos separar:

```text
Creator

↓

fluxo da operação
```

de:

```text
ConcreteCreator

↓

decisão do produto
```

Isso não significa que qualquer uso de Factory Method automaticamente garanta SRP.

O importante é observar se a separação realmente faz sentido no problema.

---

# 🧠 Factory Method e Open/Closed Principle

O padrão também pode ajudar a respeitar o:

> **Open/Closed Principle**

A ideia é:

```text
Aberto para extensão

Fechado para modificação
```

Imagine que já existam:

```text
ExportadorFITS
ExportadorPNG
ExportadorTIFF
```

Agora surge:

```text
ExportadorJPEG
```

Podemos adicionar:

```text
ExportadorJPEG
```

e:

```text
ArquivoJPEG
```

sem necessariamente alterar toda a lógica da classe base.

Visualmente:

```text
Novo formato

   |
   ├── Novo ConcreteProduct
   |
   └── Novo ConcreteCreator
```

A estrutura existente continua sendo reutilizada.

---

# ➕ Adicionando um novo formato

Imagine que surgiu:

```text
WEBP
```

Em uma abordagem fortemente baseada em `if`:

```text
Alterar código existente
```

Na abordagem com Factory Method:

```text
Criar ArquivoWEBP

        +

Criar ExportadorWEBP
```

Conceitualmente:

```text
ArquivoWEBP
       ↑
       |
ExportadorWEBP
```

A lógica geral de exportação permanece.

---

# 🔬 Relação com o exemplo do telescópio

Esse é justamente o motivo de usarmos o cenário das imagens astronômicas.

O sistema possui:

```text
Uma mesma finalidade:

Exportar imagens
```

mas:

```text
Vários tipos de arquivos
```

Portanto:

```text
Exportar

↓

precisa criar

↓

um tipo de arquivo
```

E esse tipo de arquivo pode variar.

Esse é um cenário bastante natural para estudar o Factory Method.

---

# 📁 Exemplo da estrutura de arquivos

A implementação deste estudo poderá ser organizada conceitualmente desta maneira:

```text
FactoryMethod/
│
├── main.py
│
├── arquivo.py
│
├── arquivo_fits.py
│
├── arquivo_png.py
│
├── arquivo_tiff.py
│
├── exportador.py
│
├── exportador_fits.py
│
├── exportador_png.py
│
└── exportador_tiff.py
```

Uma organização alternativa pode separar Products e Creators em diretórios:

```text
FactoryMethod/
│
├── main.py
│
├── products/
│   ├── arquivo.py
│   ├── arquivo_fits.py
│   ├── arquivo_png.py
│   └── arquivo_tiff.py
│
└── creators/
    ├── exportador.py
    ├── exportador_fits.py
    ├── exportador_png.py
    └── exportador_tiff.py
```

O objetivo da estrutura é deixar visualmente claro:

```text
Products

e

Creators
```

---

# 🧪 O que será experimentado no projeto

Durante a implementação, a ideia será observar a evolução do código.

Primeiro:

```text
Implementação simples
```

Depois:

```text
Novos formatos
```

Depois:

```text
if / elif
```

E finalmente:

```text
Factory Method
```

Assim será possível perceber o problema que levou à criação do padrão.

O objetivo não é apenas decorar a estrutura.

É perceber:

```text
Problema

↓

Solução ingênua

↓

Novos problemas

↓

Necessidade de abstração

↓

Factory Method
```

---

# 🧠 O Factory Method não é sobre "criar qualquer objeto"

Essa é uma confusão comum.

O objetivo do padrão não é simplesmente:

```text
colocar o construtor dentro de um método
```

Se fizermos:

```python
def criar():
    return MinhaClasse()
```

isso sozinho não significa necessariamente que estamos usando Factory Method.

O padrão envolve uma estrutura maior:

```text
Creator

↓

Factory Method

↓

Product
```

e principalmente a possibilidade de subclasses definirem:

```text
qual produto concreto será criado
```

---

# 🧠 O verdadeiro objetivo é controlar a variação

Imagine:

```text
Exportar imagem
```

Essa operação não muda.

O que muda é:

```text
Qual formato será utilizado.
```

Portanto:

```text
Comportamento estável

+

Criação variável
```

é uma situação onde o Factory Method pode fazer sentido.

Visualmente:

```text
Fluxo estável

      +

Produto variável

      ↓

Factory Method
```

---

# 🎯 Quando utilizar Factory Method?

O Factory Method pode ser interessante quando:

- Uma classe não deve conhecer diretamente as classes concretas que precisa criar.
- Existe uma família ou conjunto de objetos relacionados.
- O tipo concreto criado pode variar.
- A criação de objetos precisa ser especializada.
- Subclasses podem decidir qual objeto será produzido.
- Novas implementações podem surgir no futuro.
- A classe possui um fluxo de negócio estável, mas a criação de um objeto utilizado nesse fluxo varia.
- Queremos reduzir acoplamento entre código de negócio e classes concretas.
- Queremos evitar grandes cadeias de `if/elif` responsáveis pela criação de objetos.

---

# 🚫 Quando não utilizar

O Factory Method não deve ser aplicado apenas porque:

```text
"Design Pattern é uma boa prática."
```

Ele pode ser desnecessário quando:

- Existe apenas um único tipo de produto.
- Não existe previsão ou necessidade de variação.
- A criação é extremamente simples.
- Não existe uma hierarquia de `Creator`.
- A abstração criada adicionaria mais complexidade do que valor.
- O código ficaria mais difícil de entender sem um benefício real.

Por exemplo:

```python
produto = Produto()
```

pode ser perfeitamente adequado quando:

```text
Existe apenas um Produto
```

e:

```text
Não existe necessidade de variação.
```

---

# 🟢 Prós

## Reduz acoplamento

O `Creator` não precisa depender diretamente de todos os produtos concretos.

Em vez de:

```text
Creator
 |
 ├── ProductA
 ├── ProductB
 └── ProductC
```

podemos ter:

```text
Creator
 |
 v
Product
```

---

## Facilita a extensão

Novos produtos podem ser adicionados criando novos:

```text
ConcreteProduct
```

e:

```text
ConcreteCreator
```

---

## Centraliza a criação no ponto correto

A lógica de criação fica concentrada no:

```text
Factory Method
```

e suas implementações.

---

## Favorece o polimorfismo

O código trabalha com:

```text
Product
```

enquanto recebe:

```text
ConcreteProduct
```

---

## Evita grandes condicionais

Podemos substituir:

```text
if
elif
elif
elif
```

por:

```text
sobrescrita de método
```

---

## Facilita manutenção

A lógica principal de negócio pode permanecer estável mesmo quando novos tipos de produtos aparecem.

---

# 🔴 Contras

## Aumenta a quantidade de classes

Pode ser necessário criar:

```text
Creator
ConcreteCreatorA
ConcreteCreatorB
ConcreteCreatorC
```

e:

```text
Product
ConcreteProductA
ConcreteProductB
ConcreteProductC
```

Isso aumenta a quantidade de código.

---

## Pode deixar a solução mais complexa

Um problema simples pode acabar envolvendo:

```text
Herança

+

Interfaces

+

Subclasses
```

quando uma solução direta seria suficiente.

---

## Existe forte relação com herança

A implementação tradicional do Factory Method utiliza subclasses para decidir qual produto será criado.

Consequentemente:

```text
Creator

↓

ConcreteCreator
```

faz parte da solução.

Isso pode não ser adequado em todos os projetos.

---

## Nem sempre uma hierarquia de creators faz sentido

O padrão se torna mais interessante quando realmente existe uma variação entre os criadores.

Se não existe:

```text
ConcreteCreatorA
ConcreteCreatorB
```

a estrutura pode ser desnecessária.

---

# 🧠 Factory Method e herança

Um ponto importante apresentado no padrão é:

> **A decisão sobre o objeto criado é feita pelas subclasses.**

Por exemplo:

```text
Creator
     |
     ├── CreatorA
     |
     └── CreatorB
```

Cada subclasse possui sua própria implementação:

```text
CreatorA
   |
   └── ProductA
```

```text
CreatorB
   |
   └── ProductB
```

Portanto:

```text
Herança

+

Polimorfismo

+

Criação de objetos
```

são elementos fundamentais da abordagem clássica.

---

# 🔄 Fluxo completo do padrão

Podemos resumir todo o processo assim:

```text
Cliente

   |
   v

Creator

   |
   | executa operação
   v

factory_method()

   |
   v

Product

   |
   └── pode ser ConcreteProduct
```

Quando usamos uma implementação concreta:

```text
Cliente

   |
   v

ConcreteCreator

   |
   v

factory_method()

   |
   v

ConcreteProduct
```

O cliente sabe:

```text
"Preciso de um Creator."
```

e:

```text
"Esse Creator produz um Product."
```

Mas não precisa necessariamente conhecer toda a lógica de criação.

---

# 📚 Factory Method em linguagem simples

Podemos pensar assim:

Imagine uma empresa que possui uma regra:

```text
"Precisamos fabricar um produto."
```

A empresa define:

```text
Criar produto
```

Mas cada filial decide:

```text
Qual produto específico fabricar.
```

Então:

```text
Empresa
   |
   └── criar_produto()
```

Uma filial:

```text
Filial A

↓

cria Produto A
```

Outra:

```text
Filial B

↓

cria Produto B
```

A regra geral continua sendo a mesma:

```text
Criar produto
```

Mas a implementação varia.

---

# 🔭 Aplicando essa analogia ao telescópio

No nosso projeto:

```text
Creator

↓

Exportador
```

A operação é:

```text
Exportar imagens
```

Mas o formato muda.

Portanto:

```text
ExportadorFITS
        |
        └── cria ArquivoFITS
```

```text
ExportadorPNG
        |
        └── cria ArquivoPNG
```

```text
ExportadorTIFF
        |
        └── cria ArquivoTIFF
```

A regra geral:

```text
Exportar imagens
```

continua a mesma.

O que varia:

```text
Tipo de arquivo
```

é delegado ao Factory Method.

---

# 🧩 Factory Method em uma visão geral

```text
                         Factory Method
                                |
                                v
                   Método responsável por criar
                                |
                                v
                             Product
                                |
                ┌───────────────┼───────────────┐
                |               |               |
                v               v               v
          ProductFITS      ProductPNG      ProductTIFF
```

Do lado do Creator:

```text
                         Creator
                            |
                    factory_method()
                            |
             ┌──────────────┼──────────────┐
             |              |              |
             v              v              v
       CreatorFITS      CreatorPNG     CreatorTIFF
```

Com as relações:

```text
CreatorFITS
    |
    └── factory_method()
            |
            v
       ProductFITS
```

```text
CreatorPNG
    |
    └── factory_method()
            |
            v
        ProductPNG
```

```text
CreatorTIFF
    |
    └── factory_method()
            |
            v
        ProductTIFF
```

---

# 📌 Relação entre os participantes

Podemos memorizar os papéis dessa forma:

```text
Product

↓

O que será criado
```

```text
ConcreteProduct

↓

Implementação concreta do produto
```

```text
Creator

↓

Define como a operação utiliza o produto
e declara o Factory Method
```

```text
ConcreteCreator

↓

Decide qual produto concreto criar
```

```text
Client

↓

Utiliza a estrutura
```

---

# 🧠 Uma frase para memorizar

Uma maneira simples de memorizar o Factory Method é:

> **"A classe define o que precisa ser criado, mas a subclasse decide o que será criado."**

Ou ainda:

```text
Creator

↓

"Preciso de um Product."

ConcreteCreator

↓

"Eu decido qual Product criar."
```

---

# 📝 Resumo Final

O **Factory Method** é um Design Pattern **criacional** utilizado para **delegar a criação de objetos para métodos especializados**, permitindo que subclasses definam qual implementação concreta será instanciada.

Seu objetivo principal é reduzir o acoplamento entre:

```text
Código de negócio
```

e:

```text
Classes concretas utilizadas na criação.
```

A estrutura básica pode ser resumida como:

```text
Creator

   |
   └── Factory Method
            |
            v
         Product
```

Com subclasses:

```text
ConcreteCreatorA
       |
       └── cria ConcreteProductA
```

e:

```text
ConcreteCreatorB
       |
       └── cria ConcreteProductB
```

No problema deste projeto, temos um sistema que precisa exportar imagens astronômicas em diferentes formatos:

```text
FITS
PNG
TIFF
```

Uma solução ingênua poderia colocar toda a criação dentro de:

```text
if / elif / else
```

por exemplo:

```python
if formato == "fits":
    arquivo = ArquivoFITS()

elif formato == "png":
    arquivo = ArquivoPNG()

elif formato == "tiff":
    arquivo = ArquivoTIFF()
```

O problema é que essa classe passa a conhecer todos os tipos concretos.

Com o Factory Method, a responsabilidade é separada.

A classe base pode dizer:

```text
"Preciso de um Arquivo."
```

e uma subclasse decide:

```text
"Vou criar ArquivoFITS."
```

ou:

```text
"Vou criar ArquivoPNG."
```

ou:

```text
"Vou criar ArquivoTIFF."
```

Assim:

```text
Fluxo da operação

↓

permanece na classe base
```

enquanto:

```text
Escolha do objeto concreto

↓

fica no Factory Method
```

No exemplo das imagens astronômicas:

```text
Exportador
     |
     └── criar_arquivo()
              |
              v
            Arquivo
```

e:

```text
ExportadorFITS
      |
      └── ArquivoFITS
```

```text
ExportadorPNG
      |
      └── ArquivoPNG
```

```text
ExportadorTIFF
      |
      └── ArquivoTIFF
```

A ideia mais importante para memorizar é:

> **Factory Method = definir um método para criação de objetos e permitir que subclasses decidam qual classe concreta será instanciada.**

Ou, de maneira ainda mais simples:

```text
Creator

↓

Define o processo

↓

Factory Method

↓

Subclasse escolhe o produto
```

E no nosso projeto:

```text
Exportador

↓

exportar()

↓

criar_arquivo()

↓

ArquivoFITS / ArquivoPNG / ArquivoTIFF
```

Portanto, a essência do padrão é:

> **"Não deixe o código que executa uma operação ficar fortemente acoplado ao código que decide qual objeto concreto deve ser criado."**

O **Factory Method** cria um ponto de extensão para essa decisão e utiliza **abstração, herança e polimorfismo** para permitir diferentes produtos sem espalhar sua lógica de criação pelo sistema.
