from usuario import Usuario

class Aluno(Usuario):

    def limite_emprestimos(self):
        return 3
    
    def __str__(self):

       return f"[{self.obter_matricula()} - ALUNO], {self.obter_nome()} - {self.obter_matricula()} (Limite - { self.limite_emprestimos()})"  

if __name__ == "__main__":

    # TESTANDO ERROS DE CRIAÇÃO DO OBJETO
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        aluno = Aluno()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM PARÂMETROS INVÁLIDOS")
    try:
        aluno = Aluno("", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM MATRÍCULA INVÁLIDA")
    try:
        aluno = Aluno("", "Ludovico")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM NOME INVÁLIDO")
    try:
        aluno = Aluno("A001", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    try:
        # TESTANDO CRIAÇÃO OK
        print("\nTESTANDO A CRIAÇÃO DE UM OBJETO VÁLIDO")
        aluno = Aluno("A001", "Ludovico Monjardim")

        # TESTANDO OS GETTERS HERDADOS
        print("\nGETTERS")
        print(f"Matrícula: {aluno.obter_matricula()}")
        print(f"Nome.....: {aluno.obter_nome()}")

        # TESTANDO O SETTER HERDADO
        aluno.alterar_nome("Ludovico Monjardim Casagrande")

        print("\nALTEREI OS DADOS")
        print(f"Matrícula: {aluno.obter_matricula()}")
        print(f"Nome.....: {aluno.obter_nome()}")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO O SETTER COM TEXTO VAZIO
    print("\nTESTANDO O SETTER COM TEXTO VAZIO")
    try:
        aluno.alterar_nome("")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO NOME COM APENAS ESPAÇOS
    print("\nTESTANDO NOME COM APENAS ESPAÇOS")
    try:
        aluno.alterar_nome("   ")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO NOME COM TIPO INVÁLIDO
    print("\nTESTANDO NOME COM TIPO INVÁLIDO")
    try:
        aluno.alterar_nome(123)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO LIMITE DE EMPRÉSTIMOS
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS")
    print(f"Limite: {aluno.limite_emprestimos()}")


    # TESTANDO O MÉTODO __str__
    print("\nTESTANDO O MÉTODO __str__")
    print(aluno)


        


