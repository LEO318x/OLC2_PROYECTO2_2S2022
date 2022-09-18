from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO
from Simbolo.Vector import Vector
from Simbolo.Simbolo import Simbolo


class NuevoVector(Expresion):
    def __init__(self, fila, columna, listaexpresiones, capacidad_max=None):
        super().__init__(fila, columna)
        self.listaexpresiones = listaexpresiones
        self.tipo = None
        self.capacidad_maxima = capacidad_max

    def ejecutar(self, entorno):
        lexpresiones = self.listaexpresiones
        capacidadmax = 0
        if self.capacidad_maxima is not None:
            tmpcap = self.capacidad_maxima.ejecutar(entorno)
            capacidadmax = tmpcap.valor

        vect = Vector()
        vect.setCapacidadMax(capacidadmax)

        for expresion in lexpresiones:
            valor = expresion.ejecutar(entorno)
            vect.setAtributo(Simbolo('', valor.valor, valor.tipo, None))
        return Retorno(vect, TIPO_DATO.VECT)
