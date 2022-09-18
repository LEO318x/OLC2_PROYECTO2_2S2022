from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import *


class Literal(Expresion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        #print(f'----->{self.tipo}')
        if self.tipo == TIPO_DATO.INTEGER:
            return Retorno(self.valor, TIPO_DATO.INTEGER)
        elif self.tipo == TIPO_DATO.FLOAT:
            return Retorno(self.valor, TIPO_DATO.FLOAT)
        elif self.tipo == TIPO_DATO.STRING:
            return Retorno(self.valor, TIPO_DATO.STRING)
        elif self.tipo == TIPO_DATO.RSTR:
            return Retorno(self.valor, TIPO_DATO.RSTR)
        elif self.tipo == TIPO_DATO.CHAR:
            if len(self.valor) > 1:
                tmpchar = self.valor
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Char no puede ser mayor a 1'))
                print(f'Error_Lit: Char no puede ser > 1')
                return Retorno(tmpchar[0:1], TIPO_DATO.CHAR)
            else:
                return Retorno(self.valor, TIPO_DATO.CHAR)
        elif self.tipo == TIPO_DATO.BOOL:
            if self.valor == 'true':
                self.valor = True
            elif self.valor == 'false':
                self.valor = False
            return Retorno(self.valor, TIPO_DATO.BOOL)
