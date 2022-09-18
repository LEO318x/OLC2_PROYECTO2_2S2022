from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lsimbolos, lerrores
from Simbolo.Tipo import TIPO_DATO

class Declaracion(Instruccion):
    def __init__(self, id, valor, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.mutable = mutable

    def ejecutar(self, entorno):
        #print(f'Decla: {type(self.valor)}')
        val = self.valor.ejecutar(entorno)
        #print(f'Decla: {val.tipo}')
        lsimbolos.append((self.id, "Variable", val.tipo, entorno.nombre, self.fila, self.columna))
        entorno.guardar(self.id, val.valor, val.tipo, self.mutable)

class Declaracion_Tipo(Instruccion):
    def __init__(self, id, valor, tipo, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mutable = mutable

    def ejecutar(self, entorno):
        val = self.valor.ejecutar(entorno)
        #print(f'dec_tipo_ejec: {val.tipo}, -> {self.tipo}')
        if val.tipo == self.tipo:
            lsimbolos.append((self.id, "Variable", self.tipo, entorno.nombre, self.fila, self.columna))
            entorno.guardar_var_tipo(self.id, val.valor, self.tipo, self.mutable)
        else:
            print(f'Error_decla_tipo_ejecutar: La variable "{self.id}" a declarar no coincide con el tipo de dato {self.tipo} != {val.tipo}')
            lerrores.append(Error(self.fila, self.columna, 'Global', 'La variable a declarar no es del mismo tipo'))
        #print(f'Decla: {val.tipo}')

