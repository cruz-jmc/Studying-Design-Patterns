# Singleton - Reference: <https://refactoring.guru/pt-br/design-patterns/singleton>

## 📌 Objetivo

O **Singleton** é um Design Pattern **criacional** utilizado para **garantir que uma determinada classe possua apenas uma instância durante a execução da aplicação e fornecer um ponto global de acesso a essa instância**.

De acordo com o **GoF — *Design Patterns: Elements of Reusable Object-Oriented Software***, a intenção do Singleton pode ser resumida como:

> **Garantir que uma classe tenha somente uma instância e fornecer um ponto global de acesso a ela.**

A ideia pode ser representada da seguinte maneira:

```text
              Classe Singleton

                    │
                    │ cria
                    ▼

               ┌─────────┐
               │ Instância│
               │   única  │
               └─────────┘
                    ▲
                    │
          ┌─────────┼─────────┐
          │         │         │
          │         │         │
       Cliente A  Cliente B  Cliente C
```

Todos os clientes acessam:

```
a mesma instância
```

e não criam objetos independentes da classe.

---

# 🧠 A ideia central

Normalmente, quando criamos uma classe em Python, podemos criar quantos objetos quisermos.

Por exemplo:

```
objeto_1 = MinhaClasse()
objeto_2 = MinhaClasse()
objeto_3 = MinhaClasse()
```

Teremos:

```
objeto_1 → instância diferente

objeto_2 → instância diferente

objeto_3 → instância diferente
```

Visualmente:

```
MinhaClasse

   │
   ├──► objeto_1
   │
   ├──► objeto_2
   │
   └──► objeto_3
```

No Singleton, queremos algo diferente.

Mesmo que diferentes partes da aplicação solicitem a classe:

```
objeto_1 = Singleton()
objeto_2 = Singleton()
objeto_3 = Singleton()
```

o resultado conceitual será:

```
objeto_1 ─────┐
              │
objeto_2 ─────┼────► mesma instância
              │
objeto_3 ─────┘
```

Portanto:

```
objeto_1 is objeto_2

objeto_2 is objeto_3

objeto_1 is objeto_3
```

Todos apontam para o mesmo objeto.

---

# 🏭 Categoria do Singleton

O Singleton pertence à categoria dos padrões:

> **Criacionais**

Os Design Patterns criacionais estão relacionados à:

```
criação de objetos
```

Eles procuram fornecer mecanismos para controlar ou abstrair a maneira como os objetos são criados.

No caso do Singleton, o problema é bastante específico:

```
Como impedir que uma classe possua várias instâncias
quando precisamos de apenas uma?
```

Portanto:

```
Singleton

    ↓

Controla a criação

    ↓

Garante uma única instância
```

---

# ⚠️ O Singleton é um padrão controverso

O Singleton é um dos padrões mais conhecidos e também um dos mais controversos.

Isso acontece porque ele resolve um problema real:

```
Precisamos de apenas uma instância
```

mas sua solução normalmente envolve:

```
acesso global
```

E o acesso global pode introduzir diversos problemas de design.

Por isso, é comum encontrar discussões sobre o Singleton como:

```
Design Pattern

        versus

Antipadrão
```

O objetivo deste estudo não é simplesmente dizer que:

```
Singleton é bom
```

ou:

```
Singleton é ruim
```

Mas entender:

```
qual problema ele resolve

↓

como ele funciona

↓

quais são suas consequências

↓

quando seu uso pode fazer sentido

↓

quando outras soluções são preferíveis
```

---

# 🚨 O problema que iremos resolver

Imagine um sistema que precisa trabalhar com um banco de dados PostgreSQL.

A aplicação possui vários componentes:

```
Exportador

Processador

Notificador

Relatório

API

Serviço de busca
```

Todos eles precisam consultar o banco.

Podemos representar:

```
                 Aplicação

        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
    Exportador  Processador  Notificador
        │          │          │
        ▼          ▼          ▼
      Banco      Banco       Banco
```

Uma primeira implementação poderia simplesmente criar uma nova conexão sempre que algum componente precisasse acessar o banco.

Por exemplo:

```
Exportador

↓

ConexaoBD()

↓

abre conexão
```

Depois:

```
Processador

↓

ConexaoBD()

↓

abre outra conexão
```

E:

```
Notificador

↓

ConexaoBD()

↓

abre outra conexão
```

Isso parece simples.

Porém, existe um problema.

---

# 🔌 O custo de abrir uma conexão

Uma conexão com o banco de dados não é necessariamente uma operação barata.

No exemplo utilizado neste estudo, cada conexão realiza operações como:

```
Abrir socket

↓

Autenticar

↓

Negociar protocolo

↓

Estabelecer comunicação

↓

Executar consultas
```

Podemos imaginar:

```
Cliente
   │
   │
   ▼
Abrir socket
   │
   ▼
Autenticar
   │
   ▼
Negociar protocolo
   │
   ▼
Conexão estabelecida
```

No exemplo apresentado em aula, o processo de handshake pode consumir aproximadamente:

```
3 × 1,5 segundos
```

Ou seja:

```
≈ 4,5 segundos
```

para estabelecer a conexão.

Se a aplicação abrir uma nova conexão repetidamente:

```
requisição 1 → nova conexão
requisição 2 → nova conexão
requisição 3 → nova conexão
requisição 4 → nova conexão
...
```

o custo pode se acumular.

---

# 💥 O problema de criar várias conexões

Imagine que três componentes façam:

```
bd1 = ConexaoBD("postgres://acervo")

bd2 = ConexaoBD("postgres://acervo")

bd3 = ConexaoBD("postgres://acervo")
```

Teríamos:

```
bd1
 │
 └──► socket 1

bd2
 │
 └──► socket 2

bd3
 │
 └──► socket 3
```

Mesmo utilizando exatamente o mesmo banco:

```
postgres://acervo
```

criamos:

```
3 objetos

3 conexões

3 sockets
```

Isso pode ser desnecessário quando a conexão representa um recurso compartilhado que deveria ser único dentro daquele contexto.

---

# 🗄️ O limite de conexões do PostgreSQL

Outro problema é que bancos de dados possuem limites de conexões simultâneas.

No exemplo apresentado na aula, considera-se:

```
PostgreSQL

máximo de conexões = 100
```

Imagine uma aplicação que constantemente cria novas conexões:

```
Aplicação

↓

ConexaoBD()

↓

ConexaoBD()

↓

ConexaoBD()

↓

ConexaoBD()

↓

...
```

Se cada componente criar sua própria conexão sem controle, podemos chegar rapidamente ao limite.

Visualmente:

```
Aplicação

   │
   ├──► Conexão 1
   │
   ├──► Conexão 2
   │
   ├──► Conexão 3
   │
   ├──► Conexão 4
   │
   ├──► ...
   │
   └──► Conexão 100
```

Quando o limite é atingido:

```
nova tentativa de conexão

        ↓

       ❌

limite atingido
```

Portanto, precisamos controlar o acesso ao recurso.

---

# 🔄 O problema do recurso compartilhado

A conexão com o banco pode representar um recurso que deve ser compartilhado.

Em vez de termos:

```
Exportador
    │
    └──► Conexão própria

Processador
    │
    └──► Conexão própria

Notificador
    │
    └──► Conexão própria
```

podemos imaginar:

```
                    ConexãoBD

                       ▲
                       │
          ┌────────────┼────────────┐
          │            │            │
          │            │            │
      Exportador   Processador  Notificador
```

Todos acessam:

```
a mesma instância
```

---

# 🧠 Uma única instância

A ideia do Singleton é:

```
ConexaoBD

↓

Só pode existir uma instância
```

Portanto:

```
ConexaoBD()
ConexaoBD()
ConexaoBD()
```

não devem produzir:

```
objeto A
objeto B
objeto C
```

Mas sim:

```
objeto A ─────┐
              │
objeto B ─────┼──► mesma instância
              │
objeto C ─────┘
```

Podemos representar:

```
             ┌─────────────────┐
             │    ConexaoBD    │
             │                 │
             │ socket único    │
             │ conexão única   │
             └─────────────────┘
                ▲      ▲      ▲
                │      │      │
                │      │      │
           Exportador Processador Notificador
```

---

# 🎯 Intenção do Singleton

A intenção do padrão pode ser dividida em duas partes.

## 1. Garantir uma única instância

A classe deve controlar sua própria criação.

```
Singleton

↓

Existe uma instância?

        │
   ┌────┴────┐
   │         │
  Sim       Não
   │         │
   ▼         ▼
Retorna   Cria
existente instância
```

Depois da criação:

```
próximas chamadas

↓

retornam a mesma instância
```

---

## 2. Fornecer um ponto global de acesso

Além de garantir uma única instância, o Singleton fornece uma maneira centralizada de acessá-la.

Conceitualmente:

```
Singleton.getInstance()
```

ou, dependendo da implementação em Python:

```
Singleton()
```

O importante é que o cliente não precise criar várias instâncias independentes.

---

# 🏗️ Estrutura clássica do Singleton

A estrutura apresentada pelo GoF pode ser representada conceitualmente assim:

```
                 Singleton
              ┌───────────────┐
              │               │
              │ - instance    │
              │               │
              │ - Singleton() │
              │               │
              │ + getInstance │
              │               │
              └───────────────┘
                      ▲
                      │
                      │
                    Client
```

O Singleton possui:

```
uma referência para sua própria instância
```

e um mecanismo para:

```
criar a instância quando necessário

ou

retornar a instância que já existe
```

---

# 🔐 O construtor controlado

Uma característica importante do Singleton tradicional é controlar o construtor.

A ideia é impedir que o cliente faça livremente:

```
new Singleton()
```

ou, em Python:

```
Singleton()
```

para criar uma nova instância a cada chamada.

Em linguagens como Java e C++, isso pode ser feito tornando o construtor:

```
privado
```

Assim:

```
Client

   │
   │ não pode criar diretamente
   ▼

Singleton
```

O acesso acontece por meio de algo como:

```
getInstance()
```

Em Python, entretanto, não existe exatamente um modificador de acesso `private` como em Java.

Por isso, outras técnicas são utilizadas para controlar a criação.

---

# 🐍 Singleton em Python

Python possui características que tornam o Singleton diferente de sua implementação clássica em linguagens como Java ou C++.

Em Python, existem várias maneiras de implementar o conceito.

Neste estudo, iremos observar **três formas de implementação**, justamente para entender que o padrão não depende de uma única técnica.

Podemos pensar nas abordagens como:

```
Singleton

├── Implementação tradicional
│
├── Implementação utilizando decorator
│
└── Implementação utilizando metaclass
```

Além disso, existe uma característica muito importante da própria linguagem:

```
Módulos Python já possuem comportamento semelhante a Singleton.
```

---

# 📦 Módulos Python e Singleton

Em Python, quando um módulo é importado, ele é carregado e reutilizado pelo mecanismo de importação da linguagem.

Por exemplo:

```
config.py
```

pode conter determinados objetos compartilhados.

Outros arquivos podem fazer:

```
from config import configuracao
```

Em vez de criar uma nova instância independente toda vez, os diferentes consumidores podem utilizar o mesmo objeto disponibilizado pelo módulo.

Podemos representar:

```
                 config.py

                    │
                    ▼

             objeto compartilhado
                    ▲
                    │
          ┌─────────┼─────────┐
          │         │         │
          ▼         ▼         ▼
       módulo A  módulo B  módulo C
```

Por isso, em Python, muitas vezes o próprio sistema de módulos já resolve o problema que alguém tentaria resolver com Singleton.

Essa é uma das razões pelas quais o uso explícito do Singleton em Python deve ser analisado com cuidado.

---

# ⚠️ Singleton não significa "qualquer objeto global"

É importante diferenciar:

```
Singleton
```

de:

```
variável global
```

Uma variável global simplesmente fornece um objeto acessível globalmente.

O Singleton, por sua vez, encapsula a regra:

```
a classe possui uma única instância
```

e controla sua criação/acesso.

Porém, na prática, o Singleton frequentemente acaba funcionando como:

```
estado global compartilhado
```

E é justamente essa característica que pode gerar vários problemas de design.

---

# 🚨 Por que o Singleton é chamado de antipadrão?

O Singleton é chamado de antipadrão em diversos contextos porque suas características podem introduzir problemas importantes.

O problema não é simplesmente:

```
"ter uma única instância"
```

O problema está principalmente na combinação:

```
instância única

+

acesso global

+

estado compartilhado
```

Essa combinação pode aumentar o acoplamento e dificultar testes e manutenção.

