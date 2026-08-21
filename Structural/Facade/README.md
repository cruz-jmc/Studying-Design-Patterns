# Facade

## 📌 Objetivo

O **Facade** é um Design Pattern estrutural utilizado para **fornecer uma interface unificada e simplificada para um conjunto de interfaces de um subsistema**.

A ideia principal é esconder a complexidade interna de um sistema atrás de uma classe que oferece uma interface mais simples para o cliente.

Em outras palavras:

> **Facade cria um ponto de entrada simples para utilizar um subsistema complexo.**

O cliente não precisa conhecer todas as classes internas nem saber a ordem em que suas operações precisam ser executadas.

---

## ❗ Problema

Imagine que estamos desenvolvendo uma aplicação capaz de **converter arquivos de vídeo**.

Para realizar uma conversão, o sistema precisa executar diversas operações diferentes:

1. Abrir o arquivo de vídeo;
2. Identificar o codec utilizado;
3. Escolher o codec de destino;
4. Ler os dados do vídeo;
5. Converter os dados;
6. Processar o áudio;
7. Retornar o vídeo convertido.

Cada uma dessas responsabilidades pode estar representada por uma classe diferente.

Por exemplo:

```text
VideoFile
CodecFactory
BitrateReader
AudioMixer
OggCompressionCodec
MPEG4CompressionCodec
```
