# Composite - Reference: <https://refactoring.guru/pt-br/design-patterns/composite>

## 📌 Objetivo

O **Composite** é um Design Pattern **estrutural** utilizado para **compor objetos em estruturas de árvore**, representando hierarquias do tipo:

> **parte-todo**

A principal ideia do padrão é permitir que o cliente trate:

- objetos individuais;
- grupos de objetos;
- estruturas compostas por vários objetos;

de maneira **uniforme**.

Em outras palavras, o cliente não precisa saber se está trabalhando com:

```text
Um objeto individual
```

ou:

```text
Um grupo de objetos
```

Por exemplo, imagine um sistema de arquivos.

O cliente pode querer descobrir o tamanho de um item:

```text
item.tamanho()
```

Mas esse `item` pode ser:

```text
Arquivo
```

ou:

```text
Pasta
```

O arquivo possui um tamanho próprio.

Já a pasta possui um tamanho calculado a partir dos objetos que ela contém.

Mesmo assim, o cliente não precisa perguntar:

```text
Isso é um arquivo?

ou

Isso é uma pasta?
```

Ele simplesmente utiliza:

```text
item.tamanho()
```

E cada objeto sabe como responder.

A ideia central do Composite pode ser resumida assim:

> **Organizar objetos em estruturas de árvore e permitir que objetos individuais e composições de objetos sejam tratados de maneira uniforme.**

---

# 🌳 O Problema

Imagine que estamos desenvolvendo um sistema de armazenamento de imagens produzidas por telescópios espaciais.

Essas imagens são organizadas em uma estrutura semelhante a um sistema de arquivos.

Por exemplo:

```text
acervo/
│
├── 2026-08-01/
│   │
│   ├── hubble_001.fits        450 MB
│   ├── hubble_002.fits        450 MB
│   │
│   └── calibracao/
│       ├── dark_frame.fits     80 MB
│       └── flat_field.fits     80 MB
│
├── 2026-08-02/
│   │
│   ├── hubble_003.fits        450 MB
│   │
│   └── processadas/
│       │
│       └── mosaico/
│           ├── andromeda.tiff       1200 MB
│           └── hubble_003_lut.png      2 MB
│
└── README.md                  0.01 MB
```

O sistema possui:

```text
Arquivos
```

e:

```text
Pastas
```

Mas existe uma característica importante:

> Uma pasta pode conter arquivos e outras pastas.

Por exemplo:

```text
Pasta
│
├── Arquivo
│
├── Arquivo
│
└── Pasta
    │
    ├── Arquivo
    │
    └── Pasta
        │
        └── Arquivo
```

Portanto, temos uma estrutura hierárquica em forma de:

> **árvore**

---

# ❓ Os requisitos

Agora imagine que novos requisitos surgiram para o sistema.

Precisamos responder perguntas como:

```text
Qual é o tamanho total da pasta 2026-08-02?
```

Também:

```text
Quantos arquivos existem dentro do acervo?
```

E:

```text
Onde está localizado o arquivo andromeda.tiff?
```

Além disso, podemos querer listar toda a estrutura:

```text
acervo/
│
├── 2026-08-01/
│   ├── hubble_001.fits
│   ├── hubble_002.fits
│   └── calibracao/
│       ├── dark_frame.fits
│       └── flat_field.fits
│
└── 2026-08-02/
    ├── hubble_003.fits
    └── processadas/
        └── mosaico/
            ├── andromeda.tiff
            └── hubble_003_lut.png
```

Inicialmente, essas operações parecem simples.

Mas existe um problema conceitual.

Temos dois tipos principais de objetos:

```text
Arquivo
```

e:

```text
Pasta
```

Eles possuem comportamentos diferentes.

---

# 📄 Arquivos possuem valores próprios

Um arquivo possui informações próprias.

Por exemplo:

```text
andromeda.tiff

1200 MB
```

Portanto, quando perguntamos:

```text
Qual é o tamanho deste arquivo?
```

A resposta é direta:

```text
1200 MB
```

Podemos representar:

```text
Arquivo

↓

Possui um valor próprio

↓

Responde diretamente
```

O arquivo não precisa perguntar nada para outros objetos.

---

# 📁 Pastas possuem outros objetos

Uma pasta funciona de maneira diferente.

Por exemplo:

```text
mosaico/
│
├── andromeda.tiff
│      1200 MB
│
└── hubble_003_lut.png
       2 MB
```

