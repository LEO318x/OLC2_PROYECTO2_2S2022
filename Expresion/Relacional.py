from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value
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

    def traducir(self, entorno, C3D):
        valorIzq = self.exprIzq.traducir(entorno, C3D)
        valorDer = self.exprDer.traducir(entorno, C3D)

        if TIPO_RELACIONAL.MAYOR == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, ">", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)

        elif TIPO_RELACIONAL.MENOR == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, "<", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)

        elif TIPO_RELACIONAL.MAYORIGUAL == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, ">=", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)

        elif TIPO_RELACIONAL.MENORIGUAL == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, "<=", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)

        elif TIPO_RELACIONAL.IGUALACION == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, "==", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)

        elif TIPO_RELACIONAL.DISTINTO == self.tipo_operacion:
            temp = C3D.nueva_temporal()
            truelabel = C3D.nuevo_label()
            falselabel = C3D.nuevo_label()

            C3D.agregar_if(valorIzq.valor, valorDer.valor, "!=", truelabel)
            C3D.agregar_goto(falselabel)
            if valorIzq.valor < valorDer.valor:
                return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)
