class DadosAluno:

    def __init__(self):
        self.nome = []
        self.matricula = []
        self.endereco = []

    def inserir(self, p_nome, p_matricula, p_endereco):
        # Inserindo os novos dados no objeto
        self.nome.append(p_nome)
        self.matricula.append(p_matricula)
        self.endereco.append(p_endereco)

    def exibir(self, mensagem):
        print(mensagem)
        qtde = len(self.nome)
        for i in range(qtde):
            print(f"{i+1}) Nome: {self.nome[i]}")
            print(f"   Matricula: {self.matricula[i]}")
            print(f"   Endereço: {self.endereco[i]}\n")
    
    def deletarLista(self):
        if len(self.nome) == 0:
            print("A lista já se encontra vazia.")
        else:
            self.exibir()
            opcao = input("\nTem certeza que deseja excluir todos os alunos (S/N)?")
            if opcao.lower() in ('s', 'sim'):
                self.nome.clear()
                self.matr.clear()
                print("\nOs Alunos foram excluídos.")
                print("Arquivo vazio!")
            elif opcao.lower() in ('n', 'não'):
                print("Os alunos não foram excluídos!")
            else:
                print("Entrada inválida!")

    def deletarItem(self):
        print("Aluno removido com sucesso. ")