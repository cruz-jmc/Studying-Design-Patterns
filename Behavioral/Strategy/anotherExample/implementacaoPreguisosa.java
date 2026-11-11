package Behavioral.Strategy.anotherExample;

public class implementacaoPreguisosa {
    public void checkout(double valor, String tipoPagamento) {

        if (tipoPagamento.equals("PIX")) {
            System.out.println("Pagamento via Pix: R$ " + valor);
        } else if (tipoPagamento.equals("CARTAO")) {
            System.out.println("Pagamento via cartão: R$ " + valor);
        }
    }
}
// Desrespeita o princípio OCP do SOLID pois apesar de funcionar, ele apresenta algumas limitações:
//- Acoplamento: o carrinho conhece diretamente todos os tipos de pagamento.
//- Manutenção: adicionar um novo método exige modificar a classe CarrinhoDeCompras.
//- Responsabilidade: a classe acumula o gerenciamento da compra e as regras de pagamento.
//- Escalabilidade: conforme novos pagamentos são adicionados, os condicionais aumentam.