Quando perguntamos:

```text
Qual é o tamanho da pasta mosaico?
```

A pasta não possui necessariamente um único valor próprio.

Ela precisa perguntar:

```text
Qual é o tamanho de cada filho?
```

Então:

```text
andromeda.tiff

↓

1200 MB
```

e:

```text
hubble_003_lut.png

↓

2 MB
```

Depois:

```text
1200 MB

+

2 MB

↓

1202 MB
```

Portanto:

```text
Pasta

↓

Pergunta aos filhos

↓

Obtém os resultados

↓

Combina os resultados
```

---

# 🔁 O problema da recursão

Agora imagine uma estrutura maior:

```text
2026-08-02/
│
├── hubble_003.fits
│      450 MB
│
└── processadas/
       │
       └── mosaico/
            │
            ├── andromeda.tiff
            │      1200 MB
            │
            └── hubble_003_lut.png
                   2 MB
```

Para calcular o tamanho de:

```text
2026-08-02/
```

precisamos perguntar:

```text
Qual é o tamanho de hubble_003.fits?
```

Resultado:

```text
450 MB
```

Depois:

```text
Qual é o tamanho de processadas/?
```

Mas `processadas/` também é uma pasta.

Portanto, ela precisa perguntar aos seus filhos.

Ela chega em:

```text
mosaico/
```

Que também pergunta aos seus filhos.

Portanto:

```text
2026-08-02/

↓

processadas/

↓

mosaico/

↓

arquivos
```

Temos uma estrutura naturalmente:

> **recursiva**

Uma pasta pode conter outra pasta.

Que pode conter outra pasta.

Que pode conter arquivos.

Indefinidamente.

---

# 💥 Uma possível implementação sem Composite

Uma primeira tentativa poderia ser tratar arquivos e pastas separadamente.

Por exemplo:

```text
Arquivo

↓

Possui uma lógica
```

e:

```text
Pasta

↓

Possui outra lógica
```

Então, sempre que o cliente recebe um objeto, ele precisa descobrir com qual tipo está trabalhando.

Conceitualmente:

```text
Cliente

↓

Isso é um Arquivo?

      │
   ┌──┴──┐
   │     │
  Sim   Não
   │     │
   v     v
Executa  Isso é uma Pasta?
lógica        │
           ┌──┴──┐
           │     │
          Sim   Não
           │
           v
      Executa lógica
```

Em linguagens orientadas a objetos, isso pode resultar em várias verificações de tipo.

Por exemplo:

```text
É Arquivo?

É Pasta?

É Arquivo?

É Pasta?
```

Essas verificações podem começar a aparecer em várias partes do sistema.

---

# 🚨 O problema dos tipos espalhados

Imagine que precisamos implementar as seguintes operações:

```text
Calcular tamanho
```

```text
Contar arquivos
```

```text
Buscar por nome
```

```text
Listar em árvore
```

Para cada operação, poderíamos precisar diferenciar:

```text
Arquivo
```

e:

```text
Pasta
```

Visualmente:

```text
Calcular tamanho

├── Arquivo?
└── Pasta?


Contar arquivos

├── Arquivo?
└── Pasta?


Buscar por nome

├── Arquivo?
└── Pasta?


Listar estrutura

├── Arquivo?
└── Pasta?
```

A lógica que diferencia os tipos começa a ficar espalhada pelo sistema.

---

# 🔴 O problema de extensibilidade

Agora imagine que futuramente seja criado um novo tipo de objeto.

Por exemplo:

```text
Atalho
```

Ou:

```text
Arquivo Compactado
```

Ou:

```text
Link Simbólico
```

Sem uma boa abstração, várias funcionalidades existentes poderiam precisar ser modificadas.

Por exemplo:

```text
Calcular tamanho

↓

Modificar
```

```text
Contar arquivos

↓

Modificar
```

```text
Buscar

↓

Modificar
```

```text
Listar

↓

Modificar
```

Ou seja:

```text
Novo tipo

↓

Modificar várias funcionalidades existentes
```

Isso pode gerar um sistema difícil de manter.

---

# 🧠 Mas por que o cliente precisa saber?

Existe uma pergunta conceitual importante.

Imagine que o cliente deseja saber:

```text
Qual é o tamanho deste item?
```

Por que ele deveria precisar saber se o item é:

```text
Arquivo
```

ou:

```text
Pasta?
```

