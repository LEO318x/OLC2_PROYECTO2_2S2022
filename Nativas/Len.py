from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Len(Instruccion):
    def __init__(self, fila, columna, id):
        super().__init__(fila, columna)
        self.id = id

    def ejecutar(self, entorno):
        valor = self.id.ejecutar(entorno)
        if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.VECT:
            tamanio = valor.valor.getTamanio()
            return Retorno(tamanio, TIPO_DATO.INTEGER)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'len solo se puede usar solo para arreglos y vectores'))
            print(f'Error, len solo se puede usar solo para arreglos y vectores')
            return Retorno(-1, TIPO_DATO.ERROR)

    def traducir(self, entorno, C3D):
        valor = self.id.traducir(entorno, C3D)
        if valor.tipo == TIPO_DATO.ARRAY or valor.tipo == TIPO_DATO.VECT:
            tamanio = valor.tamanio
            print(f'len tamanio:{tamanio}')
            return C3D_Value(str(tamanio), False, TIPO_DATO.INTEGER, None, None)
        else:
            lerrores.append(
                Error(self.fila, self.columna, entorno.nombre, 'len solo se puede usar solo para arreglos y vectores'))
            print(f'Error, len solo se puede usar solo para arreglos y vectores')
            return Retorno(-1, TIPO_DATO.ERROR)