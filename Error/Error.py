from datetime import datetime


class Error:
    def __init__(self, linea, columna, ambito, mensaje, tipo=None):
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        self.ambito = ambito
        self.mensaje = mensaje
        self.fechahora = datetime.now()


if __name__ == '__main__':
    test = Error(1, 2, "global", "Error en la instruccion xD")
    print(f'{test}')
