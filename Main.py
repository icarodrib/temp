# Biblioteca para guardar todas as coisas essenciais para esse codigo funcionar.
from essenciais import *
# Inicio do Programa
clear()
menu()
while True:
    # Entrada da opção de operação do usuario
    opcao = input("Digite a opção que deseja utilizar: ")
    opcao = opcao.lower()
    # Operação de inserção dos dados do aluno
    if (opcao == '1' or opcao == 'inserir aluno'):
        clear()
        # Inserção dos dados por parte do usuario
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matricula do aluno: ")
        endereco = input("Digite o endereço do aluno: ")
        clear()
        while True:
            # Confirmação por parte do usuario que os dados estão corretos
            print("Você tem certeza que deseja inserir os dados abaixo?\n")
            print(f"Nome: {nome}",f"   Matricula: {matricula}",f"   Endereço: {endereco}\n")
            opcao = input("1) Sim\n2) Não\n\nDigite a opção que deseja utilizar: ")
            opcao = opcao.lower()
            # Confirmado
            if (opcao == '1' or opcao == "sim"):
                # Alocação dos dados para o objeto
                da.inserir(nome,matricula,endereco)
                clear()
                print("* Dados inseridos com sucesso.")
                break
            # Cancelado
            elif (opcao == '2' or opcao =='nao' or opcao == 'não'):
                # Cancelamento de alocação dos dados
                clear()
                print ("* Operação cancelada.")
                break
            # Caso não escolha nenhuma das duas fica no loop
            else:
                clear()
                print("Opção digitada invalida.\nPor favor digite uma opção valida.\n")
        menu()
    # Parte de consulta de dados
    elif (opcao == '3' or opcao == 'consultar lista'):
        clear()
        # Checagem se a lista está vazia
        qtde = len(da.nome)
        if (qtde == 0):
            print("* A lista está vazia no momento.")
        # Consulta dos dados cadastrados 
        elif (qtde == 1):
            da.exibir("Aluno cadastrado: \n")
            print("\nAperte a tecla 'Enter' para retornar ao menu")
            while True:
                opcao = input()
                if (opcao != "" or opcao == ""):
                    clear()
                    break
        else:
            da.exibir(f"{qtde} Alunos cadastrados: \n")
            print("\nAperte a tecla 'Enter' para retornar ao menu")
            while True:
                opcao = input()
                if (opcao != "" or opcao == ""):
                    clear()
                    break
        menu()
    elif (opcao == '5' or opcao == 'sair'):
        clear()
        break
    else:
        clear()
        print("Opção digita não é valida, por favor tente novamente...")
        menu()
print("Programa finalizado com sucesso.")