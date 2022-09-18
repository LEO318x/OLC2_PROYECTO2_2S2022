from Abstract.Instruccion import Instruccion


class Main(Instruccion):
    def __init__(self, fila, columna, linstrucciones):
        super().__init__(fila, columna)
        self.linstrucciones = linstrucciones

    def ejecutar(self, entorno):
        for m in self.linstrucciones:
            m.ejecutar(entorno)