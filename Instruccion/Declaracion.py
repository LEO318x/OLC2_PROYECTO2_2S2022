from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lsimbolos, lerrores, lsimbolosc3d
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
            if val.istemp:
                pos = C3D.sumar_stack()
                entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, 0)
                C3D.agregar_setstack(pos, val.valor)
            else:
                tamanio = len(val.valor)
                t = C3D.nueva_temporal()
                pos = C3D.sumar_stack()
                entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, tamanio)
                C3D.agregar_string(t, val.valor)
                C3D.agregar_setstack(pos, t)
        elif val.tipo == TIPO_DATO.BOOL:
            print(f'decla bool {val.valor} istemp {val.istemp}')
            if val.istemp:
                tamanio = 1
                pos = C3D.sumar_stack()
                entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, tamanio)
                C3D.agregar_setstack(pos, val.valor)
            else:
                if val.true_label is None:
                    t = C3D.nueva_temporal()
                    val.true_label = t
                if val.false_label is None:
                    t = C3D.nueva_temporal()
                    val.false_label = t

                pos = C3D.sumar_stack()
                salida = C3D.nuevo_label()
                C3D.agregar_label(val.true_label)
                C3D.agregar_setstack(pos, 1)
                C3D.agregar_goto(salida)
                C3D.agregar_label(val.false_label)
                C3D.agregar_setstack(pos, 0)
                C3D.agregar_label(salida)
                entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, 0)
        elif val.tipo == TIPO_DATO.ARRAY:
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, val.false_label)
            C3D.agregar_setstack(pos, val.valor)
            print(f'decla array | id: {self.id} valor:{val.valor} tipo:{val.tipo}, tamanio:{val.false_label}')
            pass
                # pos = C3D.sumar_stack()
                # print(f'Decla_Bool: {val.valor}')

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
            lsimbolosc3d.append((self.id, "Variable", self.tipo, entorno.nombre, self.fila, self.columna))
            entorno.guardar_var_tipo(self.id, val.valor, self.tipo, self.mutable)
        else:
            print(
                f'Error_decla_tipo_ejecutar: La variable "{self.id}" a declarar no coincide con el tipo de dato {self.tipo} != {val.tipo}')
            lerrores.append(Error(self.fila, self.columna, 'Global', 'La variable a declarar no es del mismo tipo'))
        # print(f'Decla: {val.tipo}')

    def traducir(self, entorno, C3D):
        # print(f'Decla: {type(self.valor)}')
        val = self.valor.traducir(entorno, C3D)
        # print(f'Decla: {val.tipo}')
        lsimbolosc3d.append((self.id, "Variable", self.tipo, entorno.nombre, self.fila, self.columna))
        print(f'Decla: {val.tipo}')
        C3D.comentario("Inicio Declaracion")
        if self.tipo == TIPO_DATO.INTEGER or self.tipo == TIPO_DATO.FLOAT:
            tamanio = 1
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, self.tipo, pos, tamanio)
            C3D.agregar_setstack(pos, val.valor)
        elif self.tipo == TIPO_DATO.CHAR:
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, self.tipo, pos, 0)
            C3D.agregar_setstack(pos, ord(val.valor))
        elif self.tipo == TIPO_DATO.STRING or self.tipo == TIPO_DATO.RSTR:
            print(f"Decla_string: {self.tipo}, {val.valor}")
            tamanio = len(val.valor)
            t = C3D.nueva_temporal()
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, self.tipo, pos, tamanio)
            C3D.agregar_string(t, val.valor)
            C3D.agregar_setstack(pos, t)
        elif self.tipo == TIPO_DATO.BOOL:
            print(f'decla bool {val.valor} istemp {val.istemp}')
            if val.istemp:
                print(f'efecita')
                tamanio = 1
                if val.true_label is None:
                    t = C3D.nueva_temporal()
                    val.true_label = t
                if val.false_label is None:
                    t = C3D.nueva_temporal()
                    val.false_label = t
                pos = C3D.sumar_stack()
                salida = C3D.nuevo_label()
                C3D.agregar_label(val.true_label)
                C3D.agregar_setstack(pos, 1)
                C3D.agregar_goto(salida)
                C3D.agregar_label(val.false_label)
                C3D.agregar_setstack(pos, 0)
                C3D.agregar_label(salida)
                entorno.c3d_guardar_var(self.id, val.valor, self.tipo, pos, tamanio)

            else:
                if val.true_label is None:
                    t = C3D.nueva_temporal()
                    val.true_label = t
                if val.false_label is None:
                    t = C3D.nueva_temporal()
                    val.false_label = t
                pos = C3D.sumar_stack()
                salida = C3D.nuevo_label()
                C3D.agregar_label(val.true_label)
                C3D.agregar_setstack(pos, 1)
                C3D.agregar_goto(salida)
                C3D.agregar_label(val.false_label)
                C3D.agregar_setstack(pos, 0)
                C3D.agregar_label(salida)
                entorno.c3d_guardar_var(self.id, val.valor, self.tipo, pos, 1)
        elif val.tipo == TIPO_DATO.ARRAY:
            pos = C3D.sumar_stack()
            entorno.c3d_guardar_var(self.id, val.valor, val.tipo, pos, val.false_label)
            C3D.agregar_setstack(pos, val.valor)
            print(f'decla array | id: {self.id} valor:{val.valor} tipo:{val.tipo}, tamanio:{val.false_label}')

                # pos = C3D.sumar_stack()
                # print(f'Decla_Bool: {val.valor}')

        C3D.comentario("Fin Declaracion")
        return C3D_Value(None, False, TIPO_DATO.INTEGER, None, None)
