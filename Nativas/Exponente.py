from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
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

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio Exponente")
        valorIzq = self.exprIzq.traducir(entorno, C3D)
        valorDer = self.exprDer.traducir(entorno, C3D)

        l1 = C3D.nueva_temporal()
        l2 = C3D.nueva_temporal()
        l3 = C3D.nueva_temporal()

        t1 = C3D.nueva_temporal()
        t2 = C3D.nueva_temporal()

        C3D.agregar_codigo(f'{t1} = {valorIzq.valor};')
        C3D.agregar_codigo(f'{t2} = {valorDer.valor};')

        numero = t1
        potencia = t2
        resultado = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{resultado} = {numero};')

        C3D.agregar_label(l1)
        C3D.agregar_if(potencia, "1", ">", l2)
        C3D.agregar_goto(l3)
        # instrucciones
        C3D.agregar_label(l2)
        C3D.agregar_codigo(f'{resultado} = {resultado} * {numero};')
        C3D.agregar_codigo(f'{potencia} = {potencia} - 1;')
        C3D.agregar_goto(l1)
        C3D.agregar_label(l3)
        C3D.comentario("Fin Exponente")
        return C3D_Value(resultado, True, valorIzq.tipo, None, None)