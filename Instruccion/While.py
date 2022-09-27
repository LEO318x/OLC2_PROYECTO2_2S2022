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

    def traducir(self, entorno, C3D):
        C3D.comentario("Inicio While")
        nuevoEntorno = Entorno("While", entorno)
        etiqueta_while = C3D.nuevo_label()
        lbreak = C3D.nuevo_label()
        lcontinue = C3D.nuevo_label()

        C3D.agregar_label(etiqueta_while)
        condicion = self.condicion.traducir(nuevoEntorno, C3D)
        truelabel = condicion.true_label
        falselabel = condicion.false_label

        C3D.agregar_label(truelabel)
        print(f'codigo: {self.codigo}')
        elemento = self.codigo.traducir(nuevoEntorno, C3D)
        print(f'while elemento {elemento}')
        if elemento is not None:
            if elemento.tipo == TIPO_DATO.BREAK:
                C3D.comentario("BREAK")
                C3D.agregar_goto(lbreak)
            elif elemento.tipo == TIPO_DATO.CONTINUE:
                C3D.comentario("CONTINUE")
                C3D.agregar_goto(etiqueta_while)
        C3D.agregar_goto(etiqueta_while)
        C3D.agregar_label(falselabel)
        C3D.agregar_label(lbreak)


        # print(f'While {condicion}, valor: {condicion.valor} tipo: {condicion.tipo}')
        C3D.comentario("Fin While")
        #return elemento