A pergunta continua sendo:

```text
Qual é o tamanho?
```

Portanto, seria interessante que tanto arquivos quanto pastas respondessem à mesma pergunta.

Algo como:

```text
item.tamanho()
```

Independentemente de o objeto ser:

```text
Arquivo
```

ou:

```text
Pasta
```

É exatamente esse tipo de problema que o **Composite** resolve.

---

# 💡 A Ideia do Composite

A solução é criar uma abstração comum.

Podemos imaginar:

```text
Item
```

Essa abstração representa qualquer elemento da estrutura.

Então:

```text
                    Item
                     │
            ┌────────┴────────┐
            │                 │
            v                 v
         Arquivo             Pasta
```

O cliente trabalha apenas com:

```text
Item
```

Em vez de depender diretamente de:

```text
Arquivo
```

ou:

```text
Pasta
```

Assim, o cliente pode perguntar:

```text
Qual é o tamanho?
```

através de uma única operação conceitual:

```text
item.tamanho()
```

Cada objeto responde de acordo com sua própria natureza.

---

# 🌱 Leaf — A Folha

No Composite, um objeto individual que não possui filhos é chamado de:

> **Leaf**

Ou:

> **Folha**

No nosso exemplo:

```text
Arquivo
```

é uma folha.

Por exemplo:

```text
hubble_001.fits

450 MB
```

O arquivo não possui outros objetos dentro dele.

Portanto:

```text
Arquivo

↓

Não possui filhos

↓

Possui comportamento próprio
```

Quando recebe uma operação, normalmente responde diretamente.

Por exemplo:

```text
Qual é seu tamanho?

↓

450 MB
```

---

# 🌳 Composite — O Composto

Um objeto que pode conter outros objetos é chamado de:

> **Composite**

Ou:

> **Composto / Contêiner**

No nosso exemplo:

```text
Pasta
```

é um Composite.

Uma pasta pode possuir:

```text
Arquivo
```

ou:

```text
Outra Pasta
```

Por exemplo:

```text
Pasta

├── Arquivo
│
├── Arquivo
│
└── Pasta
    │
    ├── Arquivo
    │
    └── Arquivo
```

A principal diferença é:

```text
Leaf

↓

Não possui filhos
```

Enquanto:

```text
Composite

↓

Possui filhos
```

Mas ambos podem ser tratados como:

```text
Component
```

ou, no nosso exemplo:

```text
Item
```

---

# 🔄 A uniformidade

Essa é uma das ideias mais importantes do padrão.

O cliente pode trabalhar com:

```text
Item
```

Sem precisar saber se o objeto concreto é:

```text
Arquivo
```

ou:

```text
Pasta
```

Visualmente:

```text
Cliente

   │

   │ pergunta: tamanho()

   v

  Item

 /   \

v     v

Arquivo  Pasta
```

Ambos respondem à mesma operação.

Porém, internamente, cada um possui uma lógica diferente.

```text
Arquivo

↓

Retorna seu próprio tamanho
```

Enquanto:

```text
Pasta

↓

Pergunta aos filhos

↓

Obtém os tamanhos

↓

Soma os resultados
```

A diferença de comportamento fica encapsulada dentro dos próprios objetos.

---

# 🔁 Onde entra a recursão?

A recursão é uma parte fundamental do Composite.

Imagine:

```text
acervo/
│
├── arquivo_1
│
└── pasta_A/
    │
    ├── arquivo_2
    │
    └── pasta_B/
        │
        └── arquivo_3
```

Quando perguntamos:

```text
Qual é o tamanho do acervo?
```

O processo conceitual é:

```text
acervo

↓

Pergunta aos seus filhos
```

Um dos filhos é:

```text
arquivo_1

↓

Responde diretamente
```

Outro filho é:

```text
pasta_A

↓

Pergunta aos seus próprios filhos
```

Um dos filhos de `pasta_A` é:

```text
pasta_B

↓

Pergunta aos seus próprios filhos
```

Até chegar em:

```text
arquivo_3

↓

Responde diretamente
```

Portanto:

```text
Composite

↓

Delegação para os filhos

↓

Filho pode ser Leaf

ou

↓

Filho pode ser outro Composite

↓

Repete o processo
```

---

# 🧠 A recursão sai do cliente

Sem Composite, o cliente poderia precisar controlar toda a navegação pela árvore.

Ele precisaria saber:

