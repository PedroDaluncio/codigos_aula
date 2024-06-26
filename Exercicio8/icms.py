from imposto import Imposto


class ICMS(Imposto):
    def __init__(self, aliquota, diferenca_estado: float):
        super().__init__(aliquota)
        self.__diferenca_estado = diferenca_estado

    @property
    def diferenca_estado(self):
        return self.__diferenca_estado

    @diferenca_estado.setter
    def diferenca_estado(self, diferenca_estado: float):
        if isinstance(diferenca_estado, float):
            self.__diferenca_estado = diferenca_estado

    def calcula_aliquota(self):
        valor = self.aliquota + self.__diferenca_estado
        return valor
