nome = input("Nome: ")
turma = input("Turma: ")
with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"\n{nome};{turma} \n")
