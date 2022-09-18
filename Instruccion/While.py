from Abstract.Instruccion import Instruccion
from Simbolo.Entorno import Entorno
from Simbolo.Tipo import TIPO_DATO


class While(Instruccion):
    def __init__(self, fila, columna, condicion, codigo):
        super().__init__(fila, columna)
        self.condicion = condicion
        self.codigo = codigo

    def ejecutar(self, entorno):
        #print(f'while_ejec: {self.condicion}')
        nuevoEntorno = Entorno("While", entorno)
        condicion = self.condicion.ejecutar(nuevoEntorno)

        if condicion.tipo != TIPO_DATO.BOOL:
            print(f'Error_If: La condición no es booleana, fila: {self.fila}, columna: {self.columna}')


        while condicion.valor == True:
            elemento = self.codigo.ejecutar(nuevoEntorno)
            if elemento is not None:
                if elemento.tipo == TIPO_DATO.BREAK:
                    break
                elif elemento.tipo == TIPO_DATO.CONTINUE:
                    continue
                else:
                    #print(f'while_ejec_elem: {elemento.tipo}')
                    return elemento
            condicion = self.condicion.ejecutar(nuevoEntorno)
            if condicion.tipo != TIPO_DATO.BOOL:
                print(f'La condición no es booleana, fila: {self.fila}, columna: {self.columna}')
