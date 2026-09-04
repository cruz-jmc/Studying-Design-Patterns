# Studying Design Patterns

Repositório destinado ao **estudo e à prática de Design Patterns (Padrões de Projeto)** utilizando a linguagem **Python**.

O objetivo deste repositório é servir como um ambiente de aprendizado no qual cada padrão de projeto é estudado individualmente, implementado em Python e acompanhado de exemplos práticos que ajudam a compreender seu propósito, estrutura e funcionamento.

---

## 📚 Sobre o repositório

Este repositório foi criado como apoio aos meus estudos durante a disciplina de **Design Patterns**, cursada no **4º período do curso de Engenharia de Software da Universidade de Pernambuco (UPE) — Campus Garanhuns**, com o professor **Carlos**.

Além de servir como material de acompanhamento da disciplina, o projeto também tem como objetivo ajudar outras pessoas que estejam estudando Design Patterns por conta própria e queiram utilizar exemplos práticos em Python como material de estudo.

A ideia é que o repositório evolua junto com os estudos: cada novo padrão aprendido será implementado, organizado e documentado em sua própria pasta.

---

## 🎯 Objetivos

Este projeto tem como principais objetivos:

- Estudar os principais Design Patterns de forma prática;
- Compreender o problema que cada padrão procura solucionar;
- Entender a estrutura e os participantes de cada padrão;
- Implementar os padrões utilizando Python;
- Praticar conceitos de Programação Orientada a Objetos;
- Observar como os padrões podem melhorar a organização e a manutenção do código;
- Servir como material de consulta durante os estudos;
- Disponibilizar exemplos que possam ajudar outras pessoas interessadas em aprender Design Patterns.

---

## 🧩 Design Patterns estudados

Os padrões estão organizados nas três categorias tradicionais:

### 🏗️ Padrões Criacionais

Padrões relacionados à **criação de objetos**, buscando fornecer mecanismos mais flexíveis e reutilizáveis para instanciar objetos.

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton

### 🧱 Padrões Estruturais

Padrões relacionados à **composição de classes e objetos**, facilitando a criação de estruturas maiores sem perder flexibilidade e organização.

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

### 🔄 Padrões Comportamentais

Padrões relacionados aos **algoritmos, comunicação e distribuição de responsabilidades entre objetos**.

- Chain of Responsibility
- Command
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

> **Observação:** o catálogo utilizado como referência neste repositório apresenta 22 Design Patterns. O catálogo clássico do GoF possui 23 padrões, sendo o padrão **Interpreter** o único que não está presente no catálogo utilizado neste projeto.

---

## 🗂️ Organização do projeto

O repositório é dividido de acordo com as três categorias de Design Patterns:

```text
Studying-Design-Patterns/
│
├── Behavioral/
│   ├── Chain_of_Responsibility/
│   ├── Command/
│   ├── Iterator/
│   ├── Mediator/
│   ├── Memento/
│   ├── Observer/
│   ├── State/
│   ├── Strategy/
│   ├── Template_Method/
│   └── Visitor/
│
├── Creational/
│   ├── Abstract_Factory/
│   ├── Builder/
│   ├── Factory_Method/
│   ├── Prototype/
│   └── Singleton/
│
└── Structural/
    ├── Adapter/
    ├── Bridge/
    ├── Composite/
    ├── Decorator/
    ├── Facade/
    ├── Flyweight/
    └── Proxy/
```

Cada Design Pattern possui sua própria pasta e funciona como um exemplo independente.

A quantidade de arquivos dentro de cada pasta pode variar de acordo com a complexidade do padrão. Classes, interfaces, abstrações e demais componentes podem ser separados em diferentes arquivos `.py` quando isso contribuir para uma melhor organização e compreensão da implementação.

---

## 🐍 Linguagem

Todas as implementações deste repositório são feitas utilizando:

- **Python 3**

Os exemplos priorizam uma implementação simples e didática, buscando representar os conceitos fundamentais de cada Design Pattern sem adicionar complexidade desnecessária.

---

## ▶️ Executando os exemplos

Cada Design Pattern possui um arquivo `main.py`, responsável por demonstrar o funcionamento daquele padrão.

Por exemplo, considerando a estrutura:

```text
Structural/
└── Adapter/
    ├── main.py
    ├── player.py
    ├── video_adapter.py
    ├── video_player.py
    └── README.md
```

Primeiro, entre na pasta do padrão:

```bash
cd Structural/Adapter
```

Depois, execute o `main.py`:

```bash
python main.py
```

---

### Executando diretamente a partir da raiz

Também é possível manter o terminal na raiz do projeto e executar o `main.py` informando seu caminho:

```bash
python Structural/Adapter/main.py
```

Outro exemplo:

```bash
python Structural/Facade/main.py
```

Ou:

```bash
python Behavioral/Strategy/main.py
```

Dessa forma, não é necessário abrir uma nova janela do VS Code para cada Design Pattern.

---

## 💻 Ambiente de desenvolvimento

A recomendação é abrir a pasta **`Studying-Design-Patterns` como pasta-raiz do projeto no VS Code**.

```text
VS Code
└── Studying-Design-Patterns/
    ├── Behavioral/
    ├── Creational/
    └── Structural/
```

Assim, todos os Design Patterns ficam disponíveis no mesmo espaço de trabalho.

Cada padrão pode ser acessado individualmente através do Explorer do VS Code, enquanto o projeto inteiro permanece aberto como uma única workspace.

---

## 📖 Estrutura de cada Design Pattern

Sempre que fizer sentido, cada padrão poderá possuir uma estrutura semelhante a:

```text
Pattern/
│
├── main.py
├── classe_1.py
├── classe_2.py
├── classe_3.py
└── README.md
```

### `main.py`

Responsável pela demonstração do padrão.

É onde os objetos são instanciados e onde o comportamento do Design Pattern é executado.

### Arquivos `.py`

Contêm as classes, interfaces, abstrações e demais componentes necessários para implementar o padrão.

As classes são separadas em diferentes arquivos quando isso ajuda a representar melhor as responsabilidades existentes no padrão.

### `README.md`

Quando presente, contém uma explicação específica daquele Design Pattern, incluindo conceitos, problema, solução, participantes e funcionamento da implementação.

---

## 🧪 Exemplo: Adapter

A implementação do Adapter segue uma estrutura semelhante a:

```text
Adapter/
│
├── main.py
├── player.py
├── video_adapter.py
├── video_player.py
└── README.md
```

Nesse exemplo, o `main.py` demonstra a utilização do padrão, enquanto os demais arquivos representam os diferentes componentes envolvidos na solução.

A ideia é que cada implementação seja pequena o suficiente para ser compreendida individualmente e, ao mesmo tempo, completa o suficiente para demonstrar o funcionamento do padrão na prática.

---

## 🌱 Evolução do projeto

Este repositório é um projeto de estudo e, portanto, está em constante evolução.

Novos padrões, exemplos, explicações e melhorias na implementação podem ser adicionados conforme o avanço dos estudos.

A intenção não é apenas reunir códigos prontos, mas **registrar o processo de aprendizado dos Design Patterns através da implementação prática em Python**.

---

## 🎓 Contexto acadêmico

Este projeto foi desenvolvido como apoio aos estudos da disciplina de **Design Patterns**, cursada no:

- **Curso:** Engenharia de Software
- **Período:** 4º período
- **Instituição:** Universidade de Pernambuco — UPE
- **Campus:** Garanhuns
- **Professor:** Carlos

Professor Carlos: [GitHub](https://github.com/casm3)

---

## 🤝 Para quem este repositório pode ser útil?

Este repositório pode ser utilizado por:

- estudantes de Engenharia de Software;
- estudantes de Ciência da Computação;
- pessoas estudando Programação Orientada a Objetos;
- pessoas aprendendo Design Patterns;
- desenvolvedores que desejam revisar os padrões clássicos;
- qualquer pessoa interessada em praticar Design Patterns utilizando Python.

Sinta-se à vontade para utilizar os exemplos como material de estudo e referência.

---

## 📌 Propósito

> **Aprender Design Patterns não apenas conhecendo suas definições, mas entendendo os problemas que eles resolvem e praticando sua implementação.**

Este repositório existe para acompanhar esse processo de aprendizado, servindo tanto como registro dos meus estudos na disciplina de **Design Patterns** quanto como material de apoio para qualquer pessoa que queira estudar o assunto por conta própria.
