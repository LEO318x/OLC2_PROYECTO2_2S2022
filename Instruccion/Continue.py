from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class Continue(Instruccion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, entorno):
        return Retorno('continue', TIPO_DATO.CONTINUE)

    def traducir(self, entorno, C3D):
        return Retorno('continue', TIPO_DATO.CONTINUE)
