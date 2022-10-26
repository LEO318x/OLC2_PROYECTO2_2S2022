import math

from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Sqrt(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        if expr.valor > 0:
            if expr.tipo == TIPO_DATO.FLOAT:
                return Retorno(math.sqrt(expr.valor), TIPO_DATO.FLOAT)
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede operar'))
                print(f'Error_Sqrt: No se puede operar')
                return Retorno(0, TIPO_DATO.INTEGER)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede operar número negativo en raíz'))
            print(f'Error_Sqrt: No se puede operar número negativo en raíz')
            return Retorno(0, TIPO_DATO.INTEGER)

    def traducir(self, entorno, C3D):
        expr = self.expresion.traducir(entorno, C3D)

        C3D.comentario("Inicio raíz cuadrada")
        cont = C3D.nueva_temporal()
        sqrt = C3D.nueva_temporal()
        temp = C3D.nueva_temporal()


        # while(sqrt!=temp){
        # temp = sqrt;
        # sqrt = (number/temp+temp)/2;
        # }

        l1 = C3D.nuevo_label()
        l2 = C3D.nuevo_label()
        l3 = C3D.nuevo_label()

        number = expr.valor;
        C3D.agregar_codigo(f'{sqrt} = {number} / 2;')
        C3D.agregar_codigo(f'{temp} = 0;')
        C3D.agregar_label(l1)
        C3D.agregar_if(sqrt, temp, "!=", l2)
        C3D.agregar_goto(l3)
        C3D.agregar_label(l2)
        C3D.agregar_codigo(f'{temp} = {sqrt};')
        t1 = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{t1} = {number} / {temp};')
        t2 = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{t2} = {t1} + {temp};')
        t3 = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{t3} = {t2} / 2;')
        C3D.agregar_codigo(f'{sqrt} = {t3};')
        C3D.agregar_goto(l1)
        C3D.agregar_label(l3)
        C3D.comentario("Fin de raíz cuadrada")
        return C3D_Value(sqrt, True, TIPO_DATO.FLOAT, None, None)
