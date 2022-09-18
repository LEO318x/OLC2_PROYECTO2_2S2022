from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO
import Expresion.Acceso


class ContainsVector(Instruccion):
    def __init__(self, fila, columna, id, expresion):
        super().__init__(fila, columna)
        self.id = id
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = None
        if isinstance(self.id, Expresion.Acceso.Acceso):
            valor = self.id.ejecutar(entorno)
        else:
            valor = entorno.getVar(self.id)


        if valor.tipo == TIPO_DATO.VECT:
            expre = self.expresion.ejecutar(entorno)
            res = valor.valor.contains(expre.valor)
            return Retorno(res, TIPO_DATO.BOOL)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'NO es de tipo vector!'))
            print(f'NO es de tipo vector!')
            return Retorno(-1, TIPO_DATO.ERROR)

