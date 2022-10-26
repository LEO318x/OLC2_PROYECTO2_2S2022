from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


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

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio Asignacion")
        val = self.valor.traducir(entorno, C3D)
        if val.tipo == TIPO_DATO.INTEGER:
            var = entorno.c3d_getVar(self.id)
            C3D.agregar_setstack(var.posicion, val.valor)
        elif val.tipo == TIPO_DATO.FLOAT:
            var = entorno.c3d_getVar(self.id)
            C3D.agregar_setstack(var.posicion, val.valor)
        elif val.tipo == TIPO_DATO.CHAR:
            var = entorno.c3d_getVar(self.id)
            C3D.agregar_setstack(var.posicion, val.valor)
        elif val.tipo == TIPO_DATO.STRING or val.tipo == TIPO_DATO.RSTR:
            var = entorno.c3d_getVar(self.id)
            C3D.agregar_setstack(var.posicion, val.valor)
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
            # print(f'asignacion_traducir: {val}')
            var = entorno.c3d_getVar(self.id)
            # print(f'asignacion_traducir var: {var} pos: {var.posicion}')
            # print(f'asignacion_traducir valor {val.valor}')
            C3D.agregar_setstack(var.posicion, val.valor)
            #entorno.c3d_asignar_var(self.id, val.valor, val.tipo)
        C3D.comentario("Fin Asignacion")
