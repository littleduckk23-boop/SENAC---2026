class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

    def __str__(self):
        return f"[{self.turma}] - {self.nome}"