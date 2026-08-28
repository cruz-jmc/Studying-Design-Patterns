# Proxy

## 📌 Objetivo

O **Proxy** é um Design Pattern estrutural utilizado para **fornecer um objeto representante ou substituto para outro objeto**, permitindo **controlar o acesso ao objeto real**.

A ideia principal do Proxy é que o cliente não precisa necessariamente conversar diretamente com o objeto real.

Em vez disso, existe um objeto intermediário:

```text
Cliente

   |

   v

Proxy

   |

   v

Objeto Real
```

O Proxy possui a **mesma interface** do objeto real. Por isso, para o cliente, a diferença entre utilizar o Proxy ou o objeto real pode ser praticamente invisível.

Uma forma simples de entender o padrão é:

> Em vez de entregar diretamente um objeto ao cliente, entregamos um representante desse objeto capaz de controlar quando, como ou se o objeto real será utilizado.

---

# ❗ Problema

Imagine que estamos desenvolvendo um sistema de armazenamento de imagens produzidas por um telescópio espacial.

Essas imagens possuem alta resolução e podem ocupar uma quantidade significativa de memória.

Suponha que:

```text
Cada imagem possui aproximadamente:

450 MB
```

Durante uma única sessão, o sistema pode possuir centenas de imagens disponíveis.

Por exemplo:

```text
300 imagens
```

Se cada imagem possuir aproximadamente:

```text
450 MB
```

o sistema poderia tentar carregar:

```text
300 × 450 MB = 135.000 MB
```

Ou aproximadamente:

```text
135 GB
```

em uma única sessão.

Mas surge uma pergunta importante:

> O usuário realmente vai abrir todas essas imagens?

Provavelmente não.

Talvez o usuário abra apenas:

```text
3

4

10
```

das centenas de imagens disponíveis.

Mesmo assim, uma implementação mal projetada poderia carregar todas as imagens antecipadamente.

---

# 💥 Onde está o desperdício?

Imagine uma galeria contendo:

```text
300 imagens
```

O sistema poderia fazer:

```text
Criar Image 1
Carregar Image 1

Criar Image 2
Carregar Image 2

Criar Image 3
Carregar Image 3

...

Criar Image 300
Carregar Image 300
```

Porém, o usuário pode abrir apenas:

```text
Image 3

Image 47

Image 210
```

Isso significa que centenas de imagens foram carregadas sem necessidade.

Temos desperdício de:

- memória RAM;
- espaço em cache;
- processamento;
- tempo de carregamento;
- recursos de armazenamento;
- largura de banda, caso as imagens estejam em um servidor remoto.

---

## 🔴 O problema conceitual

O problema acontece porque o cliente conversa diretamente com o objeto pesado.

Podemos representar assim:

```text
Cliente
   |
   v
HighResolutionImage
   |
   v
Carrega arquivo pesado
```

E, nesse caso, simplesmente criar o objeto já pode significar carregar todos os seus recursos.

Isso é problemático quando:

- o objeto é pesado;
- sua criação é lenta;
- consome muita memória;
- acessa arquivos;
- acessa banco de dados;
- faz requisições pela rede;
- o objeto pode nunca ser utilizado.

---

# 💡 Uma possível solução

Uma ideia seria:

> Carregar a imagem apenas quando ela realmente for necessária.

Por exemplo:

```text
Abrir galeria
      |
      v
Mostrar miniaturas
      |
      v
Usuário clicou na imagem?
      |
   +--+--+
   |     |
  Não   Sim
   |     |
   v     v
Não     Carregar
carrega  imagem
```

Isso evita carregar todas as imagens antecipadamente.

Mas surge uma nova pergunta:

> Como implementar esse comportamento sem alterar a forma como o cliente utiliza a imagem?

O cliente idealmente deveria continuar utilizando algo parecido com:

```python
image.display()
```

Sem precisar saber se a imagem:

- já foi carregada;
- ainda não foi carregada;
- está sendo carregada remotamente;
- está sendo buscada de um cache.

É exatamente nesse tipo de situação que o **Proxy** se torna útil.

---

# 💡 Solução com Proxy

Em vez de entregar diretamente o objeto `HighResolutionImage` ao cliente, podemos entregar um Proxy.

```text
Cliente

   |

   v

ImageProxy

   |

   | cria o objeto real apenas quando necessário

   v

HighResolutionImage
```

O cliente continua utilizando a mesma interface.

Por exemplo:

```python
image.display()
```

Mas internamente o Proxy pode decidir:

