from Abstract.Instruccion import Instruccion
from Simbolo.Entorno import Entorno
from Simbolo.Tipo import TIPO_DATO


class Loop(Instruccion):
    def __init__(self, fila, columna, codigo):
        super().__init__(fila, columna)
        self.codigo = codigo

    def ejecutar(self, entorno):
        nuevoEntorno = Entorno("Loop", entorno)
        while True:
            elemento = self.codigo.ejecutar(nuevoEntorno)
            if elemento is not None:
                if elemento.tipo == TIPO_DATO.BREAK:
                    break
                elif elemento.tipo == TIPO_DATO.CONTINUE:
                    continue
                else:
                    # print(f'while_ejec_elem: {elemento.tipo}')
                    return elemento