import Simbolo.Struct
from Abstract.Instruccion import Instruccion
from Simbolo.Tipo import TIPO_DATO


class BuscarTipo(Instruccion):
    def __init__(self, fila, columna, tipo):
        super().__init__(fila, columna)
        self.tipo = tipo

    def ejecutar(self, entorno):
        tipo = ""
        match self.tipo:
            case 'i64':
                tipo = TIPO_DATO.INTEGER
            case 'f64':
                tipo = TIPO_DATO.FLOAT
            case 'bool':
                tipo = TIPO_DATO.BOOL
            case 'String':
                tipo = TIPO_DATO.STRING
            case '&str':
                tipo = TIPO_DATO.RSTR
            case 'char':
                tipo = TIPO_DATO.CHAR
            case _:
                envGlobal = entorno.getGlobal()
                print(f'buscar_tipo:{self.tipo}')
                if envGlobal.getDefEstructura(self.tipo) is not None:
                    valor = envGlobal.getDefEstructura(self.tipo)
                    if isinstance(valor, Simbolo.Struct.Struct):
                        tipo = TIPO_DATO.STRUCT
                else:
                    tipo = TIPO_DATO.TYPE
        return tipo
