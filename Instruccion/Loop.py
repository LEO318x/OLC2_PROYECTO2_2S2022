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

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio Loop")
        nuevoEntorno = Entorno("Loop", entorno)

        l1 = C3D.nuevo_label()
        l2 = C3D.nuevo_label()
        l3 = C3D.nuevo_label()

        tcontinue = C3D.nuevo_label()
        C3D.agregar_continue(tcontinue)
        C3D.agregar_label(C3D.obtener_continue())

        C3D.agregar_label(l1)
        C3D.agregar_if(0, 1, "<", l2)
        C3D.agregar_goto(l3)
        C3D.agregar_label(l2)
        # Instrucciones
        elemento = self.codigo.traducir(nuevoEntorno, C3D)
        C3D.agregar_goto(l1)
        C3D.agregar_label(l3)
        if C3D.obtener_break() is not None:
            C3D.agregar_label(C3D.obtener_break())
            C3D.limpiar_break()

        C3D.comentario("Fin Loop")
        return None