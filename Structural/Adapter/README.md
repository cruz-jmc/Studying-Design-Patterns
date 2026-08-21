# Adapter

## 📌 Objetivo

O **Adapter** é um Design Pattern estrutural utilizado quando queremos fazer com que **objetos com interfaces incompatíveis trabalhem juntos**.

A ideia principal é criar uma classe intermediária, chamada **Adapter**, que recebe uma interface existente e a adapta para o formato que o restante do sistema espera.

Em outras palavras:

> O Adapter funciona como um "tradutor" entre duas interfaces incompatíveis.

---

## ❗ Problema

Imagine que estamos desenvolvendo um sistema de reprodução de mídia.

Nosso sistema possui uma classe `MediaPlayer` que sabe reproduzir mídias através de um método chamado:

```python
play()
```

O `MediaPlayer` espera receber um objeto que siga essa interface.

Por exemplo, nosso `AudioPlayer` implementa corretamente o método esperado:

```python
class AudioPlayer(Target):

    def play(self):
        print("Reproduzindo áudio")
```

Portanto, podemos fazer:

```python
MediaPlayer(AudioPlayer()).execute()
```

O problema aparece quando queremos adicionar um novo tipo de player.

Temos uma classe `VideoPlayer` que já existe e sabe reproduzir vídeos, mas sua interface é diferente:

```python
class VideoPlayer:

    def play_mp4(self):
        print("Reproduzindo vídeo MP4")
```

Perceba que o `MediaPlayer` espera:

```text
play()
```

enquanto o `VideoPlayer` oferece:

```text
play_mp4()
```

As interfaces são incompatíveis.

---

## 🔴 O que aconteceria sem o Adapter?

Poderíamos modificar o `VideoPlayer` para trocar:

```python
play_mp4()
```

por:

```python
play()
```

Porém, isso nem sempre é possível ou desejável.

Imagine que `VideoPlayer`:

- seja uma classe de uma biblioteca externa;
- tenha sido criada por outra equipe;
- seja utilizada por vários sistemas;
- não possa ser modificada;
- possua uma interface que precisamos preservar.

Nesse caso, alterar a classe original para atender às necessidades do nosso sistema poderia gerar problemas de manutenção e acoplamento.

Precisamos então de uma maneira de fazer as duas interfaces trabalharem juntas **sem modificar o `VideoPlayer`**.

---

## 💡 Solução

Criamos uma classe chamada `VideoAdapter`.

O `VideoAdapter` implementa a interface que o `MediaPlayer` espera:

```python
play()
```

mas internamente utiliza o método que o `VideoPlayer` possui:

```python
play_mp4()
```

Podemos representar a adaptação da seguinte maneira:

```text
MediaPlayer
    |
    | espera
    v
  play()
    |
    v
VideoAdapter
    |
    | traduz a chamada
    v
play_mp4()
    |
    v
VideoPlayer
```

Assim, o `MediaPlayer` não precisa saber que está trabalhando com um `VideoPlayer`.

Para ele, existe apenas um objeto que possui o método:

```python
play()
```

---

## 🧩 Estrutura do exemplo

A implementação deste projeto possui os seguintes componentes:

```text
Adapter/
│
├── main.py
├── player.py
├── video_adapter.py
├── video_player.py
└── README.md
```

### `Target`

O `Target` representa a interface que o cliente espera utilizar.

Neste exemplo:

```python
class Target(ABC):

    @abstractmethod
    def play(self):
        raise NotImplementedError
```

O sistema espera que os players possuam:

```python
play()
```

---

### `AudioPlayer`

O `AudioPlayer` é uma implementação que já segue diretamente a interface esperada:

```python
class AudioPlayer(Target):

    def play(self):
        print("Reproduzindo áudio")
```

Portanto:

```text
AudioPlayer
     |
     | possui
     v
  play()
     |
     v
MediaPlayer
```

Não precisamos de Adapter nesse caso.

---

### `MediaPlayer`

O `MediaPlayer` representa o **cliente** que utiliza a interface `Target`.

```python
class MediaPlayer:

    def __init__(self, player: Target):
        self.player = player

    def execute(self):
        self.player.play()
```

O ponto importante é que o `MediaPlayer` não precisa conhecer os detalhes de cada implementação.

Ele simplesmente espera receber um objeto compatível com `Target`.

---

### `VideoPlayer`

O `VideoPlayer` representa o **Adaptee**.

Ele possui a funcionalidade que queremos utilizar, mas sua interface não é compatível com a esperada pelo sistema.

