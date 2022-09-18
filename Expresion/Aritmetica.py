import math

from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import *


class Aritmetica(Expresion):
    def __init__(self, exprIzq, tipo_operacion, exprDer, fila, columna, unaria):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.fila = fila
        self.columna = columna
        self.unaria = unaria

    def ejecutar(self, entorno):
        if self.unaria:
            expr = self.exprDer.ejecutar(entorno)
            if TIPO_DATO.INTEGER == expr.tipo:
                resultado = Retorno(expr.valor * -1, TIPO_DATO.INTEGER)
                return resultado
            elif TIPO_DATO.FLOAT == expr.tipo:
                resultado = Retorno(expr.valor * -1, TIPO_DATO.FLOAT)
                return resultado

        valorIzq = self.exprIzq.ejecutar(entorno)
        valorDer = self.exprDer.ejecutar(entorno)

        #print(f'--->{self.fila}, {self.columna}')
        #print(f'--->{valorIzq}, {valorDer}')
        if TIPO_DATO.INTEGER == valorIzq.tipo and TIPO_DATO.INTEGER == valorDer.tipo:
            if TIPO_OPERACION.SUMA == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor + valorDer.valor, TIPO_DATO.INTEGER)
            elif TIPO_OPERACION.RESTA == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor - valorDer.valor, TIPO_DATO.INTEGER)
            elif TIPO_OPERACION.MULTI == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor * valorDer.valor, TIPO_DATO.INTEGER)
            elif TIPO_OPERACION.DIV == self.tipo_operacion:
                if valorDer.valor == 0:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede dividir entre 0'))
                    print(f'No se puede dividir entre 0 >:(')
                    resultado = Retorno(0, TIPO_DATO.INTEGER)
                else:
                    resultado = Retorno(int(valorIzq.valor / valorDer.valor), TIPO_DATO.INTEGER)
            elif TIPO_OPERACION.MOD == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor % valorDer.valor, TIPO_DATO.INTEGER)
        elif TIPO_DATO.FLOAT == valorIzq.tipo and TIPO_DATO.FLOAT == valorDer.tipo:
            if TIPO_OPERACION.SUMA == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor + valorDer.valor, TIPO_DATO.FLOAT)
            elif TIPO_OPERACION.RESTA == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor - valorDer.valor, TIPO_DATO.FLOAT)
            elif TIPO_OPERACION.MULTI == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor * valorDer.valor, TIPO_DATO.FLOAT)
            elif TIPO_OPERACION.DIV == self.tipo_operacion:
                if valorDer.valor == 0:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede dividir entre 0'))
                    print(f'No se puede dividir entre 0 >:(')
                    resultado = Retorno(0, TIPO_DATO.FLOAT)
                else:
                    resultado = Retorno(valorIzq.valor / valorDer.valor, TIPO_DATO.FLOAT)
            elif TIPO_OPERACION.MOD == self.tipo_operacion:
                resultado = Retorno(valorIzq.valor % valorDer.valor, TIPO_DATO.FLOAT)
        elif TIPO_DATO.STRING == valorIzq.tipo and TIPO_DATO.RSTR == valorDer.tipo:
                if TIPO_OPERACION.SUMA == self.tipo_operacion:
                    resultado = Retorno(valorIzq.valor + valorDer.valor, TIPO_DATO.STRING)
                    return resultado
                else:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Operacion no permitida'))
                    print(f'Arit: Operacion no permitida')
                    resultado = Retorno(0, TIPO_DATO.INTEGER)
                return resultado
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Los tipos de datos no coinciden'))
            print(f'Los tipos de datos no coinciden {valorIzq.tipo}!={valorDer.tipo}')
            resultado = Retorno(0, TIPO_DATO.INTEGER)
        return resultado