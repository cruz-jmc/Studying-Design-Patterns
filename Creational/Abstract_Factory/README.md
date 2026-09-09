# Abstract Factory - Reference: https://refactoring.guru/pt-br/design-patterns/abstract-factory

## 📌 Objetivo

O **Abstract Factory** é um Design Pattern **criacional** utilizado para **criar famílias de objetos relacionados ou dependentes sem que o código cliente precise conhecer as classes concretas desses objetos**.

A principal ideia do padrão é separar:

```text
A criação dos objetos
```

da:

```text
Utilização dos objetos
```

Além disso, o Abstract Factory permite garantir que os objetos criados pertençam a uma mesma:

> **família de produtos compatíveis entre si.**

Por exemplo, imagine que estamos desenvolvendo uma aplicação que possui diferentes temas visuais.

Podemos ter:

```text
Tema Claro
```

e:

```text
Tema Escuro
```

Cada tema possui vários componentes:

```text
Botão
Checkbox
Janela
```

No tema claro:

```text
Botão Claro
Checkbox Claro
Janela Clara
```

No tema escuro:

```text
Botão Escuro
Checkbox Escuro
Janela Escura
```

Existe uma relação importante entre esses objetos.

Não queremos criar uma combinação como:

```text
Botão Claro
+
Checkbox Escuro
+
Janela Clara
```

Pois os objetos pertencem a famílias diferentes.

Queremos trabalhar com famílias completas:

```text
Família Clara

Botão Claro
Checkbox Claro
Janela Clara
```

ou:

```text
Família Escura

Botão Escuro
Checkbox Escuro
Janela Escura
```

A ideia central do Abstract Factory pode ser resumida assim:

> **Criar famílias de objetos relacionados sem depender diretamente de suas classes concretas.**

---

# 🏭 O Problema

Imagine que estamos desenvolvendo uma aplicação de interface gráfica que precisa funcionar em diferentes sistemas operacionais.

Por exemplo:

```text
Windows
```

e:

```text
Linux
```

Cada sistema operacional possui sua própria aparência e implementação dos componentes gráficos.

Nossa aplicação precisa trabalhar com componentes como:

```text
Botão
```

```text
Checkbox
```

e:

```text
Janela
```

Podemos imaginar as seguintes famílias:

```text
Família Windows

Botão Windows
Checkbox Windows
Janela Windows
```

e:

```text
Família Linux

Botão Linux
Checkbox Linux
Janela Linux
```

Visualmente:

```text
                 Componentes da UI

                       │
             ┌─────────┴─────────┐
             │                   │
             v                   v
         Windows               Linux
             │                   │
       ┌─────┼─────┐       ┌─────┼─────┐
       │     │     │       │     │     │
       v     v     v       v     v     v

     Botão  Check  Janela  Botão  Check  Janela
```

A aplicação precisa escolher uma família.

Se estiver executando no Windows:

```text
Botão Windows
Checkbox Windows
Janela Windows
```

Se estiver executando no Linux:

```text
Botão Linux
Checkbox Linux
Janela Linux
```

O problema começa quando pensamos em **como esses objetos serão criados**.

---

# ❓ Como criar os objetos?

Uma primeira tentativa seria simplesmente instanciar as classes concretas.

Por exemplo:

```text
BotaoWindows()
```

```text
CheckboxWindows()
```

```text
JanelaWindows()
```

Enquanto no Linux:

```text
BotaoLinux()
```

```text
CheckboxLinux()
```

```text
JanelaLinux()
```

Isso parece funcionar.

Porém, precisamos perguntar:

> **Quem decide qual classe concreta deve ser criada?**

Se o próprio código cliente tomar essa decisão, ele precisará conhecer todas as implementações.

Conceitualmente:

```text
Cliente

   │
   ├── Sistema Windows?
   │       │
   │       ├── BotaoWindows
   │       ├── CheckboxWindows
   │       └── JanelaWindows
   │
   └── Sistema Linux?
           │
           ├── BotaoLinux
           ├── CheckboxLinux
           └── JanelaLinux
```

O cliente passa a conhecer diretamente:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
BotaoLinux
CheckboxLinux
JanelaLinux
```

Isso cria um forte acoplamento.

---

# 💥 O problema do código cliente

Imagine que o código principal precise verificar qual sistema operacional está sendo utilizado.

Poderíamos acabar com algo conceitualmente parecido com:

```text
Se sistema == Windows:

    criar BotaoWindows
    criar CheckboxWindows
    criar JanelaWindows

Senão se sistema == Linux:

    criar BotaoLinux
    criar CheckboxLinux
    criar JanelaLinux
```

Inicialmente, isso pode parecer aceitável.

Mas imagine que a aplicação cresça.

Agora temos:

```text
Botão
Checkbox
Janela
Menu
Campo de texto
Barra de progresso
```

E precisamos suportar:

```text
Windows
Linux
macOS
```

O código começa a crescer:

```text
Se Windows:

    criar BotaoWindows
    criar CheckboxWindows
    criar JanelaWindows
    criar MenuWindows
    criar CampoTextoWindows
    criar BarraWindows

Se Linux:

    criar BotaoLinux
    criar CheckboxLinux
    criar JanelaLinux
    criar MenuLinux
    criar CampoTextoLinux
    criar BarraLinux

Se macOS:

    criar BotaoMacOS
    criar CheckboxMacOS
    criar JanelaMacOS
    criar MenuMacOS
    criar CampoTextoMacOS
    criar BarraMacOS
