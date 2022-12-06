def getTamanho(x):
    return len(x)

def aumentaPreco(p):
    return p*1.1

frutas = ["Laranja", "banana", "abacaxi - terra de areia"]

jogadores = ("Maria", "José", "júlia", "Carlos", "joana", "Marcelo")

tamFrutas = map(getTamanho, frutas)
print("Frutas: ", list(tamFrutas))

tamJogadores = map(getTamanho, jogadores)
print("Frutas: ", list(tamJogadores))

precos = [6.0, 5.5, 4.99, 10.00]
novosPrecos = map(aumentaPreco, precos)
print("Novos Preços: ", list(novosPrecos))

produto = {
    0: 10.0,
    1: 5.0,
    5: 1.5

}
print(produto)

novoProduto = map(aumentaPreco, produto.values())
print(list(novoProduto))