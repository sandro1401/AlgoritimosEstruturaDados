# Fila de carros de uma lavagem
from Fila import Fila

fifo = Fila()

fifo.add ("ABC-1234", 240500)
fifo.add ("BCA-2234", 2500)
fifo.add ("BBB-3334", 220500)

fifo.remover()
fifo.remover()
fifo.add ("XXX-1234", 2400)

fifo.remover()
fifo.remover()
