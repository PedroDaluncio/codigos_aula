

class Editora:
    def __init__(self, codigo: int, nome: str):
        if isinstance(codigo, int) and isinstance(nome, str):
            self.__codigo = codigo
            self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
