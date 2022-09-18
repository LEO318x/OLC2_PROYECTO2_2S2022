from Abstract.Instruccion import Instruccion
from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import Simbolo
from Simbolo.Tipo import TIPO_DATO

class AsignarArreglo(Instruccion):
    def __init__(self, fila, columna, anterior, indice, valor):
        super().__init__(fila, columna)
        self.anterior = anterior
        self.indice = indice
        self.valor = valor

    def ejecutar(self, entorno):
        #print(f'nuevov: {self.anterior}, indice: {self.indice}, valor: {self.valor}')
        nuevoValor = self.valor.ejecutar(entorno)
        anterior = self.anterior.ejecutar(entorno)
        # print(f'anterior: {anterior.valor}')
        if anterior.tipo != TIPO_DATO.ARRAY:
            print(f'Acceso_Arreglo_Error: No es un arreglo')
            return Retorno("Error", TIPO_DATO.ERROR)
        indice = self.indice.ejecutar(entorno)
        # print(f'Acceso_Arreglo: anterior {anterior.valor}')
        if indice.tipo != TIPO_DATO.INTEGER:
            print(f'Acceso_Arreglo_Error: El indice no es númerico')
            return Retorno("Error", TIPO_DATO.ERROR)
        if indice.valor < anterior.valor.getTamanio():
            #print(f'AsigArreglo: {indice.valor}, nue: {nuevoValor.valor}')
            valor = anterior.valor.setAtributoConIndex(indice.valor, Simbolo('', nuevoValor.valor, nuevoValor.tipo, None))
        else:
            print(f'Acceso_Arreglo_Error: Indice del arreglo fuera de los límites')
            return Retorno("Error", TIPO_DATO.ERROR)