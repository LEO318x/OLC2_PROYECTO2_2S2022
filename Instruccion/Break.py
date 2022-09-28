from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Break(Instruccion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, entorno):
        return Retorno('break', TIPO_DATO.BREAK)

    def traducir(self, entorno, C3D):
        C3D.comentario("BREAK")
        tbreak = C3D.nuevo_label()
        C3D.agregar_break(tbreak)
        C3D.agregar_goto(tbreak)
        return None
        # return C3D_Value('break', False, TIPO_DATO.BREAK, None, None)

        