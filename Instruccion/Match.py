from Abstract.Instruccion import Instruccion


class Match(Instruccion):
    def __init__(self, fila, columna, expre, lmatch):
        super().__init__(fila, columna)
        self.expre = expre
        self.lmatch = lmatch

    def ejecutar(self, entorno):
        print(f'Match_Expre: {self.expre}')
        print(f'Match_Lmatch: {self.lmatch[0][0].ejecutar(entorno)}')
        pass