from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_RELACIONAL, TIPO_DATO, TIPO_LOGICO


class Logica(Expresion):
    def __init__(self, exprIzq, tipo_operacion, exprDer, fila, columna):
        self.exprIzq = exprIzq
        self.tipo_operacion = tipo_operacion
        self.exprDer = exprDer
        self.fila = fila
        self.columna = columna

    def ejecutar(self, entorno):
        if self.tipo_operacion == TIPO_LOGICO.NOT:
            valorDer = self.exprDer.ejecutar(entorno)
            return Retorno(not valorDer.valor, TIPO_DATO.BOOL)

        valorIzq = self.exprIzq.ejecutar(entorno)
        valorDer = self.exprDer.ejecutar(entorno)

        if TIPO_LOGICO.AND == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor and valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_LOGICO.OR == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor or valorDer.valor, TIPO_DATO.BOOL)
            return resultado