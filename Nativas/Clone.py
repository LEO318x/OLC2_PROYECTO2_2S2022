import copy

from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno


class Clone(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        expr = copy.deepcopy(expr)
        return Retorno(expr.valor, expr.tipo)
