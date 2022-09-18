from Abstract.Expresion import Expresion


class AsignarVector(Expresion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, entorno):
        pass