---

# 🌎 O problema do estado global

Imagine:

```
Singleton

↓

possui estado compartilhado
```

Toda parte da aplicação que acessa o Singleton pode alterar esse estado.

Visualmente:

```
              Singleton
            estado global
                  ▲
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
     Serviço A Serviço B Serviço C
```

Se:

```
Serviço A
```

alterar o estado:

```
estado = X
```

o:

```
Serviço B
```

poderá observar essa alteração.

Isso cria uma dependência implícita.

---

# 🧪 O problema dos testes

Uma das maiores críticas ao Singleton está relacionada a testes unitários.

Imagine:

```
Singleton

↓

possui estado
```

O teste A executa:

```
Singleton.estado = "A"
```

Depois o teste termina.

O teste B começa:

```
Singleton.estado
```

Mas o estado pode continuar sendo:

```
"A"
```

Então o teste B pode receber dados deixados pelo teste A.

Visualmente:

```
Teste A
   │
   ▼
Singleton
   │
   ▼
estado = "A"
   │
   │
   ▼
Teste termina
   │
   │
   ▼
Teste B
   │
   ▼
Singleton
   │
   ▼
estado ainda é "A"
```

Isso pode gerar:

```
testes acoplados
```

ou:

```
dependência entre testes
```

O ideal para testes unitários é que cada teste possa possuir um estado controlado e isolado.

---

# 🔴 O problema do teste virar integração

Considere:

```
class Exportador:

    exportar():
        dados = ConexaoBD().consultar(...)
```

O código do `Exportador` não recebe explicitamente uma conexão.

Ele simplesmente acessa:

```
ConexaoBD()
```

O teste pode então fazer:

```
Exportador().exportar(imagens)
```

e acabar abrindo:

```
uma conexão real com o banco
```

Consequentemente:

```
Teste unitário

↓

Exportador

↓

Singleton

↓

Banco de dados real
```

O teste que deveria testar apenas:

```
Exportador
```

passa a depender de:

```
Banco de dados
```

Isso pode transformá-lo, na prática, em um teste de integração.

---

# 👻 Dependências escondidas

Outra crítica importante é que o Singleton pode esconder dependências.

Considere conceitualmente:

```
class Exportador:

    exportar():
        dados = ConexaoBD().consultar(...)
```

O construtor do `Exportador` não informa:

```
"Eu preciso de uma ConexaoBD."
```

A dependência está escondida dentro do método.

Visualmente:

```
Exportador

   │
   │ dependência escondida
   ▼

ConexaoBD
```

Uma abordagem mais explícita seria:

```
Exportador

   │
   │ recebe
   ▼

ConexaoBD
```

Por exemplo:

```
Exportador(bd)
```

Agora a dependência pode ser observada diretamente.

Conceitualmente:

```
bd = ConexaoBD()

Exportador(bd)
Processador(bd)
Notificador(bd)
```

A conexão continua sendo compartilhada, mas o compartilhamento não precisa necessariamente estar escondido dentro das classes.

---

# 🧩 Singleton e Injeção de Dependência

Uma alternativa comum ao Singleton é utilizar:

> **Injeção de Dependência**

Em vez de:

```
Exportador

↓

ConexaoBD()
```

podemos ter:

```
Exportador

← ConexaoBD
```

Ou seja, a dependência é fornecida externamente.

Visualmente:

```
              Aplicação

                  │
                  │ cria
                  ▼

              ConexaoBD
                  │
          ┌───────┼───────┐
          │       │       │
          ▼       ▼       ▼
      Exportador Processador Notificador
```

Nesse modelo, a aplicação pode controlar quantas instâncias existem.

Portanto:

```
uma instância compartilhada
```

não necessariamente exige:

```
Singleton
```

Podemos simplesmente criar uma instância e passá-la para quem precisa.

---

# 🆚 Singleton versus dependência explícita

Com Singleton:

```
Exportador
    │
    │ procura
    ▼
Singleton
```

A dependência é implícita.

Com injeção de dependência:

```
Aplicação
    │
    │ fornece
    ▼
Exportador
```

A dependência fica explícita.

Podemos visualizar:

```
Singleton:

Exportador ─────► ConexaoBD
                    ▲
                    │
                global

Injeção:

Aplicação
   │
   ├──► ConexaoBD
   │
   └──► Exportador
           ▲
           │
           └── recebe ConexaoBD
```

---

# 🧵 Singleton e concorrência

Existe ainda outro problema importante:

> **Multithreading**

Imagine duas threads acessando o Singleton simultaneamente.

```
Thread A
   │
   ▼
verifica se existe instância

Thread B
   │
   ▼
verifica se existe instância
```

Se as duas verificarem exatamente ao mesmo tempo:

```
instância ainda não existe
```

ambas podem tentar criá-la.

Visualmente:

```
              Singleton
                  ▲
          ┌───────┴───────┐
          │               │
       Thread A         Thread B
          │               │
          ▼               ▼
     verifica         verifica
     instância        instância
          │               │
          ▼               ▼
       não existe       não existe
          │               │
          ▼               ▼
       cria A            cria B
```

O resultado pode ser:

```
duas instâncias
```

Isso viola a promessa do Singleton.

---

# 🔒 O problema do Lock

Por isso, em aplicações multithread, uma implementação clássica do Singleton pode precisar de algum mecanismo de sincronização.

Conceitualmente:

```
if instance == null:

    adquirir lock

    if instance == null:
        instance = Singleton()

    liberar lock
```

A ideia é garantir que somente uma thread possa realizar a criação naquele momento.

Visualmente:

```
Thread A
   │
   ▼
adquire Lock
   │
   ▼
cria instância
   │
   ▼
libera Lock
   │
   ▼
Thread B
   │
   ▼
obtém a mesma instância
```

Portanto:

> **Sem sincronização adequada, uma implementação de Singleton pode falhar em garantir unicidade em ambientes concorrentes.**

---

# 🐍 Como isso se relaciona com Python?

Python possui características próprias relacionadas à execução concorrente e ao modelo de threads.

Mesmo assim, o conceito permanece importante:

```
se a aplicação puder acessar a criação
simultaneamente,

↓

é necessário considerar concorrência
```

Portanto, uma implementação de Singleton não deve simplesmente assumir:

```
"ninguém vai chamar ao mesmo tempo."
```

