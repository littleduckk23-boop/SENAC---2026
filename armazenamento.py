nomes = ["Ana", "Adalberto", "Cavalo de Tróia"]
with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

