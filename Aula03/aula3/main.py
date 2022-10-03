from categoria import Categoria 
from produto import Produto 


cat01 = Categoria("Bebidas")
p1 = Produto("Coca-Cola", 7.29, cat01 )

p2 = Produto("Pepsi", 5.99, cat01 )
p2 = Produto("Pepsi", 5.99, cat01 )
p3 = Produto("X-Tudo", 25.99, Categoria("Lanches") )
p4 = Produto("X-Acebolado", 20.99, p3.categoria) 



p1.imprimir()
p3.imprimir()
p4.imprimir()