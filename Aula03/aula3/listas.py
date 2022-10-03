carros = ["Uno", "Doblo", "Toro", "147"]

print(carros)

print(carros[2])

print(carros[2:4])

print(carros[-3:-1])

print(carros[-4:-1])


produtos = ["arros", "feijão", "açucar", "refrigerante"]
precos = [5, 10, 4, 8]
quantidades = [4, 12, 21, 6]


def produtoLista(posicao):
    print (produtos[posicao], precos[posicao], quantidades[posicao])

def removerProdutoLista(posicao):
    return produtos.pop(posicao), precos.pop(posicao), quantidades.pop(posicao)


produtoLista(0)


removerProdutoLista(1)

produtoLista(1)

