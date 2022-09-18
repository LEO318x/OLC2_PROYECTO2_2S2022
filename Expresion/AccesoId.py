from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO


class AccesoID(Expresion):
    def __init__(self, fila, columna, expresion, key):
        super().__init__(fila, columna)
        self.expresion = expresion
        self.key = key

    def ejecutar(self, entorno):
        left = self.expresion.ejecutar(entorno)
        #print(f'{left.tipo}')
        if left.tipo == TIPO_DATO.STRUCT:
            valor = left.valor.get(self.key)
            return valor
        else:
            lerrores.append(
                Error(self.fila, self.columna, entorno.nombre, 'La variable no existe'))
            print(f'Error_LlamarExprStruct: la variable no existe')
            return Retorno(-1, TIPO_DATO.ERROR)
