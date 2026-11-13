class Emprestimo:
    def __init__(self, aluno, livro):
        self.aluno = aluno
        self.livro = livro

def salvar_emprestimo(emprestimo):
    with open("emprestimos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{emprestimo.aluno};{emprestimo.livro}\n")

def carregar_emprestimos():
    emprestimos = []

    try:
        with open(
            "emprestimos.txt", "r", encoding="utf-8"
        ) as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                aluno, livro = linha.split(";", 1)
                emprestimo = Emprestimo(aluno, livro)
                emprestimos.append(emprestimo)
    except FileNotFoundError:
        pass

    return emprestimos

emprestimos = carregar_emprestimos()
for emprestimo in emprestimos:
    print(emprestimo.aluno, "-", emprestimo.livro)

aluno = input("Aluno: ")
livro = input("Livro: ")
emprestimo = Emprestimo(aluno, livro)
salvar_emprestimo(emprestimo)
