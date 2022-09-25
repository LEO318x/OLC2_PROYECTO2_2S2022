from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Simbolo import C3D_Value


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
            #print(f'Acc_Eje: {valor}')
            C3D.comentario("Inicio variable")
            nueva_t = C3D.nueva_temporal()
            C3D.agregar_getstack(nueva_t, valor.posicion)
            C3D.comentario("Fin variable")
            return C3D_Value(nueva_t, True, valor.tipo, None, None)
        else:
            lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'La variable no existe'))
            print(f'Error_Acc, la variable "{self.id}" no existe')
            return None
