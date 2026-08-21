# Adapter — Integração com BeeAI

## 📚 Sobre o problema

Este exercício apresenta uma situação prática para aplicação do **Design Pattern Adapter**.

Uma equipe desenvolveu um sistema responsável por analisar relatórios financeiros. O sistema recebe os dados através de uma interface padronizada chamada `DataLoader`, que fornece uma lista de dicionários.

Posteriormente, a empresa adquiriu uma ferramenta de Business Intelligence chamada **BeeAI**. A ferramenta possui todas as informações necessárias para alimentar o sistema, porém sua API utiliza uma estrutura completamente diferente da esperada pelo sistema atual.

Além disso, existem duas restrições importantes:

- O código da BeeAI é proprietário e **não pode ser modificado**.
- O sistema atual está em produção e **não deve ser alterado**.

Portanto, precisamos fazer com que os dois sistemas trabalhem juntos **sem modificar nenhum deles**.

É justamente nesse ponto que o **Adapter** entra em ação.

---

## 🎯 Objetivo

O objetivo deste exercício é utilizar o **Adapter Pattern** para adaptar a interface fornecida pela `BeeAiClient` à interface `DataLoader` esperada pelo `ReportAnalyzer`.

O fluxo será:

```text
BeeAiClient
     │
     ▼
BeeAiAdapter
     │
     ▼
DataLoader
     │
     ▼
ReportAnalyzer
```

O `BeeAiAdapter` funciona como uma camada intermediária responsável por converter os dados da BeeAI para o formato que o sistema atual entende.

---

## 🧩 Problema

O sistema existente trabalha com uma interface:

```python
class DataLoader(ABC):

    @abstractmethod
    def load(self) -> list[dict]:
        ...
```

Portanto, o `ReportAnalyzer` espera receber um objeto que possua o método:

```python
load()
```

E que retorne uma lista de dicionários:

```python
[
    {
        "id": 1337,
        "date": "2026-08-01",
        "final_price": 1000.00
    }
]
```

Porém, a BeeAI fornece os mesmos dados em outro formato:

```python
headers = ["id", "date", "final_price"]

rows = [
    [1337, "2026-08-01", 1000.00],
    [1338, "2026-08-02", 4000.50],
    [1339, "2026-08-03", 1500.00]
]
```

Temos, portanto, uma incompatibilidade entre as duas interfaces.

---

## 🔌 Solução com Adapter

Criamos uma classe intermediária:

```python
class BeeAiAdapter(DataLoader):
```

Essa classe implementa a interface que o sistema atual espera, mas internamente utiliza a API da BeeAI.

O Adapter converte:

```text
headers + rows
      │
      ▼
BeeAiAdapter
      │
      ▼
list[dict]
```

Assim, o `ReportAnalyzer` não precisa saber como a BeeAI funciona.

---

## 👥 Participantes do Adapter Pattern

Neste exercício, cada componente representa um papel clássico do Design Pattern Adapter:

| Papel       | Implementação    |
| ----------- | ---------------- |
| **Target**  | `DataLoader`     |
| **Client**  | `ReportAnalyzer` |
| **Adaptee** | `BeeAiClient`    |
| **Adapter** | `BeeAiAdapter`   |

### Target — `DataLoader`

Define a interface que o sistema espera utilizar.

```python
class DataLoader(ABC):

    @abstractmethod
    def load(self) -> list[dict]:
        raise NotImplementedError
```

---

### Client — `ReportAnalyzer`

É o sistema que utiliza o `DataLoader`.

```python
class ReportAnalyzer:

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def average(self) -> float:
        data = self.loader.load()

        total = sum(item["final_price"] for item in data)

        return total / len(data)
```

O `ReportAnalyzer` não conhece a BeeAI.

Ele apenas sabe que recebeu um `DataLoader` e que pode chamar:

```python
self.loader.load()
```

---

### Adaptee — `BeeAiClient`

É a ferramenta externa que possui uma interface incompatível com o sistema.

```python
class BeeAiClient:

    def __init__(self):
        self.headers = ["id", "date", "final_price"]

        self.rows = [
            [1337, "2026-08-01", 1000.00],
            [1338, "2026-08-02", 4000.50],
            [1339, "2026-08-03", 1500.00]
        ]
```

Seu código não pode ser modificado.

---

### Adapter — `BeeAiAdapter`

É responsável por adaptar a interface da BeeAI para a interface esperada pelo sistema.

```python
from data_loader import DataLoader


class BeeAiAdapter(DataLoader):

    def __init__(self, client):
        self.client = client

    def load(self) -> list[dict]:

        return [
            dict(zip(self.client.headers, row))
            for row in self.client.rows
        ]
```

O Adapter transforma:

```python
headers = ["id", "date", "final_price"]

row = [1337, "2026-08-01", 1000.00]
```

em:

```python
{
    "id": 1337,
    "date": "2026-08-01",
    "final_price": 1000.00
}
```

---

# 🗂️ Estrutura dos arquivos

A implementação deste exercício está organizada da seguinte forma:

```text
Another_Example/
│
├── main.py
├── data_loader.py
├── report_analyzer.py
├── bee_ai.py
├── bee_ai_adapter.py
└── README.md
```

### `data_loader.py`

