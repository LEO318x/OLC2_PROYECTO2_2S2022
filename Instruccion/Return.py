from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Reporte.Reportes import lsimbolos
from Simbolo.Tipo import TIPO_DATO


class Return(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.ejecutar(entorno)
        #print(f'ejec_return: valor {valor.valor}, tipo: {valor.tipo}')
        return Retorno(valor, TIPO_DATO.RETURN)