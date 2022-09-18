from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores


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