```text
Isso é arquivo?

Isso é pasta?

Preciso percorrer os filhos?

Preciso chamar novamente a operação?
```

Com Composite, a ideia é diferente.

O cliente apenas envia a mensagem:

```text
item.operacao()
```

A própria estrutura se encarrega de continuar o processo.

Visualmente:

```text
Cliente

   │

   v

Composite

   │

   v

Filho

   │

   v

Outro Composite

   │

   v

Outro Filho
```

Portanto:

> **A recursão sai do cliente e entra na estrutura de objetos.**

Essa é uma das características mais importantes do Composite.

---

# 🏗️ Estrutura conceitual do Composite

A estrutura clássica pode ser representada assim:

```text
                    Component
                        │
        ┌───────────────┴───────────────┐
        │                               │
        v                               v
      Leaf                         Composite
                                        │
                                        │ contém
                                        v
                                   Component
                                  /         \
                                 /           \
                              Leaf        Composite
```

No nosso exemplo:

```text
                    Item
                     │
          ┌──────────┴──────────┐
          │                     │
          v                     v
       Arquivo                Pasta
                                │
                                │ contém
                                v
                               Item
                          /      |      \
                         /       |       \
                    Arquivo   Pasta   Arquivo
```

Existe uma ideia muito importante aqui.

Uma pasta não deve necessariamente depender exclusivamente de:

```text
Arquivos
```

Ela trabalha com:

```text
Itens
```

Portanto, seus filhos podem ser:

```text
Arquivos
```

ou:

```text
Pastas
```

Como uma pasta também é um `Item`, ela pode estar dentro de outra pasta.

É isso que permite criar uma árvore.

---

# 🧩 Participantes do Composite

O Composite geralmente possui alguns participantes principais.

---

## 🔷 Component

O `Component` representa a abstração comum.

No nosso exemplo:

```text
Item
```

Ele representa qualquer elemento da estrutura.

Conceitualmente, define quais operações podem ser realizadas.

Por exemplo:

```text
Calcular tamanho

Contar arquivos

Buscar

Listar
```

A grande vantagem é que o cliente trabalha com a abstração.

Assim:

```text
Cliente

↓

Item
```

Em vez de:

```text
Cliente

↓

Arquivo ou Pasta?
```

---

## 🌱 Leaf

O `Leaf` representa um objeto individual.

No nosso exemplo:

```text
Arquivo
```

Um arquivo:

```text
Não possui filhos
```

Ele responde diretamente às operações.

Por exemplo:

```text
Qual é o tamanho?

↓

450 MB
```

Para contar arquivos:

```text
Sou um arquivo

↓

1
```

A folha representa normalmente o nível final da árvore.

---

## 🌳 Composite

O `Composite` representa um objeto que possui outros objetos.

No nosso exemplo:

```text
Pasta
```

A pasta contém vários:

```text
Itens
```

Esses itens podem ser:

```text
Arquivos
```

ou:

```text
Pastas
```

Quando recebe uma operação, o Composite normalmente:

```text
Percorre seus filhos

↓

Delega a operação para cada um

↓

Combina os resultados
```

Por exemplo:

```text
Pasta

↓

Pergunta tamanho para cada filho

↓

Soma os resultados

↓

Retorna o total
```

---

## 👤 Client

O `Client` é o código que utiliza a estrutura.

Ele monta e manipula a árvore.

O ponto mais importante é:

> O cliente deve trabalhar com a abstração comum.

O cliente não deve precisar conhecer todos os detalhes da estrutura interna.

Ele deve poder perguntar:

```text
Qual é o tamanho deste item?
```

Ou:

```text
Quantos arquivos existem neste item?
```

Sem precisar saber exatamente qual é o tipo concreto.

---

# 📊 Participantes no nosso exemplo

| Participante  | Exemplo   | Responsabilidade                        |
| ------------- | --------- | --------------------------------------- |
| **Component** | `Item`    | Define uma abstração comum              |
| **Leaf**      | `Arquivo` | Representa um objeto individual         |
| **Composite** | `Pasta`   | Representa um contêiner de outros itens |
| **Client**    | Aplicação | Utiliza e monta a estrutura             |

---

# 💾 Exemplo: calcular tamanho

Considere:

```text
2026-08-02/
│
├── hubble_003.fits
│      450 MB
│
└── processadas/
       │
       └── mosaico/
            │
            ├── andromeda.tiff
            │      1200 MB
            │
            └── hubble_003_lut.png
                   2 MB
```