```text
A imagem já foi carregada?
        |
    +---+---+
    |       |
   Não      Sim
    |       |
    v       v
Carregar   Exibir
    |
    v
Exibir
```

Esse comportamento é chamado de:

> **Lazy Loading**, ou **Inicialização Preguiçosa**.

---

# 🦥 O que é Lazy Loading?

**Lazy Loading** significa:

> Criar ou carregar um recurso apenas quando ele realmente for necessário.

No exemplo da imagem:

### Sem Lazy Loading

```text
Aplicação inicia
       |
       v
Carrega todas as imagens
       |
       v
Usuário talvez utilize algumas
```

### Com Lazy Loading

```text
Aplicação inicia
       |
       v
Imagens ainda não são carregadas
       |
       v
Usuário solicita uma imagem
       |
       v
Proxy carrega apenas essa imagem
```

Portanto, o Proxy pode evitar o desperdício de recursos.

---

# 🧩 Estrutura conceitual do Proxy

O Proxy geralmente possui quatro participantes principais.

```text
Client
   |
   v
Subject
  / \
 /   \
v     v
Proxy  RealSubject
```

Cada participante possui uma responsabilidade diferente.

---

## 🔷 Subject

O `Subject` representa a interface comum entre o Proxy e o objeto real.

Por exemplo:

```python
class Image:
    def display(self):
        ...
```

Tanto o Proxy quanto o objeto real implementam essa interface.

```text
Image
  |
  +--------+
  |        |
  v        v
Proxy   RealImage
```

Essa interface é extremamente importante.

É ela que permite que o cliente utilize tanto o Proxy quanto o objeto real da mesma forma.

---

## 🟢 RealSubject

O `RealSubject` representa o objeto real.

No nosso exemplo:

```text
HighResolutionImage
```

Ele possui a lógica principal.

```text
HighResolutionImage
       |
       v
Carrega a imagem
       |
       v
Armazena os dados
       |
       v
Exibe a imagem
```

É normalmente o objeto que queremos proteger, controlar ou evitar criar antecipadamente.

---

## 🟡 Proxy

O `Proxy` representa o objeto intermediário.

Ele implementa a mesma interface do objeto real.

```text
Image
  |
  +----------------+
  |                |
  v                v
ImageProxy   HighResolutionImage
```

O Proxy mantém uma referência para o objeto real.

```text
ImageProxy
     |
     | possui
     v
HighResolutionImage
```

Antes de encaminhar uma operação para o objeto real, o Proxy pode adicionar comportamentos.

Por exemplo:

```text
Verificar permissões
Registrar acesso
Verificar cache
Criar objeto
Conectar remotamente
Carregar recurso
```

Depois disso:

```text
Proxy
   |
   v
Objeto Real
```

---

## 👤 Client

O `Client` é o código que utiliza o serviço.

O ponto importante é:

> O cliente deve depender da interface comum, e não diretamente da classe concreta do objeto real.

Assim, o cliente pode utilizar:

```python
image.display()
```

sem precisar saber se `image` é:

```text
HighResolutionImage
```

ou:

```text
ImageProxy
```

Essa troca deve ser transparente.

---

# 🔄 Visualizando o funcionamento

Podemos representar o fluxo assim:

```text
          Cliente

             |

             | display()

             v

            Proxy

             |

      A imagem existe?

          /      \

        Não       Sim

        |          |

        v          |

 Criar objeto       |

      real          |

        |           |

        +-----------+

             |

             v

      HighResolutionImage

             |

             v

      Carregar/Exibir
```

Na primeira chamada:

```text
Cliente
   |
   v
Proxy
   |
   v
Objeto real ainda não existe
   |
   v
Criar objeto real
   |
   v
Carregar imagem
   |
   v
Exibir imagem
```

Nas próximas chamadas:

```text
Cliente
   |
   v
Proxy
   |
   v
Objeto real já existe
   |
   v
Exibir imagem
```

---

# 🏗️ Exemplo conceitual em Python

Primeiro, podemos criar uma interface comum.

```python
from abc import ABC, abstractmethod


class Image(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError
```

Essa classe define o contrato.

Tanto o Proxy quanto a imagem real devem possuir:

```python
display()
```

---

# 🖼️ Objeto real

Agora podemos criar o objeto pesado.

```python
class HighResolutionImage(Image):

    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Carregando imagem de alta resolução: {self.filename}")

    def display(self):
        print(f"Exibindo imagem: {self.filename}")
```

A criação desse objeto executa:

```python
self.load_image()
```

Portanto:

