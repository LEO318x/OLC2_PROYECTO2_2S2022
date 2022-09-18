from Abstract.Expresion import Expresion
from Abstract.Retorno import Retorno
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO


class AccesoArregloVector(Expresion):
    def __init__(self, fila, columna, anterior, indice):
        super().__init__(fila, columna)
        self.anterior = anterior
        self.indice = indice

    def ejecutar(self, entorno):
        #print(f'ACCARR: {self.anterior}')
        anterior = self.anterior.ejecutar(entorno)
        #print(f'anterior: {anterior.valor}')
        if anterior.tipo == TIPO_DATO.ARRAY or anterior.tipo == TIPO_DATO.VECT:
            indice = self.indice.ejecutar(entorno)
            #print(f'Acceso_Arreglo: anterior {anterior.valor}')
            if indice.tipo != TIPO_DATO.INTEGER:
                lerrores.append(
                    Error(self.fila, self.columna, entorno.nombre, 'El indice nos es númerico'))
                print(f'Acceso_Arreglo_Error: El indice no es númerico')
                return Retorno("Error", TIPO_DATO.ERROR)
            #print(f'anterior: {anterior.valor}')
            if indice.valor < anterior.valor.getTamanio():
                valor = anterior.valor.getAtributo(indice.valor)
            else:
                lerrores.append(
                    Error(self.fila, self.columna, entorno.nombre, 'Indice del arreglo o vector fuera de los límites'))
                print(f'Acceso_Arreglo_Error: Indice del arreglo o vector fuera de los límites')
                return Retorno("Error", TIPO_DATO.ERROR)
            return Retorno(valor.valor, valor.tipo)
        else:
            lerrores.append(
                Error(self.fila, self.columna, entorno.nombre, 'No es un arreglo o vector'))
            print(f'Acceso_Arreglo_Error: No es un arreglo o vector')
            return Retorno("Error", TIPO_DATO.ERROR)
