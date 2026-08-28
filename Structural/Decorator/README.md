# Decorator

## 📌 Objetivo

O **Decorator** é um Design Pattern **estrutural** utilizado para **adicionar novas responsabilidades ou comportamentos a um objeto dinamicamente**.

Em vez de modificar diretamente a classe original ou criar diversas subclasses para representar todas as possíveis combinações de comportamentos, o Decorator permite **envolver um objeto com outros objetos** que adicionam funcionalidades antes ou depois da execução do comportamento original.

Uma forma simples de entender o Decorator é:

> Em vez de criar uma nova subclasse para cada combinação possível de comportamentos, envolvemos um objeto com outros objetos que adicionam responsabilidades.

Por exemplo:

```text
Imagem
```

pode se transformar em:

```text
Log(
    MarcaDagua(
        Imagem
    )
)
```

Ou:

```text
Contraste(
    Compressao(
        MarcaDagua(
            Imagem
        )
    )
)
```

Cada camada adiciona um novo comportamento ao objeto original.

---

# ❗ Problema

Imagine que estamos desenvolvendo um sistema responsável por exibir imagens de alta resolução.

Inicialmente, temos apenas uma classe:

```text
ImagemAltaResolucao
```

Essa classe possui uma operação responsável por exibir a imagem:

```text
exibir()
```

Podemos representar a situação inicial assim:

```text
ImagemAltaResolucao

        |

        |

        v

      exibir()
```

Tudo funciona corretamente.

Porém, depois de algum tempo, novos requisitos começam a surgir.

Agora algumas imagens precisam:

- receber uma marca d'água;
- ser comprimidas antes de serem exibidas;
- possuir um log de auditoria;
- receber ajuste de contraste antes da exibição.

O detalhe importante é que **nem todas as imagens receberão os mesmos tratamentos**.

O cliente deve poder escolher, **em tempo de execução**, quais comportamentos deseja aplicar.

Por exemplo:

```text
Imagem + Marca d'água + Log
```

Outra imagem pode utilizar:

```text
Imagem + Compressão + Contraste + Marca d'água
```

Outra pode utilizar:

```text
Imagem
```

sem nenhum comportamento adicional.

E outra pode utilizar:

```text
Imagem + todos os tratamentos
```

---

# 🔴 O problema com herança

Uma primeira tentativa poderia ser utilizar herança.

Poderíamos criar subclasses para cada novo comportamento.

Por exemplo:

```text
ImagemAltaResolucao

├── ImagemComMarcaDagua
│
├── ImagemComprimida
│
├── ImagemComLog
│
└── ImagemComContraste
```

Até aqui, parece uma solução simples.

Porém, rapidamente surge outro problema.

E se uma imagem precisar possuir mais de um comportamento?

Por exemplo:

```text
Imagem + Marca d'água + Log
```

Seria necessário criar:

```text
ImagemComMarcaDaguaELog
```

Se outra imagem precisar de:

```text
Imagem + Compressão + Contraste
```

teríamos:

```text
ImagemComprimidaComContraste
```

E para:

```text
Imagem + Compressão + Log + Marca d'água
```

teríamos:

```text
ImagemComprimidaComLogComMarcaDagua
```

A quantidade de subclasses começa a crescer rapidamente.

---

# 💥 Explosão de subclasses

O problema acontece porque estamos tentando representar **combinações de comportamentos através de herança**.

Imagine que possuímos os seguintes comportamentos opcionais:

```text
1. Marca d'água
2. Compressão
3. Contraste
4. Log
```

Cada comportamento pode estar:

```text
Aplicado
```

ou:

```text
Não aplicado
```

Portanto, para cada comportamento temos duas possibilidades.

Com quatro comportamentos opcionais, podemos ter:

```text
2⁴ = 16 combinações possíveis
```

Algumas dessas combinações seriam:

```text
Imagem

Imagem + MarcaDagua

Imagem + Compressao

Imagem + Contraste

Imagem + Log

Imagem + MarcaDagua + Log

Imagem + Compressao + Contraste

Imagem + Compressao + MarcaDagua + Log

Imagem + todos os comportamentos
```

