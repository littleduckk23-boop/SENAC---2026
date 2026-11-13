from carregar_objetos import Aluno
alunos = []
with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        nome, turma = linha.split(";")
        aluno = {"nome": nome, "turma": turma}
        alunos.append(Aluno(aluno["nome"], aluno["turma"]))

    for aluno in alunos:
        print(aluno)