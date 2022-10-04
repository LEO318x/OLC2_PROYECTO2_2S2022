from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Reporte.Reportes import lsimbolos
from Simbolo.Arreglo import Arreglo
from Simbolo.Simbolo import Simbolo, C3D_Value
from Simbolo.Tipo import TIPO_DATO


class NuevoArreglo(Expresion):
    def __init__(self, fila, columna, listaexpre):
        super().__init__(fila, columna)
        self.listaexpre = listaexpre
        self.tipo = ""

    def ejecutar(self, entorno):
        lexpresiones = self.listaexpre
        #print(f'nuevo_arreglo: {lexpresiones}')
        arr = Arreglo()
        #index = 0

        for expresion in lexpresiones:
            valor = expresion.ejecutar(entorno)
            print(f'nuevo arreglo expre: {valor.tipo}')
            #index += 1
            arr.setAtributo(Simbolo('', valor.valor, valor.tipo, None))
        return Retorno(arr, TIPO_DATO.ARRAY)

    def traducir(self, entorno, C3D):
        lexpr = self.listaexpre
        C3D.comentario("Inicio Array")
        t = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{t} = H;')
        C3D.agregar_codigo(f'heap[(int)H] = {len(lexpr)};')
        C3D.agregar_codigo(f'H = H + 1;')
        for expr in lexpr:
            valor = expr.traducir(entorno, C3D)
            print(f'arr valor: {valor.valor}')
            C3D.agregar_codigo(f'heap[(int)H] = {valor.valor};')
            C3D.agregar_codigo(f'H = H + 1;')
        C3D.comentario("Fin Array")
        return C3D_Value(t, True, TIPO_DATO.ARRAY, None, len(lexpr))