Quando perguntamos:

```text
Qual é o tamanho de 2026-08-02?
```

O processo acontece conceitualmente assim:

```text
2026-08-02/

↓

Pergunta aos filhos
```

Primeiro:

```text
hubble_003.fits

↓

450 MB
```

Depois:

```text
processadas/

↓

Pergunta aos seus filhos
```

Chegando em:

```text
mosaico/

↓

Pergunta aos seus filhos
```

Os arquivos respondem:

```text
andromeda.tiff

↓

1200 MB
```

e:

```text
hubble_003_lut.png

↓

2 MB
```

Então:

```text
mosaico/

↓

1200 + 2

↓

1202 MB
```

Depois:

```text
processadas/

↓

1202 MB
```

Finalmente:

```text
2026-08-02/

↓

450 + 1202

↓

1652 MB
```

Visualmente:

```text
Cliente

   │

   │ tamanho()

   v

2026-08-02/

   │

   ├─────────────────────┐
   │                     │
   v                     v

450 MB              processadas/

                          │

                          v

                      mosaico/

                     /         \
                    v           v

               1200 MB        2 MB


Resultado:

450 + 1200 + 2

=

1652 MB
```

---

# 🔢 Exemplo: contar arquivos

Outro requisito é:

```text
Quantos arquivos existem dentro do acervo?
```

Um arquivo pode responder:

```text
Sou um arquivo

↓

1
```

Uma pasta responde:

```text
Perguntar para cada filho

↓

Somar as respostas
```

Por exemplo:

```text
Pasta

├── Arquivo → 1
│
├── Arquivo → 1
│
└── Pasta
    │
    ├── Arquivo → 1
    │
    └── Arquivo → 1
```

Resultado:

```text
1 + 1 + 1 + 1

=

4 arquivos
```

Mais uma vez, a estrutura é percorrida naturalmente.

---

# 🔎 Exemplo: buscar um arquivo

Outro requisito é descobrir:

```text
Onde está andromeda.tiff?
```

A busca percorre a árvore.

Conceitualmente:

```text
acervo/

↓

Verificar filhos
```

Depois:

```text
2026-08-01/

↓

Arquivo encontrado?

Não
```

Depois:

```text
2026-08-02/

↓

Verificar filhos
```

Depois:

```text
processadas/

↓

Verificar filhos
```

Depois:

```text
mosaico/

↓

Verificar filhos
```

Finalmente:

```text
andromeda.tiff

↓

Encontrado!
```

O resultado poderia indicar:

```text
acervo/2026-08-02/processadas/mosaico/andromeda.tiff
```

A busca acontece navegando naturalmente pela árvore.

---

# 📁 Exemplo-problema deste projeto

Neste projeto, o Composite será estudado através de um sistema simplificado de armazenamento de imagens extraterrestres.

A estrutura será semelhante a:

```text
acervo/
│
├── 2026-08-01/
│   │
│   ├── hubble_001.fits        450 MB
│   ├── hubble_002.fits        450 MB
│   │
│   └── calibracao/
│       ├── dark_frame.fits     80 MB
│       └── flat_field.fits     80 MB
│
├── 2026-08-02/
│   │
│   ├── hubble_003.fits        450 MB
│   │
│   └── processadas/
│       │
│       └── mosaico/
│           ├── andromeda.tiff       1200 MB
│           └── hubble_003_lut.png      2 MB
│
└── README.md                  0.01 MB
```

O objetivo será representar essa estrutura como uma árvore.

Cada elemento poderá ser tratado através de uma abstração comum.

Os requisitos conceituais incluem:

```text
Calcular o tamanho total de uma pasta
```

```text
Contar quantos arquivos existem em uma estrutura
```

```text
Buscar um arquivo pelo nome
```

```text
Encontrar a localização de um arquivo
```

```text
Listar a estrutura em formato de árvore
```

O objetivo é que o cliente não precise diferenciar explicitamente:

```text
Arquivo
```

de:

```text
Pasta
```

A pergunta:

```text
Qual é o tamanho deste item?
```

continua sendo a mesma.

A pergunta:

```text
Quantos arquivos existem neste item?
```

também continua sendo a mesma.

A estrutura interna é responsável por descobrir como responder.

---

# ♾️ Uma estrutura naturalmente recursiva

