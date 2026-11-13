from biblioteca import Biblioteca
from aluno import Aluno
from professor import Professor
from usuario import Usuario
from livro import Livro
from emprestimo import Emprestimo

# MENU INTERATIVO
biblioteca = Biblioteca("Biblioteca de Alexandria")
def menu():
    print("""
=================================
-- CADASTRAR --------------------
1 - Livro
2 - Usuário
--- REGISTRAR -------------------
3 - Empréstimo
4 - Devolução
--- LISTAR ----------------------
5 - Livros
6 - Usuários
7 - Empréstimos ativos
--- FUNCIONALIDADES -------------
8 - Popular dados de exemplo       
(opcional, mas recomendável)
=================================
0 - Sair
=================================
""")

    opcao = input("Escolha uma opção: ").strip()
    return opcao


def cadastrar_usuario():
    continuar = True
    while continuar:
        print("Digite [0] para voltar ao menu...")
        while continuar:
            nome = input("Informe o nome do usuário: ").strip()
            if nome == "0":
                continuar = False
                continue
            if len(nome) == 0:
                print("Nome é obrigatório. Por favor preencha-o.".center(33))
                print()
                continue 
            if not nome.isalpha():
                    print("\n", "O seu nome precisa ter caracteres do alfabeto.".center(33))
                    continue
            break

        while continuar:
            matricula = input("O usuário é aluno ou professor? [A/P]: ").strip().upper()
            if matricula == "0":
                continuar = False
                continue
            if len(matricula) == 0:
                print("A matrícula é obrigatória. Por favor, preencha-a.")
                continue

            if matricula.upper() == "A":
                usuario = Aluno(nome, matricula)
                biblioteca.adicionar_usuario(usuario)
                print()
                print("Usuário cadastrado com sucesso.".center(33))
                print()
                return usuario

            if matricula.upper() == "P":
                usuario = Professor(matricula, nome)
                biblioteca.adicionar_usuario(usuario)
                return usuario
            
            if matricula not in "PA":
                print("A escolha deve ser P[PROFESSOR] OU A[ALUNO]. Por favor, tente novamente.".center(33))
                continue
            break

    if continuar:
        print()
        print("Usuário cadastrado com sucesso.".center(33))
        print()


def cadastrar_livro():
    while True:
        print("Digite [0] para voltar ao menu...")

        titulo = input("Informe o título do livro: ").strip()
        if titulo == "0":
           break
        if not titulo:
            print("A porra do livro precisa ter um título, animal.".center(33))
            print()
            continue

        codigo = input("Informe o código do livro: ").strip()
        if not codigo:
            print("A porra do livro precisa ter um código, animal.".center(33))
            print()
            continue

        verificacao = biblioteca.buscar_livro(codigo)
        if not verificacao:
            print("Livro já cadastrado.".center(33).upper())
            break

        autor = input("Informe o autor do livro: ").strip()
        ano = input("Ano (opcional): ")
        livro = Livro(titulo, codigo, autor, ano)
        biblioteca.adicionar_livro(livro)
        print("Livro cadastrado.".center(33))

        break

def cadastros_usuario():
    print("Lista de usuários: ")
    biblioteca.listar_usuarios()

def cadastros_livro():
    print("Lista de livros:")
    biblioteca.listar_livros()

def registrar_emprestimo():
    while True:
        titulo = input("Informe o título do livro que está a ser emprestado: ").strip() 
        livro = biblioteca.buscar_livro(titulo)
        if livro is None:
            print("Não há usuarios.".center(33))
            break   

        matricula = input("Informe a matrícula do usuário: ")
        usuario = biblioteca.buscar_usuario(matricula)
        if usuario is None:
            break

        data_emprestimo = input("Informe o dia em que o livro foi emprestado: ")
        data_devolucao = input("Informe o dia em que o livro será entregue: ")

        emprestimo = Emprestimo(livro, usuario, data_emprestimo, data_devolucao)
        biblioteca.realizar_emprestimo(emprestimo)
        livro.emprestar()
        usuario.pegar_emprestado(livro)

        return emprestimo

def registrar_devolucao():
    codigo = input("Informe o título do livro que está a ser devolvido")
    livro = biblioteca.buscar_livro(codigo)
    
def main():
    while True:

        opcao = menu()
        if opcao == "0":
            break

        if len(opcao) == 0:
            print("Você precisa escolher uma opção.".center(33))
        match opcao:
            case "1":
                print()
                print(" CADASTRAR LIVRO ".center(33, "="))
                print()
                cadastrar_livro()
                input("\nClique [ENTER] para voltar ao menu...")

            case "2":
                print()
                print(" CADASTRAR USUÁRIO ".center(33, "="))
                print()
                cadastrar_usuario()
                input("\nClique [ENTER] para voltar ao menu...")

            case "3":           
                print()
                print("REGISTRAR EMPRÉSTIMO".center(33))
                print()
                registrar_emprestimo()
                print()
                input("\nClique [ENTER] para voltar ao menu...")

            case "4":
                print()
                print("REGISTRAR DEVOLUÇÃO".center(33))
                print()
                print("Em desenvolvimento.".center(33))
                print()
                input("\nClique [ENTER] para voltar ao menu...")

            case "5":
                print()
                print("LISTAR LIVROS".center(33))
                print()
                cadastros_livro()
                input("\nClique [ENTER] para voltar ao menu...")

            case "6":
                print()
                print("LISTAR USUÁRIOS".center(33))
                print()
                cadastros_usuario()
                input("\nClique [ENTER] para voltar ao menu...")

            case "7":
                print()
                print("LISTA DE EMPRÉSTIMOS".center(33))
                print()
                biblioteca.listar_emprestimos_ativos()
                input("\nClique [ENTER] para voltar ao menu...")
    print("Programa encerrado.")

if __name__ == "__main__":
    main()