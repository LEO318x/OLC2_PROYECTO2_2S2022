from Abstract.Instruccion import Instruccion


class Asignacion(Instruccion):
    def __init__(self, id, valor, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor

    def ejecutar(self, entorno):
        #print(f'asig_ejec: {self.id}')
        val = self.valor.ejecutar(entorno)
        #print(f'Asig: {self.valor}')
        entorno.asignar_var(self.id, val.valor, val.tipo)
