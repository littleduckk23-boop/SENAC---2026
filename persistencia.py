
with open("alunos.txt", "a", encoding="utf-8") as arquivo:
    nome = input("Cade seu nome: ")
    conteudo = arquivo.write(nome + "\n")

with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(f"\nConteúdo do arquivo:\n{conteudo}...")

