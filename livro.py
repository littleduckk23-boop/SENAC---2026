class Livro:
    def __init__(self, titulo, autor, codigo, ano = None):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True

    def emprestar(self):
       if self._disponivel:
           self._disponivel = False
           return True
       return False


    def devolver(self):
       self._disponivel = True

    # OS PEGADOR LÁ (GETTERS)
    def obter_codigo(self):
        return self._codigo

    def obter_titulo(self):
        return self._titulo
        
    def obter_autor(self):
        return self._autor

    def obter_ano(self):
        return self._ano

    def esta_disponivel(self):
        status = "Disponível" if self._disponivel else "Indisponível"
        return status

    # OS DEFINIDORES LÁ (SETTERS)
    def alterar_titulo(self, titulo):
        self._titulo = titulo 

    def alterar_autor(self, autor):
        self._autor = autor

    def alterar_ano(self, ano):
        self._ano = ano
    

    def __str__(self):
        if self._ano:
            return f"Título - {self.obter_titulo()}\nAutor - {self.obter_autor()}\nCódigo - {self.obter_codigo()}\nStatus - {self.esta_disponivel()}\nAno - {self.obter_ano()}"
        return f"Título - {self.obter_titulo()}\nAutor - {self.obter_autor()}\nCódigo - {self.obter_codigo()}\nStatus - {self.esta_disponivel()}\n"
    

if __name__ == "__main__":
    # TESTANDO ERROS DE CRIAÇÃO DO OBJETO
    print("\nTESTANDO CRIAÇÃO DE OBJETO SEM PARÂMETROS")
    try:
        livro = Livro()
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    print("\nTESTANDO CRIAÇÃO DE OBJETO COM PARÂMETROS INVÁLIDOS")
    try:
        livro = Livro("","","")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    try:
        # TESTANDO CRIAÇÃO OK
        print("\nTESTANDO A CRIAÇÃO DE UM OBJETO VÁLIDO")
        livro = Livro("Machado de Assis", "Dom Casmurro", "L001", 1899)

        print(livro)

        # TESTANDO OS GETTERS
        print("\nGETTERS")
        print(f"Código....: {livro.obter_codigo()}")
        print(f"Título....: {livro.obter_titulo()}")
        print(f"Autor.....: {livro.obter_autor()}")
        print(f"Ano.......: {livro.obter_ano()}")
        print(f"Disponível: {livro.esta_disponivel()}")

        # TESTANDO O EMPRÉSTIMO
        livro.emprestar()
        print("\nEMPRESTEI")
        print(f"Disponível: {livro.esta_disponivel()}")

        # TESTANDO A DEVOLUÇÃO
        livro.devolver()
        print("\nDEVOLVI")
        print(f"Disponível: {livro.esta_disponivel()}")

        # TESTANDO OS SETTERS
        livro.alterar_titulo("A maravilhosa história da vida de Ludovico")
        livro.alterar_autor("Ludovico Monjardim")
        livro.alterar_ano(1971)

        print("\nALTEREI OS DADOS")
        print(livro)

        # TESTANDO UMA OPERAÇÃO INVÁLIDA
        print("\nTESTANDO EMPRÉSTIMO DUPLICADO")
        livro.emprestar()
        livro.emprestar()

    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")


    # TESTANDO OS SETTERS ERRADOS
    print("\nTESTANDO OS SETTERS ERRADOS")
    try:
        livro.alterar_titulo("")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    try:
        livro.alterar_autor("")
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

    try:
        livro.alterar_ano(-1)
    except (ValueError, TypeError) as erro:
        print(f"\nErro: {erro}")

