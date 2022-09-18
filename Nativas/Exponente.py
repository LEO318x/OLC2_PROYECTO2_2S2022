from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import *

class Exponente(Expresion):
    def __init__(self, exprIzq, tipo_operacion, exprDer, fila, columna):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        valorIzq = self.exprIzq.ejecutar(entorno)
        valorDer = self.exprDer.ejecutar(entorno)

        if TIPO_DATO.INTEGER == valorIzq.tipo and TIPO_DATO.INTEGER == valorDer.tipo:
            if TIPO_OPERACION.EXPO == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor ** valorDer.valor, TIPO_DATO.INTEGER)
        elif TIPO_DATO.FLOAT == valorIzq.tipo and TIPO_DATO.FLOAT == valorDer.tipo:
            if TIPO_OPERACION.EXPO == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor ** valorDer.valor, TIPO_DATO.FLOAT)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'Expo_Error: No coinciden los tipos {self.exprIzq.tipo} != {self.exprDer.tipo}'))
            print(f'Expo_Error: No coinciden los tipos {self.exprIzq.tipo} != {self.exprDer.tipo}')
            resultado = Retorno(0, TIPO_DATO.INTEGER)
        return resultado