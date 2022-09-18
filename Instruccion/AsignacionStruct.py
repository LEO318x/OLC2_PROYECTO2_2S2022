from Abstract.Expresion import Expresion
from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import Simbolo
from Simbolo.Tipo import TIPO_DATO


class AsignacionStruct(Instruccion):
    def __init__(self, fila, columna, ids, expresion):
        super().__init__(fila, columna)
        self.ids = ids
        self.expresion = expresion

    def ejecutar(self, entorno):
        #print(f'ids{self.ids}')
        valor = self.expresion.ejecutar(entorno)
        simbolo = entorno.getVar(self.ids[0])
        if simbolo.mutable:
            for i in range(1, len(self.ids) - 1):
                if simbolo.tipo == TIPO_DATO.STRUCT:
                    simbolo = simbolo.valor.get(self.ids[i])
                #print(f'asigstruct: simbv: {simbolo.valor} simb: {simbolo.tipo} vvalor: {valor.valor} vtipo: {valor.tipo}')

            ultimo = self.ids[len(self.ids)-1]
            if ultimo in simbolo.valor:
                if simbolo.valor.get(ultimo).tipo == valor.tipo:
                    simbolo.valor.update({ultimo: valor})
                else:
                    print(f'Error_AsigStruct: Tipo de dato no coincide con el definido en el struct')
            else:
                print(f'Error_AsigStruct: El campo no existe en el struct, no se puede editar')
        else:
            print(f'Error_AsigStruct: La estructura no es mutable')
        pass
