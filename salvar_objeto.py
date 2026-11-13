class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma


alunos = []

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        nome, turma = linha.split(";")

        aluno = Aluno(nome, turma)

        alunos.append(aluno)


for aluno in alunos:
    print(aluno.nome, "-", aluno.turma)