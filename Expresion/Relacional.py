from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_RELACIONAL, TIPO_DATO


class Relacional(Expresion):
    def __init__(self, exprIzq, tipo_operacion, exprDer, fila, columna):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        valorIzq = self.exprIzq.ejecutar(entorno)
        valorDer = self.exprDer.ejecutar(entorno)

        if TIPO_RELACIONAL.MAYOR == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor > valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_RELACIONAL.MENOR == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor < valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_RELACIONAL.MAYORIGUAL == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor >= valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_RELACIONAL.MENORIGUAL == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor <= valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_RELACIONAL.IGUALACION == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor == valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_RELACIONAL.DISTINTO == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor != valorDer.valor, TIPO_DATO.BOOL)
            return resultado
