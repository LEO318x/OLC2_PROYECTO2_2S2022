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
