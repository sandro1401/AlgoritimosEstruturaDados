from lista import ListaDuplamenteEncadeada

#def main() :
l1 = ListaDuplamenteEncadeada()
l1.inserir("h")
l1.inserir("f")
l1.inserir("g")
l1.inserir("a")


print(" Antes ordenar ", end = "")
l1.imprimir()
l1.Sorteio()
print("\n Após ordenar", end = "")
l1.imprimir()

l1.remover("g")

#if __name__ == "__main__": main()