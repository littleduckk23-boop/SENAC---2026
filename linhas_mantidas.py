linhas_mantidas = []

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        nome, turma = linha.split(";")

        if nome != "Carlos":
            linhas_mantidas.append(linha)


with open("alunos.txt", "w", encoding="utf-8") as arquivo:
    for linha in linhas_mantidas:
        arquivo.write(linha + "\n")