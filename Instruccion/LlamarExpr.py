from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Entorno import Entorno
from Simbolo.Tipo import TIPO_DATO


class LlamarExpr(Instruccion):
    def __init__(self, fila, columna, id, parametros):
        super().__init__(fila, columna)
        self.id = id
        self.parametros = parametros

    def ejecutar(self, entorno):
        # print(f'llamar_ejec {self.id}')
        func = entorno.getFuncion(self.id)
        if func != None:
            nuevoEntorno = Entorno(self.id, entorno.getGlobal())
            tiporetorno = func.tipo_retorno
            for i in range(len(self.parametros)):
                # print(f'{i}')
                valor = self.parametros[i].ejecutar(entorno)
                funcparvalor = func.parametros[i].id
                funcpartipo = func.parametros[i].tipo

                #print(f'llamarexpr_ejec: {valor.tipo}, {funcpartipo}, retorno: {tiporetorno}')
                if valor.tipo == funcpartipo:
                    nuevoEntorno.guardar_var_tipo(funcparvalor, valor.valor, funcpartipo, False)
                else:
                    print(f'El parametro ingresado no coincide con el definido en la función')
                    return Retorno(-1, TIPO_DATO.ERROR)
                # print(f'llamar_val: {funcparvalor}, {funcpartipo}, {valor.valor}')
            valor = func.sentencia.ejecutar(nuevoEntorno)
            #print(f'llamar_expr_ejec: {valor.valor.tipo}, {tiporetorno}')
            valor_tiporetorno = valor.valor.tipo
            #print(f'verificar_retorno: {valor.tipo}')
            if valor_tiporetorno == tiporetorno:
                return valor.valor
            else:
                print(f'El valor de retorno no coincide con el definido en la función, {valor_tiporetorno} != {tiporetorno}')
                return Retorno(-1, TIPO_DATO.ERROR)

    def traducir(self, entorno, C3D):
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
