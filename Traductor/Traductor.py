class Traductor:
    def __init__(self):
        self.cont_t = 3
        self.cont_s = 0
        self.cont_h = 0

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
        self.cuerpo_fin = "}"

    def agregarTraduccion(self, txt):
        self.cuerpo_instrucciones += txt + '\n'

    def obtenerTraduccion(self):
        self.generarT()
        unirTraduccion = self.encabezado + self.valores_t + self.cuerpo_nativas + self.cuerpo_inicio + self.cuerpo_instrucciones + self.cuerpo_fin
        return unirTraduccion

    def generarT(self):
        for i in range(0, self.cont_t):
            if i == self.cont_t - 1:
                self.valores_t += f't{i};'
            else:
                self.valores_t += f't{i}, '

    def sumarT(self):
        self.cont_t += 1

    def getT(self):
        return self.cont_t

    def sumarS(self):
        self.cont_s += 1

    def getS(self):
        return self.cont_s

    def sumarH(self):
        self.cont_h += 1

    def getH(self):
        return self.cont_h

if __name__ == '__main__':
    print("------------------------")
