# Import de Classe + os
import os
from Classe import DadosAluno

# Instancia da classe DadosAlunos
da = DadosAluno()

# Função para conseguir limpar o console com o comando do proprio SO
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Função para mostrar o menu ao usuario
def menu():
    x = """-------------------------
|  -  -  M E N U  -  -  |
-------------------------
| Opções:               |
| 1) Inserir aluno      |
| 2) Excluir aluno      |
| 3) Consultar lista    |
| 4) Excluir lista      |
| 5) Sair               |
-------------------------
 """
    print(x)
