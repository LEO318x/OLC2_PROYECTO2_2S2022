from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO


class CapacityVector(Instruccion):
    def __init__(self, fila, columna, id):
        super().__init__(fila, columna)
        self.id = id

    def ejecutar(self, entorno):
        valor = self.id.ejecutar(entorno)
        if valor.tipo == TIPO_DATO.VECT:
            capacidad = valor.valor.getTamanioMax()
            return Retorno(capacidad, TIPO_DATO.INTEGER)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'NO es de tipo vector!'))
            print(f'NO es de tipo vector!')
            return Retorno(-1, TIPO_DATO.ERROR)
