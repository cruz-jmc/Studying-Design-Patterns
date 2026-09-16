# Exemplo-Problema — Sistema de Interface com Temas

## 📌 Descrição do problema

Imagine um sistema de interface gráfica (UI) que precisa funcionar com **dois temas diferentes**:

- 🌑 **Dark**
- ☀️ **Light**

Cada tema possui seus próprios componentes visuais. Neste exemplo, trabalharemos com dois tipos de componentes:

- **Botão**
- **Janela**

O sistema precisa conseguir criar os componentes correspondentes ao tema selecionado.

Por exemplo:

### 🌑 Tema Dark

Ao utilizar o tema Dark, a aplicação deverá trabalhar com:

- `BotaoDark`
- `JanelaDark`

### ☀️ Tema Light

Ao utilizar o tema Light, a aplicação deverá trabalhar com:

- `BotaoLight`
- `JanelaLight`

A aplicação deverá conseguir trabalhar com os componentes de interface sem precisar lidar diretamente com os detalhes de implementação de cada componente concreto.

---

# 🧩 Componentes do exemplo

O exemplo será dividido em três grupos principais:

1. Interfaces dos produtos
2. Fábricas dos componentes
3. Aplicação

---

## 1. Interfaces dos produtos

As interfaces representam os tipos de componentes que podem ser utilizados pela aplicação.

### `Botao`

Representa um botão da interface.

O botão deverá possuir um comportamento comum:

```text
Botao
└── desenhar()
```

A partir dessa interface serão criados os botões específicos para cada tema:

```text
Botao
├── BotaoDark
└── BotaoLight
```

---

### `Janela`

Representa uma janela da interface.

A janela deverá possuir um comportamento comum:

```text
Janela
└── exibir()
```

A partir dessa interface serão criadas as janelas específicas para cada tema:

```text
Janela
├── JanelaDark
└── JanelaLight
```

---

# 2. Fábricas dos componentes

A aplicação terá uma fábrica responsável por criar os componentes da interface.

A interface `UIFactory` deverá definir duas operações:

```text
UIFactory
├── criar_botao()
└── criar_janela()
```

Teremos duas implementações dessa fábrica:

```text
UIFactory
├── DarkThemeFactory
└── LightThemeFactory
```

---

## `DarkThemeFactory`

A `DarkThemeFactory` será responsável pela criação dos componentes relacionados ao tema Dark.

```text
DarkThemeFactory
├── criar_botao()  → BotaoDark
└── criar_janela() → JanelaDark
```

Quando a aplicação estiver utilizando essa fábrica, os componentes criados deverão pertencer ao conjunto Dark.

---

## `LightThemeFactory`

A `LightThemeFactory` será responsável pela criação dos componentes relacionados ao tema Light.

```text
LightThemeFactory
├── criar_botao()  → BotaoLight
└── criar_janela() → JanelaLight
```

Quando a aplicação estiver utilizando essa fábrica, os componentes criados deverão pertencer ao conjunto Light.

---

# 3. Aplicação

A classe `Aplicacao` representa o sistema que utiliza os componentes da interface.

Ela deverá receber uma `UIFactory` e utilizá-la para criar:

- um botão;
- uma janela.

Sua estrutura pode ser representada da seguinte forma:

```text
Aplicacao
├── factory
├── botao
└── janela
```

A aplicação utilizará os componentes por meio das interfaces `Botao` e `Janela`.

Dessa forma, a `Aplicacao` não precisará trabalhar diretamente com classes como:

```text
BotaoDark
BotaoLight
JanelaDark
JanelaLight
```

Ela trabalhará com os tipos gerais:

```text
Botao
Janela
```

---

# 📂 Estrutura dos arquivos

A implementação em Python poderá ser organizada da seguinte maneira:

```text
Another_Example/
│
├── README.md
│
├── main.py
│
├── factory/
│   ├── __init__.py
│   ├── ui_factory.py
│   ├── dark_theme_factory.py
│   └── light_theme_factory.py
│
└── produto/
    ├── __init__.py
    ├── botao.py
    ├── botao_dark.py
    ├── botao_light.py
    ├── janela.py
    ├── janela_dark.py
    └── janela_light.py
```

---

# 📄 Descrição dos arquivos

## `main.py`

É o arquivo responsável por executar o exemplo.

Nele será possível:

- escolher uma fábrica;
- criar a aplicação;
- criar um botão;
- criar uma janela;
- utilizar os componentes criados.

O `main.py` funcionará como ponto de entrada da aplicação.

---

# 🏭 Diretório `factory/`

O diretório `factory/` conterá as classes responsáveis pela criação dos componentes da interface.

---

## `factory/ui_factory.py`

Contém a definição da `UIFactory`.

Ela deverá declarar os métodos responsáveis pela criação dos componentes:

```text
UIFactory
├── criar_botao()
└── criar_janela()
```