Se tentarmos representar todas essas combinações utilizando subclasses, teremos uma grande quantidade de classes.

Por exemplo:

```text
ImagemAltaResolucao

├── ImagemComMarcaDagua
├── ImagemComCompressao
├── ImagemComContraste
├── ImagemComLog
│
├── ImagemComMarcaDaguaELog
├── ImagemComCompressaoELog
├── ImagemComContrasteELog
│
├── ImagemComCompressaoEContraste
├── ImagemComCompressaoEMarcaDagua
├── ImagemComContrasteEMarcaDagua
│
├── ImagemComCompressaoEContrasteELog
├── ImagemComCompressaoEMarcaDaguaELog
├── ImagemComContrasteEMarcaDaguaELog
│
└── ...
```

Quanto mais comportamentos forem adicionados ao sistema, maior será o número de combinações.

Esse problema é conhecido como:

> **Explosão de subclasses.**

---

# ❌ Por que isso é um problema?

Utilizar herança para representar todas as combinações torna o sistema:

- mais difícil de entender;
- mais difícil de manter;
- mais difícil de expandir;
- mais acoplado;
- mais propenso à duplicação de código;
- cheio de classes pequenas e muito parecidas.

Além disso, sempre que um novo comportamento for adicionado, várias novas combinações podem precisar ser criadas.

Imagine que adicionamos um novo requisito:

```text
Criptografia
```

Agora todas as combinações existentes poderiam potencialmente possuir também:

```text
+ Criptografia
```

A quantidade de subclasses aumentaria ainda mais.

O problema não é apenas a quantidade de classes.

O problema principal é que estamos tentando utilizar **herança para representar comportamentos combináveis**.

---

# 💡 Solução

O Decorator resolve esse problema utilizando **composição de objetos**.

Em vez de criar subclasses para cada combinação, criamos objetos que podem envolver outros objetos.

Cada objeto envolvido adiciona um comportamento.

Podemos imaginar:

```text
ImagemAltaResolucao
```

como o objeto original.

Depois podemos envolvê-lo:

```text
MarcaDagua(
    ImagemAltaResolucao
)
```

Agora podemos adicionar outro comportamento:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

E podemos continuar adicionando camadas:

```text
Contraste(
    Compressao(
        MarcaDagua(
            ImagemAltaResolucao
        )
    )
)
```

Cada camada é um **Decorator**.

---

# 🎁 Por que o nome "Decorator"?

O nome **Decorator** significa literalmente:

```text
Decorador
```

A ideia é semelhante a decorar um objeto.

Imagine uma caixa simples:

```text
Caixa
```

Podemos adicionar uma decoração:

```text
Papel de presente(
    Caixa
)
```

Depois podemos adicionar outra:

```text
Laço(
    Papel de presente(
        Caixa
    )
)
```

A caixa original continua existindo.

Porém, agora ela possui comportamentos ou características adicionais.

No Decorator acontece algo semelhante.

Temos:

```text
Objeto original
```

e adicionamos camadas ao redor dele:

```text
Decorator

    |

    v

Objeto Decorado
```

Ou:

```text
Decorator

    |

    v

Decorator

    |

    v

Objeto Original
```

Cada camada adiciona uma responsabilidade.

---

# 🧩 A ideia de "Wrapper"

O Decorator também é conhecido como um tipo de:

```text
Wrapper
```

ou:

```text
Invólucro
```

Isso acontece porque um Decorator **envolve outro objeto**.

Por exemplo:

```text
MarcaDagua(
    ImagemAltaResolucao
)
```

A classe `MarcaDagua` funciona como um invólucro ao redor da imagem.

Podemos visualizar:

```text
+----------------------+
|      MarcaDagua      |
|                      |
|  +----------------+  |
|  |                |  |
|  |     Imagem     |  |
|  |                |  |
|  +----------------+  |
|                      |
+----------------------+
```

Se adicionarmos outro Decorator:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

