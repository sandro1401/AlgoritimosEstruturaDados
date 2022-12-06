from abc import ABCMeta, abstractmethod

class Impresso(metaclass=ABCMeta):
    def __init__(self, titulo, qtdPaginas, autor):
        self.titulo = titulo
        self._paginas = qtdPaginas
        self.__autor = autor
        self.proximo = None

    def getPaginas(self):
        if self._paginas >= 10:
            return self._paginas
        else:
            return -1

    def setPaginas(self, qtd):
        if qtd > 0:
            self._paginas = qtd
        
    @property
    def autor(self):
        if self.__autor != None:
            return self.__autor
        else:
            return None

    @autor.setter
    def autor(self, autor):
        if autor != None:
            self.__autor = autor

    @abstractmethod
    def cadastrar(self):
        pass

    def __str__(self):
        return f"Título: {self.titulo}\nPáginas: {self._paginas}\nAutor: {self.__autor}"