from Cliente import Cliente
from Filme import Filme

class Locadora:
    def __init__(self):
        self.filmes = []
        self.clientes = []

    def cadastrar_filme(self, filme):
        self.filmes.append(filme)
        print(f"Filme '{filme.titulo}' cadastrado com sucesso!")

    def cadastrar_cliente(self, cliente):
        for c in self.clientes:
            if c.cpf == cliente.cpf:
                print(f"Erro: O CPF '{cliente.cpf}' já está cadastrado.")
                return
        self.clientes.append(cliente)
        print(f"Cliente: '{cliente.nome}' | CPF: {cliente.cpf} cadastrado com sucesso!")

    def listar_filmes_disponiveis(self):
        if not self.filmes:
            print("Não há filmes cadastrados.")
            return

        print("--- Filmes Disponíveis ---")
        for filme in self.filmes:
            if filme.disponivel:
                print(f"Código: {filme.codigo} | Título: {filme.titulo} | Gênero: {filme.genero} | Ano: {filme.ano}")

    def listar_clientes(self):
        if not self.clientes:
            print("Não há clientes cadastrados.")
            return
            
        print("--- Clientes Cadastrados ---")
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

        print(f"Aluguel realizado com sucesso!")
        print(f"Filme: '{filme_encontrado.titulo}' alugado para o cliente '{cliente_encontrado.nome}'.")
    
    def devolver_filme(self, codigo_filme):
        filme_encontrado = None
        
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

        print(f"Devolução realizada com sucesso!")
        print(f"O filme '{filme_encontrado.titulo}' foi devolvido e agora está disponível.")