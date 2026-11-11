package Behavioral.Strategy.anotherExample.strategy;

public class PagamentoPix implements EstrategiaPagamento {
    @Override
    public void processarPagamento(double valor) {
        System.out.println("Pagamento via Pix: R$ " + valor);
    }
}
