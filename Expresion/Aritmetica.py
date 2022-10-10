import math

from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
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

    def traducir(self, entorno, C3D):
        if self.unaria:
            nueva_temp = C3D.nueva_temporal()
            expr = self.exprDer.traducir(entorno, C3D)
            if TIPO_DATO.INTEGER == expr.tipo:
                C3D.agregar_expresion(nueva_temp, expr.valor, -1, "*")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_DATO.FLOAT == expr.tipo:
                C3D.agregar_expresion(nueva_temp, expr.valor, -1, "*")
                return C3D_Value(nueva_temp, True, TIPO_DATO.FLOAT, "", "")

        valorIzq = self.exprIzq.traducir(entorno, C3D)
        valorDer = self.exprDer.traducir(entorno, C3D)

        # print(f'--->{self.fila}, {self.columna}')
        # print(f'--->{valorIzq}, {valorDer}')
        nueva_temp = C3D.nueva_temporal()
        if TIPO_DATO.INTEGER == valorIzq.tipo and TIPO_DATO.INTEGER == valorDer.tipo:
            if TIPO_OPERACION.SUMA == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "+")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.RESTA == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "-")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.MULTI == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "*")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.DIV == self.tipo_operacion:
                if valorDer.valor == "0":
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede dividir entre 0'))
                    print(f'No se puede dividir entre 0 >:(')

                sal = C3D.nuevo_label()
                v = C3D.nuevo_label()
                f = C3D.nuevo_label()

                C3D.agregar_if(valorDer.valor, 0, "==", v)
                C3D.agregar_goto(f)

                C3D.agregar_label(v)
                #Instrucciones si cond verdadera
                C3D.agregar_codigo(f'print_err_div();')
                C3D.agregar_expresion(nueva_temp, -1, 1, "/")
                C3D.agregar_goto(sal)

                C3D.agregar_label(f)
                #Instrucciones si cond falsa
                if valorDer.valor != "0":
                    C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "/")
                C3D.agregar_label(sal)

                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.MOD == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, f'(int){valorIzq.valor}', f'(int){valorDer.valor}', "%")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
        elif TIPO_DATO.FLOAT == valorIzq.tipo and TIPO_DATO.FLOAT == valorDer.tipo:
            if TIPO_OPERACION.SUMA == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "+")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.RESTA == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "-")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.MULTI == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "*")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
            elif TIPO_OPERACION.DIV == self.tipo_operacion:
                if valorDer.valor == "0":
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede dividir entre 0'))
                    print(f'No se puede dividir entre 0 >:(')

                sal = C3D.nuevo_label()
                v = C3D.nuevo_label()
                f = C3D.nuevo_label()

                C3D.agregar_if(valorDer.valor, 0, "==", v)
                C3D.agregar_goto(f)

                C3D.agregar_label(v)
                # Instrucciones si cond verdadera
                C3D.agregar_codigo(f'print_err_div();')
                C3D.agregar_expresion(nueva_temp, -1, 1, "/")
                C3D.agregar_goto(sal)

                C3D.agregar_label(f)
                # Instrucciones si cond falsa
                if valorDer.valor != "0":
                    C3D.agregar_expresion(nueva_temp, valorIzq.valor, valorDer.valor, "/")
                C3D.agregar_label(sal)

                return C3D_Value(nueva_temp, True, TIPO_DATO.FLOAT, "", "")
            elif TIPO_OPERACION.MOD == self.tipo_operacion:
                C3D.agregar_expresion(nueva_temp, f'(int){valorIzq.valor}', f'(int){valorDer.valor}', "%")
                return C3D_Value(nueva_temp, True, TIPO_DATO.INTEGER, "", "")
        elif TIPO_DATO.STRING == valorIzq.tipo or TIPO_DATO.RSTR == valorDer.tipo:
            if TIPO_OPERACION.SUMA == self.tipo_operacion:
                print(f'Concat izq: {valorIzq.valor} istemp: {valorIzq.istemp} | der: {valorDer.valor} istemp: {valorDer.istemp}')
                C3D.comentario("Inicio concatenacion")
                if valorIzq.istemp is False:
                    t = C3D.nueva_temporal()
                    pos = C3D.sumar_stack()
                    C3D.agregar_string(t, valorIzq.valor)
                    C3D.agregar_setstack(pos, t)
                    valorIzq.valor = t

                if valorDer.istemp is False:
                    t = C3D.nueva_temporal()
                    pos = C3D.sumar_stack()
                    C3D.agregar_string(t, valorDer.valor)
                    C3D.agregar_setstack(pos, t)
                    valorDer.valor = t

                C3D.agregar_codigo(f'P = P + {C3D.get_stack()};')
                C3D.agregar_codigo(f't3 = {valorIzq.valor};')
                C3D.agregar_codigo(f't4 = {valorDer.valor};')
                C3D.agregar_codigo(f'concatenar_string();')
                C3D.agregar_codigo(f'{nueva_temp} = stack[(int) P];')
                C3D.agregar_codigo(f'P = P - {C3D.get_stack()};')
                C3D.comentario("Fin concatenacion")
                return C3D_Value(nueva_temp, True, TIPO_DATO.STRING, None, None)
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Operacion no permitida'))
                print(f'Arit: Operacion no permitida')
            return C3D_Value(-1, True, TIPO_DATO.ERROR, None, None)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Los tipos de datos no coinciden'))
            print(f'Los tipos de datos no coinciden {valorIzq.tipo}!={valorDer.tipo}')
            resultado = Retorno(0, TIPO_DATO.INTEGER)
        return resultado