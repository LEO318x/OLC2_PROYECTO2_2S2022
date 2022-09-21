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

    def traducir(self, entorno, entornoC3D):
        val = self.valor.traducir(entorno, entornoC3D)
        s_actual = entornoC3D.getS()
        t = entornoC3D.getT()
        entornoC3D.sumarT()

        tamanio = 0
        print(f'c3d_guardar_var: {self.id, val.valor, val.tipo, s_actual, tamanio}')
        entorno.c3d_guardar_var(self.id, val.valor, val.tipo, s_actual, tamanio)
        if val.tipo == TIPO_DATO.INTEGER or val.tipo == TIPO_DATO.FLOAT:
            entornoC3D.agregarTraduccion(f't{t} = P;')
            entornoC3D.agregarTraduccion(f't{t} = t{t} + 0;')
            entornoC3D.agregarTraduccion(f'stack[(int) t{t}] = {val.valor};')
        elif val.tipo == TIPO_DATO.STRING or val.tipo == TIPO_DATO.RSTR:
            entornoC3D.setCadenaTraduccion(val.valor)



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

    def traducir(self, entorno, entornoC3D):
        val = self.valor.traducir(entorno, entornoC3D)
        h_actual = entornoC3D.getS()
        entornoC3D.sumarS()
        tamanio = 0
        print(f'c3d_guardar_var: {self.id, val.valor, val.tipo, h_actual, tamanio}')
        entorno.c3d_guardar_var(self.id, val.valor, val.tipo, h_actual, tamanio)
