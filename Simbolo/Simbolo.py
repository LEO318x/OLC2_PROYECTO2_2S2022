

class Simbolo:
    def __init__(self, id, valor, tipo, mutable):
        self.id = id
        self.valor = valor
        self.tipo = tipo  # Tipo Retorno
        self.mutable = mutable

class C3D_Simbolo:
    def __init__(self, id, valor, tipo, posicion, tamanio):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.posicion = posicion
        self.tamanio = tamanio
