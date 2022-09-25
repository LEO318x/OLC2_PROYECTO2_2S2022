from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lsimbolos, lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Declaracion(Instruccion):
    def __init__(self, id, valor, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.mutable = mutable

    def ejecutar(self, entorno):
        # print(f'Decla: {type(self.valor)}')
        val = self.valor.ejecutar(entorno)
        # print(f'Decla: {val.tipo}')
        lsimbolos.append((self.id, "Variable", val.tipo, entorno.nombre, self.fila, self.columna))
        entorno.guardar(self.id, val.valor, val.tipo, self.mutable)

    def traducir(self, entorno, C3D):
        # print(f'Decla: {type(self.valor)}')
        val = self.valor.traducir(entorno, C3D)
        # print(f'Decla: {val.tipo}')
        lsimbolos.append((self.id, "Variable", val.tipo, entorno.nombre, self.fila, self.columna))
        print(f'Decla: {val.tipo}')
        C3D.comentario("Inicio Declaracion")
        if val.tipo == TIPO_DATO.INTEGER or val.tipo == TIPO_DATO.FLOAT:
            tamanio = 1
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, tamanio)
            C3D.agregar_setstack(pos, val.valor)
        elif val.tipo == TIPO_DATO.CHAR:
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, 0)
            C3D.agregar_setstack(pos, ord(val.valor))
        elif val.tipo == TIPO_DATO.STRING or val.tipo == TIPO_DATO.RSTR:
            print(f"Decla_string: {val.tipo}, {val.valor}")
            tamanio = len(val.valor)
            t = C3D.nueva_temporal()
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, tamanio)
            C3D.agregar_string(t, val.valor)
            C3D.agregar_setstack(pos, t)
        elif val.tipo == TIPO_DATO.BOOL:
            salida = C3D.nuevo_label()
            pos = C3D.sumar_stack()
            print(f'Decla_Bool: {val.valor}')
            C3D.agregar_label(val.true_label)
            C3D.agregar_setstack(pos, 1)
            C3D.agregar_goto(salida)
            C3D.agregar_label(val.false_label)
            C3D.agregar_setstack(pos, 0)
            C3D.agregar_label(salida)
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, 0)
        C3D.comentario("Fin Declaracion")
        return C3D_Value(None, False, TIPO_DATO.INTEGER, None, None)



class Declaracion_Tipo(Instruccion):
    def __init__(self, id, valor, tipo, mutable, fila, columna):
        super().__init__(fila, columna)
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.mutable = mutable

    def ejecutar(self, entorno):
        val = self.valor.ejecutar(entorno)
        # print(f'dec_tipo_ejec: {val.tipo}, -> {self.tipo}')
        if val.tipo == self.tipo:
            lsimbolos.append((self.id, "Variable", self.tipo, entorno.nombre, self.fila, self.columna))
            entorno.guardar_var_tipo(self.id, val.valor, self.tipo, self.mutable)
        else:
            print(
                f'Error_decla_tipo_ejecutar: La variable "{self.id}" a declarar no coincide con el tipo de dato {self.tipo} != {val.tipo}')
            lerrores.append(Error(self.fila, self.columna, 'Global', 'La variable a declarar no es del mismo tipo'))
        # print(f'Decla: {val.tipo}')

    def traducir(self, entorno, C3D):
        pass
