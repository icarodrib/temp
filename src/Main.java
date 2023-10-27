import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Autenticacao autenticacao = new Autenticacao();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            limparTela();

            System.out.println("1. Login");
            System.out.println("2. Registrar novo usuario");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opçao: ");
            String escolha = scanner.next();
            scanner.nextLine(); 

            switch (escolha) {
                case "1":
                    System.out.print("Digite o nome de usuário: ");
                    String nomeDeUsuario = scanner.nextLine();
                    System.out.print("Digite a senha: ");
                    String senha = scanner.nextLine();

                    if (autenticacao.autenticar(nomeDeUsuario, senha)) {
                        System.out.println("Login bem-sucedido!");
                    } else {
                        System.out.println("Login falhou. Nome de usuário ou senha incorretos.");
                    }
                    pausar();
                    break;
                case "2":
                    System.out.print("Digite o novo nome de usuário: ");
                    String novoNomeDeUsuario = scanner.nextLine();
                    System.out.print("Digite a nova senha: ");
                    String novaSenha = scanner.nextLine();

                    autenticacao.adicionarUsuario(novoNomeDeUsuario, novaSenha);

                    System.out.println("Novo usuário registrado com sucesso!");
                    pausar();
                    break;
                case "3":
                    System.out.println("Saindo do programa. Até mais!");
                    pausar();
                    scanner.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    pausar();
            }
        }
    }

    private static void limparTela() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private static void pausar() {
        System.out.println("Pressione Enter para continuar...");
        try {
            System.in.read();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}