```

A lógica de criação começa a ficar espalhada pelo sistema.

---

# 🚨 O problema do acoplamento

O cliente passa a depender diretamente das classes concretas.

Por exemplo:

```text
Cliente
   │
   ├── BotaoWindows
   ├── CheckboxWindows
   ├── JanelaWindows
   │
   ├── BotaoLinux
   ├── CheckboxLinux
   ├── JanelaLinux
   │
   └── ...
```

Isso significa que o cliente precisa conhecer detalhes de implementação.

A consequência é:

```text
Classes concretas
        ↓
Código cliente
        ↓
Alto acoplamento
```

Idealmente, gostaríamos de algo diferente.

O cliente deveria dizer:

```text
Preciso de um botão.
```

E não:

```text
Preciso de um BotaoWindows.
```

Da mesma forma:

```text
Preciso de um checkbox.
```

E não:

```text
Preciso de um CheckboxLinux.
```

A decisão sobre qual classe concreta utilizar deveria ficar em outro lugar.

---

# 🧠 Uma abstração para os produtos

Podemos começar criando abstrações para os componentes.

Por exemplo:

```text
Botao
```

representaria qualquer tipo de botão.

Então poderíamos ter:

```text
Botao
   │
   ├── BotaoWindows
   │
   └── BotaoLinux
```

Da mesma forma:

```text
Checkbox
   │
   ├── CheckboxWindows
   │
   └── CheckboxLinux
```

E:

```text
Janela
   │
   ├── JanelaWindows
   │
   └── JanelaLinux
```

Agora temos abstrações para os produtos.

Porém, ainda precisamos resolver um problema:

> **Como criar a família correta de produtos?**

---

# 👨‍👩‍👧‍👦 O conceito de família de produtos

Esse é um dos conceitos mais importantes do Abstract Factory.

Uma **família de produtos** é um conjunto de objetos relacionados que devem trabalhar juntos.

No nosso exemplo:

```text
Família Windows
```

é composta por:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Enquanto:

```text
Família Linux
```

é composta por:

```text
BotaoLinux
CheckboxLinux
JanelaLinux
```

Visualmente:

```text
                 FAMÍLIAS

        ┌─────────────────────────┐
        │                         │
        v                         v

    Windows                     Linux
       │                           │
   ┌───┼───┐                   ┌───┼───┐
   │   │   │                   │   │   │
   v   v   v                   v   v   v

 Botão Check Janela          Botão Check Janela
```

A ideia é:

> **Produtos da mesma família devem ser compatíveis entre si.**

Portanto:

```text
BotaoWindows
+
CheckboxWindows
+
JanelaWindows
```

é uma combinação válida.

Da mesma maneira:

```text
BotaoLinux
+
CheckboxLinux
+
JanelaLinux
```

é uma combinação válida.

Mas:

```text
BotaoWindows
+
CheckboxLinux
+
JanelaWindows
```

pode representar uma combinação inconsistente.

---

# ❌ O problema das combinações incompatíveis

Imagine que cada produto seja criado independentemente.

O cliente poderia fazer:

```text
botao = BotaoWindows()
checkbox = CheckboxLinux()
janela = JanelaWindows()
```

Tecnicamente, nada impede isso.

Porém, conceitualmente, temos:

```text
Família Windows

Botão Windows
Janela Windows

Família Linux

Checkbox Linux
```

A aplicação está utilizando componentes de famílias diferentes.

Isso pode gerar:

```text
Inconsistência visual
```

```text
Comportamento inesperado
```

ou:

```text
Componentes incompatíveis
```

Portanto, além de esconder a criação das classes concretas, queremos que o mecanismo de criação também ajude a manter a consistência da família.

---

# 💡 A ideia do Abstract Factory

A solução é criar uma abstração responsável por criar uma **família inteira de produtos relacionados**.

Essa abstração é chamada de:

> **Abstract Factory**

Podemos imaginar:

```text
FabricaAbstrata
```

Ela define operações como:

```text
criar_botao()
```

```text
criar_checkbox()
```

```text
criar_janela()
```

Porém, ela não determina diretamente qual implementação concreta será criada.

Ela define apenas o contrato.

Visualmente:

```text
                 AbstractFactory

                       │
       ┌───────────────┴───────────────┐
       │                               │
       v                               v

FabricaWindows                   FabricaLinux

       │                               │
       ├── criar_botao()              ├── criar_botao()
       │                               │
       ├── criar_checkbox()           ├── criar_checkbox()
       │                               │
       └── criar_janela()             └── criar_janela()
```

A fábrica concreta decide quais classes serão instanciadas.

---

# 🏭 Abstract Factory e Factory

É importante não confundir:

```text
Factory Method
```

com:

```text
Abstract Factory
```

O **Factory Method** normalmente está relacionado à criação de **um produto**, através de um método de fábrica que pode ser sobrescrito pelas subclasses.

Já o **Abstract Factory** trabalha com:

> **famílias de produtos relacionados.**

Por exemplo:

```text
Abstract Factory

├── criar_botao()
├── criar_checkbox()
└── criar_janela()
```

Uma fábrica concreta pode implementar todos esses métodos.

```text
FabricaWindows

├── criar_botao()     → BotaoWindows
├── criar_checkbox()  → CheckboxWindows
└── criar_janela()    → JanelaWindows
```

Outra:

```text
FabricaLinux

