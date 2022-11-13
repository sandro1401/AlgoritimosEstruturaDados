from Torre import Torre
from Apartamento import Apartamento
from FilaEspera import FilaEspera

torre1 = Torre()
fila_espera = FilaEspera()
# vaga2 = Vaga()

torre1.cadastrar(1,'Torre Norte', 'Av: A')
torre1.imprimir()

apto1 = Apartamento()
apto1.cadastrar(1,101, torre1.nome)

""" Criando fila para fila_espera"""
fila_espera.adicionar(2, 202, torre1)
fila_espera.adicionar(4,404, torre1)
fila_espera.adicionar(5,505, torre1)
fila_espera.adicionar(6,606, torre1)

# Removendo aptos da fila(remove do inicio da fila)
fila_espera.remover(1)

# Adiciona apto na fila (entra no final da fila)
fila_espera.adicionar(7,707, torre1)

fila_espera.remover(1)
fila_espera.remover(1)
fila_espera.remover(1)
fila_espera.remover(1)



