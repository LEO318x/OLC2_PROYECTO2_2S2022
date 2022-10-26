from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Abs(Instruccion):
    def __init__(self, fila, columna, expresion):
        super().__init__(fila, columna)
        self.expresion = expresion

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)
        if expr.tipo == TIPO_DATO.INTEGER:
            return Retorno(abs(expr.valor), TIPO_DATO.INTEGER)
        elif expr.tipo == TIPO_DATO.FLOAT:
            return Retorno(abs(expr.valor), TIPO_DATO.FLOAT)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'No se puede operar'))
            print(f'Error_Abs: No se puede operar')
            return Retorno(0, TIPO_DATO.INTEGER)

    def traducir(self, entorno, C3D):
        expr = self.expresion.traducir(entorno, C3D)
        tmp = C3D.nueva_temporal()
        verdadero = C3D.nuevo_label()
        falsa = C3D.nuevo_label()
        salida = C3D.nuevo_label()

        print(f'abs valor: {expr.valor} tipo: {expr.tipo} truel: {expr.true_label} falsel: {expr.false_label}')
        C3D.comentario("Inicio valor absoluto")
        C3D.agregar_if(expr.valor, "-1", "<=", verdadero)
        C3D.agregar_goto(falsa)

        C3D.agregar_label(verdadero)
        C3D.agregar_codigo(f'{tmp} = {expr.valor} * -1;')
        C3D.agregar_goto(salida)

        C3D.agregar_label(falsa)
        C3D.agregar_codigo(f'{tmp} = {expr.valor} * 1;')

        C3D.agregar_label(salida)
        C3D.comentario("Fin valor absoluto")

        return C3D_Value(tmp, True, expr.tipo, None, None)