temos:

```text
+----------------------+
|         Log          |
|                      |
|  +----------------+  |
|  |   MarcaDagua   |  |
|  |                |  |
|  | +------------+ |  |
|  | |   Imagem   | |  |
|  | +------------+ |  |
|  |                |  |
|  +----------------+  |
|                      |
+----------------------+
```

Cada Decorator envolve outro objeto.

---

# 🔑 A característica mais importante do Decorator

Para que um Decorator possa ser utilizado no lugar do objeto original, ambos precisam compartilhar a mesma interface.

Por exemplo:

```text
Imagem
```

define:

```text
exibir()
```

Então:

```text
ImagemAltaResolucao
```

implementa:

```text
exibir()
```

Mas os Decorators também precisam implementar:

```text
exibir()
```

Assim, para o cliente, todos podem ser utilizados da mesma forma.

Por exemplo:

```text
Imagem
```

Pode ser:

```text
ImagemAltaResolucao
```

ou:

```text
MarcaDagua(ImagemAltaResolucao)
```

ou:

```text
Log(MarcaDagua(ImagemAltaResolucao))
```

Todos continuam sendo tratados como:

```text
Imagem
```

Essa característica permite adicionar camadas sem que o cliente precise conhecer todos os detalhes internos.

---

# 🏗️ Estrutura conceitual

O Decorator possui quatro participantes principais.

```text
Component
    |
    |
    +----------------------+
    |                      |
    v                      v
ConcreteComponent      BaseDecorator
                           |
                           |
                    +------+------+
                    |             |
                    v             v
             ConcreteDecorator  ConcreteDecorator
```

Vamos entender cada um deles.

---

# 🧱 Component

O **Component** define uma interface comum tanto para o objeto original quanto para os Decorators.

No nosso exemplo:

```text
Imagem
```

poderia ser o `Component`.

Ela define a operação:

```text
exibir()
```

Conceitualmente:

```python
class Imagem:

    def exibir(self):
        ...
```

A principal responsabilidade do `Component` é garantir que todos os objetos possam ser utilizados através da mesma interface.

---

# 🖼️ ConcreteComponent

O **ConcreteComponent** representa o objeto original que possui o comportamento principal.

No nosso domínio:

```text
ImagemAltaResolucao
```

é o objeto real.

Podemos representar:

```text
Imagem

    |

    v

ImagemAltaResolucao
```

Essa classe possui o comportamento original:

```text
exibir imagem
```

Por exemplo:

```python
class ImagemAltaResolucao(Imagem):

    def exibir(self):
        print("Exibindo imagem em alta resolução")
```

Ela funciona mesmo sem nenhum Decorator.

---

# 🎁 BaseDecorator

O **BaseDecorator** é uma classe que também implementa a interface do `Component`.

Porém, ele possui uma referência para outro objeto `Component`.

Conceitualmente:

```text
BaseDecorator

    |

    | possui uma referência

    v

Component
```

Podemos imaginar:

```python
class ImagemDecorator(Imagem):

    def __init__(self, imagem: Imagem):
        self.imagem = imagem
```

O Decorator recebe uma imagem.

Essa imagem pode ser:

```text
ImagemAltaResolucao
```

ou outro Decorator.

Por exemplo:

```text
ImagemDecorator

        |

        v

MarcaDagua

        |

        v

ImagemAltaResolucao
```

Ou:

```text
Log

 |

 v

Compressao

 |

 v

MarcaDagua

 |

 v

ImagemAltaResolucao
```

Essa capacidade de envolver outros Decorators é o que permite criar várias combinações.

---

# 🎨 ConcreteDecorator

Os **ConcreteDecorators** são responsáveis por adicionar comportamentos específicos.

No nosso exemplo teremos comportamentos como:

```text
MarcaDagua
```

```text
Compressao
```

```text
Contraste
```

```text
Log
```

Cada um representa uma responsabilidade adicional.

Por exemplo:

```text
MarcaDagua
```

pode:

```text
Adicionar marca d'água
```

