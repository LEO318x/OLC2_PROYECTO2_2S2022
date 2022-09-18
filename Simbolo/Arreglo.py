from Simbolo.Simbolo import Simbolo


class Arreglo:
    def __init__(self):
        self.valores = []

    def getAtributo(self, index):
        return self.valores[index]

    def setAtributo(self, valor: Simbolo):
        self.valores.append(valor)

    def setAtributoConIndex(self, index, valor: Simbolo):
        self.valores[index] = valor

    def getAtributos(self):
        return self.valores

    def getTamanio(self):
        return len(self.valores)


