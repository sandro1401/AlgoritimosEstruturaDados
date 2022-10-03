produtos = ["coca cola", "pepsi", "cheetos"]
precos = [7.79, 5.99, 3.5]
quantidades = [100, 50, 75]

def imprimir(posicao):
    print("nome: " , produtos[posicao] )
    print("preco: " , precos[posicao] )
    print("quantidade: " , quantidades[posicao] )

def imprimirTodos():
    for i in range(len(produtos)):
        print("nome: " , produtos[i] )
        print("preco: " , precos[i] )
        print("quantidade: " , quantidades[i] )
        print("----------------------")


def remover(posicao):
    produtos.pop(posicao)
    precos.pop(posicao)
    quantidades.pop(posicao)
    imprimirTodos()


print("1-Imprimir um produto  da lista")
print("2-excluir um produto da lista")

opcao = int(input("Digite sua opçao: "))
posicao = int(input("Digite a posição: "))

if opcao == 1:
    imprimir(posicao)
elif opcao == 2:
    remover(posicao)
else:
    imprimirTodos()
