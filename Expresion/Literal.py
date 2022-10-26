from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import *


class Literal(Expresion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        # print(f'----->{self.tipo}')
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

    def traducir(self, entorno, C3D):
        # print(f'----->{self.tipo}')
        if self.tipo == TIPO_DATO.INTEGER:
            return C3D_Value(str(self.valor), False, TIPO_DATO.INTEGER, None, None)
        elif self.tipo == TIPO_DATO.FLOAT:
            return C3D_Value(str(self.valor), False, TIPO_DATO.FLOAT, None, None)
        elif self.tipo == TIPO_DATO.STRING:
            return C3D_Value(str(self.valor), False, TIPO_DATO.STRING, None, None)
        elif self.tipo == TIPO_DATO.RSTR:
            return C3D_Value(self.valor, False, TIPO_DATO.RSTR, None, None)
        elif self.tipo == TIPO_DATO.CHAR:
            if len(self.valor) > 1:
                tmpchar = self.valor
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Char no puede ser mayor a 1'))
                print(f'Error_Lit: Char no puede ser > 1')
                return C3D_Value(tmpchar[0:1], False, TIPO_DATO.CHAR, None, None)
            else:
                return C3D_Value(self.valor, False, TIPO_DATO.CHAR, None, None)
        elif self.tipo == TIPO_DATO.BOOL:
            print(f'Literal Booleana')
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()
            if self.valor == 'true':
                # C3D.agregar_goto(truelabel)
                C3D.agregar_if(1, 0, ">", truelabel)
                C3D.agregar_goto(falselabel)
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            elif self.valor == 'false':
                # C3D.agregar_goto(falselabel)
                C3D.agregar_if(0, 1, ">", truelabel)
                C3D.agregar_goto(falselabel)
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)
