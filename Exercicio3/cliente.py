

class Cliente:
    def __init__(self, nome, fone):
        self.__nome = None
        self.__fone = None
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, int):
            self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        return self.__nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        self.__fone = fone
        return self.__fone
