from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Simbolo import C3D_Value
from Simbolo.Tipo import TIPO_DATO


class Casteo(Instruccion):
    def __init__(self, fila, columna, tipo_a_convertir, valor):
        super().__init__(fila, columna)
        self.exprIzq = valor
        self.tipo_convertir = tipo_a_convertir

    def ejecutar(self, entorno):
        exprIzq = self.exprIzq.ejecutar(entorno)
        #print(f'casteo: {exprIzq}')
        if self.tipo_convertir == TIPO_DATO.INTEGER:
            try:
                tmpvalor = int(exprIzq.valor)
                return Retorno(tmpvalor, TIPO_DATO.INTEGER)
            except:
                print(f'Error no se puede convertir el tipo de dato a integer')
        elif self.tipo_convertir == TIPO_DATO.FLOAT:
            try:
                tmpvalor = float(exprIzq.valor)
                return Retorno(tmpvalor, TIPO_DATO.FLOAT)
            except:
                print(f'Error no se puede convertir el tipo de dato a float')
        elif self.tipo_convertir == TIPO_DATO.CHAR:
            try:
                tmpvalor = chr(exprIzq.valor)
                return Retorno(tmpvalor, TIPO_DATO.CHAR)
            except:
                print(f'Error no se puede convertir el tipo de dato a char')
        elif self.tipo_convertir == TIPO_DATO.BOOL:
            try:
                tmpvalor = bool(exprIzq.valor)
                return Retorno(tmpvalor, TIPO_DATO.BOOL)
            except:
                print(f'Error no se puede convertir el tipo de dato a bool')

    def traducir(self, entorno, C3D):
        exprIzq = self.exprIzq.traducir(entorno, C3D)
        #print(f'casteo: {exprIzq}')
        if self.tipo_convertir == TIPO_DATO.INTEGER:
            try:
                # tmpvalor = int(exprIzq.valor)
                tmpvalor = exprIzq.valor
                return C3D_Value(tmpvalor, False, TIPO_DATO.INTEGER, None, None)
            except:
                print(f'Error no se puede convertir el tipo de dato a integer')
        elif self.tipo_convertir == TIPO_DATO.FLOAT:
            try:
                # tmpvalor = float(exprIzq.valor)
                tmpvalor = exprIzq.valor
                return C3D_Value(tmpvalor, False, TIPO_DATO.FLOAT, None, None)
            except:
                print(f'Error no se puede convertir el tipo de dato a float')
        elif self.tipo_convertir == TIPO_DATO.CHAR:
            try:
                # tmpvalor = chr(exprIzq.valor)
                tmpvalor = exprIzq.valor
                return C3D_Value(tmpvalor, False, TIPO_DATO.CHAR, None, None)
            except:
                print(f'Error no se puede convertir el tipo de dato a char')
        elif self.tipo_convertir == TIPO_DATO.BOOL:
            try:
                # tmpvalor = bool(exprIzq.valor)
                tmpvalor = exprIzq.valor
                return C3D_Value(tmpvalor, False, TIPO_DATO.BOOL, None, None)
            except:
                print(f'Error no se puede convertir el tipo de dato a bool')
