from Pessoa import Pessoa
from Endereco import Endereco
from Cidade import Cidade

c1 = Cidade(1, "Porto Alegre", "RS")
end1 = Endereco(1,"Rua...", c1)
p1 = Pessoa(1,"Gui", "51-9999-5555", end1)
p1.cadastrar("Gui", c1)
end1.imprimir()
