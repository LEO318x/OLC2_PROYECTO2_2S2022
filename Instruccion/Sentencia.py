from Abstract.Instruccion import Instruccion
from Simbolo.Entorno import Entorno


class Sentencia(Instruccion):
    def __init__(self, fila, columna, sentencias):
        super().__init__(fila, columna)
        self.sentencias = sentencias

    def ejecutar(self, entorno):
        nuevoEntorno = Entorno(entorno.nombre, entorno)
        for instr in self.sentencias:
            elemento = instr.ejecutar(nuevoEntorno)
            if elemento is not None:
                return elemento

    def traducir(self, entorno, C3D):
        nuevoEntorno = Entorno(entorno.nombre, entorno)
        for instr in self.sentencias:
            elemento = instr.traducir(nuevoEntorno, C3D)
            if elemento is not None:
                elemento = instr.traducir(nuevoEntorno, C3D)
                return elemento