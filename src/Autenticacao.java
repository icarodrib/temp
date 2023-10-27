import java.util.HashSet;
import java.util.Set;

public class Autenticacao {
    private Set<Usuario> usuarios;

    public Autenticacao() {
        usuarios = new HashSet<>();
    }

    public boolean adicionarUsuario(String nomeDeUsuario, String senha) {
        Usuario novoUsuario = new Usuario(nomeDeUsuario, senha);
        if (usuarios.contains(novoUsuario)) {
            return false; // Nome de usuário já existe
        }
        usuarios.add(novoUsuario);
        return true; // Usuário registrado com sucesso
    }

    public boolean autenticar(String nomeDeUsuario, String senha) {
        String senhaCriptografada = Usuario.criptografarSenha(senha);
        for (Usuario usuario : usuarios) {
            if (usuario.getNomeDeUsuario().equals(nomeDeUsuario) && usuario.getSenhaCriptografada().equals(senhaCriptografada)) {
                return true;
            }
        }
        return false;
    }
}