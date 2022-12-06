from No import  No

class ListaDuplamenteEncadeada :
	def __init__(self) :
		self.inicio = None
		self.fim = None
	
	def inserir(self, value) :
		node = No(value)
		if (self.inicio == None) :
			self.inicio = node
			self.fim = node
			return
		self.fim.proximo = node
		node.anterior = self.fim
		self.fim = node
	
	def imprimir(self) :
		if (self.inicio == None) :
			print("Lista esta vazia")
		else :
			print("\n ordem entrada: ", end = ": ")
			temp = self.inicio
			while (temp != None) :
				print(temp.dado, end = "  ")
				temp = temp.proximo
			
			print("\n ordenada: ", end = ": ")
			temp = self.fim
			while (temp != None) :
				print( temp.dado, end = "  ")
				temp = temp.anterior
			
			print(end = "\n")
		
	
	def posicao(self, primeiro, segundo) :
		valor = primeiro.dado
		primeiro.dado = segundo.dado
		segundo.dado = valor
	
	def Sorteio(self) :
		if (self.inicio == None) :
			return
		servico = True
		start = self.inicio
		while (servico == True) :
			servico = False
			while (start != None and start.proximo != None) :
				if (start.dado > start.proximo.dado) :
					self.posicao(start, start.proximo)
					servico = True
				start = start.proximo
			start = self.inicio

	def remover(self, valor):
		removeu = False
		if self.inicio == None:
			print("Lista vazia")
		else:
			if self.inicio.proximo == None and self.inicio.dado == valor:
				self.inicio = None
				self.fim = None
			else:
				if self.inicio.dado == valor:
					self.inicio.proximo.anterior = None
					self.inicio = self.inicio.proximo
					removeu = True

				else:
					aux = self.inicio
					temp = self.inicio.proximo
					while(temp):
						if temp.dado == valor:
							if temp.proximo == None:
								self.fim = aux #self.fim = temp.anteiro
							else:
								temp.proximo.anterior = aux
							aux.proximo = temp.proximo 
							break
						temp = temp.proximo
		self.imprimir()
		