Uma das características fundamentais do Composite é que um Composite pode conter objetos da mesma abstração que ele próprio implementa.

No nosso exemplo:

```text
Pasta

↓

contém

↓

Item
```

Mas:

```text
Item
```

pode ser:

```text
Arquivo
```

ou:

```text
Pasta
```

Portanto:

```text
Pasta

↓

contém outra Pasta

↓

que contém outra Pasta

↓

que contém Arquivos
```

A profundidade pode crescer indefinidamente.

Por exemplo:

```text
Pasta
│
└── Pasta
    │
    └── Pasta
        │
        └── Pasta
            │
            └── Arquivo
```

Essa capacidade é exatamente o que torna o Composite apropriado para estruturas em árvore.

---

# 🆚 Sem Composite

Sem uma abstração comum, o cliente pode acabar dependendo dos tipos concretos.

Conceitualmente:

```text
Cliente

↓

Isso é Arquivo?

   │
   ├── Sim → Executar lógica de Arquivo
   │
   └── Não

        ↓

    Isso é Pasta?

        │
        └── Sim → Executar lógica de Pasta
```

O cliente precisa conhecer os tipos.

---

# 🆚 Com Composite

Com Composite:

```text
Cliente

   │

   │ operation()

   v

Component

   │

   ├───────────────┐
   │               │
   v               v

Leaf          Composite
```

O cliente simplesmente trabalha com:

```text
Component
```

Ou, no nosso exemplo:

```text
Item
```

Ele envia a mensagem.

Cada objeto sabe como responder.

---

# 🎯 Quando utilizar Composite?

O Composite é especialmente útil quando:

- existe uma estrutura hierárquica;
- existe uma relação parte-todo;
- objetos individuais e grupos de objetos devem ser tratados da mesma maneira;
- a estrutura possui formato de árvore;
- objetos podem conter outros objetos semelhantes;
- queremos evitar verificações constantes de tipo;
- queremos encapsular a recursão dentro da estrutura;
- o cliente não deveria precisar saber a diferença entre um objeto individual e uma composição.

---

# 🌍 Exemplos comuns de Composite

O Composite aparece naturalmente em diversos tipos de sistemas.

---

## 📁 Sistemas de arquivos

```text
Pasta

↓

contém

↓

Arquivos e Pastas
```

Exemplo:

```text
home/
│
├── documentos/
│   ├── trabalho.pdf
│   └── faculdade/
│       └── atividade.pdf
│
└── imagens/
    └── foto.png
```

---

## 🖥️ Interfaces gráficas

Uma interface pode possuir:

```text
Janela

↓

Painel

↓

Botões

Campos

Outros painéis
```

Um painel pode conter outros componentes.

Esses componentes podem novamente conter outros componentes.

---

## 🏢 Estruturas organizacionais

Por exemplo:

```text
Empresa

↓

Departamento

↓

Equipe

↓

Funcionários
```

Uma organização possui uma estrutura hierárquica.

---

## 📋 Menus

```text
Menu

↓

Submenu

↓

Itens
```

Um menu pode conter:

```text
Itens
```

e:

```text
Outros menus
```

---

## 🌐 Estruturas HTML

Uma página HTML também pode ser vista como uma árvore.

Por exemplo:

```text
html
│
└── body
    │
    ├── header
    │
    ├── main
    │   │
    │   ├── section
    │   │
    │   └── section
    │
    └── footer
```

Elementos podem conter outros elementos.

---

# 🧠 Composite e Polimorfismo

O Composite utiliza fortemente:

> **Polimorfismo**

O cliente possui uma referência para uma abstração.

Mas o objeto concreto pode variar.

Por exemplo:

```text
Item
```

Pode representar:

```text
Arquivo
```

ou:

```text
Pasta
```

Quando uma operação é solicitada, cada objeto responde de acordo com sua própria implementação.

A mesma pergunta:

```text
Qual é o tamanho?
```

gera comportamentos diferentes.

Para um arquivo:

```text
Retornar tamanho próprio
```

Para uma pasta:

```text
Perguntar aos filhos

↓

Somar resultados
```

A mensagem é a mesma.

O comportamento é diferente.

---

# 🧠 Composite e o Princípio Aberto/Fechado

Um dos benefícios conceituais do Composite é reduzir a necessidade de modificar o cliente quando novos tipos de objetos são adicionados.

Imagine que futuramente seja criado:

```text
Arquivo Compactado
```

Se esse novo objeto também puder ser tratado como um:

```text
Item
```

o cliente pode continuar fazendo as mesmas perguntas.

Por exemplo:

```text
Qual é o tamanho?
```

O novo objeto pode responder de acordo com sua própria lógica.

Não é necessário que o cliente conheça todos os tipos existentes.

Isso favorece o princípio:

> **Aberto para extensão e fechado para modificação.**

Ou seja:

```text
Novo tipo

↓

Adicionar uma nova implementação

↓

Sem necessariamente modificar o cliente
```

---

# 🟢 Prós

## Uniformidade

O cliente trata:

```text
Objeto individual
```

e:

```text
Grupo de objetos
```

da mesma maneira.

---

## Redução de condicionais

Reduz a necessidade de espalhar verificações como:

```text
É Arquivo?

É Pasta?
```

pelo sistema.

---

## Estruturas hierárquicas naturais

É excelente para representar:

```text
Árvores
```

e:

```text
Hierarquias parte-todo
```

---

## Recursão encapsulada

A lógica de percorrer a estrutura fica dentro dos próprios objetos.

O cliente não precisa controlar manualmente toda a recursão.

---

## Facilidade para o cliente

O cliente trabalha com uma abstração comum.

---

## Extensibilidade

Novos tipos podem ser adicionados à estrutura com menor necessidade de modificar o código cliente.

---

# 🔴 Contras

## Pode aumentar a abstração

Mesmo um problema relativamente simples pode precisar de:

```text
Component

+

Leaf

+

Composite
```

Isso adiciona novas camadas ao sistema.

---

## Pode tornar o design mais complexo

Estruturas recursivas podem ser mais difíceis de entender inicialmente.

---

## Algumas operações podem não fazer sentido para todos

Um Composite pode possuir filhos.

Uma folha não.

Isso exige cuidado ao definir quais responsabilidades pertencem à abstração comum.

---

## Pode ser exagero

Para estruturas pequenas, sem hierarquia e sem relação parte-todo, o Composite pode adicionar complexidade desnecessária.

Como qualquer Design Pattern:

> **O Composite deve ser utilizado para resolver um problema existente, e não apenas porque o padrão existe.**

---

# 📌 Ideia principal para memorizar

O Composite pode ser resumido assim:

```text
Objetos individuais

+

Grupos de objetos

↓

Mesma abstração
```

Ou:

```text
Cliente

↓

Não precisa saber

↓

Leaf ou Composite?
```

O cliente simplesmente faz uma solicitação.

Cada objeto responde de acordo com sua natureza.

---

# 📝 Resumo Final

O **Composite** é um Design Pattern estrutural utilizado para representar estruturas hierárquicas em forma de árvore.

Ele é especialmente útil quando existe uma relação:

```text
parte-todo
```

Sua principal característica é permitir que:

```text
Objetos individuais
```

e:

```text
Composições de objetos
```

sejam tratados de maneira uniforme.

No exemplo do sistema de armazenamento de imagens extraterrestres:

```text
Arquivo

↓

Leaf
```

Enquanto:

```text
Pasta

↓

Composite
```

Ambos fazem parte da mesma abstração:

```text
Item
```

Portanto, o cliente não precisa saber se está trabalhando com um arquivo ou uma pasta.

Ele simplesmente faz uma pergunta.

Por exemplo:

```text
Qual é o tamanho?
```

Uma folha responde diretamente.

Um Composite delega a pergunta aos seus filhos.

Esses filhos podem novamente ser:

```text
Folhas
```

ou:

```text
Composites
```

Criando uma estrutura recursiva.

A ideia mais importante para memorizar é:

> **Composite = organizar objetos em estruturas de árvore e permitir que objetos individuais e grupos de objetos sejam tratados da mesma maneira.**

No exemplo:

```text
Cliente

   │

   v

Item

   │

   ├───────────────┐
   │               │
   v               v

Arquivo          Pasta

                   │

                   v

              outros Itens
```

Assim, perguntas como:

```text
Qual é o tamanho desta pasta?
```

```text
Quantos arquivos existem aqui?
```

```text
Onde está este arquivo?
```

podem ser resolvidas navegando naturalmente pela árvore.

O cliente não precisa controlar a recursão manualmente.

A própria estrutura se encarrega de percorrer seus elementos.

> **A essência do Composite é esconder a complexidade de uma estrutura hierárquica atrás de uma abstração uniforme.**
