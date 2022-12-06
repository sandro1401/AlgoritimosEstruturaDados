# Construir uma pilha de livros para dar baixa nos empréstimos.
# O livro deve conter relação com os autores cadastrados.
from Autor import Autor
from Livro import Livro
from Pilha import Pilha


a1 = Autor("Érico Veríssimo", 98)
a2 = Autor("Fernando Pessoa", 120)

l1 = Livro("O Tempo e o Vento", 250, a1)
l2 = Livro("O Continente", 120, a1, 'Capa Dura')
l3 = Livro("Tabacaria", 150, a2)

livros = Pilha()
livros.imprimir()
livros.adicionarLivro(l2)
print("-------------------------")
livros.adicionarLivro(l1)
# livros.adicionarLivro(l3)
livros.imprimir()
