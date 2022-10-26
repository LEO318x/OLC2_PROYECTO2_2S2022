from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Entorno import Entorno
from Simbolo.Tipo import TIPO_DATO


class ForIn(Instruccion):
    def __init__(self, fila, columna, identificador, expr1=None, expr2=None, instrucciones=None):
        super().__init__(fila, columna)
        self.id = identificador
        self.expr1 = expr1
        self.expr2 = expr2
        self.instrucciones = instrucciones

    def ejecutar(self, entorno):

        inicio = self.expr1.ejecutar(entorno)
        final = self.expr2.ejecutar(entorno)

        if inicio.tipo == TIPO_DATO.INTEGER:
            if final.tipo == TIPO_DATO.INTEGER:
                nuevo_entorno = Entorno("ForIn", entorno)
                for value in range(inicio.valor, final.valor):
                    nuevo_entorno.guardar_var_tipo(self.id, value, TIPO_DATO.INTEGER, True)
                    # print(f'forin_ejec: {self.instrucciones.ejecutar(nuevo_entorno)}')
                    elemento = self.instrucciones.ejecutar(nuevo_entorno)
                    if elemento is not None:
                        if elemento.tipo == TIPO_DATO.BREAK:
                            break
                        elif elemento.tipo == TIPO_DATO.CONTINUE:
                            continue
                        else:
                            # print(f'while_ejec_elem: {elemento.tipo}')
                            # return elemento
                            pass
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre,
                                      f'Error_ForIN: El limite inferior debe ser de: {TIPO_DATO.INTEGER} y NO {inicio.tipo}'))
                print(f'Error_ForIN: El limite inferior debe ser de: {TIPO_DATO.INTEGER} y NO {inicio.tipo}')
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre,
                                  f'Error_ForIN: El limite superior debe ser de: {TIPO_DATO.INTEGER} y NO {final.tipo}'))
            print(f'Error_ForIN: El limite superior debe ser de: {TIPO_DATO.INTEGER} y NO {final.tipo}')

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio For")

        inicio = self.expr1.traducir(entorno, C3D)
        final = self.expr2.traducir(entorno, C3D)

        if inicio.tipo == TIPO_DATO.INTEGER:
            if final.tipo == TIPO_DATO.INTEGER:
                nuevo_entorno = Entorno("ForIn", entorno)
                tamanio = 1
                pos = pos = C3D.sumar_stack()


                l1 = C3D.nuevo_label()
                l2 = C3D.nuevo_label()
                l3 = C3D.nuevo_label()

                tcontinue = C3D.nuevo_label()
                C3D.agregar_continue(tcontinue)
                C3D.agregar_label(C3D.obtener_continue())
                temp = C3D.nueva_temporal()
                nuevo_entorno.c3d_guardar_var_tipo(self.id, temp, TIPO_DATO.INTEGER, pos, tamanio)
                C3D.agregar_codigo(f'{temp} = {inicio.valor};')
                C3D.agregar_label(l1)
                C3D.agregar_setstack(pos, temp)
                C3D.agregar_if(temp, final.valor, "<", l2)
                C3D.agregar_goto(l3)
                C3D.agregar_label(l2)
                # Instrucciones
                elemento = self.instrucciones.traducir(nuevo_entorno, C3D)
                C3D.agregar_codigo(f'{temp} = {temp} + 1;')
                C3D.agregar_goto(l1)
                C3D.agregar_label(l3)
                if C3D.obtener_break() is not None:
                    C3D.agregar_label(C3D.obtener_break())
                    C3D.limpiar_break()

                C3D.comentario("Fin For")


class ForInAV(Instruccion):
    def __init__(self, fila, columna, identificador, expresion, instrucciones = None):
        super().__init__(fila, columna)
        self.id = identificador
        self.expresion = expresion
        self.instrucciones = instrucciones

    def ejecutar(self, entorno):
        expr = self.expresion.ejecutar(entorno)

        if expr.tipo == TIPO_DATO.ARRAY or expr.tipo == TIPO_DATO.VECT:
            valor = expr.valor
            tamanio = expr.valor.getTamanio()

            nuevo_entorno = Entorno("ForIn", entorno)
            for av in expr.valor.getAtributos():
                nuevo_entorno.guardar_var_tipo(self.id, av.valor, av.tipo, True)
                elemento = self.instrucciones.ejecutar(nuevo_entorno)
                if elemento is not None:
                    if elemento.tipo == TIPO_DATO.BREAK:
                        break
                    elif elemento.tipo == TIPO_DATO.CONTINUE:
                        continue
                    else:
                        # print(f'while_ejec_elem: {elemento.tipo}')
                        # return elemento
                        pass

