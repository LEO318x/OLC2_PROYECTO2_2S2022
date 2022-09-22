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


class C3D_Value:
    def __init__(self, value, temp, tipo, true_label, false_label):
        self.valor = value
        self.istemp = temp
        self.tipo = tipo
        self.true_label = true_label
        self.false_label = false_label
