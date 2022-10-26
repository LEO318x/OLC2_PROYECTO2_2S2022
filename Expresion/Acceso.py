from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Acceso(Expresion):
    def __init__(self, id, fila, columna):
        super().__init__(fila, columna)
        self.id = id

    def ejecutar(self, entorno):
        #print(f'id: {self.id}')
        valor = entorno.getVar(self.id)
        #print(f'Eje_Acc: {valor}, id: {self.id}')
        if valor is not None:
            #print(f'Acc_Eje: {valor}')
            return Retorno(valor.valor, valor.tipo)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'La variable no existe'))
            print(f'Error_Acc, la variable "{self.id}" no existe')
            return None

    def traducir(self, entorno, C3D):
        #print(f'id: {self.id}')
        valor = entorno.c3d_getVar(self.id)
        #print(f'Eje_Acc: {valor}, id: {self.id}')
        if valor is not None:
            print(f'Acc_Eje: {valor.valor}, tipo: {valor.tipo}')

            C3D.comentario("Inicio variable")
            if valor.tipo == TIPO_DATO.BOOL:
                truelabel = C3D.nuevo_label()
                falselabel = C3D.nuevo_label()
                if valor.valor == 1:
                    # C3D.agregar_goto(truelabel)
                    C3D.agregar_if(1, 0, ">", truelabel)
                    C3D.agregar_goto(falselabel)
                    return C3D_Value(1, False, TIPO_DATO.BOOL, truelabel, falselabel)
                elif valor.valor == 0:
                    # C3D.agregar_goto(falselabel)
                    C3D.agregar_if(0, 1, ">", truelabel)
                    C3D.agregar_goto(falselabel)
                    return C3D_Value(0, False, TIPO_DATO.BOOL, truelabel, falselabel)
            else:
                nueva_t = C3D.nueva_temporal()
                C3D.agregar_getstack(nueva_t, valor.posicion)
                C3D.comentario("Fin variable")
                if valor.tipo == TIPO_DATO.ARRAY:
                    return C3D_Value(nueva_t, True, valor.tipo, None, None, valor.tamanio)
                else:
                    return C3D_Value(nueva_t, True, valor.tipo, None, None)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'La variable no existe'))
            print(f'Error_Acc, la variable "{self.id}" no existe')
            return None
