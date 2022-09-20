import Simbolo.Arreglo
from Abstract.Instruccion import Instruccion
from Error.Error import Error
from Reporte.Reportes import lerrores
from Simbolo.Tipo import TIPO_DATO
from Recolector.Recolector import recolector
from Simbolo import Arreglo
from Simbolo import Vector

class Print(Instruccion):

    def __init__(self, fila, columna, lexpression):
        super().__init__(fila, columna)
        self.lexpresion = lexpression

    def ejecutar(self, entorno):
        tmpls = self.lexpresion.copy()
        tmplsaux = self.lexpresion.copy()
        if len(tmpls) > 1:
            tmpexpr = tmpls[0].ejecutar(entorno)
            #print(f'imp_eje: {tmpexpr.valor}')
            if "{}" in tmpexpr.valor or "{:?}" in tmpexpr.valor:
                del tmpls[0]
                tmpprint = tmpexpr.valor
                lstemp = []
                for expresion in tmpls:
                    valor = expresion.ejecutar(entorno)
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo) or isinstance(valor.valor, Simbolo.Vector.Vector):
                        lstemp.append(self.imprimirArregloVector(valor.valor))
                    else:
                        lstemp.append(valor.valor)
                try:
                    tmpls = tmplsaux
                    tmpprint = tmpexpr.valor.format(*lstemp)
                    recolector.append(str(tmpprint))
                    print(f'{tmpprint}')
                except:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'Error_Print: ¿¿¿Misma cantidad de expresiones y ' + "{}{:?} o tipo dato no coincide con {}{:?} ???"))
                    print(f'Error_Print: ¿¿¿Misma cantidad de expresiones y', "{}{:?} o tipo dato no coincide con {}{:?} ???")
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'imp_error: Falta', "{} {:?}"))
                print(f'imp_error: Falta', "{} {:?}")
        else:
            for expresion in tmpls:
                valor = expresion.ejecutar(entorno)
                if valor.tipo != TIPO_DATO.STRUCT:
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo) or isinstance(valor.valor, Simbolo.Vector.Vector):
                        recolector.append(self.imprimirArregloVector(valor.valor))
                        print(f"{self.imprimirArregloVector(valor.valor)}")
                    else:
                        recolector.append(valor.valor)
                        print(f"{valor.valor}")
                else:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre, 'Error al imprimir'))
                    print(f'Error al imprimir')

    def imprimirArregloVector(self, arreglo):
        tmp = "["
        auxCount = 0
        for x in arreglo.getAtributos():
            if isinstance(x.valor, Simbolo.Arreglo.Arreglo) or isinstance(x.valor, Simbolo.Vector.Vector):
                ret = self.imprimirArregloVector(x.valor)
                tmp += str(ret)
            else:
                if auxCount == arreglo.getTamanio() - 1:
                    tmp += str(x.valor)
                else:
                    tmp += str(x.valor) + ","
            auxCount += 1

        tmp += "]"
        return tmp

    def traducir(self, entorno, entornoC3D):
        for expresion in self.lexpresion:
            tmp_expre = expresion.traducir(entorno, entornoC3D)
            if tmp_expre.tipo == TIPO_DATO.RSTR or tmp_expre.tipo == TIPO_DATO.STRING:
                tamanio = len(tmp_expre.valor)
                p = entornoC3D.getS()
                h = entornoC3D.getH()

                t = entornoC3D.getT()
                entornoC3D.sumarT()
                entornoC3D.agregarTraduccion(f't{t} =  H;')
                entornoC3D.agregarTraduccion(f'stack[(int) P] = H;')
                entornoC3D.agregarTraduccion(f'P = P + 1;')
                entornoC3D.sumarS()
                for e in tmp_expre.valor:
                    h = entornoC3D.getH()
                    entornoC3D.agregarTraduccion(f'heap[(int) H] = {ord(e)};')
                    entornoC3D.agregarTraduccion(f'H = H + 1;')
                    entornoC3D.sumarH()
                    print(ord(e))
                entornoC3D.agregarTraduccion(f'heap[(int) H] = 10;')
                entornoC3D.agregarTraduccion(f'H = H + 1;')
                entornoC3D.agregarTraduccion(f'heap[(int) H] = -1;')
                entornoC3D.agregarTraduccion(f'H = H + 1;')
                entornoC3D.sumarH()
                entornoC3D.agregarTraduccion(f'stack[(int)P] = t{t};')
                entornoC3D.agregarTraduccion(f'imprimir();')
            elif tmp_expre.tipo == TIPO_DATO.INTEGER:
                print(f'print_c3d: {tmp_expre.tipo}')
                entornoC3D.agregarTraduccion(f'printf("%d",{str(tmp_expre.valor)});')
            elif tmp_expre.tipo == TIPO_DATO.FLOAT:
                print(f'print_c3d: {tmp_expre.tipo}')
                entornoC3D.agregarTraduccion(f'printf("%f",{str(tmp_expre.valor)});')
            #print(f'print_c3d: {tmp_expre.valor}')
        return None