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
            # print(f'imp_eje: {tmpexpr.valor}')
            if "{}" in tmpexpr.valor or "{:?}" in tmpexpr.valor:
                del tmpls[0]
                tmpprint = tmpexpr.valor
                lstemp = []
                for expresion in tmpls:
                    valor = expresion.ejecutar(entorno)
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo) or isinstance(valor.valor,
                                                                                      Simbolo.Vector.Vector):
                        lstemp.append(self.imprimirArregloVector(valor.valor))
                    else:
                        lstemp.append(valor.valor)
                try:
                    tmpls = tmplsaux
                    tmpprint = tmpexpr.valor.format(*lstemp)
                    recolector.append(str(tmpprint))
                    print(f'{tmpprint}')
                except:
                    lerrores.append(Error(self.fila, self.columna, entorno.nombre,
                                          f'Error_Print: ¿¿¿Misma cantidad de expresiones y ' + "{}{:?} o tipo dato no coincide con {}{:?} ???"))
                    print(f'Error_Print: ¿¿¿Misma cantidad de expresiones y',
                          "{}{:?} o tipo dato no coincide con {}{:?} ???")
            else:
                lerrores.append(Error(self.fila, self.columna, entorno.nombre, f'imp_error: Falta', "{} {:?}"))
                print(f'imp_error: Falta', "{} {:?}")
        else:
            for expresion in tmpls:
                valor = expresion.ejecutar(entorno)
                if valor.tipo != TIPO_DATO.STRUCT:
                    if isinstance(valor.valor, Simbolo.Arreglo.Arreglo) or isinstance(valor.valor,
                                                                                      Simbolo.Vector.Vector):
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

    def traducir(self, entorno, C3D):
        for expresion in self.lexpresion:
            tmp_expre = expresion.traducir(entorno, C3D)
            print(f'c3d_print: {tmp_expre} valor: {tmp_expre.valor} tipo: {tmp_expre.tipo}')
            C3D.comentario("Impresion")
            if tmp_expre.tipo == TIPO_DATO.BOOL:
                etiqueta = C3D.nuevo_label()
                etiqueta2 = C3D.nuevo_label()
                etiquetasal = C3D.nuevo_label()

                C3D.agregar_if(tmp_expre.valor, 1, "==", etiqueta)
                C3D.agregar_goto(etiqueta2)
                C3D.agregar_label(etiqueta)
                C3D.agregar_codigo("print_true_proc();")
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
                C3D.agregar_goto(etiquetasal)
                C3D.agregar_label(etiqueta2)
                C3D.agregar_codigo("print_false_proc();")
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
                C3D.agregar_label(etiquetasal)

            elif tmp_expre.tipo == TIPO_DATO.INTEGER:
                C3D.agregar_print("d", f'(int) {tmp_expre.valor}')
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
            elif tmp_expre.tipo == TIPO_DATO.FLOAT:
                C3D.agregar_print("f", f'{tmp_expre.valor}')
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
            elif tmp_expre.tipo == TIPO_DATO.STRING or tmp_expre.tipo == TIPO_DATO.RSTR:
                print(f'c3d_print_valor: {tmp_expre.valor} istemp: {tmp_expre.istemp}')
                C3D.agregar_codigo(f'stack[(int)P] = {tmp_expre.valor};')
                C3D.agregar_codigo(f'imprimir();')
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
            elif tmp_expre.tipo == TIPO_DATO.CHAR:
                C3D.agregar_print("c", f'(int) {tmp_expre.valor}')
                C3D.agregar_codigo(f'printf("%c", (int)10);')
                C3D.agregar_codigo(f'printf("%c", (int)13);')
