# 🧬 Prototype — Padrão de Projeto Criacional

> **Referências principais:**  
> - [Refactoring Guru — Prototype](https://refactoring.guru/pt-br/design-patterns/prototype)
> - **Design Patterns: Elements of Reusable Object-Oriented Software** — Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides (GoF)

---

# 📌 1. O que é o Prototype?

O **Prototype** é um **Design Pattern criacional** utilizado para criar novos objetos a partir da **cópia de um objeto existente**, chamado de **protótipo**.

Em vez de construir um objeto completamente novo a partir de sua classe, o Prototype permite que o próprio objeto seja responsável por criar uma cópia de si mesmo.

A ideia central pode ser resumida assim:

```text
Objeto existente
       │
       │ clone()
       ▼
Novo objeto
```

Enquanto uma criação tradicional parte diretamente de uma classe:

```text
Classe
  │
  │ instanciação
  ▼
Novo objeto
```

o Prototype parte de uma instância já existente:

```text
Objeto existente
       │
       │ clonagem
       ▼
Cópia do objeto
```

Essa abordagem é especialmente interessante quando o objeto já possui uma configuração que seria trabalhosa, repetitiva ou custosa de reconstruir.

---

# 🎯 2. Intenção do padrão

A definição apresentada pelo **GoF** para o Prototype pode ser entendida como:

> **Especificar os tipos de objetos a serem criados usando uma instância protótipo e criar novos objetos pela cópia desse protótipo.**

O ponto mais importante dessa definição é perceber que o objeto que servirá como modelo já existe.

Assim:

```text
Protótipo
    │
    │ clone()
    ├───────────────┐
    ▼               ▼
Cópia 1          Cópia 2
```

O cliente não precisa necessariamente saber todos os detalhes internos necessários para construir aquele objeto.

Ele simplesmente solicita:

```text
"Faça uma cópia de você."
```

---

# 🧠 3. O problema que o Prototype resolve

O problema começa quando temos um objeto e precisamos criar **uma cópia exata ou muito semelhante dele**.

À primeira vista, parece simples:

```python
copia = Forma()

copia.x = original.x
copia.y = original.y
copia.cor = original.cor
```

Parece que resolvemos o problema.

Porém, essa abordagem possui algumas dificuldades.

---

## 🔍 3.1. Nem todo campo é visível de fora

Considere uma classe como:

```python
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        self.__cache_area = 3.14159 * raio ** 2
        self.__id_render = _proximo_id()
```

Existem informações que fazem parte do estado interno do objeto:

```text
Circulo
│
├── raio
├── __cache_area
└── __id_render
```

O código externo pode não conseguir simplesmente acessar ou reproduzir todos esses detalhes corretamente.

Isso significa que tentar copiar o objeto manualmente pode ser problemático.

---

# 🧱 4. O problema de conhecer a classe concreta

Existe ainda outro problema.

Suponha que exista uma função responsável por duplicar uma forma:

```python
def duplicar(forma: Forma) -> Forma:
    nova = Circulo(...)
    ...
```

Nesse caso, o código que realiza a cópia precisa conhecer uma classe concreta:

```text
duplicar()
   │
   └── conhece Circulo
```

Mas e se recebermos um:

```text
Retangulo
```

ou:

```text
Triangulo
```

ou qualquer outra implementação de `Forma`?

Poderíamos acabar criando uma sequência de decisões:

```text
if é Círculo:
    ...
elif é Retângulo:
    ...
elif é Triângulo:
    ...
else:
    ...
```

Esse tipo de solução aumenta o acoplamento entre o código cliente e as classes concretas.

---

# 💡 5. A ideia do Prototype

Se o problema é que o código externo não consegue copiar corretamente o objeto, podemos **delegar a responsabilidade da cópia para o próprio objeto**.

Em vez de:

```text
Cliente
   │
   ├── conhece como copiar Círculo
   ├── conhece como copiar Retângulo
   └── conhece como copiar outras formas
```

passamos para:

```text
Cliente
   │
   │ clone()
   ▼
Forma
   │
   ├── Círculo → sabe clonar a si mesmo
   ├── Retângulo → sabe clonar a si mesmo
   └── outra Forma → sabe clonar a si mesma
```

A chamada passa a ser simples:

```python
copia = original.clone()
```

O objeto conhece seu próprio estado interno e é responsável por produzir sua cópia.

---

# 🧬 6. O objeto se copia

Essa é uma das ideias mais importantes do Prototype.

Em vez de o cliente dizer:

```text
"Crie um Círculo e copie estes campos."
```

o cliente diz:

```text
"Clone este objeto."
```

Conceitualmente:

```text
original
   │
   │ clone()
   ▼
cópia
```

O objeto que suporta clonagem é chamado de **protótipo**.

---

# 👨‍💻 7. Exemplo-problema: formas geométricas

O exemplo apresentado nas aulas utiliza uma hierarquia de **formas geométricas**.

Podemos imaginar uma estrutura como:

```text
                 Forma
                   │
          ┌────────┴────────┐
          │                 │
       Círculo           Retângulo
```

A classe `Forma` representa uma abstração comum.

Cada forma pode possuir informações como:

```text
posição
cor
dimensões
configurações internas
estado específico
```

O problema surge quando queremos duplicar formas sem precisar conhecer qual é a classe concreta de cada objeto.

---

# 🔴 8. O problema de copiar uma Forma

Imagine que temos:

```python
original = Forma()
```

e queremos:

```text
uma cópia exata do objeto
```

Uma primeira tentativa seria criar outra forma e copiar seus atributos:

```python
copia = Forma()
copia.x = original.x
copia.y = original.y
copia.cor = original.cor
```

O problema é que isso pressupõe que:

1. sabemos todos os atributos;
2. conseguimos acessar esses atributos;
3. sabemos como cada atributo deve ser copiado;
4. sabemos qual classe concreta deve ser criada;
5. sabemos como copiar os objetos internos.

Isso pode funcionar para objetos simples, mas se torna cada vez mais complicado conforme a classe cresce.

---

# 🔐 9. Campos internos e estado privado

O exemplo da aula mostra justamente esse problema.

Um `Circulo` pode possuir:

```python
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        self.__cache_area = 3.14159 * raio ** 2
        self.__id_render = _proximo_id()
```

Observe que nem todas as informações são necessariamente públicas.

Podemos representar:

```text
Circulo
│
├── raio
│
├── __cache_area
│
└── __id_render
```

O código externo não deveria precisar conhecer todos esses detalhes internos para conseguir duplicar o objeto.

Essa é uma das motivações para colocar a operação de clonagem dentro do próprio objeto.

---

# 🧩 10. A solução: `clone()`

Com Prototype, podemos definir uma operação de clonagem:

```python
copia = original.clone()
```

Agora:

```text
Cliente
   │
   │ clone()
   ▼
Protótipo
   │
   ▼
Nova cópia
```

A responsabilidade pela cópia deixa de estar no cliente e passa para o objeto que conhece sua própria estrutura.

---

# 🔄 11. O cliente não precisa conhecer a classe concreta

Esse é outro ponto fundamental.

Imagine uma lista contendo diferentes formas:

```text
formas
│
├── Círculo
├── Retângulo
├── Círculo
├── Retângulo
└── outra Forma
```

O cliente pode trabalhar apenas com a abstração:

```python
def duplicar_todas(formas: list[Forma]) -> list[Forma]:
    return [f.clone() for f in formas]
```

A ideia é:

```text
                    Forma
                      │
                ┌─────┴─────┐
                │            │
             Círculo      Retângulo
                │            │
              clone()      clone()
                │            │
                └─────┬──────┘
                      ▼
                 novas cópias
```

O cliente não precisa fazer:

```text
if Círculo
    ...
elif Retângulo
    ...
```

Ele simplesmente chama:

```text
clone()
```

em cada objeto.

---

# 🏗️ 12. O que é o protótipo?

O **protótipo** é o objeto existente que será utilizado como base para criar uma nova instância.

Podemos representar:

```text
       PROTÓTIPO
           │
        clone()
           │
      ┌────┴────┐
      ▼         ▼
   Cópia 1   Cópia 2
```

Por exemplo:

```text
Círculo original
       │
       │ clone()
       ▼
Novo Círculo
```

O objeto original não precisa desaparecer nem ser modificado.

A operação cria uma nova instância.

---

# 🧱 13. Estrutura do Prototype

O GoF apresenta três participantes principais:

1. **Prototype**
2. **ConcretePrototype**
3. **Client**

---

## 13.1. Prototype

O `Prototype` declara a operação de clonagem.

Geralmente:

```text
clone()
```

Ele define o contrato que permite ao cliente solicitar uma cópia.

Conceitualmente:

```text
Prototype
│
└── clone()
```

---

## 13.2. ConcretePrototype

O `ConcretePrototype` implementa a operação de clonagem.

Por exemplo:

```text
ConcretePrototype
       │
       └── clone()
```

Uma classe concreta sabe como copiar seu próprio estado.

No nosso exemplo:

```text
Forma
 │
 ├── Círculo
 │      └── clone()
 │
 └── Retângulo
        └── clone()
```

---

## 13.3. Client

O `Client` utiliza o protótipo para criar novos objetos.

O cliente não precisa conhecer os detalhes da implementação da clonagem.

Conceitualmente:

```text
Client
  │
  │ clone()
  ▼
Prototype
```

Isso permite trabalhar com diferentes tipos concretos através da mesma interface.

---

# 📐 14. Estrutura conceitual

Podemos representar o padrão da seguinte maneira:

```text
┌───────────────┐
│     Client    │
└───────┬───────┘
        │
        │ clone()
        ▼
┌─────────────────────┐
│ «interface»         │
│      Prototype      │
├─────────────────────┤
│ + clone(): Prototype│
└──────────┬──────────┘
           ▲
           │
     ┌─────┴──────────────┐
     │                    │
┌────┴────────┐     ┌─────┴────────┐
│   Circulo   │     │  Retangulo    │
├─────────────┤     ├───────────────┤
│ estado      │     │ estado        │
├─────────────┤     ├───────────────┤
│ + clone()   │     │ + clone()     │
└─────────────┘     └───────────────┘
```

A ideia principal é:

```text
Client
  │
  │ não precisa saber
  │ qual é a classe concreta
  ▼
Prototype
  │
  │ clone()
  ▼
ConcretePrototype
```

---

# 🔍 15. Por que o objeto deve clonar a si mesmo?

A principal vantagem é o **encapsulamento da lógica de cópia**.

Considere:

```text
Forma
│
├── posição
├── cor
├── estado interno
├── configurações
└── outros dados
```

Se o cliente fizer a cópia:

```text
Cliente
   │
   ├── copia posição
   ├── copia cor
   ├── copia estado
   ├── copia configurações
   └── ...
```

o cliente precisa conhecer detalhes da implementação.

Com Prototype:

```text
Cliente
   │
   │ clone()
   ▼
Forma
   │
   ├── conhece seus campos
   ├── conhece seu estado
   └── conhece como se copiar
```

Assim, a lógica relacionada à cópia permanece dentro do objeto.

---

# ⚠️ 16. O problema de usar `if`, `elif`, `else`

Sem Prototype, uma implementação poderia acabar seguindo uma lógica semelhante a:

```text
se for Círculo:
    crie um Círculo
    copie os dados

senão se for Retângulo:
    crie um Retângulo
    copie os dados

senão:
    trate outro tipo
```

Conceitualmente:

```text
             duplicar()
                  │
          ┌───────┼────────┐
          ▼       ▼        ▼
       Círculo Retângulo  Outro
```

Quanto mais tipos forem adicionados, mais decisões podem aparecer.

Com Prototype:

```text
             duplicar()
                  │
                  │ clone()
                  ▼
              Prototype
             /         \
        Círculo      Retângulo
          clone()       clone()
```

O cliente não precisa conhecer cada classe concreta.

---

# 🚀 17. Duplicando várias formas

Uma das consequências interessantes é poder trabalhar com uma coleção heterogênea de objetos.

Por exemplo:

```text
formas
│
├── Círculo
├── Retângulo
├── Círculo
└── Retângulo
```

Podemos pensar no processo:

```text
para cada forma:

    forma.clone()
```

O resultado:

```text
formas originais
│
├── Círculo ──────► Círculo cópia
├── Retângulo ────► Retângulo cópia
├── Círculo ──────► Círculo cópia
└── Retângulo ────► Retângulo cópia
```

A operação é polimórfica: cada objeto sabe qual tipo de cópia precisa produzir.

---

# 💰 18. Quando clonar pode ser mais barato?

Uma das situações citadas na definição do Prototype é quando **clonar pode ser mais barato do que construir novamente**.

Imagine um objeto cujo estado resulta de operações custosas.

Por exemplo:

```text
Matrizes
   │
   ├── cálculos
   ├── transformações
   ├── operações matemáticas
   └── resultado pronto
```

Se já temos um objeto com o resultado calculado:

```text
Objeto pronto
     │
     │ clone()
     ▼
Cópia pronta
```

podemos aproveitar o estado já construído.

Em vez de:

```text
recalcular
   ↓
construir
   ↓
configurar
```

podemos:

```text
objeto existente
       ↓
     clone()
       ↓
nova cópia
```

Isso não significa que clonar será sempre mais rápido. A vantagem depende do custo real da construção e da complexidade do objeto.

---

# 🆚 19. Prototype comparado com outros padrões criacionais

O Prototype faz parte dos **padrões criacionais**, assim como:

- Factory Method;
- Abstract Factory;
- Builder;
- Singleton.

Uma maneira simples de diferenciar as ideias é observar **de onde o novo objeto é criado**.

| Padrão | Cria objeto a partir de |
|---|---|
| Factory Method | Uma classe/fábrica através de um método |
| Abstract Factory | Uma família de objetos relacionados |
| Builder | Etapas de construção |
| **Prototype** | **Outro objeto existente** |
| Singleton | Uma única instância controlada |

A comparação apresentada na aula pode ser resumida assim:

```text
Factory Method / Abstract Factory → uma classe/fábrica
Builder                         → etapas
Prototype                       → outro objeto
```

---

# 🔄 20. Prototype x Factory Method

No **Factory Method**, normalmente temos um método responsável por decidir ou delegar a criação de uma nova instância.

A ideia geral é:

```text
Cliente
   │
   │ solicita criação
   ▼
Factory Method
   │
   ▼
Novo objeto
```

No Prototype:

```text
Cliente
   │
   │ clone()
   ▼
Objeto existente
   │
   ▼
Cópia
```

A diferença central é a origem da nova instância:

```text
Factory Method
    → criação a partir de uma classe/fábrica

Prototype
    → criação a partir de um objeto existente
```

---

# 🧱 21. Prototype x Builder

O **Builder** concentra-se no processo de construção.

Podemos imaginar:

```text
Builder
   │
   ├── etapa 1
   ├── etapa 2
   ├── etapa 3
   └── etapa 4
          │
          ▼
      objeto pronto
```

Já o Prototype parte de algo que já existe:

```text
Objeto pronto
     │
     │ clone()
     ▼
Outro objeto
```

Assim:

```text
Builder
→ construir passo a passo

Prototype
→ copiar um objeto existente
```

---

# 🏭 22. Prototype x Abstract Factory

O **Abstract Factory** trabalha com famílias de produtos relacionados.

Por exemplo:

```text
Fábrica Dark
   ├── Botão Dark
   └── Janela Dark

Fábrica Light
   ├── Botão Light
   └── Janela Light
```

No Prototype, temos um objeto existente servindo como modelo:

```text
Protótipo
   │
   ├── clone() → objeto 1
   ├── clone() → objeto 2
   └── clone() → objeto 3
```

Portanto:

```text
Abstract Factory
→ cria objetos relacionados através de uma fábrica

Prototype
→ cria objetos através da cópia de uma instância existente
```

---

# 📋 23. Shallow Copy e Deep Copy

Ao estudar Prototype, é importante compreender que **copiar um objeto não significa necessariamente duplicar profundamente toda a estrutura interna dele**.

Existem, de maneira geral, dois conceitos importantes:

```text
Shallow Copy
Deep Copy
```

---

## 🟡 23.1. Shallow Copy

Uma **cópia superficial** copia o objeto, mas objetos internos referenciados podem continuar sendo compartilhados.

Conceitualmente:

```text
Original
   │
   ├── dados
   │
   └── objeto interno ─────┐
                           │
                           ▼
                         memória
                           ▲
                           │
   ┌── objeto interno ────┘
   │
Cópia
```

Isso significa que devemos ter cuidado com atributos mutáveis.

Em Python, uma ferramenta relacionada a esse conceito é:

```python
copy.copy()
```

---

## 🟢 23.2. Deep Copy

Uma **cópia profunda** procura duplicar também os objetos internos.

Conceitualmente:

```text
Original
   │
   └── objeto interno A

Cópia
   │
   └── objeto interno B
```

Agora os objetos internos também possuem cópias independentes.

Em Python:

```python
copy.deepcopy()
```

---

# ⚠️ 24. O Prototype não significa simplesmente chamar `copy.deepcopy()`

É importante não reduzir o padrão à função:

```python
copy.deepcopy()
```

O **Prototype é um padrão de projeto**, isto é, uma decisão de arquitetura sobre **como a criação de objetos será organizada**.

O ponto central é:

```text
O objeto fornece uma operação de clonagem.
```

A forma como essa clonagem é implementada pode variar.

Pode envolver:

```text
copy.copy()
copy.deepcopy()
construtor de cópia
atributos específicos
lógica própria
```

dependendo do domínio e do estado do objeto.

---

# 🗂️ 25. Registro de protótipos

Uma aplicação pode possuir vários protótipos previamente configurados.

Por exemplo:

```text
Registro de Protótipos
│
├── círculo vermelho
├── círculo azul
├── retângulo vermelho
└── retângulo azul
```

O cliente poderia solicitar um protótipo pelo nome:

```text
"círculo azul"
```

e então cloná-lo:

```text
Registro
   │
   │ busca "círculo azul"
   ▼
Protótipo
   │
   │ clone()
   ▼
Nova forma
```

Esse tipo de estrutura é conhecido como **Prototype Registry**.

Ela pode ser útil quando existem muitos objetos-modelo pré-configurados.

---

# 🧩 26. Exemplo do fluxo que será estudado

O exemplo deste estudo será baseado na hierarquia de formas apresentada na aula.

Teremos uma abstração semelhante a:

```text
Forma
│
├── posição
├── cor
└── clone()
```

E implementações concretas:

```text
Forma
│
├── Círculo
│
└── Retângulo
```

Cada implementação deverá saber como criar uma cópia de si mesma.

O fluxo será:

```text
1. Criar uma forma
        │
        ▼
2. Configurar seu estado
        │
        ▼
3. Guardar a forma como protótipo
        │
        ▼
4. Chamar clone()
        │
        ▼
5. Obter uma nova forma
        │
        ▼
6. Trabalhar com a cópia
```

---

# 🧪 27. Exemplo conceitual

Imagine:

```text
Círculo original
│
├── posição = (10, 20)
├── cor = vermelho
├── raio = 50
└── estado interno
```

Depois:

```text
original.clone()
```

produz:

```text
Novo Círculo
│
├── posição = (10, 20)
├── cor = vermelho
├── raio = 50
└── estado interno copiado
```

Depois da clonagem, podemos alterar a cópia sem alterar o objeto original, desde que a estratégia de cópia utilizada produza a independência necessária entre os estados.

Por exemplo:

```text
Original
cor = vermelho

        clone()

Cópia
cor = vermelho
```

Depois:

```text
Original
cor = vermelho

Cópia
cor = azul
```

O objetivo é que:

```text
Original ≠ Cópia
```

em identidade, mesmo que inicialmente possuam estados equivalentes.

---

# 🧠 28. Identidade x estado

Esse detalhe é muito importante.

Quando clonamos:

```text
original.clone()
```

não queremos simplesmente outra referência para o mesmo objeto.

Queremos uma nova instância.

Conceitualmente:

```text
Original ───────► Objeto A
Cópia   ───────► Objeto B
```

e não:

```text
Original ───────┐
                ├──► Objeto A
Cópia   ────────┘
```

Portanto:

```text
Original
   ≠
Cópia
```

em identidade.

Porém, inicialmente:

```text
estado(original)
      ≈
estado(cópia)
```

dependendo da estratégia de clonagem.

---

# 🔐 29. Encapsulamento

O Prototype também está relacionado ao princípio de **encapsulamento**.

O cliente não precisa conhecer:

```text
como o objeto foi construído;
quais atributos internos existem;
como os atributos devem ser copiados;
quais subclasses existem;
quais detalhes internos precisam ser preservados.
```

Ele apenas utiliza:

```text
clone()
```

Podemos visualizar:

```text
                  Cliente
                     │
                     │ clone()
                     ▼
              ┌──────────────┐
              │  Protótipo   │
              │              │
              │ sabe como    │
              │ se copiar    │
              └──────────────┘
```

---

# 🔌 30. Polimorfismo

O exemplo das formas também demonstra o uso de **polimorfismo**.

O cliente pode trabalhar com:

```text
Forma
```

sem precisar saber se o objeto concreto é:

```text
Círculo
Retângulo
```

ou outra implementação.

A chamada:

```python
forma.clone()
```

será resolvida de acordo com o objeto concreto.

Assim:

```text
Forma
  │
  ├── Círculo
  │      └── clone()
  │
  └── Retângulo
         └── clone()
```

O mesmo contrato:

```text
clone()
```

pode produzir cópias de diferentes tipos.

---

# 📐 31. Estrutura do exemplo-problema

A estrutura conceitual do nosso exemplo pode ser representada assim:

```text
                  ┌───────────────┐
                  │     Forma     │
                  ├───────────────┤
                  │ + clone()     │
                  └───────┬───────┘
                          │
                ┌─────────┴─────────┐
                │                   │
        ┌───────▼───────┐   ┌───────▼────────┐
        │    Círculo    │   │   Retângulo    │
        ├───────────────┤   ├────────────────┤
        │ raio          │   │ largura        │
        │ estado interno│   │ altura         │
        ├───────────────┤   ├────────────────┤
        │ + clone()     │   │ + clone()      │
        └───────────────┘   └────────────────┘
```

O cliente trabalha com:

```text
Forma
```

e não precisa decidir:

```text
"Círculo ou Retângulo?"
```

A própria instância sabe como realizar a clonagem.

---

# 🔁 32. Fluxo completo

O fluxo do Prototype pode ser entendido em quatro etapas:

```text
┌────────────────────────────┐
│ 1. Existe um objeto pronto │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 2. O objeto suporta clone()│
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 3. Cliente chama clone()   │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│ 4. Nova instância é criada │
└────────────────────────────┘
```

Ou, de maneira mais curta:

```text
Objeto existente
      ↓
   clone()
      ↓
Nova instância
```

---

# 🆚 33. Criação tradicional x Prototype

## Criação tradicional

```text
Classe
  │
  ▼
Construtor
  │
  ▼
Configuração
  │
  ▼
Objeto
```

Para vários objetos:

```text
Classe → Objeto 1
Classe → Objeto 2
Classe → Objeto 3
Classe → Objeto 4
```

---

## Prototype

```text
Objeto configurado
       │
       ├── clone() → Objeto 1
       ├── clone() → Objeto 2
       ├── clone() → Objeto 3
       └── clone() → Objeto 4
```

A diferença fundamental é:

```text
Criação tradicional
→ começa na classe

Prototype
→ começa em uma instância existente
```

---

# 🧠 34. Quando utilizar Prototype?

O Prototype pode ser interessante quando:

### 1. A criação do objeto é complexa

Por exemplo:

```text
muitos atributos
muitas configurações
objetos internos
processamentos
```

---

### 2. Existem muitos objetos semelhantes

Por exemplo:

```text
protótipo
   │
   ├── clone
   ├── clone
   ├── clone
   └── clone
```

---

### 3. Queremos evitar reconstrução repetitiva

Em vez de:

```text
criar
configurar
configurar
configurar
```

podemos:

```text
clonar
```

e modificar somente o que for diferente.

---

### 4. O código cliente não deve conhecer as classes concretas

O cliente pode trabalhar através de:

```text
Prototype
```

e chamar:

```text
clone()
```

---

### 5. A construção é custosa

Quando a criação envolve operações caras, pode ser interessante aproveitar o estado de um objeto já pronto.

---

# ⚠️ 35. Quando tomar cuidado?

O Prototype não é automaticamente a melhor solução.

É importante analisar a estrutura do objeto.

Se o objeto possui referências internas, precisamos decidir cuidadosamente como elas serão copiadas.

Por exemplo:

```text
Objeto
│
├── atributo simples
├── atributo simples
└── objeto interno
```

A pergunta passa a ser:

```text
O objeto interno deve ser compartilhado?
```

ou:

```text
O objeto interno também deve ser clonado?
```

Essa decisão faz parte da implementação correta do protótipo.

---

# 🟡 36. Vantagens

Entre as principais vantagens estão:

### ✅ Redução da dependência de classes concretas

O cliente pode trabalhar com o contrato:

```text
clone()
```

---

### ✅ Encapsulamento da lógica de cópia

O próprio objeto conhece sua estrutura.

---

### ✅ Reutilização de objetos configurados

Podemos manter protótipos prontos:

```text
Protótipo A
Protótipo B
Protótipo C
```

e gerar cópias conforme necessário.

---

### ✅ Evita reconstrução repetitiva

Em determinados cenários, copiar um objeto pronto pode ser mais simples ou barato do que construí-lo novamente.

---

### ✅ Facilita a criação de variações

Podemos:

```text
clonar
   ↓
alterar alguns atributos
   ↓
obter uma nova configuração
```

---

# 🔴 37. Desvantagens e dificuldades

Também existem desafios.

### ❌ Clonar objetos complexos pode ser difícil

Principalmente quando existem:

```text
referências
objetos internos
coleções
recursos externos
estado compartilhado
```

---

### ❌ Deep copy pode ser complexo

Nem sempre podemos simplesmente duplicar tudo.

Alguns objetos podem representar:

```text
conexões
arquivos
recursos externos
identificadores únicos
objetos que não devem ser compartilhados
```

---

### ❌ Pode haver problemas com estado interno

É necessário entender quais partes devem ser:

```text
copiadas
```

e quais devem ser:

```text
compartilhadas
```

---

# 🧬 38. Prototype e identificadores internos

O exemplo apresentado na aula mostra outro ponto interessante:

```text
__id_render = _proximo_id()
```

Imagine que o objeto original possua:

```text
id = 10
```

Se ele for clonado, precisamos pensar:

```text
A cópia deve continuar com id = 10?
```

ou:

```text
A cópia deve receber um novo id?
```

A resposta depende do significado daquele campo.

Isso mostra que implementar Prototype não significa apenas copiar mecanicamente todos os atributos.

Precisamos compreender o **significado do estado** do objeto.

---

# 🧩 39. Prototype e responsabilidade da clonagem

Uma das principais ideias do padrão é colocar a responsabilidade no próprio objeto.

Sem Prototype:

```text
Cliente
│
├── conhece Círculo
├── conhece Retângulo
├── conhece seus atributos
└── sabe como copiá-los
```

Com Prototype:

```text
Cliente
│
└── chama clone()

Círculo
└── sabe clonar Círculo

Retângulo
└── sabe clonar Retângulo
```

Isso torna o cliente mais independente das classes concretas.

---

# 🧪 40. O que será observado na implementação

Na implementação prática deste estudo, devemos observar principalmente:

```text
1. Qual é o Prototype?
2. Onde o método clone() é declarado?
3. Quais classes são ConcretePrototype?
4. Como cada classe realiza sua cópia?
5. Quem é o Client?
6. O cliente conhece as classes concretas?
7. O estado original permanece independente da cópia?
8. Existem atributos mutáveis?
9. Existe necessidade de cópia profunda?
```

Essas perguntas ajudam a identificar o padrão no código.

---

# 📚 41. Relação com SOLID

O Prototype não é um princípio SOLID, mas sua utilização pode contribuir para determinadas propriedades de um sistema.

Por exemplo, quando o cliente trabalha através de uma abstração:

```text
Prototype
   │
   └── clone()
```

em vez de conhecer diretamente:

```text
Círculo
Retângulo
Triângulo
...
```

podemos reduzir determinadas dependências de classes concretas.

Isso pode ajudar na organização do código e na separação de responsabilidades.

Porém, não devemos utilizar o Prototype simplesmente para "cumprir SOLID". O padrão deve ser utilizado quando o problema de criação por clonagem realmente existir.

---

# 🗃️ 42. Possível registro de protótipos

Em aplicações maiores, podemos ter algo semelhante a:

```text
┌───────────────────────────┐
│   Prototype Registry      │
├───────────────────────────┤
│ círculo_vermelho          │
│ círculo_azul              │
│ retângulo_vermelho        │
│ retângulo_azul            │
└─────────────┬─────────────┘
              │
              │ buscar
              ▼
          Protótipo
              │
              │ clone()
              ▼
          Nova forma
```

O registro funciona como uma coleção de modelos prontos.

Essa técnica é útil quando o sistema possui muitos protótipos pré-configurados.

---

# 🧭 43. Como reconhecer Prototype em um código?

Ao analisar um código, procure por sinais como:

```text
clone()
copy()
duplicar()
copiar()
```

e por estruturas em que:

```text
objeto existente
      ↓
cópia
```

é utilizado para criar novas instâncias.

Também é comum encontrar:

```text
Prototype
ConcretePrototype
Client
```

ou equivalentes com outros nomes.

---

# 🔎 44. Checklist para identificar o padrão

Pergunte:

```text
☐ Existe um objeto já criado que serve de modelo?

☐ Existe uma operação de clonagem?

☐ O próprio objeto sabe como se copiar?

☐ O cliente consegue clonar sem conhecer a classe concreta?

☐ Existem vários tipos concretos que implementam a mesma operação?

☐ A criação por cópia evita reconstrução repetitiva?
```

Quanto mais respostas forem "sim", maior a relação do código com a ideia do Prototype.

---

# 🧱 45. Estrutura que será utilizada neste estudo

A implementação deverá seguir a ideia apresentada nas aulas:

```text
Prototype
│
├── Forma
│
├── Círculo
│
├── Retângulo
│
└── Cliente
```

A organização exata dos arquivos poderá ser definida na etapa de implementação.

Neste momento, o objetivo é compreender o papel de cada participante:

```text
Forma
  ↓
define clone()

Círculo
  ↓
implementa clone()

Retângulo
  ↓
implementa clone()

Cliente
  ↓
solicita clone()
```

---

# 📖 46. Resumo conceitual

Podemos resumir o Prototype em uma sequência:

```text
                 PROBLEMA
                    │
                    ▼
      Criar cópias manualmente é difícil
                    │
                    ▼
       Cliente precisa conhecer detalhes
                    │
                    ▼
                  SOLUÇÃO
                    │
                    ▼
       O objeto sabe clonar a si mesmo
                    │
                    ▼
                 clone()
                    │
                    ▼
             nova instância
```

Ou simplesmente:

```text
Objeto existente
       │
       │ clone()
       ▼
Nova instância
```

---

# 🎯 47. Resumo para memorizar

> **Prototype cria novos objetos a partir da clonagem de objetos existentes.**

As ideias principais são:

```text
Prototype
│
├── objeto existente serve como modelo
│
├── clone() cria uma nova instância
│
├── o objeto conhece sua própria estrutura
│
├── o cliente não precisa conhecer a classe concreta
│
└── pode evitar construções repetitivas ou custosas
```

No exemplo das formas:

```text
Forma
│
├── Círculo
│      └── clone()
│
└── Retângulo
       └── clone()
```

O cliente pode fazer:

```text
forma.clone()
```

sem precisar decidir:

```text
if Círculo
elif Retângulo
else
```

Essa é a essência do padrão.

---

# 🧪 48. Exemplo final do problema

Antes do Prototype, podemos ter algo conceitualmente semelhante a:

```text
duplicar(forma)

    se for Círculo:
        criar Círculo
        copiar atributos

    senão se for Retângulo:
        criar Retângulo
        copiar atributos

    senão:
        tratar outro tipo
```

Com Prototype:

```text
duplicar(forma)

    return forma.clone()
```

E então:

```text
                 forma
                   │
                   │ clone()
                   ▼
             nova instância
```

Cada classe concreta fica responsável por saber como produzir sua própria cópia.

---

# 🚀 49. Próxima etapa

Depois deste README, a próxima etapa será implementar o exemplo de formas geométricas apresentado na aula.

A implementação deverá permitir estudar, na prática:

```text
Forma
  │
  ├── Círculo
  └── Retângulo
```

e observar:

```text
             Cliente
                │
                │ clone()
                ▼
             Prototype
             /       \
            /         \
       Círculo      Retângulo
          │             │
       clone()        clone()
          │             │
          ▼             ▼
       Cópia          Cópia
```

O foco será entender **por que a clonagem deve ser responsabilidade do próprio objeto** e como isso permite que o cliente trabalhe sem depender diretamente das classes concretas.

---

# 📚 50. Referências

## 📘 GoF — Design Patterns

GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Design Patterns: Elements of Reusable Object-Oriented Software**. Addison-Wesley, 1994.

O Prototype faz parte dos padrões **criacionais** apresentados pelo GoF.

---

## 🌐 Refactoring Guru

**Prototype — Refactoring Guru.**

https://refactoring.guru/pt-br/design-patterns/prototype

A referência apresenta o problema, a ideia, a estrutura e os exemplos relacionados ao padrão Prototype.

---

## 🐍 Documentação oficial do Python — `copy`

**The Python Standard Library — `copy`: Shallow and deep copy operations.**

https://docs.python.org/3/library/copy.html

A documentação é útil para compreender as operações de cópia superficial e profunda utilizadas na linguagem Python.

---

# 📝 51. Observação sobre este estudo

Este README tem como objetivo servir como material de estudo antes da implementação.

A intenção não é apenas memorizar que:

```text
Prototype = clone()
```

mas compreender **por que o padrão existe**.

O raciocínio principal é:

```text
Tenho um objeto complexo
        │
        ▼
Preciso de outro parecido
        │
        ▼
Não quero reconstruí-lo manualmente
        │
        ▼
Não quero que o cliente conheça seus detalhes internos
        │
        ▼
Delego a clonagem ao próprio objeto
        │
        ▼
              clone()
        │
        ▼
Nova instância
```

Assim, o Prototype pode ser entendido como uma forma de **delegar ao próprio objeto a responsabilidade de criar uma cópia de si mesmo**, reduzindo a necessidade de o código cliente conhecer detalhes da construção e da classe concreta.

---

# 🧠 52. Mapa mental

```text
                         PROTOTYPE
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
          Criacional      clone()        Objeto existente
                             │
                             ▼
                       Nova instância
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
          Encapsulamento             Polimorfismo
                │                         │
                ▼                         ▼
       objeto sabe copiar        cliente usa Prototype
                                          │
                                          ▼
                                  não conhece concreto
```

---

# ✅ 53. Conclusão

O **Prototype** resolve um problema específico de criação:

> **Como criar novos objetos a partir de objetos existentes sem obrigar o cliente a conhecer todos os detalhes necessários para reconstruí-los?**

A resposta do padrão é:

```text
Deixe o próprio objeto fornecer uma operação de clonagem.
```

Assim:

```text
             objeto existente
                    │
                    │ clone()
                    ▼
              nova instância
```

No exemplo das formas geométricas:

```text
              Forma
                │
        ┌───────┴───────┐
        │               │
     Círculo         Retângulo
        │               │
     clone()          clone()
        │               │
        ▼               ▼
      cópia             cópia
```

O cliente pode trabalhar com:

```text
Forma
```

sem precisar conhecer antecipadamente se está lidando com:

```text
Círculo
Retângulo
```

ou outra implementação de `Forma`.

Essa é a principal ideia que deverá ser observada na implementação:

```text
                    PROTOTYPE
                        │
                        ▼
              "Copie a si mesmo."
                        │
                        ▼
                     clone()
                        │
                        ▼
                 nova instância
```