├── criar_botao()     → BotaoLinux
├── criar_checkbox()  → CheckboxLinux
└── criar_janela()    → JanelaLinux
```

Portanto:

> **Abstract Factory é especialmente útil quando precisamos criar vários produtos relacionados que devem pertencer à mesma família.**

---

# 🧩 Produtos abstratos

Antes de entender as fábricas, precisamos entender os produtos.

Podemos definir:

```text
Botao
```

como uma abstração.

Ela poderia possuir uma operação:

```text
renderizar()
```

Então:

```text
Botao
   │
   ├── BotaoWindows
   │
   └── BotaoLinux
```

Cada implementação sabe como renderizar seu próprio botão.

Por exemplo:

```text
BotaoWindows

↓

Renderiza botão no estilo Windows
```

Enquanto:

```text
BotaoLinux

↓

Renderiza botão no estilo Linux
```

A mesma ideia pode ser aplicada aos demais produtos.

---

# 🧱 Estrutura dos produtos

Podemos representar:

```text
                         Produtos

              ┌────────────┼────────────┐
              │            │            │
              v            v            v

            Botao       Checkbox      Janela
              │            │            │
          ┌───┴───┐    ┌───┴───┐    ┌───┴───┐
          │       │    │       │    │       │
          v       v    v       v    v       v

       Windows  Linux Windows Linux Windows Linux
```

Agora temos:

```text
Produtos abstratos
```

e:

```text
Produtos concretos
```

A fábrica será responsável por conectar essas duas partes.

---

# 🏭 Fábrica abstrata

A fábrica abstrata define como uma família de produtos pode ser criada.

Por exemplo:

```text
FabricaGUI

    criar_botao()

    criar_checkbox()

    criar_janela()
```

Observe que ela não precisa dizer:

```text
criar BotaoWindows
```

ou:

```text
criar BotaoLinux
```

Ela simplesmente define:

```text
criar_botao()
```

Isso é importante porque o cliente passa a depender da abstração.

---

# 🏭 Fábrica concreta

Agora podemos criar uma fábrica específica para cada família.

Por exemplo:

```text
FabricaWindows
```

Ela implementa:

```text
criar_botao()
```

retornando:

```text
BotaoWindows
```

Também:

```text
criar_checkbox()
```

retornando:

```text
CheckboxWindows
```

E:

```text
criar_janela()
```

retornando:

```text
JanelaWindows
```

Visualmente:

```text
FabricaWindows

    │
    ├── criar_botao()
    │       ↓
    │   BotaoWindows
    │
    ├── criar_checkbox()
    │       ↓
    │   CheckboxWindows
    │
    └── criar_janela()
            ↓
        JanelaWindows
```

Observe que a fábrica cria uma família consistente.

---

# 🐧 Outra fábrica concreta

Podemos fazer o mesmo para Linux.

```text
FabricaLinux
```

Ela implementa:

```text
criar_botao()
```

retornando:

```text
BotaoLinux
```

Depois:

```text
criar_checkbox()
```

retornando:

```text
CheckboxLinux
```

E:

```text
criar_janela()
```

retornando:

```text
JanelaLinux
```

Visualmente:

```text
FabricaLinux

    │
    ├── criar_botao()
    │       ↓
    │   BotaoLinux
    │
    ├── criar_checkbox()
    │       ↓
    │   CheckboxLinux
    │
    └── criar_janela()
            ↓
        JanelaLinux
```

Assim, cada fábrica conhece somente sua própria família.

---

# 👤 O papel do Client

O cliente é o código que utiliza os produtos.

Uma característica fundamental é que o cliente deve depender das abstrações.

Por exemplo:

```text
Cliente
   │
   v
FabricaGUI
```

O cliente não precisa saber:

```text
BotaoWindows
```

nem:

```text
BotaoLinux
```

Ele simplesmente faz:

```text
fabrica.criar_botao()
```

Da mesma maneira:

```text
fabrica.criar_checkbox()
```

e:

```text
fabrica.criar_janela()
```

A fábrica concreta escolhida determina quais produtos serão criados.

---

# 🔄 O fluxo completo

Imagine que a aplicação detectou:

```text
Sistema operacional = Windows
```

Então escolhemos:

```text
FabricaWindows
```

O cliente faz:

```text
fabrica.criar_botao()
```

A fábrica retorna:

```text
BotaoWindows
```

Depois:

```text
fabrica.criar_checkbox()
```

retorna:

```text
CheckboxWindows
```

E:

```text
fabrica.criar_janela()
```

retorna:

```text
JanelaWindows
```

O fluxo completo fica:

```text
Cliente

   │
   │ escolhe
   v

FabricaWindows

   │
   ├── criar_botao()
   │       ↓
   │   BotaoWindows
   │
   ├── criar_checkbox()
   │       ↓
   │   CheckboxWindows
   │
   └── criar_janela()
           ↓
       JanelaWindows
```

Se a aplicação estiver no Linux:

```text
Cliente

   │
   │ escolhe
   v

FabricaLinux

   │
   ├── criar_botao()
   │       ↓
   │   BotaoLinux
   │
   ├── criar_checkbox()
   │       ↓
   │   CheckboxLinux
   │
   └── criar_janela()
           ↓
       JanelaLinux
```

O cliente continua praticamente igual.

Apenas a fábrica muda.

---

# 🔀 Trocando a família inteira

Essa é uma das grandes vantagens do padrão.

Imagine que o cliente receba:

```text
FabricaWindows
```

Ele cria:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Agora trocamos:

```text
FabricaWindows
```

por:

```text
FabricaLinux
```

O cliente passa a receber:

```text
BotaoLinux
CheckboxLinux
JanelaLinux
```

Não precisamos alterar o código responsável por utilizar os produtos.

Visualmente:

```text
                Cliente
                   │
                   v
             AbstractFactory
                   │
          ┌────────┴────────┐
          │                 │
          v                 v

   FabricaWindows      FabricaLinux
          │                 │
          v                 v

 Família Windows      Família Linux
