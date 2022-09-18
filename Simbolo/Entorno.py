# from Tipo import TIPO_DATO
from Simbolo.Simbolo import Simbolo


class Entorno:
    def __init__(self, nombre, anterior=None):
        self.nombre = nombre
        self.variables = {}
        self.funciones = dict()
        self.estructuras = dict()
        self.anterior = anterior

    def guardar(self, id, valor, tipo, mutable):
        env = self
        # print(f'Env->{id, valor, tipo}')
        while env != None:
            if id in env.variables:
                # if mutable:
                env.variables.update({id: Simbolo(id, valor, tipo, mutable)})
                # else:
                # print(f'Err_Ent: La variable {id} no es mutable, no se puede modificar')
                return
            env = env.anterior
        self.variables.update({id: Simbolo(id, valor, tipo, mutable)})
        # print(f'Ent_var: {self.variables}')

    def guardar_var_tipo(self, id, valor, tipo, mutable):
        env = self
        # print(f'Env_var_tipo->{id, valor, tipo}')
        while env != None:
            if id in env.variables:
                env.variables.update({id: Simbolo(id, valor, tipo, mutable)})
                return
            env = env.anterior
        self.variables.update({id: Simbolo(id, valor, tipo, mutable)})
        # print(f'Ent_var: {self.variables}')

    def asignar_var(self, id, valor, tipo):
        env = self
        # print(f'Env_AsigVar->{id, valor, tipo}')
        while env is not None:
            if id in env.variables:
                tmpvar = env.variables.get(id)
                is_mut = tmpvar.mutable
                # print(f'Env_AsigVar->{tmpvar.tipo}')
                if is_mut:
                    env.variables.update({id: Simbolo(id, valor, tipo, is_mut)})
                    return
                else:
                    print(f'Err_Ent_AsigVar: La variable "{id}" no es mutable, no se puede modificar!')
                    return
                # print(f'{env.variables.get(id).mutable}')
            # else:
            # print(f'Err_Ent_Asig: La variable no existe')
            env = env.anterior
        if env is None:
            print(f'Err_Ent_Asig: La variable no existe')
            return
            # print(f'Ent_var: {self.variables}')

    def getVar(self, id):
        env = self
        # print(f'Env_getvar-> {id}, {env.variables}')
        while env != None:
            if id in env.variables:
                return env.variables.get(id)
            env = env.anterior
        return None

    def guardarFuncion(self, id, funcion):
        #print(f'ent_guardFuncion {id}, funcion: {funcion}')
        self.funciones.update({id: funcion})


    def getFuncion(self, id):
        env = self
        while env != None:
            if id in env.funciones:
                return env.funciones.get(id)
            env = env.anterior
        return None

    def guardarEstructura(self, id, struct):
        env = self
        if id in env.estructuras:
            print(f'Struct_Env_Error: Ya se encuentra una estructura con el mismo nombre')
        else:
            self.estructuras.update({id: struct})

    def getDefEstructura(self, id):
        env = self
        while env != None:
            if id in env.estructuras:
                return env.estructuras.get(id)
            env = env.anterior
        return None


    def getGlobal(self):
        env = self
        while env.anterior != None:
            env = env.anterior
        return env
