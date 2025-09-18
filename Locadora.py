# Locadora.py
from Cliente import Cliente
from Filme import Filme

class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []

    ####Salvar nos arquivos
    def salvar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as arquivo:
            for cliente in self.clientes:
                arquivo.write(f"{cliente.nome};{cliente.cpf}\n")

    def salvar_filmes(self):
        with open("filmes.txt", "w", encoding="utf-8") as arquivo:
            for filme in self.filmes:
                arquivo.write(f"{filme.codigo};{filme.titulo};{filme.genero};{filme.ano};{filme.disponivel}\n")

    ####Salvar nos arquivos


    def cadastrar_filme(self, filme):
        self.filmes.append(filme)
        self.salvar_filmes()
        print(f"Filme '{filme.titulo}' cadastrado com sucesso!")

    def cadastrar_cliente(self, cliente):
        for c in self.clientes:
            if c.cpf == cliente.cpf:
                print(f"Erro: O CPF '{cliente.cpf}' já está cadastrado.")
                return
        self.clientes.append(cliente)
        self.salvar_clientes()
        print(f"Cliente: '{cliente.nome}' | CPF: {cliente.cpf} cadastrado com sucesso!")

    def listar_filmes_disponiveis(self):
        if not self.filmes:
            print("Não há filmes cadastrados.")
            return

        print("\n--- Filmes Disponíveis ---")
        for filme in self.filmes:
            if filme.disponivel:
                print(f"Código: {filme.codigo} | Título: {filme.titulo} | Gênero: {filme.genero} | Ano: {filme.ano}")

    def listar_clientes(self):
        if not self.clientes:
            print("Não há clientes cadastrados.")
            return

        print("\n--- Clientes Cadastrados ---")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome} | CPF: {cliente.cpf}")

    def alugar_filme(self, cpf_cliente, codigo_filme):
        cliente_encontrado = None
        filme_encontrado = None

        for cliente in self.clientes:
            if cliente.cpf == cpf_cliente:
                cliente_encontrado = cliente
                break

        if not cliente_encontrado:
            print("Erro: Cliente não encontrado.")
            return

        for filme in self.filmes:
            if filme.codigo == codigo_filme:
                filme_encontrado = filme
                break

        if not filme_encontrado:
            print("Erro: Filme não encontrado.")
            return

        if not filme_encontrado.disponivel:
            print(f"Erro: O filme '{filme_encontrado.titulo}' já está alugado.")
            return

        filme_encontrado.disponivel = False
        self.salvar_filmes()

        print(f"\nAluguel realizado com sucesso!")
        print(f"Filme: '{filme_encontrado.titulo}' alugado para o cliente '{cliente_encontrado.nome}'.")

    def devolver_filme(self, cpf_cliente, codigo_filme):
        cliente_encontrado = None
        filme_encontrado = None

        for cliente in self.clientes:
            if cliente.cpf == cpf_cliente:
                cliente_encontrado = cliente
                break

        if not cliente_encontrado:
            print("Erro: Cliente não encontrado.")
            return

        for filme in self.filmes:
            if filme.codigo == codigo_filme:
                filme_encontrado = filme
                break

        if not filme_encontrado:
            print("Erro: Filme não encontrado.")
            return

        if filme_encontrado.disponivel:
            print(f"Erro: O filme '{filme_encontrado.titulo}' não está alugado.")
            return

        filme_encontrado.disponivel = True
        self.salvar_filmes()

        print(f"\nDevolução realizada com sucesso!")
        print(f"O filme '{filme_encontrado.titulo}' foi devolvido pelo cliente '{cliente_encontrado.nome}'.")