```

Portanto:

> **Trocar a fábrica significa trocar a família de produtos criada.**

---

# 🧠 A fábrica não é o produto

É importante separar esses conceitos.

A:

```text
Fábrica
```

é responsável por:

```text
CRIAR
```

Enquanto os:

```text
Produtos
```

são responsáveis por:

```text
FAZER
```

seu trabalho.

Por exemplo:

```text
FabricaWindows
```

cria:

```text
BotaoWindows
```

Mas quem sabe como funcionar é:

```text
BotaoWindows
```

Podemos visualizar:

```text
Fábrica

↓

Cria produtos

↓

Produtos

↓

Executam comportamentos
```

Essa separação é fundamental.

---

# 🏗️ Estrutura conceitual do Abstract Factory

A estrutura clássica pode ser representada assim:

```text
                         Client
                           │
                           v
                   AbstractFactory
                           │
             ┌─────────────┴─────────────┐
             │                           │
             v                           v

     ConcreteFactoryA            ConcreteFactoryB
             │                           │
       ┌─────┼─────┐               ┌─────┼─────┐
       │     │     │               │     │     │
       v     v     v               v     v     v

   ProductA1 ProductB1 ProductC1  ProductA2 ProductB2 ProductC2
```

A fábrica abstrata define:

```text
criar Produto A
criar Produto B
criar Produto C
```

As fábricas concretas determinam:

```text
Qual implementação concreta será criada.
```

---

# 🧩 Participantes do Abstract Factory

O Abstract Factory possui alguns participantes principais.

---

## 🏭 Abstract Factory

A **Abstract Factory** define a interface para criação dos produtos.

No nosso exemplo:

```text
FabricaGUI
```

Ela pode definir:

```text
criar_botao()

criar_checkbox()

criar_janela()
```

Ela não precisa conhecer as classes concretas.

Sua responsabilidade é estabelecer o contrato para criação da família.

---

## 🏭 Concrete Factory

A **Concrete Factory** implementa a fábrica abstrata.

Exemplos:

```text
FabricaWindows
```

e:

```text
FabricaLinux
```

Cada uma cria os produtos correspondentes à sua família.

Por exemplo:

```text
FabricaWindows

criar_botao()
    ↓
BotaoWindows
```

Enquanto:

```text
FabricaLinux

criar_botao()
    ↓
BotaoLinux
```

---

## 🔷 Abstract Product

O **Abstract Product** representa a abstração de um tipo de produto.

Por exemplo:

```text
Botao
```

Ele define o contrato que os diferentes tipos de botão devem seguir.

Da mesma forma:

```text
Checkbox
```

e:

```text
Janela
```

são outros produtos abstratos.

---

## 🧱 Concrete Product

O **Concrete Product** representa uma implementação específica de um produto.

Exemplos:

```text
BotaoWindows
```

```text
BotaoLinux
```

```text
CheckboxWindows
```

```text
CheckboxLinux
```

```text
JanelaWindows
```

```text
JanelaLinux
```

Esses objetos implementam os produtos abstratos.

---

## 👤 Client

O **Client** utiliza as fábricas e os produtos.

O cliente deve depender das abstrações.

Por exemplo:

```text
Cliente
   │
   v
FabricaGUI
   │
   ├── Botao
   ├── Checkbox
   └── Janela
```

Ele não deveria precisar conhecer diretamente:

```text
BotaoWindows
BotaoLinux
CheckboxWindows
CheckboxLinux
...
```

---

# 📊 Participantes no nosso exemplo

| Participante         | Exemplo           | Responsabilidade                                  |
| -------------------- | ----------------- | ------------------------------------------------- |
| **Abstract Factory** | `FabricaGUI`      | Define operações para criar a família de produtos |
| **Concrete Factory** | `FabricaWindows`  | Cria produtos da família Windows                  |
| **Concrete Factory** | `FabricaLinux`    | Cria produtos da família Linux                    |
| **Abstract Product** | `Botao`           | Define a abstração do botão                       |
| **Abstract Product** | `Checkbox`        | Define a abstração do checkbox                    |
| **Abstract Product** | `Janela`          | Define a abstração da janela                      |
| **Concrete Product** | `BotaoWindows`    | Implementação Windows do botão                    |
| **Concrete Product** | `BotaoLinux`      | Implementação Linux do botão                      |
| **Concrete Product** | `CheckboxWindows` | Implementação Windows do checkbox                 |
| **Concrete Product** | `CheckboxLinux`   | Implementação Linux do checkbox                   |
| **Concrete Product** | `JanelaWindows`   | Implementação Windows da janela                   |
| **Concrete Product** | `JanelaLinux`     | Implementação Linux da janela                     |
| **Client**           | Aplicação         | Utiliza a fábrica e os produtos                   |

---

# 🔗 A relação entre fábrica e família

Podemos resumir a arquitetura assim:

```text
                    Abstract Factory

                          │
            ┌─────────────┴─────────────┐
            │                           │
            v                           v

     FabricaWindows                FabricaLinux
            │                           │
            │                           │
       cria família                 cria família
            │                           │
            v                           v

     ┌──────┼──────┐              ┌──────┼──────┐
     │      │      │              │      │      │
     v      v      v              v      v      v

   Botão  Check  Janela         Botão  Check  Janela
    Win    Win     Win           Linux Linux   Linux
