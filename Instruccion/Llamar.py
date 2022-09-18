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
