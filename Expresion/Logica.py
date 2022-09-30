from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value
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

        # valorIzqt = self.exprIzq.traducir(entorno, C3D)
        # valorDert = self.exprDer.traducir(entorno, C3D)
        # print(f'Logica | Valor, Izq: {valorIzqt.valor} Der: {valorDert.valor}')
        if self.tipo_operacion == TIPO_LOGICO.OR:
            C3D.comentario("Inicio OR")
            valorIzq = self.exprIzq.traducir(entorno, C3D)
            C3D.agregar_label(valorIzq.false_label)
            valorDer = self.exprDer.traducir(entorno, C3D)
            C3D.comentario("Fin OR")
            return C3D_Value(None, False, TIPO_DATO.BOOL, f'{valorIzq.true_label}:\n{valorDer.true_label}', valorDer.false_label)
        elif self.tipo_operacion == TIPO_LOGICO.AND:
            C3D.comentario("Inicio AND")
            valorIzq = self.exprIzq.traducir(entorno, C3D)
            C3D.agregar_label(valorIzq.true_label)
            valorDer = self.exprDer.traducir(entorno, C3D)
            C3D.comentario("Fin AND")
            return C3D_Value(None, False, TIPO_DATO.BOOL, f'{valorDer.true_label}', f'{valorIzq.false_label}:\n{valorDer.false_label}')
        elif self.tipo_operacion == TIPO_LOGICO.NOT:
            C3D.comentario("Inicio NOT")
            valorDer = self.exprDer.traducir(entorno, C3D)
            if valorDer.valor == 1:
                valorDer.valor = 0
            else:
                valorDer.valor = 1
            print(f'logica valor {valorDer.valor}')
            print(f'Logica_Not | Valor, Der: {valorDer.valor}, true{valorDer.true_label}, false{valorDer.false_label}')
            C3D.comentario("Fin NOT")
            return C3D_Value(valorDer.valor, False, TIPO_DATO.BOOL, f'{valorDer.false_label}', f'{valorDer.true_label}')
            # if bool(valorIzq.valor) or bool(valorDer.valor):
            #     print(f'Logica | Valor, Izq: {valorIzq.valor} Der: {valorDer.valor}')
            #     return C3D_Value(1, False, TIPO_DATO.BOOL, verdadero, falso)
            # else:
            #     return C3D_Value(0, False, TIPO_DATO.BOOL, verdadero, falso)