```

A fábrica concreta funciona como uma espécie de:

> **ponto central de criação de uma família.**

---

# 🧠 Por que isso reduz o acoplamento?

Sem Abstract Factory:

```text
Cliente
   │
   ├── BotaoWindows
   ├── CheckboxWindows
   ├── JanelaWindows
   ├── BotaoLinux
   ├── CheckboxLinux
   └── JanelaLinux
```

O cliente conhece as implementações.

Com Abstract Factory:

```text
Cliente
   │
   v
AbstractFactory
   │
   ├── criar_botao()
   ├── criar_checkbox()
   └── criar_janela()
```

Agora:

```text
Cliente
```

conhece:

```text
Abstrações
```

e não:

```text
Classes concretas
```

A responsabilidade pela escolha das classes concretas fica nas fábricas.

---

# 🔄 Dependência invertida na criação

Podemos visualizar a diferença.

Sem uma fábrica:

```text
Cliente
   │
   ├──────────────┐
   v              v

BotaoWindows   BotaoLinux
```

O cliente conhece diretamente as implementações.

Com Abstract Factory:

```text
Cliente
   │
   v
AbstractFactory
   │
   v
ConcreteFactory
   │
   v
ConcreteProduct
```

O cliente passa a depender de abstrações.

Isso permite trocar as implementações com maior facilidade.

---

# 🖥️ Exemplo completo da aplicação

Imagine que nossa aplicação tenha uma função:

```text
criar_interface()
```

Ela recebe uma fábrica:

```text
FabricaGUI
```

Então solicita:

```text
botao = fabrica.criar_botao()

checkbox = fabrica.criar_checkbox()

janela = fabrica.criar_janela()
```

O cliente não precisa saber o que está acontecendo internamente.

Se receber:

```text
FabricaWindows
```

teremos:

```text
botao
    ↓
BotaoWindows

checkbox
    ↓
CheckboxWindows

janela
    ↓
JanelaWindows
```

Se receber:

```text
FabricaLinux
```

teremos:

```text
botao
    ↓
BotaoLinux

checkbox
    ↓
CheckboxLinux

janela
    ↓
JanelaLinux
```

O código cliente permanece trabalhando com:

```text
Botao
Checkbox
Janela
```

e:

```text
FabricaGUI
```

---

# 🎨 Outro exemplo: temas visuais

O mesmo padrão pode ser aplicado a temas.

Imagine:

```text
Tema Claro
```

e:

```text
Tema Escuro
```

Cada tema possui:

```text
Botão
Checkbox
Janela
```

Então:

```text
FabricaTemaClaro
```

cria:

```text
BotaoClaro
CheckboxClaro
JanelaClara
```

Enquanto:

```text
FabricaTemaEscuro
```

cria:

```text
BotaoEscuro
CheckboxEscuro
JanelaEscura
```

Podemos representar:

```text
                    Tema

             ┌───────┴───────┐
             │               │
             v               v

           Claro           Escuro
             │               │
       ┌─────┼─────┐   ┌─────┼─────┐
       │     │     │   │     │     │
       v     v     v   v     v     v

     Botão Check Janela Botão Check Janela
```

O cliente escolhe:

```text
FabricaTemaClaro
```

ou:

```text
FabricaTemaEscuro
```

e recebe toda a família correspondente.

---

# 🛒 Exemplo: sistema de pagamentos

Outro exemplo seria um sistema que trabalha com diferentes provedores de pagamento.

Podemos ter:

```text
Família Stripe
```

e:

```text
Família PayPal
```

Cada família poderia possuir:

```text
Processador de pagamento
Validador
Notificador
```

Então:

```text
FabricaStripe

├── criar_processador()
├── criar_validador()
└── criar_notificador()
```

Enquanto:

```text
FabricaPayPal

├── criar_processador()
├── criar_validador()
└── criar_notificador()
```

O cliente não precisa conhecer as implementações específicas.

Ele trabalha com:

```text
Processador
Validador
Notificador
```

A fábrica garante que os componentes escolhidos pertençam à mesma família.

---

# 🏦 Exemplo: sistema bancário

Também poderíamos ter diferentes famílias de componentes para bancos.

Por exemplo:

```text
Banco A
```

e:

```text
Banco B
```

Cada família poderia fornecer:

```text
Conta
Cartão
Empréstimo
```

Então:

```text
FabricaBancoA

├── criar_conta()
├── criar_cartao()
└── criar_emprestimo()
```

e:

```text
FabricaBancoB

├── criar_conta()
├── criar_cartao()
└── criar_emprestimo()
```

O cliente trabalha apenas com as abstrações.

---

# 📁 Exemplo-problema deste projeto

Neste projeto, o Abstract Factory será estudado através de uma aplicação de **interface gráfica multiplataforma**.

A aplicação deverá funcionar em diferentes sistemas operacionais.

Inicialmente teremos:

```text
Windows
```

e:

```text
Linux
```

Cada sistema operacional possui sua própria família de componentes gráficos.

A aplicação precisará trabalhar com:

```text
Botão
```

```text
Checkbox
```

e:

```text
Janela
```

Portanto, teremos duas famílias.

---

# 🪟 Família Windows

A família Windows será composta por:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Visualmente:

```text
FabricaWindows

       │
       ├── criar_botao()
       │       ↓
       │   BotaoWindows
       │
       ├── criar_checkbox()
       │       ↓
       │   CheckboxWindows
       │
       └── criar_janela()
               ↓
           JanelaWindows
