from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Reporte.Reportes import lsimbolos
from Simbolo.Simbolo import Simbolo
from Simbolo.Struct import Struct
from Simbolo.Tipo import TIPO_DATO


class DefStruct(Expresion):
    def __init__(self, fila, columna, nombre, atributos):
        super().__init__(fila, columna)
        self.nombre = nombre
        self.atributos = atributos

    def ejecutar(self, entorno):
        #print(f'nombre: {self.nombre}, atributos: {self.atributos}')
        newStruct = Struct()
        for atributo in self.atributos:
            newStruct.setAtributo(atributo)
        env = entorno.getGlobal()
        lsimbolos.append((self.nombre, "Struct", "TIPO_DATO.STRUCT", entorno.nombre, self.fila, self.columna))
        env.guardarEstructura(self.nombre, newStruct)
        #print(f"Struct: {newStruct.atributos}")