Se o objeto for realmente compartilhado entre threads, a estratégia de criação deve ser analisada cuidadosamente.

---

# 🏗️ As três formas de implementação estudadas

Neste projeto de estudos, iremos analisar três formas de implementar o Singleton em Python.

A intenção é perceber que:

```
Singleton

não é uma única implementação.
```

O padrão descreve uma intenção:

```
uma única instância

+

ponto de acesso
```

A técnica utilizada para atingir esse objetivo pode variar.

---

# 1️⃣ Singleton utilizando `__new__`

Uma primeira abordagem utiliza o método especial:

```
__new__
```

É importante entender a diferença entre:

```
__new__
```

e:

```
__init__
```

O método:

```
__new__
```

está relacionado à:

```
criação da instância
```

Enquanto:

```
__init__
```

está relacionado à:

```
inicialização da instância
```

Essa diferença é importante porque o Singleton precisa controlar justamente:

```
criação do objeto
```

Podemos representar:

```
Singleton()

   │
   ▼
__new__()

   │
   ├── instância já existe?
   │
   ├── Sim → retorna existente
   │
   └── Não → cria instância
```

Depois:

```
__init__()
```

é utilizado para inicialização conforme o comportamento da implementação.

---

# 2️⃣ Singleton utilizando Decorator

Outra abordagem consiste em utilizar um:

> **Decorator**

O decorator pode encapsular a lógica responsável por controlar a criação.

Conceitualmente:

```
              Singleton Decorator
                      │
                      ▼
                 MinhaClasse
                      │
                      ▼
              controla criação
```

Em vez de colocar toda a lógica diretamente dentro da classe, podemos utilizar uma camada externa.

Visualmente:

```
Decorator
    │
    ▼
Classe original
    │
    ▼
controle de instância
```

A ideia é separar:

```
responsabilidade da classe

```

de:

```
responsabilidade de controlar
a quantidade de instâncias
```

---

# 3️⃣ Singleton utilizando Metaclass

Uma terceira abordagem utiliza:

> **Metaclass**

Metaclasses são um conceito mais avançado de Python.

De forma simplificada:

```
objetos são instâncias de classes

classes são instâncias de metaclasses
```

Podemos imaginar:

```
Objeto
   │
   ▼
Classe
   │
   ▼
Metaclass
```

A metaclass pode controlar determinados aspectos da criação das instâncias de uma classe.

No caso do Singleton:

```
Metaclass

↓

controla criação

↓

verifica se a instância já existe

↓

retorna existente

ou

↓

cria uma nova
```

Visualmente:

```
             Metaclass
                  │
                  ▼
           controla classe
                  │
                  ▼
             Singleton
                  │
                  ▼
             uma instância
```

Essa abordagem é mais avançada e permite compreender melhor o funcionamento interno do modelo de objetos do Python.

---

# 📊 Comparando as três abordagens

Podemos resumir:

| Abordagem | Ideia principal |
| --- | --- |
| **`__new__`**            | Controlar diretamente a criação da instância       |
| **Decorator**            | Encapsular o controle de instância em um decorator |
| **Metaclass**            | Delegar o controle da criação para uma metaclass   |

Todas procuram alcançar:

```
uma única instância
```

mas utilizam mecanismos diferentes.

---

# 🧠 O que realmente importa no padrão

É importante não confundir:

```
Singleton

```

com:

```
__new__

Decorator

Metaclass
```

Esses são apenas mecanismos de implementação.

O padrão é definido pela intenção:

```
Garantir uma única instância
e fornecer acesso a ela.
```

Portanto:

```
Singleton
   │
   ├── pode ser implementado com __new__
   │
   ├── pode ser implementado com decorator
   │
   └── pode ser implementado com metaclass
```

---

# 🗄️ Exemplo-problema deste projeto

Neste projeto, iremos utilizar como exemplo um sistema que precisa acessar um banco de dados PostgreSQL utilizado por um acervo.

Imagine uma aplicação que possui diferentes componentes:

```
Exportador

Processador

Notificador
```

Todos precisam acessar:

```
PostgreSQL

postgres://acervo
```

Uma implementação ingênua poderia criar uma nova conexão sempre que um componente precisasse consultar o banco.

Teríamos:

```
Exportador
    │
    ▼
ConexaoBD()
    │
    ▼
nova conexão

Processador
    │
    ▼
ConexaoBD()
    │
    ▼
nova conexão

Notificador
    │
    ▼
ConexaoBD()
    │
    ▼
nova conexão
```

Isso gera:

```
várias instâncias

+

vários sockets

+

vários handshakes

+

maior consumo de recursos
```

---

# 💥 O problema concreto

Considere:

```
class ConexaoBD
```

Cada vez que ela é criada:

```
ConexaoBD("postgres://acervo")
```

o sistema simula:

```
abrir conexão

↓

realizar handshake

↓

autenticar

↓

negociar protocolo

↓

criar socket
```

No exemplo da aula:

```
3 × 1,5 segundos
```

para realizar o handshake.

Portanto, criar várias conexões pode ser caro.

Além disso:

```
PostgreSQL

máximo considerado:
100 conexões
```

Então, criar conexões indiscriminadamente pode consumir rapidamente o limite disponível.

---

# 🔴 O problema de ter dois objetos representando o mesmo recurso

Considere:

```
bd1 = ConexaoBD("postgres://acervo")

bd2 = ConexaoBD("postgres://acervo")
```

Podemos acabar com:

```
bd1 ───► conexão A
bd2 ───► conexão B
```

Embora ambos representem:

```
postgres://acervo
```

eles são objetos diferentes.

O requisito do nosso exemplo é que o recurso seja compartilhado:

```
bd1 ─────┐
         │
bd2 ─────┼──► mesma conexão
         │
bd3 ─────┘
```

Essa é a situação que o Singleton pretende modelar.

---

# 🧩 O papel do Singleton no exemplo

A classe:

```
ConexaoBD
```

será responsável por representar a conexão compartilhada.

A ideia conceitual será:

```
ConexaoBD

      │
      ▼

Existe instância?

      │
 ┌────┴────┐
 │         │
Sim       Não
 │         │
 ▼         ▼
retorna   cria
existente instância
```

Depois da primeira criação:

```
ConexaoBD()

↓

instância criada
```

as próximas chamadas:

```
ConexaoBD()

ConexaoBD()

ConexaoBD()
```