```

Todos esses objetos pertencem à:

```text
Família Windows
```

---

# 🐧 Família Linux

A família Linux será composta por:

```text
BotaoLinux
CheckboxLinux
JanelaLinux
```

Visualmente:

```text
FabricaLinux

       │
       ├── criar_botao()
       │       ↓
       │   BotaoLinux
       │
       ├── criar_checkbox()
       │       ↓
       │   CheckboxLinux
       │
       └── criar_janela()
               ↓
           JanelaLinux
```

Todos esses objetos pertencem à:

```text
Família Linux
```

---

# 🎯 Requisitos do projeto

A aplicação deverá permitir que o cliente:

```text
Crie um botão
```

```text
Crie um checkbox
```

```text
Crie uma janela
```

Porém, o cliente não deverá precisar escrever:

```text
BotaoWindows()
```

ou:

```text
BotaoLinux()
```

Ele deverá trabalhar com a fábrica:

```text
FabricaGUI
```

Por exemplo:

```text
fabrica.criar_botao()
```

```text
fabrica.criar_checkbox()
```

```text
fabrica.criar_janela()
```

A fábrica concreta será responsável por decidir quais classes serão instanciadas.

---

# 🔄 Cenário 1 — Windows

Imagine que a aplicação esteja sendo executada no Windows.

O cliente seleciona:

```text
FabricaWindows
```

Depois:

```text
fabrica.criar_botao()
```

resulta em:

```text
BotaoWindows
```

Depois:

```text
fabrica.criar_checkbox()
```

resulta em:

```text
CheckboxWindows
```

E:

```text
fabrica.criar_janela()
```

resulta em:

```text
JanelaWindows
```

Resultado:

```text
Família Windows

BotaoWindows
CheckboxWindows
JanelaWindows
```

---

# 🔄 Cenário 2 — Linux

Agora imagine que a aplicação esteja sendo executada no Linux.

O cliente seleciona:

```text
FabricaLinux
```

Depois:

```text
fabrica.criar_botao()
```

resulta em:

```text
BotaoLinux
```

Depois:

```text
fabrica.criar_checkbox()
```

resulta em:

```text
CheckboxLinux
```

E:

```text
fabrica.criar_janela()
```

resulta em:

```text
JanelaLinux
```

Resultado:

```text
Família Linux

BotaoLinux
CheckboxLinux
JanelaLinux
```

---

# 🚫 O que o cliente não deve fazer

O cliente não deverá possuir lógica como:

```text
Se Windows:

    BotaoWindows()

Se Linux:

    BotaoLinux()
```

Nem:

```text
Se Windows:

    CheckboxWindows()

Se Linux:

    CheckboxLinux()
```

A lógica de criação deve ficar concentrada nas fábricas.

O cliente deve trabalhar com:

```text
FabricaGUI
```

e:

```text
Botao
Checkbox
Janela
```

---

# 🏗️ Arquitetura do exemplo-problema

A estrutura geral poderá ser representada assim:

```text
                         CLIENTE
                            │
                            v
                    FabricaGUI
                            │
               ┌────────────┴────────────┐
               │                         │
               v                         v

        FabricaWindows              FabricaLinux
               │                         │
        ┌──────┼──────┐           ┌──────┼──────┐
        │      │      │           │      │      │
        v      v      v           v      v      v

      Botão  Check  Janela       Botão  Check  Janela
       Win    Win     Win         Linux  Linux   Linux
```

O cliente poderá trocar:

```text
FabricaWindows
```

por:

```text
FabricaLinux
```

sem precisar modificar a lógica de utilização dos produtos.

---

# 🔍 O que queremos demonstrar

O principal objetivo do exemplo não é criar uma interface gráfica real.

O objetivo é demonstrar os conceitos do padrão.

Queremos observar que:

```text
Cliente
```

não precisa conhecer:

```text
Classes concretas
```

Ele conhece apenas:

```text
Fábrica abstrata
```

e:

```text
Produtos abstratos
```

A fábrica concreta cuida da criação.

---

# 🧠 A grande ideia: trocar uma família inteira

Imagine que temos:

```text
FabricaWindows
```

Ela produz:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Se trocarmos para:

```text
FabricaLinux
```

passamos a produzir:

```text
BotaoLinux
CheckboxLinux
JanelaLinux
```

O cliente continua fazendo:

```text
criar_botao()
criar_checkbox()
criar_janela()
```

A diferença está na implementação da fábrica.

Portanto:

> **O Abstract Factory permite trocar uma família inteira de objetos relacionados sem modificar o código cliente que utiliza esses objetos.**

---

# 🆚 Sem Abstract Factory

Sem o padrão, poderíamos ter:

```text
Cliente

   │
   ├── if Windows
   │      │
   │      ├── BotaoWindows
   │      ├── CheckboxWindows
   │      └── JanelaWindows
   │
   └── if Linux
          │
          ├── BotaoLinux
          ├── CheckboxLinux
          └── JanelaLinux
```

O cliente conhece as classes concretas.

Além disso, a lógica de criação fica espalhada.

---

# 🆚 Com Abstract Factory

Com o padrão:

```text
Cliente

   │
   v

AbstractFactory

   │
   ├───────────────┐
   │               │
   v               v

FabricaWindows   FabricaLinux
   │               │
   v               v