antes de delegar a execução para o objeto envolvido.

---

# 🔄 Delegação de chamadas

Uma das ideias mais importantes do Decorator é a **delegação**.

Imagine:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

Quando chamamos:

```python
imagem.exibir()
```

a chamada começa no Decorator mais externo.

Fluxo:

```text
Cliente

   |

   v

Log.exibir()

   |

   v

MarcaDagua.exibir()

   |

   v

ImagemAltaResolucao.exibir()
```

Cada camada pode executar algum comportamento antes ou depois de delegar a chamada.

Por exemplo:

```text
Log
  |
  | registra a operação
  |
  v

MarcaDagua
  |
  | adiciona marca d'água
  |
  v

ImagemAltaResolucao
  |
  | exibe a imagem
  |
  v

Fim
```

---

# 🔀 Composição em múltiplas camadas

A grande vantagem do Decorator é que podemos combinar comportamentos livremente.

Imagine o objeto original:

```text
ImagemAltaResolucao
```

Podemos adicionar:

```text
MarcaDagua
```

Resultado:

```text
MarcaDagua(
    ImagemAltaResolucao
)
```

Depois:

```text
Compressao
```

Resultado:

```text
Compressao(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

Depois:

```text
Log
```

Resultado:

```text
Log(
    Compressao(
        MarcaDagua(
            ImagemAltaResolucao
        )
    )
)
```

Agora temos três comportamentos adicionais sem criar uma classe específica chamada:

```text
ImagemComLogCompressaoEMarcaDagua
```

Os comportamentos são montados dinamicamente.

---

# ⚡ Composição em tempo de execução

Essa é uma das principais características do Decorator.

O cliente pode decidir quais comportamentos deseja aplicar durante a execução do programa.

Por exemplo:

```python
imagem = ImagemAltaResolucao()
```

Nesse momento temos:

```text
ImagemAltaResolucao
```

Depois podemos adicionar:

```text
MarcaDagua
```

Conceitualmente:

```python
imagem = MarcaDagua(imagem)
```

Agora temos:

```text
MarcaDagua(
    ImagemAltaResolucao
)
```

Depois podemos adicionar:

```text
Log
```

Conceitualmente:

```python
imagem = Log(imagem)
```

Agora:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

O tipo concreto do objeto final é uma composição de vários objetos.

Porém, todos continuam seguindo a interface:

```text
Imagem
```

---

# 🧠 Visualizando o Decorator

Imagine o seguinte objeto:

```text
ImagemAltaResolucao
```

Sem Decorator:

```text
Cliente

   |

   v

ImagemAltaResolucao

   |

   v

exibir()
```

Com Decorators:

```text
Cliente

   |

   v

Log

   |

   v

Contraste

   |

   v

Compressao

   |

   v

MarcaDagua

   |

   v

ImagemAltaResolucao
```

Quando `exibir()` é chamado, a chamada percorre todas as camadas.

---

# 🖼️ Aplicando ao nosso domínio

No nosso exemplo, teremos uma interface comum chamada:

```text
Imagem
```

Essa interface será implementada tanto pela imagem original quanto pelos Decorators.

Estrutura conceitual:

```text
                    Imagem
                       |
                       |
             +---------+---------+
             |                   |
             v                   v
ImagemAltaResolucao      ImagemDecorator
                               |
                               |
                     +---------+---------+
                     |         |         |
                     v         v         v
                MarcaDagua  Compressao  Contraste
                                           |
                                           |
                                           v
                                          Log
```

Uma representação mais próxima da implementação será:

```text
Imagem

├── ImagemAltaResolucao
│
└── ImagemDecorator
    │
    ├── MarcaDagua
    │
    ├── Compressao
    │
    ├── Contraste
    │
    └── Log
