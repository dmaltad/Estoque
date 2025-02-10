produtos = {
    "cebola":{
        'preco': 10.00,
        'quantidade': 30
    },
    "tomate":{
        'preco': 20.00,
        'quantidade': 20
    },
    "batata":{
        'preco': 5.00,
        'quantidade': 50
    },
    "alface":{
        'preco': 3.00,
        'quantidade': 40
    }
}

def adicionar(produtos, nome):
    if nome not in produtos:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        produtos[nome] = {"quantidade":quantidade, "preco": preco}
        print(f"O produto {nome} foi adicionado ao estoque.")
    else:
        print("Produto já existe em estoque.")

def atualizar(produtos, nome):
    if nome in produtos:
        atualizar = int(input("Digite o número para atualizar:\n1. Preço\n2. Quantidade\n\n"))
        if atualizar == 1:
            print(f"\nPreço: {produtos[nome]["preco"]}.")
            preco = float(input("Novo preço: "))
            produtos[nome]["preco"] = preco
            print(f"O preço do produto {nome} foi atualizado.")
        if atualizar == 2:
            print(f"\nQuantidade: {produtos[nome]["quantidade"]}")
            quantidade = int(input("Nova quantidade: "))
            produtos[nome]["quantidade"] = quantidade
            print(f"A quantidade do produto {nome} foi atualizado.")
        if atualizar < 1 or atualizar > 2:
            print("\nOpção inválida!")
    else:
        print("\nProduto inválido!")

def remover(produtos, nome):
    if nome in produtos:
        del produtos[nome]
        print(f"Produto {nome} removido do estoque.")
    else:
        print("\nProduto inválido!")

def exibir():
    print("\nProdutos em estoque:\n")
    for nome, precoEquantidade in produtos.items():
        print("Nome: " + nome)
        print("Preço: " + str (precoEquantidade["preco"]))
        print("Quantidade: " + str (precoEquantidade["quantidade"]))
        print("")
def calcular():
    c = 0
    for a,b in produtos.items():
       c+=(b["preco"])*(b["quantidade"])
    print(f"\nValor total do estoque: {c}")

gerenciar = 0

while gerenciar > 0 or gerenciar < 7:
    gerenciar = int(input("\nGerenciador de Estoque\n1. Adicionar produto\n2. Atualizar produto\n3. Remover produto\n4. Exibir estoque\n5. Calcular valor total do estoque\n6. Sair\n\n"))
    if gerenciar == 1:
        adicionar(produtos, nome =  input("\nNome do produto: "))
    elif gerenciar == 2:
        atualizar(produtos, nome = input("\nNome do produto: "))
    elif gerenciar == 3:
        remover(produtos, nome = input("\nNome do produto: "))
    elif gerenciar == 4:
        exibir()
    elif gerenciar == 5:
        calcular()
    elif gerenciar == 6:
        break
    else:
        print("\nOpção inserida inválida!")
