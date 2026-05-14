# Lista de Compras

# Criamos uma lista vazia para armazenar os produtos
produtos = []

while True:
    print("\nMenu de opções:")
    print("1 - Adicionar à lista")
    print("2 - Pesquisar item")
    print("3 - Remover item")
    print("4 - Alterar item")
    print("5 - Listar produtos")
    print("6 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        while True:
            produto = input("Digite um produto para adicionar (ou 'sair' para encerrar): ").lower()
            if produto == "sair":
                break
            produtos.append(produto)
        print("Produtos adicionados com sucesso!")

    elif opcao == "2":
        produto_pesquisa = input("Digite o nome do produto a ser pesquisado: ").lower()
        if produto_pesquisa in produtos:
            print(f"Produto '{produto_pesquisa}' encontrado na lista.")
        else:
            print(f"Produto '{produto_pesquisa}' não encontrado na lista.")

    elif opcao == "3":
        produto_remover = input("Digite o nome do produto a ser removido: ").lower()
        if produto_remover in produtos:
            produtos.remove(produto_remover)
            print(f"Produto '{produto_remover}' removido com sucesso!")
        else:
            print(f"Produto '{produto_remover}' não encontrado na lista.")

    elif opcao == "4":
        produto_alterar = input("Digite o nome do produto a ser alterado: ").lower()
        if produto_alterar in produtos:
            novo_produto = input("Digite o novo nome do produto: ").lower()
            index = produtos.index(produto_alterar)
            produtos[index] = novo_produto
            print(f"Produto '{produto_alterar}' alterado para '{novo_produto}' com sucesso!")
        else:
            print(f"Produto '{produto_alterar}' não encontrado na lista.")

    elif opcao == "5":
        if not produtos:
            print("Lista vazia.")
        else:
            print("Produtos cadastrados:")
            for p in produtos:
                print(p)

    elif opcao == "6":
        print("Programa encerrado com sucesso!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

