package Behavioral.Strategy.anotherExample;

import Behavioral.Strategy.anotherExample.context.CarrinhoDeCompras;
import Behavioral.Strategy.anotherExample.strategy.PagamentoCartao;
import Behavioral.Strategy.anotherExample.strategy.PagamentoPix;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        CarrinhoDeCompras carrinho = new CarrinhoDeCompras();

        double valorCompra = 150.00;

        System.out.println("===== LOJA VIRTUAL =====");
        System.out.printf("Total da compra: R$ %.2f%n", valorCompra);

        System.out.println("\nEscolha a forma de pagamento:");
        System.out.println("1 - Pix");
        System.out.println("2 - Cartão");
        System.out.print("Opção: ");

        String opcao = scanner.nextLine();

        switch (opcao) {
            case "1":
                carrinho.setEstrategia(new PagamentoPix());
                break;

            case "2":
                carrinho.setEstrategia(new PagamentoCartao());
                break;

            default:
                System.out.println("Opção inválida!");
                return;
        }

        System.out.println("\nProcessando pagamento...");
        carrinho.checkout(valorCompra);

        System.out.println("Compra finalizada!");

    }
}