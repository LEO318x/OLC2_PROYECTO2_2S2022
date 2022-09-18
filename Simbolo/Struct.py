from Abstract.Instruccion import Instruccion
from Abstract.Retorno import Retorno
from Simbolo.Tipo import TIPO_DATO


class Struct:
    def __init__(self, atributos=None):
        if atributos is None:
            atributos = dict()
        self.atributos = atributos

    def getAtributo(self, id):
        return self.atributos.get(id)

    def getLisAtributo(self):
        return self.atributos

    def setAtributo(self, attr):
        self.atributos.update(attr)

    def setAtributobyid(self, id, valor):
        self.atributos.update({id: valor})

