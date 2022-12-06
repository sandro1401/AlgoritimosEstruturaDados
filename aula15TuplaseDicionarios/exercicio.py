# num = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"

# user = int(input("escolha um número entre 0 e 9: "))

# print(num[user])




nome = input("informe o nome: ")
n1 = float(input("informe N1: "))
n2 = float(input("informe N2: "))

dic = {
    "nome": nome,
    "Nota1": n1,
    "nota2": n2
}

media = ((n1 + n2)/2)

print(media)

dic["Média"] = media
print(dic)