---

## `factory/dark_theme_factory.py`

Contém a implementação `DarkThemeFactory`.

Essa fábrica será responsável por criar os componentes do tema Dark:

```text
DarkThemeFactory
├── criar_botao()  → BotaoDark
└── criar_janela() → JanelaDark
```

---

## `factory/light_theme_factory.py`

Contém a implementação `LightThemeFactory`.

Essa fábrica será responsável por criar os componentes do tema Light:

```text
LightThemeFactory
├── criar_botao()  → BotaoLight
└── criar_janela() → JanelaLight
```

---

# 🧱 Diretório `produto/`

O diretório `produto/` conterá as interfaces e implementações dos componentes da interface gráfica.

---

## `produto/botao.py`

Contém a definição do componente `Botao`.

Ele representa o comportamento comum de todos os botões da aplicação.

```text
Botao
└── desenhar()
```

---

## `produto/botao_dark.py`

Contém a implementação `BotaoDark`.

Esse componente representa um botão pertencente ao tema Dark.

```text
BotaoDark
└── desenhar()
```

---

## `produto/botao_light.py`

Contém a implementação `BotaoLight`.

Esse componente representa um botão pertencente ao tema Light.

```text
BotaoLight
└── desenhar()
```

---

## `produto/janela.py`

Contém a definição do componente `Janela`.

Ele representa o comportamento comum de todas as janelas da aplicação.

```text
Janela
└── exibir()
```

---

## `produto/janela_dark.py`

Contém a implementação `JanelaDark`.

Esse componente representa uma janela pertencente ao tema Dark.

```text
JanelaDark
└── exibir()
```

---

## `produto/janela_light.py`

Contém a implementação `JanelaLight`.

Esse componente representa uma janela pertencente ao tema Light.

```text
JanelaLight
└── exibir()
```

---

# 🔗 Relação entre os arquivos

A estrutura geral da implementação pode ser visualizada da seguinte maneira:

```text
                         ┌─────────────────┐
                         │    Aplicacao    │
                         └────────┬────────┘
                                  │
                                  │ utiliza
                                  ▼
                         ┌─────────────────┐
                         │    UIFactory    │
                         └────────┬────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          ┌──────────────────┐        ┌──────────────────┐
          │ DarkThemeFactory │        │ LightThemeFactory│
          └────────┬─────────┘        └─────────┬────────┘
                   │                            │
             cria │                            │ cria
                   │                            │
          ┌────────┴────────┐          ┌────────┴────────┐
          ▼                 ▼          ▼                 ▼
    ┌───────────┐     ┌────────────┐ ┌───────────┐ ┌────────────┐
    │ BotaoDark │     │ JanelaDark │ │ BotaoLight│ │ JanelaLight│
    └───────────┘     └────────────┘ └───────────┘ └────────────┘
          │                 │              │              │
          │                 │              │              │
          └──── implementam ┘              └─── implementam ┘
                   │                               │
                   ▼                               ▼
             ┌───────────┐                   ┌───────────┐
             │   Botao   │                   │  Janela   │
             └───────────┘                   └───────────┘
```

---

# 🔄 Fluxo da aplicação

O funcionamento esperado do exemplo será:

```text
1. A aplicação recebe uma UIFactory
                │
                ▼
2. A UIFactory cria um Botao
                │
                ▼
3. A UIFactory cria uma Janela
                │
                ▼
4. A aplicação utiliza o Botao
                │
                ▼
5. A aplicação utiliza a Janela
```

---

## 🌑 Utilizando o tema Dark

Quando a aplicação receber uma `DarkThemeFactory`, o fluxo será:

```text
Aplicacao
    │
    ▼
DarkThemeFactory
    │
    ├── criar_botao()  ──→ BotaoDark
    │
    └── criar_janela() ──→ JanelaDark
```

---

## ☀️ Utilizando o tema Light

Quando a aplicação receber uma `LightThemeFactory`, o fluxo será:

```text
Aplicacao
    │
    ▼
LightThemeFactory
    │
    ├── criar_botao()  ──→ BotaoLight
    │
    └── criar_janela() ──→ JanelaLight
```

---

# 🗂️ Visão geral da estrutura

A relação entre os componentes pode ser resumida da seguinte forma:

```text
                         Aplicacao
                             │
                             ▼
                         UIFactory
                       /            \
                      /              \
                     ▼                ▼
          DarkThemeFactory     LightThemeFactory
                 │                     │
           ┌─────┴─────┐         ┌─────┴─────┐
           ▼           ▼         ▼           ▼
       BotaoDark  JanelaDark  BotaoLight  JanelaLight
           │           │         │           │
           ▼           ▼         ▼           ▼
         Botao       Janela    Botao       Janela
```

O exemplo será implementado em **Python**, utilizando essa estrutura de arquivos como base para a próxima etapa da implementação.
