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
        print(f"O produto {nome} foi adicionado ao estoque.\n")
    else:
        print("Produto já existe em estoque.\n")

def atualizar(produtos, nome):
    if nome in produtos:
        atualizar = int(input("Digite o número para atualizar:\n1- Preço\n2- Quantidade\n"))
        if atualizar == 1:
            print(f"Preço: {produtos[nome]["preco"]}.")
            preco = float(input("Novo preço para o  produto: "))
            produtos[nome]["preco"] = preco
            print(f"O preço do produto {nome} foi atualizado.\n")
        if atualizar == 2:
            print(f"Quantidade: {produtos[nome]["quantidade"]}.")
            quantidade = int(input("Nova quantidade para o produto: "))
            produtos[nome]["quantidade"] = quantidade
            print(f"A quantidade do produto {nome} foi atualizado.\n")
        if atualizar < 1 or atualizar > 2:
            print("Opção inválida!\n")
    else:
        print("Produto inválido!\n")

def remover(produtos, nome):
    if nome in produtos:
        del produtos[nome]
        print("Produto removido do estoque.\n")
    else:
        print("Produto inválido!\n")

def exibir():
    print("Produtos em estoque:\n")
    for nome, precoEquantidade in produtos.items():
        print("Nome: " + nome)
        print("Preço: " + str (precoEquantidade["preco"]))
        print("Quantidade: " + str (precoEquantidade["quantidade"]))
        print("")
def calcular():
    c = 0
    for a,b in produtos.items():
       c+=(b["preco"])*(b["quantidade"])
    print(f"Valor total do estoque: {c}\n")

gerenciar = 0

while gerenciar > 0 or gerenciar < 7:
    gerenciar = int(input("Gerenciador de Estoque\n1. Adicionar produto\n2. Atualizar produto\n3. Remover produto\n4. Exibir estoque\n5. Calcular valor total do estoque\n6. Sair\n"))
    if gerenciar == 1:
        adicionar(produtos, nome =  input("Nome do produto: "))
    elif gerenciar == 2:
        atualizar(produtos, nome = input("Nome do produto: "))
    elif gerenciar == 3:
        remover(produtos, nome = input("Nome do produto: "))
    elif gerenciar == 4:
        exibir()
    elif gerenciar == 5:
        calcular()
    elif gerenciar == 6:
        break