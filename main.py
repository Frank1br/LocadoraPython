from Cliente import Cliente
from Filme import Filme
from Locadora import Locadora

def menu():
    locadora = Locadora()

    while True:
        print("\n===== LOCADORA PYTHON =====")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Filme")
        print("3. Listar Clientes")
        print("4. Listar Filmes Disponíveis")
        print("5. Alugar Filme")
        print("6. Devolver Filme")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            locadora.cadastrar_cliente(cliente)

        elif opcao == "2":
            codigo = input("Código do filme: ")
            titulo = input("Título do filme: ")
            genero = input("Gênero do filme: ")
            ano = input("Ano do filme: ")
            filme = Filme(titulo, genero, ano, codigo)
            locadora.cadastrar_filme(filme)

        elif opcao == "3":
            locadora.listar_clientes()

        elif opcao == "4":
            locadora.listar_filmes_disponiveis()

        elif opcao == "5":
            cpf = input("CPF do cliente: ")
            codigo = input("Código do filme: ")
            locadora.alugar_filme(cpf, codigo)

        elif opcao == "6":
            cpf = input("CPF do cliente: ")
            codigo = input("Código do filme para devolução: ")
            locadora.devolver_filme(cpf, codigo)

        elif opcao == "0":
            print("Saindo do sistema... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
