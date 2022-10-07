from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class ToOwned(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        return Retorno(expr.valor, TIPO_DATO.STRING)

    def traducir(self, entorno, C3D):
        expr = self.expresion.traducir(entorno, C3D)
        return C3D_Value(expr.valor, False, TIPO_DATO.STRING, False, False)