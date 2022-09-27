import copy

from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value


class Clone(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        expr = copy.deepcopy(expr)
        return Retorno(expr.valor, expr.tipo)

    def traducir(self, entorno, C3D):
        expr = self.expresion.traducir(entorno, C3D)
        expr = copy.deepcopy(expr)
        return C3D_Value(expr.valor, False, expr.tipo, None, None)
