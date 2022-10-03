from Desktop import Desktop
from Notebook import Notebook

note = Notebook()
note.cadastrar("Asus", "preto", 1000, "10 hs")
print(note.getInformacoes())

desk = Desktop()
desk.cadastrar("Dell", "Prata", 3000, "500 Watts")
print(desk.getInformacoes())