carro = {
    "modelo": "Doblo",
    "ano": 2006,
    "reboque": False,
    "capacidade": 950.253

}

print(carro)

print("ano: ", carro["ano"])

print (carro.keys())
print (carro.values())

for chave, valor in carro.items():
    print(chave , ": ", valor)

print("\n----------------------------")

for chave in carro.keys():
    print(chave , ": ", carro[chave])

print("-----------Tuplaa de Dicionários------------")

filho1 = {"nome": "Júlia", "Idade": 14}
filho2 = {"nome": "Neimar", "Idade": 30}
filho3 = {"nome": "Mauricio", "Idade": 22}

filhos = (filho1, filho2)

print(filhos)
filho1["nome"] = "Mauricio"
filho1["e-mail"] = "mm@.com"

print(filhos[0])

del filho1["Idade"]

print(filhos)