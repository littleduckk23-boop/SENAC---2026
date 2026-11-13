from aluno import Aluno
from professor import Professor
from livro import Livro
from usuario import Usuario
class Biblioteca:
    def __init__(self, nome):
       self._nome = nome
       self.livros = []
       self.usuarios = []
       self.emprestimos = []

    def obter_nome(self):
        return self._nome

    def adicionar_livro(self, livro):
       self.livros.append(livro)

    def adicionar_usuario(self, usuario):
       self.usuarios.append(usuario)

    def listar_livros(self):
        return self.livros

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            return("Não há usuários.".center(33))

        for usuario in self.usuarios:
            print(usuario)
    
    def buscar_livro(self, codigo):
        if len(self.livros) == 0:
            return ("Não há livros cadastrados.".center(33))
        for livro in self.livros:
           if livro.obter_codigo().lower() == codigo.lower():
               return livro
        return None



    def buscar_usuario(self, matricula):
       for usuario in self.usuarios:
           if usuario.matricula == matricula:
               return usuario

    def realizar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)
    
    def realizar_devolucao(self, emprestimo):
        self.emprestimos.remove(emprestimo)

    def listar_emprestimos_ativos(self):
        if len(self.emprestimos) == 0:
            print()
            return("Não há empréstimos realizados.".center(33))


    def listar_historico(self):
        if len(self.emprestimos) == 0:
            print()
            return("Não há emprestimos realizados.".center(33))
        
        for emprestimo in self.emprestimos:
            print(emprestimo)


            
