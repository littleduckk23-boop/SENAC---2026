from carregar_objetos import Aluno
def carregar_alunos():
    alunos = []
    try:
        with open(
            "fafas.txt", "r", encoding="utf-8"
        ) as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                nome, turma = linha.split(";")
                alunos.append(Aluno(nome, turma))

    except FileNotFoundError:
        pass
    return alunos

alunos = carregar_alunos()

for aluno in alunos:
    print(aluno.nome)