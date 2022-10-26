from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class Continue(Instruccion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, entorno):
        return Retorno('continue', TIPO_DATO.CONTINUE)

    def traducir(self, entorno, C3D):
        C3D.comentario("CONTINUE")
        C3D.agregar_goto(C3D.obtener_continue())
        C3D.limpiar_continue()
        return None
        # return C3D_Value('continue', False, TIPO_DATO.CONTINUE, None, None)
