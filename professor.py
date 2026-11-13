from usuario import Usuario

class Professor(Usuario):

    def limite_emprestimos(self):
        return 5
    
    def __str__(self):

       return f"[{self.obter_matricula()} - PROFESSOR], {self.obter_nome()} - {self.obter_matricula()} (Limite - { self.limite_emprestimos()})" 

if __name__ == "__main__":

    # TESTANDO ERROS DE CRIAÇÃO DO OBJETO
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        professor = Professor()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    print("\nTESTANDO CRIAÇÃO DE OBJETO COM PARÂMETROS INVÁLIDOS")
    try:
        professor = Professor("", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    print("\nTESTANDO CRIAÇÃO DE OBJETO COM MATRÍCULA INVÁLIDA")
    try:
        professor = Professor("", "Ludovico")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    print("\nTESTANDO CRIAÇÃO DE OBJETO COM NOME INVÁLIDO")
    try:
        professor = Professor("A001", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    try:
        # TESTANDO CRIAÇÃO OK
        print("\nTESTANDO A CRIAÇÃO DE UM OBJETO VÁLIDO")
        professor = Professor("A001", "Ludovico Monjardim")

        # TESTANDO OS GETTERS HERDADOS
        print("\nGETTERS")
        print(f"Matrícula: {professor.obter_matricula()}")
        print(f"Nome.....: {professor.obter_nome()}")

        # TESTANDO O SETTER HERDADO
        professor.alterar_nome("Ludovico Monjardim Casagrande")

        print("\nALTEREI OS DADOS")
        print(f"Matrícula: {professor.obter_matricula()}")
        print(f"Nome.....: {professor.obter_nome()}")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    # TESTANDO O SETTER COM TEXTO VAZIO
    print("\nTESTANDO O SETTER COM TEXTO VAZIO")
    try:
        professor.alterar_nome("")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    # TESTANDO NOME COM APENAS ESPAÇOS
    print("\nTESTANDO NOME COM APENAS ESPAÇOS")
    try:
        professor.alterar_nome("   ")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    # TESTANDO NOME COM TIPO INVÁLIDO
    print("\nTESTANDO NOME COM TIPO INVÁLIDO")
    try:
        professor.alterar_nome(123)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    # TESTANDO LIMITE DE EMPRÉSTIMOS
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS")
    print(f"Limite: {professor.limite_emprestimos()}")

    # TESTANDO O MÉTODO __str__
    print("\nTESTANDO O MÉTODO __str__")
    print(professor)