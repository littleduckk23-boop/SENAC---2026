class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma


alunos = []

nome = input("Nome: ")
turma = input("Turma: ")

aluno = Aluno(nome, turma)
alunos.append(aluno)

print("\nAlunos cadastrados:")

for aluno in alunos:
    print(aluno.nome, "-", aluno.turma)