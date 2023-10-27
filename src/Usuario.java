import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Usuario {
    private String nomeDeUsuario;
    private String senhaCriptografada;

    public Usuario(String nomeDeUsuario, String senha) {
        this.nomeDeUsuario = nomeDeUsuario;
        this.senhaCriptografada = criptografarSenha(senha);
    }

    public String getNomeDeUsuario() {
        return nomeDeUsuario;
    }

    public String getSenhaCriptografada() {
        return senhaCriptografada;
    }

    public static String criptografarSenha(String senha) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(senha.getBytes());
            StringBuilder hexString = new StringBuilder();

            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }
}