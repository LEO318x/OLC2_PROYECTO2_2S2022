from abc import ABC, abstractmethod


class Expresion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()


    @abstractmethod
    def ejecutar(self, entorno):
        pass
