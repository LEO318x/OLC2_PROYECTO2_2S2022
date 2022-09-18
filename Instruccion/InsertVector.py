from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import Simbolo
from Simbolo.Tipo import TIPO_DATO


class InsertVector(Instruccion):
    def __init__(self, fila, columna, id, indice, valor):
        super().__init__(fila, columna)
        self.id = id
        self.indice = indice
        self.valor = valor

    def ejecutar(self, entorno):
        valor = entorno.getVar(self.id)
        if valor.tipo == TIPO_DATO.VECT:
            indice = self.indice.ejecutar(entorno)
            value = self.valor.ejecutar(entorno)
            valor.valor.setAtributoConIndex(indice.valor, Simbolo('', value.valor, value.tipo, None))
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'NO es de tipo vector!'))
            print(f'NO es de tipo vector!')
            return Retorno(-1, TIPO_DATO.ERROR)
