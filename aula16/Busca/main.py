# Desafio
# • Construa um algoritmo de busca contendo um vetor de números
# inteiros de 20 posições.
# • O algoritmo deve ter duas funções, uma para busca sequencial e
# outra para busca binária.
# • Coloque um contador em cada função para contar as iterações de
# cada função.
# • Peça ao usuário que informe o valor que deseja procurar.
# • Então informe ao usuário se este valor existe no vetor e quantas
# iterações foram necessárias em cada função.

# class No :
# 	def __init__(self, dado) :
# 		self.dado = dado
# 		self.proximo = None
# 		self.anterior = None
                
# class Lista:
# 	def __init__(self) :
# 		self.inicio = None
# 		self.fim = None
	
	
# 	def imprimir(self) :
# 		if (self.inicio == None) :
# 			print("Lista esta vazia")
# 		else :
# 			print("\n Lista: ", end = ": ")
# 			temp = self.inicio
# 			while (temp != None) :
# 				print(temp.dado, end = "  ")
# 				temp = temp.proximo
			
# 			print("\n Lista: ", end = ": ")
# 			temp = self.fim
# 			while (temp != None) :
# 				print( temp.dado, end = "  ")
# 				temp = temp.anterior
			
# 			print(end = "\n")
		
	
# 	def posicao(self, primeiro, segundo) :
# 		valor = primeiro.dado
# 		primeiro.dado = segundo.dado
# 		segundo.dado = valor
	
# 	def sorteio(self) :
# 		if (self.inicio == None) :
# 			return
# 		servico = True
# 		start = self.inicio
# 		while (servico == True) :
# 			servico = False
# 			while (start != None and start.proximo != None) :
# 				if (start.dado > start.proximo.dado) :
# 					self.posicao(start, start.proximo)
# 					servico = True
# 				start = start.proximo
# 			start = self.inicio






v = [1, 15, 89, 22, 74, 88, 23, 41, 10, 12, 3, 9, 55, 40, 77, 86, 25, 19, 30, 58]



def buscaSequencial(lst, item):
    i = 0
    found = False
    count = 0
    while i < len(lst) and not found:
        count += 1
        if lst[i] == item:
            found = True
        else:
            i = i+1
    return found, count
            
	
def busca_binaria(lst, item):
    count = 0
    inicio = 0
    fim =  len(lst)- 1
    
    while inicio <= fim:
        count += 1
        centro = int(inicio+(fim - inicio)/ 2)
        if lst[centro] == item:
            return centro
        elif item > lst[centro]:
            inicio = centro + 1
        else: 
            fim = centro-1
    return -1, count

item = int(input('Digite o número deseja localizar? '))
print(f"valor existe na lista? {buscaSequencial(v,item)}")
print("----------------------------")
# v = Lista()
# v.sorteio
v1 = sorted(v)
print(f"Posição ordenada na busca Binaria: {busca_binaria(v1,item)}")