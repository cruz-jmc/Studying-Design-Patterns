package Behavioral.Strategy.anotherExample.context;

import Behavioral.Strategy.anotherExample.strategy.EstrategiaPagamento;

public class CarrinhoDeCompras {

    private EstrategiaPagamento estrategia;

    public void setEstrategia(EstrategiaPagamento estrategia) {
        this.estrategia = estrategia;
    }

    public void checkout(double total) {
        if (estrategia == null) {
            throw new IllegalStateException(
                    "Nenhuma estratégia de pagamento foi definida."
            );
        }

        estrategia.processarPagamento(total);
    }

}