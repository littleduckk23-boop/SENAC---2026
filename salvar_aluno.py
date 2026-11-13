def salvar_aluno(nome, turma):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{turma}\n")

nome = input("Nome: ")
turma = input("Turma: ")
salvar_aluno(nome, turma)