```

---

# 🧩 Participantes do Decorator

| Participante          | Exemplo no domínio    | Responsabilidade                                 |
| --------------------- | --------------------- | ------------------------------------------------ |
| **Component**         | `Imagem`              | Define a interface comum                         |
| **ConcreteComponent** | `ImagemAltaResolucao` | Representa o objeto original                     |
| **BaseDecorator**     | `ImagemDecorator`     | Mantém uma referência para outro objeto `Imagem` |
| **ConcreteDecorator** | `MarcaDagua`          | Adiciona marca d'água                            |
| **ConcreteDecorator** | `Compressao`          | Adiciona compressão                              |
| **ConcreteDecorator** | `Contraste`           | Adiciona ajuste de contraste                     |
| **ConcreteDecorator** | `Log`                 | Adiciona registro de auditoria                   |
| **Client**            | `main.py`             | Decide quais Decorators serão combinados         |

---

# 🔄 Exemplo de combinações

O mesmo objeto original pode receber diferentes combinações.

## Imagem sem tratamentos

```text
ImagemAltaResolucao
```

---

## Imagem com marca d'água

```text
MarcaDagua

    |

    v

ImagemAltaResolucao
```

---

## Imagem com marca d'água e log

```text
Log

 |

 v

MarcaDagua

 |

 v

ImagemAltaResolucao
```

---

## Imagem comprimida com contraste

```text
Contraste

    |

    v

Compressao

    |

    v

ImagemAltaResolucao
```

---

## Imagem com todos os comportamentos

```text
Log

 |

 v

Contraste

 |

 v

Compressao

 |

 v

MarcaDagua

 |

 v

ImagemAltaResolucao
```

Nenhuma dessas combinações exige uma nova subclasse específica.

---

# 📦 Ordem dos Decorators

A ordem dos Decorators pode ser importante.

Por exemplo:

```text
Compressao(
    Contraste(
        Imagem
    )
)
```

não representa necessariamente o mesmo processamento que:

```text
Contraste(
    Compressao(
        Imagem
    )
)
```

No primeiro caso:

```text
Imagem

↓

Contraste

↓

Compressão

↓

Resultado
```

No segundo:

```text
Imagem

↓

Compressão

↓

Contraste

↓

Resultado
```

Portanto:

> A composição dos Decorators permite definir não apenas quais comportamentos serão utilizados, mas também a ordem em que eles serão executados.

---

# 🎯 Quando utilizar Decorator?

O Decorator é especialmente útil quando:

- precisamos adicionar responsabilidades a objetos dinamicamente;
- diferentes comportamentos podem ser combinados;
- existem muitas combinações possíveis de funcionalidades;
- utilizar herança criaria muitas subclasses;
- queremos estender o comportamento sem modificar a classe original;
- queremos seguir o princípio Open/Closed;
- diferentes objetos podem possuir diferentes combinações de comportamentos.

---

# 📈 Vantagens

## 1. Evita explosão de subclasses

Em vez de criar:

```text
ImagemComMarcaDaguaELog

ImagemComCompressaoEContraste

ImagemComLogEContrasteEMarcaDagua
```

criamos apenas os Decorators:

```text
MarcaDagua

Compressao

Contraste

Log
```

e combinamos os objetos.

---

## 2. Permite composição dinâmica

O cliente pode decidir em tempo de execução:

```text
quais comportamentos utilizar
```

e:

```text
em qual ordem utilizá-los
```

---

## 3. Extende comportamentos sem modificar a classe original

A classe:

```text
ImagemAltaResolucao
```

não precisa ser modificada sempre que surgir uma nova funcionalidade.

Podemos simplesmente criar um novo Decorator.

Por exemplo:

```text
CriptografiaDecorator
```

ou:

```text
CacheDecorator
```

---

## 4. Favorece o princípio Open/Closed

Uma classe deve estar:

> Aberta para extensão, mas fechada para modificação.

Com Decorator podemos adicionar novos comportamentos criando novas classes.

Não precisamos alterar constantemente:

```text
ImagemAltaResolucao
```

---

## 5. Favorece composição

O Decorator segue a ideia:

> Favoreça composição de objetos em vez de herança de classes.

Em vez de:

```text
Classe A
    |
    v

Classe B
    |
    v

Classe C
```

podemos criar:

```text
Objeto

