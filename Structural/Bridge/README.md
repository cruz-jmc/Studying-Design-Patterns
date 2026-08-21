# Bridge

## Objetivo

Separar uma abstração da sua implementação para que ambas possam variar independentemente.

## Problema

Temos duas dimensões diferentes no sistema:

- Formas geométricas (`Shape`)
- Cores (`Color`)

As formas disponíveis são:

- `Circle`
- `Square`

E as cores disponíveis são:

- `Red`
- `Blue`
- `Green`

Uma abordagem utilizando apenas herança poderia gerar várias classes combinando forma e cor:

```text
CircleRed
CircleBlue
CircleGreen

SquareRed
SquareBlue
SquareGreen
```