```text
HighResolutionImage("galaxy.jpg")
              |
              v
        Carrega arquivo
```

Esse é exatamente o comportamento que queremos evitar quando a imagem ainda não é necessária.

---

# 🕵️ Criando o Proxy

Agora podemos criar:

```python
class ImageProxy(Image):

    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):

        if self.real_image is None:
            self.real_image = HighResolutionImage(self.filename)

        self.real_image.display()
```

O Proxy inicialmente possui:

```python
self.real_image = None
```

Portanto:

```text
Proxy criado

Objeto real?

Não existe
```

A imagem real ainda não foi carregada.

Quando o cliente chama:

```python
image.display()
```

o Proxy verifica:

```python
if self.real_image is None:
```

Se o objeto ainda não existe:

```text
Criar HighResolutionImage
```

Depois:

```python
self.real_image.display()
```

é executado.

---

# 🔗 Utilizando o Proxy

O cliente pode fazer:

```python
image = ImageProxy("galaxy.jpg")
```

Nesse momento:

```text
Proxy criado

Imagem real não carregada
```

Depois:

```python
image.display()
```

O fluxo será:

```text
Cliente
   |
   v
ImageProxy.display()
   |
   v
Imagem real existe?
   |
   v
Não
   |
   v
Criar HighResolutionImage
   |
   v
Carregar imagem
   |
   v
Exibir imagem
```

Se chamarmos novamente:

```python
image.display()
```

o Proxy verifica novamente.

Agora:

```text
Imagem real existe?

Sim
```

Portanto, não precisa criar e carregar novamente.

---

# ⚡ Proxy Virtual

O exemplo-problema representa um tipo muito comum de Proxy:

> **Virtual Proxy**

O Proxy Virtual é utilizado para controlar a criação de objetos pesados.

A ideia é:

```text
Não criar agora
       |
       v
Criar somente quando necessário
```

É especialmente útil quando o objeto:

- consome muita memória;
- demora para ser criado;
- acessa arquivos grandes;
- realiza processamento pesado;
- utiliza recursos externos.

Exemplos:

```text
Imagens de alta resolução
Vídeos
Documentos grandes
Modelos de Inteligência Artificial
Conexões com banco de dados
Objetos complexos
```

---

# 🔐 Proxy de Proteção

Outro uso comum do Proxy é controlar quem pode acessar um objeto.

Imagine um sistema com um serviço administrativo.

```text
Cliente
   |
   v
AdminService
```

Nem todos os usuários deveriam executar determinadas operações.

Por exemplo:

```text
Deletar usuário
Alterar permissões
Acessar dados sensíveis
Modificar configurações
```

Podemos colocar um Proxy entre o cliente e o serviço.

```text
Cliente
   |
   v
ProtectionProxy
   |
   | verifica permissões
   v
AdminService
```

O Proxy pode verificar:

```text
Usuário é administrador?
       |
    +--+--+
    |     |
   Não   Sim
    |     |
    v     v
Bloqueia Executa
```

---

## Exemplo conceitual

```python
class AdminService:

    def delete_user(self):
        print("Usuário removido")


class ProtectionProxy:

    def __init__(self, service, is_admin):
        self.service = service
        self.is_admin = is_admin

    def delete_user(self):

        if self.is_admin:
            self.service.delete_user()
        else:
            print("Acesso negado")
```

O Proxy controla o acesso antes de permitir que a operação chegue ao objeto real.

---

# 🌐 Proxy Remoto

Um Proxy também pode representar um objeto localizado em outra máquina.

Imagine:

```text
Cliente

Computador A
```

e:

```text
Serviço

Servidor B
```

Sem Proxy, o cliente precisaria lidar diretamente com:

```text
Conexões
Protocolos
Endereços IP
Serialização
Envio de dados
Recebimento de respostas
Erros de rede
```

Com um Proxy:

```text
Cliente
   |
   v
RemoteProxy
   |
   |
   | Internet/Rede
   |
   v
Servidor Remoto
   |
   v
Objeto Real
```

Para o cliente:

```python
service.operation()
```

parece uma chamada local.

Mas o Proxy pode internamente:

```text
Transformar chamada em requisição
        |
        v
Enviar pela rede
        |
        v
Servidor executa operação
        |
        v
Receber resposta
        |
        v
Retornar resultado
```

Isso é um exemplo de abstração dos detalhes da rede.

---

# 📝 Proxy de Registro

O Proxy também pode registrar as operações realizadas no objeto.

Por exemplo:

```text
Cliente
   |
   v
LoggingProxy
   |
   | registra operação
   v
Serviço Real
```

Antes de executar uma operação:

```text
Usuário X executou operação Y
```

Depois:

```text
Operação concluída
```

Isso pode ser útil para:

- auditoria;
- debugging;
- monitoramento;
- análise de uso;
- segurança.

---

# 🗃️ Proxy de Cache

Outro uso muito comum é armazenar resultados para evitar operações repetidas.

Imagine uma operação:

```python
get_product(10)
```

que consulta um banco de dados.

Na primeira chamada:

```text
Cliente
   |
   v
CacheProxy
   |
   v
Cache vazio
   |
   v
Banco de Dados
   |
   v
Resultado
   |
   v
Armazenar no cache
```

Na próxima chamada:

```python
get_product(10)
```

o Proxy pode fazer:

```text
Cliente
   |
   v
CacheProxy
   |
   v
Resultado existe no cache?
   |
   v
Sim
   |
   v
Retornar resultado imediatamente
```

Não é necessário consultar o banco novamente.

---

# 🧠 O que é Cache?

**Cache** é uma área utilizada para armazenar temporariamente dados que provavelmente serão utilizados novamente.

A ideia é simples:

> Se um resultado já foi calculado ou buscado anteriormente, talvez não seja necessário fazer todo o trabalho novamente.

Imagine:

```text
Primeira solicitação:

Cliente
   |
   v
Banco de Dados
   |
   v
Resultado
```

Depois:

```text
Resultado é armazenado
```

Na segunda solicitação:

```text
Cliente
   |
   v
Cache
   |
   v
Resultado
```

O acesso normalmente é mais rápido.

---

## Exemplo simples de Cache

Imagine:

```python
get_user(10)
```

Na primeira vez:

```text
Cache não possui usuário 10
```

Então:

```text
Consultar banco
```

Resultado:

```text
Usuário encontrado
```

O Proxy pode armazenar:

```text
Chave:

10

Valor:

Usuário
```

Na próxima chamada:

```python
get_user(10)
```

o Proxy pode verificar:

```text
Usuário 10 está no cache?
```

Se sim:

```text
Retorna diretamente
```

---

# 🧹 Ciclo de vida do Cache

O cache não deve necessariamente armazenar dados para sempre.

Imagine que temos:

```text
Usuário:

João
```

no cache.

Mas depois:

```text
João altera seu nome
```

O dado armazenado anteriormente pode ficar desatualizado.

Por isso, sistemas de cache precisam controlar:

- quando armazenar;
- quando reutilizar;
- quando atualizar;
- quando remover;
- por quanto tempo manter os dados.

Por exemplo:

```text
Cache válido por:

5 minutos
```

Depois desse tempo:

```text
Dados expiram
```

E precisam ser buscados novamente.

---

# 🔍 Referência Inteligente

Outro possível uso do Proxy é monitorar a utilização de um objeto pesado.

Imagine:

```text
Objeto pesado
```

sendo utilizado por vários clientes.

```text
Cliente A ----\
Cliente B ----- > Objeto
Cliente C ----/
```

O Proxy pode acompanhar:

```text
Quantos clientes ainda utilizam o objeto?
```

Quando nenhum cliente precisar mais dele:

```text
0 clientes
   |
   v
Liberar objeto
   |
   v
Liberar recursos
```

Isso pode ajudar a controlar:

- memória;
- conexões;
- arquivos;
- recursos externos.

---

# 🧱 Estrutura geral do Proxy

Podemos representar a estrutura clássica assim:

```text
                   Client

                      |

                      v

              ServiceInterface

                 /          \

                /            \

               v              v

            Proxy          Service

               |

               | possui uma referência

               v

            Service
```

Em uma estrutura mais detalhada:

```text
               +-------------------+
               | ServiceInterface  |
               +-------------------+
               | + operation()     |
               +-------------------+
                       ^
                       |
             +---------+---------+
             |                   |
             v                   v

       +-----------+       +-----------+
       |   Proxy   |       |  Service  |
       +-----------+       +-----------+
       | real      |       |           |
       | Service   |------>| operation |
       +-----------+       +-----------+
```

---

# 🧠 Participantes do Proxy

| Participante    | Exemplo               | Responsabilidade                 |
| --------------- | --------------------- | -------------------------------- |
| **Subject**     | `Image`               | Define a interface comum         |
| **RealSubject** | `HighResolutionImage` | Implementa a lógica real         |
| **Proxy**       | `ImageProxy`          | Controla o acesso ao objeto real |
| **Client**      | `main.py`             | Utiliza a interface              |