Família Windows  Família Linux
```

O cliente trabalha com uma abstração.

A fábrica concreta controla a criação.

---

# 🧠 Abstract Factory e polimorfismo

O Abstract Factory utiliza fortemente:

> **Polimorfismo**

Por exemplo:

```text
FabricaGUI
```

pode referenciar:

```text
FabricaWindows
```

ou:

```text
FabricaLinux
```

O cliente não precisa saber qual implementação concreta está utilizando.

Da mesma forma:

```text
Botao
```

pode representar:

```text
BotaoWindows
```

ou:

```text
BotaoLinux
```

O cliente trabalha com:

```text
Botao
```

enquanto o objeto concreto determina seu comportamento.

---

# 🧠 Abstract Factory e encapsulamento da criação

Outro benefício importante é que o padrão encapsula o conhecimento sobre:

```text
Quais classes devem ser instanciadas
```

Esse conhecimento fica dentro das fábricas concretas.

Por exemplo:

```text
FabricaWindows
```

sabe que:

```text
criar_botao()
```

deve retornar:

```text
BotaoWindows
```

O cliente não precisa saber disso.

Portanto:

```text
Cliente

↓

Pede produto

↓

Fábrica

↓

Decide implementação

↓

Cria produto
```

---

# 🧠 Abstract Factory e princípio Aberto/Fechado

Imagine que futuramente precisamos adicionar:

```text
macOS
```

Podemos criar:

```text
FabricaMacOS
```

e os produtos:

```text
BotaoMacOS
CheckboxMacOS
JanelaMacOS
```

A arquitetura passa a ser:

```text
AbstractFactory

       │
 ┌─────┼──────────┐
 │     │          │
 v     v          v

Windows Linux    macOS
```

O cliente pode continuar utilizando:

```text
FabricaGUI
```

e:

```text
Botao
Checkbox
Janela
```

Isso favorece o princípio:

> **Aberto para extensão e fechado para modificação.**

Ou seja:

```text
Nova família

↓

Nova fábrica concreta

+

Novos produtos concretos
```

sem necessariamente modificar a lógica principal do cliente.

---

# ⚠️ Um ponto importante: adicionar um novo produto

Embora adicionar uma **nova família** seja relativamente simples, existe um detalhe importante.

Imagine que atualmente temos:

```text
Botão
Checkbox
Janela
```

Agora surge a necessidade de adicionar:

```text
Menu
```

A fábrica abstrata precisará ganhar uma nova operação:

```text
criar_menu()
```

Consequentemente, todas as fábricas concretas provavelmente precisarão implementar esse novo método.

Por exemplo:

```text
FabricaWindows

criar_botao()
criar_checkbox()
criar_janela()
criar_menu()
```

E:

```text
FabricaLinux

criar_botao()
criar_checkbox()
criar_janela()
criar_menu()
```

Portanto:

> **Abstract Factory facilita a adição de novas famílias, mas pode tornar mais difícil adicionar novos tipos de produtos.**

Esse é um trade-off importante do padrão.

---

# 🟢 Prós

## Famílias consistentes

A fábrica concreta cria produtos pertencentes à mesma família.

Por exemplo:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Isso reduz o risco de combinações incompatíveis.

---

## Redução do acoplamento

O cliente não precisa depender diretamente das classes concretas.

Em vez de:

```text
BotaoWindows()
```

ele utiliza:

```text
fabrica.criar_botao()
```

---

## Isolamento das classes concretas

O código cliente não precisa conhecer detalhes de implementação dos produtos.

---

## Facilidade para trocar famílias

Podemos trocar:

```text
FabricaWindows
```

por:

```text
FabricaLinux
```

e toda a família de produtos muda.

---

## Centralização da criação

A lógica de criação fica concentrada nas fábricas concretas.

---

## Compatibilidade entre produtos

A fábrica pode garantir que os produtos criados pertençam à mesma família.

---

## Extensibilidade para novas famílias

Adicionar:

```text
macOS
```

por exemplo, pode ser feito através de:

```text
FabricaMacOS
```

e seus produtos correspondentes.

---

# 🔴 Contras

## Aumenta a quantidade de classes

Um Abstract Factory pode exigir várias abstrações e implementações.

Por exemplo:

```text
FabricaGUI
FabricaWindows
FabricaLinux

Botao
BotaoWindows
BotaoLinux

Checkbox
CheckboxWindows
CheckboxLinux

Janela
JanelaWindows
JanelaLinux
```

Para um projeto pequeno, isso pode ser bastante código.

---

## Pode aumentar a complexidade

Em vez de simplesmente fazer:

```text
Botao()
```

passamos a ter:

```text
fabrica.criar_botao()
```

e precisamos estruturar:

```text
Fábrica abstrata
```

```text
Fábricas concretas
```

```text
Produtos abstratos
```

```text
Produtos concretos
```

---

## Adicionar novos produtos pode ser trabalhoso

Se adicionarmos:

```text
Menu
```

todas as fábricas podem precisar ser modificadas.

---

## Pode ser exagero para problemas simples

Se temos apenas um produto e poucas variações, talvez outro padrão seja mais apropriado.

O Abstract Factory é especialmente útil quando existem:

```text
Vários produtos

+

Várias famílias

+

