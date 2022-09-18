from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Reporte.Reportes import lsimbolos
from Simbolo.Arreglo import Arreglo
from Simbolo.Simbolo import Simbolo
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
            #index += 1
            arr.setAtributo(Simbolo('', valor.valor, valor.tipo, None))
        return Retorno(arr, TIPO_DATO.ARRAY)
