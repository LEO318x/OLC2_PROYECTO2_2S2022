from Abstract.Instruccion import Instruccion
from Simbolo.Entorno import Entorno


class Llamar(Instruccion):
    def __init__(self, fila, columna, id, parametros):
        super().__init__(fila, columna)
        self.id = id
        self.parametros = parametros

    def ejecutar(self, entorno):
        #print(f'llamar_ejec {self.id}')
        func = entorno.getFuncion(self.id)
        if func != None:
            nuevoEntorno = Entorno(self.id, entorno.getGlobal())

            for i in range(len(self.parametros)):
                #print(f'{i}')
                valor = self.parametros[i].ejecutar(entorno)
                funcparvalor = func.parametros[i].id
                funcpartipo = func.parametros[i].tipo
                if valor.tipo == funcpartipo:
                    nuevoEntorno.guardar_var_tipo(funcparvalor, valor.valor, funcpartipo, False)
                else:
                    print(f'El parametro ingresado no coincide con el definido en la función')
                #print(f'llamar_val: {funcparvalor}, {funcpartipo}, {valor.valor}')
            func.sentencia.ejecutar(nuevoEntorno)

    def traducir(self, entorno, C3D):

        print(f'func traducir: {self.id}')
        func = entorno.c3d_getFuncion(self.id)
        print(f'func3d {func}')
        if func != None:
            nuevoEntorno = Entorno(self.id, entorno.getGlobal())


            tmpauxpar = ""
            for i in range(len(self.parametros)):
                valor = self.parametros[i].traducir(entorno, C3D)
                funcparvalor = func.parametros[i].id
                funcpartipo = func.parametros[i].tipo
                pos = C3D.sumar_stack()
                tamanio = 1
                nuevoEntorno.c3d_guardar_var_tipo(funcparvalor, valor.valor, funcpartipo, pos, tamanio)
                tmpauxpar += f'stack[(int) {pos}] = {valor.valor};\n'
                print(f'llamar func: valor: {valor.valor}, tipo: {funcpartipo}, pos: {pos}')

            C3D.agregar_codigo(f'void {self.id}()' + '{')
            func.sentencia.traducir(nuevoEntorno, C3D)
            C3D.agregar_codigo('return;')
            C3D.agregar_codigo('}')

            C3D.comentario(f'Inicio llamada a funcion')
            C3D.agregar_codigo(f'{tmpauxpar}')
            C3D.agregar_codigo(f'{self.id}();')
            C3D.comentario(f'Fin llamada a funcion')
