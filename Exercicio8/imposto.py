from abc import abstractmethod, ABC


class Imposto(ABC):
    @abstractmethod
    def __init__(self, aliquota: float):
        self.__aliquota = aliquota

    @property
    def aliquota(self):
        return self.__aliquota

    @abstractmethod
    def calcula_aliquota(self) -> float:
        pass
