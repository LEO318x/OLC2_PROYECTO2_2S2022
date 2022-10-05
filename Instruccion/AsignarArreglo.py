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

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio Asignacion Arreglo")
        nuevoValor = self.valor.traducir(entorno, C3D)
        anterior = self.anterior.traducir(entorno, C3D)
        indice = self.indice.traducir(entorno, C3D)
        t = C3D.nueva_temporal()
        C3D.agregar_codigo(f'{t} = {anterior.valor};')
        C3D.agregar_codigo(f'{t} = {t} + 1;')
        C3D.agregar_codigo(f'{t} = {t} + {indice.valor};')
        C3D.agregar_codigo(f'heap[(int){t}] = {nuevoValor.valor};')
        C3D.comentario("Fin Asignacion Arreglo")
        print(f'Asig Arr | anterior.v: {anterior.valor} indice.v{indice.valor}')