# Bridge

## 📌 Objetivo

O **Bridge** é um Design Pattern estrutural utilizado para **separar uma abstração da sua implementação**, permitindo que ambas possam evoluir e variar de maneira independente.

O principal objetivo é evitar que duas dimensões diferentes de um sistema fiquem fortemente acopladas através de herança.

Uma forma simples de entender o Bridge é:

> Em vez de criar várias subclasses combinando diferentes características, separamos essas características em duas hierarquias independentes e fazemos uma referência entre elas.

---

## ❗ Problema

Imagine que estamos desenvolvendo um sistema gráfico que trabalha com **formas geométricas e cores**.

Temos duas dimensões diferentes:

### Formas

```text
Shape
├── Circle
└── Square
```

### Cores

```text
Color
├── Red
├── Blue
└── Green
```

À primeira vista, parece simples.

Porém, queremos permitir que qualquer forma possa utilizar qualquer cor.

Então precisamos representar combinações como:

```text
Circle + Red
Circle + Blue
Circle + Green

Square + Red
Square + Blue
Square + Green
```

---

## 🔴 O problema com herança

Uma solução inicial seria criar uma classe para cada combinação:

```text
CircleRed
CircleBlue
CircleGreen

SquareRed
SquareBlue
SquareGreen
```

Temos apenas:

- 2 formas;
- 3 cores.

Isso já resulta em:

```text
2 × 3 = 6 classes
```

Agora imagine que o sistema cresça.

Adicionamos:

```text
Triangle
Rectangle
Pentagon
```

e mais cores:

```text
Yellow
Purple
Black
White
```

A quantidade de combinações cresce rapidamente.

Teríamos que criar várias classes:

```text
CircleRed
CircleBlue
CircleGreen
CircleYellow
CirclePurple
...

SquareRed
SquareBlue
SquareGreen
SquareYellow
SquarePurple
...

TriangleRed
TriangleBlue
TriangleGreen
...
```

Esse problema é conhecido como **explosão de subclasses**.

---

## 💥 Explosão de subclasses

O problema acontece porque estamos tentando representar **duas dimensões independentes através de uma única hierarquia de herança**.

Se temos:

```text
N formas
M cores
```

podemos acabar precisando de aproximadamente:

```text
N × M
```

classes para representar todas as combinações.

Quanto mais dimensões adicionamos, maior fica a quantidade de classes.

Além disso, cada nova forma ou cor pode exigir a criação de várias classes novas.

Isso torna o sistema:

- mais difícil de manter;
- mais difícil de entender;
- mais difícil de expandir;
- mais acoplado;
- mais propenso a duplicação de código.

---

## 💡 Solução

O Bridge resolve esse problema separando as duas dimensões.

Em vez de criar uma única hierarquia contendo todas as combinações, criamos **duas hierarquias independentes**:

```text
Abstração
   |
   ├── Circle
   └── Square


Implementação
   |
   ├── Red
   ├── Blue
   └── Green
```

A `Shape` possui uma referência para um objeto `Color`.

Assim:

```text
Shape
  |
  | possui
  v
Color
```

Uma forma não precisa saber como uma cor funciona internamente.

Ela apenas utiliza a interface fornecida pela implementação de `Color`.

---

## 🌉 Por que o nome "Bridge"?

O nome **Bridge** (Ponte) vem justamente da ideia de criar uma ponte entre duas hierarquias independentes.

Podemos visualizar:

```text
        ABSTRAÇÃO
            |
      +-----+-----+
      |           |
   Circle       Square
      |           |
      +-----+-----+
            |
          Bridge
            |
      +-----+-----+
      |     |     |
     Red   Blue  Green
      IMPLEMENTAÇÃO
```

A abstração utiliza a implementação através dessa "ponte".

---

## 🧩 Estrutura conceitual

O padrão possui dois lados principais.

### Abstração

Representa o conceito que o cliente deseja utilizar.

Neste exemplo:

```text
Shape
├── Circle
└── Square
```

### Implementação

Representa uma dimensão que pode variar independentemente da abstração.

Neste exemplo:

```text
Color
├── Red
├── Blue
└── Green
```

A abstração mantém uma referência para a implementação:

```text
Shape
   |
   v
Color
```

---

## 🏗️ Exemplo conceitual

Podemos imaginar a interface `Color`:

```python
from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def apply(self):
        raise NotImplementedError
```

Agora temos diferentes implementações:

```python
class Red(Color):

    def apply(self):
        return "vermelho"


class Blue(Color):

    def apply(self):
        return "azul"


class Green(Color):

    def apply(self):
        return "verde"
```

Temos então a primeira dimensão:

```text
Color
├── Red
├── Blue
└── Green
```

---

## 🔷 Abstração `Shape`

A `Shape` recebe uma implementação de `Color`:

```python
class Shape(ABC):

    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def draw(self):
        raise NotImplementedError
```

Agora podemos criar diferentes formas:

```python
class Circle(Shape):

    def draw(self):
        print(f"Círculo {self.color.apply()}")


class Square(Shape):

    def draw(self):
        print(f"Quadrado {self.color.apply()}")
```

Temos a segunda dimensão:

```text
Shape
├── Circle
└── Square
```

---

## 🔗 A conexão entre as duas dimensões

Agora podemos combinar qualquer forma com qualquer cor sem criar uma classe específica para cada combinação.

Por exemplo:

```python
circle = Circle(Red())
circle.draw()
```

Resultado:

```text
Círculo vermelho
```

Podemos trocar a cor:

```python
circle = Circle(Blue())
circle.draw()
```

Resultado:

```text
Círculo azul
```

Ou podemos trocar a forma:

```python
square = Square(Green())
square.draw()
```

Resultado:

```text
Quadrado verde
```

Não precisamos criar:

```text
CircleRed
CircleBlue
SquareGreen
```

As duas dimensões são combinadas através de composição.

---

## 🔄 Visualizando o funcionamento

Uma chamada como:

```python
Circle(Blue()).draw()
```

pode ser entendida como:

```text
             Circle
                |
                | possui
                v
              Blue
                |
                | fornece
                v
           implementação
```

A forma sabe que possui uma cor, mas não precisa conhecer os detalhes de como aquela cor funciona.

Da mesma maneira, a cor não precisa saber quais formas existem.

Isso permite que as duas hierarquias evoluam independentemente.

---

## 📈 Vantagem principal

Sem Bridge:

```text
2 formas × 3 cores = 6 classes
```

Com Bridge:

```text
2 classes de forma + 3 classes de cor
```

Se adicionarmos mais uma forma:

```text
Triangle
```

não precisamos criar:

```text
TriangleRed
TriangleBlue
TriangleGreen
```

Basta criar:

```python
class Triangle(Shape):
    ...
```

Da mesma maneira, se adicionarmos uma nova cor:

```text
Yellow
```

não precisamos criar:

```text
CircleYellow
SquareYellow
TriangleYellow
```

Basta criar:

```python
class Yellow(Color):
    ...
```

Essa independência é uma das principais vantagens do Bridge.

---

## 🧠 Participantes do Bridge

| Participante             | Exemplo                    | Responsabilidade                    |
| ------------------------ | -------------------------- | ----------------------------------- |
| **Abstraction**          | `Shape`                    | Define a abstração principal        |
| **Refined Abstraction**  | `Circle`, `Square`         | Especializa a abstração             |
| **Implementor**          | `Color`                    | Define a interface da implementação |
| **Concrete Implementor** | `Red`, `Blue`, `Green`     | Implementa a interface              |
| **Bridge**               | Referência `Shape → Color` | Conecta as duas hierarquias         |

---

## 🎯 Quando utilizar Bridge?

O Bridge é especialmente útil quando:

- existem duas ou mais dimensões independentes no sistema;
- essas dimensões podem sofrer alterações separadamente;
- utilizar herança criaria muitas subclasses;
- queremos reduzir o acoplamento entre uma abstração e sua implementação;
- queremos permitir que diferentes implementações sejam combinadas livremente;
- esperamos que tanto a abstração quanto a implementação evoluam ao longo do tempo.

---

## 🆚 Bridge × Herança

### Utilizando apenas herança

```text
Shape
│
├── CircleRed
├── CircleBlue
├── CircleGreen
├── SquareRed
├── SquareBlue
└── SquareGreen
```

As duas dimensões ficam misturadas na mesma hierarquia.

### Utilizando Bridge

```text
Shape
│
├── Circle
└── Square
     |
     | utiliza
     v
Color
│
├── Red
├── Blue
└── Green
```

As dimensões ficam separadas.

---

## 🔀 Bridge × Adapter

Embora os dois padrões sejam estruturais e possam utilizar composição, suas intenções são diferentes.

### Adapter

O Adapter geralmente é utilizado quando **já temos uma classe ou sistema existente que possui uma interface incompatível**.

Exemplo:

```text
Sistema espera:
    play()

Classe existente:
    play_mp4()
```

Criamos:

```text
VideoAdapter
```

para fazer as duas interfaces trabalharem juntas.

### Bridge

O Bridge normalmente é utilizado quando estamos **projetando a estrutura do sistema** e queremos separar duas dimensões que podem variar independentemente.

Exemplo:

```text
Shape
    +
Color
```

Em vez de:

```text
CircleRed
CircleBlue
CircleGreen
SquareRed
SquareBlue
SquareGreen
```

criamos duas hierarquias independentes:

```text
Shape ──────── Color
```

### 📝 Resumindo

> **Adapter:** "Preciso fazer duas interfaces existentes trabalharem juntas."

> **Bridge:** "Quero separar duas dimensões para que elas possam variar independentemente."

---

## 📌 Ideia principal para memorizar

O Bridge combate principalmente o problema de **explosão de subclasses causada pela combinação de diferentes dimensões de um sistema**.

A ideia central é:

```text
          Abstração
              |
              |
            Bridge
              |
              |
        Implementação
```

Ou, no exemplo:

```text
Shape
  |
  +---- Circle
  |
  +---- Square
          |
          |
       utiliza
          |
          v
        Color
          |
     +----+----+
     |    |    |
    Red  Blue Green
```

Portanto:

> **Bridge = separar uma abstração da sua implementação para que ambas possam variar independentemente.**
