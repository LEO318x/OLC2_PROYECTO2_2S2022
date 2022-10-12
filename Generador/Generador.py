class Generador:
    def __init__(self):
        # t14
        # L17
        self.temporal = 20
        self.label = 20
        self.codigo = []
        self.temp_list = []
        self.S = 0
        self.H = 0
        self.tmpbreak = None
        self.tmpcontinue = None
        self.lttemp = []
        self.lftemp = []

    def get_temporales(self):
        return self.temp_list

    def get_codigo(self):
        return self.codigo

    def sumar_stack(self):
        temp = self.S
        self.S += 1
        return temp

    def get_stack(self):
        return self.S

    def sumar_heap(self):
        temp = self.H
        self.H += 1
        return temp

    def get_heap(self):
        return self.H

    def nueva_temporal(self):
        temp = "t" + str(self.temporal)
        self.temporal += 1
        self.temp_list.append(temp)
        return temp

    def nuevo_label(self):
        temp = self.label
        self.label += 1
        return "L" + str(self.label)

    def agregar_label(self, label):
        self.codigo.append(label + ":")

    def agregar_if(self, izq, der, operador, label):
        self.codigo.append(f'if({str(izq)} {operador} {str(der)}) goto {label};')
        # self.codigo.append("if(" + str(izq) + " " + operador + " " + str(der) + ") goto " + label + ";")

    def agregar_goto(self, label):
        self.codigo.append("goto " + label + ";")

    def agregar_setstack(self, index, valor):
        self.codigo.append(f'stack[(int){index}] = {valor};')

    def agregar_getstack(self, target, valor):
        self.codigo.append(f'{target} = stack[(int) {valor}];')

    def agregar_break(self,  label):
        self.tmpbreak = label

    def obtener_break(self):
        return self.tmpbreak

    def limpiar_break(self):
        self.tmpbreak = None

    def agregar_continue(self,  label):
        self.tmpcontinue = label

    def obtener_continue(self):
        return self.tmpcontinue

    def limpiar_continue(self):
        self.tmpcontinue = None

    def agregar_lttemp(self, label):
        self.lttemp.append(label)

    def agregar_lftemp(self, label):
        self.lftemp.append(label)

    def agregar_expresion(self, target, izq, der, operador):
        self.codigo.append(f'{target} = {str(izq)} {operador} {str(der)};')
        # self.codigo.append(target + " = " + str(izq) + " " + operador + " " + str(der) + ";")

    def agregar_string(self, temp, txt):
        self.agregar_codigo(f'//Inicio string')
        # self.agregar_codigo(f'P = P + 1;')
        # self.agregar_codigo(f'stack[(int)P] = H;')
        self.agregar_codigo(f'{temp} = H;')
        for e in txt:
            self.agregar_codigo(f'heap[(int) H] = {ord(e)};')
            self.agregar_codigo(f'H = H + 1;')
        self.agregar_codigo(f'heap[(int) H] = -1;')
        self.agregar_codigo(f'H = H + 1;')
        self.agregar_codigo(f'//Fin string')


    def agregar_codigo(self, txt):
        self.codigo.append(txt)

    def construir_string(self, txt):
        for x in txt:
            pass

    def agregar_print(self, tipo_print, value):
        self.codigo.append(f'printf("%{tipo_print}", {value});')

    def comentario(self, txt):
        self.codigo.append(f'//|-->{txt}<--|')


    # def nativa_imprimir(self):
    #     txt = 'void imprimir(){\n'
    #     txt += 't0 = P + 1;\n'
    #     txt += 't1 = stack[(int)t0];\n'
    #     txt += 'L1:'
    #     txt += 't2 = heap[(int)t1];\n'
    #     txt += 'if(t2 != -1) goto L2;\n'
    #     txt += 'goto L3;\n'
    #     txt += 'L2:\n'
    #     txt += 'printf("%c",(int)t2);\n'
    #     txt += 't1 = t1 + 1;\n'
    #     txt += 'goto L1;\n'
    #     txt += 'L3:\n'
    #     txt += 'return;\n'
    #     txt += '}\n'
    #     return txt

    def nativa_imprimir(self):
        txt = "void imprimir(){\n"
        # txt += "t0 = stack[(int)P];\n"
        txt += "t1 = heap[(int)t0];\n"
        txt += "t2 = - 1;\n"
        txt += "L1:\n"
        txt += "if (t1 == t2) goto L2;\n"
        txt += "printf(\"%c\", (int)t1);\n"
        txt += "t0 = t0 + 1;\n"
        txt += "t1 = heap[(int)t0];\n"
        txt += "goto L1;\n"
        txt += "L2:\n"
        txt += "return;\n"
        txt += "}\n"
        return txt

    def concatenar_string(self):
        txt = "void concatenar_string(){\n"
        txt += "t8 = H;\n"
        txt += "t5 = t3;\n"
        txt += "t6 = t4;\n"
        txt += "L8:\n"
        txt += "t7 = heap[(int)t5];\n"
        txt += "if(t7 != -1) goto L6;\n"
        txt += "goto L7;\n"
        txt += "L6:\n"
        txt += "heap[(int)H] = t7;\n"
        txt += "H = H + 1;\n"
        txt += "t5 = t5 + 1;\n"
        txt += "goto L8;\n"
        txt += "L7:\n"
        txt += "t7 = heap[(int)t6];\n"
        txt += "if(t7 != -1) goto L9;\n"
        txt += "goto L10;\n"
        txt += "L9:\n"
        txt += "heap[(int)H] = t7;\n"
        txt += "H = H + 1;\n"
        txt += "t6 = t6 + 1;\n"
        txt += "goto L7;\n"
        txt += "L10:\n"
        txt += "heap[(int)H] = -1;\n"
        txt += "H = H + 1;\n"
        txt += "stack[(int)P] = t8;\n"
        txt += "}\n"
        return txt

    def print_true(self):
        txt = '\nvoid print_true_proc(){\n'
        txt += 'printf("%c",116);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",117);\n'
        txt += 'printf("%c",101);\n'
        txt += 'return;\n'
        txt += '}\n'
        return  txt

    def print_false(self):
        txt = '\nvoid print_false_proc(){\n'
        txt += 'printf("%c",102);\n'
        txt += 'printf("%c",97);\n'
        txt += 'printf("%c",108);\n'
        txt += 'printf("%c",115);\n'
        txt += 'printf("%c",101);\n'
        txt += 'return;\n'
        txt += '}\n'
        return txt

    def print_err_div(self):
        txt = "\nvoid print_err_div(){\n"
        txt += 'printf("%c",78);\n'
        txt += 'printf("%c",111);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",115);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",112);\n'
        txt += 'printf("%c",117);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",118);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",110);\n'
        txt += 'printf("%c",116);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",48);\n'
        txt += 'printf("%c",10);\n'
        txt += 'printf("%c",13);\n'
        txt += '}\n'
        return txt

    def print_err_arr(self):
        txt = '\nvoid print_err_arr(){\n'
        txt += 'printf("%c",73);\n'
        txt += 'printf("%c",110);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",99);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",108);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",97);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",103);\n'
        txt += 'printf("%c",108);\n'
        txt += 'printf("%c",111);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",102);\n'
        txt += 'printf("%c",117);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",114);\n'
        txt += 'printf("%c",97);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",100);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",108);\n'
        txt += 'printf("%c",111);\n'
        txt += 'printf("%c",115);\n'
        txt += 'printf("%c",32);\n'
        txt += 'printf("%c",108);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",109);\n'
        txt += 'printf("%c",105);\n'
        txt += 'printf("%c",116);\n'
        txt += 'printf("%c",101);\n'
        txt += 'printf("%c",115);\n'
        txt += 'printf("%c",10);\n'
        txt += 'printf("%c",13);\n'
        txt += '}\n'
        return txt

    def print_arr(self):
        # t9 tamanio
        # t10 expr_valor

        txt = '\nvoid print_arr(){\n'
        cont = 't11'
        valor = 't12'
        l1 = 'L11'
        l3 = 'L12'
        l2 = 'L13'
        t = 't13'

        v = 'L14'
        f = 'L15'
        s = 'L16'

        txt += f'printf("%c", (int) 91);\n'
        txt += f'{cont} = 0;'
        txt += f'{l1}:\n'
        txt += f'if ({cont} < t9) goto {l2};\n'
        txt += f'goto {l3};\n'
        txt += f'{l2}:\n'
        # instrucciones
        txt += f'{t} = t10;\n'
        txt += f'{t} = {t} + {cont};\n'
        txt += f'{t} = {t} + 1;\n'
        txt += f'{valor} = heap[(int) {t}];\n'
        txt += f'printf("%d", (int) {valor});\n'

        txt += f'if ({cont} == t9-1) goto {v};\n'
        txt += f'goto {f};\n'
        txt += f'{v}:\n'

        txt += f'goto {s};\n'
        txt += f'{f}:\n'
        txt += f'printf("%c", (int) 44);\n'
        txt += f'{s}:\n'

        txt += f'{cont} = {cont} + 1;\n'
        txt += f'goto {l1};\n'
        txt += f'{l3}:\n'
        txt += f'printf("%c", (int) 93);\n'
        txt += '}\n'
        return txt


    def generar_salida(self):
        salida = "#include <stdio.h>\n"
        salida += "float stack[100000];\n"
        salida += "float heap[100000];\n"
        salida += "float P;\n"
        salida += "float H;\n"
        salida += "float t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19"

        #salida += self.temp_list[0]
        #del self.temp_list[0]

        for element in self.temp_list:
            salida += ", "
            salida += str(element)

        salida += ";\n\n"
        salida += self.nativa_imprimir()
        salida += self.concatenar_string()
        salida += self.print_true()
        salida += self.print_false()
        salida += self.print_err_div()
        salida += self.print_err_arr()
        salida += self.print_arr()
        salida += "void main(){\n"
        salida += "P = 0;\n"
        salida += "H = 0;\n"


        for element in self.codigo:
            salida += str(element)
            salida += "\n"

        salida += "\nreturn;\n}\n"

        return salida
