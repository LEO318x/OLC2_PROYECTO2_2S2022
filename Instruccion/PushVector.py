from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import Simbolo
from Simbolo.Tipo import TIPO_DATO


class PushVector(Instruccion):
    def __init__(self, fila, columna, id, expresion):
        super().__init__(fila, columna)
        self.id = id
        self.expresion = expresion

    def ejecutar(self, entorno):
        #print(f'push_id: {self.id}')
        valor = entorno.getVar(self.id)
        if valor.tipo == TIPO_DATO.VECT:
            expre = self.expresion.ejecutar(entorno)
            valor.valor.setAtributo(Simbolo('', expre.valor, expre.tipo, None))
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'NO es de tipo vector!'))
            print(f'NO es de tipo vector!')
            return Retorno(-1, TIPO_DATO.ERROR)