Relacionamentos entre os produtos
```

---

# 🎯 Quando utilizar Abstract Factory?

O Abstract Factory é especialmente útil quando:

- precisamos criar famílias de objetos relacionados;

- os objetos de uma família devem ser compatíveis entre si;

- queremos esconder as classes concretas do cliente;

- queremos trocar famílias inteiras de produtos;

- existem diferentes plataformas, temas ou configurações;

- queremos centralizar a lógica de criação;

- queremos reduzir o acoplamento entre cliente e classes concretas;

- queremos garantir que produtos relacionados sejam criados de maneira consistente.

---

# 🌍 Exemplos comuns de Abstract Factory

O padrão pode aparecer em diversos contextos.

---

## 🖥️ Interfaces gráficas

```text
FabricaWindows
FabricaLinux
FabricaMacOS
```

Cada fábrica pode criar:

```text
Botão
Checkbox
Janela
Menu
```

---

## 🎨 Temas visuais

```text
FabricaTemaClaro
FabricaTemaEscuro
```

Cada uma cria:

```text
Botão
Janela
Menu
Campo
```

com o estilo correspondente.

---

## 🗄️ Bancos de dados

Podemos ter famílias de componentes para:

```text
PostgreSQL
MySQL
SQLite
```

Cada fábrica poderia produzir objetos relacionados como:

```text
Conexão
Comando
Transação
```

---

## ☁️ Serviços em diferentes provedores

Podemos ter:

```text
AWS
Azure
Google Cloud
```

Cada fábrica pode criar componentes relacionados aos serviços daquele provedor.

---

## 💳 Sistemas de pagamento

Podemos ter:

```text
Stripe
PayPal
Mercado Pago
```

Cada família poderia possuir:

```text
Processador
Validador
Notificador
```

---

# 🔄 Abstract Factory e Factory Method

Os dois padrões são frequentemente relacionados.

Uma forma simples de pensar é:

```text
Factory Method

↓

Criação de um produto
```

Enquanto:

```text
Abstract Factory

↓

Criação de uma família de produtos
```

Por exemplo:

```text
Factory Method

criar_botao()
```

Enquanto:

```text
Abstract Factory

criar_botao()
criar_checkbox()
criar_janela()
```

Uma Abstract Factory pode inclusive utilizar Factory Methods internamente para criar seus produtos.

---

# 🧠 Como memorizar o Abstract Factory

Uma maneira simples de lembrar é pensar em:

> **"Quero criar uma família inteira de objetos relacionados."**

Por exemplo:

```text
Windows

├── Botão Windows
├── Checkbox Windows
└── Janela Windows
```

ou:

```text
Linux

├── Botão Linux
├── Checkbox Linux
└── Janela Linux
```

Então:

```text
Abstract Factory

↓

Escolhe a família

↓

Cria os produtos daquela família
```

---

# 📌 A diferença fundamental

Podemos resumir a diferença entre uma fábrica comum e uma Abstract Factory desta maneira:

```text
Factory

↓

"Qual objeto devo criar?"
```

Enquanto:

```text
Abstract Factory

↓

"Qual família de objetos devo criar?"
```

Essa diferença é extremamente importante.

---

# 🧩 A estrutura mental do padrão

Sempre que você encontrar um problema com:

```text
Vários produtos
```

e:

```text
Várias famílias desses produtos
```

pense em:

```text
                 Abstract Factory

                       │
                       v

                   Família
                       │
             ┌─────────┼─────────┐
             │         │         │
             v         v         v

           Produto   Produto   Produto
```

Por exemplo:

```text
              Família Windows

                    │
          ┌─────────┼─────────┐
          │         │         │
          v         v         v

        Botão     Checkbox   Janela
```

Ou:

```text
              Família Linux

                    │
          ┌─────────┼─────────┐
          │         │         │
          v         v         v

        Botão     Checkbox   Janela
```

---

# 📝 Resumo Final

O **Abstract Factory** é um Design Pattern **criacional** utilizado para criar **famílias de objetos relacionados ou dependentes** sem que o cliente precise conhecer suas classes concretas.

A principal ideia é separar:

```text
Utilização dos objetos
```

da:

```text
Criação dos objetos
```

Além disso, o padrão ajuda a garantir que os objetos criados pertençam à mesma família.

No exemplo deste projeto teremos:

```text
Família Windows
```

e:

```text
Família Linux
```

Cada família possuirá:

```text
Botão
Checkbox
Janela
```

Assim:

```text
FabricaWindows
```

cria:

```text
BotaoWindows
CheckboxWindows
JanelaWindows
```

Enquanto:

```text
FabricaLinux
```

cria:

```text
BotaoLinux
CheckboxLinux
JanelaLinux
```

O cliente não precisa saber qual classe concreta está sendo instanciada.

Ele simplesmente trabalha com:

```text
FabricaGUI
```

e solicita:

```text
criar_botao()
```

```text
criar_checkbox()
```

```text
criar_janela()
```

A fábrica concreta determina quais produtos serão criados.

Visualmente:

```text
                         Cliente
                            │
                            v
                    AbstractFactory
                            │
               ┌────────────┴────────────┐
               │                         │
               v                         v

        FabricaWindows              FabricaLinux
               │                         │
        ┌──────┼──────┐           ┌──────┼──────┐
        │      │      │           │      │      │
        v      v      v           v      v      v

      Botão  Check  Janela       Botão  Check  Janela
       Win    Win     Win         Linux  Linux   Linux
```

A principal vantagem é que podemos trocar:

```text
FabricaWindows
```

por:

```text
FabricaLinux
```

e toda a família de produtos muda sem que o cliente precise conhecer as classes concretas.

A ideia mais importante para memorizar é:

> **Abstract Factory = criar famílias de objetos relacionados e compatíveis sem depender diretamente das classes concretas.**

Ou, de maneira ainda mais simples:

```text
Abstract Factory

↓

Escolhe uma família

↓

Cria todos os produtos daquela família
```

No nosso exemplo:

```text
Windows
│
├── Botão Windows
├── Checkbox Windows
└── Janela Windows
```

ou:

```text
Linux
│
├── Botão Linux
├── Checkbox Linux
└── Janela Linux
```

Portanto:

> **A essência do Abstract Factory é fornecer uma interface para criar uma família de objetos relacionados, permitindo trocar toda a família sem alterar o código cliente que utiliza esses objetos.**