envolvido por

Decorator

envolvido por

Decorator
```

---

# ⚠️ Desvantagens

Apesar das vantagens, o Decorator também possui alguns pontos negativos.

## Muitos objetos pequenos

Uma composição pode gerar vários objetos.

Por exemplo:

```text
Log

↓

Contraste

↓

Compressao

↓

MarcaDagua

↓

ImagemAltaResolucao
```

Isso pode tornar a estrutura mais difícil de acompanhar durante a depuração.

---

## A ordem importa

Dependendo do domínio, alterar a ordem dos Decorators pode alterar o resultado final.

Por isso, o cliente precisa montar corretamente a composição.

---

## A identidade concreta do objeto pode ser perdida

Depois de envolver um objeto em vários Decorators:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

o objeto externo não é mais diretamente uma instância concreta de:

```text
ImagemAltaResolucao
```

Ele é uma composição.

Isso significa que verificações específicas como:

```python
isinstance(...)
```

podem se tornar menos intuitivas.

O cliente deve preferir trabalhar através da abstração:

```text
Imagem
```

em vez de depender do tipo concreto interno.

---

# ❌ Quando não utilizar Decorator?

O Decorator pode não ser necessário quando:

- os comportamentos nunca são combinados;
- os comportamentos são sempre fixos;
- não existe necessidade de adicionar funcionalidades dinamicamente;
- uma simples herança resolveria o problema de maneira clara;
- a quantidade de variações é pequena e não deve crescer.

Por exemplo, se uma classe sempre possuir um comportamento fixo e nunca houver combinações:

```text
ImagemNormal
ImagemPremium
```

talvez uma solução mais simples seja suficiente.

O Decorator é mais útil quando temos:

```text
comportamentos independentes

+

combinações variáveis
```

---

# 🆚 Decorator Pattern × `@decorator` do Python

É importante não confundir o **Decorator Design Pattern** com os decoradores da linguagem Python.

Em Python podemos escrever:

```python
@decorator
def minha_funcao():
    ...
```

Isso é uma funcionalidade da linguagem.

O objetivo é modificar ou envolver funções e métodos.

Já o **Decorator Design Pattern** é um padrão de projeto estrutural.

Ele trabalha principalmente com:

```text
objetos

interfaces

composição

delegação
```

Podemos resumir assim:

> **Decorator Pattern:** padrão de projeto utilizado para adicionar responsabilidades a objetos através de composição.

> **`@decorator`:** recurso da linguagem Python utilizado para envolver ou modificar funções, métodos ou classes.

Apesar de possuírem ideias semelhantes de "envolver" comportamentos, não são exatamente a mesma coisa.

---

# 🧠 Problema que será implementado

Neste projeto será implementado um sistema de exibição de imagens utilizando o padrão **Decorator**.

Inicialmente teremos uma imagem simples:

```text
ImagemAltaResolucao
```

Essa imagem será capaz de executar:

```text
exibir()
```

Porém, novos requisitos serão adicionados.

Uma imagem poderá receber os seguintes tratamentos:

```text
Marca d'água
```

```text
Compressão
```

```text
Ajuste de contraste
```

```text
Log de auditoria
```

O cliente deverá decidir **em tempo de execução** quais tratamentos deseja aplicar.

---

# 📋 Requisitos

O sistema deverá permitir:

## 1. Imagem com marca d'água

```text
MarcaDagua(
    ImagemAltaResolucao
)
```

---

## 2. Imagem comprimida

```text
Compressao(
    ImagemAltaResolucao
)
```

---

## 3. Imagem com ajuste de contraste

```text
Contraste(
    ImagemAltaResolucao
)
```

---

## 4. Imagem com log

```text
Log(
    ImagemAltaResolucao
)
```

---

## 5. Combinação de tratamentos

Por exemplo:

```text
Log(
    MarcaDagua(
        ImagemAltaResolucao
    )
)
```

Ou:

```text
MarcaDagua(
    Contraste(
        Compressao(
            ImagemAltaResolucao
        )
    )
)
```

Ou ainda:

```text
Log(
    Contraste(
        Compressao(
            MarcaDagua(
                ImagemAltaResolucao
            )
        )
    )
)
```

---

# 🏗️ Estrutura esperada da implementação

A implementação deverá possuir uma estrutura semelhante a:

```text
Decorator/