if __name__ == "__main__":

    # TESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        biblioteca = Biblioteca()
        print("FALHA: a criação deveria ter sido rejeitada.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CRIAÇÃO COM NOME INVÁLIDO
    print("\nTESTANDO CRIAÇÃO DE OBJETO COM NOME INVÁLIDO")
    try:
        biblioteca = Biblioteca("")
        print("FALHA: nome vazio foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO NOME COM APENAS ESPAÇOS
    print("\nTESTANDO NOME COM APENAS ESPAÇOS")
    try:
        biblioteca = Biblioteca("   ")
        print("FALHA: nome com espaços foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO NOME COM TIPO INVÁLIDO
    print("\nTESTANDO NOME COM TIPO INVÁLIDO")
    try:
        biblioteca = Biblioteca(123)
        print("FALHA: nome numérico foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CRIAÇÃO OK
    print("\nTESTANDO A CRIAÇÃO DE UM OBJETO VÁLIDO")

    try:
        biblioteca = Biblioteca("Biblioteca SENAC")
        print(f"Biblioteca: {biblioteca.obter_nome()}")

        if biblioteca.obter_nome() == "Biblioteca SENAC":
            print("Nome da biblioteca: OK")
        else:
            print("FALHA: nome incorreto.")

        if len(biblioteca.listar_livros()) == 0:
            print("Lista inicial de livros: OK")
        else:
            print("FALHA: lista de livros deveria estar vazia.")

        if len(biblioteca.listar_usuarios()) == 0:
            print("Lista inicial de usuários: OK")
        else:
            print("FALHA: lista de usuários deveria estar vazia.")

        if len(biblioteca.listar_historico()) == 0:
            print("Histórico inicial: OK")
        else:
            print("FALHA: histórico deveria estar vazio.")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # CRIANDO OBJETOS PARA OS TESTES
    print("\nCRIANDO LIVROS E USUÁRIOS PARA OS TESTES")

    try:
        aluno = Aluno("A001", "Ludovico Monjardim")
        professor = Professor("P001", "Maria da Silva")

        livros = []

        for numero in range(1, 13):

            codigo = f"L{numero:03d}"
            titulo = f"Livro de Teste {numero}"

            livro = Livro(codigo, titulo, "Autor Exemplo", 2026)
            livros.append(livro)

        print(f"Livros criados.....: {len(livros)}")
        print(f"Aluno criado.......: {aluno}")
        print(f"Professor criado...: {professor}")

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO CADASTRO DE LIVRO INVÁLIDO
    print("\nTESTANDO CADASTRO DE LIVRO INVÁLIDO")
    try:
        biblioteca.adicionar_livro("L001")
        print("FALHA: livro inválido foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CADASTRO DE LIVROS VÁLIDOS
    print("\nTESTANDO CADASTRO DE LIVROS VÁLIDOS")

    try:
        for livro in livros:
            biblioteca.adicionar_livro(livro)

        quantidade = len(biblioteca.listar_livros())
        print(f"Livros cadastrados: {quantidade}")

        if quantidade == 12:
            print("Cadastro dos livros: OK")
        else:
            print("FALHA: quantidade de livros incorreta.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO CADASTRO DE LIVRO DUPLICADO
    print("\nTESTANDO CADASTRO DE LIVRO DUPLICADO")

    try:
        livro_duplicado = Livro("L001", "Outro Título", "Outro Autor", 2025)

        biblioteca.adicionar_livro(livro_duplicado)

        print("FALHA: código duplicado foi aceito.")

    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CADASTRO DE USUÁRIO INVÁLIDO
    print("\nTESTANDO CADASTRO DE USUÁRIO INVÁLIDO")

    try:
        biblioteca.adicionar_usuario("Ludovico")
        print("FALHA: usuário inválido foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CADASTRO DIRETO DA CLASSE USUARIO
    print("\nTESTANDO CADASTRO DIRETO DA CLASSE USUARIO")

    try:
        usuario_base = Usuario("U001", "Usuário Genérico")
        biblioteca.adicionar_usuario(usuario_base)
        print("FALHA: usuário da classe-base foi aceito.")

    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO CADASTRO DE USUÁRIOS VÁLIDOS
    print("\nTESTANDO CADASTRO DE USUÁRIOS VÁLIDOS")

    try:
        biblioteca.adicionar_usuario(aluno)
        biblioteca.adicionar_usuario(professor)
        usuarios = biblioteca.listar_usuarios()

        for usuario in usuarios:
            print(usuario)

        if len(usuarios) == 2:
            print("Cadastro de usuários: OK")
        else:
            print("FALHA: quantidade de usuários incorreta.")
            raise SystemExit(1)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO MATRÍCULA DUPLICADA
    print("\nTESTANDO CADASTRO COM MATRÍCULA DUPLICADA")

    try:
        outro_aluno = Aluno("A001", "Outro Aluno")
        biblioteca.adicionar_usuario(outro_aluno)
        print("FALHA: matrícula duplicada foi aceita.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO BUSCA DE LIVRO EXISTENTE
    print("\nTESTANDO BUSCA DE LIVRO EXISTENTE")

    livro_encontrado = biblioteca.buscar_livro("L001")

    if livro_encontrado is not None:
        print(livro_encontrado)

        if livro_encontrado is livros[0]:
            print("Busca de livro: OK")
        else:
            print("FALHA: objeto encontrado incorreto.")
    else:
        print("FALHA: livro cadastrado não encontrado.")


    # TESTANDO BUSCA DE LIVRO INEXISTENTE
    print("\nTESTANDO BUSCA DE LIVRO INEXISTENTE")

    resultado = biblioteca.buscar_livro("L999")

    if resultado is None:
        print("Busca de livro inexistente: OK")
    else:
        print("FALHA: livro inexistente foi encontrado.")


    # TESTANDO BUSCA DE USUÁRIO EXISTENTE
    print("\nTESTANDO BUSCA DE USUÁRIO EXISTENTE")
    usuario_encontrado = biblioteca.buscar_usuario("A001")
    if usuario_encontrado is aluno:
        print(usuario_encontrado)
        print("Busca de usuário: OK")
    else:
        print("FALHA: usuário incorreto ou não encontrado.")


    # TESTANDO BUSCA DE USUÁRIO INEXISTENTE
    print("\nTESTANDO BUSCA DE USUÁRIO INEXISTENTE")
    resultado = biblioteca.buscar_usuario("A999")

    if resultado is None:
        print("Busca de usuário inexistente: OK")
    else:
        print("FALHA: usuário inexistente foi encontrado.")


    # TESTANDO EMPRÉSTIMO DE LIVRO INEXISTENTE
    print("\nTESTANDO EMPRÉSTIMO DE LIVRO INEXISTENTE")

    try:
        biblioteca.realizar_emprestimo("L999", "A001")
        print("FALHA: empréstimo inválido foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO EMPRÉSTIMO PARA USUÁRIO INEXISTENTE
    print("\nTESTANDO EMPRÉSTIMO PARA USUÁRIO INEXISTENTE")

    try:
        biblioteca.realizar_emprestimo("L001", "A999")
        print("FALHA: usuário inexistente foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")

    if livros[0].esta_disponivel():
        print("Livro permaneceu disponível: OK")
    else:
        print("FALHA: livro ficou indisponível indevidamente.")
        raise SystemExit(1)


    # TESTANDO EMPRÉSTIMO VÁLIDO PARA ALUNO
    print("\nTESTANDO EMPRÉSTIMO VÁLIDO PARA ALUNO")

    try:
        emprestimo_aluno = biblioteca.realizar_emprestimo("L001", "A001")
        print(emprestimo_aluno)

        if emprestimo_aluno.esta_ativo():
            print("Empréstimo ativo: OK")
        else:
            print("FALHA: empréstimo não está ativo.")
            raise SystemExit(1)

        if not livros[0].esta_disponivel():
            print("Livro indisponível após empréstimo: OK")
        else:
            print("FALHA: livro continua disponível.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO EMPRÉSTIMO DUPLICADO
    print("\nTESTANDO EMPRÉSTIMO DE LIVRO INDISPONÍVEL")

    try:
        biblioteca.realizar_emprestimo("L001", "P001")
        print("FALHA: livro já emprestado foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO LIMITE DE EMPRÉSTIMOS DO ALUNO
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS DO ALUNO")

    try:
        biblioteca.realizar_emprestimo("L002", "A001")
        biblioteca.realizar_emprestimo("L003", "A001")

        ativos_aluno = biblioteca.emprestimos_ativos_do_usuario(aluno)
        quantidade = len(ativos_aluno)

        print(f"Limite permitido: {aluno.limite_emprestimos()}")
        print(f"Empréstimos ativos: {quantidade}")

        if quantidade == 3:
            print("Limite do aluno atingido: OK")
        else:
            print("FALHA: quantidade incorreta.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO EMPRÉSTIMO ACIMA DO LIMITE DO ALUNO
    print("\nTESTANDO QUARTO EMPRÉSTIMO DO ALUNO")

    try:
        biblioteca.realizar_emprestimo("L004", "A001")
        print("FALHA: empréstimo acima do limite foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")

    if livros[3].esta_disponivel():
        print("Livro permaneceu disponível: OK")
    else:
        print("FALHA: livro foi emprestado indevidamente.")


    # TESTANDO LIMITE DE EMPRÉSTIMOS DO PROFESSOR
    print("\nTESTANDO LIMITE DE EMPRÉSTIMOS DO PROFESSOR")

    try:
        for numero in range(5, 10):
            codigo = f"L{numero:03d}"
            biblioteca.realizar_emprestimo(codigo, "P001")

        ativos_professor = biblioteca.emprestimos_ativos_do_usuario(professor)
        quantidade = len(ativos_professor)

        print(f"Limite permitido: {professor.limite_emprestimos()}")
        print(f"Empréstimos ativos: {quantidade}")

        if quantidade == 5:
            print("Limite do professor atingido: OK")
        else:
            print("FALHA: quantidade incorreta.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO EMPRÉSTIMO ACIMA DO LIMITE DO PROFESSOR
    print("\nTESTANDO SEXTO EMPRÉSTIMO DO PROFESSOR")

    try:
        biblioteca.realizar_emprestimo("L010", "P001")
        print("FALHA: empréstimo acima do limite foi aceito.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")

    if livros[9].esta_disponivel():
        print("Livro permaneceu disponível: OK")
    else:
        print("FALHA: livro foi emprestado indevidamente.")


    # TESTANDO LISTAGEM DE EMPRÉSTIMOS ATIVOS
    print("\nTESTANDO LISTAGEM DE EMPRÉSTIMOS ATIVOS")
    ativos = biblioteca.listar_emprestimos_ativos()

    for emprestimo in ativos:
        print(emprestimo)

    print(f"\nTotal de empréstimos ativos: {len(ativos)}")

    if len(ativos) == 8:
        print("Total de empréstimos ativos: OK")
    else:
        print("FALHA: total incorreto.")
        raise SystemExit(1)


    # TESTANDO DEVOLUÇÃO DE LIVRO INEXISTENTE
    print("\nTESTANDO DEVOLUÇÃO DE LIVRO INEXISTENTE")

    try:
        biblioteca.realizar_devolucao("L999")
        print("FALHA: devolução inválida foi aceita.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO DEVOLUÇÃO SEM EMPRÉSTIMO ATIVO
    print("\nTESTANDO DEVOLUÇÃO SEM EMPRÉSTIMO ATIVO")

    try:
        biblioteca.realizar_devolucao("L011")
        print("FALHA: devolução sem empréstimo foi aceita.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO DEVOLUÇÃO VÁLIDA
    print("\nTESTANDO DEVOLUÇÃO VÁLIDA")

    try:
        devolucao = biblioteca.realizar_devolucao("L001")

        print(devolucao)
        print(f"Livro disponível: {livros[0].esta_disponivel()}")
        print(f"Empréstimo ativo: {devolucao.esta_ativo()}")
        print(f"Data devolução..: {devolucao.obter_data_devolucao()}")

        if livros[0].esta_disponivel():
            print("Disponibilidade do livro: OK")
        else:
            print("FALHA: livro continua indisponível.")
            raise SystemExit(1)

        if not devolucao.esta_ativo():
            print("Encerramento do empréstimo: OK")
        else:
            print("FALHA: empréstimo continua ativo.")
            raise SystemExit(1)

        if devolucao.obter_data_devolucao() is not None:
            print("Data de devolução registrada: OK")
        else:
            print("FALHA: data de devolução ausente.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO DEVOLUÇÃO DUPLICADA
    print("\nTESTANDO DEVOLUÇÃO DUPLICADA")

    try:
        biblioteca.realizar_devolucao("L001")
        print("FALHA: devolução duplicada foi aceita.")
    except (ValueError, TypeError) as erro:
        print(f"\nErro esperado: {erro}")


    # TESTANDO NOVO EMPRÉSTIMO APÓS DEVOLUÇÃO
    print("\nTESTANDO NOVO EMPRÉSTIMO APÓS DEVOLUÇÃO")

    try:
        novo_emprestimo = biblioteca.realizar_emprestimo("L004", "A001")
        print(novo_emprestimo)
        ativos_aluno = biblioteca.emprestimos_ativos_do_usuario(aluno)

        if novo_emprestimo.esta_ativo() and len(ativos_aluno) == 3:
            print("Novo empréstimo após liberar uma vaga: OK")
        else:
            print("FALHA: empréstimo ou contagem incorreta.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO REEMPRÉSTIMO DO LIVRO DEVOLVIDO
    print("\nTESTANDO REEMPRÉSTIMO DE LIVRO DEVOLVIDO")

    try:
        # Libera uma vaga do professor.
        biblioteca.realizar_devolucao("L005")

        # Empresta ao professor o livro devolvido pelo aluno.
        novo_emprestimo = biblioteca.realizar_emprestimo("L001", "P001")
        print(novo_emprestimo)

        if novo_emprestimo.esta_ativo():
            print("Novo empréstimo ativo: OK")
        else:
            print("FALHA: empréstimo não está ativo.")
            raise SystemExit(1)

        if not livros[0].esta_disponivel():
            print("Livro novamente indisponível: OK")
        else:
            print("FALHA: livro permanece disponível.")
            raise SystemExit(1)

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")
        raise SystemExit(1)


    # TESTANDO LISTAGEM DE LIVROS
    print("\nTESTANDO LISTAGEM DE LIVROS")
    livros_cadastrados = biblioteca.listar_livros()

    for livro in livros_cadastrados:
        print(livro)

    if len(livros_cadastrados) == 12:
        print("\nListagem de livros: OK")
    else:
        print("\nFALHA: quantidade de livros incorreta.")


    # TESTANDO LISTAGEM DE USUÁRIOS
    print("\nTESTANDO LISTAGEM DE USUÁRIOS")
    usuarios_cadastrados = biblioteca.listar_usuarios()

    for usuario in usuarios_cadastrados:
        print(usuario)

    if len(usuarios_cadastrados) == 2:
        print("\nListagem de usuários: OK")
    else:
        print("\nFALHA: quantidade de usuários incorreta.")


    # TESTANDO HISTÓRICO DE EMPRÉSTIMOS
    print("\nTESTANDO HISTÓRICO DE EMPRÉSTIMOS")
    historico = biblioteca.listar_historico()

    for emprestimo in historico:
        print(emprestimo)

    print(f"\nTotal de registros: {len(historico)}")

    if len(historico) == 10:
        print("Histórico de empréstimos: OK")
    else:
        print("FALHA: total do histórico incorreto.")


    # TESTANDO CONTAGEM FINAL DOS EMPRÉSTIMOS
    print("\nTESTANDO CONTAGEM FINAL DOS EMPRÉSTIMOS")
    ativos = biblioteca.listar_emprestimos_ativos()
    encerrados = []

    for emprestimo in historico:
        if not emprestimo.esta_ativo():
            encerrados.append(emprestimo)

    print(f"Empréstimos ativos....: {len(ativos)}")
    print(f"Empréstimos encerrados: {len(encerrados)}")
    print(f"Total no histórico....: {len(historico)}")

    if len(ativos) == 8 and len(encerrados) == 2:
        print("\nVERIFICAÇÕES FINAIS: OK")
    else:
        print("\nFALHA NAS VERIFICAÇÕES FINAIS")