from datetime import datetime, date
from zoneinfo import ZoneInfo
from livro import Livro
from biblioteca import Aluno
from professor import Professor

class Emprestimo:
    def __init__(self, livro, usuario, ativo=None):
        zona = ZoneInfo("America/Sao_Paulo")
        hoje = datetime.now(zona)
        self._livro = livro
        self._usuario = usuario
        self._data_emprestimo = hoje.strftime("%d/%m/%Y | %H:%M")
        self._data_devolucao = hoje.strftime("%d/%m/%Y | %H:%M")
        self._ativo = True

    # abrir um .txt só
    arquivo = open("emprestimos.txt", "w", enconding="utf-8")
    arquivo.close()

    def obter_livro(self):
        return self._livro

    def obter_usuario(self):
        return self._usuario

    def obter_data_emprestimo(self):
        return self._data_emprestimo

    def obter_data_devolucao(self):
        return self._data_devolucao

    def esta_ativo(self):
        return self._ativo 

    def encerrar(self):
        self._ativo = False

    def __str__(self):
        status = "Ativo" if self._ativo else "Não ativo"
        if self._ativo: 
            return f"Livro: {self.obter_livro()}\nUsuário: {self.obter_usuario()}\nData emprétimo: {self.obter_data_emprestimo()}\nData devolução: {self.obter_data_devolucao()}\nAtivo: {status}" 

        return f"{self.obter_livro()}\n{self.obter_usuario()}\n{self.obter_data_emprestimo()}\n{self.obter_data_devolucao()}\n{status}"



if __name__ == "__main__":

    # TESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        emprestimo = Emprestimo()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO CRIAÇÃO COM PARÂMETROS INVÁLIDOS
    print("\nTESTANDO CRIAÇÃO DE OBJETO COM PARÂMETROS INVÁLIDOS")
    try:
        emprestimo = Emprestimo("", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # CRIANDO OBJETOS VÁLIDOS PARA OS TESTES
    print("\nCRIANDO LIVRO E USUÁRIOS VÁLIDOS")

    try:
        livro = Livro("L001", "Dom Casmurro", "Machado de Assis", 1899)
        aluno = Aluno("A001", "Ludovico Monjardim")
        professor = Professor("P001", "Maria da Silva")

        print("\nLivro criado:")
        print(livro)

        print("\nAluno criado:")
        print(aluno)

        print("\nProfessor criado:")
        print(professor)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO CRIAÇÃO COM LIVRO INVÁLIDO
    print("\nTESTANDO CRIAÇÃO COM LIVRO INVÁLIDO")
    try:
        emprestimo = Emprestimo("L001", aluno)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO CRIAÇÃO COM USUÁRIO INVÁLIDO
    print("\nTESTANDO CRIAÇÃO COM USUÁRIO INVÁLIDO")
    try:
        emprestimo = Emprestimo(livro, "Ludovico")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO CRIAÇÃO OK
    print("\nTESTANDO A CRIAÇÃO DE UM EMPRÉSTIMO VÁLIDO")

    try:
        emprestimo = Emprestimo(livro, aluno)
        print(emprestimo)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO OS GETTERS
    print("\nGETTERS")
    print(f"Livro...........: {emprestimo.obter_livro().obter_titulo()}")
    print(f"Usuário.........: {emprestimo.obter_usuario().obter_nome()}")
    print(f"Data empréstimo.: {emprestimo.obter_data_emprestimo()}")
    print(f"Data devolução..: {emprestimo.obter_data_devolucao()}")
    print(f"Ativo...........: {emprestimo.esta_ativo()}")


    # TESTANDO LIMITE DE EMPRÉSTIMOS DO USUÁRIO
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS")
    print(f"Aluno....: {aluno.limite_emprestimos()}")
    print(f"Professor: {professor.limite_emprestimos()}")


    # TESTANDO ENCERRAMENTO DO EMPRÉSTIMO
    print("\nTESTANDO ENCERRAMENTO DO EMPRÉSTIMO")

    try:
        emprestimo.encerrar()

        print("\nEMPRÉSTIMO ENCERRADO")
        print(f"Data devolução..: {emprestimo.obter_data_devolucao()}")
        print(f"Ativo...........: {emprestimo.esta_ativo()}")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO ENCERRAMENTO DE EMPRÉSTIMO JÁ ENCERRADO
    print("\nTESTANDO ENCERRAMENTO DE EMPRÉSTIMO JÁ ENCERRADO")

    try:
        emprestimo.encerrar()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO O MÉTODO __str__
    print("\nTESTANDO O MÉTODO __str__")
    print(emprestimo)


    # TESTANDO EMPRÉSTIMO PARA PROFESSOR
    print("\nTESTANDO EMPRÉSTIMO PARA PROFESSOR")

    try:
        emprestimo_professor = Emprestimo(livro, professor)
        print(emprestimo_professor)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")