from Furadeira import Furadeira
from Lixadeira import Lixadeira

f1 = Furadeira()
f1nome = input(f'Informe o nome da ferramenta: ')
f1tensao = input(f'Informe a tensão da ferramenta: ')
f1preco = input(f'Informe o preço da ferramenta: ')
f1potencia = input(f"Informe a potencia da ferramenta: ")
f1.cadastrar(f1nome, f1tensao, f1preco, f1potencia)
print(f1.getInformacoesFuradeira())

l1 = Lixadeira()
l1nome = input(f'Informe o nome da ferramenta: ')
l1tensao = input(f'Informe a tensão da ferramenta: ')
l1preco = input(f'Informe o preço da ferramenta: ')
l1potencia = input(f"Informe a potencia da ferramenta: ")
l1rotacoes = input(f'Informe as rotações da ferramenta: ')
l1.cadastrar(l1nome, l1tensao, l1preco, l1potencia, l1rotacoes)
print(l1.getInformacoesLixadeira())
