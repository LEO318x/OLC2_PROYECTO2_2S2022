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

    def traducir(self, entorno, C3D):
        valorIzq = self.exprIzq.traducir(entorno, C3D)
        valorDer = self.exprDer.traducir(entorno, C3D)

        if TIPO_LOGICO.AND == self.tipo_operacion:
            resultado = Retorno(valorIzq.valor and valorDer.valor, TIPO_DATO.BOOL)
            return resultado
        elif TIPO_LOGICO.OR == self.tipo_operacion:
            print(f'c3d_or_izq: {valorIzq.valor}')
            print(f'c3d_or_der: {valorDer.valor}')
            t_actual = t_actual = C3D.getT()
            C3D.sumarT()
            l1 = C3D.getNuevoL()
            l2 = C3D.getNuevoL()
            l3 = C3D.getNuevoL()
            l4 = C3D.getNuevoL()

            C3D.agregarTraduccion(f'if ({valorIzq.valor}) goto L{l1};')
            C3D.agregarTraduccion(f'goto L{l2};')

            C3D.agregarTraduccion(f'L{l2}:')
            C3D.agregarTraduccion(f'if ({valorDer.valor}) goto L{l3};')
            C3D.agregarTraduccion(f'goto L{l4};')
            C3D.agregarTraduccion(f'L{l1}:')
            C3D.agregarTraduccion(f'L{l3}:')
            resultado = Retorno(valorIzq.valor or valorDer.valor, TIPO_DATO.BOOL)
            return resultado