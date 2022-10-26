from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Reporte.Reportes import lsimbolos
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Return(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.ejecutar(entorno)
        #print(f'ejec_return: valor {valor.valor}, tipo: {valor.tipo}')
        return Retorno(valor, TIPO_DATO.RETURN)

    def traducir(self, entorno, C3D):
        valor = self.expresion.traducir(entorno, C3D)
        C3D.comentario("Inicio Return")
        pos = C3D.sumar_stack()
        C3D.agregar_setstack(pos, valor.valor)
        C3D.agregar_getstack("t15", pos)
        # return C3D_Value(valor, False, TIPO_DATO.RETURN, False, False, 1)
        C3D.comentario("Fin Return")