deverão retornar:

```
a mesma instância
```

---

# 🔄 Fluxo esperado

Imagine:

```
Exportador
```

solicitando a conexão.

```
Exportador

↓

ConexaoBD()

↓

instância não existe

↓

cria conexão

↓

retorna conexão
```

Depois:

```
Processador

↓

ConexaoBD()

↓

instância já existe

↓

retorna mesma conexão
```

Depois:

```
Notificador

↓

ConexaoBD()

↓

instância já existe

↓

retorna mesma conexão
```

Visualmente:

```
              ConexaoBD

                  │
             primeira chamada
                  │
                  ▼
            cria instância
                  │
                  ▼
          ┌───────────────┐
          │   ConexãoBD   │
          │               │
          │ socket único  │
          └───────────────┘
             ▲     ▲     ▲
             │     │     │
             │     │     │
        Exportador │ Notificador
                   │
              Processador
```

---

# 🧪 O que iremos observar durante a implementação

Ao implementar as diferentes versões do Singleton, será importante observar:

```
A primeira chamada cria a instância?
A segunda chamada reutiliza a instância?
Os objetos retornados são realmente o mesmo objeto?
O custo de criação acontece apenas uma vez?
O recurso é realmente compartilhado?
```

E também:

```
O que acontece em testes?
O que acontece com estado compartilhado?
O que acontece em concorrência?
```

Essas perguntas são mais importantes do que simplesmente conseguir escrever o código.

---

# 🧪 Singleton e identidade dos objetos

Uma maneira conceitual de verificar o Singleton é comparar a identidade dos objetos.

Imagine:

```
bd1 = ConexaoBD()

bd2 = ConexaoBD()
```

Queremos:

```
bd1

e

bd2

```

apontando para:

```
o mesmo objeto
```

Visualmente:

```
bd1 ─────┐
         │
         ▼
     ┌──────────┐
     │ ConexaoBD│
     └──────────┘
         ▲
         │
bd2 ─────┘
```

Não queremos:

```
bd1 ───► objeto A

bd2 ───► objeto B
```

Portanto, o teste conceitual mais importante é:

```
bd1 is bd2
```

O resultado esperado é:

```
True
```

---

# 🌍 Ponto global de acesso

Uma das características tradicionais do Singleton é fornecer um:

> **Ponto global de acesso**

Isso significa que diferentes partes da aplicação conseguem obter a instância sem receber necessariamente uma referência diretamente.

Conceitualmente:

```
Cliente A ─────┐
               │
Cliente B ─────┼──► Singleton
               │
Cliente C ─────┘
```

Essa característica é simultaneamente:

```
uma vantagem

e

uma fonte de problemas.
```

Ela facilita o acesso:

```
qualquer parte da aplicação
pode obter a instância
```

mas também cria:

```
acoplamento global
```

---

# 🔗 Singleton e acoplamento

Imagine:

```
Exportador

↓

ConexaoBD()
```

Agora o `Exportador` depende diretamente de:

```
ConexaoBD
```

Se muitos componentes fizerem isso:

```
Exportador → ConexaoBD

Processador → ConexaoBD

Notificador → ConexaoBD

Relatorio → ConexaoBD

API → ConexaoBD
```

teremos vários pontos do sistema acoplados ao Singleton.

Visualmente:

```
                 ConexaoBD
                ▲ ▲ ▲ ▲ ▲
                │ │ │ │ │
                │ │ │ │ │
                ▼ ▼ ▼ ▼ ▼
             vários clientes
```

Isso pode dificultar alterações futuras.

---

# 🧠 O Singleton viola o S do SOLID?

O Singleton é frequentemente associado a uma possível violação do:

> **S — Single Responsibility Principle**

O princípio da responsabilidade única afirma, de forma resumida, que uma classe deve possuir uma responsabilidade bem definida.

No Singleton, uma classe pode acabar assumindo duas responsabilidades:

```
1. Executar sua responsabilidade de negócio

2. Controlar sua própria criação e unicidade
```

Por exemplo:

```
ConexaoBD

├── gerenciar comunicação com banco
│
└── controlar existência de uma única instância
```

Essa combinação pode aumentar a responsabilidade da classe.

Por isso, a crítica apresentada nas aulas é que o Singleton pode acabar violando o princípio da responsabilidade única.

---

# ⚠️ Singleton não deve ser utilizado automaticamente

É importante não concluir:

```
"Preciso compartilhar um objeto."

↓

"Vou usar Singleton."
```

Existe uma diferença entre:

```
compartilhar uma instância
```

e:

```
obrigar a classe a ser Singleton
```

Por exemplo, podemos simplesmente fazer:

```
bd = ConexaoBD()
```

e passar essa referência para os componentes que precisam dela:

```
Exportador(bd)

Processador(bd)

Notificador(bd)
```

Nesse caso:

```
há uma única instância

```

mas:

```
ConexaoBD
```

não necessariamente precisa ser implementada como Singleton.

Essa distinção é fundamental.

---

# 🏊 Pool de conexões

Um exemplo especialmente importante é:

> **Pool de conexões**

Um pool mantém um conjunto de conexões que podem ser reutilizadas.

Podemos imaginar:

```
                Connection Pool

       ┌──────────┬──────────┬──────────┐
       │          │          │          │
       ▼          ▼          ▼          ▼
   conexão 1  conexão 2  conexão 3  conexão 4
```

Quando um componente precisa acessar o banco:

```
Cliente

↓

Pool

↓

obtém uma conexão disponível
```

Depois:

```
Cliente termina

↓

devolve conexão

↓

Pool reutiliza
```

Nesse cenário, o objeto que deve ser único pode ser:

```
o Pool
```

e não necessariamente:

```
cada conexão
```

Essa distinção é extremamente importante.

---

# 🏊 Pool é Singleton, conexões não

Podemos representar:

```
                 Pool
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
     Conexão   Conexão   Conexão
```

O pool pode ser um objeto compartilhado:

```
Pool único
```

mas pode gerenciar:

```
várias conexões
```

Portanto:

> **O Singleton não significa que todos os recursos relacionados devem possuir uma única instância.**

Ele deve ser aplicado somente ao objeto que realmente precisa ter unicidade.

---

# 📝 Cache e Singleton

Outro exemplo frequentemente associado ao Singleton é:

```
Cache
```

Imagine:

```
Aplicação

↓

Cache compartilhado
```

Vários componentes podem consultar:

```
Cache

├── dados A
├── dados B
├── dados C
└── dados D
```

Ter um único cache pode fazer sentido em determinadas arquiteturas.

Porém, novamente, existe uma questão importante:

```
o cache realmente precisa ser um Singleton?
```

Ou seria suficiente criar:

```
cache = Cache()
```

e passar a referência para os componentes?

A resposta depende do design da aplicação.

---

# 📝 Logger e Singleton

Outro exemplo clássico é:

> **Logger**

Imagine:

```
Aplicação

├── Serviço A
├── Serviço B
├── Serviço C
└── Serviço D
```

Todos precisam registrar mensagens.

Podemos ter:

```
               Logger
                 ▲
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
     Serviço A Serviço B Serviço C
```

Nesse contexto, um logger compartilhado pode ser útil.

Porém, novamente, bibliotecas e frameworks frequentemente já oferecem mecanismos próprios para gerenciamento de logging.

Por isso:

> **Antes de implementar um Singleton manualmente, devemos verificar se a infraestrutura utilizada já resolve o problema.**

---

# 🚫 Quando não utilizar Singleton

O Singleton tende a ser inadequado quando:

```
a aplicação precisa de múltiplas instâncias independentes;
```

ou:

```
o objeto possui estado que deveria ser isolado;
```

ou:

```
o objeto precisa ser facilmente substituído durante testes;
```

ou:

```
a dependência pode ser fornecida explicitamente;
```

ou:

```
o framework já possui um mecanismo de gerenciamento de ciclo de vida;
```

ou:

```
uma variável ou módulo compartilhado já resolve o problema de maneira mais simples.
```

---

# 🎯 Quando o Singleton pode fazer sentido?

O Singleton pode ser considerado quando existe uma necessidade real de:

```
uma única instância
```

e essa unicidade faz parte do design do sistema.

Alguns exemplos possíveis:

```
Configuração global controlada
Logger compartilhado
Gerenciador único de determinado recurso
Pool de conexões
Cache compartilhado
```

Mas sempre devemos perguntar:

```
Esse objeto realmente precisa ser único?

```

E também:

```
Ele precisa ser globalmente acessível?

```

E:

```
O framework já possui uma solução para isso?
```

---

# 🧠 Singleton versus módulo Python

Em Python, existe uma comparação especialmente importante:

```
Singleton tradicional
```

versus:

```
módulo Python
```

Um módulo pode fornecer:

```
funções

objetos

configurações

estado compartilhado
```

e o mecanismo de importação permite que diferentes partes da aplicação utilizem o mesmo módulo.

Por isso, para alguns problemas, podemos simplesmente utilizar:

```
config.py
```

ou:

```
database.py
```

em vez de construir uma estrutura complexa de Singleton.

A pergunta deve ser:

```
Eu realmente preciso de uma classe Singleton?

```

ou:

```
Um módulo já resolve o problema?
```

---

# 📚 Singleton segundo o GoF

No livro:

> **Design Patterns: Elements of Reusable Object-Oriented Software**

de:

```
Erich Gamma
Richard Helm
Ralph Johnson
John Vlissides
```

o Singleton está entre os padrões:

```
Criacionais
```

Sua intenção está relacionada a:

```
garantir uma única instância

+

fornecer um ponto global de acesso
```

O GoF também discute características como:

```
controle da criação da instância

acesso à instância

extensibilidade

unicidade
```

O estudo do padrão não deve se limitar à implementação.

O mais importante é compreender:

```
qual problema está sendo resolvido

e

quais consequências a solução introduz.
```

---

# 🌐 Singleton segundo o Refactoring Guru

O Refactoring Guru classifica o Singleton como:

```
Padrão criacional
```

A ideia central apresentada é:

```
garantir que uma classe tenha uma única instância

e

fornecer um ponto de acesso global a essa instância.
```

Referência:

[https://refactoring.guru/pt-br/design-patterns/singleton](https://refactoring.guru/pt-br/design-patterns/singleton)

O site também destaca que o Singleton é considerado controverso justamente por seus efeitos sobre:

```
estado global

acoplamento

testabilidade
```

Por isso, estudar o padrão também significa estudar suas desvantagens.

---

# 🧩 Estrutura conceitual completa

Podemos representar o Singleton tradicional da seguinte forma:

```
                       Client
                          │
                          │
                          ▼
                  getInstance()
                          │
                          ▼
                 ┌────────────────┐
                 │    Singleton   │
                 │                │
                 │ - instance     │
                 │                │
                 │ - constructor  │
                 │                │
                 │ + getInstance  │
                 └────────────────┘
                          │
                          │
                          ▼
                   única instância
```

A sequência é:

```
Cliente
   │
   ▼
solicita instância
   │
   ▼
Singleton verifica
   │
   ├── instância existe?
   │
   │       ├── Sim
   │       │    │
   │       │    ▼
   │       │ retorna existente
   │       │
   │       └── Não
   │            │
   │            ▼
   │       cria instância
   │            │
   │            ▼
   │       retorna instância
```

---

# 🔄 Ciclo de vida da instância

O Singleton normalmente possui um ciclo de vida semelhante a:

```
Estado inicial

↓

instância não existe

↓

primeira solicitação

↓

criação da instância

↓

instância armazenada

↓

segunda solicitação

↓

instância já existe

↓

retorna instância existente

↓

terceira solicitação

↓

retorna mesma instância

↓

...
```

Visualmente:

```
                início

                  │
                  ▼

        instância não existe

                  │
                  ▼

          primeira chamada

                  │
                  ▼

          cria instância

                  │
                  ▼

        ┌──────────────────┐
        │ instância única  │
        └──────────────────┘
             ▲    ▲    ▲
             │    │    │
             │    │    │
         chamada chamada chamada
            2      3      4
```

---

# 🧠 Lazy Initialization

Uma característica comum das implementações de Singleton é a:

> **Inicialização preguiçosa — Lazy Initialization**

Isso significa:

```
não criar a instância imediatamente
```

mas:

```
criar somente quando alguém solicitar pela primeira vez.
```

Podemos representar:

```
Programa inicia

↓

Singleton ainda não existe

↓

Cliente solicita

↓

cria instância

↓

reutiliza nas próximas chamadas
```

Isso pode evitar criar um recurso caro caso ele nunca seja utilizado.

No nosso exemplo:

```
ConexaoBD
```

pode ser criada somente quando realmente houver necessidade de acessar o banco.

---

# ⚡ Singleton e recursos caros

Esse comportamento pode ser especialmente interessante quando a criação do objeto é cara.

Por exemplo:

```
abrir conexão

↓

autenticar

↓

negociar protocolo

↓

configurar recurso
```

Se a aplicação nunca utilizar o banco:

```
não há necessidade de criar a conexão
```

Se utilizar:

```
cria na primeira necessidade

↓

reutiliza depois
```

---

# ⚠️ Lazy Initialization não resolve todos os problemas

Apesar de útil, a inicialização preguiçosa não resolve automaticamente:

```
concorrência

testabilidade

acoplamento

estado global

dependências escondidas
```

Por exemplo:

```
duas threads

↓

ambas percebem que a instância não existe

↓

ambas tentam criar

↓

problema
```

Por isso:

> **Lazy Initialization e Singleton thread-safe são problemas relacionados, mas não são a mesma coisa.**

---

# 🧪 Singleton e isolamento de testes

Imagine:

```
Teste 1
   │
   ▼
Singleton
   │
   ▼
estado = X
```

Depois:

```
Teste 2
   │
   ▼
Singleton
   │
   ▼
estado = X
```

O segundo teste pode herdar o estado do primeiro.

Idealmente:

```
Teste 1

↓

ambiente isolado

Teste 2

↓

ambiente isolado
```

Mas o Singleton pode criar:

```
estado compartilhado
```

entre eles.

Essa é uma das razões pelas quais o Singleton é frequentemente criticado em ambientes de testes unitários.

---

# 🧠 Uma observação importante sobre o problema do banco

É importante não concluir que:

```
"Singleton é a solução correta para conexões de banco."
```

Na prática, aplicações modernas normalmente utilizam:

```
connection pools

frameworks

gerenciadores de recursos

injeção de dependência

mecanismos de ciclo de vida
```

O objetivo deste projeto é:

```
estudar o Singleton
```

e utilizar:

```
ConexaoBD
```

como um exemplo didático para visualizar:

```
criação única

reutilização

recurso compartilhado

ponto global de acesso
```

Portanto, o exemplo não deve ser interpretado como uma recomendação arquitetural para substituir um pool de conexões por um Singleton.

---

# 🟢 Prós

## Uma única instância

O Singleton garante que exista:

```
uma única instância
```

da classe dentro do escopo definido pela implementação.

---

## Controle da criação

A própria classe pode controlar:

```
quando a instância é criada

e

quando uma instância existente é retornada.
```

---

## Acesso centralizado

Existe um ponto conhecido para obter a instância:

```
Singleton
```

Isso pode simplificar o acesso a determinados recursos compartilhados.

---

## Lazy Initialization

A instância pode ser criada:

```
somente quando necessária.
```

Isso pode ser interessante para objetos cuja criação possui custo significativo.

---

## Compartilhamento de recursos

Pode ser útil quando realmente existe a necessidade de compartilhar:

```
um recurso único
```

como determinado gerenciador ou coordenador.

---

## Evita múltiplas inicializações

No exemplo da conexão:

```
primeira chamada

↓

cria conexão
```

e:

```
chamadas seguintes

↓

reutilizam conexão
```

Isso evita repetir desnecessariamente a inicialização do recurso.

---

# 🔴 Contras

## Estado global

O Singleton frequentemente funciona como:

```
estado global compartilhado
```

Isso pode tornar o comportamento do sistema mais difícil de acompanhar.

---

## Dependências escondidas

Uma classe pode acessar o Singleton diretamente sem declarar que depende dele.

Por exemplo:

```
Exportador

↓

ConexaoBD()
```

A dependência fica escondida dentro da implementação.

---

## Dificuldade de testes

O estado compartilhado pode sobreviver entre testes e dificultar o isolamento.

---

## Maior acoplamento

Várias classes podem passar a depender diretamente do Singleton.

```
Classe A ──┐
Classe B ──┤
Classe C ──┼──► Singleton
Classe D ──┤
Classe E ──┘
```

---

## Problemas de concorrência

Uma implementação inadequada pode criar mais de uma instância quando acessada simultaneamente por múltiplas threads.

---

## Pode violar o princípio da responsabilidade única

A classe pode acabar sendo responsável tanto por:

```
sua função principal
```

quanto por:

```
controlar sua própria instanciação.
```

---

## Pode dificultar substituição de dependências

Em testes ou diferentes ambientes, pode ser desejável substituir:

```
ConexaoBD
```

por:

```
MockConexaoBD
```

ou:

```
FakeConexaoBD
```

O acesso global pode dificultar essa substituição.

---

## Pode ser desnecessário

Em Python, muitas vezes:

```
módulos

injeção de dependência

objetos compartilhados

frameworks
```

podem resolver o problema sem a necessidade de um Singleton explícito.

---

# 🆚 Singleton e objeto compartilhado

Existe uma diferença conceitual importante entre:

```
Singleton
```

e:

```
objeto compartilhado.
```

Podemos simplesmente fazer:

```
bd = ConexaoBD()
```

e compartilhar:

```
Exportador(bd)

Processador(bd)

Notificador(bd)
```

Temos:

```
uma instância compartilhada
```

mas não necessariamente:

```
uma classe Singleton.
```

Essa abordagem mantém a responsabilidade de criar e distribuir o objeto fora da classe.

Visualmente:

```
                Aplicação
                   │
                   ▼
              cria ConexaoBD
                   │
                   ▼
              ┌───────────┐
              │ ConexaoBD │
              └───────────┘
                ▲    ▲    ▲
                │    │    │
                ▼    ▼    ▼
                A    B    C
```

Esse modelo é importante porque mostra que:

> **Compartilhamento de instância não exige necessariamente Singleton.**

---

# 🧠 A pergunta mais importante

Antes de implementar um Singleton, devemos perguntar:

```
Por que preciso de uma única instância?
```

Depois:

```
Por que ela precisa ser globalmente acessível?
```

Depois:

```
Posso simplesmente criar uma instância
e compartilhá-la explicitamente?
```

E finalmente:

```
Existe alguma solução fornecida pelo framework
ou pela própria linguagem?
```

Essas perguntas ajudam a evitar o uso indiscriminado do padrão.

---

# 🎯 Quando utilizar?

O Singleton pode ser considerado quando:

```
Existe exatamente um recurso lógico
que deve possuir uma única instância.
```

E quando:

```
essa unicidade é uma regra real do domínio
ou da infraestrutura.
```

Exemplos possíveis:

```
Gerenciador único de determinado recurso
Logger compartilhado
Pool de conexões
Cache compartilhado
Configuração global controlada
```

Mas sempre devemos verificar se:

```
um módulo

ou

injeção de dependência

ou

um framework

```

já resolve o problema de forma mais simples.

---

# 🚫 Quando evitar?

Evite utilizar Singleton apenas porque:

```
"quero acessar esse objeto de qualquer lugar."
```

Esse é um forte sinal de que o padrão pode estar sendo utilizado apenas para criar:

```
estado global.
```

Também é importante evitar quando:

```
existem múltiplas instâncias legítimas;
o estado deveria ser isolado;
a classe é frequentemente utilizada em testes unitários;
a dependência pode ser fornecida explicitamente;
o framework já possui gerenciamento de ciclo de vida;
```

ou:

```
um módulo Python resolve o problema.
```

---

# 📊 Resumo das responsabilidades

| Elemento | Responsabilidade |
| --- | --- |
| **Singleton**            | Garantir que exista uma única instância   |
| **Instância**            | Representar o recurso compartilhado       |
| **Cliente**              | Solicitar e utilizar a instância          |
| **Método de acesso**     | Retornar a instância existente ou criá-la |
| **Estado interno**       | Ser compartilhado entre os consumidores   |

No exemplo:

| Conceito | Exemplo |
| --- | --- |
| **Singleton**             | `ConexaoBD`                                         |
| **Recurso compartilhado** | Conexão com PostgreSQL                              |
| **Clientes**              | Exportador, Processador, Notificador                |
| **Ponto de acesso**       | Mecanismo utilizado pela implementação do Singleton |
| **Problema**              | Evitar múltiplas conexões/instâncias desnecessárias |

---

# 🔄 Fluxo completo do exemplo

Podemos resumir o problema desta maneira:

```
                    Aplicação
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
   Exportador      Processador     Notificador
        │               │               │
        └───────────────┼───────────────┘
                        │
                        ▼
                    ConexaoBD
                        │
                        ▼
                 existe instância?
                    /         \
                  Sim          Não
                  │             │
                  ▼             ▼
             reutiliza        cria
                  │             │
                  └──────┬──────┘
                         │
                         ▼
                 mesma instância
                         │
                         ▼
                  PostgreSQL
```

A ideia é:

```
Primeira chamada

↓

cria o recurso
```

Enquanto:

```
chamadas seguintes

↓

reutilizam o recurso
```

---

# 🧠 A essência do Singleton

Podemos memorizar o Singleton com três ideias:

```
1. Uma única instância
2. Controle da criação
3. Ponto de acesso à instância
```

Visualmente:

```
             Singleton

                 │
       ┌─────────┴─────────┐
       │                   │
       ▼                   ▼
 uma instância        acesso controlado
       │                   │
       └─────────┬─────────┘
                 │
                 ▼
        recurso compartilhado
```

---

# 📝 Resumo Final

O **Singleton** é um Design Pattern **criacional** cujo objetivo é:

> **Garantir que uma classe tenha somente uma instância e fornecer um ponto global de acesso a ela.**

A estrutura tradicional envolve:

```
uma instância armazenada

+

um mecanismo de acesso

+

controle da criação
```

No nosso exemplo, utilizaremos:

```
ConexaoBD
```

para representar um recurso compartilhado.

A aplicação possui vários componentes:

```
Exportador

Processador

Notificador
```

Todos precisam acessar:

```
PostgreSQL
```

Uma implementação ingênua poderia produzir:

```
Exportador → conexão 1

Processador → conexão 2

Notificador → conexão 3
```

Isso pode gerar:

```
múltiplos sockets

múltiplos handshakes

maior consumo de recursos

maior número de conexões

possibilidade de atingir limites do banco
```

Com o Singleton, a ideia conceitual passa a ser:

```
Exportador ─────┐
                │
Processador ────┼──► ConexaoBD única
                │
Notificador ────┘
```

As diferentes partes da aplicação utilizam:

```
a mesma instância.
```

Neste estudo também veremos três formas de implementar o Singleton em Python:

```
__new__

Decorator

Metaclass
```

Além disso, veremos uma característica importante da própria linguagem:

```
Módulos Python já possuem comportamento
que muitas vezes elimina a necessidade
de um Singleton explícito.
```

Porém, o ponto mais importante não é aprender a escrever:

```
class Singleton
```

O ponto principal é entender as consequências arquiteturais.

O Singleton pode oferecer:

```
uma única instância

controle da criação

acesso compartilhado

lazy initialization

reutilização de recursos
```

Mas também pode introduzir:

```
estado global

dependências escondidas

acoplamento

dificuldade de testes

problemas de concorrência

violação do princípio da responsabilidade única

dificuldade de substituição de dependências
```

Por isso:

> **Singleton não deve ser utilizado simplesmente porque precisamos compartilhar um objeto.**

Primeiro devemos perguntar:

```
O objeto realmente precisa ser único?
```

Depois:

```
Ele precisa ser globalmente acessível?
```

E finalmente:

```
Existe uma alternativa mais simples?
```

Como:

```
injeção de dependência

objeto compartilhado

módulo Python

pool de recursos

gerenciamento fornecido pelo framework
```

A principal ideia para memorizar é:

> **Singleton = garantir uma única instância + fornecer um ponto de acesso a ela.**

E uma segunda ideia é igualmente importante:

> **O fato de o Singleton ser um padrão do GoF não significa que ele deva ser utilizado sempre que existir um objeto compartilhado.**

No exemplo deste projeto:

```
                 ConexaoBD
                     │
              única instância
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
   Exportador    Processador  Notificador
        │            │            │
        └────────────┼────────────┘
                     │
                     ▼
                 PostgreSQL
```

A implementação servirá para estudar o mecanismo de:

```
criação única

↓

reutilização

↓

compartilhamento

↓

acesso controlado
```

mas também para compreender por que o Singleton é considerado por muitos desenvolvedores um padrão **controverso** e, em determinados contextos, um possível **antipadrão**.
