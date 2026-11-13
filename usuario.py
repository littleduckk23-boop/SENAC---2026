

class Usuario:
    def __init__(self, matricula, nome):
        self._nome = nome
        self._matricula = matricula

    def obter_codigo(self):
        return self._nome

    def obter_nome(self):
        return self._nome

    def obter_matricula(self):
        return self._matricula

    def alterar_nome(self, novo_nome):
        self._nome = novo_nome
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError

    def limite_emprestimos(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

if __name__ == "__main__":
    # TESTANDO ERROS DE CRIAÇÃO DO OBJETO
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        usuario = Usuario()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM PARÂMETROS INVÁLIDOS")
    try:
        usuario = Usuario("", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM NOME INVÁLIDO")
    try:
        usuario = Usuario("U001", "")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    try:
        # TESTANDO CRIAÇÃO OK
        print("\nTESTANDO A CRIAÇÃO DE UM OBJETO VÁLIDO")
        usuario = Usuario("U001", "Ludovico Monjardim")

        # TESTANDO OS GETTERS
        print("\nGETTERS")
        print(f"Matrícula: {usuario.obter_matricula()}")
        print(f"Nome.....: {usuario.obter_nome()}")

        # TESTANDO O SETTER
        usuario.alterar_nome("Ludovico Monjardim Casagrande")

        print("\nALTEREI OS DADOS")
        print(f"Matrícula: {usuario.obter_matricula()}")
        print(f"Nome.....: {usuario.obter_nome()}")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO O SETTER ERRADO
    print("\nTESTANDO O SETTER ERRADO")
    try:
        usuario.alterar_nome("")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO NOME COM APENAS ESPAÇOS
    print("\nTESTANDO NOME COM APENAS ESPAÇOS")
    try:
        usuario.alterar_nome("   ")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO NOME COM TIPO INVÁLIDO
    print("\nTESTANDO NOME COM TIPO INVÁLIDO")
    try:
        usuario.alterar_nome(123)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO MÉTODO NÃO IMPLEMENTADO
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS")
    try:
        usuario.limite_emprestimos()
    except NotImplementedError as erro:
        print(f"\nErro: {erro}")


    # TESTANDO __str__ NÃO IMPLEMENTADO
    print("\nTESTANDO O MÉTODO __str__")
    try:
        print(usuario)
    except NotImplementedError as erro:
        print(f"\nErro: {erro}")