---

# 🔄 O Proxy e a transparência

Uma das ideias mais importantes do Proxy é:

> O cliente deve poder utilizar o Proxy da mesma forma que utilizaria o objeto real.

Por exemplo:

```python
image.display()
```

O cliente não precisa saber se `image` é:

```python
HighResolutionImage
```

ou:

```python
ImageProxy
```

Isso acontece porque ambos possuem a mesma interface.

```text
              Image

                |

         +------+------+

         |             |

         v             v

     ImageProxy   HighResolutionImage
```

Ambos implementam:

```text
display()
```

---

# 🆚 Proxy × Objeto Real

Sem Proxy:

```text
Cliente
   |
   v
Objeto Real
```

O cliente possui acesso direto.

Com Proxy:

```text
Cliente
   |
   v
Proxy
   |
   v
Objeto Real
```

O Proxy pode decidir:

```text
Quando criar
Quando carregar
Quem pode acessar
Como registrar
Quando usar cache
Como acessar remotamente
```

---

# 🎯 Quando utilizar Proxy?

O Proxy é especialmente útil quando:

- um objeto é pesado para criar;
- um recurso deve ser carregado apenas quando necessário;
- precisamos controlar permissões de acesso;
- o objeto está localizado em outro servidor;
- precisamos registrar operações;
- queremos utilizar cache;
- precisamos controlar o ciclo de vida de objetos;
- queremos esconder detalhes de acesso a recursos complexos.

---

# ⚠️ Quando não utilizar Proxy?

O Proxy pode adicionar complexidade desnecessária.

Não é recomendado quando:

- o objeto é simples;
- a criação do objeto é barata;
- não existe necessidade de controlar acesso;
- não existe benefício real em utilizar Lazy Loading;
- o comportamento poderia ser implementado diretamente sem aumentar o acoplamento.

Adicionar um Proxy apenas porque o padrão existe pode gerar:

```text
Mais classes

+

Mais abstrações

+

Mais complexidade
```

sem oferecer um benefício real.

---

# ⚖️ Prós e Contras

## 🟢 Prós

- controla o acesso ao objeto real;
- permite Lazy Loading;
- pode reduzir o consumo de memória;
- pode adicionar controle de permissões;
- pode implementar cache;
- pode registrar operações;
- pode representar objetos remotos;
- permite adicionar comportamentos sem alterar diretamente o objeto real;
- o cliente pode utilizar a mesma interface.

---

## 🔴 Contras

- adiciona uma nova classe;
- aumenta o nível de abstração;
- pode tornar o fluxo mais difícil de acompanhar;
- pode introduzir atrasos inesperados;
- pode ser complexidade desnecessária para objetos simples.

---

# 📌 Ideia principal para memorizar

A ideia central do Proxy pode ser resumida assim:

```text
Cliente

   |

   v

Representante

   |

   v

Objeto Real
```

O cliente não conversa necessariamente diretamente com o objeto real.

O Proxy fica entre os dois e pode controlar:

```text
Quando criar

Quando carregar

Quem pode acessar

Como registrar

Como armazenar em cache

Como acessar remotamente
```

Portanto:

> **Proxy = fornecer um objeto representante de outro objeto para controlar o acesso a esse objeto.**

No exemplo das imagens:

```text
Cliente

   |

   v

ImageProxy

   |

   | carrega somente quando necessário

   v

HighResolutionImage
```

A grande vantagem é que o cliente continua utilizando a mesma interface:

```python
image.display()
```

sem precisar saber se está conversando diretamente com o objeto real ou com um Proxy.

---

# 🧠 Resumo final

O Proxy é um padrão estrutural que utiliza um objeto intermediário para representar outro objeto.

Sua principal característica é:

```text
Proxy e Objeto Real

↓

possuem a mesma interface
```

Isso permite que o Proxy seja utilizado como substituto do objeto real.

O Proxy pode então controlar:

- inicialização;
- carregamento;
- acesso;
- permissões;
- cache;
- registros;
- comunicação remota;
- ciclo de vida.

No exemplo das imagens:

```text
Sem Proxy:

Cliente
   |
   v
Imagem pesada
   |
   v
Carregamento imediato
```

Com Proxy:

```text
Cliente
   |
   v
ImageProxy
   |
   v
Imagem pesada somente quando necessário
```

A ideia mais importante para memorizar é:

> **O Proxy representa o objeto real e controla o acesso a ele sem que o cliente precise necessariamente perceber essa intermediação.**
