from usuarios import cadastrar_usuario, listar_usuarios, buscar_usuario, excluir_usuario


def mostrar_menu():
    print("\n=== CADASTRO DE USUÁRIOS ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")


def main():
    usuarios = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            try:
                cadastrar_usuario(usuarios, nome, email)
                print("Usuário cadastrado com sucesso!")
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            resultado = listar_usuarios(usuarios)
            if not resultado:
                print("Nenhum usuário cadastrado.")
            for usuario in resultado:
                print(f"Nome: {usuario['nome']} | E-mail: {usuario['email']}")

        elif opcao == "3":
            nome = input("Nome para buscar: ")
            usuario = buscar_usuario(usuarios, nome)
            print(usuario if usuario else "Usuário não encontrado.")

        elif opcao == "4":
            email = input("E-mail do usuário que deseja excluir: ")
            if excluir_usuario(usuarios, email):
                print("Usuário excluído.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
