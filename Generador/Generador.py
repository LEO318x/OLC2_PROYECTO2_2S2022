class Generador:
    def __init__(self):
        self.temporal = 3
        self.label = 3
        self.codigo = []
        self.temp_list = []
        self.S = 0
        self.H = 0

    def get_temporales(self):
        return self.temp_list

    def get_codigo(self):
        return self.codigo

    def nueva_temporal(self):
        temp = "t" + str(self.temporal)
        self.temporal += 1
        self.temp_list.append(temp)
        return temp

    def nueva_etiqueta(self):
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
        self.codigo.append(f'stack[{index}] = {valor};')

    def agregar_getstack(self, target, valor):
        self.codigo.append(f'{target} = stack[{valor}];')

    def agregar_expresion(self, target, izq, der, operador):
        self.codigo.append(f'{target} = {str(izq)} {operador} {str(der)};')
        # self.codigo.append(target + " = " + str(izq) + " " + operador + " " + str(der) + ";")

    def agregar_print(self, tipo_print, value):
        self.codigo.append(f'printf("%{tipo_print}", {value});')

    def comentario(self, txt):
        self.codigo.append(f'/***')
        self.codigo.append(f'* {txt}')
        self.codigo.append(f'***/')

    def nativa_imprimir(self):
        txt = "void imprimir(){\n"
        txt += "t0 = stack[(int)P];\n"
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

    def generar_salida(self):
        salida = "#include <stdio.h>\n"
        salida += "float stack[100000];\n"
        salida += "float heap[100000];\n"
        salida += "float P;\n"
        salida += "float H;\n"
        salida += "float t0, t1, t2"

        #salida += self.temp_list[0]
        #del self.temp_list[0]

        for element in self.temp_list:
            salida += ", "
            salida += str(element)

        salida += ";\n\n"
        salida += self.nativa_imprimir()
        salida += "void main(){\n"


        for element in self.codigo:
            salida += str(element)
            salida += "\n"

        salida += "\nreturn;\n}\n"

        return salida
