class Traductor:
    def __init__(self):
        self.T = 3
        self.S = 0
        self.H = 0
        self.L = 2

        self.encabezado = """
#include <stdio.h>
float stack[10000];
float heap[10000];
float P;
float H;
"""
        self.valores_t = "float "
        self.cuerpo_nativas = """
void imprimir () {
	t0 = stack[(int)P];
	t1 = heap[(int)t0];
	t2 = - 1;
L1:
	if (t1 == t2) goto L2;
	printf("%c", (int)t1);
	t0 = t0 + 1;
	t1 = heap[(int)t0];
	goto L1;
L2:
	return;
}
"""
        self.cuerpo_inicio = """
int main(){
    P = 0;
    H = 0;
"""
        self.cuerpo_instrucciones = ""
        self.cuerpo_fin = "\n return 0; \n }"

    def agregarTraduccion(self, txt):
        self.cuerpo_instrucciones += txt + '\n'

    def obtenerTraduccion(self):
        self.generarT()
        unirTraduccion = self.encabezado + self.valores_t + self.cuerpo_nativas + self.cuerpo_inicio + self.cuerpo_instrucciones + self.cuerpo_fin
        return unirTraduccion

    def generarT(self):
        for i in range(0, self.T):
            if i == self.T - 1:
                self.valores_t += f't{i};'
            else:
                self.valores_t += f't{i}, '

    def sumarT(self):
        self.T += 1

    def getT(self):
        return self.T

    def getNuevoT(self):
        self.T += 1
        return self.T

    def sumarS(self):
        self.S += 1

    def getS(self):
        return self.S

    def sumarH(self):
        self.H += 1

    def getH(self):
        return self.H

    def getL(self):
        return self.L

    def sumarL(self):
        self.L += 1

    def getNuevoL(self):
        self.L += 1
        return self.L

    def setCadenaTraduccion(self, txt):
        tamanio = len(txt)
        p = self.getS()
        h = self.getH()

        t = self.getT()
        self.sumarT()
        self.agregarTraduccion(f't{t} =  H;')
        self.agregarTraduccion(f'stack[(int) P] = H;')
        self.agregarTraduccion(f'P = P + 1;')
        self.sumarS()
        for e in txt:
            h = self.getH()
            self.agregarTraduccion(f'heap[(int) H] = {ord(e)};')
            self.agregarTraduccion(f'H = H + 1;')
            self.sumarH()
            print(ord(e))
        self.agregarTraduccion(f'heap[(int) H] = -1;')
        self.agregarTraduccion(f'H = H + 1;')
        self.sumarH()

if __name__ == '__main__':
    print("------------------------")
