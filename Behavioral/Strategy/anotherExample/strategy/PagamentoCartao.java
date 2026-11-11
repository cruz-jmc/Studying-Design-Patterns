package Behavioral.Strategy.anotherExample.strategy;

public class PagamentoCartao implements EstrategiaPagamento {

    @Override
    public void processarPagamento(double valor) {
        System.out.println("Pagamento via cartão: R$ " + valor);
    }
}