├── main.py
│
├── imagem.py
│
├── imagem_alta_resolucao.py
│
├── imagem_decorator.py
│
├── marca_dagua.py
│
├── compressao.py
│
├── contraste.py
│
└── log.py
```

Cada arquivo possuirá uma responsabilidade específica.

---

# 🧩 Responsabilidade das classes

## `Imagem`

Será o:

```text
Component
```

Definirá a interface comum.

Por exemplo:

```text
exibir()
```

---

## `ImagemAltaResolucao`

Será o:

```text
ConcreteComponent
```

Representará o objeto real.

Será responsável pelo comportamento original de exibir uma imagem.

---

## `ImagemDecorator`

Será o:

```text
BaseDecorator
```

Manterá uma referência para outro objeto:

```text
Imagem
```

Essa referência permitirá envolver:

```text
ImagemAltaResolucao
```

ou outro Decorator.

---

## `MarcaDagua`

Será um:

```text
ConcreteDecorator
```

Responsável por adicionar uma marca d'água.

---

## `Compressao`

Será um:

```text
ConcreteDecorator
```

Responsável por aplicar compressão.

---

## `Contraste`

Será um:

```text
ConcreteDecorator
```

Responsável por aplicar ajuste de contraste.

---

## `Log`

Será um:

```text
ConcreteDecorator
```

Responsável por registrar informações de auditoria.

---

## `main.py`

Será o:

```text
Client
```

O cliente será responsável por decidir quais objetos serão combinados.

Será nele que construiremos diferentes composições.

Por exemplo:

```text
ImagemAltaResolucao
```

```text
MarcaDagua + ImagemAltaResolucao
```

```text
Log + MarcaDagua + ImagemAltaResolucao
```

```text
Log + Contraste + Compressao + MarcaDagua + ImagemAltaResolucao
```

---

# 🔄 Fluxo esperado

Imagine que o cliente monte:

```text
Log(
    Compressao(
        MarcaDagua(
            ImagemAltaResolucao
        )
    )
)
```

Quando:

```text
exibir()
```

for chamado, teremos conceitualmente:

```text
Cliente

   |

   v

Log

   |

   v

Compressao

   |

   v

MarcaDagua

   |

   v

ImagemAltaResolucao
```

Cada camada poderá adicionar seu comportamento e delegar a chamada para o próximo objeto.

---

# 🎯 Objetivo da implementação

O principal objetivo deste exercício é entender como o Decorator permite transformar:

```text
várias combinações possíveis

↓

muitas subclasses
```

em:

```text
poucos componentes reutilizáveis

↓

combinados dinamicamente
```

Em vez de criar classes como:

```text
ImagemComMarcaDaguaELog
```

```text
ImagemComCompressaoEContraste
```

```text
ImagemComCompressaoELogEMarcaDagua
```

criaremos apenas Decorators independentes:

```text
MarcaDagua
```

```text
Compressao
```

```text
Contraste
```

```text
Log
```

e deixaremos o cliente montar qualquer combinação necessária.

---

# 📌 Ideia principal para memorizar

O Decorator resolve principalmente o problema de:

> **Adicionar diferentes combinações de comportamentos a objetos sem criar uma explosão de subclasses.**

A ideia central é:

```text
Objeto original

      ↓

Decorator

      ↓

Decorator

      ↓

Decorator
```

Ou, no nosso exemplo:

```text
ImagemAltaResolucao

        ↓

    MarcaDagua

        ↓

    Compressao

        ↓

     Contraste

        ↓

        Log
```

Portanto:

> **Decorator = adicionar responsabilidades a um objeto dinamicamente através de composição, envolvendo o objeto com outros objetos que implementam a mesma interface.**
