from Simbolo.Simbolo import Simbolo


class Vector:
    def __init__(self):
        self.valores = []
        self.tamanio_max = 0

    def getAtributo(self, index):
        return self.valores[index]

    def getAtributos(self):
        return self.valores

    def setAtributo(self, valor: Simbolo):
        self.tamanio_max += 1
        if len(self.valores) > self.tamanio_max:
            self.tamanio_max *= 2
        self.valores.append(valor)

    def setAtributoConIndex(self, index, valor: Simbolo):
        # print(f'vector: {index}')
        try:
            self.valores[index] = valor
        except:
            self.valores.append(valor)

    def setCapacidadMax(self, capacidad):
        self.tamanio_max = capacidad

    def remove(self, index):
        tmp = self.valores[index]
        del self.valores[index]
        return tmp

    def getTodo(self):
        return self.valores

    def getTamanio(self):
        return len(self.valores)

    def getTamanioMax(self):
        return self.tamanio_max

    def contains(self, valor):
        for content in self.valores:
            if content.valor == valor:
                return True
        return False