```python
class VideoPlayer:

    def play_mp4(self):
        print("Reproduzindo vídeo MP4")
```

Ele possui a funcionalidade necessária, porém com outro nome de método.

---

### `VideoAdapter`

O `VideoAdapter` é o **Adapter**.

Ele implementa `Target`:

```python
class VideoAdapter(Target):
```

e recebe um `VideoPlayer`:

```python
def __init__(self, adaptee):
    self.adaptee = adaptee
```

Quando o sistema chama:

```python
play()
```

o Adapter converte essa chamada para:

```python
play_mp4()
```

Implementação:

```python
class VideoAdapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def play(self):
        self.adaptee.play_mp4()
```

---

## 🔄 Fluxo completo

Quando executamos:

```python
MediaPlayer(VideoAdapter(VideoPlayer())).execute()
```

o fluxo é:

```text
1. MediaPlayer.execute()
        |
        v
2. VideoAdapter.play()
        |
        v
3. VideoPlayer.play_mp4()
        |
        v
4. "Reproduzindo vídeo MP4"
```

Ou visualmente:

```text
              interface esperada
                     |
                     v
               +-----------+
               |   Target  |
               |   play()  |
               +-----------+
                     ^
                     |
               +-----------+
               |  Adapter  |
               |           |
               |   play()  |
               +-----------+
                     |
                     | adapta
                     v
               +-----------+
               |  Adaptee  |
               |           |
               | play_mp4()|
               +-----------+
```

---

## ▶️ Executando o exemplo

A partir da pasta `Adapter`:

```bash
python main.py
```

O resultado esperado é semelhante a:

```text
Reproduzindo áudio
Reproduzindo vídeo MP4
```

---

## 🧠 Participantes do Adapter neste exemplo

| Participante        | Classe         | Responsabilidade                                        |
| ------------------- | -------------- | ------------------------------------------------------- |
| **Target**          | `Target`       | Define a interface esperada pelo sistema                |
| **Client**          | `MediaPlayer`  | Utiliza a interface `Target`                            |
| **Adapter**         | `VideoAdapter` | Adapta uma interface para outra                         |
| **Adaptee**         | `VideoPlayer`  | Possui a funcionalidade, mas com interface incompatível |
| **Concrete Target** | `AudioPlayer`  | Implementa diretamente a interface esperada             |

---

## 🎯 Quando utilizar Adapter?

O Adapter é especialmente útil quando:

- uma classe existente possui uma interface incompatível com o sistema;
- não podemos ou não queremos modificar a classe existente;
- precisamos integrar código legado;
- precisamos integrar uma biblioteca externa;
- duas partes do sistema possuem interfaces diferentes;
- queremos reutilizar uma classe existente sem alterar sua implementação.

---

## ⚠️ Ideia principal para memorizar

O Adapter **não muda necessariamente o comportamento do objeto adaptado**.

Ele muda a **forma como o objeto é acessado**.

Neste exemplo:

```text
VideoPlayer
    |
    | possui
    v
play_mp4()
```

é transformado, através do Adapter, em algo que o sistema consegue utilizar:

```text
VideoAdapter
    |
    | disponibiliza
    v
play()
```

Portanto:

> **Adapter = adaptar uma interface existente para outra interface esperada.**

---

## 🔀 Adapter × Bridge

Adapter e Bridge podem parecer semelhantes porque ambos utilizam composição e conectam objetos.

Porém, existe uma diferença importante na intenção.

### Adapter

Normalmente é utilizado quando **já temos classes existentes que não foram projetadas para trabalhar juntas**.

O problema aparece depois:

```text
Sistema espera → play()

Classe existente → play_mp4()
```

Criamos um Adapter para fazer essas interfaces conversarem.

### Bridge

É utilizado quando estamos **projetando o sistema** e queremos separar duas dimensões que podem variar independentemente.

Por exemplo:

```text
Forma
├── Circle
└── Square

Cor
├── Red
├── Blue
└── Green
```

Em vez de criar:

```text
CircleRed
CircleBlue
CircleGreen
SquareRed
SquareBlue
SquareGreen
```

separamos as duas dimensões e fazemos a abstração utilizar uma implementação.

De forma resumida:

```text
Adapter
    ↓
"Tenho duas interfaces incompatíveis.
Preciso fazer elas trabalharem juntas."

Bridge
    ↓
"Tenho duas dimensões que podem variar.
Quero separá-las para que possam evoluir independentemente."
```

### 📝 Resumindo

> **Adapter adapta algo que já existe.**
>
> **Bridge separa algo que estamos projetando.**
