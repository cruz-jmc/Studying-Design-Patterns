# Adapter

## Objetivo

Permitir que objetos com interfaces incompatíveis
trabalhem juntos.

## Problema

MediaPlayer espera um objeto que possua:

play()

Porém VideoPlayer possui:

play_mp4()

## Solução

Criamos VideoAdapter, que converte:

play()
↓
play_mp4()

## Estrutura

MediaPlayer
↓
VideoAdapter
↓
VideoPlayer