Contém o **Target**, representado pela classe `DataLoader`.

### `report_analyzer.py`

Contém o **Client**, representado pela classe `ReportAnalyzer`.

### `bee_ai.py`

Contém o **Adaptee**, representado pela classe `BeeAiClient`.

### `bee_ai_adapter.py`

Contém o **Adapter**, representado pela classe `BeeAiAdapter`.

### `main.py`

Responsável por instanciar os objetos e demonstrar o funcionamento do padrão.

---

# ▶️ Execução

A partir da pasta `Another_Example`, execute:

```bash
python main.py
```

O fluxo executado pelo `main.py` será:

```text
BeeAiClient
     │
     ▼
BeeAiAdapter
     │
     ▼
ReportAnalyzer
     │
     ▼
average()
```

O `ReportAnalyzer` recebe o Adapter como se ele fosse um `DataLoader` comum.

---

# 🔄 Comparação com o problema anterior

Este exercício possui a mesma ideia fundamental do exemplo anterior do reprodutor de mídia, porém aplicada a um problema mais próximo de um cenário real.

## 1. Comparação entre os dois exemplos

No exemplo anterior tínhamos:

```text
MediaPlayer
    │
    ▼
VideoAdapter
    │
    ▼
VideoPlayer
```

Neste exercício temos:

```text
ReportAnalyzer
    │
    ▼
BeeAiAdapter
    │
    ▼
BeeAiClient
```

Os dois exemplos utilizam exatamente a mesma ideia:

> Um objeto possui uma interface incompatível com aquilo que o sistema espera, então criamos um Adapter para fazer a comunicação entre eles.

---

## 2. Diferença entre os dois exemplos

No exemplo anterior, o Adapter precisava adaptar o nome de um método.

O `MediaPlayer` esperava:

```python
play()
```

Enquanto o `VideoPlayer` possuía:

```python
play_mp4()
```

O `VideoAdapter` fazia essa adaptação:

```text
play()
  │
  ▼
VideoAdapter
  │
  ▼
play_mp4()
```

Neste exercício, a incompatibilidade está no **formato dos dados**.

A BeeAI fornece:

```python
headers = ["id", "date", "final_price"]

rows = [
    [1337, "2026-08-01", 1000.00],
    [1338, "2026-08-02", 4000.50],
    [1339, "2026-08-03", 1500.00]
]
```

Enquanto o sistema espera:

```python
[
    {
        "id": 1337,
        "date": "2026-08-01",
        "final_price": 1000.00
    },
    {
        "id": 1338,
        "date": "2026-08-02",
        "final_price": 4000.50
    },
    {
        "id": 1339,
        "date": "2026-08-03",
        "final_price": 1500.00
    }
]
```

Portanto:

```text
Exemplo anterior:

play()
  ↓
play_mp4()


Exercício BeeAI:

headers + rows
      ↓
   list[dict]
```

O Adapter não precisa necessariamente adaptar apenas métodos. Ele pode adaptar **interfaces, formatos de dados, parâmetros, estruturas ou qualquer outra incompatibilidade entre componentes**.

---

## 3. Uma forma simples de entender o Adapter

Podemos imaginar que o `ReportAnalyzer` e a `BeeAiClient` falam "idiomas diferentes".

O `ReportAnalyzer` diz:

```text
"Eu preciso de um DataLoader que tenha load()."
```

Enquanto a BeeAI fornece:

```text
"Eu tenho headers e rows."
```

O `BeeAiAdapter` funciona como um tradutor:

```text
                    BeeAiClient
                         │
                         │
                  headers + rows
                         │
                         ▼
                  BeeAiAdapter
                         │
                         │
                    list[dict]
                         │
                         ▼
                  ReportAnalyzer
```

O `ReportAnalyzer` não precisa conhecer a existência da BeeAI.

A BeeAI também não precisa ser modificada.

O Adapter é responsável por fazer toda a tradução necessária entre os dois.

---

# 💡 Conceito principal

O **Adapter Pattern** permite que objetos com interfaces incompatíveis trabalhem juntos sem que seja necessário modificar o código existente.

Neste exercício:

```text
┌──────────────────┐
│  ReportAnalyzer  │
│     (Client)     │
└────────┬─────────┘
         │
         │ espera DataLoader
         ▼
┌──────────────────┐
│   BeeAiAdapter    │
│    (Adapter)      │
└────────┬─────────┘
         │
         │ utiliza
         ▼
┌──────────────────┐
│   BeeAiClient     │
│    (Adaptee)      │
└──────────────────┘
```

A principal vantagem é que conseguimos integrar a BeeAI ao sistema existente **sem modificar o código do sistema e sem modificar a ferramenta externa**.

---

## 📌 Resumo

```text
Target
  │
  └── DataLoader
          ▲
          │
          │ implementa
          │
      BeeAiAdapter
          │
          │ adapta
          ▼
     BeeAiClient
       (BeeAI)


Client
  │
  └── ReportAnalyzer
```

**DataLoader** define o que o sistema espera.

**ReportAnalyzer** utiliza essa interface.

**BeeAiClient** possui uma interface diferente.

**BeeAiAdapter** faz a conversão entre os dois.

Esse é o princípio fundamental do **Adapter Design Pattern**.
